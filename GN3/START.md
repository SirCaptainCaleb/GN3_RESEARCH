# GN3 startup

This file is only a retrieval bootstrap. It does not replace `GN3/ARCHITECTURE.md` or define project policy.

Before doing mathematics, auditing, directing, synchronizing Slack, or editing GN3 state, retrieve the required long files by blob SHA so they are read completely in one call.

Repository: `SirCaptainCaleb/GN3_RESEARCH`

## Required retrieval method

For each long required file:

1. Call `GitHub.fetch_file` on the exact path with `start_line=1` and `end_line=1`.
2. Read the returned file `sha`.
3. Call `GitHub.fetch_blob` with that SHA.
4. Treat the `fetch_blob` result, not the one-line `fetch_file` result, as the file read.

Do not initialize from GitHub search results, excerpts, summaries, an unbounded `fetch_file` call, or memory. Do not begin substantive work if the blob fetch failed or was incomplete.

## Startup files

Always retrieve completely, using the method above:

- `GN3/ARCHITECTURE.md`
- `GN3/PROOF_SPINE/TWO_TIGHT_PATHS.md`
- `GN3/TOOLKIT/README.md`

The toolkit is part of startup mathematical context, not an optional lookup shelf. After reading `GN3/TOOLKIT/README.md`, also retrieve and read every standalone toolkit module that it currently indexes. Results merely indexed back into the proof spine need not be reread separately beyond the required proof-spine read.

Then follow the startup instructions in `GN3/ARCHITECTURE.md` for any additional current-state or role-specific files.

The architecture remains the sole durable authority for GN3 operating rules. This file exists only to make complete retrieval reliable.