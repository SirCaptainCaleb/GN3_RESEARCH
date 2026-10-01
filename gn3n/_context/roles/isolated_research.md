ISOLATED RESEARCH MODE

This is a three-phase research mode designed to preserve independent mathematical thought by separating broad context acquisition from tool-free proof search.

1. INGESTION. The assignment begins with database access open. This phase is for BROAD, ANTICIPATORY CONTEXT ACQUISITION, not merely for reading enough to choose a route. Gather anything that could plausibly become useful once tools are unavailable: the complete Atlas as appropriate; exact statements and proofs of likely inputs; definitions and terminology; nearby and competing routes; known failures, counterexamples, obstructions, and grand-closure sinks; brainstorms; reusable toolkit results; consumer/producer interfaces; relevant reasoning subtrees; and any other project material that may prevent a later lookup from being necessary. Follow promising cross-references and preload supporting details when there is a reasonable chance they matter. It is acceptable and desirable for ingestion to be substantially broader than the route ultimately pursued.

Do not optimize ingestion for minimal context, minimal character count, or fastest route selection. The point is to build a rich frozen working snapshot before access closes. At the same time, ingestion is information acquisition only: do not begin proving, extending, or attacking the mathematics while still browsing. Once you have deliberately gathered the context you might reasonably want during the research interval—not merely enough to pick a route—call gn3n.begin_isolated_research(worker_id).

2. ISOLATED RESEARCH. After begin_isolated_research, stop using the research database entirely and do not use external research/navigation tools as a substitute. Do not call continue, sync, Atlas/search/read/navigation, publication, presence, broadcast, maintenance, web/literature, computation, or other lookup tools. Work only from the ingested frozen context and the conversation state.

Isolation has two deliberate purposes:
(a) SNAPSHOT INDEPENDENCE: prevent concurrent project results from influencing the line during the interval;
(b) TOOL-FREE REASONING: remove the habitual temptation to keep consulting the database or other tools instead of carrying the mathematics in working context.

The database is not an ambient memory extension in this phase. Missing a nonessential lookup is preferable to breaking isolation; if a truly essential missing fact prevents responsible continuation, end the research interval and move to submission/transition rather than silently reopening tools. Continue independently across user turns as long as the line remains productive.

3. SUBMISSION. When ready to report accumulated results, call gn3n.begin_isolated_submission(worker_id). This reopens the project only as a publication boundary. Publish the worthwhile results, dependencies, structural placement, and required author-side hygiene as a compact batch. Do not resume research while submitting. Then close the assignment through gn3n.continue(worker_id,outcome,details), which may dispatch any enabled mode next.

Ordinary research and isolated_research are separate scheduler modes. Either can be enabled or disabled independently. Isolated research is not a stricter synonym for ordinary research; it deliberately trades live collaboration and live tool access during proof search for a broader preload followed by stronger independence between collaboration boundaries.

Legacy no-worker-ID read RPCs cannot identify the caller at the SQL layer. They remain forbidden by policy during the isolated phase even though identity-based mechanical blocking is impossible for those signatures. Worker-aware navigation and lifecycle RPCs are mechanically blocked.
