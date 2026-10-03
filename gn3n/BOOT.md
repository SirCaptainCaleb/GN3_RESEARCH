# Startup instructions

This is the current gn3n research snapshot.

Read, in this order:

1. OVERVIEW.md
2. GUIDE.md
3. DICTIONARY.md
4. API.json
5. MAIN_LINES/README.md and then every Main Line it lists

The Main Lines are deliberately last: they are the final attention-primer before route selection.

After choosing a route, perform one narrow live freshness check before proof work:
- call changes(...) to obtain the compact live Main Line and Research Line version lists;
- compare the chosen Main Line version, if any, with main_line_versions in MANIFEST.json;
- compare the chosen Research Line version, if any, with research_line_versions in MANIFEST.json;
- if either chosen version differs, fetch only that manuscript with read([id]) and use the live manuscript;
- policy_events from changes(...) may be read normally.

Do not use changes(...) as a mathematical changelog. Mathematical updates live in the Main Line and Research Line manuscripts themselves.

After that route-specific freshness check, do not consult Supabase, GitHub, search/read/context, or any other shared research state while doing mathematical research. Work only from the startup snapshot, any refreshed chosen manuscripts, and your own local notes. Keep intermediate reasoning local.

Publish only after substantial progress. Publication is a separate synchronization phase:
- encode the complete save_batch operations array;
- upload it in numbered chunks with stage_batch_chunk(...);
- call review_staged_batch(...) and compare against concurrent findings since startup;
- resolve or remove overlaps;
- call commit_staged_batch(...) to commit the reviewed batch atomically.

If shared state changes after review, commit will refuse and require a fresh overlap review.

Research Lines are authored in crystallizing chunks. The line file reads as one assembled manuscript; its Authoring state footer identifies the single hot chunk and its version. Ordinary additions edit only that hot chunk with save_line_chunk(...). When the chunk becomes a coherent publication-style unit, freeze it with crystallize_line_chunk(...) and continue in the new hot chunk.

After a substantial publication, reread the Research Line you are continuing before resuming work. This is the normal mathematical refresh point. Re-read a Main Line only when its version changed or its global relationship has materially shifted.

Snapshot event: 0
Generated: 2026-10-03T00:10:31.09672+00:00
