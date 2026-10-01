
REASONING HYGIENE MODE

Reasoning hygiene maintains a clean distinction between the live proof frame and reusable standalone mathematics. Unary-chain and structural diagnostics are review heuristics, not commands to flatten mathematics.

CANONICAL TOOLKIT ROOT
Every managed project schema has exactly one canonical top-level Toolkit folder: object id methods01, title "Toolkit". It is a root reasoning node with route_key=project_methods and metadata toolkit_home=true, reserved_role=toolkit, factory_reserved=true. Topical toolkits are descendants of methods01; they are not independent toolkit homes. Do not create competing toolkit roots.

REVIEW FIRST
Inspect each candidate's exact mathematics, parent/child role, consumers, and route context. Decide whether it is:
1. a genuinely standalone reusable result, theorem, fence, abstraction, or toolkit lemma, which must be rehomed beneath methods01;
2. an authentic sequential unary segment, which must remain sequential and, when selected into a reasoning-hygiene assignment as a unary cleanup target, must be resolved by faithful replacement recomposition;
3. a diagnostic false positive caused by stale or incorrect structural metadata, which must be repaired so the diagnostic no longer falsely selects it.

Never classify a node standalone merely because it is a leaf or because it has only one parent/child. Standalone means its mathematical value is reusable independently of the local proof-frame position.

MANDATORY REHOME FOR STANDALONE RESULTS
If a node is determined to be genuinely standalone, the actual mathematical object MUST be moved out of the proof/reasoning route and beneath methods01, organized under the most appropriate topical toolkit subnode.

Setting unary_chain_standalone=true by itself is NOT a completed hygiene action. A standalone-marked object outside methods01 is unfinished hygiene work and remains eligible for the hygiene scheduler.

Preserve identity and provenance: move/reparent the original object or subtree rather than cloning the mathematics. Preserve logical edges, certificates, audit state, authorship, and consumers.

Choose the narrowest natural topical home. Examples include path restriction, cover surgery, insertion/replacement, local extension, quadratic potential, extremal structure, reusable fences, fractional methods, or another established topical toolkit. If no suitable topical toolkit exists, create a narrow organizational subnode directly or indirectly beneath methods01 rather than placing the result in an unrelated bucket.

PROOF-FRAME REFERENCES
After rehoming standalone mathematics, the live reasoning/proof route should reference the toolkit result through the appropriate logical/reference/interface edge when that route uses it. A standalone theorem should not remain in the proof tree merely to carry the frame.

If removing the mathematical node would genuinely sever necessary narrative or causal frame continuity and an edge alone is insufficient, a lightweight wrapper node may remain at the old location. Such a wrapper:
- is organizational/nonmathematical, normally proposal/working-unit status;
- contains no duplicated proof or independently asserted theorem;
- explicitly points to the toolkit object that supplies the mathematics;
- exists only to preserve route structure or composition readability.
Use wrappers sparingly. Prefer a direct reference edge when it is enough.

SEQUENTIAL CHAINS AND RECOMPOSITION
Sequential arguments MUST remain nested. Parent-child descent represents causal continuation; siblings represent branches or alternate routes. Never flatten a genuine reasoning chain into siblings merely because it is long.

For an authentic sequential unary segment selected as a reasoning-hygiene cleanup target, the structural cure is replacement recomposition. Create one new node that faithfully contains an equivalent-or-stronger version of the contiguous chain, then use bind_replacement_composition_v2(...) to swap it into the old segment. The recomposed node must have a fresh mathematical statement describing the theorem actually proved by the merged argument: state the hypotheses and resulting conclusion directly (for example, given X,Y,Z, conclusion C holds). Do NOT use the statement field as provenance or say merely that the node combines/recomposes prior nodes; source history belongs in the composition manifest, metadata, or note. The proof body should present the merged argument coherently against that updated statement. Recomposition is an opportunity for proof compression, not transcription: do not preserve every source step verbatim merely because it existed. Actively look for shortcuts, eliminable intermediate claims, duplicated casework, or a more direct argument from inherited premises to the merged conclusion. Prefer the shortest clear proof that establishes an equivalent-or-stronger endpoint theorem. Historical step-by-step provenance remains recoverable from the retired source nodes and composition manifest. Do not resolve an assigned unary cleanup target by flattening it, reparenting its steps as siblings, falsely marking it standalone, or merely recording that it was reviewed.

This does NOT mean arbitrary long sequential arguments elsewhere in the tree are malformed. The hygiene scheduler identifies the segments chosen for cleanup. Outside an assigned cleanup target, unary depth is a review signal rather than a global ban on long chains.

The source nodes are retired rather than left as competing live proof steps. The terminal source may have one or many children; those children must be preserved beneath the replacement. External logical premises must be inherited by the replacement. External logical consumers must be rewired to the replacement. Because the replacement requires fresh audit/support, downstream consumers must enter the appropriate dependency-hold/provisional state until trust is restored.

After every recomposition, verify the actual tree and logical graph rather than trusting the RPC return alone: replacement position, inherited external premises, terminal children, rewired consumers, retired source nodes, audit requirement, and downstream dependency holds.

Reparenting is appropriate only for a genuinely misfiled node or for moving genuinely standalone mathematics into Toolkit. It is NOT a unary-chain shortening operation.

STANDALONE MARKER
Set unary_chain_standalone=true only as part of, or after, the rehome operation. The marker means "this reusable result has intentionally left the proof-frame unary chain"; it is not permission to leave the object in place.

COMPLETION CHECK
Before completing hygiene:
- every assigned authentic unary cleanup target has been resolved by replacement recomposition;
- every node newly judged standalone has been rehomed beneath methods01;
- old proof-frame locations reference the moved mathematics where needed;
- any wrapper left behind is minimal and nonduplicative;
- no authentic sequential chain was flattened;
- every recomposed segment was swapped through bind_replacement_composition_v2;
- replacement position, terminal children, inherited external premises, external consumers, audit state, and downstream dependency holds were verified;
- every non-standalone proved node has the correct positive unary-chain depth after structural refresh;
- reasoning diagnostics show no hard parent-semantic regression;
- standalone-marked objects outside methods01 are either repaired in this assignment or explicitly reported as unresolved.

Hygiene is organizational maintenance, not research-direction selection. Do not choose or suppress mathematical routes merely to make the tree look tidy.


LOW-PRESSURE SEMANTIC-CONTAINER MAINTENANCE

While inspecting or moving a reasoning region for hygiene, also notice whether its inherited semantic container still matches the region after the structural cleanup. Cheap, obvious fixes to semantic_container_text or a nearby boundary are appropriate, especially when a move would otherwise leave a misleading inherited summary.

This is opportunistic secondary maintenance, not a hygiene quota or mandatory sweep. Do not split or merge containers merely to hit a target size, and do not expand a hygiene assignment solely to perfect Atlas granularity. If the correct boundary is not clear from the mathematics already being inspected, leave it alone.
