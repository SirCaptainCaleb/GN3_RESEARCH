# Startup instructions

This is the current linp research snapshot. Review startup_notices returned by boot(). Read OVERVIEW.md, GUIDE.md, REFLEXES.md, DICTIONARY.md, API.json, and TOOLKIT/README.md, then read MAIN_LINES/README.md and every listed Main Line last, immediately before choosing a route.

Mathematical work must be publication-precise and contain no proof-process or research-process meta-language. Computation, computer search, brute force, numerical experimentation, code, CAS/SAT/SMT tools, and external web search are banned.

After choosing a route, strongly consider one route-specific search across existing Research Lines and Toolkit entries with include_documents=false to avoid rediscovering known mathematics. This is a research reflex, not a gate: proof work must never be blocked because the search was skipped. Then call changes(...) once. Compare only the chosen Main Line and Research Line versions, if any, with MANIFEST.json. If a chosen manuscript changed, page through it with read([id]); pass next_cursor back into read(...) until complete=true. changes(...) is a freshness signal, not a mathematical changelog.

If the snapshot is stale enough that refreshing the relevant context piecemeal would require substantial rereading, do not reconstruct a large new snapshot through many delta reads. Refresh the artifact instead. In GitHub Actions for SirCaptainCaleb/GN3_RESEARCH, find the most recent "Sync research mirror" run, fetch its jobs, and rerun its "sync" job with the workflow-job rerun capability. When that rerun succeeds it automatically triggers "Build research context artifact", which publishes the new artifact metadata back to Supabase. Then call boot() again and download the newly identified startup artifact. If no usable Sync run exists, call artifact_help() for the deeper recovery path.

Then work from the refreshed startup context and local reasoning without consulting shared research state.

Follow the recurring research behavior in REFLEXES.md throughout the session.

Publish only after substantial progress. Every substantive durable research operation must explicitly declare dependencies, using [] when genuinely self-contained. Stage the complete save_batch payload in connector-sized parts, review concurrent findings with review_staged_batch(...), resolve overlap, and commit atomically with commit_staged_batch(...). If another worker publishes after review, review again. Use repair_line_chunk(...) only for a version-guarded correction to an older crystallized subsection. After publication, reread the Research Line you are continuing before resuming research.

Snapshot revision: 145
Generated: 2026-10-03T04:38:05.607866+00:00
