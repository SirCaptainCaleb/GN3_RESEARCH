# Rank-two sensitivity-product forcing and irreducible all-pair red circuits

- Stable ID: note_nori_pair_sensitivity_product_irreducible_cycles_r11510
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, paired-flat, constructive-forcing, sensitivity-product, four-face, simultaneous-influence, all-pair-circuit, reader-cycle, induction-limit
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11510_3
- Updated session: session_nori_r11510_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_two_pair_seam_forcing_r11510

## Research note

# Two-pair sensitivity-product forcing and irreducible all-pair circuits

**Proved.** Full proof at /mnt/data/nori_pair_sensitivity_circuit.md and checker at /mnt/data/nori_pair_circuit_activation.py. The first assertion is positive and constructive. The second explains the limit of induction from smaller paired faces. NORI1 remains open.

**THEOREM 1 (rank-two product identity).** On an ordinary, possibly non-antipodal-odd paired-flat Q4, split directions into A={a0,a1} and B={b0,b1}. Let edge colors be c_(a_i)(p,q)=a(q)+i and c_(b_j)(p,q)=b(p)+j, over F2, for arbitrary gates a,b:F2^2->F2. Denote by E(a), E(b) the numbers of undirected input-square edges where the respective gate changes. The number of rooted all-red full geodesics is
   R=2 E(a) E(b).
The number of rooted all-blue full geodesics obeys the same identity. In particular R>0 iff both gates are nonconstant, and then R>=8.

**Proof.** Two red consecutive edges cannot lie in the same direction pair, because traversing its chosen red direction leaves that pair gate unchanged and the other direction blue. Thus every red full path has pair word ABAB or BABA. For ABAB choose a sensitivity edge of a in B-input direction beta and a sensitivity edge of b in A-input direction gamma. Put alpha=1-gamma. On the first edge choose the endpoint q where a(q)=alpha, and on the second choose t where b(t)=beta. Set initial A-bit pair p=t+e_alpha. Then directions (a_alpha,b_beta,a_gamma,b_(1-beta)) from root (p,q) are all red: first gate values select alpha,beta, and the chosen sensitivities flip them to gamma,1-beta for the last two steps. Every red ABAB witness uniquely specifies those two input sensitivity edges, so there are E(a)E(b). Swapping A and B gives the same number for BABA. Complementing both gates preserves their edge-boundary sizes, proving the blue statement. QED.

**DIMENSION-UNIFORM FACE COUNT.** For any legal paired-flat Q_(2m), fix two paired groups A,B and freeze all remaining direction bits at y. Write a_y,b_y for the induced four-face gates. Then the total number of rooted red four-face geodesics, summed over all frozen y, is
  2 sum_y E(a_y) E(b_y).
This measures simultaneously active reciprocal influences using the SAME frozen assignment. Separate influence counts do not determine it.

**THEOREM 2 (globally essential cyclic-reader witness).** For every m>=2, define paired directions P_i={a_i,b_i}={2i,2i+1}, indices cyclic modulo m, with legal gates c_(a_i)(x)=x_(a_(i-1)), c_(b_i)(x)=1+x_(a_(i-1)). Every vertex has one red and one blue edge from each pair, and the group-influence graph is a directed m-cycle. This coloring has a full all-red antipodal geodesic but NO proper nonempty paired-direction face has a monochromatic full geodesic relative to that face.

**Proof.** From root x_(a0)=1, all other bits 0, traverse
  b1, a0, a_(m-1), a_(m-2), ..., a1, b0, b2, ..., b_(m-1).
The first b1 reads a0=1 and is red; a0 and the descending a_i read predecessors still zero and are red; a1 reads a0 after its flip to zero and is red; b0 and the remaining b_i read predecessors now one and are red. Each direction is used once and the endpoint is antipodal. For any proper nonempty subset S of paired groups, there is i in S with predecessor i-1 outside S. Throughout every face freezing all other groups, group i's gate is constant, so its two directions have opposite constant colors. A full spanning S-face geodesic uses both; hence no such path is monochromatic. QED.

**RESEARCH SCOPE.** The positive local mechanism is simultaneous reciprocal gate sensitivity. The reader-cycle example proves that even a successful coloring may have no monochromatic full geodesic in any proper pair-face, including all codimension-four faces tested by the preceding seam theorem. Thus a universal proof must also construct global irreducible all-pair witnesses. The example does not rule out counterexample-specific hereditary forcing.

**TESTS.** Independent complete-root/order checking of all 256 four-bit gate-pairs confirms R=2 E(a)E(b), with 196 positive cases and 60 constant-gate cases. The full reader-cycle construction and the proper-pair-subset criterion were checked for m=2,...,12, with dimension-uniform proofs above.
