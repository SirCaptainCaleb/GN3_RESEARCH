# Startup instructions

Review startup_notices returned by boot().

Use the extracted artifact as the working research context. Read OVERVIEW.md, GUIDE.md, REFLEXES.md, DICTIONARY.md, API.md, and TOOLKIT/README.md. Then read ARTICLES/README.md and every listed Article last. Article files are compiled from ordered Sections and mark every Section boundary; read the corresponding SECTIONS file or call read([section_id]) when one Section is the relevant target.

Choose a route and call changes(...) once using this artifact's snapshot revision as the freshness baseline. Compare the chosen Article and Section versions with MANIFEST.json. Continue directly from the artifact for every matching version. For each manuscript whose live version is newer, read the current manuscript completely with read([id]), following next_cursor until complete=true, and use that refreshed manuscript as the local working copy.

When target_revision materially exceeds the artifact snapshot revision, use artifact_help() to refresh the artifact, call boot() again, and continue from the refreshed artifact.

Then begin research under GUIDE.md and REFLEXES.md.

Snapshot revision: 402
Generated: 2026-10-03T21:01:26.736418+00:00
