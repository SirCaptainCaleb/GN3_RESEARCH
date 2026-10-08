# Geodesic-support labels are automatically one-bit-Lipschitz on legal covers, but antipodally even

# Exact Kuhn/Fan neighborhood condition already holds on legal geodesic-extension edges

Consider the full (or one-switch admissible) directed path-state graph of cube geodesics, where an arc P->P' prepends or appends ONE previously unused coordinate i and retains an ACTUAL geodesic, as in the NORI exact two-ended automaton. Give each state the bit-string support label
lambda(P)=1_(S(P)) in {0,1}^n, where S(P) is the set of directions traversed by P.

**Theorem 1 (path-consistent cubical 1-Lipschitz property).** Along EVERY legal cover edge P->P', one has
d_H(lambda(P),lambda(P'))=1.
This is independent of the edge or three-face coloring, and remains true on the finite-memory quotient since endpoints determine S. Moreover under the correct NORI involution Theta(P)=(bar v_k,...,bar v_0), one has
lambda(Theta(P))=lambda(P),
NOT complement(lambda(P)).
Thus the required neighborhood part of the published cubical Sperner theorem is AUTOMATIC on the honest geodesic transition graph, while its antipodal boundary/face condition is NOT.

Proof. By definition each cover appends or prepends a new coordinate i not in S(P); hence S(P')=S(P) union {i}, so labels differ at precisely i. Complementing and reversing a path does not change its used direction set, giving Theta equality.

**Theorem 2 (full cubical chart cannot be assumed from the transition DAG).** If the admissible path-state complex contains a completely filled n-dimensional cubical grid cell/chart whose every Boolean support corner and all monotone directional transitions lift to a SINGLE same-root path witness, then it already contains a full rank-n geodesic and the desired conjecture conclusion follows. Hence using the entire full uncolored support grid as if all its cells were color-admissible is circular; the local 1-bit property holds only on existing legal arcs, not on missing edges of a hypothetical cubical tessellation.

**Proof.** In the common-root chart, the 1^n corner represents S=[n], and its path witness is a full directed antipodal geodesic, monochromatic in the edge proving ground or <=1 ordered-three-face change in NORI depending on the allowed transition automaton. Therefore construction of such a chart is at least as hard as the desired existence theorem. Conversely an abstract all-support cubical chart forgetting the path witnesses has no sound extraction.

**Research guidance.** The two real cubical Sperner obligations are:
(A) a suitable disk/box domain of PATH-CERTIFIED states, perhaps with fractional/interpolated repairs, whose cells have coherent physical geodesic lifts; and
(B) opposite-face boundary labels with lambda_i=0/1, or an alternative relative antipodal condition, despite ordinary Theta fixing rather than complementing S.
This refines the earlier assessment: Hamming-one regularity is free on legal covers, so focus on topology and boundary carriers instead of trying to prove local metric smoothness. This observation does not solve NORI.
