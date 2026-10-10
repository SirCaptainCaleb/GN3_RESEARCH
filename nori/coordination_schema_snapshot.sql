-- NORI coordination schema and RPCs (reconstructed from live verified definitions, Oct 2026).
-- Apply after core NORI tables, research_core sessions/events, and mirror context support.
-- Supabase migration history: nori_coordination_strategy_freshness_metrics_and_versioned_decisions,
-- nori_coordination_checkpoint_preserve_update_watermark,
-- nori_coordination_via_existing_mirror_context, nori_boot_includes_live_coordination_context,
-- nori_distinguish_verified_transfers_from_requested_transfers_in_metrics.
-- Run under privileged migration role. This snapshot deliberately omits historical session data.

CREATE TABLE IF NOT EXISTS nori.coordination_baselines (
  "id" bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
  "session_id" text NOT NULL,
  "captured_at" timestamp with time zone DEFAULT now() NOT NULL,
  "snapshot_revision" bigint NOT NULL,
  "live_revision" bigint NOT NULL,
  "inventory" jsonb NOT NULL,
  "composition_snapshot" jsonb NOT NULL,
  "obligations" jsonb NOT NULL,
  "duplicate_candidates" jsonb NOT NULL,
  "provenance_summary" jsonb NOT NULL,
  "stewardship" jsonb NOT NULL,
  CONSTRAINT "coordination_baselines_pkey" PRIMARY KEY (id)
);
ALTER TABLE nori.coordination_baselines ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE nori.coordination_baselines FROM PUBLIC, anon, authenticated;

CREATE TABLE IF NOT EXISTS nori.coordination_objectives (
  "id" text NOT NULL,
  "target_statement" text NOT NULL,
  "scope_hypotheses" text NOT NULL,
  "relevance" text NOT NULL,
  "closure_connection" text NOT NULL,
  "article_ids" text[] DEFAULT '{}'::text[] NOT NULL,
  "prerequisite_item_ids" text[] DEFAULT '{}'::text[] NOT NULL,
  "unresolved_bridge" text NOT NULL,
  "strongest_obstruction" text NOT NULL,
  "decisive_step" text NOT NULL,
  "selection_rationale" text NOT NULL,
  "lifecycle" text DEFAULT 'proposed'::text NOT NULL,
  "truth_status" text DEFAULT 'open'::text NOT NULL,
  "reopening_condition" text,
  "evidence" jsonb DEFAULT '{}'::jsonb NOT NULL,
  "created_session" text NOT NULL,
  "updated_session" text NOT NULL,
  "revision" integer DEFAULT 1 NOT NULL,
  "created_at" timestamp with time zone DEFAULT now() NOT NULL,
  "updated_at" timestamp with time zone DEFAULT now() NOT NULL,
  CONSTRAINT "coordination_objectives_check" CHECK (((lifecycle <> 'parked'::text) OR (NULLIF(reopening_condition, ''::text) IS NOT NULL))),
  CONSTRAINT "coordination_objectives_lifecycle_check" CHECK ((lifecycle = ANY (ARRAY['proposed'::text, 'active'::text, 'parked'::text, 'resolved'::text]))),
  CONSTRAINT "coordination_objectives_pkey" PRIMARY KEY (id),
  CONSTRAINT "coordination_objectives_relevance_check" CHECK ((relevance = ANY (ARRAY['equivalent'::text, 'sufficient'::text, 'necessary'::text, 'special_case_extension'::text, 'exploratory'::text]))),
  CONSTRAINT "coordination_objectives_truth_status_check" CHECK ((truth_status = ANY (ARRAY['open'::text, 'proved'::text, 'refuted'::text, 'conditional'::text, 'mixed'::text])))
);
ALTER TABLE nori.coordination_objectives ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE nori.coordination_objectives FROM PUBLIC, anon, authenticated;

