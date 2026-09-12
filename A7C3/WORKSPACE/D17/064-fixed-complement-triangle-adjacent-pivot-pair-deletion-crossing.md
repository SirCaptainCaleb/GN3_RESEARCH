# An adjacent active-pivot pair forces a universal direct crossing on the two-hole residue

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-triangle-adjacent-pivot-pair-deletion-crossing`

**Summary:** In the same-support branch of the anchored two-transfer absorber, fix p=y_i, A=R_i=Omega-y_i, B=Q[2,t], and D={q0,q1}. The branch gives a Hamilton absorber on D+A, while the original Q is a Hamilton absorber on D+B. Moreover A+p=Omega is non-Hamiltonian, B+p is non-Hamiltonian by the double-prefix push, and A+B is non-Hamiltonian because the transferred-label turn (q0,q1,p) is tight, so a Hamilton A+B path would pair with that trimer to two-cover H. For any exact two-cover T of H-D, accepted R508 applied with absorber D+A forces an A|(B+p) selected crossing, and applied again to the same T with absorber D+B forces a B|(A+p) crossing. If T had no direct A-B selected edge, both forced crossings would pass through p. Since p then has selected degree two and no other interclass transition is possible, the maximal-block quotient has b_A+b_B=3; one of A,B is one whole T-block adjacent to p, Hamiltonizing A+p or B+p, contradiction. Hence every exact H-D cover selects a direct A-B edge. The three class pair-unions A+B,A+p,B+p are all non-Hamiltonian but exactly two-coverable, and p cannot be isolated, so every exact H-D cover has connected interaction on {A,B,{p}}. The pure block-word proof of R942 therefore yields a rainbow hinge or split-star weave for every representative, with singleton p forbidden as the split center and the direct A-B state retained. Thus a wrap-blocked same-support reversal is already a universal pair-deletion crossing object, not an endpoint-only dead end.

### 1. Same-support adjacent-pivot coordinates
Retain the same-support branch of `fixed-complement-triangle-double-transfer-reversal-absorber` SV21962. Fix the corresponding transfer index i and put

  p=y_i,
  A=R_i=(y_{i+2},y_{i+1},M),
  B=Q^{(2)}=(q_2,q_3,...,q_t),
  D={q_0,q_1}.

The same-support branch gives a literal Hamilton path

  P_A=(q_0,q_1,A)                                      (AP.1)

on D union A. The original complementary rail

  Q=(q_0,q_1,q_2,...,q_t)                              (AP.2)

is a literal Hamilton path on D union B.

The transferred label p also satisfies

  (q_0,q_1,p) tight                                    (AP.3)

by SV21962.

Three pair-unions in the residue W=H-D are non-Hamiltonian:

  A+p = Omega                                           (AP.4)

is the original critical block and is non-Hamiltonian;

  B+p                                                   (AP.5)

is non-Hamiltonian by `fixed-complement-triangle-transfer-double-prefix-push` SV21176; and

  A+B                                                   (AP.6)

is non-Hamiltonian because a Hamilton path on A+B together with the tight trimer (q_0,q_1,p) from (AP.3) would be a spanning two-cover of H.

Each of the three pair-unions is nevertheless covered by its two displayed Hamilton atoms, so each has path-cover number exactly two.

### 2. Two absorbers act on the same arbitrary two-hole cover
Because D is a proper tight dimer, accepted R4 gives exact path-cover number two on

  W=H-D=A disjoint_union B disjoint_union {p}.

Let T be an arbitrary literal exact two-cover of W.

Apply accepted R508 with deletion set D, absorbable block S=A, and absorber P_A from (AP.1), whose support is exactly D union A. Its reconstructed proof forces T to select an adjacency crossing

  A | (B+p).                                            (AP.7)

Apply R508 again to the SAME T with S=B and absorber Q from (AP.2), whose support is exactly D union B. This forces a selected adjacency crossing

  B | (A+p).                                            (AP.8)

Thus every exact W-cover carries both crossing obligations simultaneously.

### 3. The two obligations force a direct A-B selected state
Suppose, toward contradiction, that T selects no A-B adjacency. Then (AP.7) can only be realized by an A-p selected adjacency, while (AP.8) can only be realized by a B-p selected adjacency.

The singleton p therefore has selected degree two in the two-path forest T, with one neighbor in A and one in B. It is internal on one T-rail. Since an ordinary path vertex has selected degree at most two and A-B states are absent, these are the only interclass selected adjacencies in T.

Split the two T-rails into maximal A-blocks, maximal B-blocks, and the singleton p. Let b_A,b_B be the numbers of A- and B-blocks. Contracting the maximal blocks gives a forest with exactly two connected components, because T has exactly two rails. It has

  b_A+b_B+1

vertices and exactly two interclass edges, namely A-p and p-B. Therefore

  2=(b_A+b_B+1)-2,

so

  b_A+b_B=3.                                            (AP.9)

Hence one of A or B occurs as exactly one maximal T-block. That whole block is adjacent to p in T. The block together with p is therefore a contiguous tight T-subpath spanning A+p or B+p, respectively. This Hamiltonizes one of the two non-Hamiltonian supports (AP.4)-(AP.5), contradiction.

Consequently every literal exact two-cover T of H-D selects a DIRECT physical adjacency

  A | B.                                                (AP.10)

This is universal over all exact representatives of the pair-deletion residue.

### 4. Connected three-class interaction and the R942 block-word normal form
The direct A-B state (AP.10) is present in every exact W-cover. The singleton p cannot be an isolated T-component: if it were, the other T-rail would be a Hamilton path on A+B, contradicting (AP.6). Therefore p has a selected adjacency to A or B, and the class-interaction graph on

  {A,B,{p}}

is connected for every exact T.

The hypotheses used in the block-word part of accepted R942 are now present intrinsically: three nonempty Hamilton atoms, all three pair-unions non-Hamiltonian with path-cover number two, and a connected two-rail interaction. Repeating that purely combinatorial proof, contract every maximal class block along the two T-rails. Exactly one of the following occurs.

**RAINBOW HINGE.** Some T-rail has three consecutive maximal blocks X-K-Y carrying all three distinct class labels. Retain both actual selected boundary states and the complete physical middle block K.

**SPLIT-STAR WEAVE.** No three consecutive blocks have three distinct labels. Then each T-rail alternates between exactly two class labels; the two rail-pairs are distinct and share one center class K, which is split nontrivially between the two rails. The singleton {p} cannot be this center, so K is A or B. Retain the actual split K=K_1 disjoint_union K_2, both literal T-rail words, and a consecutive state in the retained Hamilton source order on K crossing K_1|K_2. The universal direct A-B state (AP.10) remains current in the same T.

Thus the same-support adjacent-pivot branch is already a connected arbitrary-fragmentation object on one fixed pair-deletion residue.

### 5. Relation to the two wrap gates
The two-wrap-gate section SV22283 says that the same-support reversal either closes through R561 or is blocked at one of two transfer-index-independent physical turns near the terminal end of M. The present theorem is orthogonal to that rotation test: whenever the same-support branch exists at all, every exact H-{q_0,q_1} cover already has the universal direct A-B crossing (AP.10) and the rainbow-hinge/split-star normal form above.

Therefore a surviving wrap blocker is not an endpoint-only shield. It coexists with a current universal pair-deletion crossing between the active puncture rail A=R_i and the shortened complementary rail B=Q[2,t]. The next consumer should spend the named wrap blocker together with this connected three-class reconstruction, rather than export either one separately as generic signed or balanced-pair currency.

The terminal TTT case is the exact order dual.

### 6. Scope
This is a working deduction from the retained anchored-transfer geometry plus accepted R4 and R508. It does not close CBCA and does not assert that the rainbow hinge or split-star weave is itself absorbable. Its gain is the representative quantifier: the direct A-B selected state is forced in every exact two-cover of the same two-hole residue.
