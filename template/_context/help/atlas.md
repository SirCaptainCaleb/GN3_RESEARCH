
ATLAS

atlas() returns the complete conceptual mathematical Atlas derived from live semantic-container boundaries. Every eligible node with semantic_container_text starts an Atlas entry; descendants inherit the nearest such container until another boundary begins. The default Atlas is not truncated and atlas_height affects sibling prominence/order only, never membership.

Each conceptual entry gives its container ID, nearest parent container, title, semantic summary, direct member count, and pending/obstructed counts. Use atlas(container_id) for that conceptual subtree; targeted subtree views additionally include direct member object IDs.

atlas('pending') and atlas('obstructed') select conceptual containers with direct pending or obstructed members. Other selectors may match object/research/mathematical/audit/support classifications represented by a container.

atlas('all',limit), atlas('objects',limit), and atlas('raw',limit) are the paginated raw eligible-object index. This is the escape hatch for exhaustive object-level navigation. The Atlas is deliberately not embedded in startup(); call atlas() immediately after startup() before continue(worker_id).

Archive-hidden, trashed, failed-audit, fence-only, and effectively superseded material is omitted. Retained semantic parents with active descendants may remain as context.
