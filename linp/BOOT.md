# Startup instructions

This is the current linp research snapshot. Read OVERVIEW.md, GUIDE.md, DICTIONARY.md, and API.json, then read MAIN_LINES/README.md and every listed Main Line last, immediately before choosing a route.

Mathematical work must be publication-precise and contain no proof-process or research-process meta-language. Computation, computer search, brute force, numerical experimentation, code, CAS/SAT/SMT tools, and external web search are banned.

After choosing a route, call changes(...) once. Compare only the chosen Main Line and Research Line versions, if any, with MANIFEST.json; read([id]) only for a chosen manuscript whose live version differs. changes(...) is a freshness signal, not a mathematical changelog. Then work from the refreshed startup context and local reasoning without consulting shared research state.

Research reflex: for every worthwhile result, identify the mechanism that proves it, seek its strongest natural formulation, weaken unnecessary hypotheses, and test useful generalizations or stronger consequences. If it belongs to a predecessor chain, try to apply it as early as possible; determine the minimum additional conditions needed there and ask whether they can themselves be proved or forced.

Research Lines are assembled manuscripts authored through subsection-sized chunks. Rewrite only the hot chunk during ordinary development; crystallize it at a natural subsection boundary, not at each theorem. A mature Research Line should be roughly section-sized before being compressed by rewrite into an existing or new Main Line.

Publish only after substantial progress. Stage the complete save_batch payload in connector-sized parts, review concurrent findings with review_staged_batch(...), resolve overlap, and commit atomically with commit_staged_batch(...). If another worker publishes after review, review again. After publication, reread the Research Line you are continuing before resuming research.

Snapshot event: 0
Generated: 2026-10-03T00:28:38.757259+00:00
