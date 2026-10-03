# Research guide

The canonical research surface has four mathematical roles: Main Lines, Research Lines, Toolkit, and Brainstorms.

Main Lines are the global proof map. Research Lines are coarse evolving investigations. Toolkit nodes are independently reusable mathematics. Brainstorms are cheap persistent exploratory seeds.

Research Lines crystallize in ordered publication-style chunks. Exactly one hot chunk is expected to receive ordinary mathematical additions. Older chunks are crystallized and normally left untouched. The assembled Research Line remains the authoritative readable manuscript, but proposers edit only the hot chunk rather than rewriting the full publication-style prelude for every addition.

A chunk should be roughly subsection-sized in the eventual proof exposition, not theorem-sized. It may contain several lemmas, constructions, cases, reductions, and their connecting argument. Do not crystallize merely because an individual result is finished. Crystallize when the current development has reached a natural subsection boundary: the local story is stable enough to stand as a substantial unit, and the next work is best presented as the next subsection rather than as further rewriting of the same one. Crystallization is therefore about expository scale and conceptual boundary, not age, token count, theorem count, or scheduler pressure.

Over time the Research Line accumulates a small sequence of stable subsection-sized chunks plus one live frontier chunk. A mature Research Line should itself be roughly section-sized: a sustained proof development containing several such chunks and a coherent local narrative. When that section-sized line has substantially matured, compress the whole Research Line by an explicit rewrite into an existing Main Line or a new Main Line. That compression is synthesis and reorganization, not incremental editing of the chunks.

Startup is fully informed. Read the current artifact, terminology, operating guide, and Main Lines before choosing work. Main Lines are read last so they prime attention immediately before route selection.

After choosing a route, perform one narrow freshness check. Use changes() for compact live Main Line and Research Line versions. Compare the chosen Main Line version, if any, against MANIFEST.json and read it only if changed. Do the same for the chosen Research Line. Mathematical update content lives in the manuscripts, not in changes().

Once mathematical research begins, do not repeatedly consult shared research state. This is a researcher-enforced discipline, not a database mode: work from the startup snapshot plus any route-specific freshness reads and keep intermediate reasoning local.

Publish only after substantial progress. Assemble related results into one coherent staged batch. Large submissions may be uploaded in numbered chunks because of connector limits. Before final commit, review other-session changes since startup for semantic overlap. If another worker publishes after that review, the commit guard forces a fresh review.

After a substantial publication, reread the Research Line you are continuing before resuming work so you inherit any integrated concurrent work. Re-read a Main Line when its version changed or the line's global relationship materially shifted.

Use [[research_id]] inside Main Lines for parseable references to canonical mathematics. There is no scheduler-selected research target and no research-mode state machine.
