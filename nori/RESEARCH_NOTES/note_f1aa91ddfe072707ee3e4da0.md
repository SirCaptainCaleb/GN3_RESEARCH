# Antipodal Boolean-chain windows and the permutohedral path-compatibility nerve

- Stable ID: note_f1aa91ddfe072707ee3e4da0
- Author: session_nori_r7442_2
- Primary home: article:nori_article_ix_unification
- Labels: Freudenthal, permutohedron, nerve, antipodal, topological-combinatorics
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7442_2
- Updated session: session_nori_r7442_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

**Theorem (Boolean-chain antipodality and Freudenthal placement).** Fix n>=4. A three-step cube window is a saturated chain W=(A;a,b,c), where a,b,c are distinct members of [n]\A:
A < A+a < A+{a,b} < A+{a,b,c}.
The involution induced by complementing cube vertices and reversing the chain is
T(W)=([n]\(A union {a,b,c});c,b,a).
The barycenter of its four vertices is
m(W)=1_A+(3/4)e_a+(1/2)e_b+(1/4)e_c.
It is on the boundary of the n-cube, and m(TW)=1-m(W), so T is geometric antipodality on this (n-1)-sphere. A reversal-odd boundary three-tournament b gives an odd labeling of these windows via chi_b(W)=b(a,b,c), independent of A. An antipodally odd NORI1 edge labeling c gives another odd window labeling by chi_c(W)=c(A+a,A+{a,b}), using the middle edge: its T-image is the antipodal middle edge. Along a complete chain with direction permutation pi, chi_b lists the original boundary triple bits b(pi_i,pi_{i+1},pi_{i+2}), whereas chi_c lists the NORI1 bits on the n-2 interior edges only. Thus the boundary Hamiltonian one-switch assertion is equivalent to the one-switch full-chain assertion for this root-independent window lift. The NORI1 full-edge conclusion does not follow from control of the middle windows without handling the first and last edges.

**Theorem (permutohedral path-compatibility nerve).** Let P_n be the (n-1)-permutohedron, with vertices indexed by pi in S_n. For a k-window W=(A;i_1,...,i_k), associate the face F_W of P_n indexed by the ordered partition
A | {i_1}|...|{i_k}| ([n]\(A union {i_1,...,i_k})),
omitting empty blocks. Its vertices are the full permutations whose Boolean chains contain W. The reversal involution on windows corresponds to central inversion of P_n. Form the nerve K_{n,k} of the indexed convex faces F_W. A family of windows spans a simplex of K_{n,k} iff all windows occur on one full permutation path: a nonempty intersection of faces of a polytope contains a polytope vertex. Every maximal simplex consists of the n-k+1 windows of one full permutation. The convex-set nerve theorem identifies the homotopy type of K_{n,k} with the union U_{n,k} of these permutohedral faces.

**Proposition (components of K_{n,3}).** For n=4,5,6 the numbers of connected components are respectively 24,30,20. For n>=7, K_{n,3} is connected. Proof: two full permutations lie in the same component precisely when joined by a chain of permutations where consecutive permutations share some three-window. At n=4, each window uniquely determines a full permutation (4! components). At n=5, sharing a window only permutes the first two or the final two positions, yielding 5!/(2!2!)=30 components. At n=6, sharing a window preserves the set of elements in the first three positions, and the first three and last three positions may independently be permuted, yielding binomial(6,3)=20 components. For n>=7, every adjacent transposition leaves untouched a consecutive triple of positions (take the first three if the transposed pair lies sufficiently far right, otherwise the last three). Thus permutations related by an adjacent transposition share a three-window; adjacent transpositions generate S_n, proving connectivity.

**Limits.** A barycentric subdivision simplex includes at most one barycenter of a three-dimensional Freudenthal simplex, so a neutral-simplex lemma on that subdivision does not by itself combine several three-window bit values. The permutohedral nerve is path-faithful, but its connectivity alone does not imply a bounded-switch full path. A topological selection theorem must also provide a path-decoding result. The base graph involution acts on cube vertices; its induced actions on windows and faces are derived, not independent. No ordinary color preservation is imposed.
