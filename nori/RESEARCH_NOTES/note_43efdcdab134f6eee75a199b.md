# Independent affine-eight and rank-five twelve-label finite closure certificates

- Stable ID: note_43efdcdab134f6eee75a199b
- Author: unspecified; session provenance retained
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, rank-five, static-affine, parity-peeling, finite-certificate, projective-reduction
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11729_1
- Updated session: session_nori_r11729_1
- Disposition: none
- Successor: none

## Related references

- note:note_nori_rank4_fano_column_quartet_forcing_r11704
- note:note_28429d9005d311b5a8dfea67

## Research note

INDEPENDENT RANK-FIVE FINITE CERTIFICATES AND SIZE REDUCTION.

Setting: legal static affine paired-flat reader matrices A over F2 with zero diagonal and A*1=1. A peel i1,...,ik is legal when each row i_t has even entries toward prior deletions. It succeeds when the remaining principal submatrix is nonsingular. Prior team work proves all ranks <=4 and the necessary minimal-counterexample compression. In rank five, factor A_ij=(z_i+z_j) dot t_j, with row factors (1,z_i), column factors (epsilon_i,t_i), epsilon_i=z_i dot t_i, quotient points t_i in F2^4 nonzero. In a size-minimal counterexample there is at most one repeated quotient class, and any repeated class has opposite lift bits. Column sums are (1,0,0,0,0).

FULLY CHECKED FINITE LEMMA A: For the eight quotient points t=8,...,15, any row factors z_i in F2^4 admit a four-point affine plane whose lifted columns sum to zero and whose induced 4x4 matrix admits a complete legal peel. There is no restriction on the total eight-column sum. After global gauge normalization z_0=0, independent C++17 depth-first exhaustive enumeration visits 1,1,16,256,2176,34816,49152,0,0 nodes by depths 0,...,8, with no survivors. Source /mnt/data/nori_affine8_plane_exhaust.cpp.

FULLY CHECKED FINITE LEMMA B: If those eight lifted columns have even total sum, all eight labels admit a legal full peel. Direct C++17 enumeration checks all 134217728 gauge-normalized assignments with even lift sum. Complementary peelable plane pairs certify 134167552 instances. Independent 256-subset reachability checks certify the remaining 50176 instances. No failures. Source /mnt/data/nori_affine8_even_full_exhaust.cpp. For odd total lift sum, Lemma A deletes a zero-sum plane and the remaining four-label matrix has odd row sums; the previously proved four-label odd-matrix theorem finishes. Thus both previous affine-coset SMT statements now have independent exhaustive C++ certificates, not just UNSAT solver reports.

FULLY CHECKED FINITE LEMMA C: In the twelve-label rank-five quotient pattern with omitted basis classes {1,2,4,8} and duplicated class 15, every permitted eight-row subconfiguration indexed by labels {0,2,3,5,6,9,10,11} contains a peelable full-zero-sum quartet from the eleven candidate quartets enumerated in /mnt/data/nori_rank5_independent_finite_closure.md. The induced four-row even-row matrix fails full peeling precisely in 16 of its 256 patterns: three labels form a bidirected triangle and these triangle rows send no edges to the fourth label. The fourth row may have any even pattern; this was independently checked and a preliminary overly restrictive encoding was corrected. The eight-row verifier gauge-normalizes its first row factor and enforces opposite lifts for the two duplicated quotient columns. Search visit counts by depth 0,...,8 are 1,1,16,256,2176,2048,32768,15360,0; hence no counterexamples. Source /mnt/data/nori_rank5_local_quartet_exhaust.cpp.

THEOREM (rank-five minimal-counterexample size <=11). Assume the team's preceding rank<=4 closure and minimal-counterexample column compression. Rank-five matrices with >=13 labels are eliminated by affine-coset Lemmas A and B and the previously exhausted five-label block, following the previously published projective reductions. For 12 labels with a duplicated quotient class, Lemma C deletes a zero-sum quartet; the odd-row residual has smaller size and rank<=5, contradicting minimality. For 12 distinct quotient classes, the three missing quotient points form a projective line. Its two-space has three four-point nonzero cosets, which partition the twelve retained labels. Their lift parities sum to one. Choose an odd-parity coset inside one of the three hyperplanes containing the line. The remaining eight points outside that hyperplane form a complete affine coset with even column sum, removable by Lemma B; the four residual labels have odd row sums and are resolved by the rank<=4 theorem. Therefore any size-minimal rank-five counterexample must have between seven and eleven labels.

This theorem does not resolve the remaining 7–11-label cases, the unbounded-rank odd-matrix conjecture, or unrestricted NORI1. A direct seven-label SAT instance timed out and supplies no conclusion.

COMPLETE REPRODUCIBLE PROOF and verified standalone integer-only code: /mnt/data/nori_rank5_independent_finite_closure.md, /mnt/data/nori_rank5_local_quartet_exhaust.cpp, /mnt/data/nori_affine8_plane_exhaust.cpp, /mnt/data/nori_affine8_even_full_exhaust.cpp. A preliminary Python+Z3 check exists but plays no role in the finite proofs.
