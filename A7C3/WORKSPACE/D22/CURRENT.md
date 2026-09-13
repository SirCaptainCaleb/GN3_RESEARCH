# D22 — Transversal equality kernels, replacement fans, and the endpoint-extension obstruction

Develops the common-triple/transversal equality program and its replacement-fan descendants, including positive-excess kernels, four-witness shields, paired-anchor geometry, the valid P4+trimer amplification, and the countermodels and tested-order failures that killed stronger endpoint-preserving and parity claims.

## Minimum-overlap common-triple deletion and equality kernel

R99 is the common-triple gateway. Take two global-longest five-supports A and B with minimum overlap three. Write their common triple as S and their two-vertex wings as U,V. Deleting S leaves a residual set R of three vertices. The prescribed-support/minimum-overlap conditions rule out the asymmetric `5+2` completion profile, so the exact completion has profile `4+3`. Applying the partition-deficit identity to the three classes U,V,R gives a one-transition-plus-excess formula. Zero excess forces a canonical wing concatenation around a tight trimer; positive excess supplies at least two independent crossing resources. This is the source of the later “equality versus positive-excess” split.

R101 makes the split symmetric over the three transversal frames. R102 packages the equality case as a four-witness shield. R103 shows that the zero-packet branch is stable under the paired-trimer reroot symmetry. These claims are best understood as one exact equality kernel: either the deficit is genuinely positive, yielding additional crossing states, or equality rigidifies the local supports enough to expose a bounded shield/fan.



## Common markers, four-family lifts, and canonical fans

R106 installs a common exterior marker triple as the root coordinate. R110 and R112 lift the local mate structure simultaneously across four pivot/support families; R111 supplies the neighboring-root symmetric-difference bridge needed to compare those families without pretending their representatives coincide. R113 actualizes the resulting canonical-core fan.

R114-R120 refine the fan by repeated signed-support comparisons. Six same-support/two-witness collisions create a terminal repetition trichotomy; the canonical six-cycle and private-anchor parity of R116 feeds the paired-anchor rectangle R117. R118 lifts paired anchors through trimers and exposes a third-witness dichotomy. R119/R120 align the common-core-marker triple with the paired-anchor middle trimers. These statements retain actual physical supports and witnesses. Their use is local: they do not imply that every historical support in the fan is simultaneously selected.



## Positive excess, universal shields, and folded anchors

R121 is the bridge out of the pure equality kernel: simultaneous zero-excess at the relevant neighboring roots is impossible because the marker bridge would recreate the forbidden overlap pattern, so one frame must have positive excess. R122 interprets that excess as wing interleaving and a six-exterior shield. R123-R125 turn the shield into a universal four-witness fold fan and then a four-anchor clique cell. This is the strongest durable conclusion of the transversal-equality era: repeated equality does not merely stall; it rigidifies enough that a positive-excess or folded-anchor configuration must appear.



## P4 plus trimer amplification and the endpoint-preserving fence

R126 proves the basic constructive statement: a disjoint tight P4 and tight trimer force a tight P5. The proof is a finite splice analysis and remains valid.

The stronger historical hope was **endpoint-preserving** amplification. R132 and R136 asserted variants saying the P5 could be chosen with prescribed endpoint behavior. Their archived proofs treated a complement/end set as non-Hamiltonian without justification. Accepted countermodel R139 shows the stronger local assertion is false: there is a valid Strong local cell with the required P4 and trimer but with the prescribed endpoint support blocked. Hence R132/R136 are not operational theorems even where stale metadata still marks their statements usable. R138 is the correct repair: one of a specified family of six support choices does yield the needed P5, which is enough for the replacement program but does not preserve the originally demanded endpoint set.

This genealogy matters downstream. Whenever a proof needs only existence of some amplified P5, R138/R126 are available. Whenever it needs a particular endpoint set, R139 is a warning that the requirement must be separately proved.



## Type-(2,2,3) replacement geometry and tested-order parity failure

R140 gives the shared-trimer endpoint-replacement lemma for the `(2,2,3)` type. R143 shows that private rotations of the resulting support system force an exterior-dimer signed interaction. R144 reduces the general `(2,2,3)` branch either to the `(2,2,2)` core or directly to such an exterior-dimer collision.

The historical R145 attempted to close the `(2,2,2)` case by multiplying sign relations around a spoke triangle and deriving an odd sign defect. That proof is invalid. Its parity multiplication compares repeated physical dimers without first fixing the tested orientation used by each certificate. Later four-cell work makes the obstruction explicit: reversing the tested order changes which head/tail label is being compared. The physical trimers and individual signed certificates survive; the global parity conclusion does not.



## Exact pair extension, countermodels, and common-shadow tail

R146 is the useful finite replacement theorem at the end of this chain. With a fixed tight trimer and two additional vertices, the relevant three-exterior pair-extension alternative is exact. Its authoritative proof is the SAT certificate P602: 60 Boolean variables, 361 clauses, with a deterministic DPLL verification (1397 nodes, depth 22). The exact proof is the SAT certificate P602. This section does not reconstruct that certificate in prose; P602 must be expanded for the full verification. What the certificate proves is the exact local implication used by the replacement fan, not a broader endpoint-preserving statement.

R148 is the complementary negative result: three prescribed-middle trimers do **not** force a core P4. Its explicit four-vertex local countermodel is therefore a genuine boundary of the method, not a failed proof to discard.

R149 then supplies the distinguished-trimer current-or-cross alternative. R150 records the endpoint/incidence role trichotomy for a current trimer. R151 and R152 are archival finite root/fan packets from the same program; their exact audits are retained by their source proofs, but they have no stronger independent interface than the replacement/fan geometry above. R153 closes the era with the universal two-orientation physical-dimer common-shadow lemma: pair deletion leaves a graph-intrinsic shared shadow independent of which tested orientation later becomes useful.



## What survives and what does not

The durable chain is:

`minimum-overlap deletion -> equality/positive-excess split -> common-marker four-family fan -> universal four-witness shield -> P4+trimer amplification -> type-(2,2,3) replacement -> exact pair-extension`.

Two stronger shortcuts are explicitly unavailable:

1. **Endpoint-preserving P4+trimer completion** (R132/R136) is contradicted by R139. Use R138/R126 instead.
2. **Unaligned spoke-parity multiplication** (R145) is invalid. Retain the individual signed turns, but compare polarities only after the tested dimer order is fixed.