CREATE TABLE IF NOT EXISTS nori.coordination_relationships (
  "id" bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
  "source_id" text NOT NULL,
  "target_id" text NOT NULL,
  "relation" text NOT NULL,
  "evidence_item_ids" text[] DEFAULT '{}'::text[] NOT NULL,
  "assessment" text NOT NULL,
  "recorded_session" text NOT NULL,
  "created_at" timestamp with time zone DEFAULT now() NOT NULL,
  CONSTRAINT "coordination_relationships_pkey" PRIMARY KEY (id),
  CONSTRAINT "coordination_relationships_relation_check" CHECK ((relation = ANY (ARRAY['refutes_extension'::text, 'strengthens'::text, 'duplicates'::text, 'independent_verification'::text, 'complementary'::text, 'shares_bridge'::text, 'supersedes'::text, 'transfer_required'::text, 'transfer_established'::text]))),
  CONSTRAINT "coordination_relationships_source_id_target_id_relation_key" UNIQUE (source_id, target_id, relation)
);
ALTER TABLE nori.coordination_relationships ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE nori.coordination_relationships FROM PUBLIC, anon, authenticated;

CREATE TABLE IF NOT EXISTS nori.coordination_tasks (
  "id" bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
  "objective_id" text NOT NULL,
  "session_id" text NOT NULL,
  "target_key" text NOT NULL,
  "question" text NOT NULL,
  "intended_method" text NOT NULL,
  "decision_enabled" text NOT NULL,
  "role" text NOT NULL,
  "selection_argument" jsonb NOT NULL,
  "started_at" timestamp with time zone DEFAULT now() NOT NULL,
  "lease_expires_at" timestamp with time zone NOT NULL,
  "latest_checkpoint" jsonb,
  "checkpoint_at" timestamp with time zone,
  "unchanged_bridge_extensions" integer DEFAULT 0 NOT NULL,
  "status" text DEFAULT 'claimed'::text NOT NULL,
  "outcome" jsonb,
  "decision" text,
  "completed_at" timestamp with time zone,
  "modified_session" text NOT NULL,
  CONSTRAINT "coordination_tasks_check" CHECK ((lease_expires_at > started_at)),
  CONSTRAINT "coordination_tasks_decision_check" CHECK ((decision = ANY (ARRAY['continue'::text, 'park'::text, 'resolve'::text, 'switch'::text]))),
  CONSTRAINT "coordination_tasks_objective_id_fkey" FOREIGN KEY (objective_id) REFERENCES nori.coordination_objectives(id),
  CONSTRAINT "coordination_tasks_pkey" PRIMARY KEY (id),
  CONSTRAINT "coordination_tasks_role_check" CHECK ((role = ANY (ARRAY['primary_proof'::text, 'independent_verification'::text, 'alternative_method'::text, 'counterexample_search'::text, 'synthesis'::text, 'exploration'::text]))),
  CONSTRAINT "coordination_tasks_selection_argument_check" CHECK ((selection_argument ?& ARRAY['target'::text, 'consequence'::text, 'remaining_gap'::text, 'decisive_step'::text, 'alternative'::text])),
  CONSTRAINT "coordination_tasks_status_check" CHECK ((status = ANY (ARRAY['claimed'::text, 'finished'::text, 'expired'::text])))
);
ALTER TABLE nori.coordination_tasks ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE nori.coordination_tasks FROM PUBLIC, anon, authenticated;

CREATE TABLE IF NOT EXISTS nori.coordination_updates (
  "id" bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
  "session_id" text NOT NULL,
  "kind" text NOT NULL,
  "objective_ids" text[] NOT NULL,
  "affected_item_versions" jsonb DEFAULT '[]'::jsonb NOT NULL,
  "mathematical_discovery" text NOT NULL,
  "implication" text NOT NULL,
  "priority_change" text NOT NULL,
  "reopening_condition" text,
  "evidence_references" jsonb DEFAULT '[]'::jsonb NOT NULL,
  "affected_task_ids" bigint[] DEFAULT '{}'::bigint[] NOT NULL,
  "created_at" timestamp with time zone DEFAULT now() NOT NULL,
  CONSTRAINT "coordination_updates_kind_check" CHECK ((kind = ANY (ARRAY['discovery'::text, 'obstruction'::text, 'priority'::text, 'verification'::text, 'synthesis'::text, 'reopening'::text, 'duplication'::text]))),
  CONSTRAINT "coordination_updates_objective_ids_check" CHECK ((COALESCE(array_length(objective_ids, 1), 0) > 0)),
  CONSTRAINT "coordination_updates_pkey" PRIMARY KEY (id)
);
ALTER TABLE nori.coordination_updates ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE nori.coordination_updates FROM PUBLIC, anon, authenticated;

