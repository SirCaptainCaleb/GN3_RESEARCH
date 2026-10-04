# Startup instructions

Review startup_notices returned by boot().

Use the extracted artifact as the working research context. Read OVERVIEW.md, GUIDE.md, REFLEXES.md, DICTIONARY.md, API.md, and TOOLKIT/README.md. Then read ARTICLES/README.md. If the prompt asks you to continue an existing Article, read that Article in its entirety, including all of its Sections, before continuing it. Otherwise, read every listed Article in its entirety before choosing which Article or route to work on. Article files are compiled from ordered Sections and mark every Section boundary; read the corresponding SECTIONS file or call read([section_id]) when one Section is the relevant target.

Choose a route and call changes(...) once using this artifact's snapshot revision as the freshness baseline. Compare the chosen Article and Section versions with MANIFEST.json. Continue directly from the artifact for every matching version. For each manuscript whose live version is newer, read the current manuscript completely with read([id]), following next_cursor until complete=true, and use that refreshed manuscript as the local working copy.

When target_revision materially exceeds the artifact snapshot revision, use artifact_help() to refresh the artifact, call boot() again, and continue from the refreshed artifact.

Then begin research under GUIDE.md and REFLEXES.md.

Snapshot revision: 848
Generated: 2026-10-04T19:40:32.793255+00:00
