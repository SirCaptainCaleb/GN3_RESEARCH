# R24 audit: canonical proof unresolved, theorem quarantined pending verification

**Workspace:** D17
**State:** limitation
**Key:** `r24-proof-correctness-status-and-quarantine-impact`

**Summary:** Project-level audit record for R24. The currently selected canonical proof of R24 is the legacy proof P22. This audit could not reconstruct P22 from the present library/database representation, and no accepted D/DR section presently certifies the R24 theorem statement from first principles. Because R24 is a dependency of multiple downstream results, R24 should remain quarantined/unusable until its selected proof is independently reconstructed and verified or a new accepted proof is written. This is a review-state statement, not a proof that R24 is false.

### Audit target
R24, `Singleton order floor and short-complement rigidity`, currently has one selected proof in the theorem lattice: P22.

### What was checked
- Dependency graph: R24 has substantial downstream use, including direct descendants R46, R369, R461, R623, R628, R829, R900, R912, and R921 in the current result graph.
- D17 references: many later sections cite or historically mention R24, but no presently inspected D17 section supplied a self-contained first-principles proof of the exact R24 theorem statement.
- Proof-store accessibility: the project database identifies P22 as the selected proof, but the current research-library interface used in this session did not expose a reconstructible body for P22.

### Audit conclusion
The theorem is not certified by this audit. The failure is epistemic: the canonical proof body could not be independently reconstructed and checked from the current authoritative artifacts.

Therefore:

1. R24 should remain quarantined and unusable as a dependency until verification is complete.
2. Downstream results which use R24 require either independent reproof or explicit quarantine propagation.
3. This audit does NOT assert a counterexample to R24 and does NOT mark the theorem mathematically false.

### Repair path
A future verification pass should do one of:

- recover the exact selected proof P22 and check every turn/cover/order claim against accepted dependencies;
- or write a new self-contained R24 proof using only currently accepted roots and certify that proof through the normal review pipeline.

Until then, treating R24 as an accepted black box is unsafe.