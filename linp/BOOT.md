# Startup instructions

Review startup_notices returned by boot().

Use the extracted artifact as the working research context. Read OVERVIEW.md, GUIDE.md, REFLEXES.md, DICTIONARY.md, API.md, and TOOLKIT/README.md. Then read MAIN_LINES/README.md and every listed Main Line last. Main Line files are compiled from ordered Research Lines and mark every Research Line boundary; read the corresponding RESEARCH_LINES file or call read([research_line_id]) when one segment is the relevant target.

Choose a route and call changes(...) once using this artifact's snapshot revision as the freshness baseline. Compare the chosen Main Line and Research Line versions with MANIFEST.json. Continue directly from the artifact for every matching version. For each manuscript whose live version is newer, read the current manuscript completely with read([id]), following next_cursor until complete=true, and use that refreshed manuscript as the local working copy.

When target_revision materially exceeds the artifact snapshot revision, use artifact_help() to refresh the artifact, call boot() again, and continue from the refreshed artifact.

Then begin research under GUIDE.md and REFLEXES.md.

Snapshot revision: 402
Generated: 2026-10-03T17:39:09.609649+00:00
