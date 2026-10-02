# Research guide

The canonical research surface has four mathematical roles: Main Lines, Research Lines, Toolkit, and Brainstorms.

Main Lines are the global proof map. Research Lines are coarse evolving investigations whose manuscripts carry the internal reasoning chain. Toolkit nodes are independently reusable mathematics. Brainstorms are cheap persistent exploratory seeds.

Startup is deliberately fully informed. Read the current artifact, terminology, operating guide, and Main Lines before choosing work. Main Lines are read last so they prime attention immediately before route selection.

After choosing a route, perform one narrow freshness check before beginning proof work. Call changes() for the compact live version lists. Compare the chosen Main Line version, if any, against MANIFEST.json; if it differs, read only that Main Line. Then compare the chosen Research Line version, if any; if it differs, read only that Research Line. Do not consume mathematical updates from a changelog. The manuscripts themselves are authoritative.

Once mathematical research begins, do not repeatedly consult shared research state. This is a researcher-enforced discipline, not a database mode: work from the startup snapshot plus any route-specific freshness reads and keep intermediate reasoning local.

Publish only after substantial progress. Assemble related results into one coherent batch. Because connector payloads are small, large batches may be uploaded in numbered staging chunks. Before final commit, review other-session changes since startup for semantic overlap, reconcile any collision, and then commit the batch atomically. If another worker publishes after that review, the commit guard forces a fresh review.

After a substantial publication, the natural refresh point is the Research Line manuscript itself: reread the line you are continuing so you inherit any integrated concurrent work. Consult a Main Line again only when its version changed or the line's global relationship has materially shifted.

Use [[research_id]] inside Main Lines for parseable references to canonical mathematics. Exact logical dependencies are declared against mathematical versions. Supersession is preference, archiving is inactivity, audit failure is a proof/formulation problem, and refutation means the claim is false; these are distinct.

There is no scheduler-selected research target and no research-mode state machine.
