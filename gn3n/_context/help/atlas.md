
ATLAS

atlas() returns the complete conceptual mathematical Atlas derived from live semantic-container boundaries. Every eligible node with semantic_container_text starts an Atlas entry; descendants inherit the nearest such container until another boundary begins. The default Atlas is not truncated and atlas_height affects sibling prominence/order only, never membership.

Each conceptual entry gives its container ID, nearest parent container, title, semantic summary, direct member count, and pending/obstructed counts. Use atlas(container_id) for that conceptual subtree; targeted subtree views additionally include direct member object IDs.

atlas('pending') and atlas('obstructed') select conceptual containers with direct pending or obstructed members. Other selectors may match object/research/mathematical/audit/support classifications represented by a container.

atlas('all',limit), atlas('objects',limit), and atlas('raw',limit) are the paginated raw eligible-object index. This is the escape hatch for exhaustive object-level navigation. The Atlas is deliberately not embedded in startup(); call atlas() immediately after startup() before continue(worker_id).

Archive-hidden, trashed, failed-audit, fence-only, and effectively superseded material is omitted. Retained semantic parents with active descendants may remain as context.


DIRECTIONAL SEMANTIC-CONTAINER STANDARD

A semantic container is not a topic label, filing category, or inventory of nearby concepts. Its purpose is to communicate the mathematical direction of the represented branch.

A good semantic_container_text should, as compactly as the mathematics allows, answer:
- GIVEN: what hypotheses, configuration, reduction state, or inherited interface this branch starts from;
- KNOW: what the branch has actually established, including the strongest useful conclusion or mechanism;
- LEADS TO / REMAINS: what this result enables next, what consumer it feeds, or what unresolved obstruction/conjectural step remains.

Write containers as mathematical transition summaries: “Given A, B forces C; therefore route D reduces to E, with F still unresolved.” Natural prose is preferred; the labels GIVEN/KNOW/REMAINS need not appear literally.

Do not write containers as lists such as “Results about A, B, C,” “Toolkit for X,” or “Work on Y,” unless the node is a genuinely organizational special root whose purpose is only classification. For ordinary mathematical branches, a reader should be able to infer movement through the proof from the container text alone.

The summary should synthesize the represented descendant region rather than merely restating the container node itself. Include unresolved direction when it is important for route choice. Avoid historical/process narration and avoid enumerating every local lemma.

When a branch changes mathematical phase—new hypotheses, a materially stronger producer, a different consumer, or a distinct unresolved interface—that is a natural place for a new semantic-container boundary. Do not create a boundary merely because the subject vocabulary changes.

Atlas quality is judged primarily by whether a fresh mathematician can read it top-to-bottom and understand the project’s major mathematical routes, established transitions, and remaining gaps.
