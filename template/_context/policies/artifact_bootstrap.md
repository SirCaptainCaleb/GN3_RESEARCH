ARTIFACT STARTUP

Use the latest research-context release as the baseline reference instead of loading the ordinary startup packet.

1. Resolve the latest release with the GitHub connector. In code mode, execute exactly:

await tools.mcp__GitHub__fetch({
  url: "https://api.github.com/repos/SirCaptainCaleb/GN3_RESEARCH/releases/latest"
})

From the returned release JSON, find the asset named research-context.zip and use its browser_download_url with the environment's normal file-download capability. Unpack the ZIP and use the directory matching this Supabase schema (gn3n, linp, or template).

2. Treat the artifact as a read-only convenience snapshot of Supabase. The boot() response identifies artifact_revision and live_repository_revision. Use the artifact as reference through artifact_revision. For anything newer than that revision, and before any mutation whose correctness depends on current state, query live Supabase.

3. Use the worker_id returned by boot() for lifecycle and write RPCs. When ready for an operational assignment, call continue(worker_id).

FALLBACK

If the GitHub release or artifact cannot be accessed, use the ordinary live startup path instead:

select * from <project_schema>.startup();

Supabase remains authoritative for live state, RPC behavior, policy changes, trust state, assignments, and updates. The artifact is only a convenience view.
