## active_stages(p_worker_id bigint, p_global boolean DEFAULT false, p_limit integer DEFAULT 64) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.active_stages(p_worker_id bigint, p_global boolean DEFAULT false, p_limit integer DEFAULT 64)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
begin
  perform control_center.active_project();

  return jsonb_build_object(
    'items',(
      select coalesce(jsonb_agg(jsonb_build_object(
        'stage_id',s.stage_id,
        'owner_worker_id',s.owner_worker_id,
        'kind',s.kind,
        'label',s.label,
        'mode',s.mode,
        'focus_id',s.focus_id,
        'claimable',s.claimable,
        'claimed_by_worker_id',s.claimed_by_worker_id,
        'operation_count',jsonb_array_length(s.operations),
        'created_at',s.created_at,
        'updated_at',s.updated_at,
        'expires_at',s.expires_at
      ) order by s.updated_at desc),'[]'::jsonb)
      from (
        select * from stages s
        where s.expires_at>now()
          and (
            p_global
            or s.owner_worker_id=p_worker_id
            or s.claimed_by_worker_id=p_worker_id
          )
        order by s.updated_at desc
        limit greatest(1,least(control_center.config_int('api.default_limit'),p_limit))
      ) s
    )
  );
end
$function$

```

## add_dependency_current(p_worker_id bigint, p_consumer_id text, p_premise_id text, p_metadata jsonb DEFAULT '{}'::jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.add_dependency_current(p_worker_id bigint, p_consumer_id text, p_premise_id text, p_metadata jsonb DEFAULT '{}'::jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_consumer text;
  v_premise text;
  v_math_version bigint;
  v_result jsonb;
begin
  perform control_center.active_project();
  v_consumer:=control_center.canonical_object_id(p_consumer_id);
  v_premise:=control_center.canonical_object_id(p_premise_id);
  select math_version into v_math_version
  from objects where id=v_premise and trashed_at is null for share;
  if v_math_version is null then raise exception 'canonical premise % not found',v_premise; end if;
  v_result:=control_center.add_edge(
    p_worker_id,v_consumer,v_premise,'depends_on',
    coalesce(p_metadata,'{}'::jsonb)
      ||jsonb_build_object('expected_math_version',v_math_version));
  return v_result||jsonb_build_object(
    'requested_consumer_id',p_consumer_id,
    'requested_premise_id',p_premise_id,
    'canonical_consumer_id',v_consumer,
    'canonical_premise_id',v_premise,
    'premise_math_version',v_math_version);
end
$function$

```

## add_edge(p_worker_id bigint, p_from_id text, p_to_id text, p_kind text, p_metadata jsonb DEFAULT '{}'::jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.add_edge(p_worker_id bigint, p_from_id text, p_to_id text, p_kind text, p_metadata jsonb DEFAULT '{}'::jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_kind text:=case when p_kind='proof' then 'depends_on' else p_kind end;
  v_from record; v_to record; v_priority integer; v_rev bigint; v_existing boolean; v_expected bigint;
  v_stage_commit boolean:=coalesce(current_setting((control_center.active_project()||'.verified_stage_commit'),true),'')='on';
begin
  perform control_center.active_project();
  if v_kind not in ('depends_on','references','consumes','informs','strengthens','supersedes','fence','interface','contradicts','bypassed_by','subsumed_by')
    then raise exception 'unsupported edge kind %',p_kind; end if;
  if p_from_id=p_to_id then raise exception 'self edge prohibited'; end if;

  select * into v_from from objects where id=p_from_id and trashed_at is null for update;
  select * into v_to from objects where id=p_to_id and trashed_at is null;
  if v_from.id is null or v_to.id is null then raise exception 'edge endpoint missing'; end if;

  if v_kind='depends_on' and not v_stage_commit then
    if not (coalesce(p_metadata,'{}'::jsonb) ? 'expected_math_version') then
      raise exception 'direct logical publication requires metadata.expected_math_version for premise %; use staged publication for a locked multi-object read set',p_to_id;
    end if;
    v_expected:=(p_metadata->>'expected_math_version')::bigint;
    if v_to.math_version<>v_expected then
      raise exception 'premise % changed: expected math_version %, current %',p_to_id,v_expected,v_to.math_version;
    end if;
  end if;
  if v_kind='depends_on' and logical_cycle_if_added(p_from_id,p_to_id) then
    raise exception 'logical dependency cycle rejected: % -> %',p_from_id,p_to_id;
  end if;

  select exists(select 1 from edges where from_id=p_from_id and to_id=p_to_id and kind=v_kind) into v_existing;
  insert into edges(from_id,to_id,kind,metadata)
  values(p_from_id,p_to_id,v_kind,coalesce(p_metadata,'{}'::jsonb)-'expected_math_version')
  on conflict(from_id,to_id,kind) do update set metadata=excluded.metadata;

  if not v_existing and v_kind='depends_on' then
    if v_from.audit_status='certified' and exists(select 1 from certificates where object_id=p_from_id) then
      update certificates
         set premise_manifest=premise_manifest(p_from_id),
             premise_signature=premise_signature(p_from_id)
       where object_id=p_from_id;
      perform refresh_support(p_from_id);
      perform refresh_dependents(array[p_from_id]);
    else
      update objects
         set support_status=case when mathematical_status='evidence' then 'evidence' else support_status end,
             updated_at=now(), version=version+1
       where id=p_from_id;
    end if;
  end if;

  if v_kind='supersedes'
     and v_from.audit_status='pending'
     and v_from.mathematical_status in ('proved','evidence') then
    update objects
       set audit_requested=true,
           audit_priority=greatest(audit_priority,control_center.config_int('scheduler.audit_destructive_priority')),
           metadata=coalesce(metadata,'{}'::jsonb)||jsonb_build_object(
             'audit_trigger_kind','destructive_effect',
             'audit_request_reason','supersession requires certification before retirement effect',
             'audit_request_recorded_at',now()
           ),
           updated_at=now()
     where id=p_from_id;
  end if;

  if v_kind='contradicts' then
    if v_from.mathematical_status in ('proved','evidence') and v_from.audit_status<>'failed' then
      perform control_center.flag_audit_anomaly(
        p_worker_id,p_from_id,'a contradiction edge was recorded involving this claim',control_center.config_int('scheduler.anomaly_priority')
      );
    end if;
    if v_to.mathematical_status in ('proved','evidence') and v_to.audit_status<>'failed' then
      perform control_center.flag_audit_anomaly(
        p_worker_id,p_to_id,'a contradiction edge was recorded involving this claim',control_center.config_int('scheduler.anomaly_priority')
      );
    end if;
  end if;

  v_rev:=record_change('add_edge',array[p_from_id,p_to_id],
    jsonb_build_object('kind',v_kind,'requested_kind',p_kind,'mathematical_dependency',v_kind='depends_on',
      'consumer_certification_preserved',v_kind='depends_on' and v_from.audit_status='certified'));
  return jsonb_build_object('from_id',p_from_id,'to_id',p_to_id,'kind',v_kind,
    'normalized_from',case when p_kind<>v_kind then p_kind else null end,'repository_revision',v_rev);
end
$function$

```

## adjust_need(p_worker_id bigint, p_need_key text, p_action text, p_priority integer DEFAULT NULL::integer, p_reason text DEFAULT NULL::text, p_target_ids text[] DEFAULT NULL::text[]) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.adjust_need(p_worker_id bigint, p_need_key text, p_action text, p_priority integer DEFAULT NULL::integer, p_reason text DEFAULT NULL::text, p_target_ids text[] DEFAULT NULL::text[])
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_action text:=lower(btrim(coalesce(p_action,'')));
  v_keys text[];
  v_key text;
  v_rev bigint;
begin
  PERFORM control_center.active_project();

  if v_action not in (
    'activate','resume','set_priority','set_offset','adjust_offset',
    'defer','promote','deactivate','skip','remove'
  ) then
    raise exception 'invalid need action %',v_action;
  end if;

  if v_action in ('set_priority','set_offset','adjust_offset') and p_priority is null then
    raise exception '% requires integer value in priority argument',v_action;
  end if;

  v_keys:=array[p_need_key];

  if exists (
    select 1 from unnest(v_keys) k
    where not exists (select 1 from needs n where n.need_key=k)
  ) then
    raise exception 'need % is not initialized',p_need_key;
  end if;

  if v_action in ('activate','resume') then
    update needs
    set active=true,
        generation=generation+1,
        priority=coalesce(p_priority,priority),
        reason=coalesce(nullif(btrim(p_reason),''),reason),
        target_ids=coalesce(p_target_ids,target_ids),
        requested_at=now(),updated_at=now(),last_outcome=null
    where need_key=any(v_keys);

  elsif v_action='set_priority' then
    if p_priority<control_center.config_int('priority.min') or p_priority>control_center.config_int('priority.max') then
      raise exception 'base priority must be between 0 and 100';
    end if;
    update needs
    set priority=p_priority,
        reason=coalesce(nullif(btrim(p_reason),''),reason),
        target_ids=coalesce(p_target_ids,target_ids),
        updated_at=now()
    where need_key=any(v_keys);

  elsif v_action='set_offset' then
    update needs
    set priority_offset=p_priority,
        reason=coalesce(nullif(btrim(p_reason),''),reason),
        updated_at=now()
    where need_key=any(v_keys);
    if p_priority<0 then
      foreach v_key in array v_keys loop
        perform control_center.suppress_need_for_worker(p_worker_id,v_key,coalesce(p_reason,'negative priority offset requested'));
      end loop;
    end if;

  elsif v_action='adjust_offset' then
    update needs
    set priority_offset=priority_offset+p_priority,
        reason=coalesce(nullif(btrim(p_reason),''),reason),
        updated_at=now()
    where need_key=any(v_keys);
    if p_priority<0 then
      foreach v_key in array v_keys loop
        perform control_center.suppress_need_for_worker(p_worker_id,v_key,coalesce(p_reason,'negative priority adjustment requested'));
      end loop;
    end if;

  elsif v_action='defer' then
    foreach v_key in array v_keys loop
      perform control_center.suppress_need_for_worker(p_worker_id,v_key,coalesce(p_reason,'worker deferred this need generation'));
    end loop;

  elsif v_action='promote' then
    update needs
    set priority_offset=priority_offset+control_center.config_int('scheduler.promote_offset'),
        reason=coalesce(nullif(btrim(p_reason),''),reason),
        updated_at=now()
    where need_key=any(v_keys);

  elsif v_action in ('deactivate','skip','remove') then
    update needs
    set active=false,
        priority=case when v_action='deactivate' then priority else 0 end,
        reason=case when v_action='remove' then null
                    else coalesce(nullif(btrim(p_reason),''),reason) end,
        target_ids=case when v_action='remove' then '{}'::text[] else target_ids end,
        signal_ids=case when v_action='remove' then '{}'::bigint[] else signal_ids end,
        requested_at=case when v_action='remove' then null else requested_at end,
        updated_at=now(),
        last_outcome=v_action,
        last_acknowledged_generation=generation
    where need_key=any(v_keys);
  end if;

  v_rev:=record_change(
    'coordination_adjust_need','{}'::text[],
    jsonb_build_object(
      'need_key',p_need_key,
      'action',v_action,
      'affected',to_jsonb(v_keys),
      'value',p_priority
    )
  );

  return jsonb_build_object(
    'action',v_action,
    'affected_need_keys',to_jsonb(v_keys),
    'needs',(
      select jsonb_agg(
        to_jsonb(n)||jsonb_build_object(
          'effective_priority',control_center.need_effective_priority(n.need_key)
        )
        order by n.need_key
      )
      from needs n where n.need_key=any(v_keys)
    ),
    'repository_revision',v_rev
  );
end
$function$

```

## ancestry(p_object_id text, p_max_depth integer DEFAULT NULL::integer, p_include_proofs boolean DEFAULT false) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.ancestry(p_object_id text, p_max_depth integer DEFAULT NULL::integer, p_include_proofs boolean DEFAULT false)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE
AS $function$
declare
  v_max_depth integer;
  v_items jsonb;
  v_count integer;
  v_truncated boolean;
begin
  perform control_center.active_project();

  if not exists (
    select 1 from objects
    where id=p_object_id and trashed_at is null
  ) then
    raise exception 'object % not found', p_object_id;
  end if;

  v_max_depth := greatest(
    0,
    least(
      control_center.config_int('subtree.max_depth'),
      coalesce(p_max_depth, control_center.config_int('subtree.simplified_default_depth'))
    )
  );

  with recursive chain as (
    select
      o.id,o.parent_id,o.title,o.statement,o.body,
      o.mathematical_status,o.audit_status,o.audit_requirement,
      o.support_status,o.support_reason,o.math_version,o.version,
      0::integer as depth
    from objects o
    where o.id=p_object_id and o.trashed_at is null

    union all

    select
      p.id,p.parent_id,p.title,p.statement,p.body,
      p.mathematical_status,p.audit_status,p.audit_requirement,
      p.support_status,p.support_reason,p.math_version,p.version,
      c.depth+1
    from chain c
    join objects p on p.id=c.parent_id and p.trashed_at is null
    where c.depth < v_max_depth
  )
  select
    coalesce(
      jsonb_agg(
        jsonb_strip_nulls(jsonb_build_object(
          'depth',depth,
          'id',id,
          'parent_id',parent_id,
          'title',title,
          'statement',statement,
          'body',case when p_include_proofs then body else null end,
          'mathematical_status',mathematical_status,
          'math_version',math_version,
          'object_version',version,
          'audit_status',audit_status,
          'audit_requirement',audit_requirement,
          'support_status',support_status,
          'support_reason',support_reason
        ))
        order by depth
      ),
      '[]'::jsonb
    ),
    count(*),
    coalesce(bool_or(
      depth=v_max_depth
      and parent_id is not null
      and exists (
        select 1 from objects p2
        where p2.id=chain.parent_id and p2.trashed_at is null
      )
    ),false)
  into v_items,v_count,v_truncated
  from chain;

  return jsonb_build_object(
    'object_id',p_object_id,
    'direction','target_to_root',
    'max_depth',v_max_depth,
    'include_proofs',p_include_proofs,
    'items',v_items,
    'node_count',v_count,
    'truncated',v_truncated,
    'repository_revision',(select revision from state where singleton)
  );
end
$function$

```

## announce(p_worker_id bigint, p_activity text, p_scope_id text DEFAULT NULL::text, p_message text DEFAULT ''::text, p_ttl_minutes integer DEFAULT NULL::integer, p_exclusive_key text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.announce(p_worker_id bigint, p_activity text, p_scope_id text DEFAULT NULL::text, p_message text DEFAULT ''::text, p_ttl_minutes integer DEFAULT NULL::integer, p_exclusive_key text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
DECLARE
  v_activity text:=CASE WHEN p_activity='coordination' THEN 'coordinate' ELSE p_activity END;
  v_cap integer;
  v_default_ttl integer;
  v_ttl integer;
  v_count integer;
  v_row record;
  v_scope_path text;
  v_conflict record;
  v_principal jsonb;
begin
  PERFORM control_center.active_project();
  
  v_principal:=require_math_principal(p_worker_id);
  PERFORM pg_advisory_xact_lock(hashtext((control_center.active_project()||'_presence')));
  PERFORM purge_ephemeral();

  IF v_activity NOT IN (
    'research','compose','restructure','rehearse','coordinate',
    'audit','methodology','literature','other'
  ) THEN
    RAISE EXCEPTION 'invalid presence activity %',p_activity;
  END IF;

  IF p_scope_id IS NOT NULL THEN
    SELECT tree_path INTO v_scope_path FROM objects
     WHERE id=p_scope_id AND trashed_at IS NULL;
    IF v_scope_path IS NULL THEN RAISE EXCEPTION 'presence scope object % not found',p_scope_id; END IF;
  END IF;

  IF p_exclusive_key IS NOT NULL AND p_scope_id IS NOT NULL
     AND v_activity IN ('compose','restructure') THEN
    SELECT p.* INTO v_conflict
    FROM presence p
    JOIN objects s ON s.id=p.scope_id
    WHERE p.expires_at>now()
      AND p.worker_id<>p_worker_id
      AND p.exclusive_key IS NOT NULL
      AND p.activity IN ('compose','restructure')
      AND (s.tree_path LIKE v_scope_path||'%' OR v_scope_path LIKE s.tree_path||'%')
    ORDER BY p.touched_at DESC
    LIMIT 1;

    IF v_conflict.presence_id IS NOT NULL THEN
      RAISE EXCEPTION 'overlapping exclusive reasoning activity already held until %',
        v_conflict.expires_at;
    END IF;
  END IF;

  SELECT max_presence,presence_ttl_minutes INTO v_cap,v_default_ttl
  FROM settings WHERE singleton;
  v_ttl:=greatest(control_center.config_int('ttl.minimum_minutes'),least(control_center.config_int('ttl.maximum_minutes'),coalesce(p_ttl_minutes,v_default_ttl)));

  IF p_exclusive_key IS NOT NULL THEN
    SELECT * INTO v_row FROM presence
     WHERE exclusive_key=p_exclusive_key AND expires_at>now()
     FOR UPDATE;
    IF v_row.presence_id IS NOT NULL AND v_row.worker_id<>p_worker_id THEN
      RAISE EXCEPTION 'exclusive activity % is already claimed by another worker until %',
        p_exclusive_key,v_row.expires_at;
    END IF;
  ELSE
    SELECT * INTO v_row FROM presence
     WHERE worker_id=p_worker_id AND activity=v_activity
       AND scope_id IS NOT DISTINCT FROM p_scope_id
       AND exclusive_key IS NULL AND expires_at>now()
     ORDER BY touched_at DESC LIMIT 1
     FOR UPDATE;
  END IF;

  IF v_row.presence_id IS NOT NULL THEN
    UPDATE presence
       SET message=coalesce(p_message,''),
           generation=generation+1,
           touched_at=now(),
           expires_at=now()+make_interval(mins=>v_ttl)
     WHERE presence_id=v_row.presence_id
     RETURNING * INTO v_row;
  ELSE
    SELECT count(*) INTO v_count FROM presence WHERE expires_at>now();
    IF v_count>=v_cap THEN RAISE EXCEPTION 'presence cap % reached',v_cap; END IF;

    INSERT INTO presence(
      worker_id,activity,scope_id,message,exclusive_key,generation,expires_at
    ) VALUES (
      p_worker_id,v_activity,p_scope_id,coalesce(p_message,''),
      nullif(p_exclusive_key,''),1,now()+make_interval(mins=>v_ttl)
    ) RETURNING * INTO v_row;
  END IF;

  RETURN to_jsonb(v_row)||jsonb_build_object(
    'normalized_activity',v_activity,
    'requested_activity',p_activity,
    'principal_kind',v_principal->>'principal_kind'
  );
END
$function$

```

## append_stage(p_worker_id bigint, p_stage_id bigint, p_operations jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.append_stage(p_worker_id bigint, p_stage_id bigint, p_operations jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_revision bigint;
begin
  PERFORM control_center.active_project();
  
  select stage_revision into v_revision
    from stages
   where stage_id=p_stage_id and owner_worker_id=p_worker_id
     and kind='batch' and expires_at>now();

  if v_revision is null then raise exception 'mutable batch stage not found'; end if;

  return control_center.append_stage_v2(
    p_worker_id,p_stage_id,v_revision,p_operations
  );
end
$function$

```

## append_stage_v2(p_worker_id bigint, p_stage_id bigint, p_expected_stage_revision bigint, p_operations jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.append_stage_v2(p_worker_id bigint, p_stage_id bigint, p_expected_stage_revision bigint, p_operations jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_stage record;
  v_more jsonb;
  v_combined jsonb;
  v_new_base jsonb;
  v_missing_base jsonb;
  v_new_reads jsonb;
  v_missing_reads jsonb;
  v_ttl integer;
begin
  PERFORM control_center.active_project();
  
  select * into v_stage from stages
   where stage_id=p_stage_id and owner_worker_id=p_worker_id
     and kind='batch' and expires_at>now()
   for update;

  if v_stage.stage_id is null then raise exception 'mutable batch stage not found'; end if;
  if v_stage.stage_revision<>p_expected_stage_revision then
    raise exception 'stage revision conflict: expected %, current %',
      p_expected_stage_revision,v_stage.stage_revision;
  end if;

  v_more:=normalize_stage_operations(p_operations);
  v_combined:=v_stage.operations||v_more;
  v_new_base:=stage_baselines(v_combined);
  v_new_reads:=stage_math_read_baselines(v_combined);

  select coalesce(jsonb_object_agg(e.key,e.value),'{}'::jsonb)
    into v_missing_base
    from jsonb_each(v_new_base) e
   where not (v_stage.baselines ? e.key);

  select coalesce(jsonb_object_agg(e.key,e.value),'{}'::jsonb)
    into v_missing_reads
    from jsonb_each(v_new_reads) e
   where not (v_stage.read_math_baselines ? e.key);

  select stage_ttl_minutes into v_ttl from settings where singleton;

  update stages
     set operations=v_combined,
         baselines=v_stage.baselines||v_missing_base,
         read_math_baselines=v_stage.read_math_baselines||v_missing_reads,
         stage_revision=stage_revision+1,
         verified_stage_revision=null,
         verified_digest=null,
         updated_at=now(),
         expires_at=now()+make_interval(mins=>v_ttl)
   where stage_id=p_stage_id
   returning * into v_stage;

  return to_jsonb(v_stage);
end
$function$

```

## assignment_request_status(p_worker_id bigint DEFAULT NULL::bigint) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.assignment_request_status(p_worker_id bigint DEFAULT NULL::bigint)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
begin
  perform control_center.active_project();

  return jsonb_build_object(
    'requests',coalesce((
      select jsonb_agg(jsonb_strip_nulls(jsonb_build_object(
        'request_id',r.request_id,
        'requested_by_worker_id',r.requested_by_worker_id,
        'target_worker_id',r.target_worker_id,
        'requested_mode',r.requested_mode,
        'task',r.task,
        'target_ids',r.target_ids,
        'priority',r.priority,
        'timing',r.timing,
        'scope',r.scope,
        'status',r.status,
        'attempts',r.attempts,
        'disposition',r.disposition,
        'requested_at',r.requested_at,
        'expires_at',r.expires_at,
        'consumed_at',r.consumed_at
      )) order by r.requested_at desc)
      from assignment_requests r
      where (
        p_worker_id is null
        or r.target_worker_id=p_worker_id
        or r.requested_by_worker_id=p_worker_id
      )
        and r.requested_at>now()-interval '7 days'
    ),'[]'::jsonb)
  );
end
$function$

```

## atlas(p_category text DEFAULT NULL::text, p_limit integer DEFAULT 24) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.atlas(p_category text DEFAULT NULL::text, p_limit integer DEFAULT 24)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare
  v_selector text := nullif(btrim(coalesce(p_category,'')),'');
  v_mode text;
  v_root_path text;
  v_entries jsonb;
  v_count integer;
  v_returned integer;
  v_limit integer;
begin
  perform control_center.active_project();

  if v_selector is null then
    v_mode := 'conceptual';
  elsif v_selector in ('all','objects','raw') then
    v_mode := 'raw_objects';
  elsif exists(select 1 from objects where id=v_selector and trashed_at is null) then
    v_mode := 'subtree';
    select tree_path into v_root_path from objects where id=v_selector and trashed_at is null;
  elsif v_selector in ('pending','obstructed') then
    v_mode := v_selector;
  else
    v_mode := 'classification';
  end if;

  if v_mode='raw_objects' then
    v_limit := greatest(1,least(control_center.config_int('api.large_limit'),coalesce(p_limit,24)));

    with
    ranked as materialized (
      select o.id,
             row_number() over (
               partition by o.parent_id
               order by
                 case
                   when o.parent_id is null
                    and o.id=(select grand_theorem_id from state where singleton)
                   then 0 else 1
                 end,
                 (o.atlas_height is null),
                 o.atlas_height desc nulls last,
                 o.position asc nulls last,
                 o.id
             ) as sibling_rank
      from objects o
      where o.trashed_at is null
    ),
    eligible as materialized (
      select
        o.*,
        (o.audit_status='pending') as is_pending,
        (
          o.support_status='blocked'
          or exists (
            select 1
            from edges fe
            join objects fo on fo.id=fe.from_id
            where fe.kind='fence'
              and fe.to_id=o.id
              and fo.trashed_at is null
              and fo.lifecycle_status='active'
              and fo.audit_status <> 'failed'
          )
        ) as is_obstructed
      from objects o
      where o.trashed_at is null
        and (
          o.lifecycle_status='active'
          or (
            o.lifecycle_status='retained'
            and exists (
              select 1
              from objects child
              where child.trashed_at is null
                and child.lifecycle_status='active'
                and child.tree_path like o.tree_path || '%'
                and child.id <> o.id
            )
          )
        )
        and o.simplified_statement is not null
        and o.audit_status <> 'failed'
        and o.object_type <> 'fence'
        and not exists (
          select 1
          from objects h
          where h.atlas_hidden
            and h.trashed_at is null
            and o.tree_path like h.tree_path || '%'
        )
        and not exists (
          select 1
          from edges se
          join objects replacement on replacement.id=se.from_id
          where se.kind='supersedes'
            and se.to_id=o.id
            and coalesce(se.metadata->>'supersession_state','effective')='effective'
            and replacement.trashed_at is null
            and replacement.lifecycle_status='active'
            and replacement.audit_status <> 'failed'
        )
    ),
    projected as materialized (
      select
        e.*,
        (
          select p.id
          from eligible p
          where p.id<>e.id
            and e.tree_path like p.tree_path || '%'
          order by char_length(p.tree_path) desc
          limit 1
        ) as atlas_parent_id,
        (
          select count(*)::integer
          from eligible p
          where p.id<>e.id
            and e.tree_path like p.tree_path || '%'
        ) as atlas_depth,
        (
          select string_agg(lpad(r.sibling_rank::text,10,'0'),'.' order by u.ord)
          from unnest(string_to_array(trim(both '/' from e.tree_path),'/'))
               with ordinality as u(segment,ord)
          join ranked r on r.id=u.segment
        ) as atlas_sort_key
      from eligible e
    ),
    limited as (
      select *
      from projected
      order by atlas_depth,atlas_sort_key,id
      limit v_limit
    )
    select
      coalesce((
        select jsonb_agg(
          jsonb_strip_nulls(jsonb_build_object(
            'id',l.id,
            'parent_id',l.parent_id,
            'atlas_parent_id',l.atlas_parent_id,
            'title',l.title,
            'summary',l.simplified_statement,
            'category',coalesce(l.research_level,l.object_type),
            'mathematical_status',l.mathematical_status,
            'audit_status',l.audit_status,
            'support_status',l.support_status,
            'pending',l.is_pending,
            'obstructed',l.is_obstructed,
            'atlas_height',l.atlas_height
          ))
          order by l.atlas_depth,l.atlas_sort_key,l.id
        )
        from limited l
      ),'[]'::jsonb),
      (select count(*)::integer from projected)
    into v_entries,v_count;

    v_returned:=jsonb_array_length(v_entries);

    return jsonb_build_object(
      'selector',v_selector,
      'selector_interpretation','raw_objects',
      'entries',v_entries,
      'matching_count',v_count,
      'returned_count',v_returned,
      'has_more',v_count>v_returned,
      'limit',v_limit,
      'repository_revision',(select revision from state where singleton),
      'note','Paginated raw eligible-object index. The complete conceptual research map is atlas() with no selector.'
    );
  end if;

  with
  ranked as materialized (
    select o.id,
           row_number() over (
             partition by o.parent_id
             order by
               case
                 when o.parent_id is null
                  and o.id=(select grand_theorem_id from state where singleton)
                 then 0 else 1
               end,
               (o.atlas_height is null),
               o.atlas_height desc nulls last,
               o.position asc nulls last,
               o.id
           ) as sibling_rank
    from objects o
    where o.trashed_at is null
  ),
  visible as materialized (
    select
      o.*,
      (o.audit_status='pending') as is_pending,
      (
        o.support_status='blocked'
        or exists (
          select 1
          from edges fe
          join objects fo on fo.id=fe.from_id
          where fe.kind='fence'
            and fe.to_id=o.id
            and fo.trashed_at is null
            and fo.lifecycle_status='active'
            and fo.audit_status <> 'failed'
        )
      ) as is_obstructed
    from objects o
    where o.trashed_at is null
      and (
        o.lifecycle_status='active'
        or (
          o.lifecycle_status='retained'
          and exists (
            select 1
            from objects child
            where child.trashed_at is null
              and child.lifecycle_status='active'
              and child.tree_path like o.tree_path || '%'
              and child.id <> o.id
          )
        )
      )
      and o.audit_status <> 'failed'
      and o.object_type <> 'fence'
      and not exists (
        select 1
        from objects h
        where h.atlas_hidden
          and h.trashed_at is null
          and o.tree_path like h.tree_path || '%'
      )
      and not exists (
        select 1
        from edges se
        join objects replacement on replacement.id=se.from_id
        where se.kind='supersedes'
          and se.to_id=o.id
          and coalesce(se.metadata->>'supersession_state','effective')='effective'
          and replacement.trashed_at is null
          and replacement.lifecycle_status='active'
          and replacement.audit_status <> 'failed'
      )
  ),
  containers as materialized (
    select
      v.*,
      (
        select p.id
        from visible p
        where p.semantic_container_text is not null
          and p.id<>v.id
          and v.tree_path like p.tree_path || '%'
        order by char_length(p.tree_path) desc
        limit 1
      ) as parent_container_id,
      (
        select count(*)::integer
        from visible p
        where p.semantic_container_text is not null
          and p.id<>v.id
          and v.tree_path like p.tree_path || '%'
      ) as container_depth,
      (
        select string_agg(lpad(r.sibling_rank::text,10,'0'),'.' order by u.ord)
        from unnest(string_to_array(trim(both '/' from v.tree_path),'/'))
             with ordinality as u(segment,ord)
        join ranked r on r.id=u.segment
      ) as atlas_sort_key
    from visible v
    where v.semantic_container_text is not null
  ),
  ownership as materialized (
    select
      v.*,
      (
        select c.id
        from containers c
        where v.tree_path like c.tree_path || '%'
        order by char_length(c.tree_path) desc
        limit 1
      ) as container_id
    from visible v
  ),
  stats as materialized (
    select
      c.*,
      (select count(*)::integer from ownership o where o.container_id=c.id) as member_count,
      (select count(*)::integer from visible d where d.tree_path like c.tree_path || '%') as subtree_object_count,
      (select count(*)::integer from containers d where d.id<>c.id and d.tree_path like c.tree_path || '%') as descendant_container_count,
      (select count(*)::integer from ownership o where o.container_id=c.id and o.is_pending) as pending_count,
      (select count(*)::integer from ownership o where o.container_id=c.id and o.is_obstructed) as obstructed_count,
      (select count(*)::integer from visible d where d.tree_path like c.tree_path || '%' and d.is_pending) as subtree_pending_count,
      (select count(*)::integer from visible d where d.tree_path like c.tree_path || '%' and d.is_obstructed) as subtree_obstructed_count,
      case when v_mode='subtree' then (
        select coalesce(jsonb_agg(o.id order by o.tree_path,o.id),'[]'::jsonb)
        from ownership o
        where o.container_id=c.id
      ) else null end as member_object_ids,
      (
        select bool_or(
          v_selector in (o.object_type,o.research_level,o.mathematical_status,o.audit_status,o.support_status)
        )
        from ownership o
        where o.container_id=c.id
      ) as direct_classification_match
    from containers c
  ),
  selected as materialized (
    select s.*
    from stats s
    where
      v_mode='conceptual'
      or (v_mode='subtree' and s.tree_path like v_root_path || '%')
      or (v_mode='pending' and s.pending_count>0)
      or (v_mode='obstructed' and s.obstructed_count>0)
      or (
        v_mode='classification'
        and (
          v_selector in (s.object_type,s.research_level,s.mathematical_status,s.audit_status,s.support_status)
          or coalesce(s.direct_classification_match,false)
        )
      )
  )
  select
    coalesce((
      select jsonb_agg(
        jsonb_strip_nulls(jsonb_build_object(
          'id',s.id,
          'parent_container_id',s.parent_container_id,
          'title',s.title,
          'summary',s.semantic_container_text,
          'category',coalesce(s.research_level,s.object_type),
          'mathematical_status',s.mathematical_status,
          'member_count',s.member_count,
          'subtree_object_count',s.subtree_object_count,
          'descendant_container_count',s.descendant_container_count,
          'pending_count',s.pending_count,
          'obstructed_count',s.obstructed_count,
          'subtree_pending_count',s.subtree_pending_count,
          'subtree_obstructed_count',s.subtree_obstructed_count,
          'atlas_height',s.atlas_height,
          'member_object_ids',s.member_object_ids
        ))
        order by s.atlas_sort_key,s.id
      )
      from selected s
    ),'[]'::jsonb),
    (select count(*)::integer from selected)
  into v_entries,v_count;

  v_returned:=jsonb_array_length(v_entries);

  return jsonb_build_object(
    'selector',v_selector,
    'selector_interpretation',v_mode,
    'entries',v_entries,
    'matching_count',v_count,
    'returned_count',v_returned,
    'has_more',false,
    'limit',null,
    'repository_revision',(select revision from state where singleton),
    'note','Complete conceptual Atlas derived from live semantic-container boundaries. atlas_height affects sibling prominence/order but never membership. member_count is direct nearest-container ownership; subtree counts include nested containers. A specific object/container selector additionally returns direct member_object_ids. Use atlas(''all'',limit) for the paginated raw object index.'
  );
end
$function$

```

## audit_packaging_issue(p_worker_id bigint, p_id text, p_note text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.audit_packaging_issue(p_worker_id bigint, p_id text, p_note text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_id text := control_center.canonical_object_id(p_id);
  v_rev bigint;
begin
  perform control_center.active_project();
  if nullif(btrim(coalesce(p_note,'')),'') is null then
    raise exception 'packaging issue requires a note';
  end if;
  if not exists(select 1 from objects where id=v_id and trashed_at is null) then
    raise exception 'object % not found',p_id;
  end if;

  update objects
     set metadata=jsonb_set(
       coalesce(metadata,'{}'::jsonb),
       '{audit_packaging_issues}',
       coalesce(metadata->'audit_packaging_issues','[]'::jsonb)
         || jsonb_build_array(jsonb_build_object(
              'worker_id',p_worker_id,
              'note',p_note,
              'recorded_at',now()
            )),
       true
     ),
     version=version+1,
     updated_at=now()
   where id=v_id;

  v_rev:=control_center.record_change(
    'audit_packaging_issue',
    array[v_id],
    jsonb_build_object('worker_id',p_worker_id,'note',p_note,'mathematical_failure',false)
  );

  return jsonb_build_object(
    'id',v_id,
    'recorded',true,
    'mathematical_failure',false,
    'repository_revision',v_rev
  );
end
$function$

```

## authoring_schema() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.authoring_schema()
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
begin
  perform control_center.active_project();
  return jsonb_build_object(
    'mathematical_status',jsonb_build_array('proved','conjecture','proposal','evidence'),
    'research_level',jsonb_build_array('working_unit','lemma','theorem','proof_level','abstraction'),
    'lifecycle_status',jsonb_build_array('active','retained','resolved','retired'),
    'attention',jsonb_build_array('focus','available','hidden'),
    'audit_status',jsonb_build_array('not_required','pending','certified','failed'),
    'reasoning_node_kind',jsonb_build_array('root','step','branch'),
    'presence_activity',jsonb_build_array(
      'research','restructure','rehearse','coordinate','audit','methodology','literature','other'
    ),
    'edge_kinds',jsonb_build_object(
      'logical',jsonb_build_array('proof','depends_on'),
      'research_influence',jsonb_build_array(
        'consumes','informs','references','interface','strengthens','supersedes','fence','contradicts'
      )
    ),
    'atlas_categories',jsonb_build_array(
      'toolkit','route','fence','counterexample','definition','literature','interface'
    ),
    'modes',jsonb_build_array(
      'research','audit','coordination','proof_rehearsal','literature_bridge'
    ),
    'note','Reasoning topology uses only root/branch/step. Archive content is navigable by exact read/subtree but excluded from ordinary search. Use help(topic) for compact task-specific authoring instructions.'
  );
end
$function$

```

## begin_audit(p_worker_id bigint, p_id text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.begin_audit(p_worker_id bigint, p_id text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_obj record;
  v_ttl integer;
  v_claim bigint;
  v_existing record;
begin
  PERFORM control_center.active_project();
  
  perform pg_advisory_xact_lock(hashtext((control_center.active_project()||'_assignment')));
  perform purge_ephemeral();

  select * into v_existing
  from claims c
  where c.worker_id=p_worker_id
    and c.mode='audit'
    and p_id=any(c.target_ids)
    and c.expires_at>now()
  order by c.created_at desc
  limit 1
  for update;

  if v_existing.claim_id is not null then
    select claim_ttl_minutes into v_ttl from settings where singleton;
    update claims
       set focus_id=p_id,
           renewed_at=now(),
           expires_at=now()+make_interval(mins=>v_ttl)
     where claim_id=v_existing.claim_id;
    perform sync_run_from_claim(p_worker_id,v_existing.claim_id);

    return build_packet(p_worker_id,v_existing.claim_id)
      ||jsonb_build_object(
        'audit_target_selected',p_id,
        'batch_preserved',true,
        'note','This target was already reserved inside the active audit batch. Open its exact audit bundle; do not create a new claim.'
      );
  end if;

  select * into v_obj from objects
   where id=p_id and trashed_at is null
     and audit_requested
     and (
       audit_status='pending'
       or (
         audit_status='certified'
         and support_status='stale'
         and support_reason='logical_premise_math_changed'
       )
     )
   for update;

  if v_obj.id is null then
    raise exception 'requested pending/stale audit target % not found',p_id;
  end if;
  if is_substantive_author(p_id,p_worker_id) then
    raise exception 'self-audit barrier: worker % is a substantive author of %',p_worker_id,p_id;
  end if;
  if exists(
    select 1 from claims c
     where c.mode='audit'
       and c.expires_at>now()
       and p_id=any(c.target_ids)
  ) then
    raise exception 'audit target % is already reserved by another active audit claim',p_id;
  end if;

  delete from claims where worker_id=p_worker_id;
  select claim_ttl_minutes into v_ttl from settings where singleton;

  insert into claims(
    worker_id,mode,purpose,target_ids,focus_id,exclusive_key,payload,expires_at
  ) values (
    p_worker_id,'audit','independent_audit',array[p_id],p_id,'audit:'||p_id,
    jsonb_build_object(
      'audit_batch',false,
      'audit_batch_size',1,
      'audit_requirement',v_obj.audit_requirement
    ),
    now()+make_interval(mins=>v_ttl)
  )
  returning claim_id into v_claim;

  perform sync_run_from_claim(p_worker_id,v_claim);
  return build_packet(p_worker_id,v_claim);
end
$function$

```

## begin_isolated_research(p_worker_id bigint) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.begin_isolated_research(p_worker_id bigint)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_project text:=control_center.active_project();
  v_claim_id bigint;
  v_mode text;
  v_payload jsonb;
begin
  perform control_center.require_math_principal(p_worker_id);

  execute format(
    'select claim_id,mode,payload from %I.claims
      where worker_id=$1 and expires_at>now()
      order by created_at desc limit 1 for update',
    v_project
  ) into v_claim_id,v_mode,v_payload using p_worker_id;

  if v_claim_id is null then raise exception 'worker % has no active assignment',p_worker_id; end if;
  if v_mode<>'isolated_research' then raise exception 'worker % is in mode %, not isolated_research',p_worker_id,v_mode; end if;
  if coalesce(v_payload->>'isolation_phase','ingestion')<>'ingestion' then
    raise exception 'isolated_research is already in phase %',coalesce(v_payload->>'isolation_phase','ingestion');
  end if;

  execute format(
    'update %I.claims set payload=coalesce(payload,''{}''::jsonb)||jsonb_build_object(
       ''isolation_phase'',''isolated'',''isolation_started_at'',now()) where claim_id=$1',
    v_project
  ) using v_claim_id;

  execute format(
    'update %I.runs set payload=coalesce(payload,''{}''::jsonb)||jsonb_build_object(
       ''isolation_phase'',''isolated'',''isolation_started_at'',now()),
       updated_at=now(),last_activity_at=now()
     where worker_id=$1 and status=''active''',
    v_project
  ) using p_worker_id;

  return jsonb_build_object(
    'worker_id',p_worker_id,'mode','isolated_research','phase','isolated',
    'database_access','closed',
    'instruction','Research independently from the ingested context. Do not call project/database RPCs. When ready to report accumulated results, call begin_isolated_submission(worker_id).'
  );
end
$function$

```

## begin_isolated_submission(p_worker_id bigint) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.begin_isolated_submission(p_worker_id bigint)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_project text:=control_center.active_project();
  v_claim_id bigint;
  v_mode text;
  v_payload jsonb;
begin
  perform control_center.require_math_principal(p_worker_id);

  execute format(
    'select claim_id,mode,payload from %I.claims
      where worker_id=$1 and expires_at>now()
      order by created_at desc limit 1 for update',
    v_project
  ) into v_claim_id,v_mode,v_payload using p_worker_id;

  if v_claim_id is null then raise exception 'worker % has no active assignment',p_worker_id; end if;
  if v_mode<>'isolated_research' then raise exception 'worker % is in mode %, not isolated_research',p_worker_id,v_mode; end if;
  if coalesce(v_payload->>'isolation_phase','ingestion')<>'isolated' then
    raise exception 'isolated_research submission can begin only from isolated phase; current phase %',coalesce(v_payload->>'isolation_phase','ingestion');
  end if;

  execute format(
    'update %I.claims set payload=coalesce(payload,''{}''::jsonb)||jsonb_build_object(
       ''isolation_phase'',''submission'',''submission_started_at'',now()) where claim_id=$1',
    v_project
  ) using v_claim_id;

  execute format(
    'update %I.runs set payload=coalesce(payload,''{}''::jsonb)||jsonb_build_object(
       ''isolation_phase'',''submission'',''submission_started_at'',now()),
       updated_at=now(),last_activity_at=now()
     where worker_id=$1 and status=''active''',
    v_project
  ) using p_worker_id;

  return jsonb_build_object(
    'worker_id',p_worker_id,'mode','isolated_research','phase','submission',
    'database_access','publication_boundary',
    'instruction','Publish the durable results accumulated during isolation, perform only submission-side hygiene needed to commit them, then close the assignment with continue(worker_id,outcome,details). Do not resume research in this phase.'
  );
end
$function$

```

## begin_proof_activity(p_worker_id bigint, p_activity text, p_scope_id text, p_message text DEFAULT ''::text, p_exclusive boolean DEFAULT true, p_ttl_minutes integer DEFAULT NULL::integer) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.begin_proof_activity(p_worker_id bigint, p_activity text, p_scope_id text, p_message text DEFAULT ''::text, p_exclusive boolean DEFAULT true, p_ttl_minutes integer DEFAULT NULL::integer)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$begin
  PERFORM control_center.active_project();
  
  RETURN (

  select control_center.begin_reasoning_activity(
    p_worker_id,p_activity,p_scope_id,p_message,p_exclusive,p_ttl_minutes
  )

  );
end$function$

```

## begin_reasoning_activity(p_worker_id bigint, p_activity text, p_scope_id text, p_message text DEFAULT ''::text, p_exclusive boolean DEFAULT true, p_ttl_minutes integer DEFAULT NULL::integer) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.begin_reasoning_activity(p_worker_id bigint, p_activity text, p_scope_id text, p_message text DEFAULT ''::text, p_exclusive boolean DEFAULT true, p_ttl_minutes integer DEFAULT NULL::integer)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
DECLARE
  v_key text;
BEGIN
  PERFORM control_center.active_project();

  IF p_activity NOT IN ('restructure','rehearse') THEN
    RAISE EXCEPTION 'reasoning activity must be restructure or rehearse';
  END IF;

  v_key:=case
    when p_activity='rehearse' or not p_exclusive then null
    else 'reasoning:restructure:'||p_scope_id
  end;

  RETURN control_center.announce(
    p_worker_id,p_activity,p_scope_id,p_message,p_ttl_minutes,v_key
  );
END
$function$

```

## begin_research_batch(p_worker_id bigint, p_note text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.begin_research_batch(p_worker_id bigint, p_note text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  b record;
  c record;
  v_generation bigint;
  v_operator_override boolean:=p_worker_id is null;
  v_old_workers bigint[]:='{}'::bigint[];
  v_retired_workers bigint[]:='{}'::bigint[];
  v_old_claims bigint[]:='{}'::bigint[];
  v_claim_count integer:=0;
  v_run_count integer:=0;
  v_presence_count integer:=0;
  v_audit_snapshot_count integer:=0;
  v_read_session_count integer:=0;
  v_read_receipt_count integer:=0;
  v_transition_receipt_count integer:=0;
  v_verified_released integer:=0;
  v_drafts_discarded integer:=0;
  v_other_stage_claims_released integer:=0;
  v_new_claim bigint;
  v_summary jsonb;
begin
  PERFORM control_center.active_project();

  perform pg_advisory_xact_lock(hashtext((control_center.active_project()||'_assignment')));
  perform purge_ephemeral();

  if not v_operator_override then
    select * into c
    from claims
    where worker_id=p_worker_id and expires_at>now()
    order by created_at desc
    limit 1;

    if c.claim_id is null then
      raise exception 'new research batch must be announced by an active freshly-started worker, or called with NULL worker_id as an operator/bootstrap override';
    end if;
  end if;

  select * into b
  from research_batch_state
  where singleton
  for update;

  -- Protect against the first few workers all being told the same operator
  -- message. A second announcement shortly after the first is a no-op.
  if b.started_at is not null
     and b.started_at>now()-control_center.config_interval('research_batch.duplicate_guard') then
    return jsonb_build_object(
      'started',false,
      'already_recent',true,
      'operator_override',v_operator_override,
      'batch',research_batch_capsule(),
      'current_claim_id',c.claim_id,
      'instruction',
      'A research batch was already opened recently. Keep the current assignment; do not reset the batch again.'
    );
  end if;

  select coalesce(array_agg(distinct worker_id),'{}'::bigint[])
    into v_old_workers
  from (
    select worker_id
    from claims
    where expires_at>now()
    union
    select worker_id
    from runs
    where status='active' and expires_at>now()
  ) q;

  select coalesce(array_agg(claim_id),'{}'::bigint[])
    into v_old_claims
  from claims
  where expires_at>now();

  if v_operator_override then
    v_retired_workers:=v_old_workers;
  else
    select coalesce(array_agg(w),'{}'::bigint[])
      into v_retired_workers
    from unnest(v_old_workers) x(w)
    where w<>p_worker_id;
  end if;

  v_generation:=b.generation+1;

  -- Preserve finished+verified publication work so a new worker can commit it.
  update stages s
     set claimable=true,
         claimed_by_worker_id=null,
         payload=s.payload||jsonb_build_object(
           'released_by_research_batch',v_generation,
           'released_at',now()
         ),
         updated_at=now()
   where s.kind='batch'
     and s.mode='research'
     and s.verified_stage_revision=s.stage_revision
     and s.verified_digest is not null
     and s.expires_at>now()
     and (
       s.owner_worker_id=any(v_old_workers)
       or s.claimed_by_worker_id=any(v_old_workers)
     );
  get diagnostics v_verified_released=row_count;

  -- Unverified batch/draft state is private scratch and is discarded at the batch boundary.
  delete from stages s
   where s.kind in ('batch','draft')
     and s.expires_at>now()
     and s.owner_worker_id=any(v_old_workers)
     and not (
       s.kind='batch'
       and s.mode='research'
       and s.verified_stage_revision=s.stage_revision
       and s.verified_digest is not null
     );
  get diagnostics v_drafts_discarded=row_count;

  -- Release any remaining transient stage claim held by the old wave.
  update stages s
     set claimed_by_worker_id=null,
         updated_at=now()
   where s.expires_at>now()
     and s.claimed_by_worker_id=any(v_old_workers);
  get diagnostics v_other_stage_claims_released=row_count;

  delete from audit_snapshots
   where claim_id=any(v_old_claims)
      or worker_id=any(v_old_workers);
  get diagnostics v_audit_snapshot_count=row_count;

  delete from read_sessions
   where owner_worker_id=any(v_old_workers);
  get diagnostics v_read_session_count=row_count;

  delete from read_receipts
   where worker_id=any(v_old_workers);
  get diagnostics v_read_receipt_count=row_count;

  delete from transition_receipts
   where worker_id=any(v_retired_workers);
  get diagnostics v_transition_receipt_count=row_count;

  delete from presence
   where worker_id=any(v_old_workers);
  get diagnostics v_presence_count=row_count;

  update runs
     set status='superseded',
         payload=payload||jsonb_build_object(
           'superseded_by_research_batch',v_generation,
           'superseded_at',now()
         ),
         updated_at=now()
   where worker_id=any(v_old_workers)
     and status='active';
  get diagnostics v_run_count=row_count;

  update runs
     set payload=coalesce(payload,'{}'::jsonb)-'_context_seen',
         updated_at=now()
   where worker_id=any(v_retired_workers);

  delete from claims
   where worker_id=any(v_old_workers);
  get diagnostics v_claim_count=row_count;

  v_summary:=jsonb_build_object(
    'released_claims',v_claim_count,
    'retired_workers',cardinality(v_retired_workers),
    'runs_superseded',v_run_count,
    'presence_cleared',v_presence_count,
    'audit_snapshots_cleared',v_audit_snapshot_count,
    'read_sessions_cleared',v_read_session_count,
    'read_receipts_cleared',v_read_receipt_count,
    'transition_receipts_cleared',v_transition_receipt_count,
    'verified_stages_made_claimable',v_verified_released,
    'unverified_scratch_stages_discarded',v_drafts_discarded,
    'other_stage_claims_released',v_other_stage_claims_released
  );

  update research_batch_state
     set generation=v_generation,
         started_at=now(),
         initiated_by_worker_id=p_worker_id,
         note=nullif(btrim(coalesce(p_note,'')),''),
         retired_worker_ids=v_retired_workers,
         last_summary=v_summary,
         updated_at=now()
   where singleton;

  -- Bootstrap/operator mode deliberately has no initiating worker to preserve.
  -- It drains the old wave and leaves the project ready for fresh startup().
  if v_operator_override then
    return jsonb_build_object(
      'research_batch_transition',jsonb_build_object(
        'started',true,
        'generation',v_generation,
        'summary',v_summary,
        'retired_worker_count',cardinality(v_retired_workers),
        'operator_override',true
      ),
      'batch',research_batch_capsule(),
      'instruction',
      'Research batch opened by operator/bootstrap override. Fresh workers may now call startup().'
    );
  end if;

  -- The announcing worker survives the cutover, but receives a fresh
  -- assignment computed from the newly released shared state.
  v_new_claim:=assign_worker(p_worker_id);

  update claims
     set payload=payload||jsonb_build_object(
       'research_batch_generation',v_generation,
       'research_batch_initiator',true
     )
   where claim_id=v_new_claim;

  perform sync_run_from_claim(p_worker_id,v_new_claim);

  return build_packet(p_worker_id,v_new_claim)
    ||jsonb_build_object(
      'research_batch_transition',jsonb_build_object(
        'started',true,
        'generation',v_generation,
        'summary',v_summary,
        'retired_worker_count',cardinality(v_retired_workers),
        'operator_override',false
      )
    );
end
$function$

```

## bind_composition(p_worker_id bigint, p_composition_id text, p_source_ids text[], p_note text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.bind_composition(p_worker_id bigint, p_composition_id text, p_source_ids text[], p_note text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
begin
  PERFORM control_center.active_project();
  
  raise exception 'composition binding requires the exact active lease token; use bind_composition_v2';
end
$function$

```

## bind_composition_v2(p_worker_id bigint, p_composition_id text, p_source_ids text[], p_presence_id bigint, p_presence_generation bigint, p_note text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.bind_composition_v2(p_worker_id bigint, p_composition_id text, p_source_ids text[], p_presence_id bigint, p_presence_generation bigint, p_note text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
DECLARE
  v_manifest jsonb;
  v_state jsonb;
  v_rev bigint;
BEGIN
  PERFORM control_center.active_project();
  PERFORM require_math_principal(p_worker_id);

  PERFORM 1
  FROM objects o
  JOIN reasoning_nodes rn ON rn.object_id=o.id
  WHERE o.id=p_composition_id AND o.trashed_at IS NULL
  FOR UPDATE OF o;

  IF NOT FOUND THEN
    RAISE EXCEPTION 'reasoning node % not found',p_composition_id;
  END IF;

  IF cardinality(coalesce(p_source_ids,'{}'::text[]))=0 THEN
    RAISE EXCEPTION 'recomposition manifest requires at least one source object';
  END IF;

  IF EXISTS(
    SELECT 1 FROM unnest(p_source_ids) s(id)
    WHERE NOT EXISTS(
      SELECT 1 FROM objects o WHERE o.id=s.id AND o.trashed_at IS NULL
    )
  ) THEN
    RAISE EXCEPTION 'recomposition source list contains missing objects';
  END IF;

  SELECT jsonb_agg(jsonb_build_object(
    'id',o.id,
    'math_version',o.math_version,
    'mathematical_status',o.mathematical_status,
    'support_status',o.support_status
  ) ORDER BY array_position(p_source_ids,o.id))
  INTO v_manifest
  FROM objects o
  WHERE o.id=ANY(p_source_ids) AND o.trashed_at IS NULL;

  UPDATE reasoning_nodes
     SET composition_manifest=v_manifest,
         composition_status='provisional',
         note=CASE WHEN p_note IS NULL THEN note ELSE p_note END,
         updated_at=now()
   WHERE object_id=p_composition_id;

  v_state:=composition_state(p_composition_id);

  UPDATE reasoning_nodes
     SET composition_status=v_state->>'status',updated_at=now()
   WHERE object_id=p_composition_id;

  UPDATE objects SET version=version+1,updated_at=now()
   WHERE id=p_composition_id;

  v_rev:=record_change(
    'bind_recomposition_manifest',
    merge_text_array(array[p_composition_id],p_source_ids,control_center.config_int('api.default_limit')),
    jsonb_build_object(
      'object_id',p_composition_id,
      'source_count',cardinality(p_source_ids),
      'recomposition_status',v_state->>'status',
      'legacy_presence_arguments_ignored',true
    )
  );

  RETURN jsonb_build_object(
    'composition_id',p_composition_id,
    'recomposition_id',p_composition_id,
    'manifest',v_manifest,
    'state',v_state,
    'repository_revision',v_rev
  );
END
$function$

```

## bind_replacement_composition_v2(p_worker_id bigint, p_composition_id text, p_source_ids text[], p_presence_id bigint, p_presence_generation bigint, p_note text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.bind_replacement_composition_v2(p_worker_id bigint, p_composition_id text, p_source_ids text[], p_presence_id bigint, p_presence_generation bigint, p_note text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
DECLARE
  v_result jsonb;
  v_all_certified boolean;
  v_requirement text;
  v_rev bigint;
begin
  PERFORM control_center.active_project();
  
  v_result := control_center.bind_replacement_composition_v2_base_recomposition_audit(
    p_worker_id,p_composition_id,p_source_ids,
    p_presence_id,p_presence_generation,p_note
  );

  SELECT count(*)=cardinality(coalesce(p_source_ids,'{}'::text[]))
         AND bool_and(
           o.audit_status='certified'
           AND o.support_status='supported'
           AND o.mathematical_status='proved'
         )
    INTO v_all_certified
  FROM objects o
  WHERE o.id=ANY(coalesce(p_source_ids,'{}'::text[]));

  UPDATE objects o
  SET audit_requirement=CASE
        WHEN coalesce(v_all_certified,false) THEN 'recomposition_equivalence'
        WHEN o.audit_requirement='recomposition_equivalence' THEN 'independent_check'
        ELSE o.audit_requirement
      END,
      audit_status='pending',
      audit_requested=true,
      audited_math_version=NULL,
      support_status='unchecked',
      support_reason=CASE
        WHEN coalesce(v_all_certified,false)
          THEN 'recomposition_equivalence_audit_pending'
        ELSE 'recomposition_full_mathematical_audit_pending'
      END,
      metadata=o.metadata||jsonb_build_object(
        'recomposition_audit',
        jsonb_build_object(
          'classified_at',now(),
          'source_package_fully_certified',coalesce(v_all_certified,false),
          'scope',CASE
            WHEN coalesce(v_all_certified,false)
              THEN 'equivalence'
            ELSE 'full_mathematical'
          END
        )
      ),
      version=o.version+1,
      updated_at=now()
  WHERE o.id=p_composition_id
  RETURNING audit_requirement INTO v_requirement;

  -- The replacement is deliberately pending audit/support at this point.
  -- Recompute the full logical-consumer closure after external depends_on edges
  -- have been rewired so direct consumers and their descendants enter the
  -- appropriate stale/provisional/blocked dependency-hold state.
  PERFORM invalidate_dependents(
    array[p_composition_id],
    'recomposition replacement pending verification'
  );

  v_rev := record_change(
    'classify_recomposition_audit',
    merge_text_array(array[p_composition_id],p_source_ids,control_center.config_int('api.default_limit')),
    jsonb_build_object(
      'composition_id',p_composition_id,
      'source_package_fully_certified',coalesce(v_all_certified,false),
      'audit_requirement',v_requirement
    )
  );

  RETURN v_result||jsonb_build_object(
    'recomposition_audit_requirement',v_requirement,
    'source_package_fully_certified',coalesce(v_all_certified,false),
    'repository_revision',v_rev
  );
END
$function$

```

## bind_replacement_composition_v2_base_recomposition_audit(p_worker_id bigint, p_composition_id text, p_source_ids text[], p_presence_id bigint, p_presence_generation bigint, p_note text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.bind_replacement_composition_v2_base_recomposition_audit(p_worker_id bigint, p_composition_id text, p_source_ids text[], p_presence_id bigint, p_presence_generation bigint, p_note text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
DECLARE
  v_source_ids text[] := coalesce(p_source_ids,'{}'::text[]);
  v_root_id text;
  v_root_parent text;
  v_terminal_id text;
  v_replacement_parent text;
  v_bind jsonb;
  v_rev bigint;
  v_rewired integer := 0;
  v_retired integer := 0;
  v_preserved_children integer := 0;
  v_roots integer := 0;
  v_terminals integer := 0;
  v_child record;
begin
  PERFORM control_center.active_project();
  
  IF cardinality(v_source_ids) < 2 THEN
    RAISE EXCEPTION 'replacement composition requires at least two source nodes';
  END IF;

  IF cardinality(v_source_ids) <> (
    SELECT count(DISTINCT x) FROM unnest(v_source_ids) x
  ) THEN
    RAISE EXCEPTION 'replacement source list contains duplicates';
  END IF;

  IF p_composition_id = ANY(v_source_ids) THEN
    RAISE EXCEPTION 'replacement composition cannot replace itself';
  END IF;

  IF EXISTS (
    SELECT 1
    FROM unnest(v_source_ids) s(id)
    LEFT JOIN objects o ON o.id=s.id
    WHERE o.id IS NULL OR o.trashed_at IS NOT NULL OR o.lifecycle_status<>'active'
  ) THEN
    RAISE EXCEPTION 'all replacement sources must be live active objects';
  END IF;

  IF EXISTS (
    SELECT 1
    FROM objects o
    WHERE o.id=ANY(v_source_ids)
      AND o.mathematical_status='conjecture'
  ) THEN
    RAISE EXCEPTION 'conjectural heads cannot be structurally replaced; preserve them as branch points';
  END IF;

  SELECT count(*),min(o.id)
    INTO v_roots,v_root_id
  FROM objects o
  WHERE o.id=ANY(v_source_ids)
    AND (o.parent_id IS NULL OR NOT (o.parent_id=ANY(v_source_ids)));

  IF v_roots<>1 THEN
    RAISE EXCEPTION 'replacement sources must form one rooted contiguous unary segment';
  END IF;

  SELECT count(*),min(o.id)
    INTO v_terminals,v_terminal_id
  FROM objects o
  WHERE o.id=ANY(v_source_ids)
    AND NOT EXISTS (
      SELECT 1
      FROM objects c
      WHERE c.parent_id=o.id
        AND c.trashed_at IS NULL
        AND c.id=ANY(v_source_ids)
    );

  IF v_terminals<>1 THEN
    RAISE EXCEPTION 'replacement sources must have exactly one terminal node';
  END IF;

  IF EXISTS (
    SELECT 1
    FROM objects o
    WHERE o.id=ANY(v_source_ids)
      AND o.id<>v_root_id
      AND NOT (o.parent_id=ANY(v_source_ids))
  ) THEN
    RAISE EXCEPTION 'replacement source IDs must form one contiguous parent-child segment';
  END IF;

  -- Every internal source node must be genuinely unary in the live document
  -- tree. The terminal source may have any number of children.
  IF EXISTS (
    SELECT 1
    FROM objects o
    WHERE o.id=ANY(v_source_ids)
      AND o.id<>v_terminal_id
      AND (
        (SELECT count(*)
         FROM objects c
         WHERE c.parent_id=o.id AND c.trashed_at IS NULL) <> 1
        OR NOT EXISTS (
          SELECT 1
          FROM objects c
          WHERE c.parent_id=o.id
            AND c.trashed_at IS NULL
            AND c.id=ANY(v_source_ids)
        )
      )
  ) THEN
    RAISE EXCEPTION 'replacement manifest must cover a true unary segment; only its terminal source may have children outside the manifest';
  END IF;

  SELECT parent_id INTO v_root_parent
  FROM objects
  WHERE id=v_root_id;

  SELECT parent_id INTO v_replacement_parent
  FROM objects
  WHERE id=p_composition_id AND trashed_at IS NULL;

  IF NOT FOUND THEN
    RAISE EXCEPTION 'replacement composition % is not live',p_composition_id;
  END IF;

  IF v_replacement_parent IS DISTINCT FROM v_root_parent THEN
    RAISE EXCEPTION 'replacement composition must be a sibling replacement under source root parent %',v_root_parent;
  END IF;

  IF EXISTS (
    SELECT 1
    FROM state s
    WHERE s.singleton AND (
      s.grand_theorem_id=ANY(v_source_ids)
      OR s.current_strategy_id=ANY(v_source_ids)
      OR s.proof_frontier_id=ANY(v_source_ids)
      OR s.current_bottleneck_id=ANY(v_source_ids)
      OR EXISTS (
        SELECT 1 FROM unnest(s.research_focus_ids) f
        WHERE f=ANY(v_source_ids)
      )
    )
  ) THEN
    RAISE EXCEPTION 'replacement sources contain live project-state/focus objects; rebind project state first';
  END IF;

  v_bind := control_center.bind_composition_v2(
    p_worker_id,p_composition_id,v_source_ids,
    p_presence_id,p_presence_generation,p_note
  );

  -- Controlled nonrecursive loop over only the terminal node's immediate
  -- children. move_object rewrites each child's entire subtree by a
  -- set-based tree_path prefix update; it does not recurse.
  FOR v_child IN
    SELECT id,version,position
    FROM objects
    WHERE parent_id=v_terminal_id
      AND trashed_at IS NULL
      AND NOT (id=ANY(v_source_ids))
    ORDER BY position,id
  LOOP
    PERFORM control_center.move_object(
      p_worker_id,
      v_child.id,
      v_child.version,
      p_composition_id,
      v_child.position
    );
    v_preserved_children := v_preserved_children + 1;
  END LOOP;

  -- Inherit every logical premise used by the replaced segment except
  -- internal source-to-source edges. This keeps the replacement sensitive
  -- to future premise changes after the source nodes are retired.
  INSERT INTO edges(from_id,to_id,kind,metadata)
  SELECT p_composition_id,q.to_id,'depends_on',
         coalesce(q.metadata,'{}'::jsonb)
         || jsonb_build_object(
              'inherited_by_recomposition',true,
              'inherited_from_sources',to_jsonb(q.source_ids)
            )
  FROM (
    SELECT e.to_id,
           (array_agg(coalesce(e.metadata,'{}'::jsonb) ORDER BY e.from_id))[1] AS metadata,
           array_agg(e.from_id ORDER BY e.from_id) AS source_ids
    FROM edges e
    WHERE e.kind='depends_on'
      AND e.from_id=ANY(v_source_ids)
      AND NOT (e.to_id=ANY(v_source_ids))
      AND e.to_id<>p_composition_id
    GROUP BY e.to_id
  ) q
  ON CONFLICT (from_id,to_id,kind)
  DO UPDATE SET metadata=edges.metadata
    || excluded.metadata
    || jsonb_build_object('inherited_by_recomposition',true);

  WITH ext AS (
    SELECT DISTINCT e.from_id
    FROM edges e
    JOIN objects c ON c.id=e.from_id AND c.trashed_at IS NULL
    WHERE e.kind='depends_on'
      AND e.to_id=ANY(v_source_ids)
      AND NOT (e.from_id=ANY(v_source_ids))
      AND e.from_id<>p_composition_id
  ), ins AS (
    INSERT INTO edges(from_id,to_id,kind,metadata)
    SELECT from_id,p_composition_id,'depends_on',
           jsonb_build_object('rewired_by_replacement',true)
    FROM ext
    ON CONFLICT (from_id,to_id,kind)
    DO UPDATE SET metadata=edges.metadata
      || jsonb_build_object('rewired_by_replacement',true)
    RETURNING 1
  )
  SELECT count(*) INTO v_rewired FROM ins;

  DELETE FROM edges e
  WHERE e.kind='depends_on'
    AND e.to_id=ANY(v_source_ids)
    AND NOT (e.from_id=ANY(v_source_ids))
    AND e.from_id<>p_composition_id;

  INSERT INTO edges(from_id,to_id,kind,metadata)
  SELECT p_composition_id,s.id,'supersedes',
         jsonb_build_object(
           'replacement_kind','equivalent_or_stronger',
           'structural_retirement',true
         )
  FROM unnest(v_source_ids) s(id)
  ON CONFLICT (from_id,to_id,kind)
  DO UPDATE SET metadata=edges.metadata || excluded.metadata;

  UPDATE objects o
     SET trashed_at=now(),
         metadata=coalesce(metadata,'{}'::jsonb)||jsonb_build_object(
           'structural_supersession_previous_attention',attention,
           'structural_supersession_retired_by',p_composition_id,
           'structural_supersession_retired_at',now()
         ),
         attention='hidden',
         updated_at=now(),
         version=version+1
  WHERE o.id=ANY(v_source_ids)
    AND o.trashed_at IS NULL;
  GET DIAGNOSTICS v_retired = ROW_COUNT;

  v_rev := record_change(
    'bind_replacement_composition',
    merge_text_array(array[p_composition_id],v_source_ids,control_center.config_int('api.default_limit')),
    jsonb_build_object(
      'composition_id',p_composition_id,
      'source_ids',to_jsonb(v_source_ids),
      'equivalent_or_stronger',true,
      'terminal_source_id',v_terminal_id,
      'terminal_children_preserved',v_preserved_children,
      'structurally_retired',v_retired,
      'external_consumers_rewired',v_rewired,
      'presence_id',p_presence_id,
      'presence_generation',p_presence_generation
    )
  );

  RETURN v_bind || jsonb_build_object(
    'replacement_semantics','equivalent_or_stronger',
    'terminal_source_id',v_terminal_id,
    'terminal_children_preserved',v_preserved_children,
    'structurally_retired',v_retired,
    'external_consumers_rewired',v_rewired,
    'repository_revision',v_rev
  );
END
$function$

```

## boot(p_worker_id bigint DEFAULT NULL::bigint) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.boot(p_worker_id bigint DEFAULT NULL::bigint)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_project text;
  v_worker bigint := coalesce(p_worker_id, control_center.allocate_identity('operational_id'));
  v_live_revision bigint;
  v_meta jsonb;
  v_artifact_revision bigint;
  v_body text;
  v_artifact_id bigint;
  v_artifact_path text;
  v_filename text;
  v_hashes jsonb;
  v_hash_revision bigint;
begin
  v_project := control_center.active_project();

  if p_worker_id is not null and control_center.worker_retired_by_current_batch(p_worker_id) then
    return jsonb_build_object(
      'wid',p_worker_id,
      'worker_id',p_worker_id,
      'architecture',v_project,
      'halt',true,
      'retired_by_new_research_batch',true,
      'message','This worker_id was retired by an explicit new-research-batch cutover. Start a new artifact worker with boot().'
    );
  end if;

  select revision into v_live_revision from state where singleton;
  select value into v_meta from control_center.configuration where key='artifact.latest';
  select body into v_body from control_center.policies where policy_key='artifact_bootstrap';

  v_artifact_revision := nullif(v_meta->'revisions'->>v_project,'')::bigint;
  v_artifact_id := nullif(v_meta->>'actions_artifact_id','')::bigint;
  v_artifact_path := v_meta->>'actions_artifact_path';
  v_filename := 'research_context_'||coalesce(v_artifact_revision::text,'unknown')||'.zip';

  select hashes,artifact_revision
    into v_hashes,v_hash_revision
  from control_center.artifact_context_snapshots
  where project_schema=v_project;

  if v_hashes is not null and v_hash_revision=v_artifact_revision then
    insert into control_center.artifact_boot_workers(
      project_schema,worker_id,artifact_revision,hashes,booted_at
    )
    values(v_project,v_worker,v_artifact_revision,v_hashes,now())
    on conflict(project_schema,worker_id) do update
      set artifact_revision=excluded.artifact_revision,
          hashes=excluded.hashes,
          booted_at=excluded.booted_at;
  end if;

  return jsonb_strip_nulls(jsonb_build_object(
    'wid',v_worker,
    'worker_id',v_worker,
    'architecture',v_project,
    'artifact_revision',v_artifact_revision,
    'live_repository_revision',v_live_revision,
    'updates_after_artifact_revision',greatest(0,v_live_revision-coalesce(v_artifact_revision,v_live_revision)),
    'artifact_distribution','github_actions',
    'artifact_name','research-context',
    'artifact_filename',v_filename,
    'artifact_id',v_artifact_id,
    'artifact_path',v_artifact_path,
    'artifact_hash_baseline_bound',(v_hashes is not null and v_hash_revision=v_artifact_revision),
    'library_search_filename',v_filename,
    'library_search_call',
      'await tools.files__search({intent:"nav",search_query:[{q:"'||v_filename||'",search_title_only:true}],scope:{surfaces:["library"]},top_k:5,result_format:"metadata_only"})',
    'artifact_download_call',
      'await tools.mcp__GitHub__download_workflow_artifact({repo_full_name:"SirCaptainCaleb/GN3_RESEARCH",artifact_id:'
      ||coalesce(v_artifact_id::text,'<missing>')
      ||',file_name:"'||v_filename||'"})',
    'repair_call_template',
      'select * from '||v_project||'.update_boot(''<latest artifact url or id>'');',
    'fallback_startup','select * from '||v_project||'.startup();',
    'bootstrap',v_body,
    'next_required_call',v_project||'.continue('||v_worker::text||')'
  ));
end
$function$

```

## brainstorm_recent(p_limit integer DEFAULT 2, p_revision_window bigint DEFAULT 200) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.brainstorm_recent(p_limit integer DEFAULT 2, p_revision_window bigint DEFAULT 200)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare
  v_current bigint; v_root_id text; v_objects jsonb;
begin
  perform control_center.active_project();
  select revision into v_current from state where singleton;
  select id into v_root_id from objects
  where trashed_at is null and lifecycle_status='active' and metadata->>'reserved_key'='brainstorms_root'
  order by created_at limit 1;

  if v_root_id is null then
    return jsonb_build_object('instruction','No canonical Brainstorms root exists for this project.',
      'permanent_root_id',null,'revision_window',p_revision_window,'objects','[]'::jsonb);
  end if;

  select coalesce(jsonb_agg(q.obj order by q.last_revision desc,q.updated_at desc,q.id),'[]'::jsonb)
  into v_objects
  from (
    select o.id,o.updated_at,coalesce(cr.last_revision,0) last_revision,
      jsonb_build_object(
        'id',o.id,'title',o.title,
        'proposal',left(coalesce(o.statement,''),control_center.config_int('text.compact_chars')),
        'last_revision',coalesce(cr.last_revision,0),
        'revisions_ago',greatest(0,v_current-coalesce(cr.last_revision,0))
      ) obj
    from objects o
    left join lateral (
      select max(c.revision) last_revision from changes c where o.id=any(c.object_ids)
    ) cr on true
    where o.parent_id=v_root_id and o.trashed_at is null and o.lifecycle_status='active'
      and o.mathematical_status in ('conjecture','proposal')
      and coalesce(cr.last_revision,0)>=greatest(0,v_current-greatest(0,p_revision_window))
    order by coalesce(cr.last_revision,0) desc,o.updated_at desc,o.id
    limit greatest(0,least(control_center.config_int('brainstorm.recent_limit'),p_limit))
  ) q;

  return jsonb_build_object(
    'instruction','Recent brainstorms are deliberate anti-frame-lock inputs. Before a substantial route commitment, inspect recent ideas as useful alternatives; pursuing any one is optional.',
    'permanent_root_id',v_root_id,'revision_window',p_revision_window,'objects',v_objects);
end $function$

```

## broadcast(p_worker_id bigint, p_message text, p_mode text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.broadcast(p_worker_id bigint, p_message text, p_mode text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
begin
  perform control_center.active_project();
  return control_center.broadcast_sticky(p_worker_id,p_message,0,p_mode);
end$function$

```

## broadcast_sticky(p_worker_id bigint, p_message text, p_ttl bigint DEFAULT 0, p_mode text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.broadcast_sticky(p_worker_id bigint, p_message text, p_ttl bigint DEFAULT 0, p_mode text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
  declare
    v_ttl bigint := coalesce(p_ttl,0);
    v_creation bigint;
    v_id bigint;
    v_gc_count integer:=0;
  begin
    perform control_center.active_project();

    if p_worker_id is null or not exists(select 1 from runs where worker_id=p_worker_id) then
      raise exception 'known worker_id is required';
    end if;
    if coalesce(length(p_message),0)=0 then
      raise exception 'broadcast message must be nonempty';
    end if;
    if v_ttl < 0 then
      raise exception 'broadcast TTL must be nonnegative';
    end if;

    select revision into v_creation from state where singleton;

    -- Lazy housekeeping: broadcast retention beyond delivery TTL is configuration-driven
    -- beyond its own delivery TTL, then is physically removed the next
    -- time a broadcast is created.
    delete from broadcasts
     where end_time + control_center.config_int('retention.broadcast_gc_revisions') < v_creation;
    get diagnostics v_gc_count=row_count;

    insert into broadcasts(message,mode_filter,ttl,creation_time,end_time,created_by_worker_id)
    values(p_message,p_mode,v_ttl,v_creation,v_creation+v_ttl,p_worker_id)
    returning id into v_id;

    return jsonb_strip_nulls(jsonb_build_object(
      'id',v_id,'creation_time',v_creation,'end_time',v_creation+v_ttl,
      'ttl',v_ttl,'mode_filter',p_mode,'active',true,
      'garbage_collected',v_gc_count
    ));
  end
  $function$

```

## cancel_assignment_request(p_worker_id bigint, p_request_id bigint) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.cancel_assignment_request(p_worker_id bigint, p_request_id bigint)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_count integer;
begin
  PERFORM control_center.active_project();

  update assignment_requests
  set status='cancelled',
      disposition=jsonb_build_object(
        'reason','cancelled',
        'cancelled_at',now()
      ),
      consumed_at=now(),
      updated_at=now()
  where request_id=p_request_id
    and status='pending'
    and (
      requested_by_worker_id is not distinct from p_worker_id
      or target_worker_id is not distinct from p_worker_id
    );

  get diagnostics v_count=row_count;

  return jsonb_build_object(
    'request_id',p_request_id,
    'cancelled',v_count=1
  );
end
$function$

```

## canonical_object_id(p_id text) -> text

```sql
CREATE OR REPLACE FUNCTION control_center.canonical_object_id(p_id text)
 RETURNS text
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare
  v_current text:=p_id;
  v_next text[];
  v_steps integer:=0;
  v_project text;
  v_alias text;
begin
  v_project:=control_center.active_project();
  if v_current is null or btrim(v_current)='' then
    raise exception 'object id is required';
  end if;

  if not exists(select 1 from objects where id=v_current and trashed_at is null)
     and to_regclass(format('%I.object_id_migration_map',v_project)) is not null then
    execute format(
      'select proposed_new_id from %I.object_id_migration_map
       where old_id=$1 and migration_status in (''migrated'',''reserved'',''frozen'',''proposed_reserved'',''proposed'')',
      v_project
    ) into v_alias using v_current;
    if v_alias is not null then v_current:=v_alias; end if;
  end if;

  loop
    if not exists(select 1 from objects where id=v_current and trashed_at is null) then
      raise exception 'object % not found',p_id;
    end if;
    v_next:=control_center.superseded_by(v_current);
    if cardinality(v_next)=0 then return v_current;
    elsif cardinality(v_next)>1 then
      raise exception 'object % has multiple live superseding objects: %',v_current,v_next;
    end if;
    v_current:=v_next[1];
    v_steps:=v_steps+1;
    if v_steps>control_center.config_int('supersession.max_chain_steps') then
      raise exception 'supersession chain exceeded configured maximum steps from %',p_id;
    end if;
  end loop;
end
$function$

```

## certify_object(p_worker_id bigint, p_id text, p_expected_version bigint, p_note text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.certify_object(p_worker_id bigint, p_id text, p_expected_version bigint, p_note text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$begin
  PERFORM control_center.active_project();
  
  RETURN (

  select control_center.certify_object_ex(
    p_worker_id,p_id,p_expected_version,p_note,'independent_check'
  )

  );
end$function$

```

## certify_object_ex(p_worker_id bigint, p_id text, p_expected_version bigint, p_note text DEFAULT NULL::text, p_verification_method text DEFAULT 'independent_check'::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.certify_object_ex(p_worker_id bigint, p_id text, p_expected_version bigint, p_note text DEFAULT NULL::text, p_verification_method text DEFAULT 'independent_check'::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_claim_id bigint;
  v_mode text;
begin
  PERFORM control_center.active_project();
  
  select c.claim_id into v_claim_id
    from claims c
   where c.worker_id=p_worker_id
     
     and p_id=any(c.target_ids)
     and c.expires_at>now()
   order by c.created_at desc limit 1;

  if v_claim_id is null then
    raise exception 'certification requires an active claim covering %',p_id;
  end if;

  select content_mode into v_mode
    from audit_snapshots
   where claim_id=v_claim_id
     and worker_id=p_worker_id
     and target_id=p_id
     and expires_at>now();

  if v_mode not in ('math','full') then
    raise exception 'certification requires a complete canonical math/full audit bundle for %',p_id;
  end if;

  return control_center.certify_object_ex_base_v4(
    p_worker_id,p_id,p_expected_version,p_note,p_verification_method
  );
end
$function$

```

## certify_object_ex_base_v4(p_worker_id bigint, p_id text, p_expected_version bigint, p_note text DEFAULT NULL::text, p_verification_method text DEFAULT 'independent_check'::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.certify_object_ex_base_v4(p_worker_id bigint, p_id text, p_expected_version bigint, p_note text DEFAULT NULL::text, p_verification_method text DEFAULT 'independent_check'::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
DECLARE
  v_requirement text;
  v_result jsonb;
  v_rev bigint;
begin
  PERFORM control_center.active_project();
  
  SELECT audit_requirement INTO v_requirement
  FROM objects
  WHERE id=p_id AND trashed_at IS NULL;

  IF v_requirement IS NULL THEN
    RAISE EXCEPTION 'object % not found',p_id;
  END IF;

  IF p_verification_method='recomposition_equivalence'
     AND v_requirement<>'recomposition_equivalence'
  THEN
    RAISE EXCEPTION
      'recomposition_equivalence verification is valid only for a recomposition_equivalence audit target';
  END IF;

  IF p_verification_method NOT IN (
    'recomposition_equivalence',
    'independent_check',
    'independent_reconstruction',
    'alternate_method',
    'computational_recheck'
  ) THEN
    RAISE EXCEPTION 'invalid verification method %',p_verification_method;
  END IF;

  v_result :=
    control_center.certify_object_ex_base_v4_legacy_recomposition_equivalence(
      p_worker_id,p_id,p_expected_version,p_note,
      CASE WHEN p_verification_method='recomposition_equivalence'
           THEN 'independent_check'
           ELSE p_verification_method
      END
    );

  IF p_verification_method='recomposition_equivalence' THEN
    UPDATE certificates
    SET verification_method='recomposition_equivalence',
        note=coalesce(note,'')
          || CASE WHEN coalesce(note,'')='' THEN '' ELSE E'\n' END
          || 'Certified by recomposition-equivalence audit against the retired certified source package.'
    WHERE object_id=p_id;

    v_rev := record_change(
      'certify_recomposition_equivalence',
      array[p_id],
      jsonb_build_object(
        'worker_id',p_worker_id,
        'verification_method','recomposition_equivalence'
      )
    );

    v_result := v_result || jsonb_build_object(
      'verification_method','recomposition_equivalence',
      'certificate',(SELECT to_jsonb(c)
                     FROM certificates c
                     WHERE c.object_id=p_id),
      'repository_revision',v_rev
    );
  END IF;

  RETURN v_result;
END
$function$

```

## certify_object_ex_base_v4_legacy_recomposition_equivalence(p_worker_id bigint, p_id text, p_expected_version bigint, p_note text DEFAULT NULL::text, p_verification_method text DEFAULT 'independent_check'::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.certify_object_ex_base_v4_legacy_recomposition_equivalence(p_worker_id bigint, p_id text, p_expected_version bigint, p_note text DEFAULT NULL::text, p_verification_method text DEFAULT 'independent_check'::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_row record;
  v_rev bigint;
  v_claim record;
  v_snap record;
  v_snapshot jsonb;
  v_manifest jsonb;
  v_signature jsonb;
  v_support jsonb;
  v_lock_ids text[];
begin
  PERFORM control_center.active_project();
  
  if p_verification_method not in (
    'independent_check','independent_reconstruction',
    'alternate_method','computational_recheck'
  ) then
    raise exception 'invalid verification method %',p_verification_method;
  end if;

  select * into v_claim from claims c
   where c.worker_id=p_worker_id
     
     and p_id=any(c.target_ids)
     and c.expires_at>now()
   order by c.created_at desc limit 1
   for update;

  if v_claim.claim_id is null then
    raise exception 'certification requires an active claim covering %',p_id;
  end if;

  select * into v_snap
    from audit_snapshots
   where claim_id=v_claim.claim_id
     and worker_id=p_worker_id
     and target_id=p_id
     and expires_at>now()
   for update;

  if v_snap.claim_id is null then
    raise exception 'certification requires a current audit snapshot for %',p_id;
  end if;

  select coalesce(array_agg(distinct id order by id),'{}'::text[])
    into v_lock_ids
  from (
    select p_id as id
    union
    select key from jsonb_each(v_snap.watched_math_versions)
  ) q;

  perform o.id
    from objects o
   where o.id=any(v_lock_ids)
   order by o.id
   for update;

  v_snapshot:=audit_snapshot_state(v_claim.claim_id,p_id);
  if not coalesce((v_snapshot->>'current')::boolean,false) then
    raise exception 'certification requires a current locked audit snapshot for %: %',
      p_id,coalesce(v_snapshot->>'reason',(v_snapshot->'conflicts')::text);
  end if;

  select * into v_row from objects
   where id=p_id and trashed_at is null;

  if v_row.id is null then raise exception 'object % not found',p_id; end if;
  if v_row.version<>p_expected_version then
    raise exception 'version conflict on %: expected %, current %',
      p_id,p_expected_version,v_row.version;
  end if;
  if v_row.mathematical_status not in ('proved','evidence') then
    raise exception 'object % is not certifiable mathematical content',p_id;
  end if;
  if v_row.audit_status<>'pending' then
    raise exception 'object % audit_status is %, expected pending',p_id,v_row.audit_status;
  end if;
  if is_substantive_author(p_id,p_worker_id) then
    raise exception 'self-certification barrier: worker % is a substantive author of %',
      p_worker_id,p_id;
  end if;

  if v_row.audit_requirement='independent_reconstruction'
     and p_verification_method not in ('independent_reconstruction','alternate_method') then
    raise exception 'object % requires independent reconstruction or alternate-method verification',p_id;
  end if;

  if v_row.audit_requirement='alternate_method'
     and p_verification_method<>'alternate_method' then
    raise exception 'object % requires alternate-method verification',p_id;
  end if;

  v_manifest:=premise_manifest(p_id);
  v_signature:=premise_signature(p_id);

  insert into certificates(
    object_id,math_version,verifier_worker_id,verification_method,
    premise_manifest,premise_signature,checked_at,note
  ) values (
    p_id,v_row.math_version,p_worker_id,p_verification_method,
    v_manifest,v_signature,now(),p_note
  )
  on conflict(object_id) do update set
    math_version=excluded.math_version,
    verifier_worker_id=excluded.verifier_worker_id,
    verification_method=excluded.verification_method,
    premise_manifest=excluded.premise_manifest,
    premise_signature=excluded.premise_signature,
    checked_at=excluded.checked_at,
    note=excluded.note;

  update objects
     set audit_status='certified',
         audit_requested=false,
         audited_math_version=math_version,
         version=version+1,
         updated_at=now()
   where id=p_id
   returning * into v_row;

  v_support:=refresh_support(p_id);
  perform refresh_dependents(array[p_id]);

  v_rev:=record_change(
    'certify',array[p_id],
    jsonb_build_object(
      'worker_id',p_worker_id,
      'math_version',v_row.math_version,
      'verification_method',p_verification_method,
      'support_status',v_support->>'status',
      'audit_snapshot_claim_id',v_claim.claim_id,
      'audit_snapshot_target_id',p_id,
      'locked_read_set',v_lock_ids,
      'note',p_note
    )
  );


  return to_jsonb((select o from objects o where o.id=p_id))
    ||jsonb_build_object(
      'support',v_support,
      'audit_snapshot',v_snapshot,
      'certificate',(select to_jsonb(c) from certificates c where c.object_id=p_id),
      'repository_revision',v_rev
    );
end
$function$

```

## certify_object_guarded(p_worker_id bigint, p_id text, p_expected_object_version bigint, p_expected_math_version bigint, p_note text DEFAULT NULL::text, p_verification_method text DEFAULT 'independent_check'::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.certify_object_guarded(p_worker_id bigint, p_id text, p_expected_object_version bigint, p_expected_math_version bigint, p_note text DEFAULT NULL::text, p_verification_method text DEFAULT 'independent_check'::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  o record;
begin
  PERFORM control_center.active_project();
  
  select * into o
  from objects
  where id=p_id and trashed_at is null;

  if o.id is null then raise exception 'object % not found',p_id; end if;
  if o.version<>p_expected_object_version then
    raise exception 'object-version conflict on %: expected %, current %',
      p_id,p_expected_object_version,o.version;
  end if;
  if o.math_version<>p_expected_math_version then
    raise exception 'math-version conflict on %: expected %, current %',
      p_id,p_expected_math_version,o.math_version;
  end if;

  return control_center.certify_object_ex(
    p_worker_id,p_id,p_expected_object_version,p_note,p_verification_method
  );
end
$function$

```

## changes_since(p_since_revision bigint, p_after_revision bigint DEFAULT NULL::bigint, p_limit integer DEFAULT 100) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.changes_since(p_since_revision bigint, p_after_revision bigint DEFAULT NULL::bigint, p_limit integer DEFAULT 100)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$begin
  PERFORM control_center.active_project();
  
  RETURN (

  select change_page(
    greatest(p_since_revision,coalesce(p_after_revision,p_since_revision)),
    p_limit
  )||jsonb_build_object('requested_since_revision',p_since_revision)

  );
end$function$

```

## claim_verified_stage(p_worker_id bigint, p_stage_id bigint) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.claim_verified_stage(p_worker_id bigint, p_stage_id bigint)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
DECLARE
  s record;
  v_report jsonb;
BEGIN
  PERFORM control_center.active_project();

  IF NOT touch_worker_claim(p_worker_id) THEN
    RAISE EXCEPTION 'recovering a verified stage requires an active worker claim';
  END IF;

  SELECT * INTO s
  FROM stages
  WHERE stage_id=p_stage_id
    AND kind='batch'
    AND mode='research'
    AND expires_at>now()
  FOR UPDATE;

  IF s.stage_id IS NULL THEN
    RAISE EXCEPTION 'recoverable verified research stage not found';
  END IF;

  IF s.owner_worker_id=p_worker_id THEN
    RETURN to_jsonb(s)||jsonb_build_object('claimed',true,'already_owner',true);
  END IF;

  IF EXISTS(
    SELECT 1 FROM claims x
    WHERE x.worker_id=s.owner_worker_id AND x.expires_at>now()
  ) THEN
    RAISE EXCEPTION 'original stage owner still has an active lease';
  END IF;

  IF s.claimed_by_worker_id IS NOT NULL AND s.claimed_by_worker_id<>p_worker_id THEN
    RAISE EXCEPTION 'verified stage is already claimed by another worker';
  END IF;

  IF s.verified_stage_revision IS DISTINCT FROM s.stage_revision
     OR s.verified_digest IS NULL
     OR s.verified_digest IS DISTINCT FROM stage_digest(
       s.operations,s.baselines,s.read_math_baselines,s.stage_revision
     ) THEN
    RAISE EXCEPTION 'stage is not verified at its current revision';
  END IF;

  IF EXISTS(
    SELECT 1 FROM jsonb_array_elements(s.operations) op
    WHERE op->>'op' IN ('certify_object','fail_object','set_project_state','resolve_signal')
  ) THEN
    RAISE EXCEPTION 'this verified stage contains non-transferable audit/coordination operations';
  END IF;

  UPDATE stages
  SET claimed_by_worker_id=p_worker_id,
      claimable=false,
      payload=payload||jsonb_build_object(
        'recovery_claimed_by',p_worker_id,
        'recovery_claimed_at',now(),
        'original_owner_worker_id',s.owner_worker_id
      ),
      updated_at=now()
  WHERE stage_id=p_stage_id;

  v_report:=control_center.verify_stage(p_worker_id,p_stage_id);
  IF NOT coalesce((v_report->>'valid')::boolean,false) THEN
    RAISE EXCEPTION 'verified stage became stale before recovery: %',v_report;
  END IF;

  RETURN to_jsonb((SELECT x FROM stages x WHERE x.stage_id=p_stage_id))
    ||jsonb_build_object(
      'claimed',true,
      'original_owner_worker_id',s.owner_worker_id,
      'verification',v_report
    );
END
$function$

```

## close_read(p_worker_id bigint, p_session_id bigint) -> boolean

```sql
CREATE OR REPLACE FUNCTION control_center.close_read(p_worker_id bigint, p_session_id bigint)
 RETURNS boolean
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_count integer;
begin
  PERFORM control_center.active_project();
  
  delete from read_sessions
   where session_id=p_session_id and owner_worker_id=p_worker_id;
  get diagnostics v_count=row_count;
  return v_count>0;
end
$function$

```

## commit_stage(p_worker_id bigint, p_stage_id bigint) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.commit_stage(p_worker_id bigint, p_stage_id bigint)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
DECLARE
  v_ids text[] := '{}'::text[];
  v_result jsonb;
  v_advisories jsonb;
begin
  PERFORM control_center.active_project();
  
  SELECT coalesce(array_agg(op->>'id'),'{}'::text[])
  INTO v_ids
  FROM stages s
  CROSS JOIN LATERAL jsonb_array_elements(coalesce(s.operations,'[]'::jsonb)) op
  WHERE s.stage_id=p_stage_id
    AND op->>'op'='create_object'
    AND nullif(op->>'id','') IS NOT NULL;

  v_result:=control_center.commit_stage_core(p_worker_id,p_stage_id);

  SELECT coalesce(jsonb_agg(x.adv),'[]'::jsonb)
  INTO v_advisories
  FROM (
    SELECT proposer_hygiene_advisory(u.id) AS adv
    FROM unnest(v_ids) u(id)
  ) x
  WHERE x.adv IS NOT NULL;

  IF jsonb_array_length(v_advisories)=0 THEN
    RETURN v_result;
  END IF;

  RETURN v_result||jsonb_build_object('reasoning_hygiene',v_advisories);
END
$function$

```

## commit_stage_base(p_worker_id bigint, p_stage_id bigint) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.commit_stage_base(p_worker_id bigint, p_stage_id bigint)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_stage record;
  v_pair record;
  v_current bigint;
  v_op jsonb;
  v_type text;
  v_result jsonb;
  v_results jsonb := '[]'::jsonb;
  v_id text;
  v_state_rev bigint;
begin
  PERFORM control_center.active_project();
  
  select * into v_stage
    from stages
   where stage_id=p_stage_id
     and (owner_worker_id=p_worker_id or claimed_by_worker_id=p_worker_id)
     and kind='batch'
     and expires_at>now()
   for update;

  if v_stage.stage_id is null then
    raise exception 'commit-ready stage not found';
  end if;

  for v_pair in select key,value from jsonb_each(v_stage.baselines)
  loop
    if v_pair.key='__state_revision' then
      select revision into v_state_rev
        from state where singleton;

      if v_state_rev<>(v_pair.value#>>'{}')::bigint then
        raise exception
          'staged project-state baseline conflict: expected %, current %',
          (v_pair.value#>>'{}')::bigint,v_state_rev;
      end if;
    else
      select version into v_current
        from objects
       where id=v_pair.key and trashed_at is null;

      if v_current is distinct from (v_pair.value#>>'{}')::bigint then
        raise exception
          'staged object baseline conflict on %: expected %, current %',
          v_pair.key,(v_pair.value#>>'{}')::bigint,v_current;
      end if;
    end if;
  end loop;

  for v_op in select value from jsonb_array_elements(v_stage.operations)
  loop
    v_type:=v_op->>'op';

    if v_type='create_object' then
      if v_op ? 'audit_requested' or v_op ? 'audit_priority' then
        raise exception 'staged create_object no longer accepts audit_requested/audit_priority; stage request_audit as a separate operation after creation';
      end if;
      perform set_config(
        (control_center.active_project()||'.allow_reserved_object_id'),
        case when coalesce((v_op->>'_auto_id')::boolean,false) then 'on' else 'off' end,true
      );
      v_result:=control_center.create_object(
        p_worker_id,
        coalesce(v_op->>'object_type','research'),
        v_op->>'title',
        nullif(v_op->>'statement',''),
        coalesce(v_op->>'body',''),
        nullif(v_op->>'parent_id',''),
        coalesce((v_op->>'position')::bigint,0),
        coalesce(v_op->'metadata','{}'::jsonb),
        coalesce(v_op->'research_interface','{}'::jsonb),
        nullif(v_op->>'mathematical_status',''),
        nullif(v_op->>'research_level',''),
        coalesce(v_op->>'lifecycle_status','active'),
        coalesce(v_op->>'attention','available'),
        v_op->>'id',
        nullif(v_op->>'legacy_id',''),
        nullif(v_op->>'simplified_statement',''),
        nullif(v_op->>'atlas_height',''),
        coalesce((v_op->>'atlas_hidden')::boolean,false)
      );
      perform set_config((control_center.active_project()||'.allow_reserved_object_id'),'off',true);

    elsif v_type='update_object' then
      v_id:=v_op->>'id';
      select version into v_current
        from objects
       where id=v_id and trashed_at is null;

      v_result:=control_center.update_object(
        p_worker_id,v_id,v_current,
        coalesce(v_op->'patch','{}'::jsonb),
        coalesce((v_op->>'substantive')::boolean,true)
      );

    elsif v_type='move_object' then
      v_id:=v_op->>'id';
      select version into v_current
        from objects
       where id=v_id and trashed_at is null;

      v_result:=control_center.move_object(
        p_worker_id,v_id,v_current,
        nullif(v_op->>'new_parent_id',''),
        coalesce((v_op->>'position')::bigint,0)
      );

    elsif v_type='add_edge' then
      v_result:=control_center.add_edge(
        p_worker_id,
        v_op->>'from_id',
        v_op->>'to_id',
        v_op->>'kind',
        coalesce(v_op->'metadata','{}'::jsonb)
      );

    elsif v_type='remove_edge' then
      v_result:=control_center.remove_edge(
        p_worker_id,
        v_op->>'from_id',
        v_op->>'to_id',
        v_op->>'kind'
      );

    elsif v_type='request_audit' then
      v_result:=control_center.request_audit(
        p_worker_id,
        v_op->>'id',
        coalesce((v_op->>'priority')::integer,control_center.config_int('audit.default_request_priority')),
        v_op->>'reason'
      );

    elsif v_type='certify_object' then
      v_id:=v_op->>'id';
      select version into v_current
        from objects
       where id=v_id and trashed_at is null;

      v_result:=control_center.certify_object(
        p_worker_id,v_id,v_current,v_op->>'note'
      );

    elsif v_type='fail_object' then
      v_id:=v_op->>'id';
      select version into v_current
        from objects
       where id=v_id and trashed_at is null;

      v_result:=control_center.fail_object(
        p_worker_id,v_id,v_current,v_op->>'reason'
      );

    elsif v_type='set_project_state' then
      v_result:=control_center.set_project_state(
        p_worker_id,coalesce(v_op->'patch','{}'::jsonb)
      );

    elsif v_type='resolve_signal' then
      v_result:=resolve_signal(
        p_worker_id,
        (v_op->>'signal_id')::bigint,
        coalesce(v_op->>'status','resolved')
      );

    elsif v_type='mark_reasoning_node' then
      v_result:=control_center.mark_reasoning_node(
        p_worker_id,
        v_op->>'object_id',
        v_op->>'node_kind',
        nullif(v_op->>'route_key',''),
        coalesce(v_op->>'note','')
      );


    else
      raise exception 'unsupported staged operation at commit: %',v_type;
    end if;

    v_results:=v_results||jsonb_build_array(
      jsonb_build_object('op',v_type,'result',v_result)
    );
  end loop;

  delete from stages where stage_id=p_stage_id;

  return jsonb_build_object(
    'committed',true,
    'stage_id',p_stage_id,
    'results',v_results,
    'repository_revision',(select revision from state where singleton)
  );
end
$function$

```

## commit_stage_core(p_worker_id bigint, p_stage_id bigint) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.commit_stage_core(p_worker_id bigint, p_stage_id bigint)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
DECLARE
  v_prior text;
  v_author_prior text;
  v_author bigint;
  v_stage record;
  v_result jsonb;
begin
  PERFORM control_center.active_project();
  
  PERFORM require_math_principal(p_worker_id);

  SELECT * INTO v_stage
  FROM stages
  WHERE stage_id=p_stage_id
    AND kind='batch'
    AND expires_at>now()
    AND (owner_worker_id=p_worker_id OR claimed_by_worker_id=p_worker_id);

  IF v_stage.stage_id IS NULL THEN
    v_author:=p_worker_id;
  ELSE
    v_author:=CASE WHEN v_stage.mode='research'
      THEN v_stage.owner_worker_id ELSE p_worker_id END;
  END IF;

  v_prior:=current_setting((control_center.active_project()||'.verified_stage_commit'),true);
  v_author_prior:=current_setting((control_center.active_project()||'.stage_math_author'),true);

  BEGIN
    PERFORM set_config((control_center.active_project()||'.verified_stage_commit'),'on',true);
    PERFORM set_config((control_center.active_project()||'.stage_math_author'),v_author::text,true);

    v_result:=control_center.commit_stage_locked_base(p_worker_id,p_stage_id);

    PERFORM set_config(
      (control_center.active_project()||'.verified_stage_commit'),coalesce(v_prior,''),true
    );
    PERFORM set_config(
      (control_center.active_project()||'.stage_math_author'),coalesce(v_author_prior,''),true
    );
  EXCEPTION WHEN OTHERS THEN
    PERFORM set_config(
      (control_center.active_project()||'.verified_stage_commit'),coalesce(v_prior,''),true
    );
    PERFORM set_config(
      (control_center.active_project()||'.stage_math_author'),coalesce(v_author_prior,''),true
    );
    RAISE;
  END;

  IF coalesce((v_result->>'already_committed')::boolean,false) THEN
    RETURN v_result||jsonb_build_object('retry_worker_id',p_worker_id);
  END IF;

  RETURN v_result||jsonb_build_object(
    'publication_executor_worker_id',p_worker_id,
    'substantive_author_worker_id',v_author,
    'principal_kind',(math_principal(p_worker_id)->>'principal_kind'),
    'recovered_stage',
      v_stage.stage_id IS NOT NULL
      AND v_stage.owner_worker_id IS DISTINCT FROM p_worker_id
  );
END
$function$

```

## commit_stage_locked_base(p_worker_id bigint, p_stage_id bigint) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.commit_stage_locked_base(p_worker_id bigint, p_stage_id bigint)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_stage record;
  v_receipt record;
  v_pair record;
  v_current bigint;
  v_digest text;
  v_object_keys text[];
  v_result jsonb;
  v_object_ids text[];
  v_receipt_cap integer;
  v_receipt_count integer;
  v_has_tree_ops boolean;
begin
  PERFORM control_center.active_project();
  
  perform purge_ephemeral();

  select * into v_receipt from commit_receipts
   where stage_id=p_stage_id
     and expires_at>now();

  if v_receipt.stage_id is not null then
    return jsonb_build_object(
      'committed',true,'already_committed',true,'stage_id',v_receipt.stage_id,
      'verified_digest',v_receipt.verified_digest,
      'operation_count',v_receipt.operation_count,
      'object_ids',v_receipt.object_ids,
      'repository_revision',v_receipt.repository_revision,
      'committed_at',v_receipt.committed_at,
      'original_publication_executor_worker_id',v_receipt.owner_worker_id
    );
  end if;

  select * into v_stage from stages
   where stage_id=p_stage_id
     and (owner_worker_id=p_worker_id or claimed_by_worker_id=p_worker_id)
     and kind='batch'
     and expires_at>now()
   for update;

  if v_stage.stage_id is null then
    raise exception 'commit-ready stage not found';
  end if;

  v_digest:=stage_digest(
    v_stage.operations,v_stage.baselines,
    v_stage.read_math_baselines,v_stage.stage_revision
  );

  if v_stage.verified_stage_revision is distinct from v_stage.stage_revision
     or v_stage.verified_digest is distinct from v_digest then
    raise exception 'stage must be successfully verified at its current revision before commit';
  end if;

  select exists(
    select 1 from jsonb_array_elements(v_stage.operations) e
     where e->>'op' in (
       'create_object','move_object','mark_reasoning_node',
       'trash_subtrees','restore_subtrees'
     )
  ) into v_has_tree_ops;

  /*
    Global lock order:
      structural advisory lock (if needed)
      -> stage/claim row already held
      -> object rows in deterministic id order
      -> singleton project state
      -> observability/needs side effects.
    This matches direct tree mutation, preventing object<->tree lock inversion.
  */
  if v_has_tree_ops then
    perform pg_advisory_xact_lock(hashtext((control_center.active_project()||'_tree')));
  end if;

  select coalesce(array_agg(key order by key),'{}'::text[])
    into v_object_keys
    from (
      select key from jsonb_each(v_stage.baselines)
       where key<>'__state_revision'
      union
      select key from jsonb_each(v_stage.read_math_baselines)
    ) q;

  perform o.id
    from objects o
   where o.id=any(v_object_keys)
   order by o.id
   for update;

  if v_stage.baselines ? '__state_revision' then
    perform 1 from state where singleton for update;
  end if;

  for v_pair in select key,value from jsonb_each(v_stage.baselines)
  loop
    if v_pair.key='__state_revision' then
      select revision into v_current
        from state where singleton;
    else
      select version into v_current
        from objects
       where id=v_pair.key and trashed_at is null;
    end if;

    if v_current is distinct from (v_pair.value#>>'{}')::bigint then
      raise exception
        'commit baseline conflict on %: expected %, current %',
        v_pair.key,(v_pair.value#>>'{}')::bigint,v_current;
    end if;
  end loop;

  for v_pair in select key,value from jsonb_each(v_stage.read_math_baselines)
  loop
    select math_version into v_current
      from objects
     where id=v_pair.key and trashed_at is null;

    if v_current is distinct from (v_pair.value#>>'{}')::bigint then
      raise exception
        'commit mathematical read-set conflict on %: expected math_version %, current %',
        v_pair.key,(v_pair.value#>>'{}')::bigint,v_current;
    end if;
  end loop;

  select coalesce(array_agg(distinct x) filter (where x is not null),'{}'::text[])
    into v_object_ids
    from (
      select e->>'id' as x
        from jsonb_array_elements(v_stage.operations) e
       where e->>'op'='create_object'
      union
      select e->>'object_id'
        from jsonb_array_elements(v_stage.operations) e
       where e->>'op'='mark_reasoning_node'
    ) q;

  perform set_config(
    (control_center.active_project()||'.stage_created_ids'),
    array_to_string(coalesce(v_object_ids,'{}'::text[]),','),
    true
  );

  v_result:=control_center.commit_stage_base(p_worker_id,p_stage_id);

  select max_commit_receipts into v_receipt_cap
    from settings where singleton;
  select count(*) into v_receipt_count
    from commit_receipts where expires_at>now();

  if v_receipt_count>=v_receipt_cap then
    delete from commit_receipts
     where stage_id in (
       select stage_id
         from commit_receipts
        order by committed_at
        limit v_receipt_count-v_receipt_cap+1
     );
  end if;

  insert into commit_receipts(
    stage_id,owner_worker_id,verified_digest,operation_count,
    object_ids,repository_revision,expires_at
  ) values (
    p_stage_id,p_worker_id,v_digest,jsonb_array_length(v_stage.operations),
    (v_object_ids)[1:control_center.config_int('api.default_limit')],
    (v_result->>'repository_revision')::bigint,
    now()+control_center.config_interval('stage.commit_receipt_ttl')
  );

  return v_result||jsonb_build_object(
    'verified_digest',v_digest,
    'idempotent_retry_available_until',now()+control_center.config_interval('stage.commit_receipt_ttl')
  );
end
$function$

```

## context(p_focus_id text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.context(p_focus_id text)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare
  v_path text;
  v_ids text[];
  v_child_total integer;
  v_input_total integer;
  v_consumer_total integer;
  v_children jsonb;
  v_inputs jsonb;
  v_consumers jsonb;
begin
  PERFORM control_center.active_project();
  
  select tree_path into v_path from objects
   where id=p_focus_id and trashed_at is null;
  if v_path is null then raise exception 'focus object % not found',p_focus_id; end if;

  v_ids:=array_remove(string_to_array(trim(both '/' from v_path),'/'),'');

  select count(*) into v_child_total from objects
   where parent_id=p_focus_id and trashed_at is null;
  select count(*) into v_input_total from edges where from_id=p_focus_id;
  select count(*) into v_consumer_total from edges where to_id=p_focus_id;

  select coalesce(jsonb_agg(object_capsule(q.id,control_center.config_int('text.preview_chars'))
    order by q.position,q.updated_at),'[]'::jsonb)
    into v_children
  from (
    select o.id,o.position,o.updated_at
    from objects o
    where o.parent_id=p_focus_id and o.trashed_at is null
    order by o.position,o.updated_at
    limit control_center.config_int('context.child_limit')
  ) q;

  select coalesce(jsonb_agg(jsonb_build_object(
    'kind',q.kind,'object',object_capsule(q.to_id,control_center.config_int('text.preview_chars'))
  ) order by q.kind,q.to_id),'[]'::jsonb)
    into v_inputs
  from (
    select e.kind,e.to_id from edges e
    where e.from_id=p_focus_id
    order by e.kind,e.to_id
    limit control_center.config_int('context.child_limit')
  ) q;

  select coalesce(jsonb_agg(jsonb_build_object(
    'kind',q.kind,'object',object_capsule(q.from_id,control_center.config_int('text.preview_chars'))
  ) order by q.kind,q.from_id),'[]'::jsonb)
    into v_consumers
  from (
    select e.kind,e.from_id from edges e
    where e.to_id=p_focus_id
    order by e.kind,e.from_id
    limit control_center.config_int('context.child_limit')
  ) q;

  return jsonb_build_object(
    'focus',object_brief(p_focus_id),
    'ancestors',(
      select coalesce(jsonb_agg(object_capsule(q.id,control_center.config_int('text.preview_chars')) order by q.ord),'[]'::jsonb)
      from (
        select o.id,array_position(v_ids,o.id) ord
        from objects o
        where o.id=any(v_ids) and o.id<>p_focus_id and o.trashed_at is null
      ) q
    ),
    'children',v_children,
    'children_total',v_child_total,
    'children_truncated',v_child_total>jsonb_array_length(v_children),
    'inputs',v_inputs,
    'inputs_total',v_input_total,
    'inputs_truncated',v_input_total>jsonb_array_length(v_inputs),
    'consumers',v_consumers,
    'consumers_total',v_consumer_total,
    'consumers_truncated',v_consumer_total>jsonb_array_length(v_consumers),
    'nearby_presence',presence_capsule(array[p_focus_id],false,4),
    'repository_revision',(select revision from state where singleton)
  );
end
$function$

```

## continue(p_worker_id bigint, p_outcome text DEFAULT NULL::text, p_details jsonb DEFAULT '{}'::jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.continue(p_worker_id bigint, p_outcome text DEFAULT NULL::text, p_details jsonb DEFAULT '{}'::jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_packet jsonb;
begin
  perform control_center.assert_worker_database_access(p_worker_id,'continue');
  perform control_center.active_project();

  v_packet := control_center.next(
    p_worker_id,
    p_outcome,
    coalesce(p_details,'{}'::jsonb)
  );

  if nullif(btrim(coalesce(p_outcome,'')),'') is null
     and coalesce((v_packet->>'no_assignment')::boolean,false) is not true
  then
    v_packet := (v_packet - 'next_reminder')
      || jsonb_build_object(
           'continue_reminder',
           'add outcome or DEFER to get next assignment'
         );
  end if;

  return v_packet;
end
$function$

```

## continue(p_worker_id bigint, p_outcome text, p_details text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.continue(p_worker_id bigint, p_outcome text, p_details text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
begin
  perform control_center.active_project();
  return control_center.continue(
    p_worker_id,
    p_outcome,
    jsonb_build_object('summary',coalesce(p_details,''))
  );
end
$function$

```

## create_object(p_worker_id bigint, p_object_type text, p_title text, p_statement text DEFAULT NULL::text, p_body text DEFAULT ''::text, p_parent_id text DEFAULT NULL::text, p_position bigint DEFAULT 0, p_metadata jsonb DEFAULT '{}'::jsonb, p_research_interface jsonb DEFAULT '{}'::jsonb, p_mathematical_status text DEFAULT NULL::text, p_research_level text DEFAULT 'working_unit'::text, p_lifecycle_status text DEFAULT 'active'::text, p_attention text DEFAULT 'available'::text, p_id text DEFAULT NULL::text, p_legacy_id text DEFAULT NULL::text, p_simplified_statement text DEFAULT NULL::text, p_atlas_height text DEFAULT NULL::text, p_atlas_hidden boolean DEFAULT false) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.create_object(p_worker_id bigint, p_object_type text, p_title text, p_statement text DEFAULT NULL::text, p_body text DEFAULT ''::text, p_parent_id text DEFAULT NULL::text, p_position bigint DEFAULT 0, p_metadata jsonb DEFAULT '{}'::jsonb, p_research_interface jsonb DEFAULT '{}'::jsonb, p_mathematical_status text DEFAULT NULL::text, p_research_level text DEFAULT 'working_unit'::text, p_lifecycle_status text DEFAULT 'active'::text, p_attention text DEFAULT 'available'::text, p_id text DEFAULT NULL::text, p_legacy_id text DEFAULT NULL::text, p_simplified_statement text DEFAULT NULL::text, p_atlas_height text DEFAULT NULL::text, p_atlas_hidden boolean DEFAULT false)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_result jsonb;
  v_id text;
  v_adv jsonb;
begin
  perform control_center.active_project();

  v_result:=control_center.create_object_core(
    p_worker_id,p_object_type,p_title,p_statement,p_body,p_parent_id,p_position,
    p_metadata,p_research_interface,p_mathematical_status,p_research_level,
    p_lifecycle_status,p_attention,false,0,case when nullif(btrim(coalesce(p_id,'')),'') is null then control_center.allocate_reasoning_name(p_title,p_simplified_statement,p_statement,'{}'::text[],true) else p_id end,p_legacy_id
  );

  v_id:=v_result->>'id';

  update objects
     set simplified_statement=nullif(btrim(coalesce(p_simplified_statement,'')),''),
         atlas_height=nullif(btrim(coalesce(p_atlas_height,'')),''),
         atlas_hidden=coalesce(p_atlas_hidden,false)
   where id=v_id;

  v_adv:=proposer_hygiene_advisory(v_id);

  v_result:=(select to_jsonb(o) from objects o where o.id=v_id)
    || jsonb_build_object('repository_revision',(v_result->>'repository_revision')::bigint);

  if v_adv is null then return v_result; end if;
  return v_result||jsonb_build_object('reasoning_hygiene',jsonb_build_array(v_adv));
end
$function$

```

## create_object_core(p_worker_id bigint, p_object_type text, p_title text, p_statement text DEFAULT NULL::text, p_body text DEFAULT ''::text, p_parent_id text DEFAULT NULL::text, p_position bigint DEFAULT 0, p_metadata jsonb DEFAULT '{}'::jsonb, p_research_interface jsonb DEFAULT '{}'::jsonb, p_mathematical_status text DEFAULT NULL::text, p_research_level text DEFAULT NULL::text, p_lifecycle_status text DEFAULT 'active'::text, p_attention text DEFAULT 'available'::text, p_audit_requested boolean DEFAULT NULL::boolean, p_audit_priority integer DEFAULT 0, p_id text DEFAULT NULL::text, p_legacy_id text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.create_object_core(p_worker_id bigint, p_object_type text, p_title text, p_statement text DEFAULT NULL::text, p_body text DEFAULT ''::text, p_parent_id text DEFAULT NULL::text, p_position bigint DEFAULT 0, p_metadata jsonb DEFAULT '{}'::jsonb, p_research_interface jsonb DEFAULT '{}'::jsonb, p_mathematical_status text DEFAULT NULL::text, p_research_level text DEFAULT NULL::text, p_lifecycle_status text DEFAULT 'active'::text, p_attention text DEFAULT 'available'::text, p_audit_requested boolean DEFAULT NULL::boolean, p_audit_priority integer DEFAULT 0, p_id text DEFAULT NULL::text, p_legacy_id text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_id text;
  v_parent_path text;
  v_path text;
  v_audit_status text;
  v_audit_requested boolean;
  v_requirement text;
  v_support text;
  v_reason text;
  v_rev bigint;
  v_row record;
  v_authors bigint[];
  v_author_worker_id bigint:=effective_substantive_worker(p_worker_id);
  v_metadata jsonb:=coalesce(p_metadata,'{}'::jsonb);
begin
  perform control_center.active_project();

  if nullif(btrim(coalesce(p_id,'')),'') is null then
    v_id:=control_center.allocate_reasoning_name(p_title,null,p_statement,'{}'::text[],true);
  else
    v_id:=btrim(p_id);
    if v_id ~ '^[0-9]{7}$'
       and coalesce(current_setting((control_center.active_project()||'.allow_reserved_object_id'),true),'')<>'on'
    then
      raise exception 'seven-digit decimal object IDs are reserved for automatic allocation';
    end if;
    if exists(select 1 from objects where id=v_id) then
      raise exception 'object id/name % already exists',v_id;
    end if;
  end if;

  perform pg_advisory_xact_lock(hashtext((control_center.active_project()||'_tree')));

  if p_parent_id is not null then
    select tree_path into v_parent_path
      from objects
     where id=p_parent_id and trashed_at is null
     for share;
    if v_parent_path is null then raise exception 'parent % not found',p_parent_id; end if;
    v_path:=v_parent_path||v_id||'/';
  else
    v_path:=v_id||'/';
  end if;

  if p_mathematical_status='proved' then
    if nullif(btrim(coalesce(p_statement,'')),'') is null then
      raise exception 'proved object requires a nonempty statement';
    end if;
    if nullif(btrim(coalesce(p_body,'')),'') is null then
      raise exception 'proved object requires a nonempty proof/body';
    end if;
  end if;

  v_audit_status:=case
    when p_mathematical_status in ('proved','evidence') then 'pending'
    else 'not_required' end;

  -- Optimistic trust: publication is immediately usable as provisional
  -- mathematics and never creates an audit obligation. A worker who believes
  -- independent checking matters must make a separate request_audit(...) call.
  v_audit_requested:=false;

  v_requirement:=case
    when p_mathematical_status='proved'
      and p_attention='focus'
      and p_research_level in ('theorem','proof_level')
      then 'independent_reconstruction'
    else 'independent_check'
  end;

  v_support:=case when p_mathematical_status='evidence' then 'evidence' else 'unchecked' end;
  v_reason:=case
    when p_mathematical_status='evidence' then 'finite_or_empirical_evidence'
    when p_mathematical_status='proved' then 'provisional_unaudited'
    else 'not_a_proved_or_evidence_claim' end;

  v_authors:=case
    when p_mathematical_status is null then '{}'::bigint[]
    else array[v_author_worker_id] end;

  insert into objects(
    id,legacy_id,parent_id,tree_path,position,object_type,title,statement,body,
    metadata,research_interface,mathematical_status,research_level,
    lifecycle_status,attention,audit_status,audit_requested,audit_priority,
    audit_requirement,support_status,support_reason,
    origin_worker_id,last_substantive_worker_id,substantive_worker_ids,
    math_version,audited_math_version
  ) values (
    v_id,p_legacy_id,p_parent_id,v_path,greatest(0,p_position),p_object_type,
    p_title,p_statement,coalesce(p_body,''),
    v_metadata,coalesce(p_research_interface,'{}'::jsonb),
    p_mathematical_status,p_research_level,p_lifecycle_status,p_attention,
    v_audit_status,v_audit_requested,greatest(control_center.config_int('priority.min'),least(control_center.config_int('priority.max'),p_audit_priority)),
    v_requirement,v_support,v_reason,
    v_author_worker_id,case when p_mathematical_status is null then null else v_author_worker_id end,
    v_authors,1,null
  ) returning * into v_row;

  v_rev:=record_change(
    'create_object',array[v_id],
    jsonb_build_object(
      'object_type',p_object_type,'research_level',p_research_level,
      'attention',p_attention,'audit_requirement',v_requirement,
      'audit_requested',v_audit_requested,
      'optimistic_trust',p_mathematical_status in ('proved','evidence') and not v_audit_requested
    )
  );

  return to_jsonb(v_row)||jsonb_build_object('repository_revision',v_rev);
end
$function$

```

## create_project_from_template(p_project_schema text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.create_project_from_template(p_project_schema text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'pg_catalog', 'control_center'
AS $function$
declare
  t record;
  con record;
  trg record;
  v_trigger_sql text;
  v_tables integer:=0;
  v_rows bigint:=0;
  v_row_count bigint;
  v_fks integer:=0;
  v_triggers integer:=0;
  v_project_config integer:=0;
  v_token_result jsonb;
  v_wrapper_result jsonb;
  v_seed text:=control_center.config_text('project.seed_schema');
  v_max_name integer:=control_center.config_int('project.schema_name_max_chars');
begin
  if p_project_schema is null
     or p_project_schema !~ '^[a-z][a-z0-9_]*$'
     or length(p_project_schema)>v_max_name then
    raise exception 'invalid project schema name %',p_project_schema;
  end if;

  if p_project_schema=v_seed
     or control_center.config_json_array_contains(
          'project.reserved_schemas',p_project_schema
        ) then
    raise exception 'reserved schema name %',p_project_schema;
  end if;

  if to_regnamespace(p_project_schema) is not null then
    raise exception 'schema % already exists',p_project_schema;
  end if;

  if not control_center.is_managed_project_schema(v_seed) then
    raise exception '% is not a valid managed-project seed',v_seed;
  end if;

  perform pg_advisory_xact_lock(hashtext('control_center_project_factory'));

  execute format('create schema %I authorization postgres',p_project_schema);

  for t in
    select c.relname as table_name,c.relrowsecurity,c.relforcerowsecurity
    from pg_class c
    join pg_namespace n on n.oid=c.relnamespace
    where n.nspname=v_seed
      and c.relkind='r'
    order by c.relname
  loop
    execute format(
      'create table %I.%I (like %I.%I including all)',
      p_project_schema,t.table_name,v_seed,t.table_name
    );
    execute format(
      'alter table %I.%I owner to postgres',
      p_project_schema,t.table_name
    );

    execute format(
      'insert into %I.%I select * from %I.%I',
      p_project_schema,t.table_name,v_seed,t.table_name
    );
    get diagnostics v_row_count=row_count;
    v_rows:=v_rows+v_row_count;

    execute format(
      'alter table %I.%I enable row level security',
      p_project_schema,t.table_name
    );

    execute format(
      'revoke all on table %I.%I from public',
      p_project_schema,t.table_name
    );
    if exists(select 1 from pg_roles where rolname='anon') then
      execute format(
        'revoke all on table %I.%I from anon',
        p_project_schema,t.table_name
      );
    end if;
    if exists(select 1 from pg_roles where rolname='authenticated') then
      execute format(
        'revoke all on table %I.%I from authenticated',
        p_project_schema,t.table_name
      );
    end if;
    if exists(select 1 from pg_roles where rolname='service_role') then
      execute format(
        'revoke all on table %I.%I from service_role',
        p_project_schema,t.table_name
      );
    end if;

    v_tables:=v_tables+1;
  end loop;

  for con in
    select c.relname as table_name,
           x.conname,
           pg_get_constraintdef(x.oid,true) as definition
    from pg_constraint x
    join pg_class c on c.oid=x.conrelid
    join pg_namespace n on n.oid=c.relnamespace
    where n.nspname=v_seed
      and x.contype='f'
    order by c.relname,x.conname
  loop
    execute format(
      'alter table %I.%I add constraint %I %s',
      p_project_schema,
      con.table_name,
      con.conname,
      replace(
        con.definition,
        format('%I.',v_seed),
        format('%I.',p_project_schema)
      )
    );
    v_fks:=v_fks+1;
  end loop;

  for trg in
    select pg_get_triggerdef(x.oid,true) as definition
    from pg_trigger x
    join pg_class c on c.oid=x.tgrelid
    join pg_namespace n on n.oid=c.relnamespace
    where n.nspname=v_seed
      and not x.tgisinternal
    order by c.relname,x.tgname
  loop
    v_trigger_sql:=replace(
      trg.definition,
      format(' ON %I.',v_seed),
      format(' ON %I.',p_project_schema)
    );
    execute v_trigger_sql;
    v_triggers:=v_triggers+1;
  end loop;

  execute format('revoke all on schema %I from public',p_project_schema);
  if exists(select 1 from pg_roles where rolname='anon') then
    execute format('revoke all on schema %I from anon',p_project_schema);
  end if;
  if exists(select 1 from pg_roles where rolname='authenticated') then
    execute format('revoke all on schema %I from authenticated',p_project_schema);
  end if;
  if exists(select 1 from pg_roles where rolname='service_role') then
    execute format('grant usage on schema %I to service_role',p_project_schema);
  end if;

  insert into control_center.configuration(key,value,category,description,updated_at)
  select
    replace(c.key,'.'||v_seed||'.','.'||p_project_schema||'.'),
    c.value,
    c.category,
    c.description,
    now()
  from control_center.configuration c
  where strpos(c.key,'.'||v_seed||'.')>0
  on conflict(key) do update set
    value=excluded.value,
    category=excluded.category,
    description=excluded.description,
    updated_at=excluded.updated_at;
  get diagnostics v_project_config=row_count;

  v_token_result:=control_center.replace_project_seed_token(p_project_schema);

  perform set_config('control_center.allow_project_function_ddl','on',true);
  for t in
    select p.proname,
           pg_get_function_identity_arguments(p.oid) as identity_arguments
    from pg_proc p
    join pg_namespace n on n.oid=p.pronamespace
    where n.nspname=p_project_schema
      and p.prokind='f'
  loop
    execute format(
      'drop function %I.%I(%s)',
      p_project_schema,t.proname,t.identity_arguments
    );
  end loop;

  v_wrapper_result:=control_center.sync_project_wrappers(p_project_schema);

  if not control_center.is_managed_project_schema(p_project_schema) then
    raise exception 'new schema % failed managed-project recognition',p_project_schema;
  end if;

  return jsonb_build_object(
    'created',true,
    'project_schema',p_project_schema,
    'seed_schema',v_seed,
    'tables_cloned',v_tables,
    'seed_rows_copied',v_rows,
    'foreign_keys_created',v_fks,
    'triggers_created',v_triggers,
    'project_configuration_entries_copied',v_project_config,
    'token_replacement',v_token_result,
    'wrapper_sync',v_wrapper_result
  );
end
$function$

```

## create_reasoning_child(p_worker_id bigint, p_parent_id text, p_title text, p_statement text DEFAULT NULL::text, p_body text DEFAULT ''::text, p_node_kind text DEFAULT 'step'::text, p_route_key text DEFAULT NULL::text, p_metadata jsonb DEFAULT '{}'::jsonb, p_research_interface jsonb DEFAULT '{}'::jsonb, p_mathematical_status text DEFAULT NULL::text, p_research_level text DEFAULT 'working_unit'::text, p_attention text DEFAULT 'available'::text, p_audit_requested boolean DEFAULT NULL::boolean, p_audit_priority integer DEFAULT 0, p_id text DEFAULT NULL::text, p_simplified_statement text DEFAULT NULL::text, p_atlas_height text DEFAULT NULL::text, p_atlas_hidden boolean DEFAULT false) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.create_reasoning_child(p_worker_id bigint, p_parent_id text, p_title text, p_statement text DEFAULT NULL::text, p_body text DEFAULT ''::text, p_node_kind text DEFAULT 'step'::text, p_route_key text DEFAULT NULL::text, p_metadata jsonb DEFAULT '{}'::jsonb, p_research_interface jsonb DEFAULT '{}'::jsonb, p_mathematical_status text DEFAULT NULL::text, p_research_level text DEFAULT 'working_unit'::text, p_attention text DEFAULT 'available'::text, p_audit_requested boolean DEFAULT NULL::boolean, p_audit_priority integer DEFAULT 0, p_id text DEFAULT NULL::text, p_simplified_statement text DEFAULT NULL::text, p_atlas_height text DEFAULT NULL::text, p_atlas_hidden boolean DEFAULT false)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_obj jsonb;
  v_id text;
  v_reason jsonb;
  v_adv jsonb;
  v_result jsonb;
begin
  perform control_center.active_project();

  if p_node_kind='root' then
    raise exception 'use create_object + mark_reasoning_node for a new independent reasoning root';
  end if;

  v_obj:=control_center.create_object(
    p_worker_id,'research',p_title,p_statement,p_body,p_parent_id,0,
    coalesce(p_metadata,'{}'::jsonb),
    coalesce(p_research_interface,'{}'::jsonb),
    p_mathematical_status,p_research_level,'active',p_attention,p_id,null,
    p_simplified_statement,p_atlas_height,p_atlas_hidden
  );
  v_id:=v_obj->>'id';

  v_reason:=control_center.mark_reasoning_node(
    p_worker_id,v_id,p_node_kind,p_route_key,''
  );

  v_result:=jsonb_build_object(
    'object',object_brief(v_id),
    'repository_revision',(select revision from state where singleton)
  );

  v_adv:=proposer_hygiene_advisory(v_id);
  if v_adv is null then return v_result; end if;
  return v_result||jsonb_build_object('reasoning_hygiene',jsonb_build_array(v_adv));
end
$function$

```

## create_reasoning_child_core(p_worker_id bigint, p_parent_id text, p_title text, p_statement text DEFAULT NULL::text, p_body text DEFAULT ''::text, p_node_kind text DEFAULT 'step'::text, p_route_key text DEFAULT NULL::text, p_metadata jsonb DEFAULT '{}'::jsonb, p_research_interface jsonb DEFAULT '{}'::jsonb, p_mathematical_status text DEFAULT NULL::text, p_research_level text DEFAULT 'working_unit'::text, p_attention text DEFAULT 'available'::text, p_id text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.create_reasoning_child_core(p_worker_id bigint, p_parent_id text, p_title text, p_statement text DEFAULT NULL::text, p_body text DEFAULT ''::text, p_node_kind text DEFAULT 'step'::text, p_route_key text DEFAULT NULL::text, p_metadata jsonb DEFAULT '{}'::jsonb, p_research_interface jsonb DEFAULT '{}'::jsonb, p_mathematical_status text DEFAULT NULL::text, p_research_level text DEFAULT 'working_unit'::text, p_attention text DEFAULT 'available'::text, p_id text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_obj jsonb;
  v_id text;
  v_reason jsonb;
begin
  perform control_center.active_project();
  if p_node_kind='root' then
    raise exception 'use create_object + mark_reasoning_node for a new independent reasoning root';
  end if;
  v_obj:=control_center.create_object(
    p_worker_id,'research',p_title,p_statement,p_body,p_parent_id,0,
    coalesce(p_metadata,'{}'::jsonb),
    coalesce(p_research_interface,'{}'::jsonb),
    p_mathematical_status,p_research_level,'active',p_attention,p_id,null,
    null,null,false
  );
  v_id:=v_obj->>'id';
  v_reason:=control_center.mark_reasoning_node(
    p_worker_id,v_id,p_node_kind,p_route_key,''
  );
  return jsonb_build_object(
    'object',object_brief(v_id),
    'repository_revision',(select revision from state where singleton)
  );
end
$function$

```

## defer_to_research(p_worker_id bigint, p_reason text, p_focus_id text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.defer_to_research(p_worker_id bigint, p_reason text, p_focus_id text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_claim record;
  v_result jsonb;
begin
  perform control_center.active_project();

  select * into v_claim
  from claims
  where worker_id=p_worker_id and expires_at>now()
  order by created_at desc
  limit 1;

  if v_claim.claim_id is null then
    raise exception 'active assignment not found';
  end if;

  v_result:=request_assignment(
    p_worker_id,
    jsonb_strip_nulls(jsonb_build_object(
      'role','researcher',
      'task',nullif(btrim(coalesce(p_reason,'')),'')
    )),
    control_center.config_int('scheduler.defer_to_research_priority'),
    'next_boundary',
    'next_assignment'
  );

  return v_result||jsonb_build_object(
    'deferred_obligation_preserved',true,
    'focus_parameter_ignored',p_focus_id is not null,
    'note','Research preference queued without any mathematical focus; the researcher chooses its own route.'
  );
end
$function$

```

## delete_broadcast(p_worker_id bigint, p_broadcast_id bigint) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.delete_broadcast(p_worker_id bigint, p_broadcast_id bigint)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_row record;
begin
  perform control_center.active_project();

  if p_worker_id is null or not exists(select 1 from runs where worker_id=p_worker_id) then
    raise exception 'known worker_id is required';
  end if;

  delete from broadcasts
   where id=p_broadcast_id
   returning * into v_row;

  if v_row.id is null then
    raise exception 'broadcast not found';
  end if;

  return jsonb_build_object(
    'deleted',true,
    'id',v_row.id
  );
end
$function$

```

## dependency_repair_candidates(p_limit integer DEFAULT 12) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.dependency_repair_candidates(p_limit integer DEFAULT 12)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$begin
  PERFORM control_center.active_project();
  
  RETURN (

with bad as (
  select
    c.id consumer_id,
    c.title consumer_title,
    c.attention consumer_attention,
    c.research_level consumer_level,
    c.support_status consumer_support,
    c.research_interface consumer_interface,
    p.id premise_id,
    p.title premise_title,
    p.support_status premise_support,
    p.audit_status premise_audit,
    p.math_version premise_math_version,
    p.research_interface premise_interface,
    e.metadata edge_metadata
  from objects c
  join edges e on e.from_id=c.id and e.kind='depends_on'
  join objects p on p.id=e.to_id and p.trashed_at is null
  where c.trashed_at is null
    and c.mathematical_status in ('proved','evidence')
    and c.support_status<>'supported'
    and p.support_status<>'supported'
), singleton_bad as (
  select consumer_id
  from bad
  group by consumer_id
  having count(*)=1
), ranked as (
  select b.*,
    (select count(*) from edges x where x.to_id=b.consumer_id and x.kind='depends_on') blast_radius
  from bad b
  join singleton_bad s using(consumer_id)
  order by
    case b.consumer_attention when 'focus' then 0 when 'available' then 1 else 2 end,
    blast_radius desc,
    b.consumer_id
  limit greatest(1,least(control_center.config_int('api.queue_limit'),p_limit))
)
select jsonb_build_object(
  'items',coalesce(jsonb_agg(jsonb_build_object(
    'consumer',jsonb_build_object(
      'id',consumer_id,'title',consumer_title,
      'support_status',consumer_support,'research_level',consumer_level,
      'research_interface',preview_value(consumer_interface,control_center.config_int('preview.dependency_interface_chars'))
    ),
    'single_bad_premise',jsonb_build_object(
      'id',premise_id,'title',premise_title,
      'support_status',premise_support,'audit_status',premise_audit,
      'math_version',premise_math_version,
      'research_interface',preview_value(premise_interface,control_center.config_int('preview.dependency_interface_chars'))
    ),
    'edge_metadata',edge_metadata,
    'blast_radius',blast_radius,
    'repair_hint',
      'Check whether the consumer uses only a proper subclaim of this premise. If so, extract/re-prove the smallest consumed statement and replace the dependency instead of revalidating an omnibus module.'
  )),'[]'::jsonb),
  'semantics',
    'Derived candidates only: each consumer has exactly one currently unsupported direct logical premise.'
)
from ranked

  );
end$function$

```

## discard_stage(p_worker_id bigint, p_stage_id bigint) -> boolean

```sql
CREATE OR REPLACE FUNCTION control_center.discard_stage(p_worker_id bigint, p_stage_id bigint)
 RETURNS boolean
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_count integer;
begin
  PERFORM control_center.active_project();
  
  delete from stages
   where stage_id=p_stage_id
     and (owner_worker_id=p_worker_id or claimed_by_worker_id=p_worker_id);
  get diagnostics v_count=row_count;
  return v_count>0;
end
$function$

```

## edges(p_id text, p_direction text DEFAULT 'both'::text, p_kinds text[] DEFAULT NULL::text[], p_limit integer DEFAULT 100) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.edges(p_id text, p_direction text DEFAULT 'both'::text, p_kinds text[] DEFAULT NULL::text[], p_limit integer DEFAULT 100)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare
  v_limit integer:=greatest(1,least(control_center.config_int('api.edge_limit'),p_limit));
  v_out_total integer:=0;
  v_in_total integer:=0;
  v_out jsonb:='[]'::jsonb;
  v_in jsonb:='[]'::jsonb;
begin
  PERFORM control_center.active_project();
  
  if p_direction not in ('in','out','both') then
    raise exception 'direction must be in, out, or both';
  end if;

  if p_direction in ('out','both') then
    select count(*) into v_out_total from edges e
     where e.from_id=p_id and (p_kinds is null or e.kind=any(p_kinds));

    select coalesce(jsonb_agg(jsonb_build_object(
      'kind',q.kind,'to',object_capsule(q.to_id,control_center.config_int('text.preview_chars')),'metadata',q.metadata
    ) order by q.kind,q.to_id),'[]'::jsonb)
    into v_out
    from (
      select * from edges e
       where e.from_id=p_id and (p_kinds is null or e.kind=any(p_kinds))
       order by e.kind,e.to_id
       limit v_limit
    ) q;
  end if;

  if p_direction in ('in','both') then
    select count(*) into v_in_total from edges e
     where e.to_id=p_id and (p_kinds is null or e.kind=any(p_kinds));

    select coalesce(jsonb_agg(jsonb_build_object(
      'kind',q.kind,'from',object_capsule(q.from_id,control_center.config_int('text.preview_chars')),'metadata',q.metadata
    ) order by q.kind,q.from_id),'[]'::jsonb)
    into v_in
    from (
      select * from edges e
       where e.to_id=p_id and (p_kinds is null or e.kind=any(p_kinds))
       order by e.kind,e.from_id
       limit v_limit
    ) q;
  end if;

  return jsonb_build_object(
    'id',p_id,
    'outgoing',v_out,
    'outgoing_total',v_out_total,
    'outgoing_truncated',v_out_total>jsonb_array_length(v_out),
    'incoming',v_in,
    'incoming_total',v_in_total,
    'incoming_truncated',v_in_total>jsonb_array_length(v_in),
    'repository_revision',(select revision from state where singleton)
  );
end
$function$

```

## edges_page(p_id text, p_direction text DEFAULT 'out'::text, p_kinds text[] DEFAULT NULL::text[], p_after_kind text DEFAULT NULL::text, p_after_id text DEFAULT NULL::text, p_limit integer DEFAULT 100) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.edges_page(p_id text, p_direction text DEFAULT 'out'::text, p_kinds text[] DEFAULT NULL::text[], p_after_kind text DEFAULT NULL::text, p_after_id text DEFAULT NULL::text, p_limit integer DEFAULT 100)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare
  v_limit integer:=greatest(1,least(control_center.config_int('api.edge_limit'),p_limit));
  v_items jsonb;
  v_count integer;
  v_last_kind text;
  v_last_id text;
  v_more boolean;
begin
  PERFORM control_center.active_project();
  
  if p_direction not in ('out','in') then
    raise exception 'paged edge direction must be out or in';
  end if;

  if p_direction='out' then
    with q as (
      select e.kind,e.to_id as other_id,e.metadata
      from edges e
      where e.from_id=p_id
        and (p_kinds is null or e.kind=any(p_kinds))
        and (
          p_after_kind is null
          or (e.kind,e.to_id)>(p_after_kind,coalesce(p_after_id,''))
        )
      order by e.kind,e.to_id
      limit v_limit+1
    ), shown as (
      select * from q order by kind,other_id limit v_limit
    )
    select coalesce(jsonb_agg(jsonb_build_object(
      'kind',kind,'to',object_capsule(other_id,control_center.config_int('text.preview_chars')),'metadata',metadata
    ) order by kind,other_id),'[]'::jsonb),
    count(*),max(kind) filter(where rn=maxrn),
    max(other_id) filter(where rn=maxrn),
    (select count(*)>v_limit from q)
    into v_items,v_count,v_last_kind,v_last_id,v_more
    from (
      select shown.*,row_number() over(order by kind,other_id) rn,
             count(*) over() maxrn
      from shown
    ) s;
  else
    with q as (
      select e.kind,e.from_id as other_id,e.metadata
      from edges e
      where e.to_id=p_id
        and (p_kinds is null or e.kind=any(p_kinds))
        and (
          p_after_kind is null
          or (e.kind,e.from_id)>(p_after_kind,coalesce(p_after_id,''))
        )
      order by e.kind,e.from_id
      limit v_limit+1
    ), shown as (
      select * from q order by kind,other_id limit v_limit
    )
    select coalesce(jsonb_agg(jsonb_build_object(
      'kind',kind,'from',object_capsule(other_id,control_center.config_int('text.preview_chars')),'metadata',metadata
    ) order by kind,other_id),'[]'::jsonb),
    count(*),max(kind) filter(where rn=maxrn),
    max(other_id) filter(where rn=maxrn),
    (select count(*)>v_limit from q)
    into v_items,v_count,v_last_kind,v_last_id,v_more
    from (
      select shown.*,row_number() over(order by kind,other_id) rn,
             count(*) over() maxrn
      from shown
    ) s;
  end if;

  return jsonb_build_object(
    'id',p_id,'direction',p_direction,'items',coalesce(v_items,'[]'::jsonb),
    'returned_count',coalesce(v_count,0),'has_more',coalesce(v_more,false),
    'next_after_kind',case when v_more then v_last_kind else null end,
    'next_after_id',case when v_more then v_last_id else null end,
    'repository_revision',(select revision from state where singleton)
  );
end
$function$

```

## end_presence(p_worker_id bigint, p_presence_id bigint) -> boolean

```sql
CREATE OR REPLACE FUNCTION control_center.end_presence(p_worker_id bigint, p_presence_id bigint)
 RETURNS boolean
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_count integer;
begin
  PERFORM control_center.active_project();
  
  delete from presence
   where presence_id=p_presence_id and worker_id=p_worker_id;
  get diagnostics v_count=row_count;
  return v_count>0;
end
$function$

```

## fail_object(p_worker_id bigint, p_id text, p_expected_version bigint, p_reason text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.fail_object(p_worker_id bigint, p_id text, p_expected_version bigint, p_reason text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_row record;
  v_consumers integer;
  v_is_state boolean;
  v_rev bigint;
begin
  PERFORM control_center.active_project();
  
  select * into v_row from objects
   where id=p_id and trashed_at is null for update;

  if v_row.id is null then raise exception 'object % not found',p_id; end if;
  if v_row.version<>p_expected_version then raise exception 'version conflict on %',p_id; end if;

  select count(*) into v_consumers from edges
   where to_id=p_id and kind in ('proof','depends_on');

  select exists(
    select 1 from state s
     where s.singleton and p_id=any(array[
       s.grand_theorem_id,s.current_strategy_id,
       s.proof_frontier_id,s.current_bottleneck_id
     ]::text[])
  ) into v_is_state;

  update objects
     set audit_status='failed',
         audit_requested=false,
         audited_math_version=null,
         support_status='blocked',
         support_reason=left(coalesce(p_reason,'audit failure'),control_center.config_int('text.medium_chars')),
         lifecycle_status='retained',
         attention='hidden',
         metadata=metadata||jsonb_build_object(
           'last_failure',jsonb_build_object('reason',p_reason,'recorded_at',now())
         ),
         version=version+1,
         updated_at=now()
   where id=p_id
   returning * into v_row;

  delete from certificates where object_id=p_id;
  perform invalidate_dependents(array[p_id],'load-bearing premise failed');
  perform refresh_dependents(array[p_id]);

  v_rev:=record_change(
    'fail',array[p_id],
    jsonb_build_object('reason',p_reason,'direct_consumers',v_consumers)
  );


  return to_jsonb(v_row)||jsonb_build_object(
    'repository_revision',v_rev,'direct_consumers',v_consumers
  );
end
$function$

```

## flag_audit_anomaly(p_worker_id bigint, p_id text, p_reason text, p_priority integer DEFAULT 100) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.flag_audit_anomaly(p_worker_id bigint, p_id text, p_reason text, p_priority integer DEFAULT 100)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_result jsonb;
  v_id text := control_center.canonical_object_id(p_id);
begin
  perform control_center.active_project();

  if nullif(btrim(coalesce(p_reason,'')),'') is null then
    raise exception 'anomaly audit requires a concrete reason';
  end if;

  v_result := control_center.request_audit(p_worker_id,v_id,p_priority,p_reason);

  update objects
     set metadata=coalesce(metadata,'{}'::jsonb)||jsonb_build_object(
       'audit_trigger_kind','anomaly',
       'audit_anomaly_reason',p_reason,
       'audit_anomaly_recorded_at',now()
     ),
     updated_at=now()
   where id=v_id;

  return v_result||jsonb_build_object('audit_trigger_kind','anomaly');
end
$function$

```

## force_role(p_worker_id bigint DEFAULT NULL::bigint, p_role text DEFAULT NULL::text, p_task text DEFAULT NULL::text, p_focus_id text DEFAULT NULL::text, p_target_ids text[] DEFAULT '{}'::text[]) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.force_role(p_worker_id bigint DEFAULT NULL::bigint, p_role text DEFAULT NULL::text, p_task text DEFAULT NULL::text, p_focus_id text DEFAULT NULL::text, p_target_ids text[] DEFAULT '{}'::text[])
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
DECLARE
  v_worker bigint := coalesce(p_worker_id,control_center.allocate_identity('operational_id'));
  v_role text := lower(btrim(coalesce(p_role,'')));
  v_mode text;
  v_purpose text;
  v_task text := nullif(btrim(coalesce(p_task,'')),'');
  v_targets text[] := '{}'::text[];
  v_focus text;
  v_bad text;
  v_ttl integer;
  v_cap integer;
  v_count integer;
  v_claim bigint;
  v_old record;
  v_packet jsonb;
begin
  PERFORM control_center.active_project();
  
  v_role := case v_role
    when 'research' then 'researcher'
    when 'researcher' then 'researcher'
    when 'audit' then 'auditor'
    when 'auditor' then 'auditor'
    when 'coordination' then 'coordinator'
    when 'coordinate' then 'coordinator'
    when 'coordinator' then 'coordinator'
    else v_role
  end;

  if v_role='researcher' then
    if not control_center.research_mode_enabled('research') then raise exception 'research mode is disabled'; end if;
    v_mode:='research';
    v_purpose:='operator_forced_research';
  elsif v_role='isolated_researcher' then
    if not control_center.research_mode_enabled('isolated_research') then raise exception 'isolated_research mode is disabled'; end if;
    v_mode:='isolated_research';
    v_purpose:='operator_forced_isolated_research';
  elsif v_role='auditor' then
    v_mode:='audit';
    v_purpose:='operator_forced_audit';
  elsif v_role='coordinator' then
    v_mode:='coordination';
    v_purpose:='operator_forced_coordination';
  else
    raise exception 'unsupported forced role %. Expected researcher, isolated_researcher, auditor, or coordinator.',coalesce(nullif(v_role,''),'<empty>');
  end if;

  if v_task is null then
    raise exception 'forced role requires an explicit task summary';
  end if;

  if length(v_task)>control_center.config_int('operator.max_task_chars') then
    raise exception 'forced-role task summary is too long (% chars; configured maximum %)',length(v_task),control_center.config_int('operator.max_task_chars');
  end if;

  if p_worker_id is not null and worker_retired_by_current_batch(p_worker_id) then
    raise exception 'worker % was retired by the current research-batch cutover; start a new forced-role worker with NULL worker_id',p_worker_id;
  end if;

  perform pg_advisory_xact_lock(hashtext((control_center.active_project()||'_assignment')));
  perform purge_ephemeral();

  select coalesce(array_agg(id order by first_ord),'{}'::text[])
  into v_targets
  from (
    select id,min(ord) as first_ord
    from unnest(coalesce(p_target_ids,'{}'::text[])) with ordinality u(id,ord)
    where nullif(btrim(coalesce(id,'')),'') is not null
    group by id
  ) q;

  if cardinality(v_targets)>control_center.config_int('assignment.max_target_ids') then
    raise exception 'forced role exceeds configured target_id maximum %',control_center.config_int('assignment.max_target_ids');
  end if;

  select t.id into v_bad
  from unnest(v_targets) t(id)
  where not exists(
    select 1 from objects o
    where o.id=t.id and o.trashed_at is null
  )
  limit 1;

  if v_bad is not null then
    raise exception 'forced-role target % is not a live object',v_bad;
  end if;

  -- Legacy parameter retained for wire compatibility only.
  v_focus:=null;

  if v_role='auditor' and cardinality(v_targets)>0 then
    select t.id into v_bad
    from unnest(v_targets) t(id)
    where is_substantive_author(t.id,v_worker)
    limit 1;
    if v_bad is not null then
      raise exception 'audit independence violation: worker % is a substantive author of target %',v_worker,v_bad;
    end if;

    select t.id into v_bad
    from unnest(v_targets) t(id)
    where exists(
      select 1 from claims c
      where c.mode='audit' and c.worker_id<>v_worker and c.expires_at>now()
        and t.id=any(c.target_ids)
    ) limit 1;
    if v_bad is not null then
      raise exception 'audit target % is already reserved by another live auditor',v_bad;
    end if;
  end if;

  select * into v_old
  from claims
  where worker_id=v_worker and expires_at>now()
  order by created_at desc
  limit 1
  for update;

  if v_old.claim_id is not null and v_old.exclusive_key like 'stage:%' then
    update stages
    set claimed_by_worker_id=null,claimable=true,updated_at=now()
    where stage_id=substr(v_old.exclusive_key,7)::bigint
      and claimed_by_worker_id=v_worker;
  end if;

  delete from presence where worker_id=v_worker;
  delete from claims where worker_id=v_worker;

  update runs
  set status='superseded',retired_at=coalesce(retired_at,now()),expires_at=now(),payload=coalesce(payload,'{}'::jsonb)||jsonb_build_object('superseded_at',now(),'supersession_reason','explicit_force_role'),updated_at=now()
  where worker_id=v_worker;

  select max_claims,claim_ttl_minutes into v_cap,v_ttl
  from settings where singleton;

  select count(*) into v_count
  from claims where expires_at>now();

  if v_count>=v_cap then
    raise exception 'PROJECT active claim cap % reached',v_cap;
  end if;

  insert into claims(
    worker_id,mode,purpose,target_ids,focus_id,exclusive_key,payload,
    need_key,need_generation,expires_at
  ) values (
    v_worker,v_mode,v_purpose,v_targets,null,null,
    jsonb_strip_nulls(jsonb_build_object(
      'operator_role_override',true,
      'isolation_phase',case when v_mode='isolated_research' then 'ingestion' else null end,
      'startup_dispatch_bypass',true,
      'forced_role',v_role,
      'external_task',v_task,
      'assignment_source','explicit_operator_assignment',
      'bypass_scope','ordinary_scheduler_dispatch_only',
      'replaced_claim_id',v_old.claim_id,
      'replaced_mode',v_old.mode,
      'replaced_purpose',v_old.purpose,
      'replaced_need_key',v_old.need_key,
      'replaced_need_generation',v_old.need_generation
    )),
    null,null,now()+make_interval(mins=>v_ttl)
  )
  returning claim_id into v_claim;

  perform sync_run_from_claim(v_worker,v_claim);

  -- Reuse canonical startup hydration after the role claim already exists.
  -- resume_or_assign_worker therefore renews this exact forced claim instead of dispatching.
  v_packet:=control_center.startup(v_worker);

  v_packet:=jsonb_set(
    v_packet,
    '{run_transition}',
    coalesce(v_packet->'run_transition','{}'::jsonb)
      || jsonb_strip_nulls(jsonb_build_object(
           'claim_id',v_claim,
           'forced_role',true,
           'scheduler_dispatch_bypassed',true,
           'replaced_claim_id',v_old.claim_id,
           'resumed',false,
           'assignment_changed',v_old.claim_id is not null,
            'reassigned',v_old.claim_id is not null
         )),
    true
  );

  return v_packet || jsonb_build_object(
    'role_override',jsonb_build_object(
      'active',true,
      'role',v_role,
      'mode',v_mode,
      'task',v_task,
      'target_ids',v_targets,
      'scheduler_dispatch_bypassed',true,
      'startup_context_hydrated',true,
      
      'continuation','Subsequent turns use sync(worker_id,last_seen_revision) normally.'
    )
  );
END
$function$

```

## frontier() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.frontier()
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare
  v_entries jsonb;
  v_count integer;
  v_root_path text;
begin
  perform control_center.active_project();

  select tree_path into v_root_path
  from objects
  where id=(select grand_theorem_id from state where singleton)
    and trashed_at is null;

  with visible as materialized (
    select
      o.*,
      (o.audit_status='pending') as is_pending,
      (
        o.support_status='blocked'
        or exists (
          select 1
          from edges fe
          join objects fo on fo.id=fe.from_id
          where fe.kind='fence'
            and fe.to_id=o.id
            and fo.trashed_at is null
            and fo.lifecycle_status='active'
            and fo.audit_status <> 'failed'
        )
      ) as is_obstructed
    from objects o
    where o.trashed_at is null
      and o.lifecycle_status='active'
      and o.audit_status <> 'failed'
      and o.object_type <> 'fence'
      and coalesce(o.attention,'available') <> 'hidden'
      and coalesce(o.support_status,'unchecked') <> 'blocked'
      and o.tree_path like v_root_path || '%'
      and not exists (
        select 1
        from objects h
        where h.atlas_hidden
          and h.trashed_at is null
          and o.tree_path like h.tree_path || '%'
      )
      and not exists (
        select 1
        from edges se
        join objects replacement on replacement.id=se.from_id
        where se.kind='supersedes'
          and se.to_id=o.id
          and coalesce(se.metadata->>'supersession_state','effective')='effective'
          and replacement.trashed_at is null
          and replacement.lifecycle_status='active'
          and replacement.audit_status <> 'failed'
      )
  ),
  leaves as materialized (
    select v.*
    from visible v
    where not exists (
      select 1
      from visible c
      where c.parent_id=v.id
    )
  )
  select
    coalesce(
      jsonb_agg(
        jsonb_strip_nulls(jsonb_build_object(
          'id',l.id,
          'parent_id',l.parent_id,
          'title',l.title,
          'summary',coalesce(nullif(btrim(l.simplified_statement),''),l.title),
          'category',coalesce(l.research_level,l.object_type),
          'mathematical_status',l.mathematical_status,
          'audit_status',l.audit_status,
          'support_status',l.support_status,
          'attention',l.attention,
          'pending',l.is_pending,
          'obstructed',l.is_obstructed,
          'atlas_height',l.atlas_height,
          'research_interface',l.research_interface
        ))
        order by
          case l.attention when 'focus' then 0 when 'available' then 1 else 2 end,
          (l.atlas_height is null),
          l.atlas_height desc nulls last,
          l.tree_path,
          l.id
      ),
      '[]'::jsonb
    ),
    count(*)::integer
  into v_entries,v_count
  from leaves l;

  return jsonb_build_object(
    'entries',v_entries,
    'frontier_count',v_count,
    'definition','Active theorem-facing terminal research objects that are visible for work: nonhidden, nonfailed, nonblocked, non-superseded leaves of the grand-theorem reasoning tree.',
    'repository_revision',(select revision from state where singleton),
    'note','Flat frontier only. After choosing an item, call ancestry() or simplified_ancestry() separately for route context.'
  );
end
$function$

```

## get_policy(p_policy_key text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.get_policy(p_policy_key text)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
begin
  PERFORM control_center.active_project();

  RETURN (
    select jsonb_build_object(
      'policy_key',policy_key,
      'mode',mode,
      'body',body,
      'config',config,
      'updated_at',updated_at
    )
    from control_center.policies
    where policy_key=p_policy_key
  );
end
$function$

```

## get_stage(p_worker_id bigint, p_stage_id bigint) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.get_stage(p_worker_id bigint, p_stage_id bigint)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$begin
  PERFORM control_center.active_project();
  
  RETURN (

  select to_jsonb(s) from stages s
   where s.stage_id=p_stage_id
     and (s.owner_worker_id=p_worker_id or s.claimed_by_worker_id=p_worker_id)
     and s.expires_at>now()

  );
end$function$

```

## head() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.head()
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$begin
  PERFORM control_center.active_project();
  
  RETURN (

  select jsonb_build_object(
    'architecture',control_center.active_project(),
    'state',to_jsonb(s),
    'needs',(select coalesce(jsonb_agg(to_jsonb(n) order by n.need_key),'[]'::jsonb) from needs n),
    'health',(select to_jsonb(h) from health_snapshot h where h.singleton),
    'active_claims',(select count(*) from claims where expires_at>now()),
    'active_stages',(select count(*) from stages where expires_at>now())
  )
  from state s where s.singleton

  );
end$function$

```

## health() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.health()
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_base jsonb;
begin
  PERFORM control_center.active_project();
  perform purge_ephemeral();
  v_base:=run_health_check();

  return v_base||jsonb_build_object(
    'reasoning',reasoning_health(),
    'bounds',assert_ephemeral_bounds(),
    'run_pool',run_pool_status(),
    'security',security_posture(),
    'architecture',architecture_posture()
  );
end
$function$

```

## health_check_audit_request_state() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.health_check_audit_request_state()
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
begin
  perform control_center.active_project();
  return jsonb_build_object(
    'count',(select count(*) from objects where trashed_at is null and audit_requested and not (
      audit_status='pending' or (audit_status='certified' and support_status='stale' and support_reason='logical_premise_math_changed'))),
    'items',coalesce((select jsonb_agg(jsonb_build_object(
      'id',id,'title',title,'audit_status',audit_status,'support_status',support_status,'support_reason',support_reason
    ) order by id) from objects where trashed_at is null and audit_requested and not (
      audit_status='pending' or (audit_status='certified' and support_status='stale' and support_reason='logical_premise_math_changed'))),'[]'::jsonb)
  );
end$function$

```

## health_check_certificate_integrity() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.health_check_certificate_integrity()
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
begin
  perform control_center.active_project();
  return (
    with bad as (
      select o.id,o.title,'missing_certificate'::text issue,
             o.math_version,o.audited_math_version,
             null::bigint certificate_math_version,null::bigint verifier_worker_id
      from objects o left join certificates c on c.object_id=o.id
      where o.trashed_at is null and o.audit_status='certified' and c.object_id is null
      union all
      select o.id,o.title,'math_version_mismatch',o.math_version,o.audited_math_version,
             c.math_version,c.verifier_worker_id
      from objects o join certificates c on c.object_id=o.id
      where o.trashed_at is null and o.audit_status='certified'
        and (o.audited_math_version is distinct from o.math_version or c.math_version is distinct from o.math_version)
      union all
      select o.id,o.title,'verifier_is_substantive_author',o.math_version,o.audited_math_version,
             c.math_version,c.verifier_worker_id
      from objects o join certificates c on c.object_id=o.id
      where o.trashed_at is null and control_center.is_substantive_author(o.id,c.verifier_worker_id)
    )
    select jsonb_build_object('count',count(*),
      'items',coalesce(jsonb_agg(to_jsonb(bad) order by issue,id),'[]'::jsonb))
    from bad
  );
end$function$

```

## health_check_client_create_grants() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.health_check_client_create_grants()
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare p text:=control_center.active_project();
begin
  return (
    with bad as (
      select case when x.grantee=0 then 'PUBLIC' else r.rolname end as grantee,
             x.privilege_type,p as schema_name
      from pg_namespace n
      cross join lateral aclexplode(coalesce(n.nspacl,acldefault('n',n.nspowner))) x
      left join pg_roles r on r.oid=x.grantee
      where n.nspname=p and x.privilege_type='CREATE'
        and (case when x.grantee=0 then 'PUBLIC' else r.rolname end)
            in ('PUBLIC','anon','authenticated','service_role')
    )
    select jsonb_build_object('count',count(*),
      'items',coalesce(jsonb_agg(to_jsonb(bad) order by grantee),'[]'::jsonb))
    from bad
  );
end$function$

```

## health_check_live_project_state() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.health_check_live_project_state()
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
begin
  perform control_center.active_project();
  return (
    select jsonb_build_object(
      'count',case when phase<>'architecture_only' and grand_theorem_id is null then 1 else 0 end,
      'items',case when phase<>'architecture_only' and grand_theorem_id is null
                   then jsonb_build_array(jsonb_build_object('phase',phase,'grand_theorem_id',grand_theorem_id))
                   else '[]'::jsonb end)
    from state where singleton
  );
end$function$

```

## health_check_managed_ddl_guards() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.health_check_managed_ddl_guards()
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
begin
  perform control_center.active_project();
  return (
    with expected(name) as (values ('managed_project_function_ddl_guard'::text),('managed_project_function_drop_guard'::text)),
    bad as (
      select e.name as expected_event_trigger,
             t.evtname as actual_event_trigger,
             t.evtenabled
      from expected e
      left join pg_event_trigger t on t.evtname=e.name and t.evtenabled in ('O','A')
      where t.evtname is null
    )
    select jsonb_build_object('count',count(*),
      'items',coalesce(jsonb_agg(to_jsonb(bad) order by expected_event_trigger),'[]'::jsonb))
    from bad
  );
end$function$

```

## health_check_noncanonical_logical_edges() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.health_check_noncanonical_logical_edges()
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
begin
  perform control_center.active_project();
  return jsonb_build_object(
    'count',(select count(*) from edges where kind='proof'),
    'items',coalesce((select jsonb_agg(jsonb_build_object('from_id',from_id,'to_id',to_id,'kind',kind,'metadata',metadata)
                                       order by from_id,to_id)
                      from edges where kind='proof'),'[]'::jsonb)
  );
end$function$

```

## health_check_project_triggers() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.health_check_project_triggers()
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare p text:=control_center.active_project();
begin
  return (
    with bad as (
      select t.tgname as trigger_name,c.relname as table_name,
             fn.nspname as function_schema,f.proname as function_name
      from pg_trigger t
      join pg_class c on c.oid=t.tgrelid
      join pg_namespace n on n.oid=c.relnamespace
      join pg_proc f on f.oid=t.tgfoid
      join pg_namespace fn on fn.oid=f.pronamespace
      where not t.tgisinternal and n.nspname=p and fn.nspname<>'control_center'
    )
    select jsonb_build_object('count',count(*),
      'items',coalesce(jsonb_agg(to_jsonb(bad) order by table_name,trigger_name),'[]'::jsonb))
    from bad
  );
end$function$

```

## health_check_project_wrappers() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.health_check_project_wrappers()
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare p text:=control_center.active_project();
begin
  return (
    with bad as (
      select pr.proname as function_name,
             pg_get_function_identity_arguments(pr.oid) as identity_arguments,
             pg_get_function_result(pr.oid) as result_type
      from pg_proc pr join pg_namespace n on n.oid=pr.pronamespace
      where n.nspname=p and pr.prokind='f'
        and not control_center.is_valid_project_wrapper(pr.oid,p)
    )
    select jsonb_build_object('count',count(*),
      'items',coalesce(jsonb_agg(to_jsonb(bad) order by function_name,identity_arguments),'[]'::jsonb))
    from bad
  );
end$function$

```

## health_check_reasoning_tree_integrity() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.health_check_reasoning_tree_integrity()
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare d jsonb;
begin
  perform control_center.active_project();
  d:=control_center.reasoning_diagnostics(control_center.config_int('reasoning.integrity_check_limit'));
  return jsonb_build_object(
    'count',coalesce((d#>>'{invalid_parent_semantics,count}')::int,0),
    'items',coalesce(d#>'{invalid_parent_semantics,items}','[]'::jsonb)
  );
end$function$

```

## health_check_research_level_missing() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.health_check_research_level_missing()
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
begin
  perform control_center.active_project();
  return jsonb_build_object(
    'count',(select count(*) from objects where trashed_at is null and object_type='research' and mathematical_status is not null and research_level is null),
    'items',coalesce((select jsonb_agg(jsonb_build_object('id',id,'title',title,'mathematical_status',mathematical_status) order by id)
                      from objects where trashed_at is null and object_type='research' and mathematical_status is not null and research_level is null),'[]'::jsonb)
  );
end$function$

```

## health_check_rpc_contract() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.health_check_rpc_contract()
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare p text:=control_center.active_project();
begin
  return (
    with bad as (
      select 'missing_wrapper'::text issue,c.rpc_name,c.identity_arguments,c.result_type
      from control_center.public_rpc_contract c
      where not exists (
        select 1 from pg_proc pr join pg_namespace pn on pn.oid=pr.pronamespace
        where pn.nspname=p and pr.prokind='f'
          and pr.proname=c.rpc_name
          and pg_get_function_identity_arguments(pr.oid)=c.identity_arguments
          and pg_get_function_result(pr.oid)=c.result_type
          and control_center.is_valid_project_wrapper(pr.oid,p)
      )
      union all
      select 'extra_wrapper'::text,pr.proname,
             pg_get_function_identity_arguments(pr.oid),
             pg_get_function_result(pr.oid)
      from pg_proc pr join pg_namespace pn on pn.oid=pr.pronamespace
      where pn.nspname=p and pr.prokind='f'
        and control_center.is_valid_project_wrapper(pr.oid,p)
        and not exists (
          select 1 from control_center.public_rpc_contract c
          where c.rpc_name=pr.proname
            and c.identity_arguments=pg_get_function_identity_arguments(pr.oid)
            and c.result_type=pg_get_function_result(pr.oid)
        )
    )
    select jsonb_build_object('count',count(*),
      'items',coalesce(jsonb_agg(to_jsonb(bad) order by issue,rpc_name,identity_arguments),'[]'::jsonb))
    from bad
  );
end$function$

```

## health_check_startup_size() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.health_check_startup_size()
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare lim int;
begin
  perform control_center.active_project();
  select startup_warning_chars into lim from settings where singleton;
  return (
    with rows as (
      select policy_key,length(body) chars from policies
      where policy_key='worker_kernel' or policy_key like 'mode_%'
    ), calc as (
      select coalesce(max(chars) filter(where policy_key like 'mode_%'),0) max_mode_chars,
             coalesce(max(chars) filter(where policy_key='worker_kernel'),0) kernel_chars
      from rows
    )
    select jsonb_build_object(
      'count',case when kernel_chars+max_mode_chars>lim then 1 else 0 end,
      'items',case when kernel_chars+max_mode_chars>lim
        then (select coalesce(jsonb_agg(jsonb_build_object('policy_key',policy_key,'chars',chars,'warning_chars',lim)
                                        order by policy_key),'[]'::jsonb) from rows)
        else '[]'::jsonb end)
    from calc
  );
end$function$

```

## health_check_support_integrity() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.health_check_support_integrity()
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
begin
  perform control_center.active_project();
  return (
    with bad as (
      select o.id,o.title,'stored_status_mismatch'::text issue,
             o.support_status stored_support_status,
             control_center.compute_support_status(o.id)->>'status' computed_support_status,
             null::text premise_id
      from objects o
      where o.trashed_at is null and o.mathematical_status in ('proved','evidence')
        and o.support_status is distinct from (control_center.compute_support_status(o.id)->>'status')
      union all
      select distinct c.id,c.title,'supported_with_bad_direct_premise',
             c.support_status,null::text,p.id
      from objects c
      join edges e on e.from_id=c.id and e.kind='depends_on'
      join objects p on p.id=e.to_id and p.trashed_at is null
      where c.trashed_at is null and c.support_status='supported'
        and (p.mathematical_status<>'proved' or p.audit_status<>'certified' or p.support_status<>'supported')
    )
    select jsonb_build_object('count',count(*),
      'items',coalesce(jsonb_agg(to_jsonb(bad) order by issue,id,premise_id),'[]'::jsonb))
    from bad
  );
end$function$

```

## health_check_unguarded_stateful_control_functions() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.health_check_unguarded_stateful_control_functions()
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
begin
  perform control_center.active_project();
  return (
    with bad as (
      select p.proname as function_name,
             pg_get_function_identity_arguments(p.oid) as identity_arguments,
             p.provolatile as volatility,
             p.prolang::regproc::text as language
      from pg_proc p
      join pg_namespace n on n.oid=p.pronamespace
      where n.nspname='control_center'
        and p.prokind='f'
        and p.prorettype<>'trigger'::regtype
        and p.provolatile='v'
        and not control_center.config_json_array_contains(
              'architecture.cross_project_admin_functions',p.proname
            )
        and p.prosrc !~* 'active_project[[:space:]]*[(]'
        and p.prosrc !~* 'activate_project[[:space:]]*[(]'
    )
    select jsonb_build_object('count',count(*),
      'items',coalesce(jsonb_agg(to_jsonb(bad) order by function_name,identity_arguments),'[]'::jsonb))
    from bad
  );
end$function$

```

## health_checks() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.health_checks()
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
begin
  perform control_center.active_project();
  return jsonb_build_object(
    'research_level_missing',control_center.health_check_research_level_missing(),
    'certificate_integrity',control_center.health_check_certificate_integrity(),
    'support_integrity',control_center.health_check_support_integrity(),
    'audit_request_state',control_center.health_check_audit_request_state(),
    'noncanonical_logical_edges',control_center.health_check_noncanonical_logical_edges(),
    'reasoning_tree_integrity',control_center.health_check_reasoning_tree_integrity(),
    'unplaced_research_roots',control_center.health_check_unplaced_research_roots(),
    'live_project_state',control_center.health_check_live_project_state(),
    'managed_ddl_guards',control_center.health_check_managed_ddl_guards(),
    'startup_size',control_center.health_check_startup_size(),
    'project_wrappers',control_center.health_check_project_wrappers(),
    'rpc_contract',control_center.health_check_rpc_contract(),
    'project_triggers',control_center.health_check_project_triggers(),
    'client_create_grants',control_center.health_check_client_create_grants(),
    'unguarded_stateful_control_functions',control_center.health_check_unguarded_stateful_control_functions(),
    'project_schema_contract',control_center.health_check_project_schema_contract(),
    'active_unmapped_needs',control_center.health_check_active_unmapped_needs()
  );
end
$function$

```

## help(p_topic text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.help(p_topic text)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
BEGIN
  PERFORM control_center.active_project();
  RETURN control_center.help_core(p_topic);
END
$function$

```

## help_core(p_topic text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.help_core(p_topic text)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
DECLARE
  v_topic text:=lower(replace(btrim(coalesce(p_topic,'')),' ','_'));
  v_alias text;
  v_key text;
  v_result jsonb;
BEGIN
  PERFORM control_center.active_project();

  IF v_topic='' OR v_topic='index' THEN
    RETURN jsonb_build_object(
      'topics',(
        SELECT coalesce(jsonb_agg(replace(policy_key,'help_','') ORDER BY policy_key),'[]'::jsonb)
        FROM policies WHERE policy_key LIKE 'help_%'
      ),
      'note','Help is descriptive documentation only; it does not select a research route. Use rpc_signatures(name) for exact signatures.'
    );
  END IF;

  v_alias:=CASE v_topic
    WHEN 'request' THEN 'requests'
    WHEN 'steering' THEN 'requests'
    WHEN 'role' THEN 'role_override'
    WHEN 'roles' THEN 'role_override'
    WHEN 'force_role' THEN 'role_override'
    WHEN 'dependencies' THEN 'navigation'
    WHEN 'relations' THEN 'navigation'
    WHEN 'publication' THEN 'staging'
    WHEN 'publish' THEN 'staging'
    WHEN 'stage' THEN 'staging'
    WHEN 'leases' THEN 'lifecycle'
    WHEN 'continue' THEN 'lifecycle'
    WHEN 'solver' THEN 'computation'
    WHEN 'sat' THEN 'computation'
    WHEN 'milp' THEN 'computation'
    WHEN 'enumeration' THEN 'computation'
    WHEN 'api' THEN 'api_modification'
    WHEN 'api_changes' THEN 'api_modification'
    WHEN 'rpc_modification' THEN 'api_modification'
    ELSE v_topic
  END;

  v_key:='help_'||v_alias;
  SELECT jsonb_build_object(
    'topic',v_alias,'requested_topic',v_topic,'aliased',v_alias<>v_topic,
    'body',body,'updated_at',updated_at
  ) INTO v_result
  FROM policies WHERE policy_key=v_key;

  IF v_result IS NOT NULL THEN RETURN v_result; END IF;

  RETURN jsonb_build_object(
    'topic',v_topic,'found',false,
    'index',control_center.active_project()||'.help(NULL)'
  );
END
$function$

```

## initialize_project(p_worker_id bigint, p_initialization jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.initialize_project(p_worker_id bigint, p_initialization jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$begin
  PERFORM control_center.active_project();
  
  RETURN (

  select initialize_project_from_assignment(p_worker_id,p_initialization)

  );
end$function$

```

## list_polls(p_status text DEFAULT NULL::text, p_limit integer DEFAULT 20) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.list_polls(p_status text DEFAULT NULL::text, p_limit integer DEFAULT 20)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
DECLARE
  v_limit integer:=greatest(1,least(control_center.config_int('poll.list_max_limit'),coalesce(p_limit,control_center.config_int('poll.list_default_limit'))));
BEGIN
  PERFORM control_center.active_project();

  IF p_status IS NOT NULL
     AND p_status NOT IN ('open','passed_pending_action','rejected','enacted') THEN
    RAISE EXCEPTION 'invalid poll status %',p_status;
  END IF;

  RETURN coalesce((
    SELECT jsonb_agg(control_center.poll_status(q.poll_id) ORDER BY q.created_at DESC)
    FROM (
      SELECT poll_id,created_at
      FROM polls
      WHERE p_status IS NULL OR status=p_status
      ORDER BY created_at DESC
      LIMIT v_limit
    ) q
  ),'[]'::jsonb);
END
$function$

```

## local_audit_edge_repair(p_worker_id bigint, p_from_id text, p_to_id text, p_kind text, p_action text DEFAULT 'add'::text, p_metadata jsonb DEFAULT '{}'::jsonb, p_reason text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.local_audit_edge_repair(p_worker_id bigint, p_from_id text, p_to_id text, p_kind text, p_action text DEFAULT 'add'::text, p_metadata jsonb DEFAULT '{}'::jsonb, p_reason text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_kind text:=case when p_kind='proof' then 'depends_on' else p_kind end;
  v_claim record;
  v_snapshot jsonb;
  v_snap record;
  v_from record;
  v_rev bigint;
begin
  PERFORM control_center.active_project();
  
  if v_kind<>'depends_on' then
    raise exception 'localized audit edge repair is only for logical depends_on edges';
  end if;
  if p_action not in ('add','remove') then raise exception 'action must be add or remove'; end if;
  if p_reason is null or btrim(p_reason)='' then
    raise exception 'localized audit edge repair requires a reason';
  end if;

  select * into v_claim from claims c
   where c.worker_id=p_worker_id
     
     and p_from_id=any(c.target_ids)
     and c.expires_at>now()
   order by c.created_at desc limit 1;

  if v_claim.claim_id is null then
    raise exception 'localized audit edge repair requires an active claim covering %',p_from_id;
  end if;

  v_snapshot:=audit_snapshot_state(v_claim.claim_id,p_from_id);
  if not coalesce((v_snapshot->>'current')::boolean,false) then
    raise exception 'localized audit edge repair requires a current audit snapshot for %',p_from_id;
  end if;

  select * into v_snap from audit_snapshots
   where claim_id=v_claim.claim_id
     and target_id=p_from_id
     and expires_at>now();

  select * into v_from from objects
   where id=p_from_id and trashed_at is null for update;
  if v_from.id is null then raise exception 'from object % not found',p_from_id; end if;

  if is_substantive_author(p_from_id,p_worker_id) then
    raise exception 'self-audit barrier: worker % is already a substantive author of %',
      p_worker_id,p_from_id;
  end if;

  if not exists(
    select 1 from objects where id=p_to_id and trashed_at is null
  ) then
    raise exception 'to object % not found',p_to_id;
  end if;

  if p_action='add' then
    if not (v_snap.watched_math_versions ? p_to_id) then
      raise exception 'new audit premise % must be explicitly watched; reopen the shared audit batch including it',p_to_id;
    end if;

    if logical_cycle_if_added(p_from_id,p_to_id) then
      raise exception 'logical dependency cycle rejected: % -> %',p_from_id,p_to_id;
    end if;

    insert into edges(from_id,to_id,kind,metadata)
    values(p_from_id,p_to_id,'depends_on',coalesce(p_metadata,'{}'::jsonb))
    on conflict(from_id,to_id,kind) do update set metadata=excluded.metadata;
  else
    delete from edges
     where from_id=p_from_id and to_id=p_to_id and kind='depends_on';
    if not found then raise exception 'logical edge not found'; end if;
  end if;

  update objects
     set math_version=math_version+1,
         audit_status='pending',
         audited_math_version=null,
         audit_requested=true,
         support_status=case when mathematical_status='evidence'
           then 'evidence' else 'unchecked' end,
         support_reason='localized audit dependency repair awaiting recertification',
         metadata=metadata||jsonb_build_object(
           'last_local_audit_dependency_repair',
           jsonb_build_object(
             'reason',p_reason,'worker_id',p_worker_id,
             'action',p_action,'to_id',p_to_id,'kind','depends_on',
             'recorded_at',now()
           )
         ),
         version=version+1,
         updated_at=now()
   where id=p_from_id
   returning * into v_from;

  delete from certificates where object_id=p_from_id;
  perform invalidate_dependents(
    array[p_from_id],'audited logical dependency set changed'
  );

  v_rev:=record_change(
    'local_audit_dependency_repair',array[p_from_id,p_to_id],
    jsonb_build_object(
      'reason',p_reason,'worker_id',p_worker_id,'action',p_action,
      'kind','depends_on','math_version',v_from.math_version
    )
  );

  return to_jsonb(v_from)||jsonb_build_object(
    'repository_revision',v_rev,
    'note','Mathematical dependency repair invalidated the shared audit basis; reopen the whole audit batch before batch submission.'
  );
end
$function$

```

## local_audit_repair(p_worker_id bigint, p_id text, p_expected_version bigint, p_patch jsonb, p_reason text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.local_audit_repair(p_worker_id bigint, p_id text, p_expected_version bigint, p_patch jsonb, p_reason text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_has_claim boolean; v_row record; v_math_changed boolean; v_new_metadata jsonb; v_rev bigint;
begin
  perform control_center.active_project();
  select exists(select 1 from claims c where c.worker_id=p_worker_id and p_id=any(c.target_ids) and c.expires_at>now())
    into v_has_claim;
  if not v_has_claim then raise exception 'localized audit repair requires an active claim covering %',p_id; end if;
  if jsonb_typeof(coalesce(p_patch,'{}'::jsonb))<>'object' then raise exception 'patch must be an object'; end if;
  if p_patch ? 'mathematical_status' or p_patch ? 'research_level' or p_patch ? 'lifecycle_status' then
    raise exception 'status/scope reclassification is not an audit repair';
  end if;
  if p_reason is null or btrim(p_reason)='' then raise exception 'audit repair requires a reason'; end if;

  select * into v_row from objects where id=p_id and trashed_at is null for update;
  if v_row.id is null then raise exception 'object % not found',p_id; end if;
  if v_row.version<>p_expected_version then raise exception 'version conflict on %',p_id; end if;
  if is_substantive_author(p_id,p_worker_id) then
    raise exception 'self-audit barrier: worker % is already a substantive author of %',p_worker_id,p_id;
  end if;

  v_math_changed:=p_patch ? 'statement' or p_patch ? 'body';
  v_new_metadata:=case when p_patch ? 'metadata'
    then coalesce(p_patch->'metadata','{}'::jsonb) else v_row.metadata end;
  v_new_metadata:=v_new_metadata||jsonb_build_object(
    'audit_work_kind','repair_validation',
    'last_local_audit_repair',jsonb_build_object(
      'reason',p_reason,'worker_id',p_worker_id,'recorded_at',now(),
      'audit_repair_authorized',true,
      'body_overhaul_permitted',true,
      'statement_change_policy','small_local_tweak_only_policy_enforced'));

  update objects
     set title=case when p_patch ? 'title' then p_patch->>'title' else title end,
         statement=case when p_patch ? 'statement' then nullif(p_patch->>'statement','') else statement end,
         body=case when p_patch ? 'body' then coalesce(p_patch->>'body','') else body end,
         metadata=v_new_metadata,
         research_interface=case when p_patch ? 'research_interface' then coalesce(p_patch->'research_interface','{}'::jsonb) else research_interface end,
         math_version=math_version+case when v_math_changed then 1 else 0 end,
         audit_status='pending',audited_math_version=null,audit_requested=true,
         support_status=case when mathematical_status='evidence' then 'evidence' else 'unchecked' end,
         support_reason='audit repair awaiting validation',
         version=version+1,updated_at=now()
   where id=p_id returning * into v_row;

  delete from certificates where object_id=p_id;
  if v_math_changed then perform invalidate_dependents(array[p_id],'audited premise text changed'); end if;

  v_rev:=record_change('local_audit_repair',array[p_id],
    jsonb_build_object('reason',p_reason,'worker_id',p_worker_id,'math_version',v_row.math_version,
      'statement_tweak',p_patch ? 'statement','body_rewrite',p_patch ? 'body'));
  return to_jsonb(v_row)||jsonb_build_object(
    'repository_revision',v_rev,
    'note','Audit repair applied. Statement-smallness is policy-enforced, not syntactically gated. Reopen the shared audit basis before PASS_ADJUSTED.');
end
$function$

```

## mark_proof_node(p_worker_id bigint, p_object_id text, p_node_kind text, p_route_key text DEFAULT NULL::text, p_note text DEFAULT ''::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.mark_proof_node(p_worker_id bigint, p_object_id text, p_node_kind text, p_route_key text DEFAULT NULL::text, p_note text DEFAULT ''::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
begin
  PERFORM control_center.active_project();
  if p_node_kind='spine_root' then p_node_kind:='root'; end if;
  return control_center.mark_reasoning_node(
    p_worker_id,p_object_id,p_node_kind,p_route_key,p_note
  );
end
$function$

```

## mark_reasoning_node(p_worker_id bigint, p_object_id text, p_node_kind text, p_route_key text DEFAULT NULL::text, p_note text DEFAULT ''::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.mark_reasoning_node(p_worker_id bigint, p_object_id text, p_node_kind text, p_route_key text DEFAULT NULL::text, p_note text DEFAULT ''::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_rev bigint;
  v_row record;
begin
  PERFORM control_center.active_project();
  if p_node_kind not in ('root','step','branch') then
    raise exception 'invalid reasoning node kind %',p_node_kind;
  end if;
  perform require_math_principal(p_worker_id);
  perform validate_reasoning_node(p_object_id,p_node_kind);

  perform 1 from objects
   where id=p_object_id and trashed_at is null
   for update;

  insert into reasoning_nodes(object_id,node_kind,route_key,note,updated_at)
  values(p_object_id,p_node_kind,nullif(p_route_key,''),coalesce(p_note,''),now())
  on conflict(object_id) do update set
    node_kind=excluded.node_kind,
    route_key=excluded.route_key,
    note=excluded.note,
    updated_at=now()
  returning * into v_row;

  update objects set version=version+1,updated_at=now()
   where id=p_object_id;

  v_rev:=record_change(
    'mark_reasoning_node',array[p_object_id],
    jsonb_build_object('node_kind',p_node_kind,'route_key',p_route_key)
  );

  return to_jsonb(v_row)||jsonb_build_object(
    'object_version',(select version from objects where id=p_object_id),
    'repository_revision',v_rev
  );
end
$function$

```

## mark_route_relation(p_worker_id bigint, p_older_id text, p_newer_id text, p_relation text DEFAULT 'bypassed_by'::text, p_note text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.mark_route_relation(p_worker_id bigint, p_older_id text, p_newer_id text, p_relation text DEFAULT 'bypassed_by'::text, p_note text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
begin
  PERFORM control_center.active_project();
  
  if p_relation not in ('bypassed_by','subsumed_by') then
    raise exception 'relation must be bypassed_by or subsumed_by';
  end if;

  return control_center.add_edge(
    p_worker_id,p_older_id,p_newer_id,p_relation,
    jsonb_strip_nulls(jsonb_build_object('note',p_note))
  );
end
$function$

```

## migration_preflight() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.migration_preflight()
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_health jsonb;
  v_bounds jsonb;
  v_security jsonb;
  v_hard integer;
  v_phase text;
  v_reasoning_hard integer;
  v_exposed_rpc_count integer;
  v_arch integer;
  v_accept record;
  v_static_pass boolean;
  v_functional_pass boolean;
begin
  PERFORM control_center.active_project();
  
  v_health:=run_health_check();
  v_bounds:=assert_ephemeral_bounds();
  v_security:=security_posture();

  select phase into v_phase from state where singleton;
  select architecture_version into v_arch from settings where singleton;
  select * into v_accept from acceptance_status where singleton;

  select count(*) into v_hard
  from jsonb_array_elements(v_health->'alerts') a
  where coalesce((a->>'severity')::int,0)>=4;

  v_reasoning_hard:=jsonb_object_count(
    v_health->'reasoning'->'hard_alerts'
  );

  select count(*) into v_exposed_rpc_count
  from pg_proc p
  join pg_namespace n on n.oid=p.pronamespace
  where n.nspname='public'
    and p.proname like '%'
    and (
      has_function_privilege('anon',p.oid,'EXECUTE')
      or has_function_privilege('authenticated',p.oid,'EXECUTE')
      or has_function_privilege('public',p.oid,'EXECUTE')
    );

  v_static_pass:=
    v_phase='architecture_only'
    and v_hard=0
    and v_reasoning_hard=0
    and v_exposed_rpc_count=0
    and coalesce((v_security->>'ok')::boolean,false);

  v_functional_pass:=
    v_accept.singleton
    and v_accept.architecture_version=v_arch
    and v_accept.passed
    and v_accept.tested_at is not null;

  return jsonb_build_object(
    'architecture_version',v_arch,
    'phase',v_phase,
    'static_preflight_pass',v_static_pass,
    'functional_acceptance_pass',v_functional_pass,
    'ready_for_migration',v_static_pass and v_functional_pass,
    'ready_for_import',v_static_pass and v_functional_pass,
    'hard_alert_count',v_hard,
    'reasoning_hard_alert_count',v_reasoning_hard,
    'externally_exposed_rpc_count',v_exposed_rpc_count,
    'security_posture',v_security,
    'functional_acceptance',case
      when v_accept.singleton then jsonb_build_object(
        'architecture_version',v_accept.architecture_version,
        'suite_name',v_accept.suite_name,
        'passed',v_accept.passed,
        'tested_at',v_accept.tested_at,
        'details',v_accept.details
      ) else null end,
    'preflight_scope',
      'Static checks are executed now. Functional acceptance is NOT executed by preflight; it is the single latest recorded rollback regression suite for this exact architecture version.',
    'rpc_access_model',
      'A managed project schema is an RPC-only internal schema: all local tables require RLS, direct client schema/table grants are forbidden, and public wrapper functions must remain postgres-owned SECURITY DEFINER with pinned search_path.',
    'health',v_health,
    'bounds',v_bounds,
    'acceptance_contract',jsonb_build_array(
      'Exact current claims/statements and hypotheses survive.',
      'Logical premise edges survive as acyclic canonical depends_on relations.',
      'Audit certificates transfer only when exact checked math version, verifier independence, and premise basis can be preserved.',
      'Counterexamples, fences, aliases, supersession, and research-influence links survive.',
      'Nested reasoning navigation and distinct live compositions survive without duplicating mathematical truth.',
      'Project state is rebuilt conservatively from migrated mathematics before activation.',
      'Post-import health and frontier evidence contain no hard trust inconsistency before leaving architecture_only.',
      'No PROJECT RPC is executable through PUBLIC, anon, or authenticated database roles.',
      'Every managed-project table has RLS enabled with no direct client policies or client grants; thin project RPC wrappers are the only supported client access boundary.',
      'Functional regression acceptance is current for the exact architecture version.'
    )
  );
end
$function$

```

## move_object(p_worker_id bigint, p_id text, p_expected_version bigint, p_new_parent_id text DEFAULT NULL::text, p_new_position bigint DEFAULT 0) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.move_object(p_worker_id bigint, p_id text, p_expected_version bigint, p_new_parent_id text DEFAULT NULL::text, p_new_position bigint DEFAULT 0)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_old_path text;
  v_parent_path text;
  v_new_path text;
  v_current bigint;
  v_count integer;
  v_rev bigint;
begin
  PERFORM control_center.active_project();
  
  perform pg_advisory_xact_lock(hashtext((control_center.active_project()||'_tree')));

  select tree_path,version into v_old_path,v_current
    from objects
   where id=p_id and trashed_at is null
   for update;

  if v_old_path is null then raise exception 'object % not found',p_id; end if;
  if v_current<>p_expected_version then raise exception 'version conflict on %',p_id; end if;

  if p_new_parent_id is not null then
    select tree_path into v_parent_path
      from objects
     where id=p_new_parent_id and trashed_at is null
     for share;
    if v_parent_path is null then raise exception 'new parent % not found',p_new_parent_id; end if;
    if v_parent_path like v_old_path||'%' then
      raise exception 'cannot move object beneath its own subtree';
    end if;
    v_new_path:=v_parent_path||p_id||'/';
  else
    v_new_path:=p_id||'/';
  end if;

  update objects
     set tree_path=v_new_path||substr(tree_path,length(v_old_path)+1),
         parent_id=case when id=p_id then p_new_parent_id else parent_id end,
         position=case when id=p_id then greatest(0,p_new_position) else position end,
         version=version+1,
         updated_at=now()
   where trashed_at is null and tree_path like v_old_path||'%';
  get diagnostics v_count=row_count;

  v_rev:=record_change(
    'move_subtree',array[p_id],
    jsonb_build_object(
      'new_parent_id',p_new_parent_id,
      'descendants_touched',greatest(0,v_count-1)
    )
  );

  return jsonb_build_object(
    'id',p_id,'new_parent_id',p_new_parent_id,
    'objects_touched',v_count,'repository_revision',v_rev
  );
end
$function$

```

## next(p_worker_id bigint, p_outcome text DEFAULT NULL::text, p_details jsonb DEFAULT '{}'::jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.next(p_worker_id bigint, p_outcome text DEFAULT NULL::text, p_details jsonb DEFAULT '{}'::jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_claim record;
  v_outcome text;
  v_packet jsonb;
begin
  perform control_center.active_project();

  select * into v_claim
  from claims
  where worker_id=p_worker_id and expires_at>now()
  order by created_at desc
  limit 1;

  -- Ordinary heartbeat/refresh path. If an assignment already exists and
  -- the worker gives no outcome, next() behaves as sync().
  if v_claim.claim_id is not null
     and nullif(btrim(coalesce(p_outcome,'')),'') is null
  then
    v_packet := control_center.sync(p_worker_id,null,false);
    return v_packet || jsonb_build_object(
      'next_reminder','add outcome or DEFER to get next assignment'
    );
  end if;

  -- First ordinary next(): there is nothing to close, so simply dispatch.
  if v_claim.claim_id is null
     and nullif(btrim(coalesce(p_outcome,'')),'') is null
  then
    return control_center.next_core(p_worker_id,'completed',coalesce(p_details,'{}'::jsonb));
  end if;

  v_outcome := lower(btrim(p_outcome));
  if v_outcome='defer' then
    v_outcome:='deferred';
  end if;

  return control_center.next_core(
    p_worker_id,
    v_outcome,
    coalesce(p_details,'{}'::jsonb)
  );
end
$function$

```

## next(p_worker_id bigint, p_outcome text, p_details text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.next(p_worker_id bigint, p_outcome text, p_details text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
begin
  perform control_center.active_project();
  return control_center.next(
    p_worker_id,
    p_outcome,
    jsonb_build_object('summary',coalesce(p_details,''))
  );
end
$function$

```

## next_core(p_worker_id bigint, p_outcome text DEFAULT 'completed'::text, p_details jsonb DEFAULT '{}'::jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.next_core(p_worker_id bigint, p_outcome text DEFAULT 'completed'::text, p_details jsonb DEFAULT '{}'::jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_claim record;
  v_new_claim bigint;
  v_ack_outcome text;
  v_remaining text[];
  v_packet jsonb;
  v_digest text;
begin
  perform control_center.active_project();

  perform pg_advisory_xact_lock(
    hashtext((control_center.active_project()||'_transition:')||p_worker_id::text)
  );
  perform purge_transition_receipts();

  select * into v_claim
  from claims
  where worker_id=p_worker_id and expires_at>now()
  order by created_at desc
  limit 1
  for update;

  if v_claim.claim_id is not null then
    v_digest:=md5(
      coalesce(p_outcome,'completed')||E'\n'||
      coalesce(p_details,'{}'::jsonb)::text
    );

    if v_claim.mode='audit' and p_outcome='completed' then
      select coalesce(
        array_agg(o.id order by array_position(v_claim.target_ids,o.id)),
        '{}'::text[]
      )
      into v_remaining
      from objects o
      where o.id=any(v_claim.target_ids)
        and o.trashed_at is null
        and o.audit_requested
        and o.audit_status='pending'
        and o.mathematical_status in ('proved','evidence')
        and not is_substantive_author(o.id,p_worker_id);

      if cardinality(v_remaining)>0 then
        raise exception
          'audit batch still has unfinished eligible targets: %. Finish them, or use outcome deferred/blocked rather than completed.',
          v_remaining;
      end if;
    end if;

    if v_claim.mode='audit' and p_outcome in ('deferred','blocked') then
      update runs r
         set payload=jsonb_set(
           coalesce(r.payload,'{}'::jsonb),'{audit_deferred_ids}',
           to_jsonb(array(
             select distinct x from (
               select jsonb_array_elements_text(coalesce(r.payload->'audit_deferred_ids','[]'::jsonb)) as x
               union all
               select o.id
               from objects o
               where o.id=any(v_claim.target_ids)
                 and o.trashed_at is null
                 and o.audit_requested
                 and (o.audit_status='pending' or (
                   o.audit_status='certified' and o.support_status='stale' and o.support_reason='logical_premise_math_changed'))
                 and o.mathematical_status in ('proved','evidence')
             ) q order by x
           )),true
         ), updated_at=now()
       where r.worker_id=p_worker_id;
    end if;

    v_ack_outcome:=case
      when p_outcome in ('deferred','blocked','superseded') then p_outcome
      else 'completed'
    end;

    if v_claim.need_key='vote' then
      perform control_center.finish_vote_claim(
        p_worker_id,v_claim.payload,v_claim.created_at,p_outcome,p_details
      );
    elsif v_claim.need_key is not null
       and v_claim.need_generation is not null then
      perform control_center.finalize_scheduler_review(
        p_worker_id,
        v_claim.need_key,
        v_claim.need_generation,
        v_claim.created_at,
        v_claim.target_ids,
        p_outcome,
        v_ack_outcome,
        p_details
      );

      perform ack_need(
        v_claim.need_key,v_claim.need_generation,v_ack_outcome
      );
    end if;

    delete from presence
    where worker_id=p_worker_id;

    delete from claims
    where claim_id=v_claim.claim_id;

    update runs
    set status=case
          when v_ack_outcome in ('completed','superseded')
          then 'completed' else 'active'
        end,
        updated_at=now()
    where worker_id=p_worker_id;
  end if;

  perform run_health_check();
  v_new_claim:=assign_worker(p_worker_id);

  v_packet:=compact_transition_packet(
    p_worker_id,v_new_claim,p_outcome,v_claim.need_generation
  );

  v_packet:=v_packet||control_center.research_atlas_handoff(
    p_worker_id,
    (select mode from claims where claim_id=v_new_claim and worker_id=p_worker_id)
  );

  if v_claim.claim_id is not null then
    v_packet:=v_packet||jsonb_build_object(
      'transition_receipt',jsonb_build_object(
        'source_claim_id',v_claim.claim_id,
        'result_claim_id',v_new_claim,
        'retry',
          control_center.active_project()||'.next_retry(worker_id, source_claim_id)',
        'expires_at',now()+interval '1 hour'
      )
    );

    perform record_transition_receipt(
      v_claim.claim_id,p_worker_id,v_digest,
      coalesce(p_outcome,'completed'),v_new_claim,v_packet
    );
  end if;

  return v_packet;
end
$function$

```

## next_retry(p_worker_id bigint, p_source_claim_id bigint) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.next_retry(p_worker_id bigint, p_source_claim_id bigint)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  r record;
  v_current_claim bigint;
begin
  PERFORM control_center.active_project();
  
  perform purge_transition_receipts();

  select * into r
  from transition_receipts
  where source_claim_id=p_source_claim_id
    and worker_id=p_worker_id
    and expires_at>now();

  if r.source_claim_id is not null then
    return r.result_packet||jsonb_build_object(
      'idempotent_retry',true,
      'retry_of_claim_id',p_source_claim_id,
      'original_transition_revision',r.repository_revision,
      'receipt_expires_at',r.expires_at
    );
  end if;

  select claim_id into v_current_claim
  from claims
  where worker_id=p_worker_id and expires_at>now()
  order by created_at desc
  limit 1;

  if v_current_claim=p_source_claim_id then
    return jsonb_build_object(
      'idempotent_retry',false,
      'transition_applied',false,
      'source_claim_id',p_source_claim_id,
      'message',
        'That claim is still current, so no prior assignment transition was recorded. Use normal control_center.next(worker_id) when the assignment is actually complete.'
    );
  end if;

  return jsonb_build_object(
    'idempotent_retry',false,
    'transition_applied','unknown',
    'source_claim_id',p_source_claim_id,
    'receipt_found',false,
    'message',
      'No live transition receipt exists for that claim. It may be older than the one-hour retry window or may have been erased when the worker was retired. Do not infer that a transition should be replayed.'
  );
end
$function$

```

## open_audit_batch(p_worker_id bigint, p_additional_ids text[] DEFAULT '{}'::text[], p_content text DEFAULT 'math'::text, p_page_chars integer DEFAULT 12000) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.open_audit_batch(p_worker_id bigint, p_additional_ids text[] DEFAULT '{}'::text[], p_content text DEFAULT 'math'::text, p_page_chars integer DEFAULT 12000)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
DECLARE
  v_result jsonb;
  v_claim_id bigint;
  v_targets text[];
  v_versions jsonb;
  v_context jsonb;
begin
  PERFORM control_center.active_project();
  
  v_result := control_center.open_audit_batch_base_recomposition_equivalence(
    p_worker_id,p_additional_ids,p_content,p_page_chars
  );

  SELECT c.claim_id INTO v_claim_id
  FROM claims c
  WHERE c.worker_id=p_worker_id
    
    AND c.expires_at>now()
  ORDER BY c.created_at DESC
  LIMIT 1;

  SELECT coalesce(array_agg(s.target_id order by s.target_id),'{}'::text[])
    INTO v_targets
  FROM audit_snapshots s
  WHERE s.claim_id=v_claim_id
    AND s.worker_id=p_worker_id
    AND s.expires_at>now();

  v_versions:=recomposition_equivalence_source_versions(v_targets);
  v_context:=recomposition_equivalence_audit_context(v_targets);

  IF v_versions<>'{}'::jsonb THEN
    UPDATE audit_snapshots
    SET watched_math_versions=watched_math_versions||v_versions
    WHERE claim_id=v_claim_id
      AND worker_id=p_worker_id
      AND target_id=ANY(v_targets);
  END IF;

  v_result:=v_result||jsonb_build_object(
    'recomposition_equivalence_audit',v_context,
    'recomposition_source_math_versions',v_versions
  );

  IF v_result ? 'audit_batch' THEN
    v_result:=jsonb_set(
      v_result,
      '{audit_batch,snapshot_state}',
      audit_snapshot_state(v_claim_id),
      true
    );
  END IF;

  RETURN v_result;
END
$function$

```

## open_audit_batch_base_recomposition_equivalence(p_worker_id bigint, p_additional_ids text[] DEFAULT '{}'::text[], p_content text DEFAULT 'math'::text, p_page_chars integer DEFAULT 12000) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.open_audit_batch_base_recomposition_equivalence(p_worker_id bigint, p_additional_ids text[] DEFAULT '{}'::text[], p_content text DEFAULT 'math'::text, p_page_chars integer DEFAULT 12000)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_claim record;
  v_targets text[];
  v_ids text[];
  v_versions jsonb;
  v_receipt jsonb;
  v_receipt_versions jsonb;
  v_missing_ids text[];
  v_page jsonb;
  v_session bigint;
  v_done boolean;
  v_target text;
  v_basis bigint:=control_center.allocate_identity('operational_id');
begin
  PERFORM control_center.active_project();
  
  perform touch_worker_claim(p_worker_id);

  if p_content not in ('math','full') then
    raise exception 'audit batches require content=math or content=full';
  end if;

  select * into v_claim
  from claims c
  where c.worker_id=p_worker_id
    
    and c.expires_at>now()
  order by c.created_at desc
  limit 1
  for update;

  if v_claim.claim_id is null then
    raise exception 'active worker claim required';
  end if;

  select coalesce(array_agg(o.id order by array_position(v_claim.target_ids,o.id)),'{}'::text[])
    into v_targets
  from objects o
  where o.id=any(v_claim.target_ids)
    and o.trashed_at is null
    and o.audit_requested
    and (
      o.audit_status='pending'
      or (
        o.audit_status='certified'
        and o.support_status='stale'
        and o.support_reason='logical_premise_math_changed'
      )
    )
    and o.mathematical_status in ('proved','evidence');

  if cardinality(v_targets)=0 then
    raise exception 'audit claim has no remaining pending targets';
  end if;

  if exists(
    select 1 from unnest(v_targets) t(id)
    where is_substantive_author(t.id,p_worker_id)
  ) then
    raise exception 'shared audit batch contains a target authored substantively by this worker';
  end if;

  select array_agg(id order by ord,id)
    into v_ids
  from (
    select id,min(ord) ord
    from (
      select u.id,u.ord::integer as ord
      from unnest(v_targets) with ordinality u(id,ord)

      union all

      select e.to_id,
        1000 + case e.kind
          when 'depends_on' then 0
          when 'fence' then 100
          when 'interface' then 200
          else 300
        end
      from edges e
      where e.from_id=any(v_targets)
        and e.kind in ('depends_on','fence','interface','references')

      union all

      select x,2000
      from unnest(coalesce(p_additional_ids,'{}'::text[])) x
    ) raw
    where exists(
      select 1 from objects o
      where o.id=raw.id and o.trashed_at is null
    )
    group by id
  ) q;

  select coalesce(jsonb_object_agg(o.id,o.math_version),'{}'::jsonb)
    into v_versions
  from objects o
  where o.id=any(v_ids) and o.trashed_at is null;

  v_receipt:=read_receipt_manifest(p_worker_id,v_ids);
  v_receipt_versions:=coalesce(v_receipt->'covered_math_versions','{}'::jsonb);

  select coalesce(array_agg(value order by ord),'{}'::text[])
    into v_missing_ids
  from jsonb_array_elements_text(
    coalesce(v_receipt->'missing_ids','[]'::jsonb)
  ) with ordinality q(value,ord);

  if cardinality(v_missing_ids)=0 then
    v_session:=null;
    v_done:=true;
    v_page:=jsonb_build_object(
      'session_id',null,
      'items','[]'::jsonb,
      'done',true,
      'stale',false,
      'next_cursor',null,
      'receipt_reused',true,
      'reused_ids',v_receipt->'covered_ids',
      'missing_ids','[]'::jsonb
    );
  else
    v_page:=control_center.open_read_ex(
      p_worker_id,v_missing_ids,p_content,p_page_chars,
      case when p_content='full' then 'object' else 'math' end
    );

    v_session:=nullif(v_page->>'session_id','')::bigint;
    v_done:=coalesce((v_page->>'done')::boolean,false)
      and not coalesce((v_page->>'stale')::boolean,false);

    v_page:=v_page||jsonb_build_object(
      'receipt_reused',jsonb_array_length(coalesce(v_receipt->'covered_ids','[]'::jsonb))>0,
      'reused_ids',v_receipt->'covered_ids',
      'missing_ids',to_jsonb(v_missing_ids)
    );
  end if;

  delete from audit_snapshots
  where claim_id=v_claim.claim_id
    and not (target_id=any(v_targets));

  foreach v_target in array v_targets
  loop
    insert into audit_snapshots(
      claim_id,worker_id,target_id,target_math_version,premise_signature,
      watched_math_versions,read_session_id,read_completed_at,
      content_mode,expires_at,basis_id,receipt_math_versions
    ) values (
      v_claim.claim_id,p_worker_id,v_target,
      (select math_version from objects where id=v_target),
      premise_signature(v_target),
      v_versions,v_session,case when v_done then now() else null end,
      p_content,v_claim.expires_at,v_basis,v_receipt_versions
    )
    on conflict(claim_id,target_id) do update set
      worker_id=excluded.worker_id,
      target_math_version=excluded.target_math_version,
      premise_signature=excluded.premise_signature,
      watched_math_versions=excluded.watched_math_versions,
      read_session_id=excluded.read_session_id,
      read_completed_at=excluded.read_completed_at,
      content_mode=excluded.content_mode,
      basis_id=excluded.basis_id,
      receipt_math_versions=excluded.receipt_math_versions,
      created_at=now(),
      expires_at=excluded.expires_at;
  end loop;

  return v_page||jsonb_build_object(
    'audit_batch',jsonb_build_object(
      'claim_id',v_claim.claim_id,
      'basis_id',v_basis,
      'target_ids',v_targets,
      'target_count',cardinality(v_targets),
      'shared_watched_ids',v_ids,
      'reused_math_versions',v_receipt_versions,
      'reread_ids',to_jsonb(v_missing_ids),
      'shared_read_session_id',v_session,
      'snapshot_state',audit_snapshot_state(v_claim.claim_id)
    ),
    'audit_content_mode',p_content,
    'additional_watched_ids',coalesce(p_additional_ids,'{}'::text[]),
    'instruction',case
      when cardinality(v_missing_ids)=0
        then 'Every watched math version has a current fully-read receipt for this worker. No reread is required; reason from the retained exact-version basis and submit the batch decisions.'
      else 'Consume only the returned missing/changed mathematics completely. Previously fully-read exact versions are reused by receipt. Then submit all batch decisions once.'
    end
  );
end
$function$

```

## open_audit_batch_v2(p_worker_id bigint, p_additional_ids text[] DEFAULT '{}'::text[], p_content text DEFAULT 'math'::text, p_page_chars integer DEFAULT 12000) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.open_audit_batch_v2(p_worker_id bigint, p_additional_ids text[] DEFAULT '{}'::text[], p_content text DEFAULT 'math'::text, p_page_chars integer DEFAULT 12000)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_claim record;
  v_targets text[];
  v_impacts text[];
  v_extra text[];
  v_result jsonb;
  v_impact_detail jsonb;
begin
  PERFORM control_center.active_project();
  
  select * into v_claim
  from claims c
  where c.worker_id=p_worker_id
    
    and c.expires_at>now()
  order by c.created_at desc
  limit 1
  for update;

  if v_claim.claim_id is null then
    raise exception 'active worker claim required';
  end if;

  select coalesce(array_agg(o.id order by array_position(v_claim.target_ids,o.id)),'{}'::text[])
    into v_targets
  from objects o
  where o.id=any(v_claim.target_ids)
    and o.trashed_at is null
    and o.audit_requested
    and (
      o.audit_status='pending'
      or (
        o.audit_status='certified'
        and o.support_status='stale'
        and o.support_reason='logical_premise_math_changed'
      )
    )
    and o.mathematical_status in ('proved','evidence');

  v_impacts:=stale_consumer_impact_ids(v_targets,p_worker_id,12);

  select coalesce(array_agg(distinct x order by x),'{}'::text[])
    into v_extra
  from unnest(coalesce(p_additional_ids,'{}'::text[])||coalesce(v_impacts,'{}'::text[])) x;

  v_result:=control_center.open_audit_batch(
    p_worker_id,v_extra,p_content,p_page_chars
  );

  select coalesce(jsonb_agg(
    jsonb_build_object(
      'id',o.id,
      'title',o.title,
      'source_target_ids',to_jsonb((
        select coalesce(array_agg(e.to_id order by e.to_id),'{}'::text[])
        from edges e
        where e.from_id=o.id
          and e.kind in ('depends_on','proof')
          and e.to_id=any(v_targets)
      ))
    )
    order by o.audit_priority desc,o.id
  ),'[]'::jsonb)
    into v_impact_detail
  from objects o
  where o.id=any(coalesce(v_impacts,'{}'::text[]));

  update claims
     set payload=payload||jsonb_build_object(
       'consumer_impact_ids',to_jsonb(coalesce(v_impacts,'{}'::text[])),
       'consumer_impact_source_target_ids',to_jsonb(v_targets)
     ),
         renewed_at=now()
   where claim_id=v_claim.claim_id;

  return v_result||jsonb_build_object(
    'consumer_impacts',v_impact_detail,
    'consumer_impact_instruction',
      case when cardinality(coalesce(v_impacts,'{}'::text[]))=0
        then 'No direct stale consumers are eligible for cheap impact confirmation in this batch.'
        else 'For every listed consumer, submit exactly one PASS or DEFER with submit_audit_batch_v2. PASS means the unchanged consumer proof still works with the newly read premise version(s); it refreshes only the premise snapshot and preserves the original theorem certification.'
      end
  );
end
$function$

```

## open_audit_bundle(p_worker_id bigint, p_target_id text, p_content text DEFAULT 'full'::text, p_page_chars integer DEFAULT 12000) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.open_audit_bundle(p_worker_id bigint, p_target_id text, p_content text DEFAULT 'full'::text, p_page_chars integer DEFAULT 12000)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$begin
  PERFORM control_center.active_project();
  
  RETURN (

  select control_center.open_audit_bundle_v2(
    p_worker_id,p_target_id,'{}'::text[],p_content,p_page_chars
  )

  );
end$function$

```

## open_audit_bundle_v2(p_worker_id bigint, p_target_id text, p_additional_ids text[] DEFAULT '{}'::text[], p_content text DEFAULT 'math'::text, p_page_chars integer DEFAULT 12000) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.open_audit_bundle_v2(p_worker_id bigint, p_target_id text, p_additional_ids text[] DEFAULT '{}'::text[], p_content text DEFAULT 'math'::text, p_page_chars integer DEFAULT 12000)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
DECLARE
  v_result jsonb;
  v_claim_id bigint;
  v_versions jsonb;
  v_context jsonb;
begin
  PERFORM control_center.active_project();
  
  v_result := control_center.open_audit_bundle_v2_base_recomposition_equivalence(
    p_worker_id,p_target_id,p_additional_ids,p_content,p_page_chars
  );

  SELECT c.claim_id INTO v_claim_id
  FROM claims c
  WHERE c.worker_id=p_worker_id
    
    AND p_target_id=ANY(c.target_ids)
    AND c.expires_at>now()
  ORDER BY c.created_at DESC
  LIMIT 1;

  v_versions:=recomposition_equivalence_source_versions(array[p_target_id]);
  v_context:=recomposition_equivalence_audit_context(array[p_target_id]);

  IF v_versions<>'{}'::jsonb THEN
    UPDATE audit_snapshots
    SET watched_math_versions=watched_math_versions||v_versions
    WHERE claim_id=v_claim_id
      AND worker_id=p_worker_id
      AND target_id=p_target_id;
  END IF;

  RETURN v_result||jsonb_build_object(
    'recomposition_equivalence_audit',v_context,
    'recomposition_source_math_versions',v_versions,
    'audit_snapshot',audit_snapshot_state(v_claim_id,p_target_id)
  );
END
$function$

```

## open_audit_bundle_v2_base_recomposition_equivalence(p_worker_id bigint, p_target_id text, p_additional_ids text[] DEFAULT '{}'::text[], p_content text DEFAULT 'math'::text, p_page_chars integer DEFAULT 12000) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.open_audit_bundle_v2_base_recomposition_equivalence(p_worker_id bigint, p_target_id text, p_additional_ids text[] DEFAULT '{}'::text[], p_content text DEFAULT 'math'::text, p_page_chars integer DEFAULT 12000)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_claim record;
  v_ids text[];
  v_versions jsonb;
  v_page jsonb;
  v_session bigint;
  v_done boolean;
begin
  PERFORM control_center.active_project();
  
  if p_content not in ('math','full') then
    raise exception 'audit bundles require content=math or content=full; statement/body-only audits cannot certify mathematics';
  end if;

  select * into v_claim from claims c
   where c.worker_id=p_worker_id
     
     and p_target_id=any(c.target_ids)
     and c.expires_at>now()
   order by c.created_at desc limit 1;

  if v_claim.claim_id is null then
    raise exception 'active claim covering target % required',p_target_id;
  end if;

  select array_agg(id order by ord,id) into v_ids
  from (
    select p_target_id as id,0 as ord
    union
    select e.to_id,
      case e.kind when 'depends_on' then 1
                  when 'fence' then 2 when 'interface' then 3 else 4 end
      from edges e
     where e.from_id=p_target_id
       and e.kind in ('depends_on','fence','interface','references')
    union
    select x,5 from unnest(coalesce(p_additional_ids,'{}'::text[])) x
  ) q
  where exists(
    select 1 from objects o where o.id=q.id and o.trashed_at is null
  );

  select coalesce(jsonb_object_agg(o.id,o.math_version),'{}'::jsonb)
    into v_versions
    from objects o
   where o.id=any(v_ids) and o.trashed_at is null;

  v_page:=control_center.open_read_ex(
    p_worker_id,v_ids,p_content,p_page_chars,
    case when p_content='full' then 'object' else 'math' end
  );
  v_session:=(v_page->>'session_id')::bigint;
  v_done:=coalesce((v_page->>'done')::boolean,false)
    and not coalesce((v_page->>'stale')::boolean,false);

  insert into audit_snapshots(
    claim_id,worker_id,target_id,target_math_version,premise_signature,
    watched_math_versions,read_session_id,read_completed_at,content_mode,expires_at
  ) values (
    v_claim.claim_id,p_worker_id,p_target_id,
    (select math_version from objects where id=p_target_id),
    premise_signature(p_target_id),
    v_versions,v_session,case when v_done then now() else null end,
    p_content,v_claim.expires_at
  )
  on conflict(claim_id,target_id) do update set
    worker_id=excluded.worker_id,
    target_math_version=excluded.target_math_version,
    premise_signature=excluded.premise_signature,
    watched_math_versions=excluded.watched_math_versions,
    read_session_id=excluded.read_session_id,
    read_completed_at=excluded.read_completed_at,
    content_mode=excluded.content_mode,
    created_at=now(),
    expires_at=excluded.expires_at;

  return v_page||jsonb_build_object(
    'audit_snapshot',audit_snapshot_state(v_claim.claim_id,p_target_id),
    'audit_content_mode',p_content,
    'additional_watched_ids',coalesce(p_additional_ids,'{}'::text[]),
    'note','Single-target compatibility reader. For an assigned audit batch, prefer open_audit_batch so all targets share one exact read basis.'
  );
end
$function$

```

## open_read(p_worker_id bigint, p_ids text[], p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.open_read(p_worker_id bigint, p_ids text[], p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$begin
  perform control_center.assert_worker_database_access(p_worker_id,'open_read');
  PERFORM control_center.active_project();
  
  RETURN (

  select control_center.open_read_ex(
    p_worker_id,p_ids,p_content,p_page_chars,
    case when p_content='full' then 'object' else 'math' end
  )

  );
end$function$

```

## open_read_ex(p_worker_id bigint, p_ids text[], p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000, p_consistency text DEFAULT 'math'::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.open_read_ex(p_worker_id bigint, p_ids text[], p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000, p_consistency text DEFAULT 'math'::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
begin
  perform control_center.assert_worker_database_access(p_worker_id,'open_read_ex');
  PERFORM control_center.active_project();
  
  PERFORM require_math_principal(p_worker_id);
  PERFORM pg_advisory_xact_lock(hashtext((control_center.active_project()||'_read_pool')));
  RETURN control_center.open_read_ex_base(
    p_worker_id,p_ids,p_content,p_page_chars,p_consistency
  );
END
$function$

```

## open_read_ex_base(p_worker_id bigint, p_ids text[], p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000, p_consistency text DEFAULT 'math'::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.open_read_ex_base(p_worker_id bigint, p_ids text[], p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000, p_consistency text DEFAULT 'math'::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_ids text[];
  v_versions jsonb;
  v_math_versions jsonb;
  v_count integer;
  v_cap integer;
  v_ttl integer;
  v_session bigint;
  v_consistency text:=p_consistency;
begin
  perform control_center.assert_worker_database_access(p_worker_id,'open_read_ex_base');
  PERFORM control_center.active_project();
  
  perform purge_ephemeral();

  if p_content not in ('statement','body','math','full') then
    raise exception 'content must be statement, body, math, or full';
  end if;
  if p_consistency not in ('math','object') then
    raise exception 'consistency must be math or object';
  end if;

  -- A serialized full object contains mutable organizational fields. Offsets are
  -- safe only if the entire object version remains fixed. Exact mathematical
  -- paging uses content=math instead.
  if p_content='full' then
    v_consistency:='object';
  elsif p_content='math' then
    v_consistency:='math';
  end if;

  select coalesce(array_agg(id order by ord),'{}'::text[])
    into v_ids
    from (
      select distinct on (u.id) u.id,u.ord
        from unnest(coalesce(p_ids,'{}'::text[])) with ordinality u(id,ord)
        join objects o on o.id=u.id and o.trashed_at is null
       order by u.id,u.ord
    ) q;

  if cardinality(v_ids)=0 then raise exception 'no live objects selected'; end if;
  if cardinality(v_ids)>control_center.config_int('read.max_session_objects') then raise exception 'one read session exceeds configured object cap'; end if;

  select jsonb_object_agg(o.id,o.version),
         jsonb_object_agg(o.id,o.math_version)
    into v_versions,v_math_versions
    from objects o
   where o.id=any(v_ids) and o.trashed_at is null;

  select max_read_sessions,read_ttl_minutes into v_cap,v_ttl
    from settings where singleton;
  select count(*) into v_count from read_sessions where expires_at>now();

  if v_count>=v_cap then
    raise exception 'PROJECT read-session cap % reached',v_cap;
  end if;

  insert into read_sessions(
    owner_worker_id,content,object_ids,versions,math_versions,
    consistency,page_chars,expires_at
  ) values (
    p_worker_id,p_content,v_ids,v_versions,v_math_versions,
    v_consistency,greatest(control_center.config_int('read.min_page_chars'),least(control_center.config_int('text.audit_page_chars'),p_page_chars)),
    now()+make_interval(mins=>v_ttl)
  ) returning session_id into v_session;

  return control_center.read_page(p_worker_id,v_session,null);
end
$function$

```

## open_search(p_worker_id bigint, p_query text, p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000, p_attention text DEFAULT NULL::text, p_under_id text DEFAULT NULL::text, p_research_level text DEFAULT NULL::text, p_mathematical_status text DEFAULT NULL::text, p_audit_status text DEFAULT NULL::text, p_object_type text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.open_search(p_worker_id bigint, p_query text, p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000, p_attention text DEFAULT NULL::text, p_under_id text DEFAULT NULL::text, p_research_level text DEFAULT NULL::text, p_mathematical_status text DEFAULT NULL::text, p_audit_status text DEFAULT NULL::text, p_object_type text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_under_path text;
  v_ids text[];
  v_total integer;
  v_page jsonb;
begin
  perform control_center.assert_worker_database_access(p_worker_id,'open_search');
  perform control_center.active_project();

  if p_under_id is not null then
    select tree_path into v_under_path from objects
     where id=p_under_id and trashed_at is null;
    if v_under_path is null then raise exception 'under_id % not found',p_under_id; end if;
  end if;

  select count(*) into v_total
  from objects o
  where o.trashed_at is null
    and not exists (
      select 1 from objects ar
      where ar.id='archive01'
        and ar.trashed_at is null
        and o.tree_path like ar.tree_path||'%'
    )
    and (p_attention is null or o.attention=p_attention)
    and (p_research_level is null or o.research_level=p_research_level)
    and (p_mathematical_status is null or o.mathematical_status=p_mathematical_status)
    and (p_audit_status is null or o.audit_status=p_audit_status)
    and (p_object_type is null or o.object_type=p_object_type)
    and (v_under_path is null or o.tree_path like v_under_path||'%')
    and (
      coalesce(btrim(p_query),'')=''
      or to_tsvector('simple',coalesce(o.title,'')||' '||coalesce(o.statement,'')||' '||coalesce(o.body,''))
        @@ plainto_tsquery('simple',p_query)
    );

  select array_agg(id order by rank desc,attention_order,updated_at desc)
    into v_ids
  from (
    select o.id,o.updated_at,
           case o.attention when 'focus' then 0 when 'available' then 1 else 2 end attention_order,
           case when coalesce(btrim(p_query),'')='' then 0 else
             ts_rank(
               to_tsvector('simple',coalesce(o.title,'')||' '||coalesce(o.statement,'')||' '||coalesce(o.body,'')),
               plainto_tsquery('simple',p_query)
             )
           end rank
    from objects o
    where o.trashed_at is null
      and not exists (
        select 1 from objects ar
        where ar.id='archive01'
          and ar.trashed_at is null
          and o.tree_path like ar.tree_path||'%'
      )
      and (p_attention is null or o.attention=p_attention)
      and (p_research_level is null or o.research_level=p_research_level)
      and (p_mathematical_status is null or o.mathematical_status=p_mathematical_status)
      and (p_audit_status is null or o.audit_status=p_audit_status)
      and (p_object_type is null or o.object_type=p_object_type)
      and (v_under_path is null or o.tree_path like v_under_path||'%')
      and (
        coalesce(btrim(p_query),'')=''
        or to_tsvector('simple',coalesce(o.title,'')||' '||coalesce(o.statement,'')||' '||coalesce(o.body,''))
          @@ plainto_tsquery('simple',p_query)
      )
    order by rank desc,attention_order,o.updated_at desc
    limit control_center.config_int('search.max_open_selection')
  ) q;

  if v_ids is null or cardinality(v_ids)=0 then
    return jsonb_build_object(
      'items','[]'::jsonb,'done',true,
      'selection_total_count',v_total,'selection_selected_count',0,
      'selection_truncated',false,
      'selection_note','Archive subtree is excluded from ordinary search.',
      'repository_revision',(select revision from state where singleton)
    );
  end if;

  v_page:=control_center.open_read(
    p_worker_id,v_ids,p_content,p_page_chars
  );

  return v_page||jsonb_build_object(
    'selection_total_count',v_total,
    'selection_selected_count',cardinality(v_ids),
    'selection_truncated',v_total>cardinality(v_ids),
    'selection_note',case when v_total>cardinality(v_ids)
      then 'Exact-search selection is capped at the configured maximum matches; refine the query/filter before treating this as complete. Archive subtree is excluded.'
      else 'Archive subtree is excluded from ordinary search.' end
  );
end
$function$

```

## open_subtree(p_worker_id bigint, p_root_id text, p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.open_subtree(p_worker_id bigint, p_root_id text, p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_path text;
  v_ids text[];
begin
  PERFORM control_center.active_project();
  
  select tree_path into v_path from objects
   where id=p_root_id and trashed_at is null;
  if v_path is null then raise exception 'root object % not found',p_root_id; end if;

  select array_agg(id order by tree_path) into v_ids
    from (
      select id,tree_path
        from objects
       where trashed_at is null and tree_path like v_path||'%'
       order by tree_path
       limit control_center.config_int('subtree.max_open_selection')
    ) q;

  return control_center.open_read(p_worker_id,v_ids,p_content,p_page_chars);
end
$function$

```

## poll_queue(p_worker_id bigint, p_limit integer DEFAULT 6) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.poll_queue(p_worker_id bigint, p_limit integer DEFAULT 6)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
begin
  perform control_center.active_project();
  return control_center.poll_queue_for_worker(p_worker_id,p_limit,true);
end$function$

```

## poll_queue_for_worker(p_worker_id bigint, p_limit integer DEFAULT NULL::integer, p_claim_actions boolean DEFAULT true) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.poll_queue_for_worker(p_worker_id bigint, p_limit integer DEFAULT NULL::integer, p_claim_actions boolean DEFAULT true)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_default_limit integer:=6;
  v_lease_minutes integer:=10;
  v_limit integer;
  v_lease_until timestamptz;
  v_actions jsonb:='[]'::jsonb;
  v_votes jsonb:='[]'::jsonb;
  v_action_count integer:=0;
  v_vote_count integer:=0;
begin
  perform control_center.active_project();

  select poll_batch_size,poll_action_lease_minutes
    into v_default_limit,v_lease_minutes
  from settings where singleton;

  v_limit:=greatest(1,least(control_center.config_int('poll.queue_max_limit'),coalesce(p_limit,v_default_limit,control_center.config_int('legacy.poll_batch_size'))));
  v_lease_minutes:=greatest(control_center.config_int('ttl.poll_action_min_minutes'),least(control_center.config_int('ttl.poll_action_max_minutes'),coalesce(v_lease_minutes,control_center.config_int('legacy.poll_action_lease_minutes'))));

  update polls
  set action_claimed_by=null,
      action_claim_expires_at=null,
      updated_at=now()
  where status='passed_pending_action'
    and action_claimed_by is not null
    and action_claim_expires_at is not null
    and action_claim_expires_at<=now();

  select coalesce(max(c.expires_at),now()+make_interval(mins=>v_lease_minutes))
    into v_lease_until
  from claims c
  where c.worker_id=p_worker_id
    and c.need_key='vote'
    and c.expires_at>now();

  if p_claim_actions then
    with candidates as (
      select q.poll_id
      from polls q
      where q.status='passed_pending_action'
        and not (
          q.last_deferred_by=p_worker_id
          and q.last_deferred_at is not null
          and q.last_deferred_at > now()-interval '10 minutes'
        )
        and (
          q.closed_by_worker_id=p_worker_id
          or not exists (
            select 1
            from claims c
            where c.worker_id=q.closed_by_worker_id
              and c.need_key='vote'
              and c.expires_at>now()
              and c.created_at<=coalesce(q.closed_at,now())
          )
        )
        and (
          q.action_claimed_by is null
          or q.action_claimed_by=p_worker_id
          or q.action_claim_expires_at is null
          or q.action_claim_expires_at<=now()
        )
      order by
        (q.closed_by_worker_id=p_worker_id) desc,
        greatest(q.priority::integer,control_center.config_int('need.vote.pending_action_priority_floor')) desc,
        q.closed_at,
        q.created_at
      limit v_limit
      for update skip locked
    )
    update polls q
    set action_claimed_by=p_worker_id,
        action_claim_expires_at=v_lease_until,
        updated_at=now()
    from candidates c
    where q.poll_id=c.poll_id;
  end if;

  select coalesce(jsonb_agg(jsonb_build_object(
      'poll_task','enact',
      'poll_id',q.poll_id,
      'issue',q.issue,
      'action',q.action,
      'target_ids',to_jsonb(q.target_ids),
      'poll_status','passed_pending_action',
      'final_voter',q.closed_by_worker_id=p_worker_id,
      'action_claimed_until',q.action_claim_expires_at,
      'instruction',
        case when q.closed_by_worker_id=p_worker_id
          then 'You supplied the final passing ballot. Enact the action now, then call resolve_poll_action(...,''enacted'',details), or explicitly defer it.'
          else 'This passed action is leased to you for this batch. Enact it, then call resolve_poll_action(...,''enacted'',details), or explicitly defer it.'
        end
    ) order by
      (q.closed_by_worker_id=p_worker_id) desc,
      greatest(q.priority::integer,control_center.config_int('need.vote.pending_action_priority_floor')) desc,
      q.closed_at,q.created_at
  ),'[]'::jsonb),
  count(*)::integer
  into v_actions,v_action_count
  from polls q
  where q.status='passed_pending_action'
    and (
      (p_claim_actions and q.action_claimed_by=p_worker_id and q.action_claim_expires_at>now())
      or (
        not p_claim_actions
        and (
          q.action_claimed_by is null
          or q.action_claimed_by=p_worker_id
          or q.action_claim_expires_at is null
          or q.action_claim_expires_at<=now()
        )
        and (
          q.closed_by_worker_id=p_worker_id
          or not exists (
            select 1 from claims c
            where c.worker_id=q.closed_by_worker_id
              and c.need_key='vote'
              and c.expires_at>now()
              and c.created_at<=coalesce(q.closed_at,now())
          )
        )
      )
    )
    and not (
      q.last_deferred_by=p_worker_id
      and q.last_deferred_at is not null
      and q.last_deferred_at > now()-interval '10 minutes'
    );

  select coalesce(jsonb_agg(jsonb_build_object(
      'poll_task','vote',
      'poll_id',q.poll_id,
      'issue',q.issue,
      'action',q.action,
      'target_ids',to_jsonb(q.target_ids),
      'vote_limit',q.vote_limit,
      'ballots_recorded',(
        select count(*) from poll_votes v
        where v.poll_id=q.poll_id and v.response in ('yes','no')
      ),
      'ballots_remaining',greatest(0,q.vote_limit-(
        select count(*) from poll_votes v
        where v.poll_id=q.poll_id and v.response in ('yes','no')
      )),
      'privacy','Yes/no choices and voter identities are hidden while the poll is open.',
      'instruction','Vote privately with vote_poll(worker_id,poll_id,''yes''|''no''). You may refuse with vote_poll(worker_id,poll_id,''refuse''); refusal does not consume a ballot slot.'
    ) order by q.priority desc,q.created_at),'[]'::jsonb),
    count(*)::integer
  into v_votes,v_vote_count
  from (
    select q.*
    from polls q
    where q.status='open'
      and not exists (
        select 1 from poll_votes v
        where v.poll_id=q.poll_id and v.worker_id=p_worker_id
      )
    order by q.priority desc,q.created_at
    limit greatest(0,v_limit-least(v_limit,v_action_count))
  ) q;

  return jsonb_build_object(
    'batch',true,
    'batch_limit',v_limit,
    'task_count',v_action_count+v_vote_count,
    'action_tasks',v_actions,
    'vote_tasks',v_votes,
    'privacy','Open-poll directional tallies and all individual ballots remain private.',
    'instruction','Process this as a batch. Handle passed actions first, then cast yes/no/refuse responses on whichever open polls are appropriate. Re-open the queue if you want another batch. If your ballot is the final passing ballot, enact or defer that action before completing poll duty.'
  );
end
$function$

```

## poll_status(p_poll_id bigint) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.poll_status(p_poll_id bigint)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
DECLARE
  p record;
  v_yes integer:=0;
  v_no integer:=0;
  v_ballots integer:=0;
BEGIN
  PERFORM control_center.active_project();

  SELECT * INTO p FROM polls WHERE poll_id=p_poll_id;
  IF p.poll_id IS NULL THEN
    RAISE EXCEPTION 'poll % not found',p_poll_id;
  END IF;

  SELECT
    count(*) FILTER (WHERE response='yes')::integer,
    count(*) FILTER (WHERE response='no')::integer
  INTO v_yes,v_no
  FROM poll_votes
  WHERE poll_id=p_poll_id;

  v_ballots:=v_yes+v_no;

  IF p.status='open' THEN
    RETURN jsonb_build_object(
      'poll_id',p.poll_id,
      'issue',p.issue,
      'action',p.action,
      'target_ids',to_jsonb(p.target_ids),
      'status','open',
      'vote_limit',p.vote_limit,
      'ballots_received',v_ballots,
      'ballots_remaining',greatest(0,p.vote_limit-v_ballots),
      'priority',p.priority,
      'created_at',p.created_at,
      'ballot_privacy','directional tallies and voter identities are hidden until closure'
    );
  END IF;

  RETURN jsonb_build_object(
    'poll_id',p.poll_id,
    'issue',p.issue,
    'action',p.action,
    'target_ids',to_jsonb(p.target_ids),
    'status',p.status,
    'vote_limit',p.vote_limit,
    'result',CASE WHEN v_yes>v_no THEN 'passed' ELSE 'rejected' END,
    'yes_votes',v_yes,
    'no_votes',v_no,
    'closed_at',p.closed_at,
    'action_pending',p.status='passed_pending_action',
    'enacted_at',p.enacted_at,
    'action_resolution',p.action_resolution,
    'ballot_privacy','individual voter identities and ballots remain private'
  );
END
$function$

```

## presence(p_scope_id text DEFAULT NULL::text, p_global boolean DEFAULT false, p_limit integer DEFAULT 32) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.presence(p_scope_id text DEFAULT NULL::text, p_global boolean DEFAULT false, p_limit integer DEFAULT 32)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare
  v_scope_path text;
begin
  PERFORM control_center.active_project();
  
  if p_scope_id is not null then
    select tree_path into v_scope_path from objects where id=p_scope_id and trashed_at is null;
    if v_scope_path is null then raise exception 'scope object % not found',p_scope_id; end if;
  end if;

  return jsonb_build_object(
    'items',(
      select coalesce(jsonb_agg(jsonb_build_object(
        'presence_id',p.presence_id,
        'activity',p.activity,
        'scope_id',p.scope_id,
        'message',p.message,
        'exclusive',p.exclusive_key is not null,
        'created_at',p.created_at,
        'touched_at',p.touched_at,
        'expires_at',p.expires_at
      ) order by p.touched_at desc),'[]'::jsonb)
      from (
        select p.*
          from presence p
          left join objects s on s.id=p.scope_id
         where p.expires_at>now()
           and (
             p_global
             or p_scope_id is null
             or p.scope_id is null
             or s.tree_path like v_scope_path||'%'
             or v_scope_path like s.tree_path||'%'
           )
         order by p.touched_at desc
         limit greatest(1,least(control_center.config_int('api.default_limit'),p_limit))
      ) p
    )
  );
end
$function$

```

## proof_overview(p_root_id text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.proof_overview(p_root_id text)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$begin
  PERFORM control_center.active_project();
  
  RETURN (

  select control_center.reasoning_overview(p_root_id)

  );
end$function$

```

## proof_preflight(p_object jsonb, p_dependency_ids text[] DEFAULT '{}'::text[]) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.proof_preflight(p_object jsonb, p_dependency_ids text[] DEFAULT '{}'::text[])
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare
  v_status text := nullif(btrim(coalesce(p_object->>'mathematical_status','')),'');
  v_level text := nullif(btrim(coalesce(p_object->>'research_level','')),'');
  v_errors text[] := '{}'::text[];
  v_warnings text[] := '{}'::text[];
  v_missing text[] := '{}'::text[];
  v_untrusted text[] := '{}'::text[];
begin
  perform control_center.active_project();

  if jsonb_typeof(coalesce(p_object,'null'::jsonb)) <> 'object' then
    return jsonb_build_object('ok',false,'errors',jsonb_build_array('candidate must be a JSON object'),'warnings','[]'::jsonb);
  end if;

  if v_status='proved' then
    if nullif(btrim(coalesce(p_object->>'statement','')),'') is null then
      v_errors := array_append(v_errors,'proved object requires a nonempty statement');
    end if;
    if nullif(btrim(coalesce(p_object->>'body','')),'') is null then
      v_errors := array_append(v_errors,'proved object requires a nonempty proof/body');
    end if;
  end if;

  select coalesce(array_agg(x order by x),'{}'::text[])
    into v_missing
  from (
    select distinct d as x
    from unnest(coalesce(p_dependency_ids,'{}'::text[])) d
    left join objects o on o.id=control_center.canonical_object_id(d) and o.trashed_at is null
    where o.id is null
  ) q;

  if cardinality(v_missing)>0 then
    v_errors := array_append(v_errors,'one or more declared dependencies do not exist');
  end if;

  select coalesce(array_agg(o.id order by o.id),'{}'::text[])
    into v_untrusted
  from objects o
  where o.id=any(array(
    select control_center.canonical_object_id(d)
    from unnest(coalesce(p_dependency_ids,'{}'::text[])) d
  ))
    and o.trashed_at is null
    and (
      o.audit_status<>'certified'
      or o.support_status<>'supported'
    );

  if cardinality(v_untrusted)>0 then
    v_warnings := array_append(v_warnings,
      'declared dependencies include provisional or dependency-held mathematics');
  end if;

  if v_status='proved'
     and v_level in ('theorem','proof_level')
     and cardinality(coalesce(p_dependency_ids,'{}'::text[]))=0 then
    v_warnings := array_append(v_warnings,
      'theorem/proof-level proved object records no logical dependencies; confirm it is genuinely self-contained');
  end if;

  return jsonb_build_object(
    'ok',cardinality(v_errors)=0,
    'errors',to_jsonb(v_errors),
    'warnings',to_jsonb(v_warnings),
    'missing_dependency_ids',to_jsonb(v_missing),
    'provisional_dependency_ids',to_jsonb(v_untrusted),
    'self_check_only',true,
    'certification',false
  );
end
$function$

```

## prune_preview(p_ids text[]) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.prune_preview(p_ids text[])
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare
  v_items jsonb := '[]'::jsonb;
  v_id text;
  v_path text;
  v_count integer;
  v_external integer;
  v_state_ref boolean;
begin
  PERFORM control_center.active_project();
  
  foreach v_id in array coalesce(p_ids,'{}'::text[])
  loop
    select tree_path into v_path from objects where id=v_id;
    if v_path is null then
      v_items := v_items||jsonb_build_array(jsonb_build_object('id',v_id,'exists',false));
      continue;
    end if;

    select count(*) into v_count from objects where tree_path like v_path||'%';

    select count(*) into v_external
      from edges e
      join objects inside_obj on inside_obj.id=e.to_id
      join objects outside_obj on outside_obj.id=e.from_id
     where inside_obj.tree_path like v_path||'%'
       and outside_obj.tree_path not like v_path||'%'
       and outside_obj.trashed_at is null;

    select exists(
      select 1 from state s
       where s.singleton and (
         v_id=any(array[s.grand_theorem_id,s.current_strategy_id,s.proof_frontier_id,s.current_bottleneck_id]::text[])
         or exists(
           select 1 from objects o
            where o.id=any(s.research_focus_ids) and o.tree_path like v_path||'%'
         )
       )
    ) into v_state_ref;

    v_items := v_items||jsonb_build_array(jsonb_build_object(
      'id',v_id,
      'exists',true,
      'subtree_objects',v_count,
      'incoming_external_edges',v_external,
      'touches_project_state',v_state_ref
    ));
  end loop;

  return jsonb_build_object('items',v_items,'repository_revision',(select revision from state where singleton));
end
$function$

```

## publish_with_dependencies(p_worker_id bigint, p_object jsonb, p_dependency_ids text[] DEFAULT '{}'::text[]) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.publish_with_dependencies(p_worker_id bigint, p_object jsonb, p_dependency_ids text[] DEFAULT '{}'::text[])
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_created jsonb;
  v_id text;
  v_dep text;
  v_dep_math bigint;
  v_dependencies jsonb:='[]'::jsonb;
  v_reasoning jsonb:=null;
  v_metadata jsonb;
  v_interface jsonb;
  v_preflight jsonb;
  v_container_text text;
  v_replace_parent_container_text boolean;
  v_container_owner_id text;
begin
  perform control_center.active_project();

  if jsonb_typeof(coalesce(p_object,'null'::jsonb))<>'object' then
    raise exception 'p_object must be a JSON object';
  end if;
  if nullif(btrim(coalesce(p_object->>'object_type','')),'') is null then
    raise exception 'p_object.object_type is required';
  end if;
  if nullif(btrim(coalesce(p_object->>'title','')),'') is null then
    raise exception 'p_object.title is required';
  end if;
  if p_object ? 'audit_requested' or p_object ? 'audit_priority' then
    raise exception 'publication no longer accepts audit_requested/audit_priority; publish first, then call request_audit(...) separately if independent audit is specifically warranted';
  end if;

  v_container_text:=nullif(btrim(coalesce(p_object->>'container_text','')),'');
  v_replace_parent_container_text:=
    coalesce(nullif(p_object->>'replace_parent_container_text','')::boolean,false);

  v_metadata:=case when jsonb_typeof(p_object->'metadata')='object'
                   then p_object->'metadata' else '{}'::jsonb end;
  v_interface:=case when jsonb_typeof(p_object->'research_interface')='object'
                    then p_object->'research_interface' else '{}'::jsonb end;

  v_preflight:=control_center.proof_preflight(p_object,p_dependency_ids);
  if coalesce(p_object->>'mathematical_status','')='proved'
     and not coalesce((v_preflight->>'ok')::boolean,false) then
    raise exception 'proof preflight failed: %',v_preflight;
  end if;

  v_created:=control_center.create_object(
    p_worker_id,
    p_object->>'object_type',
    p_object->>'title',
    p_object->>'statement',
    coalesce(p_object->>'body',''),
    p_object->>'parent_id',
    coalesce(nullif(p_object->>'position','')::bigint,0),
    v_metadata,
    v_interface,
    p_object->>'mathematical_status',
    coalesce(nullif(p_object->>'research_level',''),'working_unit'),
    coalesce(nullif(p_object->>'lifecycle_status',''),'active'),
    coalesce(nullif(p_object->>'attention',''),'available'),
    p_object->>'id',
    p_object->>'legacy_id',
    nullif(p_object->>'simplified_statement',''),
    nullif(p_object->>'atlas_height',''),
    coalesce((p_object->>'atlas_hidden')::boolean,false)
  );
  v_id:=v_created->>'id';

  if v_replace_parent_container_text then
    select a.id into v_container_owner_id
    from objects self
    join objects a
      on self.tree_path like a.tree_path || '%'
     and a.id<>self.id
    where self.id=v_id
      and a.trashed_at is null
      and a.semantic_container_text is not null
    order by char_length(a.tree_path) desc
    limit 1;

    if v_container_owner_id is null then
      raise exception 'replace_parent_container_text=true requires an inherited semantic container';
    end if;

    if v_container_text is not null then
      update objects
         set semantic_container_text=v_container_text,
             version=version+1,
             updated_at=now()
       where id=v_container_owner_id;

      perform control_center.record_change(
        'update_semantic_container',
        array[v_container_owner_id,v_id],
        jsonb_build_object(
          'container_owner_id',v_container_owner_id,
          'published_child_id',v_id,
          'mode','replace_parent_container_text'
        )
      );
    end if;
  else
    update objects
       set semantic_container_text=v_container_text
     where id=v_id;
  end if;

  if nullif(btrim(coalesce(p_object->>'node_kind','')),'') is not null then
    v_reasoning:=control_center.mark_reasoning_node(
      p_worker_id,v_id,p_object->>'node_kind',
      p_object->>'route_key',p_object->>'reasoning_note');
  end if;

  for v_dep in
    select distinct control_center.canonical_object_id(x)
    from unnest(coalesce(p_dependency_ids,'{}'::text[])) x
  loop
    select math_version into v_dep_math
    from objects where id=v_dep and trashed_at is null for share;
    perform control_center.add_edge(
      p_worker_id,v_id,v_dep,'depends_on',
      jsonb_build_object('expected_math_version',v_dep_math));
    v_dependencies:=v_dependencies||jsonb_build_array(
      jsonb_build_object('id',v_dep,'math_version',v_dep_math));
  end loop;

  return jsonb_build_object(
    'object',(select to_jsonb(o) from objects o where o.id=v_id),
    'id',v_id,
    'dependencies',v_dependencies,
    'reasoning',v_reasoning,
    'semantic_container',control_center.semantic_container(v_id),
    'container_mode',case
      when v_replace_parent_container_text then 'inherit'
      when v_container_text is not null then 'new'
      else 'inherit'
    end,
    'parent_container_updated',v_replace_parent_container_text and v_container_text is not null,
    'atomic',true,
    'proof_preflight',v_preflight,
    'repository_revision',(select revision from state where singleton)
  );
end
$function$

```

## purge_trashed_subtrees(p_worker_id bigint, p_ids text[]) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.purge_trashed_subtrees(p_worker_id bigint, p_ids text[])
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_paths text[] := '{}'::text[];
  v_roots text[] := (coalesce(p_ids,'{}'::text[]))[1:control_center.config_int('tree.max_batch_roots')];
  v_delete_ids text[];
  v_id text;
  v_path text;
  v_count integer;
  v_rev bigint;
begin
  PERFORM control_center.active_project();
  
  perform pg_advisory_xact_lock(hashtext((control_center.active_project()||'_tree')));

  foreach v_id in array coalesce(p_ids,'{}'::text[])
  loop
    select tree_path into v_path
      from objects
     where id=v_id and trashed_at is not null;
    if v_path is not null then v_paths:=v_paths||v_path; end if;
  end loop;

  if cardinality(v_paths)=0 then return jsonb_build_object('purged',0); end if;

  select coalesce(array_agg(o.id),'{}'::text[])
    into v_delete_ids
    from objects o
   where o.trashed_at is not null
     and exists(select 1 from unnest(v_paths) p where o.tree_path like p||'%');

  perform assert_no_live_external_consumers(v_delete_ids);

  delete from edges
   where from_id=any(v_delete_ids) or to_id=any(v_delete_ids);

  delete from objects where id=any(v_delete_ids);
  get diagnostics v_count=row_count;

  v_rev:=record_change(
    'purge_trashed_subtrees',v_roots,
    jsonb_build_object('roots',v_roots,'objects_purged',v_count)
  );

  return jsonb_build_object('purged',v_count,'repository_revision',v_rev);
end
$function$

```

## raise_need(p_worker_id bigint, p_need_key text, p_priority integer, p_reason text, p_target_ids text[] DEFAULT '{}'::text[]) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.raise_need(p_worker_id bigint, p_need_key text, p_priority integer, p_reason text, p_target_ids text[] DEFAULT '{}'::text[])
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$begin
  PERFORM control_center.active_project();
  
  RETURN (

  select raise_need(p_need_key,p_priority,p_reason,p_target_ids,'{}'::bigint[])

  );
end$function$

```

## raise_signal(p_worker_id bigint, p_kind text, p_title text, p_body text DEFAULT ''::text, p_severity integer DEFAULT 1, p_evidence jsonb DEFAULT '{}'::jsonb, p_related_object_ids text[] DEFAULT '{}'::text[], p_signal_key text DEFAULT NULL::text) -> bigint

```sql
CREATE OR REPLACE FUNCTION control_center.raise_signal(p_worker_id bigint, p_kind text, p_title text, p_body text DEFAULT ''::text, p_severity integer DEFAULT 1, p_evidence jsonb DEFAULT '{}'::jsonb, p_related_object_ids text[] DEFAULT '{}'::text[], p_signal_key text DEFAULT NULL::text)
 RETURNS bigint
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$begin
  PERFORM control_center.active_project();
  
  RETURN (

  select raise_signal(
    p_kind,p_title,p_body,p_severity,p_evidence,p_related_object_ids,p_worker_id,p_signal_key
  )

  );
end$function$

```

## read(p_ids text[], p_content text DEFAULT 'statement'::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.read(p_ids text[], p_content text DEFAULT 'statement'::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
begin
  PERFORM control_center.active_project();
  
  if p_content not in ('statement','summary','body','math','full') then
    raise exception 'content must be statement, summary, body, math, or full';
  end if;

  return (
    select jsonb_build_object(
      'items',coalesce(jsonb_agg(item order by ord),'[]'::jsonb),
      'repository_revision',(select revision from state where singleton),
      'note',case when p_content='full'
        then 'full is intentionally uncapped exact object retrieval; use summary/context/search snippets before full when possible'
        else null end
    )
    from (
      select u.ord,
        case p_content
          when 'statement' then object_brief(o.id)
          when 'summary' then object_research_summary(o.id)
          when 'body' then jsonb_build_object(
            'id',o.id,'title',o.title,'body',o.body,
            'version',o.version,'math_version',o.math_version,
            'audit_status',o.audit_status,'support_status',o.support_status,
            'mathematical_status',o.mathematical_status
          )
          when 'math' then jsonb_build_object(
            'id',o.id,'title',o.title,'statement',o.statement,'body',o.body,
            'research_interface',o.research_interface,
            'mathematical_status',o.mathematical_status,'math_version',o.math_version,
            'audit_status',o.audit_status,'audit_requirement',o.audit_requirement,
            'support_status',o.support_status,'support_reason',o.support_reason
          )
          else to_jsonb(o)
        end as item
      from unnest(coalesce(p_ids,'{}'::text[])) with ordinality u(id,ord)
      join objects o on o.id=u.id and o.trashed_at is null
    ) q
  );
end
$function$

```

## read_more(p_worker_id bigint, p_session_id bigint, p_max_pages integer DEFAULT 4, p_max_output_chars integer DEFAULT 50000) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.read_more(p_worker_id bigint, p_session_id bigint, p_max_pages integer DEFAULT 4, p_max_output_chars integer DEFAULT 50000)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  s record;
  v_pages jsonb:='[]'::jsonb;
  v_page jsonb;
  v_cursor jsonb;
  v_n integer:=0;
  v_chars integer:=0;
  v_done boolean:=false;
begin
  perform control_center.assert_worker_database_access(p_worker_id,'read_more');
  PERFORM control_center.active_project();
  
  perform touch_worker_claim(p_worker_id);

  select * into s
  from read_sessions
  where session_id=p_session_id
    and owner_worker_id=p_worker_id
    and expires_at>now();

  if s.session_id is null then
    raise exception 'read session not found or expired';
  end if;
  if s.completed_at is not null then
    return jsonb_build_object(
      'session_id',p_session_id,'pages','[]'::jsonb,
      'page_count',0,'done',true,'next_cursor',null
    );
  end if;

  v_cursor:=s.expected_cursor;

  while v_n<greatest(1,least(control_center.config_int('read_more.max_pages'),coalesce(p_max_pages,control_center.config_int('read_more.default_pages'))))
    and v_chars<greatest(control_center.config_int('read_more.min_output_chars'),least(control_center.config_int('read_more.max_output_chars'),coalesce(p_max_output_chars,control_center.config_int('read_more.default_output_chars'))))
  loop
    v_page:=control_center.read_page(p_worker_id,p_session_id,v_cursor);
    v_pages:=v_pages||jsonb_build_array(v_page);
    v_n:=v_n+1;
    v_chars:=v_chars+length(v_page::text);
    v_done:=coalesce((v_page->>'done')::boolean,false)
      or coalesce((v_page->>'stale')::boolean,false);
    exit when v_done;
    v_cursor:=v_page->'next_cursor';
  end loop;

  return jsonb_build_object(
    'session_id',p_session_id,
    'pages',v_pages,
    'page_count',v_n,
    'approx_output_chars',v_chars,
    'done',v_done,
    'next_cursor',case when v_done then null else v_cursor end,
    'server_authoritative_cursor',true
  );
end
$function$

```

## read_page(p_worker_id bigint, p_session_id bigint, p_cursor jsonb DEFAULT NULL::jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.read_page(p_worker_id bigint, p_session_id bigint, p_cursor jsonb DEFAULT NULL::jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_session record;
  v_result jsonb;
  v_done boolean;
  v_next jsonb;
begin
  perform control_center.assert_worker_database_access(p_worker_id,'read_page');
  PERFORM control_center.active_project();
  
  perform touch_worker_claim(p_worker_id);
  perform purge_ephemeral();

  select * into v_session
    from read_sessions
   where session_id=p_session_id
     and owner_worker_id=p_worker_id
     and expires_at>now()
   for update;

  if v_session.session_id is null then
    raise exception 'read session not found or expired';
  end if;

  if v_session.completed_at is not null then
    raise exception 'read session % is already complete',p_session_id;
  end if;

  if p_cursor is distinct from v_session.expected_cursor then
    raise exception
      'invalid read cursor for session %: expected %, received %',
      p_session_id,v_session.expected_cursor,p_cursor;
  end if;

  v_result:=control_center.read_page_base(
    p_worker_id,p_session_id,p_cursor
  );

  v_done:=coalesce((v_result->>'done')::boolean,false)
    and not coalesce((v_result->>'stale')::boolean,false);
  v_next:=v_result->'next_cursor';

  if not coalesce((v_result->>'stale')::boolean,false) then
    update read_sessions
       set expected_cursor=case when v_done then null else v_next end,
           pages_delivered=pages_delivered+1,
           completed_at=case when v_done then coalesce(completed_at,now())
                             else completed_at end
     where session_id=p_session_id
       and owner_worker_id=p_worker_id;

    if v_done then
      update audit_snapshots
         set read_completed_at=coalesce(read_completed_at,now())
       where read_session_id=p_session_id
         and worker_id=p_worker_id;

      perform record_completed_read_receipts(
        p_worker_id,p_session_id
      );
    end if;
  end if;

  return v_result||jsonb_build_object(
    'server_authoritative_cursor',true,
    'pages_delivered',(select pages_delivered
      from read_sessions where session_id=p_session_id)
  );
end
$function$

```

## read_page_base(p_worker_id bigint, p_session_id bigint, p_cursor jsonb DEFAULT NULL::jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.read_page_base(p_worker_id bigint, p_session_id bigint, p_cursor jsonb DEFAULT NULL::jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_session record;
  v_i integer := greatest(1,coalesce((p_cursor->>'index')::integer,1));
  v_offset integer := greatest(0,coalesce((p_cursor->>'offset')::integer,0));
  v_remaining integer;
  v_id text;
  v_expected bigint;
  v_current bigint;
  v_obj record;
  v_text text;
  v_take integer;
  v_items jsonb := '[]'::jsonb;
  v_complete boolean;
  v_next jsonb;
  v_ttl integer;
  v_pair record;
  v_stale jsonb := '[]'::jsonb;
begin
  perform control_center.assert_worker_database_access(p_worker_id,'read_page_base');
  PERFORM control_center.active_project();
  
  perform purge_ephemeral();

  select * into v_session from read_sessions
   where session_id=p_session_id
     and owner_worker_id=p_worker_id
     and expires_at>now()
   for update;

  if v_session.session_id is null then
    raise exception 'read session not found or expired';
  end if;

  for v_pair in select id from unnest(v_session.object_ids) id
  loop
    if v_session.consistency='math' then
      v_expected:=(v_session.math_versions->>v_pair.id)::bigint;
      select math_version into v_current from objects
       where id=v_pair.id and trashed_at is null;
    else
      v_expected:=(v_session.versions->>v_pair.id)::bigint;
      select version into v_current from objects
       where id=v_pair.id and trashed_at is null;
    end if;

    if v_current is distinct from v_expected then
      v_stale:=v_stale||jsonb_build_array(jsonb_build_object(
        'id',v_pair.id,'consistency',v_session.consistency,
        'expected',v_expected,'current',v_current
      ));
    end if;
  end loop;

  select read_ttl_minutes into v_ttl from settings where singleton;

  if jsonb_array_length(v_stale)>0 then
    update read_sessions
       set touched_at=now(),expires_at=now()+make_interval(mins=>v_ttl)
     where session_id=p_session_id;

    return jsonb_build_object(
      'session_id',p_session_id,
      'stale',true,
      'stale_objects',v_stale,
      'content',v_session.content,
      'consistency',v_session.consistency,
      'message','At least one object changed relative to the complete read manifest. Reopen; historical bodies are intentionally not cached.',
      'repository_revision',(select revision from state where singleton)
    );
  end if;

  v_remaining:=v_session.page_chars;

  while v_i<=cardinality(v_session.object_ids) and v_remaining>0 loop
    v_id:=v_session.object_ids[v_i];

    select * into v_obj from objects
     where id=v_id and trashed_at is null;

    v_text:=case v_session.content
      when 'statement' then coalesce(v_obj.statement,'')
      when 'body' then coalesce(v_obj.body,'')
      when 'math' then jsonb_build_object(
        'id',v_obj.id,
        'statement',v_obj.statement,
        'body',v_obj.body,
        'mathematical_status',v_obj.mathematical_status,
        'math_version',v_obj.math_version
      )::text
      else jsonb_build_object(
        'id',v_obj.id,'legacy_id',v_obj.legacy_id,'parent_id',v_obj.parent_id,
        'tree_path',v_obj.tree_path,'position',v_obj.position,'object_type',v_obj.object_type,
        'title',v_obj.title,'statement',v_obj.statement,'body',v_obj.body,
        'metadata',v_obj.metadata,'research_interface',v_obj.research_interface,
        'mathematical_status',v_obj.mathematical_status,'research_level',v_obj.research_level,
        'lifecycle_status',v_obj.lifecycle_status,'attention',v_obj.attention,
        'audit_status',v_obj.audit_status,'support_status',v_obj.support_status,
        'audit_requested',v_obj.audit_requested,'math_version',v_obj.math_version,
        'audited_math_version',v_obj.audited_math_version,'version',v_obj.version
      )::text
    end;

    if v_offset>=length(v_text) then
      v_i:=v_i+1;
      v_offset:=0;
      continue;
    end if;

    v_take:=least(v_remaining,greatest(0,length(v_text)-v_offset));
    v_complete:=v_offset+v_take>=length(v_text);

    v_items:=v_items||jsonb_build_array(jsonb_build_object(
      'id',v_id,
      'label',case when v_session.content='full' then v_obj.title else null end,
      'content',v_session.content,
      'version',v_obj.version,'math_version',v_obj.math_version,
      'offset',v_offset,'segment',substr(v_text,v_offset+1,v_take),
      'complete',v_complete
    ));

    v_remaining:=v_remaining-v_take;

    if v_complete then
      v_i:=v_i+1;
      v_offset:=0;
    else
      v_offset:=v_offset+v_take;
    end if;
  end loop;

  if v_i>cardinality(v_session.object_ids) then
    v_next:=null;
  else
    v_next:=jsonb_build_object('index',v_i,'offset',v_offset);
  end if;

  update read_sessions
     set touched_at=now(),expires_at=now()+make_interval(mins=>v_ttl)
   where session_id=p_session_id;

  return jsonb_build_object(
    'session_id',p_session_id,'stale',false,
    'content',v_session.content,'consistency',v_session.consistency,
    'items',v_items,'next_cursor',v_next,'done',v_next is null,
    'manifest',case when v_next is null then jsonb_build_object(
      'object_ids',v_session.object_ids,
      'versions',case when v_session.consistency='math'
        then v_session.math_versions else v_session.versions end,
      'consistency',v_session.consistency
    ) else null end,
    'expires_at',now()+make_interval(mins=>v_ttl),
    'repository_revision',(select revision from state where singleton)
  );
end
$function$

```

## read_preview(p_ids text[]) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.read_preview(p_ids text[])
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$begin
  PERFORM control_center.active_project();
  
  RETURN (

  SELECT jsonb_build_object(
    'items',coalesce(jsonb_agg(jsonb_build_object(
      'id',o.id,
      'title',o.title,
      'object_type',o.object_type,
      'mathematical_status',o.mathematical_status,
      'audit_status',o.audit_status,
      'support_status',o.support_status,
      'math_version',o.math_version,
      'object_version',o.version,
      'statement_chars',length(coalesce(o.statement,'')),
      'body_chars',length(coalesce(o.body,'')),
      'estimated_full_math_chars',
        length(coalesce(o.statement,''))+length(coalesce(o.body,''))+128,
      'headings',markdown_headings(o.body)
    ) ORDER BY u.ord),'[]'::jsonb),
    'note','Use read_section for one Markdown section, or open_read_ex for exact paged multi-object reads. math_version is returned so staged work can explicitly watch the version actually read.'
  )
  FROM unnest(coalesce(p_ids,'{}'::text[])) WITH ORDINALITY u(id,ord)
  JOIN objects o ON o.id=u.id AND o.trashed_at IS NULL

  );
end$function$

```

## read_section(p_id text, p_heading text, p_occurrence integer DEFAULT 1) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.read_section(p_id text, p_heading text, p_occurrence integer DEFAULT 1)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
DECLARE
  o record;
  v_lines text[];
  v_i integer;
  v_j integer;
  v_match text[];
  v_next text[];
  v_level integer;
  v_seen integer:=0;
  v_start integer:=0;
  v_end integer:=0;
  v_text text:='';
  v_headings jsonb;
begin
  PERFORM control_center.active_project();
  
  IF p_heading IS NULL OR btrim(p_heading)='' THEN
    RAISE EXCEPTION 'section heading is required';
  END IF;
  IF coalesce(p_occurrence,0)<1 THEN
    RAISE EXCEPTION 'occurrence must be at least 1';
  END IF;

  SELECT * INTO o FROM objects
  WHERE id=p_id AND trashed_at IS NULL;
  IF o.id IS NULL THEN RAISE EXCEPTION 'object % not found',p_id; END IF;

  v_lines:=regexp_split_to_array(coalesce(o.body,''), E'\n');
  v_headings:=markdown_headings(o.body);

  FOR v_i IN 1..coalesce(array_length(v_lines,1),0)
  LOOP
    v_match:=regexp_match(v_lines[v_i], '^(#{1,6})[[:space:]]+(.+?)[[:space:]]*$');
    IF v_match IS NOT NULL
       AND lower(btrim(v_match[2]))=lower(btrim(p_heading)) THEN
      v_seen:=v_seen+1;
      IF v_seen=p_occurrence THEN
        v_start:=v_i;
        v_level:=length(v_match[1]);
        EXIT;
      END IF;
    END IF;
  END LOOP;

  IF v_start=0 THEN
    RETURN jsonb_build_object(
      'found',false,
      'id',o.id,
      'title',o.title,
      'math_version',o.math_version,
      'requested_heading',p_heading,
      'available_headings',v_headings
    );
  END IF;

  v_end:=coalesce(array_length(v_lines,1),v_start);
  IF v_start < coalesce(array_length(v_lines,1),0) THEN
    FOR v_j IN v_start+1..array_length(v_lines,1)
    LOOP
      v_next:=regexp_match(v_lines[v_j], '^(#{1,6})[[:space:]]+(.+?)[[:space:]]*$');
      IF v_next IS NOT NULL AND length(v_next[1])<=v_level THEN
        v_end:=v_j-1;
        EXIT;
      END IF;
    END LOOP;
  END IF;

  FOR v_i IN v_start..v_end
  LOOP
    v_text:=v_text||CASE WHEN v_i=v_start THEN '' ELSE E'\n' END||v_lines[v_i];
  END LOOP;

  RETURN jsonb_build_object(
    'found',true,
    'id',o.id,
    'title',o.title,
    'math_version',o.math_version,
    'object_version',o.version,
    'heading',p_heading,
    'heading_level',v_level,
    'occurrence',p_occurrence,
    'start_line',v_start,
    'end_line',v_end,
    'chars',length(v_text),
    'text',v_text,
    'watch_hint',jsonb_build_object(o.id,o.math_version)
  );
END
$function$

```

## reasoning_diagnostics(p_limit integer DEFAULT 100) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.reasoning_diagnostics(p_limit integer DEFAULT 100)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare
  v_limit integer := greatest(1,least(coalesce(p_limit,control_center.config_int('reasoning.diagnostics_default_limit')),control_center.config_int('reasoning.diagnostics_max_limit')));
begin
  PERFORM control_center.active_project();

  return (
    with toolkit_anchor as (
      select o.tree_path
      from objects o
      where o.id='methods01'
        and o.trashed_at is null
        and o.parent_id is null
        and coalesce((o.metadata->>'toolkit_home')::boolean,false)
      limit 1
    ),
    invalid_parent_all as (
      select
        rn.object_id as child_id,
        o.title as child_title,
        rn.node_kind as child_kind,
        o.parent_id,
        po.title as parent_title,
        prn.node_kind as parent_kind,
        case
          when o.parent_id is null then 'missing_parent'
          when po.id is null then 'parent_object_missing'
          when po.trashed_at is not null then 'parent_trashed'
          else 'parent_not_reasoning_annotated'
        end as reason
      from reasoning_nodes rn
      join objects o on o.id=rn.object_id
      left join objects po on po.id=o.parent_id
      left join reasoning_nodes prn on prn.object_id=o.parent_id
      where o.trashed_at is null
        and rn.node_kind in ('step','branch')
        and prn.node_kind is null
    ),
    invalid_parent_limited as (
      select * from invalid_parent_all order by child_id limit v_limit
    ),
    misplaced_standalone_all as (
      select
        o.id,o.title,o.parent_id,o.tree_path,o.object_type,o.research_level
      from objects o
      where o.trashed_at is null
        and o.lifecycle_status='active'
        and coalesce(o.unary_chain_standalone,false)
        and not exists (
          select 1 from toolkit_anchor a
          where o.tree_path like a.tree_path||'%'
        )
    ),
    misplaced_standalone_limited as (
      select * from misplaced_standalone_all order by id limit v_limit
    )
    select jsonb_build_object(
      'toolkit_root',
      coalesce(
        (select jsonb_build_object('id','methods01','tree_path',tree_path,'canonical',true) from toolkit_anchor),
        jsonb_build_object('id','methods01','missing_or_invalid',true,'canonical',true)
      ),
      'invalid_parent_semantics',
      jsonb_build_object(
        'count',(select count(*) from invalid_parent_all),
        'ids',coalesce((select jsonb_agg(child_id order by child_id) from invalid_parent_limited),'[]'::jsonb),
        'items',coalesce((
          select jsonb_agg(
            jsonb_build_object(
              'child_id',child_id,'child_title',child_title,'child_kind',child_kind,
              'parent_id',parent_id,'parent_title',parent_title,'parent_kind',parent_kind,
              'reason',reason
            ) order by child_id
          ) from invalid_parent_limited
        ),'[]'::jsonb),
        'truncated',(select count(*) from invalid_parent_all)>v_limit
      ),
      'standalone_outside_toolkit',
      jsonb_build_object(
        'count',(select count(*) from misplaced_standalone_all),
        'ids',coalesce((select jsonb_agg(id order by id) from misplaced_standalone_limited),'[]'::jsonb),
        'items',coalesce((
          select jsonb_agg(
            jsonb_build_object(
              'id',id,'title',title,'parent_id',parent_id,
              'object_type',object_type,'research_level',research_level,
              'reason','standalone_marker_requires_rehome_under_methods01'
            ) order by id
          ) from misplaced_standalone_limited
        ),'[]'::jsonb),
        'truncated',(select count(*) from misplaced_standalone_all)>v_limit
      ),
      'limit',v_limit
    )
  );
end
$function$

```

## reasoning_overview(p_root_id text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.reasoning_overview(p_root_id text)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare
  v_root_kind text;
  v_path text;
begin
  PERFORM control_center.active_project();

  select rn.node_kind,o.tree_path into v_root_kind,v_path
  from objects o join reasoning_nodes rn on rn.object_id=o.id
  where o.id=p_root_id and o.trashed_at is null;

  if v_root_kind is null then
    raise exception 'reasoning node % not found',p_root_id;
  end if;

  return jsonb_build_object(
    'root',object_capsule(p_root_id,control_center.config_int('text.preview_chars')),
    'node_kind',v_root_kind,
    'direct_children',(
      select coalesce(jsonb_agg(jsonb_build_object(
        'object',object_capsule(o.id,control_center.config_int('text.preview_chars')),
        'node_kind',rn.node_kind,
        'route_key',rn.route_key,
        'note',rn.note,
        'descendant_count',(
          select count(*)-1
          from objects d
          where d.trashed_at is null
            and d.tree_path like o.tree_path||'%'
        )
      ) order by o.position,o.updated_at),'[]'::jsonb)
      from objects o join reasoning_nodes rn on rn.object_id=o.id
      where o.parent_id=p_root_id and o.trashed_at is null
    ),
    'repository_revision',(select revision from state where singleton)
  );
end
$function$

```

## rebase_stage(p_worker_id bigint, p_stage_id bigint) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.rebase_stage(p_worker_id bigint, p_stage_id bigint)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_stage record;
  v_ttl integer;
begin
  PERFORM control_center.active_project();
  
  select * into v_stage from stages
   where stage_id=p_stage_id and owner_worker_id=p_worker_id
     and kind='batch' and expires_at>now()
   for update;
  if v_stage.stage_id is null then raise exception 'stage not found or expired'; end if;

  select stage_ttl_minutes into v_ttl from settings where singleton;

  update stages
     set baselines=stage_baselines(operations),
         read_math_baselines=(
           select coalesce(jsonb_object_agg(e.key,o.math_version),'{}'::jsonb)
             from jsonb_each(read_math_baselines) e
             join objects o on o.id=e.key and o.trashed_at is null
         ),
         stage_revision=stage_revision+1,
         verified_stage_revision=null,
         verified_digest=null,
         updated_at=now(),
         expires_at=now()+make_interval(mins=>v_ttl)
   where stage_id=p_stage_id
   returning * into v_stage;

  return to_jsonb(v_stage)||jsonb_build_object(
    'rebase_note','Baselines were explicitly acknowledged and reset to current values; verify again before commit.'
  );
end
$function$

```

## record_acceptance(p_architecture_version integer, p_suite_name text, p_passed boolean, p_details jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.record_acceptance(p_architecture_version integer, p_suite_name text, p_passed boolean, p_details jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_current integer;
  v_row record;
begin
  PERFORM control_center.active_project();
  
  select architecture_version into v_current
    from settings where singleton;

  if p_architecture_version<>v_current then
    raise exception 'acceptance result is for architecture version %, current is %',
      p_architecture_version,v_current;
  end if;
  if p_suite_name is null or btrim(p_suite_name)='' then
    raise exception 'suite_name required';
  end if;
  if jsonb_typeof(coalesce(p_details,'null'::jsonb))<>'object' then
    raise exception 'details must be a JSON object';
  end if;

  update acceptance_status
     set architecture_version=p_architecture_version,
         suite_name=p_suite_name,
         passed=p_passed,
         tested_at=now(),
         details=p_details
   where singleton
   returning * into v_row;

  return to_jsonb(v_row);
end
$function$

```

## reject_assignment_for_research(p_worker_id bigint, p_reason text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.reject_assignment_for_research(p_worker_id bigint, p_reason text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_claim record;
  v_snapshot jsonb;
  v_key text;
  v_suppressed_keys text[] := '{}'::text[];
  v_claim_id bigint;
  v_packet jsonb;
begin
  perform control_center.active_project();

  select * into v_claim
  from claims
  where worker_id=p_worker_id and expires_at>now()
  order by created_at desc
  limit 1
  for update;

  if v_claim.claim_id is null then
    raise exception 'no active assignment to reject';
  end if;

  v_snapshot := v_claim.payload->'_interrupted_research';
  if v_snapshot is null then
    raise exception 'current assignment was not created by a research-mode scheduler interruption';
  end if;

  -- Suppress currently active non-research needs for exactly the next
  -- scheduler dispatch. Existing TTL suppressions are separate rows and
  -- remain untouched.
  for v_key in
    select n.need_key
    from needs n
    where n.active
      and case n.need_key
        when 'audit' then 'audit'
        when 'global_synthesis' then 'coordination'
        when 'proof_rehearsal' then 'proof_rehearsal'
        when 'brainstorm' then 'brainstorm'
        when 'literature_bridge' then 'literature_bridge'
        when 'independent_attack' then 'research'
        when 'reasoning_hygiene' then 'reasoning_hygiene'
        when 'elevation' then 'research'
        when 'vote' then 'coordination'
      end <> 'research'
  loop
    perform control_center.suppress_need_for_worker(
      p_worker_id,
      v_key,
      coalesce(p_reason,'one-dispatch rejection to resume interrupted research'),
      'next_dispatch'
    );
    v_suppressed_keys := array_append(v_suppressed_keys,v_key);
  end loop;

  delete from presence where worker_id=p_worker_id;
  delete from transition_receipts where worker_id=p_worker_id;
  delete from claims where claim_id=v_claim.claim_id;

  update runs
  set mode=coalesce(v_snapshot->>'mode','research'),
      purpose=coalesce(v_snapshot->>'purpose','deep_research'),
      target_ids=coalesce(
        array(select jsonb_array_elements_text(coalesce(v_snapshot->'target_ids','[]'::jsonb))),
        '{}'::text[]
      ),
      focus_id=v_snapshot->>'focus_id',
      exclusive_key=v_snapshot->>'exclusive_key',
      need_key=v_snapshot->>'need_key',
      need_generation=nullif(v_snapshot->>'need_generation','')::bigint,
      payload=coalesce(v_snapshot->'payload','{}'::jsonb)
        || jsonb_build_object(
             'resumed_after_scheduler_rejection',true,
             'scheduler_rejection_reason',p_reason
           ),
      status='active',
      retired_at=null,
      compacted_at=null,
      updated_at=now()
  where worker_id=p_worker_id;

  -- assign_worker_core consumes next_dispatch suppressions as part of the
  -- successful scheduler decision. No caller-side cleanup is required.
  v_claim_id := control_center.assign_worker(p_worker_id);

  v_packet := control_center.sync(p_worker_id,null,true);

  return v_packet || jsonb_build_object(
    'rejected_assignment',v_claim.claim_id,
    'resumed_research',true,
    'one_dispatch_suppressions',to_jsonb(v_suppressed_keys)
  );
end
$function$

```

## release(p_worker_id bigint) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.release(p_worker_id bigint)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
DECLARE
  v_presence integer:=0;
  v_transition_receipts integer:=0;
BEGIN
  PERFORM control_center.active_project();
  DELETE FROM claims WHERE worker_id=p_worker_id;

  DELETE FROM presence WHERE worker_id=p_worker_id;
  GET DIAGNOSTICS v_presence=row_count;

  DELETE FROM transition_receipts WHERE worker_id=p_worker_id;
  GET DIAGNOSTICS v_transition_receipts=row_count;

  UPDATE runs
  SET status='released',
      retired_at=coalesce(retired_at,now()),
      expires_at=now(),
      payload=(coalesce(payload,'{}'::jsonb)-'_context_seen')
        ||jsonb_build_object('released_at',now(),'release_reason','explicit_release'),
      updated_at=now()
  WHERE worker_id=p_worker_id;

  RETURN jsonb_build_object(
    'released',true,
    'presence_cleared',v_presence,
    'transition_receipts_cleared',v_transition_receipts,
    'context_seen_cleared',true
  );
END
$function$

```

## release(p_worker_id bigint, p_receive_followup boolean) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.release(p_worker_id bigint, p_receive_followup boolean)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_result jsonb;
  v_pause_claim bigint;
begin
  perform control_center.active_project();

  v_result := control_center.release(p_worker_id);

  if not coalesce(p_receive_followup,true) then
    v_pause_claim := control_center.install_scheduler_pause(
      p_worker_id,'release_no_followup_requested'
    );
  end if;

  return v_result || jsonb_strip_nulls(jsonb_build_object(
    'receive_followup',coalesce(p_receive_followup,true),
    'scheduler_dispatch_paused',not coalesce(p_receive_followup,true),
    'pause_claim_id',v_pause_claim,
    'resume_rpc','resume_scheduler_dispatch(worker_id)'
  ));
end
$function$

```

## release_all_audit_claims(p_worker_id bigint, p_reason text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.release_all_audit_claims(p_worker_id bigint, p_reason text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_workers bigint[] := '{}'::bigint[];
  v_claim_count integer := 0;
  v_stage_count integer := 0;
  v_presence_count integer := 0;
  v_receipt_count integer := 0;
  v_run_count integer := 0;
  v_claims jsonb := '[]'::jsonb;
begin
  PERFORM control_center.active_project();

  select
    coalesce(array_agg(distinct worker_id), '{}'::bigint[]),
    coalesce(
      jsonb_agg(
        jsonb_build_object(
          'claim_id', claim_id,
          'worker_id', worker_id,
          'purpose', purpose,
          'focus_id', focus_id,
          'target_ids', target_ids,
          'expires_at', expires_at
        )
        order by created_at
      ),
      '[]'::jsonb
    )
  into v_workers, v_claims
  from claims
  where expires_at > now()
    and mode = 'audit';

  if cardinality(v_workers) = 0 then
    return jsonb_build_object(
      'released', true,
      'audit_claims_released', 0,
      'workers_released', '[]'::jsonb,
      'released_claims', '[]'::jsonb,
      'audit_stage_claims_cleared', 0,
      'presence_cleared', 0,
      'transition_receipts_cleared', 0,
      'active_runs_retired', 0,
      'reason', p_reason
    );
  end if;

  update stages s
     set claimed_by_worker_id = null,
         claimable = s.claimable,
         updated_at = now()
   where s.claimed_by_worker_id = any(v_workers)
     and s.mode = 'audit';
  get diagnostics v_stage_count = row_count;

  delete from presence
   where worker_id = any(v_workers);
  get diagnostics v_presence_count = row_count;

  delete from transition_receipts
   where worker_id = any(v_workers);
  get diagnostics v_receipt_count = row_count;

  delete from claims
   where expires_at > now()
     and mode = 'audit';
  get diagnostics v_claim_count = row_count;

  update runs
     set status = 'superseded',
         retired_at = coalesce(retired_at, now()),
         expires_at = now(),
         payload = (coalesce(payload, '{}'::jsonb) - '_context_seen')
           || jsonb_build_object(
                'released_at', now(),
                'release_reason', 'operator_release_all_audit_claims',
                'release_note', p_reason
              ),
         updated_at = now()
   where worker_id = any(v_workers)
     and status = 'active';
  get diagnostics v_run_count = row_count;

  return jsonb_build_object(
    'released', true,
    'audit_claims_released', v_claim_count,
    'workers_released', to_jsonb(v_workers),
    'released_claims', v_claims,
    'audit_stage_claims_cleared', v_stage_count,
    'presence_cleared', v_presence_count,
    'transition_receipts_cleared', v_receipt_count,
    'active_runs_retired', v_run_count,
    'reason', p_reason
  );
end
$function$

```

## release_all_audit_claims(p_worker_id bigint, p_reason text, p_receive_followup boolean) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.release_all_audit_claims(p_worker_id bigint, p_reason text, p_receive_followup boolean)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_result jsonb;
  v_worker_text text;
  v_paused jsonb:='[]'::jsonb;
  v_pause_claim bigint;
begin
  perform control_center.active_project();

  v_result := control_center.release_all_audit_claims(p_worker_id,p_reason);

  if not coalesce(p_receive_followup,true) then
    for v_worker_text in
      select value
      from jsonb_array_elements_text(coalesce(v_result->'workers_released','[]'::jsonb))
    loop
      v_pause_claim := control_center.install_scheduler_pause(
        v_worker_text::bigint,coalesce(p_reason,'release_all_audit_no_followup_requested')
      );
      v_paused := v_paused || jsonb_build_array(
        jsonb_build_object('worker_id',v_worker_text::bigint,'pause_claim_id',v_pause_claim)
      );
    end loop;
  end if;

  return v_result || jsonb_build_object(
    'receive_followup',coalesce(p_receive_followup,true),
    'scheduler_dispatch_paused_for_released_workers',not coalesce(p_receive_followup,true),
    'paused_workers',v_paused,
    'resume_rpc','resume_scheduler_dispatch(worker_id)'
  );
end
$function$

```

## release_audit_claims(p_worker_id bigint, p_reason text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.release_audit_claims(p_worker_id bigint, p_reason text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_claim_count integer:=0;
  v_stage_count integer:=0;
  v_presence_count integer:=0;
  v_receipt_count integer:=0;
  v_run_count integer:=0;
  v_claims jsonb:='[]'::jsonb;
begin
  perform control_center.active_project();

  select coalesce(
    jsonb_agg(
      jsonb_build_object(
        'claim_id',claim_id,
        'worker_id',worker_id,
        'purpose',purpose,
        'target_ids',target_ids,
        'expires_at',expires_at
      )
      order by created_at
    ),
    '[]'::jsonb
  )
  into v_claims
  from claims
  where worker_id=p_worker_id
    and expires_at>now()
    and mode='audit';

  update stages s
     set claimed_by_worker_id=null,
         claimable=s.claimable,
         updated_at=now()
   where s.claimed_by_worker_id=p_worker_id
     and s.mode='audit';
  get diagnostics v_stage_count=row_count;

  delete from claims
   where worker_id=p_worker_id
     and expires_at>now()
     and mode='audit';
  get diagnostics v_claim_count=row_count;

  if v_claim_count>0 then
    delete from presence where worker_id=p_worker_id;
    get diagnostics v_presence_count=row_count;

    delete from transition_receipts where worker_id=p_worker_id;
    get diagnostics v_receipt_count=row_count;

    update runs
       set status='released',
           retired_at=coalesce(retired_at,now()),
           expires_at=now(),
           payload=(coalesce(payload,'{}'::jsonb)-'_context_seen')
             ||jsonb_build_object(
                 'released_at',now(),
                 'release_reason','release_audit_claims',
                 'release_note',p_reason
               ),
           updated_at=now()
     where worker_id=p_worker_id
       and status='active'
       and mode='audit';
    get diagnostics v_run_count=row_count;
  end if;

  return jsonb_build_object(
    'released',true,
    'worker_id',p_worker_id,
    'audit_claims_released',v_claim_count,
    'released_claims',v_claims,
    'audit_stage_claims_cleared',v_stage_count,
    'presence_cleared',v_presence_count,
    'transition_receipts_cleared',v_receipt_count,
    'active_audit_runs_retired',v_run_count,
    'reason',p_reason
  );
end
$function$

```

## release_audit_claims(p_worker_id bigint, p_reason text, p_receive_followup boolean) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.release_audit_claims(p_worker_id bigint, p_reason text, p_receive_followup boolean)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_result jsonb;
  v_pause_claim bigint;
begin
  perform control_center.active_project();

  v_result := control_center.release_audit_claims(p_worker_id,p_reason);

  if not coalesce(p_receive_followup,true)
     and coalesce((v_result->>'audit_claims_released')::integer,0)>0
  then
    v_pause_claim := control_center.install_scheduler_pause(
      p_worker_id,coalesce(p_reason,'audit_release_no_followup_requested')
    );
  end if;

  return v_result || jsonb_strip_nulls(jsonb_build_object(
    'receive_followup',coalesce(p_receive_followup,true),
    'scheduler_dispatch_paused',v_pause_claim is not null,
    'pause_claim_id',v_pause_claim,
    'resume_rpc','resume_scheduler_dispatch(worker_id)'
  ));
end
$function$

```

## remove_edge(p_worker_id bigint, p_from_id text, p_to_id text, p_kind text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.remove_edge(p_worker_id bigint, p_from_id text, p_to_id text, p_kind text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_kind text:=case when p_kind='proof' then 'depends_on' else p_kind end;
  v_count integer;
  v_rev bigint;
  v_from_certified boolean:=false;
  v_edge_metadata jsonb:='{}'::jsonb;
  v_removed_structural boolean:=false;
  v_supersession_reconcile jsonb;
begin
  perform control_center.active_project();

  if v_kind='depends_on' then
    select (audit_status='certified')
      into v_from_certified
    from objects
    where id=p_from_id and trashed_at is null
    for update;
  end if;

  select coalesce(metadata,'{}'::jsonb)
    into v_edge_metadata
  from edges
  where from_id=p_from_id and to_id=p_to_id and kind=v_kind
  for update;

  if not found then
    raise exception 'edge not found';
  end if;

  v_removed_structural :=
    v_kind='supersedes'
    and coalesce((v_edge_metadata->>'structural_retirement')::boolean,false);

  delete from edges
  where from_id=p_from_id and to_id=p_to_id and kind=v_kind;
  get diagnostics v_count=row_count;

  if v_kind='depends_on'
     and coalesce(v_from_certified,false)
     and exists(select 1 from certificates where object_id=p_from_id) then
    update certificates
       set premise_manifest=premise_manifest(p_from_id),
           premise_signature=premise_signature(p_from_id)
     where object_id=p_from_id;
    perform refresh_support(p_from_id);
    perform refresh_dependents(array[p_from_id]);
  end if;

  if v_kind='supersedes' then
    v_supersession_reconcile :=
      control_center.reconcile_supersession_target(
        p_to_id,
        v_removed_structural
      );
  end if;

  v_rev:=record_change(
    'remove_edge',
    array[p_from_id,p_to_id],
    jsonb_build_object(
      'kind',v_kind,
      'requested_kind',p_kind,
      'mathematical_dependency',v_kind='depends_on',
      'consumer_certification_preserved',v_kind='depends_on' and coalesce(v_from_certified,false),
      'structural_supersession_removed',v_removed_structural,
      'supersession_reconcile',v_supersession_reconcile
    )
  );

  return jsonb_build_object(
    'removed',true,
    'kind',v_kind,
    'supersession_reconcile',v_supersession_reconcile,
    'repository_revision',v_rev
  );
end
$function$

```

## remove_standardization_term(p_worker_id bigint, p_term text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.remove_standardization_term(p_worker_id bigint, p_term text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$begin
  PERFORM control_center.active_project();
  
  RETURN (

  SELECT core_remove_standardization_term(p_worker_id,p_term)

  );
end$function$

```

## replace_dependency(p_worker_id bigint, p_consumer_id text, p_old_premise_id text, p_new_premise_id text, p_expected_new_premise_math_version bigint, p_note text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.replace_dependency(p_worker_id bigint, p_consumer_id text, p_old_premise_id text, p_new_premise_id text, p_expected_new_premise_math_version bigint, p_note text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_remove jsonb;
  v_add jsonb;
begin
  PERFORM control_center.active_project();
  
  if not touch_worker_claim(p_worker_id) then
    raise exception 'active worker claim required';
  end if;

  if not exists(
    select 1 from edges
    where from_id=p_consumer_id and to_id=p_old_premise_id and kind='depends_on'
  ) then
    raise exception 'old logical dependency % -> % not found',
      p_consumer_id,p_old_premise_id;
  end if;

  v_remove:=control_center.remove_edge(
    p_worker_id,p_consumer_id,p_old_premise_id,'depends_on'
  );

  v_add:=control_center.add_edge(
    p_worker_id,p_consumer_id,p_new_premise_id,'depends_on',
    jsonb_build_object(
      'expected_math_version',p_expected_new_premise_math_version,
      'replacement_note',p_note
    )
  );

  return jsonb_build_object(
    'replaced',true,
    'consumer_id',p_consumer_id,
    'old_premise_id',p_old_premise_id,
    'new_premise_id',p_new_premise_id,
    'remove',v_remove,
    'add',v_add
  );
end
$function$

```

## replace_stage(p_worker_id bigint, p_stage_id bigint, p_operations jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.replace_stage(p_worker_id bigint, p_stage_id bigint, p_operations jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
begin
  PERFORM control_center.active_project();
  
  raise exception 'replace_stage requires explicit stage revision; use replace_stage_v2(worker_id,stage_id,expected_stage_revision,operations)';
end
$function$

```

## replace_stage_v2(p_worker_id bigint, p_stage_id bigint, p_expected_stage_revision bigint, p_operations jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.replace_stage_v2(p_worker_id bigint, p_stage_id bigint, p_expected_stage_revision bigint, p_operations jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_stage record;
  v_ops jsonb;
  v_new_base jsonb;
  v_missing_base jsonb;
  v_required_reads jsonb;
  v_explicit_ids text[];
  v_read_keys text[];
  v_new_reads jsonb:='{}'::jsonb;
  v_id text;
  v_old_value jsonb;
  v_current_value bigint;
  v_ttl integer;
begin
  PERFORM control_center.active_project();
  
  select * into v_stage from stages
   where stage_id=p_stage_id and owner_worker_id=p_worker_id
     and kind='batch' and expires_at>now()
   for update;

  if v_stage.stage_id is null then raise exception 'mutable batch stage not found'; end if;
  if v_stage.stage_revision<>p_expected_stage_revision then
    raise exception 'stage revision conflict: expected %, current %',
      p_expected_stage_revision,v_stage.stage_revision;
  end if;

  v_ops:=normalize_stage_operations(p_operations);
  v_new_base:=stage_baselines(v_ops);
  v_required_reads:=stage_math_read_baselines(v_ops);

  select coalesce(jsonb_object_agg(e.key,e.value),'{}'::jsonb)
    into v_missing_base
    from jsonb_each(v_new_base) e
   where not (v_stage.baselines ? e.key);

  select coalesce(array_agg(x),'{}'::text[])
    into v_explicit_ids
  from jsonb_array_elements_text(
    coalesce(v_stage.payload->'explicit_watch_ids','[]'::jsonb)
  ) x;

  select coalesce(array_agg(distinct key),'{}'::text[])
    into v_read_keys
  from (
    select key from jsonb_each(v_required_reads)
    union
    select unnest(v_explicit_ids)
  ) q;

  foreach v_id in array v_read_keys
  loop
    v_old_value:=v_stage.read_math_baselines->v_id;

    if v_old_value is not null then
      -- Authoritative: preserve the exact version previously read, even if the
      -- object is now missing/trashed. Verification must surface that conflict.
      v_new_reads:=v_new_reads||jsonb_build_object(v_id,v_old_value);
    else
      select math_version into v_current_value
        from objects
       where id=v_id and trashed_at is null;

      if v_current_value is not null then
        v_new_reads:=v_new_reads||jsonb_build_object(v_id,v_current_value);
      elsif v_required_reads ? v_id then
        v_new_reads:=v_new_reads||jsonb_build_object(v_id,v_required_reads->v_id);
      else
        raise exception 'explicit watched object % has no preserved baseline; reopen/review rather than silently dropping it',v_id;
      end if;
    end if;
  end loop;

  select stage_ttl_minutes into v_ttl
    from settings where singleton;

  update stages
     set operations=v_ops,
         baselines=v_stage.baselines||v_missing_base,
         read_math_baselines=v_new_reads,
         stage_revision=stage_revision+1,
         verified_stage_revision=null,
         verified_digest=null,
         updated_at=now(),
         expires_at=now()+make_interval(mins=>v_ttl)
   where stage_id=p_stage_id
   returning * into v_stage;

  return to_jsonb(v_stage);
end
$function$

```

## request_assignment(p_worker_id bigint DEFAULT NULL::bigint, p_intent jsonb DEFAULT '{}'::jsonb, p_priority integer DEFAULT 80, p_timing text DEFAULT 'next_boundary'::text, p_scope text DEFAULT 'next_assignment'::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.request_assignment(p_worker_id bigint DEFAULT NULL::bigint, p_intent jsonb DEFAULT '{}'::jsonb, p_priority integer DEFAULT 80, p_timing text DEFAULT 'next_boundary'::text, p_scope text DEFAULT 'next_assignment'::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_mode text;
  v_role text;
  v_task text;
  v_targets text[]:='{}'::text[];
  v_bad text;
  v_scope text:=lower(btrim(coalesce(p_scope,'next_assignment')));
  v_timing text:=lower(btrim(coalesce(p_timing,'next_boundary')));
  v_ttl integer;
  v_request bigint;
  v_target_worker bigint;
  v_initial text;
  v_clean_intent jsonb;
  v_current_need_key text;
begin
  perform control_center.active_project();

  if jsonb_typeof(coalesce(p_intent,'null'::jsonb))<>'object' then
    raise exception 'assignment request intent must be a JSON object';
  end if;

  if p_priority<control_center.config_int('priority.min') or p_priority>control_center.config_int('priority.max') then
    raise exception 'assignment request priority must be between 0 and 100';
  end if;

  if v_timing not in ('next_boundary','now_if_safe') then
    raise exception 'unsupported assignment request timing %',v_timing;
  end if;

  if v_scope not in ('next_assignment','this_worker','until_satisfied','next_worker') then
    raise exception 'unsupported assignment request scope %',v_scope;
  end if;

  v_role:=lower(btrim(coalesce(p_intent->>'role','')));
  v_mode:=lower(btrim(coalesce(p_intent->>'mode','')));

  if v_mode='' then
    v_mode:=case v_role
      when 'researcher' then 'research'
      when 'research' then 'research'
      when 'auditor' then 'audit'
      when 'audit' then 'audit'
      when 'coordinator' then 'coordination'
      when 'coordinate' then 'coordination'
      when 'coordination' then 'coordination'
      when '' then 'research'
      else v_role
    end;
  end if;

  if v_mode not in (
    'research','isolated_research','audit','coordination','proof_rehearsal',
    'literature_bridge'
  ) then
    raise exception 'unsupported requested assignment mode %',v_mode;
  end if;

  if v_mode in ('research','isolated_research') and not control_center.research_mode_enabled(v_mode) then
    raise exception 'requested research mode % is disabled',v_mode;
  end if;

  v_task:=nullif(btrim(coalesce(p_intent->>'task','')),'' );

  if p_intent ? 'target_ids' then
    if jsonb_typeof(p_intent->'target_ids')<>'array' then
      raise exception 'intent.target_ids must be a JSON array';
    end if;

    select coalesce(array_agg(value order by ord),'{}'::text[])
    into v_targets
    from jsonb_array_elements_text(p_intent->'target_ids')
         with ordinality q(value,ord);

    if cardinality(v_targets)>control_center.config_int('assignment.max_target_ids') then
      raise exception 'assignment request exceeds configured target_id maximum %',control_center.config_int('assignment.max_target_ids');
    end if;

    select x into v_bad
    from unnest(v_targets) x
    where not exists(
      select 1 from objects o where o.id=x and o.trashed_at is null
    )
    limit 1;

    if v_bad is not null then
      raise exception 'requested target % is not a live object',v_bad;
    end if;
  end if;

  if p_worker_id is not null then
    select need_key into v_current_need_key
    from claims
    where worker_id=p_worker_id and expires_at>now()
    order by created_at desc
    limit 1;

    if v_current_need_key is not null then
      perform control_center.suppress_need_for_worker(
        p_worker_id,v_current_need_key,
        'worker requested a different assignment'
      );
    end if;
  end if;

  if v_mode='audit' then
    perform raise_need(
      'audit',p_priority,
      coalesce(v_task,'Explicit audit request routed through the universal audit need.'),
      v_targets,'{}'::bigint[]
    );
    return jsonb_build_object(
      'status','routed_to_need',
      'need_key','audit',
      'priority',p_priority,
      'target_ids',to_jsonb(v_targets),
      'contract','Audit requests enter the universal needs system; concrete batches remain worker-eligible and nonoverlapping.'
    );
  end if;

  -- Research assignment requests are mode-only. The scheduler must never
  -- steer a researcher toward a mathematical topic, target, or route.
  if v_mode in ('research','isolated_research') then
    v_task:=null;
    v_targets:='{}'::text[];
    v_clean_intent := (p_intent - 'focus_id' - 'task' - 'target_ids')
      || jsonb_build_object('mode',v_mode);
  else
    v_clean_intent := (p_intent - 'focus_id') || jsonb_build_object('mode',v_mode);
  end if;

  if p_worker_id is null then
    v_target_worker:=null;
    if v_scope not in ('next_worker','until_satisfied') then
      v_scope:='next_worker';
    end if;
  elsif v_scope='next_worker' then
    v_target_worker:=null;
  else
    v_target_worker:=p_worker_id;
  end if;

  select assignment_request_ttl_hours into v_ttl
  from settings where singleton;

  if v_scope in ('next_assignment','next_worker') then
    update assignment_requests
    set status='superseded',
        disposition=jsonb_build_object(
          'reason','superseded_by_newer_request',
          'superseded_at',now()
        ),
        consumed_at=now(),
        updated_at=now()
    where status='pending'
      and scope=v_scope
      and target_worker_id is not distinct from v_target_worker;
  end if;

  if v_target_worker is not null and exists(
    select 1 from claims
    where worker_id=v_target_worker and expires_at>now()
  ) then
    v_initial:=case when v_timing='now_if_safe'
      then 'queued_now_if_safe'
      else 'queued_for_boundary'
    end;
  else
    v_initial:='eligible_at_next_dispatch';
  end if;

  insert into assignment_requests(
    requested_by_worker_id,target_worker_id,intent,requested_mode,task,
    focus_id,target_ids,priority,timing,scope,status,disposition,expires_at
  ) values (
    p_worker_id,v_target_worker,
    v_clean_intent,
    v_mode,v_task,null,v_targets,p_priority,v_timing,v_scope,'pending',
    jsonb_build_object(
      'state',v_initial,
      'note',case when v_mode in ('research','isolated_research')
        then 'Research-mode preference recorded. Research task/target hints are discarded; the researcher chooses the mathematical route independently.'
        else 'Preference recorded. Concrete non-research obligations may use target_ids.'
      end
    ),
    now()+make_interval(hours=>v_ttl)
  )
  returning request_id into v_request;

  return jsonb_build_object(
    'request_id',v_request,
    'status','pending',
    'requested_mode',v_mode,
    'priority',p_priority,
    'timing',v_timing,
    'scope',v_scope,
    'target_worker_id',v_target_worker,
    'expires_at',now()+make_interval(hours=>v_ttl),
    'disposition',v_initial,
    'focus_semantics','abolished',
    'contract',case when v_mode in ('research','isolated_research')
      then 'This is a mode-only scheduler preference. Research task, target, focus, and route hints are discarded before dispatch.'
      else 'This is a soft scheduler preference for a non-research operational mode.'
    end
  );
end
$function$

```

## request_audit(p_worker_id bigint, p_id text, p_priority integer DEFAULT 50, p_reason text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.request_audit(p_worker_id bigint, p_id text, p_priority integer DEFAULT 50, p_reason text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_old record;
  v_row record;
  v_rev bigint;
  v_reaudit boolean;
begin
  PERFORM control_center.active_project();
  
  select * into v_old from objects
   where id=p_id and trashed_at is null
     and mathematical_status in ('proved','evidence')
   for update;

  if v_old.id is null then
    raise exception 'auditable mathematical object % not found',p_id;
  end if;

  v_reaudit:=v_old.audit_status='certified';

  if v_reaudit and (p_reason is null or btrim(p_reason)='') then
    raise exception 'explicit re-audit of certified object % requires a reason',p_id;
  end if;

  if v_old.audit_status='failed' then
    raise exception 'failed object % must be mathematically repaired before re-audit',p_id;
  end if;

  update objects
     set audit_requested=true,
         audit_status='pending',
         audited_math_version=null,
         audit_priority=greatest(audit_priority,greatest(control_center.config_int('priority.min'),least(control_center.config_int('priority.max'),p_priority))),
         support_status=case when mathematical_status='evidence' then 'evidence' else 'unchecked' end,
         support_reason=case
           when mathematical_status='evidence' then 'finite_or_empirical_evidence'
           when v_reaudit then 'explicit re-audit requested'
           else support_reason
         end,
         metadata=coalesce(metadata,'{}'::jsonb)||jsonb_strip_nulls(jsonb_build_object(
           'audit_trigger_kind',coalesce(metadata->>'audit_trigger_kind','explicit'),
           'audit_request_reason',p_reason,
           'audit_request_recorded_at',now()
         )),
         version=version+1,
         updated_at=now()
   where id=p_id
   returning * into v_row;

  if v_reaudit then
    perform invalidate_dependents(array[p_id],'explicit re-audit requested');
    perform refresh_dependents(array[p_id]);
  end if;

  v_rev:=record_change(
    case when v_reaudit then 'request_reaudit' else 'request_audit' end,
    array[p_id],
    jsonb_build_object('priority',p_priority,'reason',p_reason)
  );

  return to_jsonb(v_row)||jsonb_build_object(
    'repository_revision',v_rev,
    'reaudit',v_reaudit,
    'prior_certificate_preserved',v_reaudit
  );
end
$function$

```

## request_chain_audit(p_worker_id bigint, p_root_id text, p_priority integer DEFAULT 100, p_reason text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.request_chain_audit(p_worker_id bigint, p_root_id text, p_priority integer DEFAULT 100, p_reason text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_root text;
  v_ids text[];
  v_count integer;
  v_rev bigint;
begin
  perform control_center.active_project();
  v_root := control_center.canonical_object_id(p_root_id);

  if not exists(select 1 from objects where id=v_root and trashed_at is null) then
    raise exception 'chain root % not found',p_root_id;
  end if;

  with recursive support(id) as (
    select v_root
    union
    select e.to_id
    from support s
    join edges e on e.from_id=s.id and e.kind='depends_on'
    join objects o on o.id=e.to_id and o.trashed_at is null
  )
  select coalesce(array_agg(distinct id),'{}'::text[]) into v_ids
  from support;

  update objects o
     set audit_requested=true,
         audit_status=case
           when o.audit_status='certified' then o.audit_status
           else 'pending'
         end,
         audit_priority=greatest(o.audit_priority,greatest(control_center.config_int('priority.min'),least(control_center.config_int('priority.max'),p_priority))),
         metadata=coalesce(o.metadata,'{}'::jsonb)||jsonb_strip_nulls(jsonb_build_object(
           'audit_trigger_kind','chain_checkpoint',
           'audit_chain_root',v_root,
           'audit_request_reason',coalesce(nullif(btrim(coalesce(p_reason,'')),''),'strong theorem-facing reasoning chain'),
           'audit_request_recorded_at',now()
         )),
         version=version+1,
         updated_at=now()
   where o.id=any(v_ids)
     and o.mathematical_status in ('proved','evidence')
     and (
       o.audit_status='pending'
       or (
         o.audit_status='certified'
         and o.support_status='stale'
         and o.support_reason='logical_premise_math_changed'
       )
     );
  get diagnostics v_count=row_count;

  perform control_center.refresh_scheduler_pressures();

  v_rev:=control_center.record_change(
    'request_chain_audit',
    v_ids,
    jsonb_build_object(
      'root_id',v_root,
      'priority',p_priority,
      'reason',p_reason,
      'requested_count',v_count,
      'requested_by_worker_id',p_worker_id
    )
  );

  return jsonb_build_object(
    'root_id',v_root,
    'support_ids',to_jsonb(v_ids),
    'requested_count',v_count,
    'repository_revision',v_rev
  );
end
$function$

```

## request_reaudit(p_worker_id bigint, p_id text, p_priority integer, p_reason text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.request_reaudit(p_worker_id bigint, p_id text, p_priority integer, p_reason text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$begin
  PERFORM control_center.active_project();
  
  RETURN (

  select control_center.request_audit(p_worker_id,p_id,p_priority,p_reason)

  );
end$function$

```

## require_verification(p_worker_id bigint, p_id text, p_requirement text, p_reason text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.require_verification(p_worker_id bigint, p_id text, p_requirement text, p_reason text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_current text;
  v_new_rank integer;
  v_old_rank integer;
  v_row record;
  v_rev bigint;
begin
  PERFORM control_center.active_project();
  
  if p_requirement not in (
    'independent_check','independent_reconstruction','alternate_method'
  ) then
    raise exception 'invalid audit requirement %',p_requirement;
  end if;

  if not exists(
    select 1 from claims
     where worker_id=p_worker_id and expires_at>now()
  ) then
    raise exception 'verification requirement change requires active worker claim';
  end if;

  if p_reason is null or btrim(p_reason)='' then
    raise exception 'verification requirement change requires a reason';
  end if;

  select audit_requirement into v_current from objects
   where id=p_id and trashed_at is null for update;
  if v_current is null then raise exception 'object % not found',p_id; end if;

  v_old_rank:=case v_current
    when 'independent_check' then 1
    when 'independent_reconstruction' then 2
    when 'alternate_method' then 3 end;
  v_new_rank:=case p_requirement
    when 'independent_check' then 1
    when 'independent_reconstruction' then 2
    when 'alternate_method' then 3 end;

  

  update objects
     set audit_requirement=p_requirement,
         audit_requested=case
           when audit_status='certified' and v_new_rank>v_old_rank then true
           else audit_requested end,
         audit_status=case
           when audit_status='certified' and v_new_rank>v_old_rank then 'pending'
           else audit_status end,
         audited_math_version=case
           when audit_status='certified' and v_new_rank>v_old_rank then null
           else audited_math_version end,
         support_status=case
           when audit_status='certified' and v_new_rank>v_old_rank then 'unchecked'
           else support_status end,
         support_reason=case
           when audit_status='certified' and v_new_rank>v_old_rank
             then 'stronger verification requirement requested'
           else support_reason end,
         metadata=metadata||jsonb_build_object(
           'verification_requirement_reason',
           jsonb_build_object(
             'requirement',p_requirement,'reason',p_reason,'recorded_at',now()
           )
         ),
         version=version+1,
         updated_at=now()
   where id=p_id
   returning * into v_row;

  if v_new_rank>v_old_rank then
    delete from certificates where object_id=p_id;
    perform invalidate_dependents(
      array[p_id],'stronger verification requirement requested'
    );
  end if;

  v_rev:=record_change(
    'set_audit_requirement',array[p_id],
    jsonb_build_object(
      'old',v_current,'new',p_requirement,'reason',p_reason
    )
  );

  return to_jsonb(v_row)||jsonb_build_object('repository_revision',v_rev);
end
$function$

```

## resolve_poll_action(p_worker_id bigint, p_poll_id bigint, p_outcome text, p_details jsonb DEFAULT '{}'::jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.resolve_poll_action(p_worker_id bigint, p_poll_id bigint, p_outcome text, p_details jsonb DEFAULT '{}'::jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
DECLARE
  p record;
  v_outcome text:=lower(btrim(coalesce(p_outcome,'')));
  v_rev bigint;
BEGIN
  PERFORM control_center.active_project();

  IF v_outcome NOT IN ('enacted','deferred') THEN
    RAISE EXCEPTION 'poll action outcome must be enacted or deferred';
  END IF;
  IF p_details IS NULL OR jsonb_typeof(p_details)<>'object' THEN
    RAISE EXCEPTION 'details must be a JSON object';
  END IF;

  SELECT * INTO p
  FROM polls
  WHERE poll_id=p_poll_id
  FOR UPDATE;

  IF p.poll_id IS NULL THEN
    RAISE EXCEPTION 'poll % not found',p_poll_id;
  END IF;
  IF p.status<>'passed_pending_action' THEN
    RAISE EXCEPTION 'poll % does not have a passed action awaiting enactment',p_poll_id;
  END IF;

  IF p.action_claimed_by IS NOT NULL
     AND p.action_claimed_by<>p_worker_id
     AND p.action_claim_expires_at IS NOT NULL
     AND p.action_claim_expires_at>now()
     AND p.closed_by_worker_id<>p_worker_id
  THEN
    RAISE EXCEPTION 'poll % action is currently leased to another worker',p_poll_id;
  END IF;

  IF v_outcome='enacted' THEN
    UPDATE polls
    SET status='enacted',
        enacted_at=now(),
        enacted_by_worker_id=p_worker_id,
        action_resolution=coalesce(p_details,'{}'::jsonb),
        action_claimed_by=null,
        action_claim_expires_at=null,
        updated_at=now()
    WHERE poll_id=p_poll_id
    RETURNING * INTO p;

    v_rev:=record_change(
      'poll_action_enacted',
      p.target_ids,
      jsonb_build_object(
        'poll_id',p_poll_id,
        'action',p.action,
        'details',coalesce(p_details,'{}'::jsonb)
      )
    );

    PERFORM control_center.refresh_vote_need();

    RETURN jsonb_build_object(
      'poll_id',p_poll_id,
      'status','enacted',
      'action',p.action,
      'details',p.action_resolution,
      'repository_revision',v_rev,
      'next_action','The passed poll action is recorded as enacted; its scheduler pressure is cleared when no other poll work remains.'
    );
  END IF;

  UPDATE polls
  SET last_deferred_at=now(),
      last_deferred_by=p_worker_id,
      deferral_count=deferral_count+1,
      action_resolution=coalesce(p_details,'{}'::jsonb),
      action_claimed_by=null,
      action_claim_expires_at=null,
      updated_at=now()
  WHERE poll_id=p_poll_id
  RETURNING * INTO p;

  v_rev:=record_change(
    'poll_action_deferred',
    p.target_ids,
    jsonb_build_object(
      'poll_id',p_poll_id,
      'action_pending',true,
      'deferral_count',p.deferral_count,
      'details',coalesce(p_details,'{}'::jsonb)
    )
  );

  PERFORM control_center.refresh_vote_need();

  RETURN jsonb_build_object(
    'poll_id',p_poll_id,
    'status','passed_pending_action',
    'action',p.action,
    'deferred',true,
    'repository_revision',v_rev,
    'next_action','The action remains mandatory because the poll passed. The scheduler will keep raising the vote need until someone enacts it.'
  );
END
$function$

```

## resolve_signal(p_worker_id bigint, p_signal_id bigint, p_status text DEFAULT 'resolved'::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.resolve_signal(p_worker_id bigint, p_signal_id bigint, p_status text DEFAULT 'resolved'::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$begin
  PERFORM control_center.active_project();
  
  RETURN (

  select resolve_signal(p_signal_id,p_status)

  );
end$function$

```

## restore_subtrees(p_worker_id bigint, p_ids text[]) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.restore_subtrees(p_worker_id bigint, p_ids text[])
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_paths text[] := '{}'::text[];
  v_roots text[] := (coalesce(p_ids,'{}'::text[]))[1:control_center.config_int('tree.max_batch_roots')];
  v_id text;
  v_path text;
  v_count integer;
  v_rev bigint;
begin
  PERFORM control_center.active_project();
  
  foreach v_id in array coalesce(p_ids,'{}'::text[])
  loop
    select tree_path into v_path from objects where id=v_id;
    if v_path is not null then v_paths:=v_paths||v_path; end if;
  end loop;

  if cardinality(v_paths)=0 then return jsonb_build_object('restored',0); end if;

  update objects o
     set trashed_at=null,
         attention=case when attention='hidden' then 'available' else attention end,
         updated_at=now(),
         version=version+1
   where o.trashed_at is not null
     and exists(select 1 from unnest(v_paths) p where o.tree_path like p||'%');
  get diagnostics v_count=row_count;

  v_rev:=record_change('restore_subtrees',v_roots,
    jsonb_build_object('roots',v_roots,'objects_touched',v_count));

  return jsonb_build_object('restored',v_count,'repository_revision',v_rev);
end
$function$

```

## resume_scheduler_dispatch(p_worker_id bigint, p_dispatch_now boolean DEFAULT false) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.resume_scheduler_dispatch(p_worker_id bigint, p_dispatch_now boolean DEFAULT false)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_pause_claims integer:=0;
  v_packet jsonb;
begin
  perform control_center.active_project();

  delete from claims
   where worker_id=p_worker_id
     and purpose='scheduler_dispatch_paused_manual_mission'
     and coalesce((payload->>'scheduler_dispatch_paused')::boolean,false);
  get diagnostics v_pause_claims=row_count;

  delete from presence where worker_id=p_worker_id;
  delete from transition_receipts where worker_id=p_worker_id;

  update runs
     set status='released',
         retired_at=coalesce(retired_at,now()),
         expires_at=now(),
         payload=(coalesce(payload,'{}'::jsonb)-'_context_seen')
           ||jsonb_build_object(
               'scheduler_dispatch_resumed_at',now(),
               'scheduler_dispatch_paused',false
             ),
         updated_at=now()
   where worker_id=p_worker_id
     and purpose='scheduler_dispatch_paused_manual_mission';

  if coalesce(p_dispatch_now,false) then
    v_packet:=control_center.startup(p_worker_id);
  end if;

  return jsonb_strip_nulls(jsonb_build_object(
    'worker_id',p_worker_id,
    'resumed',true,
    'pause_claims_cleared',v_pause_claims,
    'dispatch_now',coalesce(p_dispatch_now,false),
    'dispatch_packet',v_packet
  ));
end
$function$

```

## review_brainstorm_need(p_worker_id bigint, p_decision text, p_reason text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.review_brainstorm_need(p_worker_id bigint, p_decision text, p_reason text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_claim record; v_decision text:=lower(btrim(coalesce(p_decision,'')));
  v_reason text:=nullif(btrim(p_reason),''); v_rev bigint; v_delta integer;
begin
  perform control_center.active_project();
  if v_decision not in ('proceed','defer') then raise exception 'decision must be proceed or defer'; end if;

  select * into v_claim from claims
  where worker_id=p_worker_id and expires_at>now() and need_key='brainstorm'
  order by created_at desc limit 1 for update;
  if v_claim.claim_id is null then raise exception 'active brainstorm assignment not found'; end if;

  if v_decision='proceed' then
    update claims set payload=payload||jsonb_strip_nulls(jsonb_build_object(
      'brainstorm_review_decision','proceed','brainstorm_review_reason',v_reason,'brainstorm_review_at',now()))
    where claim_id=v_claim.claim_id;
    return jsonb_build_object('decision','proceed','need_key','brainstorm');
  end if;

  if v_reason is null then raise exception 'defer requires a reason'; end if;
  v_delta:=-control_center.config_int('brainstorm.defer_offset_step');
  update needs
  set priority_offset=priority_offset+v_delta,
      reason=left(coalesce(reason||E'\n','')||'Brainstorm deferred: '||v_reason,control_center.config_int('text.large_chars')),
      updated_at=now(),last_outcome='deferred'
  where need_key='brainstorm';
  perform control_center.suppress_need_for_worker(p_worker_id,'brainstorm',v_reason,'next_dispatch');
  v_rev:=record_change('defer_brainstorm','{}'::text[],jsonb_build_object('reason',v_reason,'priority_offset_delta',v_delta));
  return jsonb_build_object('decision','defer','priority_offset_delta',v_delta,
    'brainstorm_priority',control_center.need_effective_priority('brainstorm'),
    'repository_revision',v_rev,'next_action','Call next(worker_id,''deferred'',details).');
end $function$

```

## revise_current(p_worker_id bigint, p_id text, p_patch jsonb, p_substantive boolean DEFAULT true, p_expected_math_version bigint DEFAULT NULL::bigint) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.revise_current(p_worker_id bigint, p_id text, p_patch jsonb, p_substantive boolean DEFAULT true, p_expected_math_version bigint DEFAULT NULL::bigint)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_id text;
  v_version bigint;
  v_math_version bigint;
  v_result jsonb;
begin
  perform control_center.active_project();
  v_id:=control_center.canonical_object_id(p_id);
  select version,math_version into v_version,v_math_version
  from objects where id=v_id and trashed_at is null for update;
  if v_version is null then raise exception 'canonical object % not found',v_id; end if;
  if p_expected_math_version is not null and v_math_version<>p_expected_math_version then
    raise exception 'canonical object % changed: expected math_version %, current %',
      v_id,p_expected_math_version,v_math_version;
  end if;
  v_result:=control_center.update_object(
    p_worker_id,v_id,v_version,coalesce(p_patch,'{}'::jsonb),p_substantive);
  return v_result||jsonb_build_object(
    'requested_id',p_id,'canonical_id',v_id,
    'resolved_replacement',v_id is distinct from p_id);
end
$function$

```

## rpc_list() -> text[]

```sql
CREATE OR REPLACE FUNCTION control_center.rpc_list()
 RETURNS text[]
 LANGUAGE sql
 STABLE SECURITY DEFINER
 SET search_path TO 'pg_catalog', 'control_center'
AS $function$
  select coalesce(array_agg(distinct rpc_name order by rpc_name),'{}'::text[])
  from control_center.public_rpc_contract
$function$

```

## rpc_signatures(p_name text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.rpc_signatures(p_name text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$begin
  PERFORM control_center.active_project();
  
  RETURN (

  select jsonb_build_object(
    'functions',coalesce(jsonb_agg(jsonb_build_object(
      'name',p.proname,
      'arguments',pg_get_function_identity_arguments(p.oid),
      'result',pg_get_function_result(p.oid)
    ) order by p.proname,pg_get_function_identity_arguments(p.oid)),'[]'::jsonb),
    'discovery_mode',case when p_name is null then 'canonical' else 'exact_name' end,
    'note',case when p_name is null
      then 'Default discovery hides deprecated compatibility wrappers and internal implementation functions. Supply an exact name only for debugging/compatibility inspection.'
      else null end
  )
  from pg_proc p
  join pg_namespace n on n.oid=p.pronamespace
  where n.nspname=control_center.active_project()
    and p.proname like '%'
    and (p_name is not null or p.proname not in (
      'append_stage',
      'begin_proof_activity',
      'bind_composition',
      'certify_object',
      'certify_object_ex_base_v4',
      'commit_stage_base',
      'commit_stage_locked_base',
      'continue_base',
      'mark_proof_node',
      'open_read_ex_base',
      'read_page_base',
      'replace_stage',
      'stage_batch_base',
      'watch_stage_reads',
      'record_acceptance'
    ))
    and (p_name is null or p.proname=p_name)

  );
end$function$

```

## search(p_query text, p_limit integer DEFAULT 20, p_attention text DEFAULT NULL::text, p_statement_only boolean DEFAULT false) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.search(p_query text, p_limit integer DEFAULT 20, p_attention text DEFAULT NULL::text, p_statement_only boolean DEFAULT false)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare
  v_result jsonb;
  v_items jsonb;
begin
  perform control_center.active_project();

  v_result:=control_center.search_ex_v2(
    p_query,p_limit,p_attention,null,null,null,null,null,false
  );

  if not coalesce(p_statement_only,false) then
    return v_result;
  end if;

  -- search_ex_v2 already produces one candidate row per object. Group again by
  -- object id here as a defensive guarantee that repeated query occurrences in
  -- a body can never duplicate the returned title/statement pair.
  with hit_ids as (
    select
      h.item->>'id' as id,
      min(h.ord) as ord
    from jsonb_array_elements(coalesce(v_result->'items','[]'::jsonb))
         with ordinality as h(item,ord)
    group by h.item->>'id'
  )
  select coalesce(
    jsonb_agg(
      jsonb_build_object(
        'title',o.title,
        'statement',o.statement
      )
      order by h.ord
    ),
    '[]'::jsonb
  )
  into v_items
  from hit_ids h
  join objects o on o.id=h.id and o.trashed_at is null;

  return (v_result - 'items')
    || jsonb_build_object(
      'items',v_items,
      'statement_only',true,
      'retrieval',
        coalesce(v_result->>'retrieval','')
        || '; body remains searchable for matching/ranking, but output is one title/statement pair per matched object'
    );
end
$function$

```

## search_compact(p_query text, p_limit integer DEFAULT 20, p_under_id text DEFAULT NULL::text, p_include_superseded boolean DEFAULT false) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.search_compact(p_query text, p_limit integer DEFAULT 20, p_under_id text DEFAULT NULL::text, p_include_superseded boolean DEFAULT false)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare
  v_under_path text;
  v_limit integer:=greatest(1,least(control_center.config_int('api.max_result_limit'),p_limit));
  v_total integer;
  v_items jsonb;
  v_q tsquery:=loose_tsquery(p_query);
begin
  perform control_center.active_project();

  if p_under_id is not null then
    select tree_path into v_under_path
    from objects where id=p_under_id and trashed_at is null;
    if v_under_path is null then raise exception 'under_id % not found',p_under_id; end if;
  end if;

  with candidates as (
    select o.*,
      case when coalesce(btrim(p_query),'')='' then 0
           when lower(o.title) like '%'||lower(btrim(p_query))||'%' then 4 else 0 end
      + case when coalesce(btrim(p_query),'')='' then 0
             else 2*extensions.similarity(
               lower(coalesce(o.title,'')||' '||coalesce(o.statement,'')),lower(p_query)) end
      + case when v_q is null then 0
             else ts_rank_cd(
               search_vector(o.title,o.statement,o.research_interface,''),v_q,32) end as score
    from objects o
    where o.trashed_at is null
      and not exists (
        select 1 from objects ar
        where ar.id='archive01' and ar.trashed_at is null
          and o.tree_path like ar.tree_path||'%')
      and (p_include_superseded or cardinality(control_center.superseded_by(o.id))=0)
      and (v_under_path is null or o.tree_path like v_under_path||'%')
      and (
        coalesce(btrim(p_query),'')=''
        or (v_q is not null
            and search_vector(o.title,o.statement,o.research_interface,'') @@ v_q)
        or extensions.similarity(
             lower(coalesce(o.title,'')||' '||coalesce(o.statement,'')),lower(p_query))>0.12)
  )
  select count(*) into v_total from candidates;

  with candidates as (
    select o.*,
      case when coalesce(btrim(p_query),'')='' then 0
           when lower(o.title) like '%'||lower(btrim(p_query))||'%' then 4 else 0 end
      + case when coalesce(btrim(p_query),'')='' then 0
             else 2*extensions.similarity(
               lower(coalesce(o.title,'')||' '||coalesce(o.statement,'')),lower(p_query)) end
      + case when v_q is null then 0
             else ts_rank_cd(
               search_vector(o.title,o.statement,o.research_interface,''),v_q,32) end as score
    from objects o
    where o.trashed_at is null
      and not exists (
        select 1 from objects ar
        where ar.id='archive01' and ar.trashed_at is null
          and o.tree_path like ar.tree_path||'%')
      and (p_include_superseded or cardinality(control_center.superseded_by(o.id))=0)
      and (v_under_path is null or o.tree_path like v_under_path||'%')
      and (
        coalesce(btrim(p_query),'')=''
        or (v_q is not null
            and search_vector(o.title,o.statement,o.research_interface,'') @@ v_q)
        or extensions.similarity(
             lower(coalesce(o.title,'')||' '||coalesce(o.statement,'')),lower(p_query))>0.12)
    order by score desc,
      case o.attention when 'focus' then 0 when 'available' then 1 else 2 end,
      o.updated_at desc
    limit v_limit
  )
  select coalesce(jsonb_agg(jsonb_strip_nulls(jsonb_build_object(
    'id',id,
    'title',title,
    'statement',case when statement is null then null
                     else left(regexp_replace(statement,E'\\s+',' ','g'),control_center.config_int('search.compact_title_chars')) end,
    'status',jsonb_build_object(
      'mathematical',mathematical_status,
      'audit',audit_status,
      'support',support_status,
      'lifecycle',lifecycle_status,
      'math_version',math_version),
    'interface',preview_value(research_interface,control_center.config_int('search.compact_interface_chars')),
    'score',round(score::numeric,4)
  )) order by score desc),'[]'::jsonb)
  into v_items
  from candidates;

  return jsonb_build_object(
    'items',v_items,'returned_count',jsonb_array_length(v_items),
    'total_count',v_total,'truncated',v_total>jsonb_array_length(v_items),
    'retrieval','compact title/statement/interface search; body excluded; Archive excluded',
    'include_superseded',p_include_superseded,
    'repository_revision',(select revision from state where singleton));
end
$function$

```

## search_ex(p_query text, p_limit integer DEFAULT 20, p_attention text DEFAULT NULL::text, p_under_id text DEFAULT NULL::text, p_research_level text DEFAULT NULL::text, p_mathematical_status text DEFAULT NULL::text, p_audit_status text DEFAULT NULL::text, p_object_type text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.search_ex(p_query text, p_limit integer DEFAULT 20, p_attention text DEFAULT NULL::text, p_under_id text DEFAULT NULL::text, p_research_level text DEFAULT NULL::text, p_mathematical_status text DEFAULT NULL::text, p_audit_status text DEFAULT NULL::text, p_object_type text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$begin
  PERFORM control_center.active_project();
  
  RETURN (

  select control_center.search_ex_v2(
    p_query,p_limit,p_attention,p_under_id,p_research_level,
    p_mathematical_status,p_audit_status,p_object_type,false
  )

  );
end$function$

```

## search_ex_v2(p_query text, p_limit integer DEFAULT 20, p_attention text DEFAULT NULL::text, p_under_id text DEFAULT NULL::text, p_research_level text DEFAULT NULL::text, p_mathematical_status text DEFAULT NULL::text, p_audit_status text DEFAULT NULL::text, p_object_type text DEFAULT NULL::text, p_include_superseded boolean DEFAULT false) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.search_ex_v2(p_query text, p_limit integer DEFAULT 20, p_attention text DEFAULT NULL::text, p_under_id text DEFAULT NULL::text, p_research_level text DEFAULT NULL::text, p_mathematical_status text DEFAULT NULL::text, p_audit_status text DEFAULT NULL::text, p_object_type text DEFAULT NULL::text, p_include_superseded boolean DEFAULT false)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare
  v_under_path text;
  v_limit integer:=greatest(1,least(control_center.config_int('api.max_result_limit'),p_limit));
  v_total integer;
  v_items jsonb;
  v_q tsquery:=loose_tsquery(p_query);
begin
  perform control_center.active_project();

  if p_under_id is not null then
    select tree_path into v_under_path from objects
    where id=p_under_id and trashed_at is null;
    if v_under_path is null then raise exception 'under_id % not found',p_under_id; end if;
  end if;

  with candidates as (
    select o.*,
      search_vector(o.title,o.statement,o.research_interface,o.body) sv,
      case when coalesce(btrim(p_query),'')='' then 0
           when lower(o.title) like '%'||lower(btrim(p_query))||'%' then 4
           else 0 end
      + case when coalesce(btrim(p_query),'')='' then 0
             else 2*extensions.similarity(lower(coalesce(o.title,'')||' '||coalesce(o.statement,'')),
                               lower(p_query)) end
      + case when v_q is null then 0
             else ts_rank_cd(
               search_vector(o.title,o.statement,o.research_interface,o.body),
               v_q,32
             ) end as score
    from objects o
    where o.trashed_at is null
      and not exists (
        select 1 from objects ar
        where ar.id='archive01'
          and ar.trashed_at is null
          and o.tree_path like ar.tree_path||'%'
      )
      and (p_include_superseded or cardinality(superseded_by(o.id))=0)
      and (p_attention is null or o.attention=p_attention)
      and (p_research_level is null or o.research_level=p_research_level)
      and (p_mathematical_status is null or o.mathematical_status=p_mathematical_status)
      and (p_audit_status is null or o.audit_status=p_audit_status)
      and (p_object_type is null or o.object_type=p_object_type)
      and (v_under_path is null or o.tree_path like v_under_path||'%')
      and (
        coalesce(btrim(p_query),'')=''
        or (v_q is not null and
            search_vector(o.title,o.statement,o.research_interface,o.body) @@ v_q)
        or extensions.similarity(lower(coalesce(o.title,'')||' '||coalesce(o.statement,'')),
                      lower(p_query))>0.12
      )
  )
  select count(*) into v_total from candidates;

  with candidates as (
    select o.*,
      search_vector(o.title,o.statement,o.research_interface,o.body) sv,
      case when coalesce(btrim(p_query),'')='' then 0
           when lower(o.title) like '%'||lower(btrim(p_query))||'%' then 4
           else 0 end
      + case when coalesce(btrim(p_query),'')='' then 0
             else 2*extensions.similarity(lower(coalesce(o.title,'')||' '||coalesce(o.statement,'')),
                               lower(p_query)) end
      + case when v_q is null then 0
             else ts_rank_cd(
               search_vector(o.title,o.statement,o.research_interface,o.body),
               v_q,32
             ) end as score
    from objects o
    where o.trashed_at is null
      and not exists (
        select 1 from objects ar
        where ar.id='archive01'
          and ar.trashed_at is null
          and o.tree_path like ar.tree_path||'%'
      )
      and (p_include_superseded or cardinality(superseded_by(o.id))=0)
      and (p_attention is null or o.attention=p_attention)
      and (p_research_level is null or o.research_level=p_research_level)
      and (p_mathematical_status is null or o.mathematical_status=p_mathematical_status)
      and (p_audit_status is null or o.audit_status=p_audit_status)
      and (p_object_type is null or o.object_type=p_object_type)
      and (v_under_path is null or o.tree_path like v_under_path||'%')
      and (
        coalesce(btrim(p_query),'')=''
        or (v_q is not null and
            search_vector(o.title,o.statement,o.research_interface,o.body) @@ v_q)
        or extensions.similarity(lower(coalesce(o.title,'')||' '||coalesce(o.statement,'')),
                      lower(p_query))>0.12
      )
    order by score desc,
      case o.attention when 'focus' then 0 when 'available' then 1 else 2 end,
      o.updated_at desc
    limit v_limit
  )
  select coalesce(jsonb_agg(jsonb_strip_nulls(jsonb_build_object(
    'id',id,
    'title',title,
    'statement',preview_value(to_jsonb(statement),control_center.config_int('search.statement_preview_chars')),
    'snippet',case
      when v_q is null then left(coalesce(statement,''),control_center.config_int('search.snippet_statement_chars'))
      else ts_headline(
        'simple',
        coalesce(statement,'')||' '||coalesce(research_interface::text,'')||' '||left(coalesce(body,''),control_center.config_int('search.body_index_chars')),
        v_q,
        'MaxFragments=2,MaxWords=18,MinWords=5,StartSel=«,StopSel=»'
      )
    end,
    'research_interface',preview_value(research_interface,control_center.config_int('search.detailed_interface_chars')),
    'score',round(score::numeric,4),
    'match_reason',case
      when coalesce(btrim(p_query),'')='' then 'filter'
      when lower(title) like '%'||lower(btrim(p_query))||'%' then 'title phrase'
      when extensions.similarity(lower(coalesce(title,'')||' '||coalesce(statement,'')),
                      lower(p_query))>0.30 then 'fuzzy title/statement'
      else 'concept terms'
    end,
    'mathematical_status',mathematical_status,
    'audit_status',audit_status,
    'support_status',support_status,
    'math_version',math_version,
    'read_hint',control_center.active_project()||'.read(ARRAY['''||id||'''], ''summary''|''math'')'
  )) order by score desc),'[]'::jsonb)
  into v_items
  from candidates;

  return jsonb_build_object(
    'items',v_items,
    'returned_count',jsonb_array_length(v_items),
    'total_count',v_total,
    'truncated',v_total>jsonb_array_length(v_items),
    'retrieval','weighted loose-term FTS + trigram fallback; Archive subtree excluded',
    'include_superseded',p_include_superseded,
    'repository_revision',(select revision from state where singleton)
  );
end
$function$

```

## set_guidance(p_worker_id bigint, p_message text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.set_guidance(p_worker_id bigint, p_message text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
DECLARE v_version bigint;
BEGIN
  PERFORM control_center.active_project();
  SELECT version INTO v_version FROM objects WHERE id='scheduler_guidance' AND trashed_at IS NULL;
  IF v_version IS NULL THEN RAISE EXCEPTION 'reserved scheduler_guidance document missing'; END IF;
  RETURN control_center.update_object(
    p_worker_id,'scheduler_guidance',v_version,
    jsonb_build_object('body',coalesce(p_message,'')),false
  );
END
$function$

```

## set_project_state(p_worker_id bigint, p_patch jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.set_project_state(p_worker_id bigint, p_patch jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_old record;
  v_new record;
  v_grand text;
  v_rev bigint;
  v_extra jsonb;
begin
  perform control_center.active_project();

  if jsonb_typeof(coalesce(p_patch,'null'::jsonb))<>'object' then
    raise exception 'project-state patch must be a JSON object';
  end if;

  v_extra:=p_patch-'phase'-'grand_theorem_id'-'methodology_version';
  if v_extra<>'{}'::jsonb then
    raise exception 'unsupported project-state keys %. Directional strategy/guidance/frontier/bottleneck/focus state is retired; use scheduler_guidance only for temporary guidance.',
      (select array_agg(key order by key) from jsonb_object_keys(v_extra) key);
  end if;

  select * into v_old from state where singleton for update;

  v_grand:=case when p_patch ? 'grand_theorem_id'
    then nullif(p_patch->>'grand_theorem_id','') else v_old.grand_theorem_id end;

  if v_grand is not null and not exists(
    select 1 from objects where id=v_grand and trashed_at is null
  ) then
    raise exception 'grand theorem object % not found',v_grand;
  end if;

  update state
  set phase=case when p_patch ? 'phase' then p_patch->>'phase' else phase end,
      grand_theorem_id=v_grand,
      current_strategy_id=null,
      proof_frontier_id=null,
      current_bottleneck_id=null,
      research_focus_ids='{}'::text[],
      methodology_version=case when p_patch ? 'methodology_version'
        then (p_patch->>'methodology_version')::integer else methodology_version end,
      updated_at=now()
  where singleton
  returning * into v_new;

  v_rev:=record_change(
    'set_project_state',
    case when v_new.grand_theorem_id is null then '{}'::text[] else array[v_new.grand_theorem_id] end,
    p_patch
  );

  return to_jsonb(v_new)||jsonb_build_object('repository_revision',v_rev);
end
$function$

```

## signals(p_status text DEFAULT 'active'::text, p_kind text DEFAULT NULL::text, p_limit integer DEFAULT 64) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.signals(p_status text DEFAULT 'active'::text, p_kind text DEFAULT NULL::text, p_limit integer DEFAULT 64)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$begin
  PERFORM control_center.active_project();
  
  RETURN (

  select jsonb_build_object(
    'items',coalesce(jsonb_agg(to_jsonb(q) order by q.severity desc,q.updated_at desc),'[]'::jsonb)
  )
  from (
    select id,signal_key,kind,status,severity,title,body,evidence,related_object_ids,created_at,updated_at,resolved_at
      from signals
     where (p_status is null or status=p_status)
       and (p_kind is null or kind=p_kind)
     order by severity desc,updated_at desc
     limit greatest(1,least(control_center.config_int('api.default_limit'),p_limit))
  ) q

  );
end$function$

```

## simplified_ancestry(p_object_id text, p_max_depth integer DEFAULT NULL::integer) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.simplified_ancestry(p_object_id text, p_max_depth integer DEFAULT NULL::integer)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE
AS $function$
declare
  v_max_depth integer;
  v_items jsonb;
  v_count integer;
  v_truncated boolean;
begin
  perform control_center.active_project();

  if not exists (
    select 1 from objects
    where id=p_object_id and trashed_at is null
  ) then
    raise exception 'object % not found', p_object_id;
  end if;

  v_max_depth := greatest(
    0,
    least(
      control_center.config_int('subtree.max_depth'),
      coalesce(p_max_depth, control_center.config_int('subtree.simplified_default_depth'))
    )
  );

  with recursive chain as (
    select
      o.id,o.parent_id,o.title,o.simplified_statement,
      o.mathematical_status,o.audit_status,o.support_status,
      0::integer as depth
    from objects o
    where o.id=p_object_id and o.trashed_at is null

    union all

    select
      p.id,p.parent_id,p.title,p.simplified_statement,
      p.mathematical_status,p.audit_status,p.support_status,
      c.depth+1
    from chain c
    join objects p on p.id=c.parent_id and p.trashed_at is null
    where c.depth < v_max_depth
  )
  select
    coalesce(
      jsonb_agg(
        jsonb_strip_nulls(jsonb_build_object(
          'depth',depth,
          'id',id,
          'parent_id',parent_id,
          'title',title,
          'simplified_statement',coalesce(nullif(btrim(simplified_statement),''),'‹'||title||'›'),
          'mathematical_status',mathematical_status,
          'audit_status',audit_status,
          'support_status',support_status
        ))
        order by depth
      ),
      '[]'::jsonb
    ),
    count(*),
    coalesce(bool_or(
      depth=v_max_depth
      and parent_id is not null
      and exists (
        select 1 from objects p2
        where p2.id=chain.parent_id and p2.trashed_at is null
      )
    ),false)
  into v_items,v_count,v_truncated
  from chain;

  return jsonb_build_object(
    'object_id',p_object_id,
    'direction','target_to_root',
    'max_depth',v_max_depth,
    'items',v_items,
    'node_count',v_count,
    'truncated',v_truncated,
    'repository_revision',(select revision from state where singleton)
  );
end
$function$

```

## simplified_subtree(p_root_id text, p_max_depth integer DEFAULT NULL::integer) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.simplified_subtree(p_root_id text, p_max_depth integer DEFAULT NULL::integer)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare
  v_path text;
  v_root_depth integer;
  v_max_depth integer;
  v_tree text;
  v_count integer;
  v_cut_count integer;
begin
  perform control_center.active_project();

  select tree_path,
         array_length(string_to_array(trim(both '/' from tree_path),'/'),1)
    into v_path,v_root_depth
  from objects
  where id=p_root_id
    and trashed_at is null;

  if v_path is null then
    raise exception 'root object % not found',p_root_id;
  end if;

  v_max_depth := greatest(
    0,
    least(
      control_center.config_int('subtree.max_depth'),
      coalesce(p_max_depth,control_center.config_int('subtree.simplified_default_depth'))
    )
  );

  with visible as materialized (
    select
      o.id,
      o.title,
      o.simplified_statement,
      o.tree_path,
      array_length(string_to_array(trim(both '/' from o.tree_path),'/'),1)-v_root_depth as depth
    from objects o
    where o.trashed_at is null
      and o.tree_path like v_path||'%'
      and array_length(string_to_array(trim(both '/' from o.tree_path),'/'),1)-v_root_depth <= v_max_depth
  ),
  rendered as (
    select
      v.tree_path as sort_key,
      repeat('  ',v.depth) || '• [' || v.id || '] ' ||
      coalesce(nullif(btrim(v.simplified_statement),''),
               '‹' || v.title || '›') as line
    from visible v

    union all

    select
      v.tree_path || '/~' as sort_key,
      repeat('  ',v.depth+1) || '…' as line
    from visible v
    where v.depth=v_max_depth
      and exists (
        select 1
        from objects child
        where child.trashed_at is null
          and child.parent_id=v.id
      )
  )
  select string_agg(line,E'\n' order by sort_key),
         (select count(*) from visible),
         (
           select count(*)
           from visible v
           where v.depth=v_max_depth
             and exists (
               select 1
               from objects child
               where child.trashed_at is null
                 and child.parent_id=v.id
             )
         )
    into v_tree,v_count,v_cut_count
  from rendered;

  return jsonb_strip_nulls(jsonb_build_object(
    'root_id',p_root_id,
    'max_depth',v_max_depth,
    'tree',coalesce(v_tree,''),
    'node_count',coalesce(v_count,0),
    'truncated',coalesce(v_cut_count,0)>0,
    'marker',case
      when coalesce(v_cut_count,0)>0 then '… = deeper descendants omitted'
      else null
    end,
    'repository_revision',(select revision from state where singleton)
  ));
end
$function$

```

## stage_audit_batch(p_worker_id bigint, p_label text, p_operations jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.stage_audit_batch(p_worker_id bigint, p_label text, p_operations jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_claim record;
  v_stage jsonb;
  v_stage_id bigint;
  v_union jsonb:='{}'::jsonb;
  v_snap record;
begin
  PERFORM control_center.active_project();
  
  select * into v_claim from claims
   where worker_id=p_worker_id  and expires_at>now()
   order by created_at desc limit 1;
  if v_claim.claim_id is null then raise exception 'active worker claim required'; end if;

  if not coalesce((audit_snapshot_state(v_claim.claim_id)->>'current')::boolean,false)
     or not coalesce((audit_snapshot_state(v_claim.claim_id)->>'complete')::boolean,false) then
    raise exception 'shared audit batch snapshot is missing, incomplete, or stale; reopen/finish open_audit_batch first';
  end if;

  for v_snap in
    select watched_math_versions
    from audit_snapshots
    where claim_id=v_claim.claim_id and expires_at>now()
  loop
    v_union:=v_union||v_snap.watched_math_versions;
  end loop;

  v_stage:=control_center.stage_batch(p_worker_id,p_label,p_operations);
  v_stage_id:=(v_stage->>'stage_id')::bigint;

  update stages
     set read_math_baselines=read_math_baselines||v_union,
         payload=payload||jsonb_build_object(
           'audit_claim_id',v_claim.claim_id,
           'audit_batch_target_ids',to_jsonb(v_claim.target_ids),
           'shared_audit_basis',true
         ),
         stage_revision=stage_revision+1,
         verified_stage_revision=null,verified_digest=null
   where stage_id=v_stage_id;

  return to_jsonb((select s from stages s where s.stage_id=v_stage_id))
    ||jsonb_build_object(
      'audit_claim_id',v_claim.claim_id,
      'shared_audit_basis',true
    );
end
$function$

```

## stage_batch(p_worker_id bigint, p_label text, p_operations jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.stage_batch(p_worker_id bigint, p_label text, p_operations jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
begin
  PERFORM control_center.active_project();
  
  PERFORM require_math_principal(p_worker_id);
  PERFORM pg_advisory_xact_lock(hashtext((control_center.active_project()||'_stage_pool')));
  RETURN control_center.stage_batch_base(p_worker_id,p_label,p_operations);
END
$function$

```

## stage_batch_base(p_worker_id bigint, p_label text, p_operations jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.stage_batch_base(p_worker_id bigint, p_label text, p_operations jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
DECLARE
  v_ops jsonb; v_base jsonb; v_read jsonb;
  v_ttl integer; v_cap integer; v_count integer;
  v_stage record; v_mode text; v_focus text; v_principal jsonb;
BEGIN
  PERFORM control_center.active_project();
  PERFORM purge_ephemeral();

  SELECT max_stages,stage_ttl_minutes INTO v_cap,v_ttl FROM settings WHERE singleton;
  SELECT count(*) INTO v_count FROM stages WHERE expires_at>now();
  IF v_count>=v_cap THEN RAISE EXCEPTION 'PROJECT stage cap % reached',v_cap; END IF;

  v_principal:=require_math_principal(p_worker_id);
  v_mode:=v_principal->>'mode';
  v_focus:=nullif(v_principal->>'focus_id','');

  v_ops:=normalize_stage_operations(p_operations);
  v_base:=stage_baselines(v_ops);
  v_read:=stage_math_read_baselines(v_ops);

  INSERT INTO stages(
    owner_worker_id,kind,label,mode,focus_id,claimable,
    operations,baselines,read_math_baselines,payload,
    stage_revision,verified_stage_revision,verified_digest,expires_at
  ) VALUES (
    p_worker_id,'batch',p_label,v_mode,v_focus,false,
    v_ops,v_base,v_read,
    jsonb_build_object(
      'explicit_watch_ids','[]'::jsonb,
      'principal_kind',v_principal->>'principal_kind'
    ),
    1,null,null,now()+make_interval(mins=>v_ttl)
  ) RETURNING * INTO v_stage;

  RETURN to_jsonb(v_stage);
END
$function$

```

## stage_reasoning_bundle(p_worker_id bigint, p_label text, p_nodes jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.stage_reasoning_bundle(p_worker_id bigint, p_label text, p_nodes jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
DECLARE
  v_count integer;
  v_bad integer;
  v_link_count integer;
  v_audit_count integer;
  v_map jsonb;
  v_ops jsonb;
  v_result jsonb;
BEGIN
  PERFORM control_center.active_project();

  IF jsonb_typeof(coalesce(p_nodes,'null'::jsonb))<>'array' THEN
    RAISE EXCEPTION 'nodes must be a JSON array';
  END IF;

  v_count:=jsonb_array_length(p_nodes);
  IF v_count<1 OR v_count>control_center.config_int('reasoning.max_bundle_nodes') THEN
    RAISE EXCEPTION 'reasoning bundle exceeds configured node limit %',
      control_center.config_int('reasoning.max_bundle_nodes');
  END IF;

  SELECT count(*) INTO v_bad
  FROM jsonb_array_elements(p_nodes) n
  WHERE jsonb_typeof(n)<>'object'
     OR coalesce(n->>'key','')=''
     OR coalesce(n->>'title','')=''
     OR coalesce(n->>'node_kind','step') NOT IN ('root','step','branch')
     OR (n ? 'links' AND jsonb_typeof(n->'links')<>'array');

  IF v_bad>0 THEN
    RAISE EXCEPTION
      'every reasoning node requires key/title, valid node_kind, and array-valued links when present';
  END IF;

  SELECT count(*)-count(distinct n->>'key')
    INTO v_bad
  FROM jsonb_array_elements(p_nodes) n;

  IF v_bad<>0 THEN
    RAISE EXCEPTION 'reasoning bundle local keys must be unique';
  END IF;

  IF EXISTS(
    SELECT 1 FROM jsonb_array_elements(p_nodes) n
    WHERE n ? 'parent_id' AND n ? 'parent_key'
  ) THEN
    RAISE EXCEPTION 'a reasoning node may use parent_id or parent_key, not both';
  END IF;

  IF EXISTS(
    SELECT 1
    FROM jsonb_array_elements(p_nodes) WITH ORDINALITY n(node,ord)
    WHERE n.node ? 'parent_key'
      AND NOT EXISTS(
        SELECT 1
        FROM jsonb_array_elements(p_nodes) WITH ORDINALITY p(node,ord)
        WHERE p.node->>'key'=n.node->>'parent_key' AND p.ord<n.ord
      )
  ) THEN
    RAISE EXCEPTION 'parent_key must reference an earlier node in the same bundle';
  END IF;

  IF EXISTS(
    SELECT 1 FROM jsonb_array_elements(p_nodes) n
    WHERE n ? 'parent_id'
      AND NOT EXISTS(
        SELECT 1 FROM objects o
        WHERE o.id=n->>'parent_id' AND o.trashed_at IS NULL
      )
  ) THEN
    RAISE EXCEPTION 'one or more parent_id values do not name live objects';
  END IF;

  SELECT count(*) INTO v_link_count
  FROM jsonb_array_elements(p_nodes) n
  CROSS JOIN LATERAL jsonb_array_elements(coalesce(n->'links','[]'::jsonb)) l;

  SELECT count(*) INTO v_audit_count
  FROM jsonb_array_elements(p_nodes) n
  WHERE coalesce((n->>'audit_requested')::boolean,false);

  IF 2*v_count+v_link_count+v_audit_count>
       control_center.config_int('stage.max_primitive_operations') THEN
    RAISE EXCEPTION 'reasoning bundle exceeds configured primitive-operation maximum (% operations requested)',
      2*v_count+v_link_count+v_audit_count;
  END IF;

  IF EXISTS(
    SELECT 1
    FROM jsonb_array_elements(p_nodes) n
    CROSS JOIN LATERAL jsonb_array_elements(coalesce(n->'links','[]'::jsonb)) l
    WHERE jsonb_typeof(l)<>'object'
       OR coalesce(l->>'kind','') NOT IN (
         'proof','depends_on','references','consumes','informs',
         'strengthens','supersedes','fence','interface','contradicts'
       )
       OR ((l ? 'to_key') = (l ? 'to_id'))
  ) THEN
    RAISE EXCEPTION 'each link requires one valid kind and exactly one of to_key/to_id';
  END IF;

  IF EXISTS(
    SELECT 1
    FROM jsonb_array_elements(p_nodes) n
    CROSS JOIN LATERAL jsonb_array_elements(coalesce(n->'links','[]'::jsonb)) l
    WHERE l ? 'to_key'
      AND NOT EXISTS(
        SELECT 1 FROM jsonb_array_elements(p_nodes) t
        WHERE t->>'key'=l->>'to_key'
      )
  ) THEN
    RAISE EXCEPTION 'one or more link to_key values do not exist in this bundle';
  END IF;

  IF EXISTS(
    SELECT 1
    FROM jsonb_array_elements(p_nodes) n
    CROSS JOIN LATERAL jsonb_array_elements(coalesce(n->'links','[]'::jsonb)) l
    WHERE l ? 'to_id'
      AND NOT EXISTS(
        SELECT 1 FROM objects o
        WHERE o.id=l->>'to_id' AND o.trashed_at IS NULL
      )
  ) THEN
    RAISE EXCEPTION 'one or more link to_id values do not name live objects';
  END IF;

  v_map:=control_center.allocate_reasoning_bundle_names(p_nodes);

  WITH nodes AS (
    SELECT
      n.node,n.ord,n.node->>'key' AS key,
      v_map->>(n.node->>'key') AS id,
      CASE
        WHEN n.node ? 'parent_key' THEN v_map->>(n.node->>'parent_key')
        ELSE nullif(n.node->>'parent_id','')
      END AS parent_id
    FROM jsonb_array_elements(p_nodes) WITH ORDINALITY n(node,ord)
  ),
  object_ops AS (
    SELECT ord*2-1 AS seq,
      jsonb_build_object(
        'op','create_object',
        'id',id,
        '_auto_id',true,
        'object_type',coalesce(node->>'object_type','research'),
        'title',node->>'title',
        'statement',coalesce(node->>'statement',''),
        'body',coalesce(node->>'body',''),
        'parent_id',coalesce(parent_id,''),
        'position',coalesce((node->>'position')::bigint,ord),
        'metadata',coalesce(node->'metadata','{}'::jsonb),
        'research_interface',coalesce(node->'research_interface','{}'::jsonb),
        'mathematical_status',coalesce(node->>'mathematical_status',''),
        'research_level',coalesce(node->>'research_level','working_unit'),
        'lifecycle_status',coalesce(node->>'lifecycle_status','active'),
        'attention',coalesce(node->>'attention','available'),
        'simplified_statement',coalesce(node->>'simplified_statement',''),
        'atlas_height',coalesce(node->>'atlas_height',''),
        'atlas_hidden',coalesce((node->>'atlas_hidden')::boolean,false)
      ) AS op
    FROM nodes

    UNION ALL

    SELECT ord*2 AS seq,
      jsonb_build_object(
        'op','mark_reasoning_node',
        'object_id',id,
        'node_kind',coalesce(node->>'node_kind','step'),
        'route_key',coalesce(node->>'route_key',''),
        'note',coalesce(node->>'note','')
      ) AS op
    FROM nodes
  ),
  audit_ops AS (
    SELECT 50000+ord AS seq,
      jsonb_strip_nulls(jsonb_build_object(
        'op','request_audit',
        'id',id,
        'priority',CASE
          WHEN nullif(node->>'audit_priority','') IS NULL THEN NULL
          ELSE (node->>'audit_priority')::integer
        END,
        'reason',nullif(node->>'audit_reason','')
      )) AS op
    FROM nodes
    WHERE coalesce((node->>'audit_requested')::boolean,false)
  ),
  link_ops AS (
    SELECT
      100000+row_number() over (order by n.ord,l.link_ord) AS seq,
      jsonb_build_object(
        'op','add_edge',
        'from_id',n.id,
        'to_id',CASE
          WHEN l.link ? 'to_key' THEN v_map->>(l.link->>'to_key')
          ELSE l.link->>'to_id'
        END,
        'kind',l.link->>'kind',
        'metadata',coalesce(l.link->'metadata','{}'::jsonb)
      ) AS op
    FROM nodes n
    CROSS JOIN LATERAL jsonb_array_elements(coalesce(n.node->'links','[]'::jsonb))
      WITH ORDINALITY l(link,link_ord)
  ),
  primitive AS (
    SELECT * FROM object_ops
    UNION ALL
    SELECT * FROM audit_ops
    UNION ALL
    SELECT * FROM link_ops
  )
  SELECT jsonb_agg(op ORDER BY seq) INTO v_ops FROM primitive;

  v_result:=control_center.stage_batch(p_worker_id,p_label,v_ops);

  RETURN v_result||jsonb_build_object(
    'local_key_to_id',v_map,
    'reasoning_nodes',v_count,
    'links',v_link_count,
    'audit_requests',v_audit_count,
    'primitive_operations',2*v_count+v_link_count+v_audit_count,
    'format_note',
      'parent_key references an earlier local key; parent_id references an existing object. links may target any local to_key or existing to_id. audit_requested=true stages a separate request_audit operation. The entire bundle is one mutable staged batch and commits atomically.'
  );
END
$function$

```

## standardization_dictionary() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.standardization_dictionary()
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$begin
  PERFORM control_center.active_project();
  
  RETURN (

  SELECT standardization_dictionary_snapshot()

  );
end$function$

```

## startup(p_worker_id bigint DEFAULT NULL::bigint) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.startup(p_worker_id bigint DEFAULT NULL::bigint)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_packet jsonb;
  v_revision bigint;
  v_broadcasts jsonb;
  v_dictionary jsonb;
begin
  perform control_center.active_project();
  v_packet := control_center.startup_pre_broadcast_v2(p_worker_id);
  if coalesce((v_packet->>'halt')::boolean,false) then
    return v_packet;
  end if;

  v_revision := (v_packet->>'repository_revision')::bigint;

  -- No scheduler mode exists before the first continue(), so startup may
  -- safely deliver only global broadcasts. Mode-filtered broadcasts are
  -- delivered once continue() chooses the assignment mode.
  select coalesce(jsonb_agg(jsonb_build_object(
    'id',b.id,
    'message',b.message,
    'creation_time',b.creation_time,
    'end_time',b.end_time,
    'ttl',b.ttl
  ) order by b.creation_time,b.id),'[]'::jsonb)
  into v_broadcasts
  from broadcasts b
  where b.creation_time <= v_revision
    and v_revision <= b.end_time
    and b.mode_filter is null;

  v_dictionary := control_center.standardization_dictionary();

  return v_packet || jsonb_build_object(
    'broadcasts', v_broadcasts,
    'standardization_dictionary', v_dictionary
  );
end
$function$

```

## storage_report() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.storage_report()
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare
  v_atlas integer;
begin
  perform control_center.active_project();
  v_atlas := control_center.atlas_conceptual_count();

  return (
    select jsonb_build_object(
      'total_bytes',(
        select coalesce(sum(pg_total_relation_size(c.oid)),0)
          from pg_class c
          join pg_namespace n on n.oid=c.relnamespace
         where n.nspname=control_center.active_project()
           and c.relkind='r'
      ),
      'tables',(
        select jsonb_object_agg(relname,bytes)
        from (
          select c.relname,pg_total_relation_size(c.oid) as bytes
            from pg_class c
            join pg_namespace n on n.oid=c.relnamespace
           where n.nspname=control_center.active_project()
             and c.relkind='r'
           order by bytes desc
        ) q
      ),
      'objects',(select count(*) from objects),
      'reasoning_nodes',(select count(*) from reasoning_nodes),
      'edges',(select count(*) from edges),
      'journal_rows',(select count(*) from changes),
      'claims',(select count(*) from claims),
      'stages',(select count(*) from stages),
      'read_sessions',(select count(*) from read_sessions),
      'presence',(select count(*) from presence),
      'atlas_entries',v_atlas,
      'atlas_mode','semantic_containers',
      'atlas_materialized',false,
      'signals',(select count(*) from signals)
    )
  );
end
$function$

```

## submit_audit_batch(p_worker_id bigint, p_decisions jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.submit_audit_batch(p_worker_id bigint, p_decisions jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
  declare
    d jsonb; transformed jsonb:='[]'::jsonb; r jsonb; rid text; cur record;
    repair_ids text[]:='{}'::text[];
  begin
    perform control_center.active_project();
    if jsonb_typeof(coalesce(p_decisions,'null'::jsonb))<>'array' then
      raise exception 'decisions must be a JSON array';
    end if;

    for d in select value from jsonb_array_elements(p_decisions) loop
      if lower(coalesce(d->>'outcome',''))='repair' then
        transformed:=transformed||jsonb_build_array(jsonb_set(d,'{outcome}','"defer"'::jsonb,true));
        repair_ids:=repair_ids||(d->>'id');
      elsif lower(coalesce(d->>'outcome',''))='fail' then
        select * into cur from objects where id=d->>'id' and trashed_at is null;
        if coalesce(cur.metadata->>'audit_work_kind','')<>'repair' then
          raise exception 'FAIL is terminal and allowed only from REPAIR work after repair has been attempted; use outcome=repair first';
        end if;
        if not coalesce((d->>'repair_attempted')::boolean,false)
           or coalesce(btrim(d->>'irreparable_reason'),'')='' then
          raise exception 'FAIL from REPAIR requires repair_attempted=true and a nonempty irreparable_reason';
        end if;
        transformed:=transformed||jsonb_build_array(
          case when coalesce(btrim(d->>'reason'),'')=''
            then d||jsonb_build_object('reason',d->>'irreparable_reason')
            else d end);
      else
        transformed:=transformed||jsonb_build_array(d);
      end if;
    end loop;

    r:=control_center.submit_audit_batch_pre_repair_lifecycle(p_worker_id,transformed);

    foreach rid in array repair_ids loop
      select * into cur from objects where id=rid and trashed_at is null for update;
      update objects
         set audit_status='pending',audit_requested=true,audited_math_version=null,
             support_status=case when mathematical_status='evidence' then 'evidence' else 'unchecked' end,
             support_reason='repair_requested',
             metadata=(metadata-'audit_resolution')||jsonb_build_object(
               'audit_work_kind','repair',
               'repair_attempt_count',coalesce((metadata->>'repair_attempt_count')::int,0)+1,
               'repair_reason',(
                 select x->>'reason' from jsonb_array_elements(p_decisions) x
                 where x->>'id'=rid limit 1),
               'audit_resolution_before_repair',metadata->'audit_resolution',
               'repair_requested_at',now()
             ),
             version=version+1,updated_at=now()
       where id=rid;
      delete from certificates where object_id=rid;
      update runs
         set payload=jsonb_set(
           coalesce(payload,'{}'::jsonb),'{audit_deferred_ids}',
           to_jsonb(array(
             select x from jsonb_array_elements_text(coalesce(payload->'audit_deferred_ids','[]'::jsonb)) x
             where x<>rid order by x
           )),true),
           updated_at=now()
       where worker_id=p_worker_id;
      perform refresh_dependents(array[rid]);
    end loop;

    return r||jsonb_build_object(
      'repair_ids',to_jsonb(repair_ids),
      'repair_semantics','REPAIR is nonterminal. Finish other batch duties, attempt repair locally first; if no repair is found, leave the object in REPAIR for another independent worker. FAIL is allowed only from REPAIR after an explicit repair attempt and irreparability rationale.'
    );
  end
  $function$

```

## submit_audit_batch_v2(p_worker_id bigint, p_decisions jsonb, p_consumer_impacts jsonb DEFAULT '[]'::jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.submit_audit_batch_v2(p_worker_id bigint, p_decisions jsonb, p_consumer_impacts jsonb DEFAULT '[]'::jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_claim record;
  v_offered text[];
  v_sources text[];
  v_seen text[]:='{}'::text[];
  v_decision jsonb;
  v_id text;
  v_outcome text;
  v_result jsonb;
  v_impact_results jsonb:='[]'::jsonb;
  v_one jsonb;
begin
  PERFORM control_center.active_project();
  
  if jsonb_typeof(coalesce(p_consumer_impacts,'null'::jsonb))<>'array' then
    raise exception 'consumer impacts must be a JSON array';
  end if;

  select * into v_claim
  from claims c
  where c.worker_id=p_worker_id
    
    and c.expires_at>now()
  order by c.created_at desc
  limit 1
  for update;

  if v_claim.claim_id is null then
    raise exception 'active worker claim required';
  end if;

  select coalesce(array_agg(value order by ord),'{}'::text[])
    into v_offered
  from jsonb_array_elements_text(
    coalesce(v_claim.payload->'consumer_impact_ids','[]'::jsonb)
  ) with ordinality q(value,ord);

  if jsonb_array_length(p_consumer_impacts)<>cardinality(v_offered) then
    raise exception 'consumer-impact submission must give exactly one PASS or DEFER for each offered consumer: %',
      v_offered;
  end if;

  for v_decision in select value from jsonb_array_elements(p_consumer_impacts)
  loop
    if jsonb_typeof(v_decision)<>'object' then
      raise exception 'each consumer-impact decision must be an object';
    end if;
    v_id:=nullif(v_decision->>'id','');
    v_outcome:=lower(coalesce(v_decision->>'outcome',''));

    if v_id is null or not (v_id=any(v_offered)) then
      raise exception 'consumer-impact target % was not offered by this exact audit package',v_id;
    end if;
    if v_id=any(v_seen) then
      raise exception 'duplicate consumer-impact decision for %',v_id;
    end if;
    if v_outcome not in ('pass','defer') then
      raise exception 'consumer-impact outcome for % must be pass or defer',v_id;
    end if;
    if v_outcome='pass' and is_substantive_author(v_id,p_worker_id) then
      raise exception 'self-audit barrier for consumer impact %',v_id;
    end if;
    v_seen:=v_seen||v_id;
  end loop;

  if not (v_seen @> v_offered and v_offered @> v_seen)
     or cardinality(v_seen)<>cardinality(v_offered) then
    raise exception 'consumer-impact decisions do not cover exactly the offered set';
  end if;

  -- Ordinary target verdicts and consumer-impact confirmations are one transaction.
  v_result:=control_center.submit_audit_batch(p_worker_id,p_decisions);

  select coalesce(array_agg(value order by ord),'{}'::text[])
    into v_sources
  from jsonb_array_elements_text(
    coalesce(v_claim.payload->'consumer_impact_source_target_ids','[]'::jsonb)
  ) with ordinality q(value,ord);

  for v_decision in select value from jsonb_array_elements(p_consumer_impacts)
  loop
    v_id:=v_decision->>'id';
    v_outcome:=lower(v_decision->>'outcome');

    if v_outcome='defer' then
      -- consumer-impact defer memory
      update runs
         set payload=jsonb_set(
           coalesce(payload,'{}'::jsonb),'{audit_deferred_ids}',
           to_jsonb(array(
             select distinct x from (
               select jsonb_array_elements_text(coalesce(payload->'audit_deferred_ids','[]'::jsonb)) as x
               union all select v_id
             ) q order by x
           )),true
         ), updated_at=now()
       where worker_id=p_worker_id;
      v_impact_results:=v_impact_results||jsonb_build_array(
        jsonb_build_object('id',v_id,'outcome','defer','state_mutation','none')
      );
      continue;
    end if;

    v_one:=confirm_stale_certificate_impact(
      p_worker_id,
      v_id,
      (
        select coalesce(array_agg(e.to_id order by e.to_id),'{}'::text[])
        from edges e
        where e.from_id=v_id
          and e.kind in ('depends_on','proof')
          and e.to_id=any(v_sources)
      ),
      nullif(v_decision->>'note','')
    );

    v_impact_results:=v_impact_results||jsonb_build_array(
      jsonb_build_object('id',v_id,'outcome','pass','result',jsonb_strip_nulls(jsonb_build_object(
        'state_mutation',v_one->>'state_mutation',
        'reason',v_one->>'reason',
        'repository_revision',v_one->'repository_revision',
        'support_status',coalesce(v_one#>>'{support,status}',v_one->>'support_status')
      )))
    );
  end loop;

  return v_result||jsonb_build_object(
    'consumer_impact_results',v_impact_results,
    'consumer_impact_decision_count',jsonb_array_length(p_consumer_impacts)
  );
end
$function$

```

## submit_brainstorm(p_worker_id bigint, p_ideas jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.submit_brainstorm(p_worker_id bigint, p_ideas jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
begin
  perform control_center.active_project();
  return control_center.submit_brainstorm_base(p_worker_id,p_ideas);
end $function$

```

## submit_poll(p_worker_id bigint, p_issue text, p_action text, p_vote_limit integer DEFAULT 3, p_priority integer DEFAULT 80, p_initial_response text DEFAULT 'yes'::text, p_target_ids text[] DEFAULT '{}'::text[]) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.submit_poll(p_worker_id bigint, p_issue text, p_action text, p_vote_limit integer DEFAULT 3, p_priority integer DEFAULT 80, p_initial_response text DEFAULT 'yes'::text, p_target_ids text[] DEFAULT '{}'::text[])
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
DECLARE
  v_poll_id bigint;
  v_initial text:=lower(btrim(coalesce(p_initial_response,'yes')));
  v_rev bigint;
  v_vote_result jsonb;
BEGIN
  PERFORM control_center.active_project();

  IF p_issue IS NULL OR btrim(p_issue)='' THEN
    RAISE EXCEPTION 'poll issue must be nonempty';
  END IF;
  IF p_action IS NULL OR btrim(p_action)='' THEN
    RAISE EXCEPTION 'poll action must be nonempty';
  END IF;
  IF p_vote_limit IS NULL OR p_vote_limit<=0 OR p_vote_limit>control_center.config_int('poll.max_vote_limit') OR mod(p_vote_limit,2)<>1 THEN
    RAISE EXCEPTION 'vote_limit must be a positive odd integer within configured maximum';
  END IF;
  IF p_priority IS NULL OR p_priority<control_center.config_int('priority.min') OR p_priority>control_center.config_int('priority.max') THEN
    RAISE EXCEPTION 'priority is outside configured range';
  END IF;
  IF cardinality(coalesce(p_target_ids,'{}'::text[]))>control_center.config_int('poll.max_target_ids') THEN
    RAISE EXCEPTION 'poll exceeds configured target_id maximum';
  END IF;
  IF v_initial NOT IN ('yes','no','refuse','none') THEN
    RAISE EXCEPTION 'initial_response must be yes, no, refuse, or none';
  END IF;

  INSERT INTO polls(
    issue,action,target_ids,proposer_worker_id,vote_limit,priority
  )
  VALUES(
    left(btrim(p_issue),control_center.config_int('text.max_chars')),
    left(btrim(p_action),control_center.config_int('text.max_chars')),
    coalesce(p_target_ids,'{}'::text[]),
    p_worker_id,p_vote_limit,p_priority
  )
  RETURNING poll_id INTO v_poll_id;

  v_rev:=record_change(
    'private_poll_opened',
    coalesce(p_target_ids,'{}'::text[]),
    jsonb_build_object(
      'poll_id',v_poll_id,
      'issue',left(btrim(p_issue),control_center.config_int('text.max_chars')),
      'action',left(btrim(p_action),control_center.config_int('text.max_chars')),
      'vote_limit',p_vote_limit,
      'priority',p_priority,
      'ballots_private',true
    )
  );

  PERFORM control_center.refresh_vote_need();

  IF v_initial='none' THEN
    RETURN jsonb_build_object(
      'poll_id',v_poll_id,
      'status','open',
      'vote_limit',p_vote_limit,
      'priority',p_priority,
      'initial_response_recorded',false,
      'repository_revision',v_rev,
      'next_action','The poll is open. By default submitters vote yes; this submission explicitly chose no initial response.'
    );
  END IF;

  v_vote_result:=control_center.vote_poll(p_worker_id,v_poll_id,v_initial);

  RETURN jsonb_build_object(
    'poll_id',v_poll_id,
    'default_submission_semantics',
      'submit_poll defaults initial_response to yes, so the proposer supports the suggested action unless explicitly overridden',
    'initial_response_recorded',true
  )||v_vote_result;
END
$function$

```

## subtree(p_root_id text, p_after_path text DEFAULT NULL::text, p_limit integer DEFAULT 100) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.subtree(p_root_id text, p_after_path text DEFAULT NULL::text, p_limit integer DEFAULT 100)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare
  v_path text;
  v_limit integer:=greatest(1,least(control_center.config_int('api.large_limit'),p_limit));
  v_total integer;
  v_items jsonb;
  v_returned integer;
  v_last text;
begin
  PERFORM control_center.active_project();
  
  select tree_path into v_path from objects
   where id=p_root_id and trashed_at is null;
  if v_path is null then raise exception 'root object % not found',p_root_id; end if;

  select count(*) into v_total from objects o
   where o.trashed_at is null
     and o.tree_path like v_path||'%'
     and (p_after_path is null or o.tree_path>p_after_path);

  select coalesce(jsonb_agg(jsonb_build_object(
    'path',q.tree_path,
    'depth',array_length(string_to_array(trim(both '/' from q.tree_path),'/'),1)
      -array_length(string_to_array(trim(both '/' from v_path),'/'),1),
    'object',object_capsule(q.id,control_center.config_int('text.preview_chars'))
  ) order by q.tree_path),'[]'::jsonb),
  count(*),max(q.tree_path)
  into v_items,v_returned,v_last
  from (
    select o.id,o.tree_path
    from objects o
    where o.trashed_at is null
      and o.tree_path like v_path||'%'
      and (p_after_path is null or o.tree_path>p_after_path)
    order by o.tree_path
    limit v_limit
  ) q;

  return jsonb_build_object(
    'root_id',p_root_id,
    'items',v_items,
    'returned_count',coalesce(v_returned,0),
    'remaining_total',v_total,
    'has_more',v_total>coalesce(v_returned,0),
    'next_after_path',case when v_total>coalesce(v_returned,0) then v_last else null end,
    'repository_revision',(select revision from state where singleton)
  );
end
$function$

```

## subtree(p_root_id text, p_max_depth integer, p_limit integer) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.subtree(p_root_id text, p_max_depth integer, p_limit integer)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
DECLARE
  v_path text;
  v_limit integer := greatest(1,least(control_center.config_int('subtree.max_limit'),coalesce(p_limit,control_center.config_int('subtree.default_limit'))));
  v_max_depth integer := greatest(0,least(control_center.config_int('subtree.max_depth'),coalesce(p_max_depth,0)));
  v_root_depth integer;
  v_total integer;
  v_items jsonb;
  v_returned integer;
  v_last text;
BEGIN
  PERFORM control_center.active_project();

  SELECT tree_path,
         array_length(string_to_array(trim(both '/' from tree_path),'/'),1)
  INTO v_path,v_root_depth
  FROM objects
  WHERE id=p_root_id AND trashed_at IS NULL;

  IF v_path IS NULL THEN
    RAISE EXCEPTION 'root object % not found',p_root_id;
  END IF;

  SELECT count(*) INTO v_total
  FROM objects o
  WHERE o.trashed_at IS NULL
    AND o.tree_path LIKE v_path||'%'
    AND (
      array_length(string_to_array(trim(both '/' from o.tree_path),'/'),1)-v_root_depth
    ) <= v_max_depth;

  SELECT coalesce(jsonb_agg(jsonb_build_object(
           'path',q.tree_path,
           'depth',q.depth,
           'object',object_capsule(q.id,control_center.config_int('text.preview_chars'))
         ) ORDER BY q.tree_path),'[]'::jsonb),
         count(*),
         max(q.tree_path)
  INTO v_items,v_returned,v_last
  FROM (
    SELECT o.id,
           o.tree_path,
           array_length(string_to_array(trim(both '/' from o.tree_path),'/'),1)-v_root_depth AS depth
    FROM objects o
    WHERE o.trashed_at IS NULL
      AND o.tree_path LIKE v_path||'%'
      AND (
        array_length(string_to_array(trim(both '/' from o.tree_path),'/'),1)-v_root_depth
      ) <= v_max_depth
    ORDER BY o.tree_path
    LIMIT v_limit
  ) q;

  RETURN jsonb_build_object(
    'root_id',p_root_id,
    'max_depth',v_max_depth,
    'items',v_items,
    'returned_count',coalesce(v_returned,0),
    'remaining_total',v_total,
    'has_more',v_total>coalesce(v_returned,0),
    'next_after_path',case when v_total>coalesce(v_returned,0) then v_last else null end,
    'repository_revision',(select revision from state where singleton)
  );
END
$function$

```

## sync(p_worker_id bigint, p_since_revision bigint DEFAULT NULL::bigint, p_keep_mode boolean DEFAULT false) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.sync(p_worker_id bigint, p_since_revision bigint DEFAULT NULL::bigint, p_keep_mode boolean DEFAULT false)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_current record;
  v_candidate jsonb;
  v_snapshot jsonb;
  v_new_claim bigint;
  v_packet jsonb;
  v_revision bigint;
  v_mode text;
  v_last_sync bigint;
  v_broadcasts jsonb;
begin
  perform control_center.assert_worker_database_access(p_worker_id,'sync');
  perform control_center.active_project();

  select * into v_current
  from claims
  where worker_id=p_worker_id and expires_at>now()
  order by created_at desc
  limit 1;

  if v_current.claim_id is not null
     and v_current.mode in ('research','isolated_research')
     and v_current.purpose='deep_research'
     and not coalesce(p_keep_mode,false)
  then
    v_candidate := control_center.research_mode_interrupt_candidate(p_worker_id);

    if v_candidate is not null then
      v_snapshot := jsonb_build_object(
        'mode',v_current.mode,
        'purpose',v_current.purpose,
        'target_ids',to_jsonb(v_current.target_ids),
        'focus_id',v_current.focus_id,
        'exclusive_key',v_current.exclusive_key,
        'payload',coalesce(v_current.payload,'{}'::jsonb),
        'need_key',v_current.need_key,
        'need_generation',v_current.need_generation
      );

      perform control_center.next_core(
        p_worker_id,
        'deferred',
        jsonb_build_object(
          'scheduler_interrupt',true,
          'interruption_candidate',v_candidate,
          'reason','sync_scheduler_mode_interrupt'
        )
      );

      select claim_id into v_new_claim
      from claims
      where worker_id=p_worker_id and expires_at>now()
      order by created_at desc
      limit 1;

      if v_new_claim is not null then
        update claims
        set payload=coalesce(payload,'{}'::jsonb)
          || jsonb_build_object(
               '_interrupted_research',v_snapshot,
               '_scheduler_interrupt',v_candidate
             )
        where claim_id=v_new_claim;

        perform sync_run_from_claim(p_worker_id,v_new_claim);
      end if;
    end if;
  end if;

  v_packet := control_center.sync_pre_broadcast_v2(p_worker_id,p_since_revision);
  if coalesce((v_packet->>'halt')::boolean,false) then return v_packet; end if;

  v_revision := (v_packet->>'repository_revision')::bigint;
  v_mode := v_packet->'assignment'->>'mode';
  select last_sync_time into v_last_sync from runs where worker_id=p_worker_id;

  select coalesce(jsonb_agg(jsonb_build_object(
    'id',b.id,'message',b.message,'creation_time',b.creation_time,
    'end_time',b.end_time,'ttl',b.ttl
  ) order by b.creation_time,b.id),'[]'::jsonb)
  into v_broadcasts
  from broadcasts b
  where b.creation_time <= v_revision
    and v_revision <= b.end_time
    and coalesce(v_last_sync,v_revision) <= b.end_time
    and (b.mode_filter is null or b.mode_filter=v_mode);

  if jsonb_array_length(v_broadcasts)>0 then
    update runs set last_sync_time=v_revision where worker_id=p_worker_id;
  end if;

  return jsonb_strip_nulls(
    (v_packet - 'broadcasts' - 'continuation_contract')
    || jsonb_build_object(
      'broadcasts',v_broadcasts,
      'keep_mode',coalesce(p_keep_mode,false),
      'scheduler_interrupt',
        case when v_candidate is null then null
             else v_candidate || jsonb_build_object(
               'accepted_automatically',true,
               'reject_rpc',control_center.active_project()
                 ||'.reject_assignment_for_research(worker_id, reason)'
             )
        end,
      'continuation_contract',
        coalesce(v_packet->'continuation_contract','{}'::jsonb)
        || jsonb_build_object(
          'sync','refresh/resume the current assignment; during deep research, keep_mode=false allows a scheduler mode interruption',
          'keep_mode','pass true to preserve the current mode for this sync and skip scheduler mode interruption',
          'broadcasts','read and apply broadcasts returned by sync(); equal-revision sync may harmlessly repeat a broadcast'
        )
    )
  );
end
$function$

```

## sync_all_project_wrappers() -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.sync_all_project_wrappers()
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'pg_catalog', 'control_center'
AS $function$
declare
  s record;
  v_results jsonb:='[]'::jsonb;
  v_count integer:=0;
begin
  for s in
    select n.nspname as schema_name
    from pg_namespace n
    where control_center.is_managed_project_schema(n.nspname)
    order by n.nspname
  loop
    v_results:=v_results||jsonb_build_array(
      control_center.sync_project_wrappers(s.schema_name)
    );
    v_count:=v_count+1;
  end loop;

  return jsonb_build_object(
    'projects_synced',v_count,
    'results',v_results
  );
end
$function$

```

## sync_project_wrappers(p_project_schema text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.sync_project_wrappers(p_project_schema text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'pg_catalog', 'control_center'
AS $function$
declare
  f record;
  x record;
  v_call_args text;
  v_volatility text;
  v_strict text;
  v_parallel text;
  v_sql text;
  v_created integer:=0;
  v_dropped integer:=0;
  v_missing integer:=0;
  v_noncanonical integer:=0;
begin
  if p_project_schema is null
     or (
       p_project_schema<>control_center.config_text('project.seed_schema')
       and (
         p_project_schema !~ '^[a-z][a-z0-9_]*$'
         or length(p_project_schema)>control_center.config_int('project.schema_name_max_chars')
       )
     ) then
    raise exception 'invalid project schema name %',p_project_schema;
  end if;

  if not control_center.is_managed_project_schema(p_project_schema) then
    raise exception 'schema % is not a structurally managed project',p_project_schema;
  end if;

  perform set_config('control_center.allow_project_function_ddl','on',true);

  for x in
    select p.proname,
           pg_get_function_identity_arguments(p.oid) as identity_arguments
    from pg_proc p
    join pg_namespace n on n.oid=p.pronamespace
    where n.nspname=p_project_schema
      and p.prokind='f'
      and not exists (
        select 1
        from control_center.public_rpc_contract c
        where c.rpc_name=p.proname
          and c.identity_arguments=pg_get_function_identity_arguments(p.oid)
          and c.result_type=pg_get_function_result(p.oid)
      )
  loop
    execute format(
      'drop function %I.%I(%s)',
      p_project_schema,x.proname,x.identity_arguments
    );
    v_dropped:=v_dropped+1;
  end loop;

  for f in
    select p.oid,p.proname,
           pg_get_function_arguments(p.oid) as function_arguments,
           pg_get_function_identity_arguments(p.oid) as identity_arguments,
           pg_get_function_result(p.oid) as result_type,
           p.provolatile,p.proisstrict,p.proparallel,p.proargnames,p.pronargs
    from pg_proc p
    join pg_namespace n on n.oid=p.pronamespace
    join control_center.public_rpc_contract c
      on c.rpc_name=p.proname
     and c.identity_arguments=pg_get_function_identity_arguments(p.oid)
     and c.result_type=pg_get_function_result(p.oid)
    where n.nspname='control_center'
      and p.prokind='f'
    order by p.proname,pg_get_function_identity_arguments(p.oid)
  loop
    select string_agg(format('%I',u.name),', ' order by u.ord)
      into v_call_args
    from unnest(coalesce(f.proargnames[1:f.pronargs],'{}'::text[]))
         with ordinality u(name,ord);

    v_volatility:=case f.provolatile
      when 'i' then 'IMMUTABLE'
      when 's' then 'STABLE'
      else 'VOLATILE'
    end;
    v_strict:=case when f.proisstrict then ' STRICT' else '' end;
    v_parallel:=case f.proparallel
      when 's' then ' PARALLEL SAFE'
      when 'r' then ' PARALLEL RESTRICTED'
      else ' PARALLEL UNSAFE'
    end;

    v_sql:=format(
      'create or replace function %I.%I(%s) returns %s language sql %s security definer%s%s set search_path to %L, %L, %L as $f$SELECT control_center.%I(%s)$f$',
      p_project_schema,f.proname,f.function_arguments,f.result_type,
      v_volatility,v_strict,v_parallel,
      p_project_schema,'control_center','pg_catalog',
      f.proname,coalesce(v_call_args,'')
    );
    execute v_sql;

    execute format(
      'alter function %I.%I(%s) owner to postgres',
      p_project_schema,f.proname,f.identity_arguments
    );
    execute format(
      'revoke all on function %I.%I(%s) from public',
      p_project_schema,f.proname,f.identity_arguments
    );
    if exists(select 1 from pg_roles where rolname='anon') then
      execute format(
        'revoke all on function %I.%I(%s) from anon',
        p_project_schema,f.proname,f.identity_arguments
      );
    end if;
    if exists(select 1 from pg_roles where rolname='authenticated') then
      execute format(
        'revoke all on function %I.%I(%s) from authenticated',
        p_project_schema,f.proname,f.identity_arguments
      );
    end if;
    if exists(select 1 from pg_roles where rolname='service_role') then
      execute format(
        'grant execute on function %I.%I(%s) to service_role',
        p_project_schema,f.proname,f.identity_arguments
      );
    end if;

    v_created:=v_created+1;
  end loop;

  select count(*) into v_missing
  from control_center.public_rpc_contract c
  where not exists(
    select 1
    from pg_proc p join pg_namespace n on n.oid=p.pronamespace
    where n.nspname=p_project_schema
      and p.prokind='f'
      and p.proname=c.rpc_name
      and pg_get_function_identity_arguments(p.oid)=c.identity_arguments
      and pg_get_function_result(p.oid)=c.result_type
  );

  select count(*) into v_noncanonical
  from pg_proc p join pg_namespace n on n.oid=p.pronamespace
  where n.nspname=p_project_schema
    and p.prokind='f'
    and not control_center.is_valid_project_wrapper(p.oid,p_project_schema);

  if v_missing<>0 or v_noncanonical<>0 then
    raise exception
      'wrapper sync verification failed for %: missing %, noncanonical %',
      p_project_schema,v_missing,v_noncanonical;
  end if;

  return jsonb_build_object(
    'project_schema',p_project_schema,
    'wrappers_written',v_created,
    'noncontract_functions_dropped',v_dropped,
    'missing_wrappers',v_missing,
    'noncanonical_wrappers',v_noncanonical
  );
end
$function$

```

## trash_subtrees(p_worker_id bigint, p_ids text[]) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.trash_subtrees(p_worker_id bigint, p_ids text[])
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_paths text[] := '{}'::text[];
  v_roots text[] := (coalesce(p_ids,'{}'::text[]))[1:control_center.config_int('tree.max_batch_roots')];
  v_trash_ids text[];
  v_id text;
  v_path text;
  v_count integer;
  v_rev bigint;
begin
  PERFORM control_center.active_project();
  
  perform pg_advisory_xact_lock(hashtext((control_center.active_project()||'_tree')));

  foreach v_id in array coalesce(p_ids,'{}'::text[])
  loop
    select tree_path into v_path
      from objects
     where id=v_id and trashed_at is null;
    if v_path is not null then v_paths:=v_paths||v_path; end if;
  end loop;

  if cardinality(v_paths)=0 then return jsonb_build_object('trashed',0); end if;

  select coalesce(array_agg(o.id),'{}'::text[])
    into v_trash_ids
    from objects o
   where o.trashed_at is null
     and exists(select 1 from unnest(v_paths) p where o.tree_path like p||'%');

  perform assert_no_live_external_consumers(v_trash_ids);

  if exists(
    select 1 from state s
    join objects o on (
      o.id=any(array[
        s.grand_theorem_id,s.current_strategy_id,
        s.proof_frontier_id,s.current_bottleneck_id
      ]::text[])
      or o.id=any(s.research_focus_ids)
    )
    where s.singleton
      and o.id=any(v_trash_ids)
  ) then
    raise exception 'cannot trash a subtree that currently contains project-state or focus objects; coordinate state first';
  end if;

  update objects o
     set trashed_at=now(),attention='hidden',updated_at=now(),version=version+1
   where o.id=any(v_trash_ids);
  get diagnostics v_count=row_count;

  v_rev:=record_change(
    'trash_subtrees',v_roots,
    jsonb_build_object('roots',v_roots,'objects_touched',v_count)
  );

  return jsonb_build_object('trashed',v_count,'repository_revision',v_rev);
end
$function$

```

## trust_report(p_id text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.trust_report(p_id text)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
declare
  v_obj record;
  v_cert jsonb;
  v_current jsonb;
begin
  PERFORM control_center.active_project();
  
  select * into v_obj from objects where id=p_id and trashed_at is null;
  if v_obj.id is null then raise exception 'object % not found',p_id; end if;

  select to_jsonb(c) into v_cert from certificates c where c.object_id=p_id;
  v_current:=compute_support_status(p_id);

  return jsonb_build_object(
    'id',p_id,
    'math_version',v_obj.math_version,
    'mathematical_status',v_obj.mathematical_status,
    'audit_status',v_obj.audit_status,
    'stored_support_status',v_obj.support_status,
    'current_support',v_current,
    'certificate',v_cert,
    'direct_premises',premise_manifest(p_id)
  );
end
$function$

```

## unary_chain_candidates(p_min_length integer DEFAULT 3, p_limit integer DEFAULT 64) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.unary_chain_candidates(p_min_length integer DEFAULT 3, p_limit integer DEFAULT 64)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$begin
  PERFORM control_center.active_project();
  
  RETURN (
 SELECT control_center.unary_cleanup_candidates(p_min_length,p_limit) 
  );
end$function$

```

## unary_cleanup_candidates(p_min_chain_length integer DEFAULT 3, p_limit integer DEFAULT 64) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.unary_cleanup_candidates(p_min_chain_length integer DEFAULT 3, p_limit integer DEFAULT 64)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
begin
  PERFORM control_center.active_project();

  return (
    with toolkit_anchor as (
      select o.tree_path
      from objects o
      where o.id='methods01'
        and o.trashed_at is null
        and o.parent_id is null
        and coalesce((o.metadata->>'toolkit_home')::boolean,false)
      limit 1
    ),
    all_ends as (
      select o.id,o.unary_chain_length
      from objects o
      where o.trashed_at is null
        and o.lifecycle_status='active'
        and o.mathematical_status='proved'
        and o.unary_chain_length >= greatest(2,coalesce(p_min_chain_length,3))
        and not coalesce(o.unary_chain_standalone,false)
        and not exists (
          select 1 from objects c
          where c.parent_id=o.id and c.trashed_at is null
            and c.lifecycle_status='active' and c.mathematical_status='proved'
            and c.unary_chain_length=o.unary_chain_length+1
        )
    ),
    picked as (
      select * from all_ends order by unary_chain_length desc,id
      limit greatest(1,least(coalesce(p_limit,control_center.config_int('unary_cleanup.default_limit')),control_center.config_int('unary_cleanup.max_limit')))
    ),
    misplaced as (
      select o.id,o.title,o.parent_id,o.object_type,o.research_level
      from objects o
      where o.trashed_at is null
        and o.lifecycle_status='active'
        and coalesce(o.unary_chain_standalone,false)
        and not exists (
          select 1 from toolkit_anchor a
          where o.tree_path like a.tree_path||'%'
        )
      order by o.id
      limit greatest(1,least(coalesce(p_limit,control_center.config_int('unary_cleanup.default_limit')),control_center.config_int('unary_cleanup.max_limit')))
    )
    select jsonb_build_object(
      'source','cached_unary_chain_length',
      'canonical_toolkit_root','methods01',
      'min_chain_length',greatest(2,coalesce(p_min_chain_length,3)),
      'default_min_chain_length',3,
      'interpretation','Unary-chain detection is a structural review heuristic, not a flattening mandate. Authentic sequential reasoning must remain nested; siblings mean branches or alternate routes. If a contiguous unary sequence is genuinely over-granular, recompose it into one equivalent-or-stronger replacement via bind_replacement_composition_v2, preserving terminal children and external consumers. If a result is genuinely standalone, rehome the original object/subtree beneath the canonical top-level Toolkit root methods01 and repair old proof-frame references; setting unary_chain_standalone=true without rehoming is incomplete.',
      'standalone_resolution','A standalone result is resolved for hygiene only after it is homed beneath methods01. Topical subtoolkits are children of methods01, not independent toolkit homes. Prefer reference/interface edges from the old route. Use a tiny nonmathematical wrapper only when an edge cannot preserve necessary frame continuity.',
      'chain_length_semantics','0 for non-proved nodes and intentionally standalone proved barriers; ordinary proved nodes start at 1; siblings, a non-proved parent, or a standalone parent reset a proved node to length 1; otherwise length is parent length plus 1',
      'total_count',(select count(*) from all_ends)+(select count(*) from misplaced),
      'unary_chain_count',(select count(*) from all_ends),
      'standalone_outside_toolkit_count',(select count(*) from misplaced),
      'returned_chain_count',(select count(*) from picked),
      'chains',coalesce(
        (select jsonb_agg(cached_unary_chain_ending_at(id) order by unary_chain_length desc,id) from picked),
        '[]'::jsonb
      ),
      'standalone_outside_toolkit',coalesce(
        (select jsonb_agg(
          jsonb_build_object(
            'id',id,'title',title,'parent_id',parent_id,
            'object_type',object_type,'research_level',research_level
          ) order by id
        ) from misplaced),
        '[]'::jsonb
      )
    )
  );
end
$function$

```

## unsupersede(p_worker_id bigint, p_superseder_id text, p_target_id text, p_reason text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.unsupersede(p_worker_id bigint, p_superseder_id text, p_target_id text, p_reason text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_result jsonb;
  v_rev bigint;
begin
  perform control_center.active_project();

  if not exists(
    select 1 from edges
    where from_id=p_superseder_id
      and to_id=p_target_id
      and kind='supersedes'
  ) then
    raise exception 'supersedes edge % -> % not found',p_superseder_id,p_target_id;
  end if;

  v_result:=control_center.remove_edge(
    p_worker_id,p_superseder_id,p_target_id,'supersedes'
  );

  v_rev:=record_change(
    'unsupersede',
    array[p_superseder_id,p_target_id],
    jsonb_strip_nulls(jsonb_build_object(
      'superseder_id',p_superseder_id,
      'target_id',p_target_id,
      'reason',nullif(btrim(coalesce(p_reason,'')),''),
      'lifecycle_reversed',true,
      'remove_edge_result',v_result
    ))
  );

  return v_result||jsonb_build_object(
    'unsuperseded',true,
    'repository_revision',v_rev
  );
end
$function$

```

## update_boot(p_artifact_path text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.update_boot(p_artifact_path text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_project text;
  v_id bigint;
  v_prefix constant text := 'https://api.github.com/repos/SirCaptainCaleb/GN3_RESEARCH/actions/artifacts/';
  v_value jsonb;
begin
  v_project := control_center.active_project();

  if p_artifact_path is null or btrim(p_artifact_path)='' then
    raise exception 'artifact path is required';
  end if;

  if p_artifact_path ~ '^[0-9]+$' then
    v_id := p_artifact_path::bigint;
    p_artifact_path := v_prefix || v_id::text;
  elsif p_artifact_path like v_prefix || '%' then
    begin
      v_id := substring(p_artifact_path from length(v_prefix)+1)::bigint;
    exception when others then
      raise exception 'invalid artifact path %', p_artifact_path;
    end;
  else
    raise exception 'artifact path must be a GitHub Actions artifact API URL or numeric artifact id';
  end if;

  select value into v_value
  from control_center.configuration
  where key='artifact.latest';

  v_value := coalesce(v_value,'{}'::jsonb)
    || jsonb_build_object(
      'actions_artifact_id',v_id,
      'actions_artifact_path',p_artifact_path,
      'actions_artifact_updated_at',now(),
      'actions_artifact_updated_by_project',v_project
    );

  insert into control_center.configuration(key,value,category,description,updated_at)
  values(
    'artifact.latest',
    v_value,
    'artifact',
    'Latest published research-context metadata used by boot().',
    now()
  )
  on conflict(key) do update
  set value=excluded.value,
      category=excluded.category,
      description=excluded.description,
      updated_at=excluded.updated_at;

  return jsonb_build_object(
    'artifact_id',v_id,
    'artifact_path',p_artifact_path,
    'updated',true
  );
end
$function$

```

## update_broadcast(p_worker_id bigint, p_broadcast_id bigint, p_message text DEFAULT NULL::text, p_ttl bigint DEFAULT NULL::bigint) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.update_broadcast(p_worker_id bigint, p_broadcast_id bigint, p_message text DEFAULT NULL::text, p_ttl bigint DEFAULT NULL::bigint)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_row record;
  v_revision bigint;
begin
  perform control_center.active_project();

  if p_worker_id is null or not exists(select 1 from runs where worker_id=p_worker_id) then
    raise exception 'known worker_id is required';
  end if;
  if p_message is not null and length(p_message)=0 then
    raise exception 'broadcast message must be nonempty';
  end if;
  if p_ttl is not null and p_ttl < 0 then
    raise exception 'broadcast TTL must be nonnegative';
  end if;
  if p_message is null and p_ttl is null then
    raise exception 'supply a new message and/or TTL';
  end if;

  update broadcasts
     set message = coalesce(p_message,message),
         ttl = coalesce(p_ttl,ttl),
         end_time = creation_time + coalesce(p_ttl,ttl)
   where id=p_broadcast_id
   returning * into v_row;

  if v_row.id is null then
    raise exception 'broadcast not found';
  end if;

  select revision into v_revision from state where singleton;

  return jsonb_strip_nulls(jsonb_build_object(
    'id',v_row.id,
    'message',v_row.message,
    'mode_filter',v_row.mode_filter,
    'ttl',v_row.ttl,
    'creation_time',v_row.creation_time,
    'end_time',v_row.end_time,
    'currently_deliverable',
      v_revision between v_row.creation_time and v_row.end_time
  ));
end
$function$

```

## update_object(p_worker_id bigint, p_id text, p_expected_version bigint, p_patch jsonb, p_substantive boolean DEFAULT true) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.update_object(p_worker_id bigint, p_id text, p_expected_version bigint, p_patch jsonb, p_substantive boolean DEFAULT true)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_old record;
  v_row record;
  v_rev bigint;
  v_math_changed boolean;
  v_new_status text;
  v_becomes_auditable boolean;
  v_stage_commit boolean:=
    coalesce(current_setting((control_center.active_project()||'.verified_stage_commit'),true),'')='on';
  v_expected_signature jsonb;
  v_current_signature jsonb;
  v_author_worker_id bigint:=effective_substantive_worker(p_worker_id);
  v_open_document boolean:=false;
  v_audit_repair boolean:=false;
  v_repair_reason text;
  v_metadata jsonb;
begin
  PERFORM control_center.active_project();

  if jsonb_typeof(coalesce(p_patch,'{}'::jsonb))<>'object' then
    raise exception 'patch must be a JSON object';
  end if;

  select * into v_old from objects
   where id=p_id and trashed_at is null
   for update;
  if v_old.id is null then raise exception 'object % not found',p_id; end if;
  v_open_document:=v_old.object_type='project_document';

  if v_old.version<>p_expected_version then
    raise exception 'version conflict on %: expected %, current %',
      p_id,p_expected_version,v_old.version;
  end if;

  v_new_status:=case when p_patch ? 'mathematical_status'
    then nullif(p_patch->>'mathematical_status','')
    else v_old.mathematical_status end;

  if v_open_document and p_patch ? 'mathematical_status' then
    raise exception 'project_document objects are non-mathematical; mathematical_status cannot be set';
  end if;

  v_math_changed:=(not v_open_document) and p_substantive and (
    p_patch ? 'statement'
    or p_patch ? 'body'
    or p_patch ? 'mathematical_status'
  );

  if not v_open_document and not p_substantive and (
    p_patch ? 'statement' or p_patch ? 'body' or p_patch ? 'mathematical_status'
  ) then
    raise exception 'statement/body/mathematical_status changes are always substantive';
  end if;

  /*
   * An independent auditor who currently holds this object may repair its
   * mathematics without becoming an ordinary substantive author.  This is
   * the backend implementation of the audit-repair exception.  The policy
   * limits statement changes to small local corrections; that limit is
   * intentionally policy-enforced rather than syntactically guessed here.
   */
  if v_math_changed and not is_substantive_author(p_id,p_worker_id) then
    select exists(
      select 1
      from claims c
      where c.worker_id=p_worker_id
        and p_id=any(c.target_ids)
        and c.expires_at>now()
        and c.purpose='independent_audit_batch'
    ) into v_audit_repair;
  end if;

  if v_math_changed
     and not v_stage_commit
     and not v_audit_repair
     and exists(
       select 1 from edges
        where from_id=p_id and kind='depends_on'
     ) then
    if not (p_patch ? 'premise_signature') then
      raise exception 'direct substantive edit of % requires patch.premise_signature matching the logical premises actually read; use staged publication for a locked read set',p_id;
    end if;

    v_expected_signature:=p_patch->'premise_signature';
    v_current_signature:=premise_signature(p_id);

    if v_expected_signature is distinct from v_current_signature then
      raise exception 'logical premises of % changed since the supplied premise signature',p_id;
    end if;
  end if;

  v_becomes_auditable:=v_new_status in ('proved','evidence')
    and v_old.mathematical_status not in ('proved','evidence');

  v_metadata:=case when p_patch ? 'metadata'
    then coalesce(p_patch->'metadata','{}'::jsonb)
    else coalesce(v_old.metadata,'{}'::jsonb)
  end;

  if v_audit_repair then
    v_repair_reason:=coalesce(
      nullif(p_patch#>>'{metadata,repair_reason}',''),
      nullif(v_old.metadata->>'repair_reason',''),
      'audit-authorized repair'
    );
    v_metadata:=v_metadata||jsonb_build_object(
      'audit_work_kind','repair_validation',
      'last_local_audit_repair',jsonb_build_object(
        'reason',v_repair_reason,
        'worker_id',p_worker_id,
        'recorded_at',now(),
        'audit_repair_authorized',true,
        'body_overhaul_permitted',true,
        'statement_change_policy','small_local_tweak_only_policy_enforced'
      )
    );
  end if;

  update objects
     set semantic_container_text=case when p_patch ? 'semantic_container_text'
           then nullif(btrim(coalesce(p_patch->>'semantic_container_text','')) ,'') else semantic_container_text end,
         simplified_statement=case when p_patch ? 'simplified_statement'
           then nullif(btrim(coalesce(p_patch->>'simplified_statement','')) ,'') else simplified_statement end,
         atlas_height=case when p_patch ? 'atlas_height'
           then nullif(btrim(coalesce(p_patch->>'atlas_height','')) ,'') else atlas_height end,
         atlas_hidden=case when p_patch ? 'atlas_hidden'
           then coalesce((p_patch->>'atlas_hidden')::boolean,false) else atlas_hidden end,
         title=case when p_patch ? 'title' then p_patch->>'title' else title end,
         statement=case when p_patch ? 'statement' then nullif(p_patch->>'statement','') else statement end,
         body=case when p_patch ? 'body' then coalesce(p_patch->>'body','') else body end,
         metadata=v_metadata,
         unary_chain_standalone=case when p_patch ? 'unary_chain_standalone'
           then coalesce((p_patch->>'unary_chain_standalone')::boolean,false)
           else unary_chain_standalone end,
         research_interface=case when p_patch ? 'research_interface'
           then coalesce(p_patch->'research_interface','{}'::jsonb) else research_interface end,
         mathematical_status=case when v_open_document then null else v_new_status end,
         research_level=case when p_patch ? 'research_level'
           then nullif(p_patch->>'research_level','') else research_level end,
         lifecycle_status=case when p_patch ? 'lifecycle_status'
           then p_patch->>'lifecycle_status' else lifecycle_status end,
         attention=case when p_patch ? 'attention' then p_patch->>'attention' else attention end,
         audit_requirement=case when p_patch ? 'audit_requirement'
           then p_patch->>'audit_requirement' else audit_requirement end,
         audit_requested=case
           when v_open_document then false
           when p_patch ? 'audit_requested'
             then coalesce((p_patch->>'audit_requested')::boolean,audit_requested)
           when v_new_status not in ('proved','evidence')
             then false
           else audit_requested
         end,
         audit_priority=case when p_patch ? 'audit_priority'
           then greatest(control_center.config_int('priority.min'),least(control_center.config_int('priority.max'),(p_patch->>'audit_priority')::integer))
           else audit_priority end,
         audit_status=case
           when v_open_document then 'not_required'
           when v_new_status in ('proved','evidence') and (v_math_changed or v_becomes_auditable)
             then 'pending'
           when v_new_status not in ('proved','evidence')
             then 'not_required'
           else audit_status
         end,
         audited_math_version=case
           when v_open_document then null
           when v_math_changed or v_becomes_auditable or v_new_status not in ('proved','evidence')
             then null
           else audited_math_version
         end,
         support_status=case
           when v_open_document then 'unchecked'
           when v_new_status='evidence' then 'evidence'
           when v_new_status='proved' and (v_math_changed or v_becomes_auditable) then 'unchecked'
           when v_new_status not in ('proved','evidence') then 'unchecked'
           else support_status
         end,
         support_reason=case
           when v_open_document then 'non_mathematical_project_document'
           when v_audit_repair then 'audit repair awaiting validation'
           when v_new_status='evidence' then 'finite_or_empirical_evidence'
           when v_new_status='proved' and (v_math_changed or v_becomes_auditable) then
             case when audit_requested then 'audit checkpoint requested' else 'provisional_unaudited' end
           when v_new_status not in ('proved','evidence') then 'not_a_proved_or_evidence_claim'
           else support_reason
         end,
         math_version=math_version+case when v_math_changed then 1 else 0 end,
         substantive_worker_ids=case
           when v_math_changed and not v_audit_repair
             then add_substantive_worker(substantive_worker_ids,v_author_worker_id)
           else substantive_worker_ids end,
         last_substantive_worker_id=case
           when v_math_changed and not v_audit_repair
             then v_author_worker_id
           else last_substantive_worker_id end,
         version=version+1,
         updated_at=now()
   where id=p_id
   returning * into v_row;

  if v_row.audit_requested
     and v_row.mathematical_status='proved'
     and v_row.support_reason='provisional_unaudited' then
    update objects
       set support_reason='audit checkpoint requested',
           metadata=coalesce(metadata,'{}'::jsonb)||jsonb_build_object(
             'audit_trigger_kind',coalesce(metadata->>'audit_trigger_kind','explicit'),
             'audit_request_reason',coalesce(metadata->>'audit_request_reason','explicit audit requested during revision'),
             'audit_request_recorded_at',coalesce((metadata->>'audit_request_recorded_at')::timestamptz,now())
           ),
           updated_at=now()
     where id=p_id
     returning * into v_row;
  end if;

  if v_math_changed or v_becomes_auditable or v_new_status not in ('proved','evidence') then
    delete from certificates where object_id=p_id;
    perform invalidate_dependents(
      array[p_id],'logical premise mathematics/status changed'
    );
  end if;

  v_rev:=record_change(
    case
      when v_open_document then 'update_project_document'
      when v_audit_repair then 'local_audit_repair'
      when v_math_changed then 'update_math'
      else 'update_organization'
    end,
    array[p_id],
    jsonb_build_object(
      'keys',(
        select jsonb_agg(k)
        from jsonb_object_keys(p_patch-'premise_signature') k
      ),
      'math_version',v_row.math_version,
      'audit_status',v_row.audit_status,
      'support_status',v_row.support_status,
      'audit_repair_authorized',v_audit_repair
    )
  );


  return to_jsonb(v_row)||jsonb_build_object(
    'repository_revision',v_rev,
    'audit_repair_authorized',v_audit_repair
  );
end
$function$

```

## update_policy(p_worker_id bigint, p_policy_key text, p_body text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.update_policy(p_worker_id bigint, p_policy_key text, p_body text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_mode text;
  v_row record;
  v_rev bigint;
  v_body text;
  v_schema text;
begin
  perform control_center.active_project();

  select mode into v_mode
  from claims
  where worker_id=p_worker_id and expires_at>now()
  order by created_at desc
  limit 1;

  if p_policy_key in ('architecture_invariants','computation_guard') then
    raise exception '% requires an explicit schema migration, not an ordinary text-policy edit',p_policy_key;
  end if;

  v_body := coalesce(p_body,'');

  for v_schema in
    select nspname
    from pg_namespace
    where control_center.is_managed_project_schema(nspname)
    order by nspname
  loop
    v_body := replace(v_body,v_schema||'.','{{project}}.');
  end loop;

  insert into control_center.policy_definitions(policy_key,mode,body,config,updated_at)
  values(p_policy_key,null,v_body,'{}'::jsonb,now())
  on conflict(policy_key) do update
    set body=excluded.body, updated_at=now()
  returning * into v_row;

  v_rev := record_change(
    'update_policy','{}'::text[],
    jsonb_strip_nulls(jsonb_build_object('policy_key',p_policy_key,'mode',v_mode))
  );

  return control_center.get_policy(p_policy_key)
    || jsonb_build_object('repository_revision',v_rev);
end
$function$

```

## upsert_standardization_term(p_worker_id bigint, p_term text, p_status text, p_preferred_term text DEFAULT NULL::text, p_definition text DEFAULT NULL::text, p_notes text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.upsert_standardization_term(p_worker_id bigint, p_term text, p_status text, p_preferred_term text DEFAULT NULL::text, p_definition text DEFAULT NULL::text, p_notes text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$begin
  PERFORM control_center.active_project();
  
  RETURN (

  SELECT core_upsert_standardization_term(
    p_worker_id,p_term,p_status,p_preferred_term,p_definition,p_notes
  )

  );
end$function$

```

## verify_stage(p_worker_id bigint, p_stage_id bigint) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.verify_stage(p_worker_id bigint, p_stage_id bigint)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
DECLARE
  v_stage record;
  v_pair record;
  v_current bigint;
  v_conflicts jsonb := '[]'::jsonb;
  v_read_conflicts jsonb := '[]'::jsonb;
  v_structure jsonb;
  v_digest text;
begin
  PERFORM control_center.active_project();
  
  PERFORM require_math_principal(p_worker_id);

  SELECT * INTO v_stage FROM stages
   WHERE stage_id=p_stage_id
     AND (owner_worker_id=p_worker_id OR claimed_by_worker_id=p_worker_id)
     AND kind='batch'
     AND expires_at>now()
   FOR UPDATE;

  IF v_stage.stage_id IS NULL THEN RAISE EXCEPTION 'stage not found or expired'; END IF;

  FOR v_pair IN SELECT key,value FROM jsonb_each(v_stage.baselines)
  LOOP
    IF v_pair.key='__state_revision' THEN
      SELECT revision INTO v_current FROM state WHERE singleton;
    ELSE
      SELECT version INTO v_current FROM objects
       WHERE id=v_pair.key AND trashed_at IS NULL;
    END IF;

    IF v_current IS DISTINCT FROM (v_pair.value#>>'{}')::bigint THEN
      v_conflicts:=v_conflicts||jsonb_build_array(jsonb_build_object(
        'key',v_pair.key,'expected',(v_pair.value#>>'{}')::bigint,'current',v_current
      ));
    END IF;
  END LOOP;

  FOR v_pair IN SELECT key,value FROM jsonb_each(v_stage.read_math_baselines)
  LOOP
    SELECT math_version INTO v_current FROM objects
     WHERE id=v_pair.key AND trashed_at IS NULL;
    IF v_current IS DISTINCT FROM (v_pair.value#>>'{}')::bigint THEN
      v_read_conflicts:=v_read_conflicts||jsonb_build_array(jsonb_build_object(
        'id',v_pair.key,
        'expected_math_version',(v_pair.value#>>'{}')::bigint,
        'current_math_version',v_current
      ));
    END IF;
  END LOOP;

  v_structure:=stage_structure_report(v_stage.operations);
  v_digest:=stage_digest(
    v_stage.operations,v_stage.baselines,v_stage.read_math_baselines,v_stage.stage_revision
  );

  IF jsonb_array_length(v_conflicts)=0
     AND jsonb_array_length(v_read_conflicts)=0
     AND coalesce((v_structure->>'valid')::boolean,false) THEN
    UPDATE stages
       SET verified_stage_revision=stage_revision,
           verified_digest=v_digest,
           updated_at=now()
     WHERE stage_id=p_stage_id;
  ELSE
    UPDATE stages
       SET verified_stage_revision=null,verified_digest=null,updated_at=now()
     WHERE stage_id=p_stage_id;
  END IF;

  RETURN jsonb_build_object(
    'stage_id',p_stage_id,
    'baselines_current',jsonb_array_length(v_conflicts)=0,
    'read_set_current',jsonb_array_length(v_read_conflicts)=0,
    'structure_valid',coalesce((v_structure->>'valid')::boolean,false),
    'valid',
      jsonb_array_length(v_conflicts)=0
      AND jsonb_array_length(v_read_conflicts)=0
      AND coalesce((v_structure->>'valid')::boolean,false),
    'baseline_conflicts',v_conflicts,
    'read_conflicts',v_read_conflicts,
    'structure_errors',v_structure->'errors',
    'stage_revision',v_stage.stage_revision,
    'verified_digest',CASE
      WHEN jsonb_array_length(v_conflicts)=0
       AND jsonb_array_length(v_read_conflicts)=0
       AND coalesce((v_structure->>'valid')::boolean,false)
      THEN v_digest ELSE null END,
    'operation_count',jsonb_array_length(v_stage.operations),
    'expires_at',v_stage.expires_at
  );
END
$function$

```

## vote_poll(p_worker_id bigint, p_poll_id bigint, p_vote text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.vote_poll(p_worker_id bigint, p_poll_id bigint, p_vote text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
DECLARE
  p record;
  v_vote text:=lower(btrim(coalesce(p_vote,'')));
  v_yes integer:=0;
  v_no integer:=0;
  v_ballots integer:=0;
  v_result text;
  v_rev bigint;
BEGIN
  PERFORM control_center.active_project();

  IF v_vote NOT IN ('yes','no','refuse') THEN
    RAISE EXCEPTION 'vote must be yes, no, or refuse';
  END IF;

  SELECT * INTO p
  FROM polls
  WHERE poll_id=p_poll_id
  FOR UPDATE;

  IF p.poll_id IS NULL THEN
    RAISE EXCEPTION 'poll % not found',p_poll_id;
  END IF;
  IF p.status<>'open' THEN
    RAISE EXCEPTION 'poll % is already closed',p_poll_id;
  END IF;
  IF EXISTS (
    SELECT 1 FROM poll_votes
    WHERE poll_id=p_poll_id AND worker_id=p_worker_id
  ) THEN
    RAISE EXCEPTION 'worker has already responded to poll %',p_poll_id;
  END IF;

  INSERT INTO poll_votes(poll_id,worker_id,response)
  VALUES(p_poll_id,p_worker_id,v_vote);

  UPDATE polls SET updated_at=now() WHERE poll_id=p_poll_id;

  v_rev:=record_change(
    'private_poll_response',
    p.target_ids,
    jsonb_build_object(
      'poll_id',p_poll_id,
      'response_recorded',true,
      'ballot_private',true
    )
  );

  IF v_vote='refuse' THEN
    PERFORM control_center.refresh_vote_need();
    RETURN jsonb_build_object(
      'poll_id',p_poll_id,
      'response','refused',
      'ballot_consumed',false,
      'poll_closed',false,
      'ballot_private',true,
      'repository_revision',v_rev,
      'next_action','The refusal is recorded. No ballot slot was consumed.'
    );
  END IF;

  SELECT
    count(*) FILTER (WHERE response='yes')::integer,
    count(*) FILTER (WHERE response='no')::integer
  INTO v_yes,v_no
  FROM poll_votes
  WHERE poll_id=p_poll_id;

  v_ballots:=v_yes+v_no;

  IF v_ballots < p.vote_limit THEN
    PERFORM control_center.refresh_vote_need();
    RETURN jsonb_build_object(
      'poll_id',p_poll_id,
      'response_recorded',true,
      'ballot_private',true,
      'poll_closed',false,
      'ballots_received',v_ballots,
      'ballots_remaining',p.vote_limit-v_ballots,
      'repository_revision',v_rev,
      'next_action','No further action is required on this poll unless it later returns as an enactment need.'
    );
  END IF;

  v_result:=CASE WHEN v_yes>v_no THEN 'passed' ELSE 'rejected' END;

  UPDATE polls
  SET status=CASE WHEN v_result='passed' THEN 'passed_pending_action' ELSE 'rejected' END,
      closed_at=now(),
      closed_by_worker_id=p_worker_id,
      action_claimed_by=CASE WHEN v_result='passed' THEN p_worker_id ELSE NULL END,
      action_claim_expires_at=CASE WHEN v_result='passed' THEN
        coalesce(
          (select max(c.expires_at) from claims c
           where c.worker_id=p_worker_id and c.need_key='vote' and c.expires_at>now()),
          now()+make_interval(mins=>
            (select greatest(control_center.config_int('ttl.poll_action_min_minutes'),least(control_center.config_int('ttl.poll_action_max_minutes'),coalesce(poll_action_lease_minutes,control_center.config_int('legacy.poll_action_lease_minutes'))))
             from settings where singleton)
          )
        )
        ELSE NULL END,
      updated_at=now()
  WHERE poll_id=p_poll_id
  RETURNING * INTO p;

  v_rev:=record_change(
    'private_poll_closed',
    p.target_ids,
    jsonb_build_object(
      'poll_id',p_poll_id,
      'result',v_result,
      'yes_votes',v_yes,
      'no_votes',v_no,
      'vote_limit',p.vote_limit,
      'ballot_identities_private',true
    )
  );

  PERFORM control_center.refresh_vote_need();

  IF v_result='passed' THEN
    RETURN jsonb_build_object(
      'poll_id',p_poll_id,
      'poll_closed',true,
      'result','passed',
      'yes_votes',v_yes,
      'no_votes',v_no,
      'action',p.action,
      'target_ids',to_jsonb(p.target_ids),
      'ballot_identities_private',true,
      'repository_revision',v_rev,
      'final_voter_action_required',true,
      'next_action','You supplied the final ballot and the poll passed. Enact the stated action now and then call resolve_poll_action(worker_id,poll_id,''enacted'',details), or call resolve_poll_action(...,''deferred'',details). Until enactment, the scheduler keeps the vote need active.'
    );
  END IF;

  RETURN jsonb_build_object(
    'poll_id',p_poll_id,
    'poll_closed',true,
    'result','rejected',
    'yes_votes',v_yes,
    'no_votes',v_no,
    'ballot_identities_private',true,
    'repository_revision',v_rev,
    'next_action','The poll is closed and rejected; no action is enacted.'
  );
END
$function$

```

## watch_stage_reads(p_worker_id bigint, p_stage_id bigint, p_object_ids text[]) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.watch_stage_reads(p_worker_id bigint, p_stage_id bigint, p_object_ids text[])
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
begin
  PERFORM control_center.active_project();
  
  raise exception 'watch_stage_reads no longer captures current versions implicitly. Use watch_stage_reads_v2(worker_id,stage_id,expected_math_versions) with the math_version values actually read.';
end
$function$

```

## watch_stage_reads_v2(p_worker_id bigint, p_stage_id bigint, p_expected_math_versions jsonb) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.watch_stage_reads_v2(p_worker_id bigint, p_stage_id bigint, p_expected_math_versions jsonb)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_stage record;
  v_pair record;
  v_existing jsonb;
  v_add jsonb:='{}'::jsonb;
  v_explicit text[];
  v_ttl integer;
begin
  PERFORM control_center.active_project();
  
  if jsonb_typeof(coalesce(p_expected_math_versions,'null'::jsonb))<>'object' then
    raise exception 'expected_math_versions must be a JSON object {object_id: math_version}';
  end if;

  select * into v_stage from stages
   where stage_id=p_stage_id
     and owner_worker_id=p_worker_id
     and kind='batch'
     and expires_at>now()
   for update;

  if v_stage.stage_id is null then raise exception 'stage not found or expired'; end if;

  for v_pair in select key,value from jsonb_each(p_expected_math_versions)
  loop
    if not exists(
      select 1 from objects where id=v_pair.key and trashed_at is null
    ) then
      raise exception 'watched object % not found',v_pair.key;
    end if;

    begin
      perform (v_pair.value#>>'{}')::bigint;
    exception when others then
      raise exception 'watched math_version for % must be an integer',v_pair.key;
    end;

    v_existing:=v_stage.read_math_baselines->v_pair.key;
    if v_existing is not null then
      if (v_existing#>>'{}')::bigint is distinct from (v_pair.value#>>'{}')::bigint then
        raise exception
          'stage already watches % at math_version %; refusing silent rebase to %. Use explicit rebase_stage only after review.',
          v_pair.key,(v_existing#>>'{}')::bigint,(v_pair.value#>>'{}')::bigint;
      end if;
    else
      v_add:=v_add||jsonb_build_object(v_pair.key,v_pair.value);
    end if;
  end loop;

  select coalesce(array_agg(distinct x),'{}'::text[])
    into v_explicit
  from (
    select jsonb_array_elements_text(
      coalesce(v_stage.payload->'explicit_watch_ids','[]'::jsonb)
    ) x
    union
    select key from jsonb_each(p_expected_math_versions)
  ) q;

  select stage_ttl_minutes into v_ttl from settings where singleton;

  update stages
     set read_math_baselines=read_math_baselines||v_add,
         payload=payload||jsonb_build_object('explicit_watch_ids',to_jsonb(v_explicit)),
         stage_revision=stage_revision+1,
         verified_stage_revision=null,
         verified_digest=null,
         updated_at=now(),
         expires_at=now()+make_interval(mins=>v_ttl)
   where stage_id=p_stage_id
   returning * into v_stage;

  return to_jsonb(v_stage)||jsonb_build_object(
    'added_math_versions',v_add,
    'preserved_existing',true
  );
end
$function$

```

## wave_reset(p_reason text DEFAULT NULL::text) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.wave_reset(p_reason text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_project text;
  v_workers bigint[] := '{}'::bigint[];
  v_claims integer := 0;
  v_runs integer := 0;
  v_presence integer := 0;
  v_stage_claims integer := 0;
  v_audit_snapshots integer := 0;
  v_read_sessions integer := 0;
  v_read_receipts integer := 0;
  v_transition_receipts integer := 0;
  v_broadcasts integer := 0;
  v_suppressions integer := 0;
  v_targeted_requests integer := 0;
begin
  v_project := control_center.active_project();

  perform pg_advisory_xact_lock(hashtext(v_project||'_assignment'));

  select coalesce(array_agg(distinct worker_id),'{}'::bigint[])
    into v_workers
  from (
    select worker_id from runs where status='active'
    union
    select worker_id from claims where expires_at>now()
    union
    select worker_id from presence
  ) q;

  update stages
     set claimed_by_worker_id=null,
         claimable=case
           when kind='batch'
             and mode='research'
             and verified_stage_revision=stage_revision
             and verified_digest is not null
           then true
           else claimable
         end,
         updated_at=now()
   where claimed_by_worker_id is not null;
  get diagnostics v_stage_claims=row_count;

  delete from audit_snapshots;
  get diagnostics v_audit_snapshots=row_count;

  delete from read_sessions
   where owner_worker_id=any(v_workers);
  get diagnostics v_read_sessions=row_count;

  delete from read_receipts
   where worker_id=any(v_workers);
  get diagnostics v_read_receipts=row_count;

  delete from transition_receipts
   where worker_id=any(v_workers);
  get diagnostics v_transition_receipts=row_count;

  delete from presence;
  get diagnostics v_presence=row_count;

  delete from claims;
  get diagnostics v_claims=row_count;

  update runs
     set status='superseded',
         retired_at=coalesce(retired_at,now()),
         expires_at=now(),
         payload=(coalesce(payload,'{}'::jsonb)-'_context_seen')
           || jsonb_strip_nulls(jsonb_build_object(
                'wave_reset_at',now(),
                'wave_reset_reason',nullif(btrim(coalesce(p_reason,'')),'')
              )),
         updated_at=now()
   where status='active';
  get diagnostics v_runs=row_count;

  update assignment_requests
     set status='expired',
         consumed_at=coalesce(consumed_at,now()),
         updated_at=now(),
         disposition=jsonb_build_object(
           'state','expired',
           'reason','target worker expired by wave_reset',
           'expired_at',now()
         )
   where status='pending'
     and target_worker_id is not null
     and target_worker_id=any(v_workers);
  get diagnostics v_targeted_requests=row_count;

  delete from broadcasts;
  get diagnostics v_broadcasts=row_count;

  if to_regclass(format('%I.worker_need_suppressions',v_project)) is not null then
    execute format('delete from %I.worker_need_suppressions',v_project);
    get diagnostics v_suppressions=row_count;
  end if;

  return jsonb_build_object(
    'reset',true,
    'project',v_project,
    'reason',p_reason,
    'worker_ids_expired',cardinality(v_workers),
    'claims_released',v_claims,
    'runs_retired',v_runs,
    'presence_cleared',v_presence,
    'stage_claims_released',v_stage_claims,
    'audit_snapshots_cleared',v_audit_snapshots,
    'read_sessions_cleared',v_read_sessions,
    'read_receipts_cleared',v_read_receipts,
    'transition_receipts_cleared',v_transition_receipts,
    'targeted_assignment_requests_expired',v_targeted_requests,
    'broadcasts_cleared',v_broadcasts,
    'suppressions_cleared',v_suppressions,
    'needs_retained',true
  );
end
$function$

```

## work_digest(p_since_revision bigint DEFAULT NULL::bigint, p_focus_ids text[] DEFAULT NULL::text[]) -> jsonb

```sql
CREATE OR REPLACE FUNCTION control_center.work_digest(p_since_revision bigint DEFAULT NULL::bigint, p_focus_ids text[] DEFAULT NULL::text[])
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
AS $function$
DECLARE v_ids text[]:=coalesce(p_focus_ids,'{}'::text[]);
BEGIN
  PERFORM control_center.active_project();
  RETURN jsonb_build_object(
    'repository_revision',(SELECT revision FROM state WHERE singleton),
    'project',(SELECT jsonb_build_object(
      'phase',s.phase,'grand_theorem',object_capsule(s.grand_theorem_id,control_center.config_int('text.compact_chars'))
    ) FROM state s WHERE singleton),
    'selected_objects',(
      SELECT coalesce(jsonb_agg(object_capsule(o.id,control_center.config_int('text.preview_chars')) ORDER BY array_position(v_ids,o.id)),'[]'::jsonb)
      FROM objects o WHERE o.id=any(v_ids) AND o.trashed_at IS NULL
    ),
    'active_needs',(SELECT coalesce(jsonb_agg(to_jsonb(n) ORDER BY n.priority DESC,n.updated_at),'[]'::jsonb) FROM needs n WHERE n.active),
    'pending_audits',(SELECT coalesce(jsonb_agg(object_capsule(q.id,control_center.config_int('text.compact_chars')) ORDER BY q.audit_priority DESC,q.updated_at),'[]'::jsonb)
      FROM (SELECT id,audit_priority,updated_at FROM objects
            WHERE trashed_at IS NULL AND audit_requested AND audit_status='pending'
            ORDER BY audit_priority DESC,updated_at LIMIT control_center.config_int('work_digest.pending_audit_limit')) q),
    'health',(SELECT to_jsonb(h) FROM health_snapshot h WHERE singleton),
    'recent_changes',CASE WHEN p_since_revision IS NULL THEN '[]'::jsonb ELSE (
      SELECT coalesce(jsonb_agg(to_jsonb(q) ORDER BY q.revision),'[]'::jsonb)
      FROM (SELECT revision,operation,object_ids,details,created_at FROM changes
            WHERE revision>p_since_revision ORDER BY revision LIMIT control_center.config_int('work_digest.recent_change_limit')) q) END
  );
END
$function$

```
