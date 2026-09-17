# GN3 startup

This file is the only bootstrap.

**Initialization is a one-time operation for a worker.** On first joining GN3, every numbered Markdown file in `GN3/INIT/` is mandatory startup reading and must be read completely, in filename order, before substantive mathematics, audit, direction, or GN3 state edits. Do not choose a subset of the init files.

After that initialization has been completed, **do not reread the full init set before every task, edit, audit, or research step.** The worker remains initialized and should keep itself current through `#gn3-changelog`.

Repository: `SirCaptainCaleb/GN3_RESEARCH`

## Preferred retrieval when shell Git is available

Git can pull a whole folder tree locally with sparse checkout. If the repository is reachable and authenticated from the shell, use for example:

```bash
git clone --filter=blob:none --sparse https://github.com/SirCaptainCaleb/GN3_RESEARCH.git
cd GN3_RESEARCH
git sparse-checkout set GN3/INIT
```

This checks out the entire `GN3/INIT/` subtree together at one repository revision. During initialization, read every `GN3/INIT/*.md` file in numeric order.

After the init read, the same checkout can add the other startup directories without cloning the legacy tree:

```bash
git sparse-checkout add GN3/PROOF_SPINE GN3/TOOLKIT
```

Read `GN3/RESEARCH_TREE.md` from the same revision with `git show HEAD:GN3/RESEARCH_TREE.md` or by adding that file to the sparse checkout with an appropriate non-cone pattern.

## GitHub-connector retrieval

The GitHub connector does not expose a repository clone operation. During initialization, pin the read to one commit:

1. Call `GitHub.fetch` on
   `https://api.github.com/repos/SirCaptainCaleb/GN3_RESEARCH/branches/main`
   and record the returned commit SHA.
2. Call `GitHub.fetch` on
   `https://api.github.com/repos/SirCaptainCaleb/GN3_RESEARCH/contents/GN3/INIT?ref=<commit-sha>`.
3. Enumerate **every numbered Markdown file returned by that directory listing**. Do not rely on a remembered file list.
4. For each file, call `GitHub.fetch_blob` with the blob `sha` returned by the pinned directory listing and read the complete blob.
5. Read all init files in numeric filename order and do not begin substantive work until all have been consumed.

For any other long file that must be read completely, use `GitHub.fetch_file(..., start_line=1, end_line=1)` to obtain its blob SHA and then read the whole file with `GitHub.fetch_blob`. Search excerpts, truncated `fetch_file` output, summaries, and memory do not count as complete reads when a complete read is required.

## Mathematical startup after `GN3/INIT/`

During initialization, every GN3 worker then reads completely, from the same pinned revision when practical:

- `GN3/PROOF_SPINE/TWO_TIGHT_PATHS.md`;
- `GN3/RESEARCH_TREE.md`;
- `GN3/TOOLKIT/README.md` and every standalone toolkit module currently indexed there.

After those reads, synchronize the live Slack surfaces relevant to the assigned role, beginning with `#gn3-changelog` and the current guidance when doing research or direction. Legacy `A7C3/` material is provenance or archaeology and is retrieved only when actually needed.

There is no separate optional research-protocol startup step: the research and audit protocols are numbered files inside `GN3/INIT/`, so they are always read during initialization.

## Staying current after initialization

Once initialized, use `#gn3-changelog` as the normal update stream.

Read changelog entries newer than the worker's last synchronization point. For each relevant entry:

- if the changelog states a sufficiently precise delta, incorporate that delta and continue;
- if the entry says that a document changed and the stated delta is not enough to work safely, read the changed document or the relevant changed portion;
- if the change affects exact mathematics being proved, audited, or edited, read the exact current mathematical text needed for that work;
- do **not** restart the full initialization sequence merely because some project state changed.

Reinitialize only when the worker is genuinely starting fresh or cannot establish a trustworthy continuity from its prior initialization and subsequent changelog synchronization. Ordinary task changes, new guidance, repository edits, and routine Slack activity do not by themselves require reinitialization.
