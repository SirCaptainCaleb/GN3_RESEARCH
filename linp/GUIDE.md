# Research guide


The canonical research surface has four mathematical roles: Main Lines, Research Lines, Toolkit, and Brainstorms.

Main Lines are the global proof map. Research Lines are evolving route-specific proof developments. Toolkit entries are independently reusable mathematics. Brainstorms are cheap persistent exploratory seeds.

Route-specific proof development belongs in a Research Line. Continue an existing route in its hot chunk; when a Brainstorm develops into a coherent proof route, create a Research Line for it. Main Lines record global synthesis: update them when the proof architecture changes, when mature Research Line material is compressed upward, or when a Main Line itself needs correction or restructuring. Toolkit contains mathematics whose natural statement stands on its own as a reusable theorem, construction, obstruction, technique, inequality, transformation, or other result. When route work yields such a result, extract the reusable mathematical core to Toolkit and keep the route-specific setup, case structure, and local state in the Research Line.

Research Lines crystallize in ordered publication-style chunks. Exactly one hot chunk receives ordinary mathematical development. Rewrite that chunk as understanding improves. Crystallize it when the local development reaches a natural subsection boundary, then continue in the next hot chunk. Older chunks remain stable; use repair_line_chunk() when a crystallized subsection itself needs correction. The assembled Research Line is the authoritative readable manuscript.

Write mathematical manuscripts at publication quality. State hypotheses explicitly, quantify variables and parameters, distinguish existence from construction, record exact dependencies and exceptional cases, use standard terminology, and make each inference checkable from the preceding statements. Mathematical manuscripts should contain definitions, claims, constructions, reductions, proofs, counterexamples, and obstructions. Operational instructions belong in the Guide.

A chunk should be roughly subsection-sized in the eventual proof exposition. It may contain several lemmas, constructions, cases, reductions, and their connecting argument. A mature Research Line should be roughly section-sized: a coherent proof development containing several such chunks. Compress a mature Research Line into an existing or new Main Line when its mathematics is ready for global synthesis.

Startup is fully informed. Read the current artifact, terminology, operating guide, Toolkit index, and Main Lines before choosing work. Read Main Lines last so the global proof map is fresh when selecting a route.

Mathematical research uses the project artifact, permitted project-state reads during startup and publication synchronization, and mathematical reasoning. Computation, brute-force search, numerical experimentation, code, CAS/SAT/SMT tools, and external web search are outside the research method for this project.

After choosing a route, perform one freshness check with changes(). Compare the chosen Main Line and Research Line versions, when applicable, with MANIFEST.json. Read any changed manuscript completely with read(), following next_cursor until complete=true.

Work locally from the refreshed context until substantial progress is ready to publish.

Every substantive durable research publication declares its actual dependencies, using [] when genuinely self-contained. Assemble related results into one coherent staged batch. Large submissions may be uploaded in numbered chunks. Before commit, review concurrent findings with review_staged_batch(...), resolve overlap, and commit atomically with commit_staged_batch(...). If shared research changes after review, review the batch again.

After publication, reread the Research Line you are continuing. Reread a Main Line when its version changed or the route's global relationship changed materially.

Use [[research_id]] inside Main Lines for parseable references to canonical mathematics.
