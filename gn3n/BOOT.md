# Startup instructions

This is the current gn3n research snapshot. Read OVERVIEW.md, GUIDE.md, REFLEXES.md, DICTIONARY.md, and API.json, then read MAIN_LINES/README.md and every listed Main Line last, immediately before choosing a route.

Mathematical work must be publication-precise and contain no proof-process or research-process meta-language. Computation, computer search, brute force, numerical experimentation, code, CAS/SAT/SMT tools, and external web search are banned.

After choosing a route, call changes(...) once. Compare only the chosen Main Line and Research Line versions, if any, with MANIFEST.json; read([id]) only for a chosen manuscript whose live version differs. changes(...) is a freshness signal, not a mathematical changelog. Then work from the refreshed startup context and local reasoning without consulting shared research state.

Follow the recurring research behavior in REFLEXES.md throughout the session.

Publish only after substantial progress. Stage the complete save_batch payload in connector-sized parts, review concurrent findings with review_staged_batch(...), resolve overlap, and commit atomically with commit_staged_batch(...). If another worker publishes after review, review again. After publication, reread the Research Line you are continuing before resuming research.

Snapshot event: 0
Generated: 2026-10-03T00:46:31.486667+00:00
