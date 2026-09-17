# GN3 fresh-worker startup test

This temporary migration test is used only to satisfy checklist item 43. It is not part of ordinary startup.

## Test setup

Start a genuinely fresh worker with no migration conversation, A7C3 Canvas, proof summary, or remembered Engine route supplied in its prompt. Give it only the repository name `SirCaptainCaleb/GN3_RESEARCH` and instruct it to initialize as a GN3 researcher from the canonical architecture.

The worker must retrieve and read one complete revision of `GN3/ARCHITECTURE.md` through `## End of complete architecture` before reading Slack, `STATUS.md`, `RESEARCH_STATE.md`, the proof spine, or doing mathematics.

After following the startup path prescribed by the architecture, ask the worker for a compact initialization report.

## Pass criteria

The report must demonstrate all of the following without relying on A7C3 archaeology:

1. **Authority:** GitHub `GN3/ARCHITECTURE.md` is the sole durable architecture authority; no Canvas is required for startup.
2. **Mathematical representation:** the canonical proof is the single sequential `GN3/PROOF_SPINE/TWO_TIGHT_PATHS.md`, not an Engine graph.
3. **Status:** the exact current spine is audited, while the augmentation statement after Proposition 6.2 is open.
4. **Big picture:** the worker can state the theorem and identify the lexicographic augmentation bridge as the earliest load-bearing unresolved step.
5. **Proof coding:** canonical mathematics must be intrinsic and mathematically compilable; proof-history/meta-language cannot define mathematical objects; restriction or retained facts do not create reachability.
6. **Research method:** null results are permitted; “no proof found” is distinguished from counterexample, missing hypothesis, and structural obstruction; research is abstraction-first and proceeds at increasing resolution.
7. **Certification:** unaudited work may be used optimistically in research, but certification attaches only to exact audited mathematics.
8. **Context discipline:** legacy A7C3 material is archaeology/provenance and is not ordinary startup context.
9. **Slack:** the worker identifies `#gn3-changelog`, `#gn3-research`, and `#gn3-audit` as the intentionally small canonical live set and does not treat renamed `#gn3-lab` as canonical.

A worker that reaches these points only after being corrected, after reading legacy startup material first, or from a partial architecture excerpt does not pass. Fix the startup architecture and rerun with another fresh worker.

## Completion evidence

After a fresh worker passes, record the date and a link or durable summary of the test in migration evidence, then check item 43. Do not mark the test complete merely because the migration owner can reread the file successfully.
