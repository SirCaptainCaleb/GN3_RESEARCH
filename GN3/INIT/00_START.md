# 00 — GN3 startup

This file is the only bootstrap. **Every numbered Markdown file in `GN3/INIT/` is mandatory startup reading and must be read completely, in filename order, before mathematics, Slack synchronization, audit, direction, or GN3 state edits.** Do not choose a subset of the init files.

Repository: `SirCaptainCaleb/GN3_RESEARCH`

## Preferred retrieval when shell Git is available

Git can pull a whole folder tree locally with sparse checkout. If the repository is reachable and authenticated from the shell, use for example:

```bash
git clone --filter=blob:none --sparse https://github.com/SirCaptainCaleb/GN3_RESEARCH.git
cd GN3_RESEARCH
git sparse-checkout set GN3/INIT
```

This checks out the entire `GN3/INIT/` subtree together at one repository revision. Read every `GN3/INIT/*.md` file in numeric order.

After the init read, the same checkout can add the other startup directories without cloning the legacy tree:

```bash
git sparse-checkout add GN3/PROOF_SPINE GN3/TOOLKIT
```

Read `GN3/RESEARCH_TREE.md` from the same revision with `git show HEAD:GN3/RESEARCH_TREE.md` or by adding that file to the sparse checkout with an appropriate non-cone pattern.

## GitHub-connector retrieval

The GitHub connector does not expose a repository clone operation. When using it, pin initialization to one commit:

1. Call `GitHub.fetch` on
   `https://api.github.com/repos/SirCaptainCaleb/GN3_RESEARCH/branches/main`
   and record the returned commit SHA.
2. Call `GitHub.fetch` on
   `https://api.github.com/repos/SirCaptainCaleb/GN3_RESEARCH/contents/GN3/INIT?ref=<commit-sha>`.
3. Enumerate **every numbered Markdown file returned by that directory listing**. Do not rely on a remembered file list.
4. For each file, call `GitHub.fetch_blob` with the blob `sha` returned by the pinned directory listing and read the complete blob.
5. Read all init files in numeric filename order and do not begin substantive work until all have been consumed.

For any other long required file, use the same pinned commit with `GitHub.fetch_file(..., ref=<commit-sha>, start_line=1, end_line=1)` to obtain its blob SHA, then read the whole file with `GitHub.fetch_blob`. Search excerpts, truncated `fetch_file` output, summaries, and memory do not count as complete reads.

## Mathematical startup after `GN3/INIT/`

Every GN3 worker then reads completely, from the same pinned revision when practical:

- `GN3/PROOF_SPINE/TWO_TIGHT_PATHS.md`;
- `GN3/RESEARCH_TREE.md`;
- `GN3/TOOLKIT/README.md` and every standalone toolkit module currently indexed there.

After those reads, synchronize the live Slack surfaces relevant to the assigned role, beginning with the current guidance when doing research or direction. Legacy `A7C3/` material is provenance or archaeology and is retrieved only when actually needed.

There is no separate optional research-protocol startup step: the research and audit protocols are numbered files inside `GN3/INIT/`, so they are always read during initialization.
