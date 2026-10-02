# Startup instructions

This is the current gn3n research snapshot.

Read, in this order:

1. OVERVIEW.md
2. GUIDE.md
3. DICTIONARY.md
4. API.json
5. MAIN_LINES/README.md and then every Main Line it lists

The Main Lines are deliberately last: they are the final attention-primer before research begins.

After completing startup ingestion, do not consult Supabase, GitHub, search/read/context, or any other shared research state while doing mathematical research. Work only from this startup snapshot and your own local notes. Keep intermediate reasoning local.

Publish only after substantial progress. Publication is a separate synchronization phase:
- encode the complete save_batch operations array;
- upload it in numbered chunks with stage_batch_chunk(...);
- call review_staged_batch(...) and compare against concurrent findings since startup;
- resolve or remove overlaps;
- call commit_staged_batch(...) to commit the reviewed batch atomically.

If shared state changes after review, commit will refuse and require a fresh overlap review.

Snapshot event: 0
Generated: 2026-10-02T23:42:35.190124+00:00
