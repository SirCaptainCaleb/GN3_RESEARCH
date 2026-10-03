# Startup instructions

This is the current gn3n research snapshot. Review startup_notices returned by boot(). Read OVERVIEW.md, GUIDE.md, REFLEXES.md, DICTIONARY.md, API.json, and TOOLKIT/README.md, then read MAIN_LINES/README.md and every listed Main Line last, immediately before choosing a route.

Mathematical work must be publication-precise and contain no proof-process or research-process meta-language. Computation, computer search, brute force, numerical experimentation, code, CAS/SAT/SMT tools, and external web search are banned.

After choosing a route, strongly consider one route-specific search across existing Research Lines and Toolkit entries with include_documents=false to avoid rediscovering known mathematics. This is a research reflex, not a gate: proof work must never be blocked because the search was skipped. Then call changes(...) once. Compare only the chosen Main Line and Research Line versions, if any, with MANIFEST.json. If a chosen manuscript changed, page through it with read([id]); pass next_cursor back into read(...) until complete=true. changes(...) is a freshness signal, not a mathematical changelog. Then work from the refreshed startup context and local reasoning without consulting shared research state.

Follow the recurring research behavior in REFLEXES.md throughout the session.

Publish only after substantial progress. Every substantive durable research operation must explicitly declare dependencies, using [] when genuinely self-contained. Stage the complete save_batch payload in connector-sized parts, review concurrent findings with review_staged_batch(...), resolve overlap, and commit atomically with commit_staged_batch(...). If another worker publishes after review, review again. Use repair_line_chunk(...) only for a version-guarded correction to an older crystallized subsection. After publication, reread the Research Line you are continuing before resuming research.

Snapshot revision: 112
Generated: 2026-10-03T03:54:25.497604+00:00
