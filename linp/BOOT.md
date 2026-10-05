# Startup instructions

Review startup_notices returned by boot().

Use the extracted artifact as the working research context. Read OVERVIEW.md, GUIDE.md, REFLEXES.md, DICTIONARY.md, API.md, and TOOLKIT/README.md. Then read ARTICLES/README.md.

If the prompt asks you to continue an existing Article, read that Article's cold composition and every contained Section file before continuing it. Inspect stale markers; for each stale Article or Section, read the Subsections named by its uncompressed-change list, and read additional Subsections when the mathematics requires them.

If the prompt does not select an Article, read every listed Article cold composition before choosing which route to work on. After choosing, descend into that Article's Sections rather than reading every Subsection in the project.

Call changes(...) once using this artifact's snapshot revision as the freshness baseline. A newer Section or Article version is not the only freshness signal: inspect composition_status/stale data because Subsection development can advance without changing the parent canonical version. Use read([subsection_id]) for exact live development when a source is newer.

Article and Section files are not generated concatenations. Their bodies are cold compositions. SUBSECTIONS/ preserves the lower-level development that may or may not survive into those compositions.

Then begin research under GUIDE.md and REFLEXES.md.

Snapshot revision: 1086
Generated: 2026-10-05T02:18:45.452379+00:00
