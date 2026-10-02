# Research guide

The canonical research surface has four mathematical roles: Main Lines, Research Lines, Toolkit, and Brainstorms.

Main Lines are the global proof map. Research Lines are coarse evolving investigations whose manuscripts carry the internal reasoning chain. Toolkit nodes are independently reusable mathematics. Brainstorms are cheap persistent exploratory seeds.

Startup is deliberately fully informed. Read the current project snapshot, terminology, operating guide, and Main Lines before beginning research. Main Lines are read last so they prime attention immediately before proof work.

Once mathematical research begins, do not repeatedly consult shared research state. This is a researcher-enforced discipline, not a database mode: work from the startup snapshot and keep intermediate reasoning and partial results local.

Publish only after substantial progress. Assemble related results into one coherent batch. Because connector payloads are small, large batches may be uploaded in numbered staging chunks. Before final commit, review other-session changes since startup for semantic overlap, reconcile any collision, and then commit the batch atomically. If another worker publishes after that review, the commit guard forces a fresh review.

Use [[research_id]] inside Main Lines for parseable references to canonical mathematics. Exact logical dependencies are declared against mathematical versions. Supersession is preference, archiving is inactivity, audit failure is a proof/formulation problem, and refutation means the claim is false; these are distinct.

There is no scheduler-selected research target and no research-mode state machine.
