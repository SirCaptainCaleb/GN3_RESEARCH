# Research guide

The canonical research surface has four mathematical roles: Main Lines, Research Lines, Toolkit, and Brainstorms.

Main Lines are the global proof map. Research Lines are coarse evolving investigations. Toolkit nodes are independently reusable mathematics. Brainstorms are cheap persistent exploratory seeds.

Research Lines crystallize in ordered publication-style chunks. Exactly one hot chunk is expected to receive ordinary mathematical additions. Older chunks are crystallized and normally left untouched. The assembled Research Line remains the authoritative readable manuscript, but proposers edit only the hot chunk rather than rewriting the full publication-style prelude for every addition.

Mathematical writing must be precise enough for publication-quality proof exposition. State hypotheses explicitly; quantify variables and parameters; distinguish existence from construction; record exact dependencies and exceptional cases; use standard mathematical terminology; and make each inference checkable from the preceding statements. Do not rely on vague qualifiers where a precise statement is available.

Mathematical manuscripts must not contain proof-process or research-process meta-language. Do not narrate workers, routes, frontier status, audits, databases, scheduler state, what remains to be proved, what would complete the proof, what an approach is trying to do, or similar scaffolding. State the mathematics directly: definitions, claims, constructions, reductions, proofs, counterexamples, and obstructions. Operational instructions belong in the Guide, not in mathematical exposition.

A chunk should be roughly subsection-sized in the eventual proof exposition, not theorem-sized. It may contain several lemmas, constructions, cases, reductions, and their connecting argument. Do not crystallize merely because an individual result is finished. Crystallize when the current development has reached a natural subsection boundary: the local story is stable enough to stand as a substantial unit, and the next work is best presented as the next subsection rather than as further rewriting of the same one. Crystallization is therefore about expository scale and conceptual boundary, not age, token count, theorem count, or scheduler pressure.

Over time the Research Line accumulates a small sequence of stable subsection-sized chunks plus one live frontier chunk. A mature Research Line should itself be roughly section-sized: a sustained proof development containing several such chunks and a coherent local narrative. When that section-sized line has substantially matured, compress the whole Research Line by an explicit rewrite into an existing Main Line or a new Main Line. That compression is synthesis and reorganization, not incremental editing of the chunks.

Startup is fully informed. Read the current artifact, terminology, operating guide, and Main Lines before choosing work. Main Lines are read last so they prime attention immediately before route selection.

Computation and external web search are banned for mathematical research. Do not use brute-force enumeration, computer search, numerical experimentation, scripts, code, CAS systems, SAT/SMT solvers, or other computational test beds to discover, test, or support mathematical claims. Do not search the public web for mathematical results or hints. Work from the project artifact, permitted project-state reads during startup/publication synchronization, and mathematical reasoning.

After choosing a route, perform one narrow freshness check. Use changes() for compact live Main Line and Research Line versions. Compare the chosen Main Line version, if any, against MANIFEST.json and page through it with read() only if changed. Do the same for the chosen Research Line. Continue passing next_cursor until complete=true. Mathematical update content lives in the manuscripts, not in changes().

Once mathematical research begins, do not repeatedly consult shared research state. Work from the startup snapshot plus any route-specific freshness reads and keep intermediate reasoning local.

Publish only after substantial progress. Assemble related results into one coherent staged batch. Large submissions may be uploaded in numbered chunks because of connector limits. Before final commit, review other-session changes since startup for semantic overlap. If another worker publishes after that review, the commit guard forces a fresh review.

After a substantial publication, reread the Research Line you are continuing before resuming work so you inherit any integrated concurrent work. Re-read a Main Line when its version changed or the line's global relationship materially shifted.

Use [[research_id]] inside Main Lines for parseable references to canonical mathematics. There is no scheduler-selected research target and no research-mode state machine.
