# Appendix — Known obstructions

**Status correction (October 10, 2026).** The original unrestricted NORI3 one-switch conjecture **has been refuted**: a legal physical `Q9` obstruction persists in larger dimensions, and the Devine–Milans `(3,3)`-tournament lift yields monochromatic paths of length at most `O(log n)` and `S_3(n)=Omega(n/log n)` compulsory switches. Thus a universal `Omega(sqrt n)` monochromatic-path lower bound is also refuted. All fixed `k>=3` admit unbounded compulsory switches, whereas NORI1 and unrestricted NORI2 remain open. The older mechanism-specific obstructions below remain valid within their stated scopes but should not be interpreted as supporting a proof of the refuted conjecture. Proofs and finite certificates appear in their Subsections; historical identifiers resolve through the legacy-reference lookup.

**Current structural barriers.** The logarithmic Devine–Milans `(3,3)`-tournament fails boundary same-triple reversal oddness on **every** unordered triple: of the three reversal pairs, one is `(0,0)`, one `(1,1)`, and one has opposite bits. Any direction-only boundary tournament differs in at least two of six ordered values per triple; thus no global edge order realizes it. The tournament lower-bound proof relies on exactly three accepted orderings of each triple, which an arbitrary physical NORI3 fiber need not have. Even an appropriately balanced fiber need not stay consistent along a cube path as the root's exterior bits change. See the revised Subsection *Logarithmic monochromatic NORI3 paths from a self-dual (3,3)-tournament*.



## Prescribed roots and unsupported support lifting

**A prescribed root need not support any full good geodesic.** In dimensions \(n\geq 6\) the exterior-weight parity construction (with the central reversal-odd correction in odd \(n\)) is legal and forces multiple color changes for every full order from a chosen root. Root motion remains permissible and necessary; see *Sharp rooted obstructions to one-change antipodal geodesics*.

**No dimension-independent positive density or sublinear root-localization bound.** For even \(n\ge6\), the legal exterior-parity coloring has good roots *exactly* at Hamming weights \(n/2-\rho_n,\ldots,n/2+\rho_n\), with \(\rho_n=1\) if \(6\mid n\) and \(\rho_n=2\) otherwise. Their density is \(\Theta(n^{-1/2})\), and the nearest good root to \(0^n\) is at distance \(n/2-\rho_n\). Thus neither a uniform positive fraction of successful roots nor a universal \(o(n)\)-radius search around a prescribed root can be assumed. See the exact thin-shell theorem in *Sharp rooted obstructions to one-change antipodal geodesics*.

**Good paths on every proper support do not imply a full good path at that root.** A verified legal \(Q_7\) coloring has an ordering with at most one switch on *every* proper support of size 3–6, yet every full seven-order from the same root has at least two switches. The full 1680-bit face-color certificate and exhaustive verifier are retained in *Maximal geodesic blockers and snake exchanges*. A more general exterior-weight construction gives all-dimensional short-path coverage without rooted full closure. These refute **coverage-only rooted implications**, not same-root *complementary reversed-terminal* intersections with their correct ordered memory, nor an unrooted conclusion.

## Exterior-bit consistency and restricted positional claims

**Naively embedding the six-path forcing certificate is unsound.** Each added exterior coordinate must meet actual equality and complemented-face constraints. A signed cycle with an odd number of complementation edges yields \(z=z\oplus1\), so the six-row pattern can have no consistent higher-dimensional physical realization. The \(Q_6\) theorem and six-path implication proof remain correct. An entirely new globally compatible forcing network or a different inductive invariant remains possible. See *Exterior-bit holonomy and the six-path extension obstruction*.

**Prescribing a sentinel slot is too strong even when a restricted family closes.** Legal face-dependent \(Q_7\) colorings can forbid every full good path with a designated direction third or fifth (exact finite coloring/certificate; historical ID \(nori_q7_fixed_sentinel_third_and_fifth_slot_2sat_counterexample_20261009\)). This does **not** refute ordinary \(Q_7\) closure with a free order. Positive one-sentinel \(Q_7\) and \(Q_8\) computer-assisted results retain their explicitly restricted exterior-dependence hypotheses; see *Seven-coordinate wing factorization and exact obstruction* and *Exterior face charts and Fourier transport*.

## Physical witness geometry versus abstract carriers

**Formal equal-support diagonals need not be actual path transitions.** The physical window-shift graph contains squares whose abstract diagonals do not correspond to any four-edge ordered-window shift. Topological or parity arguments using them as actual incidence require correction. The proven optimal physical transport and connector counts survive; extracting one full compatible path remains open. See the Article IV window-transport Subsections.

**Index in an ambient uncolored carrier is insufficient.** Actual good-path cells require joint witnessing, not pairwise label compatibility. For contiguous extension-flag models, the established equivariant collapse to the window-level graph limits the index information such a model retains. This does not rule out a different, more informative jointly witnessed carrier. See the Article II topological-carrier Subsections.

## Exchange and representation limitations

**Every adjacent exchange is local, but need not improve a defect.** A swap changes at most four consecutive physical windows; local caps and opposite-color extremal walls can coexist with insertion/swap obstructions. A strict globally terminating potential remains unproved. See *Maximal geodesic blockers and snake exchanges* and Article V.

**Edge-coloring results do not automatically transfer.** A path's physical edge-color word does not determine the ordered colors of its overlapping three-faces. Affine and central-Johnson edge theorems remain valid for the edge problem, but a NORI transfer must preserve actual exterior bits, terminal order and seam colors. See Article VIII.

These entries are curated by *mechanism*, not by the history of unsuccessful searches. A new exact proof may supersede an entry; its mathematical statement and surviving scope should then be revised.
