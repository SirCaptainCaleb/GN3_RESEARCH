# 00 — GN3 startup

This file is the only bootstrap. **Every numbered Markdown file in `GN3/INIT/` is mandatory startup reading and must be read completely, in filename order, before mathematics, Slack synchronization, audit, direction, or GN3 state edits.** Do not choose a subset of the init files.

Repository: `SirCaptainCaleb/GN3_RESEARCH`

## Preferred retrieval when shell Git is available

Git can pull a whole folder tree locally with sparse checkout. If the repository is reachable and authenticated from the shell, use for example:

```bash
git clone --filter=blob:none --sparse https://github.com/SirCaptainCaleb/GN3_RESEARCH.git
cd GN3_RESEARCH
git sparse-checkout set GN3/INIT GN3/PROOF_SPINE GN3/TOOLKIT GN3/RESEARCH_TREE.md
```

Then read every `GN3/INIT/*.md` file in numeric order. The sparse checkout also places the proof spine, toolkit, and research tree locally for the mathematical startup described below.

## GitHub-connector retrieval

The GitHub connector does not expose a repository clone operation. When using it:

1. Call `GitHub.fetch` on
   `https://api.github.com/repos/SirCaptainCaleb/GN3_RESEARCH/contents/GN3/INIT`.
2. Enumerate **every numbered Markdown file returned by that directory listing**. Do not rely on a remembered file list.
3. For each file, use its returned blob `sha` with `GitHub.fetch_blob` and read the complete blob.
4. Read the files in numeric filename order and do not begin substantive work until all have been consumed.

For any other long required file, obtain its blob SHA with a one-line `GitHub.fetch_file` call (`start_line=1`, `end_line=1`) and then read the whole file with `GitHub.fetch_blob`. Search excerpts, truncated `fetch_file` output, summaries, and memory do not count as a complete read.

## Mathematical startup after `GN3/INIT/`

Every GN3 worker then reads completely:

- `GN3/PROOF_SPINE/TWO_TIGHT_PATHS.md`;
- `GN3/RESEARCH_TREE.md`;
- `GN3/TOOLKIT/README.md` and every standalone toolkit module currently indexed there.

After those reads, synchronize the live Slack surfaces relevant to the assigned role, beginning with the current guidance when doing research or direction. Legacy `A7C3/` material is provenance or archaeology and is retrieved only when actually needed.

There is no separate optional research-protocol startup step: the research and audit protocols are numbered files inside `GN3/INIT/`, so they are always read during initialization.
