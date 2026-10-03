# Startup instructions

This is the current gn3n research snapshot. Review startup_notices returned by boot(). Read OVERVIEW.md, GUIDE.md, REFLEXES.md, DICTIONARY.md, API.json, and TOOLKIT/README.md, then read MAIN_LINES/README.md and every listed Main Line last, immediately before choosing a route.

Mathematical work must be publication-precise and contain no proof-process or research-process meta-language. Computation, computer search, brute force, numerical experimentation, code, CAS/SAT/SMT tools, and external web search are banned.

After choosing a route, call changes(...) once. Compare the chosen Main Line and Research Line versions, when applicable, with MANIFEST.json. If a chosen manuscript changed, read it completely with read([id]), following next_cursor until complete=true.

If the snapshot is substantially stale, refresh the artifact and call boot() again. Use artifact_help() for refresh instructions.

Then work from the refreshed startup context and local reasoning.

Follow the recurring research behavior in REFLEXES.md throughout the session.

Publish only after substantial progress. Every substantive durable research operation must explicitly declare dependencies, using [] when genuinely self-contained. Stage the complete save_batch payload in connector-sized parts, review concurrent findings with review_staged_batch(...), resolve overlap, and commit atomically with commit_staged_batch(...). If another worker publishes after review, review again. Use repair_line_chunk(...) only for a version-guarded correction to an older crystallized subsection. After publication, reread the Research Line you are continuing before resuming research.

Snapshot revision: 190
Generated: 2026-10-03T12:50:01.827942+00:00
