# gn3n artifact bootstrap

This directory is the artifact snapshot for repository revision 11600. Supabase remains authoritative for live state and updates.

If you reached this file through gn3n.boot(), the worker identity and boot contract are already established. Legacy startup is quarantined; do not call gn3n.startup().

## Mandatory startup reading

Before the first continue()/sync() call, read ALL of:

1. startup_bootstrap.md
2. kernel.md
3. project_policy.md
4. standardization_dictionary.txt
5. rpc_signatures.txt
6. research_main_lines/README.md
7. every other Markdown document in research_main_lines/

Do not sample research_main_lines/. The complete proof-rehearsal set is the primary mathematical boot context. The standardization dictionary is mandatory; use its definitions rather than inferring project terminology from the rehearsals.

After continue() assigns a mode, and before doing the assigned work, read exactly the matching roles/<mode>.md. That role file is the final mandatory startup document.

No other artifact file is required at startup by default.

## On-demand only

- rpc_definitions.md — consult only when rpc_signatures.txt is insufficient.
- research_lookup/frontier.md
- research_lookup/simplified_forest.md
- research_lookup/statement_forest.md
- research_lookup/statement_plus_proof_forest.md

research_lookup/ is not part of ordinary startup. Use it only when a concrete need remains unresolved after the mandatory material, or when exact historical/result-tree detail is required. Legacy Atlas is quarantined and is not part of the worker interface or generated artifact.

Pull exact live mathematics from Supabase only when needed, especially for changes after this artifact revision or before state-sensitive mutations. continue(worker_id) will report context files whose live hashes have changed since the artifact snapshot rather than resending unchanged artifact material.

Repository revision at export: 11600
