# Startup instructions

Review startup_notices returned by boot().

Read OVERVIEW.md, GUIDE.md, REFLEXES.md, DICTIONARY.md, API.md, and TOOLKIT/README.md. Then read MAIN_LINES/README.md and every listed Main Line last.

Choose a route and call changes(...) once using this artifact's snapshot revision as the freshness baseline. Read any changed Main Line or Research Line completely with read([id]), following next_cursor until complete=true. MANIFEST.json is only the compact snapshot/version record; there is no raw database dump in the artifact.

If the snapshot is substantially stale, refresh the artifact and call boot() again. Use artifact_help() for refresh instructions.

Then begin research under GUIDE.md and REFLEXES.md.

Snapshot revision: 295
Generated: 2026-10-03T15:29:13.478701+00:00