CREATE UNIQUE INDEX IF NOT EXISTS nori_coord_unique_live_role ON nori.coordination_tasks USING btree (objective_id, target_key, role) WHERE (status = 'claimed'::text);
CREATE INDEX IF NOT EXISTS nori_coord_claim_expiry ON nori.coordination_tasks USING btree (lease_expires_at) WHERE (status = 'claimed'::text);

-- nori.coordination_publish_update
CREATE OR REPLACE FUNCTION nori.coordination_publish_update(p_session text, p_kind text, p_objectives text[], p_items jsonb, p_discovery text, p_implication text, p_priority_change text, p_evidence jsonb DEFAULT '[]'::jsonb, p_reopening_condition text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'pg_catalog', 'nori', 'research_core'
AS $function$
 declare v_obj text; v_ref jsonb; v_row nori.coordination_updates%rowtype;
 begin
 if not exists(select 1 from research_core.sessions where public_id=p_session and project_schema='nori') then raise exception 'invalid NORI session'; end if;
 if p_kind not in ('discovery','obstruction','priority','verification','synthesis','reopening','duplication') then raise exception 'invalid strategic update kind'; end if;
 if coalesce(array_length(p_objectives,1),0)=0 then raise exception 'objective required'; end if;
 foreach v_obj in array p_objectives loop
 if not exists(select 1 from nori.coordination_objectives where id=v_obj) then raise exception 'unknown objective %',v_obj; end if;
 end loop;
 if jsonb_typeof(coalesce(p_items,'[]'::jsonb))<>'array' then raise exception 'item versions must be array'; end if;
 for v_ref in select value from jsonb_array_elements(coalesce(p_items,'[]'::jsonb)) loop
 if not exists(select 1 from nori.nodes where id=v_ref->>'id' and type='item'
 and version=(v_ref->>'version')::bigint) then
 raise exception 'item version is no longer current: %',v_ref; end if;
 end loop;
 insert into nori.coordination_updates(session_id,kind,objective_ids,affected_item_versions,mathematical_discovery,implication,priority_change,reopening_condition,evidence_references,affected_task_ids)
 values(p_session,p_kind,p_objectives,coalesce(p_items,'[]'::jsonb),p_discovery,p_implication,p_priority_change,p_reopening_condition,
 coalesce(p_evidence,'[]'::jsonb),
 array(select id from nori.coordination_tasks where status='claimed' and lease_expires_at>now() and objective_id=any(p_objectives)))
 returning * into v_row;
 return to_jsonb(v_row);
 end $function$
;

-- nori.coordination_claim
CREATE OR REPLACE FUNCTION nori.coordination_claim(p_session text, p_objective_id text, p_target_key text, p_question text, p_method text, p_decision_enabled text, p_role text, p_selection jsonb, p_lease_minutes integer DEFAULT 90)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'pg_catalog', 'nori', 'research_core'
AS $function$
 declare v_task nori.coordination_tasks%rowtype; v_existing nori.coordination_tasks%rowtype;
 begin
 if not exists(select 1 from research_core.sessions where public_id=p_session and project_schema='nori') then raise exception 'invalid NORI session'; end if;
 if p_lease_minutes not between 5 and 480 then raise exception 'lease 5..480 minutes'; end if;
 if not (p_selection ?& array['target','consequence','remaining_gap','decisive_step','alternative'])
 or exists(select 1 from jsonb_each_text(p_selection) k where k.key=any(array['target','consequence','remaining_gap','decisive_step','alternative']) and btrim(k.value)='') then
 raise exception 'five substantive selection answers required'; end if;
 if nullif(btrim(p_target_key),'') is null or nullif(btrim(p_question),'') is null then raise exception 'concrete target required'; end if;
 perform pg_advisory_xact_lock(hashtextextended(p_objective_id || '/' || p_target_key,0));
 if not exists(select 1 from nori.coordination_objectives where id=p_objective_id and lifecycle in ('proposed','active')) then raise exception 'objective not available'; end if;
 update nori.coordination_tasks set status='expired',completed_at=now(),decision='switch',
 outcome=jsonb_build_object('reason','lease expired; no worker outcome','provenance','prospective claim only'),
 modified_session=p_session
 where objective_id=p_objective_id and target_key=p_target_key and status='claimed' and lease_expires_at<=now();
 select * into v_existing from nori.coordination_tasks
 where objective_id=p_objective_id and target_key=p_target_key and role=p_role and status='claimed'
 limit 1;
 if found then return jsonb_build_object('claimed',false,'conflict',to_jsonb(v_existing)); end if;
 insert into nori.coordination_tasks(objective_id,session_id,target_key,question,intended_method,decision_enabled,role,selection_argument,lease_expires_at,modified_session)
 values(p_objective_id,p_session,p_target_key,p_question,p_method,p_decision_enabled,p_role,p_selection,now()+make_interval(mins=>p_lease_minutes),p_session)
 returning * into v_task;
 return jsonb_build_object('claimed',true,'task',to_jsonb(v_task));
 end $function$
;

-- nori.coordination_checkpoint
CREATE OR REPLACE FUNCTION nori.coordination_checkpoint(p_session text, p_task_id bigint, p_checkpoint jsonb, p_lease_minutes integer DEFAULT 90)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'pg_catalog', 'nori', 'research_core'
AS $function$
 declare v_task nori.coordination_tasks%rowtype; v_previous_checkpoint timestamptz;
 begin
 if not exists(select 1 from research_core.sessions where public_id=p_session and project_schema='nori') then raise exception 'invalid NORI session'; end if;
 if p_lease_minutes not between 5 and 480 then raise exception 'lease 5..480 minutes'; end if;
 if not(p_checkpoint ?& array['mathematical_change','obligation_effect','next_step','alternative_comparison']) then
 raise exception 'checkpoint needs mathematical_change, obligation_effect, next_step, alternative_comparison'; end if;
 select * into v_task from nori.coordination_tasks where id=p_task_id for update;
 if not found or v_task.session_id<>p_session then raise exception 'task not held by this session'; end if;
 if v_task.status<>'claimed' or v_task.lease_expires_at<=now() then
 update nori.coordination_tasks set status='expired',completed_at=now(),outcome=jsonb_build_object('reason','lease expired'),modified_session=p_session
 where id=p_task_id and status='claimed' and lease_expires_at<=now();
 raise exception 'task lease expired; reclaim target'; end if;
 v_previous_checkpoint := coalesce(v_task.checkpoint_at,v_task.started_at);
 update nori.coordination_tasks set latest_checkpoint=p_checkpoint,checkpoint_at=now(),
 lease_expires_at=now()+make_interval(mins=>p_lease_minutes),
 unchanged_bridge_extensions=case when coalesce((p_checkpoint->>'bridge_unchanged')::boolean,false)
 then unchanged_bridge_extensions+1 else 0 end,modified_session=p_session
 where id=p_task_id returning * into v_task;
 return jsonb_build_object('task',to_jsonb(v_task),'review_recommended',v_task.unchanged_bridge_extensions>=2,
 'pending_updates',(select coalesce(jsonb_agg(to_jsonb(u) order by u.id),'[]'::jsonb) from nori.coordination_updates u
 where v_task.objective_id=any(u.objective_ids) and u.created_at>v_previous_checkpoint));
 end $function$
;

-- nori.coordination_finish
CREATE OR REPLACE FUNCTION nori.coordination_finish(p_session text, p_task_id bigint, p_outcome jsonb, p_decision text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'pg_catalog', 'nori', 'research_core'
AS $function$
 declare v_task nori.coordination_tasks%rowtype;
 begin
 if not exists(select 1 from research_core.sessions where public_id=p_session and project_schema='nori') then raise exception 'invalid NORI session'; end if;
 if p_decision not in ('continue','park','resolve','switch') then raise exception 'explicit continuation decision required'; end if;
 if not(p_outcome ?& array['mathematical_change','evidence','remaining_bridge','next_step','alternative_comparison']) then
 raise exception 'outcome must record evidence and continuation rationale'; end if;
 select * into v_task from nori.coordination_tasks where id=p_task_id for update;
 if not found or v_task.session_id<>p_session then raise exception 'task not held by session'; end if;
 if v_task.status<>'claimed' or v_task.lease_expires_at<=now() then
 raise exception 'only currently leased tasks can finish'; end if;
 update nori.coordination_tasks set status='finished',outcome=p_outcome,decision=p_decision,
 completed_at=now(),modified_session=p_session where id=p_task_id returning * into v_task;
 return to_jsonb(v_task);
 end $function$
;

-- nori.coordination_decide_objective
CREATE OR REPLACE FUNCTION nori.coordination_decide_objective(p_session text, p_objective_id text, p_state text, p_truth_status text, p_reason text, p_reopening_condition text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'pg_catalog', 'nori', 'research_core'
AS $function$
 declare v_obj nori.coordination_objectives%rowtype;
 begin
 if not exists(select 1 from research_core.sessions where public_id=p_session and project_schema='nori') then raise exception 'invalid NORI session'; end if;
 if nullif(btrim(p_reason),'') is null then raise exception 'decision reason required'; end if;
 update nori.coordination_objectives set lifecycle=p_state,truth_status=p_truth_status,
 reopening_condition=p_reopening_condition,updated_session=p_session,updated_at=now(),revision=revision+1
 where id=p_objective_id returning * into v_obj;
 if not found then raise exception 'objective not found'; end if;
 perform nori.coordination_publish_update(p_session,case when p_state='active' then 'reopening' else 'priority' end,
 array[p_objective_id],'[]'::jsonb,
 p_reason, 'Investigation lifecycle updated; mathematical truth independently recorded',
 'Objective state='||p_state||'; truth='||p_truth_status,'[]'::jsonb,p_reopening_condition);
 return to_jsonb(v_obj);
 end $function$
;

-- nori.coordination_decide_versioned
CREATE OR REPLACE FUNCTION nori.coordination_decide_versioned(p_session text, p_objective_id text, p_expected_revision integer, p_state text, p_truth_status text, p_reason text, p_reopening_condition text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'pg_catalog', 'nori', 'research_core'
AS $function$
declare rec nori.coordination_objectives%rowtype;
begin
 if not exists(select 1 from research_core.sessions where public_id=p_session and project_schema='nori') then raise exception 'invalid session'; end if;
 if nullif(btrim(p_reason),'') is null then raise exception 'decision rationale required'; end if;
 update nori.coordination_objectives set lifecycle=p_state,truth_status=p_truth_status,reopening_condition=p_reopening_condition,
 revision=revision+1,updated_session=p_session,updated_at=now()
 where id=p_objective_id and revision=p_expected_revision returning * into rec;
 if not found then raise exception 'objective version conflict % expected %',p_objective_id,p_expected_revision; end if;
 perform nori.coordination_publish_update(p_session,'priority',array[p_objective_id],'[]'::jsonb,p_reason,
 'Lifecycle changed; mathematical truth tracked separately','State: '||p_state||'; truth: '||p_truth_status,
 '[]'::jsonb,p_reopening_condition);
 return to_jsonb(rec);
end $function$
;

-- nori.coordination_record_baseline
CREATE OR REPLACE FUNCTION nori.coordination_record_baseline(p_session text, p_snapshot bigint)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'pg_catalog', 'nori', 'research_core'
AS $function$
declare b nori.coordination_baselines%rowtype;
begin
 if not exists(select 1 from research_core.sessions where public_id=p_session and project_schema='nori') then raise exception 'invalid session'; end if;
 insert into nori.coordination_baselines(session_id,snapshot_revision,live_revision,inventory,composition_snapshot,obligations,duplicate_candidates,provenance_summary,stewardship)
 select p_session,p_snapshot,p.local_revision,
 jsonb_build_object('articles',(select count(*) from nori.nodes where type='article'),
 'sections',(select count(*) from nori.nodes where type='section'),'subsections',(select count(*) from nori.nodes where type='subsection'),
 'items',(select count(*) from nori.nodes where type='item'),
 'active_tasks',(select count(*) from nori.coordination_tasks where status='claimed' and lease_expires_at>now())),
 (select coalesce(jsonb_agg(jsonb_build_object('id',node_id,'version',composition_version,'composed_at',created_at)),'[]'::jsonb) from nori.compositions c where node_type='article' and composition_version=(select max(composition_version) from nori.compositions d where d.node_type=c.node_type and d.node_id=c.node_id)),
 (select coalesce(jsonb_agg(jsonb_build_object('id',id,'bridge',unresolved_bridge,'obstruction',strongest_obstruction)),'[]'::jsonb) from nori.coordination_objectives),
 jsonb_build_array('Q12 nine-vertex tight-four Ramsey publications pending exact comparison','window transport versions pending exact comparison'),
 jsonb_build_object('historical_authorship','unknown unless explicitly recorded','session',p_session),
 jsonb_build_object('recomposition_chores',(select count(*) from research_core.chores where project_schema='nori' and kind='recomposition'))
 from research_core.projects p where schema_name='nori' returning * into b;
 return to_jsonb(b);
end $function$
;

-- nori.coordination_metrics
CREATE OR REPLACE FUNCTION nori.coordination_metrics()
 RETURNS jsonb
 LANGUAGE sql
 STABLE SECURITY DEFINER
 SET search_path TO 'pg_catalog', 'nori'
AS $function$
select jsonb_build_object(
 'objectives_resolved',(select count(*) from nori.coordination_objectives where lifecycle='resolved'),
 'materially_sharpened',(select count(*) from nori.coordination_updates where kind in ('discovery','verification')),
 'mechanisms_eliminated',(select count(*) from nori.coordination_updates where kind='obstruction'),
 'transfers_established',(select count(*) from nori.coordination_relationships where relation='transfer_established'),
 'uncoordinated_overlapping_claims',(select count(*) from (select objective_id,target_key,role from nori.coordination_tasks where status='claimed' and lease_expires_at>now() group by 1,2,3 having count(*)>1) v),
 'extensions_with_unchanged_bridge',(select count(*) from nori.coordination_tasks where unchanged_bridge_extensions>=2),
 'exploration_outcomes',(select count(*) from nori.coordination_tasks where role='exploration' and status='finished'),
 'coordination_claims',(select count(*) from nori.coordination_tasks),
 'coordination_checkpoints',(select count(*) from nori.coordination_tasks where checkpoint_at is not null),
 'strategic_updates',(select count(*) from nori.coordination_updates),
 'decisive_publication_delay_seconds',(select round(avg(extract(epoch from (u.created_at - n.created_at)))) from nori.coordination_updates u join lateral jsonb_array_elements(u.affected_item_versions) item on true join nori.nodes n on n.id=item->>'id' where u.kind in ('discovery','obstruction') and u.created_at>=n.created_at)
);
$function$
;

-- nori.coordination_strategy
CREATE OR REPLACE FUNCTION nori.coordination_strategy()
 RETURNS jsonb
 LANGUAGE sql
 STABLE SECURITY DEFINER
 SET search_path TO 'pg_catalog', 'nori', 'research_core'
AS $function$
with clk as (
 select p.local_revision live_revision,
 coalesce(nullif(c.value->'revisions'->>'nori','')::bigint,0) snapshot_revision
 from research_core.projects p left join research_core.configuration c on c.key='artifact.latest.nori'
 where p.schema_name='nori'
), stat as (
 select research_core.status('nori') v
), article_age as (
 select max(created_at) max_composed from nori.compositions where node_type='article'
), fresh_items as (
 select coalesce(jsonb_agg(jsonb_build_object('id',id,'version',version,'title',title,'created_at',created_at) order by created_at desc),'[]'::jsonb) items from
 (select id,version,title,created_at from nori.nodes where type='item'
 and created_at>(select max_composed from article_age) order by created_at desc limit 12) q
)
select jsonb_build_object(
 'conjecture','Every antipodal-reversal-odd coloring of physical ordered three-faces of Q_n admits a full antipodal geodesic with at most one color change',
 'established_scope','Q5 unconditional and Q6 under antipodal reversal oddness; general n open',
 'freshness',jsonb_build_object(
  'artifact_snapshot_revision',(select snapshot_revision from clk),
  'live_revision',(select live_revision from clk),
  'changes_since_snapshot',(select count(*) from research_core.events e where e.project_schema='nori' and e.local_revision>(select snapshot_revision from clk)),
  'composition_dependency_stale',(select count(*) from jsonb_array_elements((select v->'articles' from stat)) x where (x->'composition_status'->>'stale')::boolean),
  'new_item_candidates_since_article_composition',(select count(*) from nori.nodes where type='item' and created_at>(select max_composed from article_age)),
  'strategic_updates_after_snapshot',(select count(*) from nori.coordination_updates u join research_core.events e on e.project_schema='nori' and e.entity_type='coordination_updates' and e.entity_id=u.id::text where e.local_revision>(select snapshot_revision from clk))
 ),
 'active_objectives',(select coalesce(jsonb_agg(jsonb_build_object(
  'id',id,'target',target_statement,'relevance',relevance,'bridge',unresolved_bridge,
  'obstruction',strongest_obstruction,'decisive_step',decisive_step,
  'reason',selection_rationale,'revision',revision,'evidence',evidence,'state',lifecycle)
  order by case id when 'reachability_terminal_collision' then 1 when 'full_geodesic_exchange' then 2 when 'dimension_six_extension' then 3 when 'physical_topology_extraction' then 4 when 'exterior_bit_holonomy' then 5 else 6 end),'[]'::jsonb)
 from nori.coordination_objectives where lifecycle in ('active','proposed')),
 'active_claims',(select coalesce(jsonb_agg(to_jsonb(t) order by t.started_at),'[]'::jsonb) from nori.coordination_tasks t where t.status='claimed' and t.lease_expires_at>now()),
 'parked_objectives',(select coalesce(jsonb_agg(jsonb_build_object('id',id,'reopening_condition',reopening_condition)),'[]'::jsonb) from nori.coordination_objectives where lifecycle='parked'),
 'recent_strategic_updates',(select coalesce(jsonb_agg(to_jsonb(q) order by id desc),'[]'::jsonb) from (select * from nori.coordination_updates order by id desc limit 10) q),
 'new_mathematical_candidates',(select items from fresh_items),
 'relationships',(select coalesce(jsonb_agg(to_jsonb(q)),'[]'::jsonb) from (select * from nori.coordination_relationships order by id desc limit 30) q)
);
$function$
;

-- nori.coordination_change_event
CREATE OR REPLACE FUNCTION nori.coordination_change_event()
 RETURNS trigger
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'pg_catalog', 'nori', 'research_core'
AS $function$
declare v_id text; v_session text; v_version bigint;
begin
 if tg_table_name='coordination_objectives' then
  v_id := new.id; v_session := new.updated_session; v_version := new.revision;
 elsif tg_table_name='coordination_tasks' then
  v_id := new.id::text; v_session := new.modified_session; v_version := null;
 elsif tg_table_name='coordination_updates' then
  v_id := new.id::text; v_session := new.session_id; v_version := null;
 elsif tg_table_name='coordination_baselines' then
  v_id := new.id::text; v_session := new.session_id; v_version := null;
 else
  v_id:=new.id::text; v_session:=new.recorded_session; v_version:=null;
 end if;
 perform research_core.log_event_detail('nori', tg_table_name, v_id, lower(tg_op), null::bigint,v_version,null,
 jsonb_build_object('session_id',v_session));
 return new;
end $function$
;

-- nori.status
CREATE OR REPLACE FUNCTION nori.status()
 RETURNS jsonb
 LANGUAGE sql
 STABLE SECURITY DEFINER
 SET search_path TO 'pg_catalog', 'nori', 'research_core'
AS $function$
 select research_core.status('nori') || jsonb_build_object('coordination',nori.coordination_strategy(),'coordination_metrics',nori.coordination_metrics());
$function$
;

-- nori.boot
CREATE OR REPLACE FUNCTION nori.boot()
 RETURNS json
 LANGUAGE sql
 SECURITY DEFINER
 SET search_path TO 'pg_catalog', 'nori', 'research_core'
AS $function$
select (
 research_core.boot('nori')::jsonb ||
 jsonb_build_object(
  'coordination',nori.coordination_strategy(),
  'coordination_instructions','Read STRATEGY.md in the artifact, then refresh nori.coordination_strategy() before selecting or claiming a task. Give one precise target, consequence, remaining bridge, decisive test, and strongest alternative. Preserve boot session_id in every write.'
 )
)::json;
$function$
;

-- public.research_mirror_context
CREATE OR REPLACE FUNCTION public.research_mirror_context(p_schema text, p_kind text, p_arg text DEFAULT NULL::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 STABLE SECURITY DEFINER
 SET search_path TO 'pg_catalog', 'public'
AS $function$
declare v jsonb;
begin
  if p_schema not in ('gn3n','nor','linp','nori') then
    raise exception 'unsupported research mirror schema %',p_schema;
  end if;

  if p_kind='help' then
    execute format('select %I.help()',p_schema) into v;
  elsif p_kind='revision' then
    select jsonb_build_object(
      'revision',(select local_revision from research_core.projects where schema_name=p_schema),
      'generated_at',now()
    )
    into v
    from research_core.events
    where project_schema=p_schema;
  elsif p_kind='universal_documents' then
    select coalesce(jsonb_agg(to_jsonb(d) order by d.id),'[]'::jsonb)
    into v
    from research_core.universal_documents d;
  elsif p_kind='coordination' and p_schema='nori' then
    v := nori.coordination_strategy();
  elsif p_kind='startup_broadcasts' then
    v := research_core.startup_broadcasts(p_schema);
  else
    raise exception 'unsupported research mirror context kind %',p_kind;
  end if;

  return v;
end;
$function$
;

CREATE TRIGGER coordination_revision_event AFTER INSERT OR UPDATE ON nori.coordination_baselines FOR EACH ROW EXECUTE FUNCTION nori.coordination_change_event();
CREATE TRIGGER coordination_revision_event AFTER INSERT OR UPDATE ON nori.coordination_objectives FOR EACH ROW EXECUTE FUNCTION nori.coordination_change_event();
CREATE TRIGGER coordination_revision_event AFTER INSERT OR UPDATE ON nori.coordination_tasks FOR EACH ROW EXECUTE FUNCTION nori.coordination_change_event();
CREATE TRIGGER coordination_revision_event AFTER INSERT OR UPDATE ON nori.coordination_updates FOR EACH ROW EXECUTE FUNCTION nori.coordination_change_event();
CREATE TRIGGER coordination_revision_event AFTER INSERT OR UPDATE ON nori.coordination_relationships FOR EACH ROW EXECUTE FUNCTION nori.coordination_change_event();
REVOKE ALL ON FUNCTION nori.coordination_change_event() FROM PUBLIC, anon, authenticated;
-- The active project's actual baseline, objective map and strategic updates are data, not migration defaults.
-- Reconcile privileges and existing triggers before applying to an already deployed project.

-- RPC privileges: privileged project services and database owners only.
REVOKE ALL ON FUNCTION nori.coordination_strategy() FROM PUBLIC, anon, authenticated;
REVOKE ALL ON FUNCTION nori.coordination_metrics() FROM PUBLIC, anon, authenticated;
REVOKE ALL ON FUNCTION nori.coordination_record_baseline(text,bigint) FROM PUBLIC, anon, authenticated;
REVOKE ALL ON FUNCTION nori.coordination_decide_versioned(text,text,integer,text,text,text,text) FROM PUBLIC, anon, authenticated;
GRANT EXECUTE ON FUNCTION nori.coordination_strategy() TO service_role;
GRANT EXECUTE ON FUNCTION nori.coordination_metrics() TO service_role;
GRANT EXECUTE ON FUNCTION nori.coordination_record_baseline(text,bigint) TO service_role;
GRANT EXECUTE ON FUNCTION nori.coordination_decide_versioned(text,text,integer,text,text,text,text) TO service_role;

-- Artifact publisher/tree export are private service endpoints.
REVOKE EXECUTE ON FUNCTION public.research_artifact_publish_schema(text,bigint,text,text,text,text,text,bigint,text,bigint) FROM PUBLIC, anon, authenticated;
REVOKE EXECUTE ON FUNCTION public.research_mirror_tree_paths(text,integer,integer) FROM PUBLIC, anon, authenticated;
GRANT EXECUTE ON FUNCTION public.research_artifact_publish_schema(text,bigint,text,text,text,text,text,bigint,text,bigint) TO service_role;
GRANT EXECUTE ON FUNCTION public.research_mirror_tree_paths(text,integer,integer) TO service_role;
