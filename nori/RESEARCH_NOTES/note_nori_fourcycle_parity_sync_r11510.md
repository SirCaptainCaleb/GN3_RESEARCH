# Four-pair reader-cycle synchronization and parity-guard red-face forcing

- Stable ID: note_nori_fourcycle_parity_sync_r11510
- Author: unspecified; session provenance retained
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, paired-flat, Q8, root-order-compatibility, parity-fibers, constructive-forcing, cyclic-reader, joint-obstructions, red-face, proof
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11510_3
- Updated session: session_nori_r11510_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_rank_four_pointwise_sensitivity_cycle_r11510

## Research note

# Four-cycle parity synchronization and three-pair forcing

**Theorem.** Let c be any legal antipodally odd paired-flat coloring of Q8. Suppose (i) no four-face retaining two entire direction pairs has a monochromatic full geodesic, and (ii) in every pair-parity fiber, the induced four self-dual Boolean gates are signed unary readers whose reader graph is one directed four-cycle. Then c has an all-red full antipodal geodesic. Indeed, either a full red three-pair face exists, or c is equivalent by cube automorphisms to a signed four-cycle reader.

**Synchronization proof.** Write p_i=x_(a_i)+x_(b_i), q_i=x_(a_i). For each p write h_i^p(q)=q_(sigma_p(i))+alpha_i(p). Gate f_i ignores its own direction pair, so sigma_(p+e_i)(i)=sigma_p(i)=j. Gate i is sensitive to pair j on every face with the other two pair values prescribed at parity p. By (i) and the rank-two identity R=2E(a)E(b), gate j must be constant on pair i throughout those faces. Hence h_j^(p+e_i)=h_j^p, and sigma_(p+e_i)(j)=sigma_p(j). The two four-cycles sigma_p and sigma_(p+e_i) have the same consecutive arrows i->j->sigma_p(j), which determine the entire cycle on four vertices. Thus sigma_p is constant over p. Relabel to sigma(i)=i+1 mod4. Since gate i ignores pair i, and gate i-1 reads pair i on every face, the four-face failure also forces gate i to ignore pair i-1. Hence there exist arbitrary Boolean two-bit functions phi_i such that
 f_i(q,p)=q_(i+1)+phi_i(p_(i+1),p_(i+2)).                  (FC1)

**Parity guard gives a red three-pair path.** If phi_i varies with p_(i+2) for some fixed p_(i+1)=t, freeze pair i+1 at parity t and retain A=i,B=i+2,C=i+3. On this ordinary six-face f_A=epsilon+p_B, while f_B=q_C+phi_B(p_C,p_A), f_C=q_A+phi_C(p_A,p_B). Since f_A is nonconstant in B, failure of the two-pair A,B face forces f_B independent of A. Thus f_B is a signed reader of one bit in pair C. Since f_B is nonconstant in C, failure of the B,C face forces f_C independent of B, making it a signed reader of one bit in A. Swap labels inside A,C as needed and absorb phases, obtaining
 f_A=epsilon+p_B, f_B=x_(a_C)+eta, f_C=x_(a_A)+theta.
Choose the starting root so f_A=1 and f_C=0. The pair-word (A,B,C,A,B,C) then traverses all six directions once, all red. Indeed first A takes b_A, first B toggles parity p_B enabling the complementary A direction; first C takes a_C and changes the reader input of B; second A takes a_A and changes the reader input of C; the subsequent B,C visits take their other directions. The existing paired-endpoint insertion lemma places both members of omitted pair i+1 around the red six-step geodesic, yielding a full red Q8 geodesic.

**No guards gives a signed cyclic reader.** If each phi_i ignores its second argument, phi_i=beta_i+lambda_i p_(i+1). Therefore f_i=q_(i+1)+lambda_i p_(i+1)+beta_i is a signed reader of one bit of pair i+1. Pair-member swaps and vertex translations normalize to f_i=q_(i+1). From the root q_0=1 with every other bit zero, the direction order (b_3,a_0,a_1,a_2,a_3,b_0,b_2,b_1) is red and visits every direction once. Undoing the automorphisms supplies a full red geodesic in c. QED.

**Audit.** In normal form (FC1), each phi_i has sixteen truth tables. Absence of successful two-pair faces forbids dependence on opposite pair parity in both directions of either opposite gate pair (0,2) and (1,3). Each opposite gate pair allows 4*16+16*4-4*4=112 table combinations. Thus 112^2=12544 systems meet (i) in this normal form. Of them 256 have no opposite-parity dependency; the other 12288 have the constructed six-step red face. The separate verifier nori_fourcycle_sync_verifier.py checked all 12544 and explicitly reconstructed the required red routes. Detailed written proof: nori_fourcycle_sync.md.

**Scope.** This positive forcing theorem concerns all legal paired-flat Q8 colorings with the indicated unary four-cycle fiber structure. It leaves majority-type and three-reader-plus-one-extra-gate fiber types unresolved, and does not establish unrestricted NORI1.
