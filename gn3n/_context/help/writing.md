
WRITING

create_object(worker_id, object_type, title, statement, body, parent_id, position,
  metadata, research_interface, mathematical_status, research_level, lifecycle_status,
  attention, audit_requested, audit_priority, id, legacy_id)

Typical mathematical_status: proved | conjecture | proposal | evidence.
Typical research_level: working_unit | lemma | theorem | proof_level | abstraction.
attention: focus | available | hidden.

research_interface should compactly expose useful proof-routing information when applicable:
  given, need, consumer, gap, working_route, on_demand_ids.
It is coordination state, not a replacement for the exact theorem statement/proof.

update_object(worker_id,id,expected_version,patch,substantive,nonsubstantive_override=false)
  statement/body/mathematical_status changes are substantive by default and advance math_version.
  For a purely editorial or representational change that touches those fields, pass substantive=false and nonsubstantive_override=true. This is an explicit caller guarantee that the mathematics is unchanged; math_version and trust state are preserved, ordinary version still advances, and the override is recorded in change metadata.
  Organizational changes preserve mathematical certification.

move_object(worker_id,id,expected_version,new_parent_id,position)
  Pure organizational move; no proof recertification.

Influence/dependency edges:
  proof, depends_on = mathematical premises and affect math identity.
  consumes, informs, references, interface, strengthens, supersedes, fence, contradicts
  record research use/structure without pretending to be proof premises.



Choose mathematical_status by epistemic role, not by polish:
- proved: you are asserting a complete proof of the stated mathematical claim;
- conjecture: a crisp mathematical assertion believed true but not proved;
- proposal: an unproved proof mechanism, reduction, construction, route, normal form, or strategic mathematical idea worth sharing;
- evidence: computation, experiments, examples, partial verification, or other support that does not prove the claim.

A useful proposal is expected to be incomplete. Its statement/body should clearly separate established inputs from the proposed inference and name the exact missing proof obligation, hostile test, or next move. Proposals are durable/searchable live mathematics and may be nested in reasoning trees, linked to consumers, and later strengthened, superseded, retired, or trashed.



STANDARD TERMINOLOGY REQUIREMENT

Write durable mathematics in ordinary publication-quality language, preferring established mathematical terminology and direct formulas over locally coined vocabulary. Before finalizing terminology, consult the project-local standardization dictionary with gn3n.standardization_dictionary(). Canonical entries are preferred; alias entries are noncanonical and should be replaced by preferred_term; prohibited entries must not be used in durable mathematical prose. The dictionary is project-local and must never be inferred from another synchronized project.

NESTING REQUIREMENT

Use parent_id as part of the mathematical research representation, not merely for cosmetic organization. If object B continues the reasoning developed in object A, create or move B beneath A (or the nearest natural causal predecessor). Logical/influence edges still record premise and influence semantics, but they do not replace nesting. Sequential reasoning should form a descending document chain; alternative next moves should be sibling children. Leave an object at root only for a genuinely independent line or when its natural parent is genuinely unknown.


SEMANTIC CONTAINERS

Every reasoning node belongs to the nearest ancestor semantic container unless it starts a new one. objects.semantic_container_text is local-only: NULL means inherit upward; a non-NULL value makes that node a semantic-container boundary summarizing what that node and its descendants are establishing. No container-owner ID is stored.

publish_with_dependencies accepts two optional p_object fields:
- container_text: proposed semantic-container summary text.
- replace_parent_container_text: boolean, default false.

If replace_parent_container_text is false, a nonblank container_text is stored on the new node and starts a new semantic container. If container_text is absent/blank, the new node inherits the nearest ancestor container.

If replace_parent_container_text is true, the new node always remains inherited (its own semantic_container_text stays NULL). With no container_text, it inherits unchanged. With container_text, the nearest ancestor semantic container is updated to that text, allowing a newly published descendant to refresh the summary of the line it extends. This mode requires an ancestor semantic container.

update_object may patch semantic_container_text directly for organizational maintenance; this is non-substantive mathematics.

SEMANTIC-CONTAINER MAINTENANCE

Container summaries and boundaries are organizational metadata. Maintain them opportunistically when nearby mathematics is already being reviewed—especially during elevation, audit, or reasoning hygiene. Prefer cheap, clearly justified corrections; do not perform broad container sweeps, optimize to a target size, or treat imperfect granularity as a mathematical defect.


SIMPLIFIED TREE VIEW

simplified_subtree(root_id,max_depth=null) shows a compact indented subtree using simplified_statement rather than full object bodies. max_depth defaults from the configurable subtree.simplified_default_depth. A … child marker means deeper descendants of that branch were omitted by the depth limit.


DIRECTIONAL CONTAINER WRITING STANDARD

semantic_container_text must describe mathematical motion, not subject classification. For an ordinary research branch, summarize the effective transition: what is assumed or inherited, what has been established, and what this now enables or leaves unresolved. Prefer prose of the form “Given A, we obtain B via C; this reduces the route to D / leaves E.”

Do not use semantic_container_text as a bag of keywords, a contents list, or a heading such as “Results about X.” Such labels destroy Atlas utility because they do not tell a reader what the branch proves or where it goes.

A container summarizes the represented descendant region, not only its boundary node. Start a new boundary when the mathematical state or direction materially changes, not merely when terminology changes. Special organizational roots such as Toolkit, Brainstorms, Archive, or project documentation may remain categorical because they are genuinely organizational rather than proof-directional.
