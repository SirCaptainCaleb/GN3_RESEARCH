# Research guide

The canonical research surface has four mathematical roles: Main Lines, Research Lines, Toolkit, and Brainstorms.

Main Lines are the global proof map. Research Lines are coarse evolving investigations. Toolkit nodes are independently reusable mathematics. Brainstorms are cheap persistent exploratory seeds.

Research Lines crystallize in ordered publication-style chunks. Exactly one hot chunk is expected to receive ordinary mathematical additions. Older chunks are crystallized and normally left untouched. The assembled Research Line remains the authoritative readable manuscript, but proposers edit only the hot chunk rather than rewriting the full publication-style prelude for every addition.

When a hot chunk has become a coherent piece of mathematics, crystallize it and open a fresh hot chunk. Over time the line accumulates a small sequence of stable chunks plus one live frontier chunk. Eventually the mathematical content of the entire Research Line should be compressed by an explicit rewrite into an existing Main Line or a new Main Line; that compression is synthesis, not incremental editing.

Startup is fully informed. Read the current artifact, terminology, operating guide, and Main Lines before choosing work. Main Lines are read last so they prime attention immediately before route selection.

After choosing a route, perform one narrow freshness check. Use changes() for compact live Main Line and Research Line versions. Compare the chosen Main Line version, if any, against MANIFEST.json and read it only if changed. Do the same for the chosen Research Line. Mathematical update content lives in the manuscripts, not in changes().

Once mathematical research begins, do not repeatedly consult shared research state. This is a researcher-enforced discipline, not a database mode: work from the startup snapshot plus any route-specific freshness reads and keep intermediate reasoning local.

Publish only after substantial progress. Assemble related results into one coherent staged batch. Large submissions may be uploaded in numbered chunks because of connector limits. Before final commit, review other-session changes since startup for semantic overlap. If another worker publishes after that review, the commit guard forces a fresh review.

After a substantial publication, reread the Research Line you are continuing before resuming work so you inherit any integrated concurrent work. Re-read a Main Line when its version changed or the line's global relationship materially shifted.

Use [[research_id]] inside Main Lines for parseable references to canonical mathematics. There is no scheduler-selected research target and no research-mode state machine.
