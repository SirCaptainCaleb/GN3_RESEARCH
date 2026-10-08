# Exact reversed-tail root-profile nerve: equivariant symmetrization, Tucker extraction, and maximal-profile label reduction

# Root-profile nerve for exact reversed-tail NORI: a Tucker-compatible label reduction

## Scope and inputs
This is a proved reformulation and label-space reduction for the ACTIVE ordered-three-face problem, not a proof of the grand conjecture. It uses the exact splice theorem nori_exact_color_free_reversed_two_tail_complement_reachability_grand_equivalence_20261008 and the classical Tucker/Borsuk–Ulam statements in literature_fixed_point_theorems. No new web or literature search was used.

Let n>=4. For J=(a,b), put D_J=[n]\{a,b}. Let R_J(x) be the either-color monochromatic terminal-memory support family of the exact splice theorem. Only nonempty PROPER U subset D_J are retained, since both branches must have a nonempty support.

Define the formal label alphabet
Omega={(J,U): J an ordered pair, empty != U proper subset D_J}
with FREE involution
tau(J,U)=(rev J,D_J\U).
Define the root profile
L_x={(J,U) in Omega: U in R_J(x)}.
Then grand closure holds iff L_x contains a tau-pair for some x. This statement retains the terminal order and has no additional seam-color condition.

Every L_x is nonempty: every singleton U yields a path of exactly three edges, hence one three-face window, for every admissible J. There are |Omega|=n(n-1)(2^(n-2)-2) labels and M=binom(n,2)(2^(n-2)-2) formal antipodal pairs.

## Theorem 1: an exact equivariant carrier without assuming physical support-complement symmetry
Let
K= union_x [Delta(L_x) union Delta(tau L_x)],
a simplicial complex on Omega. Then tau acts simplicially on K, and the following are equivalent:
(a) grand closure;
(b) K contains an edge {u,tau u};
(c) |K| has a tau-fixed point.

Proof. The splice equivalence gives (a) iff a profile L_x contains a tau-pair. Every face of K lies in L_x or tau L_x. Thus a tau-pair in K yields one in L_x after applying tau if needed, proving (a)<=> (b). An opposite edge has fixed midpoint. Conversely the unique minimal simplex supporting a fixed point is invariant under tau; since tau has no fixed vertex, it contains a tau-pair. QED.

The added reflected simplices are FORMAL carriers. We do not claim tau L_x is an actual profile at a physical antipodal root. Extraction is sound because an opposite pair inside a reflected profile reflects back to an opposite pair inside the original SAME-root profile. This avoids requiring the unsupported identity between physical antipodality and support complementation.

## Theorem 2: root-profile nerve and exponential factor reduction
Index the generating simplices by (x,+) and (x,-), and put S_(x,+)=L_x, S_(x,-)=tau L_x. Define the nerve N on these signed roots by
I in N iff intersection_(i in I) S_i != empty.
Its involution sends (x,+) to (x,-).

Then K and N are equivariantly homotopy equivalent. More directly, grand closure holds iff N has an opposite edge {(x,+),(x,-)}, equivalently iff |N| has a fixed point.

The direct extraction proof is
L_x intersect tau L_x != empty
iff there exists u with both u and tau u in L_x.
Thus an opposite root pair in this nerve is exactly the desired same-root complementary-tail witness, not merely a convex intersection.

For completeness, the equivariant nerve equivalence needs no unverified external theorem. On nonempty face posets define
F(sigma)={i: sigma subset S_i},
G(I)=intersection_(i in I) S_i.
Both maps reverse inclusion, commute with the involutions, and induce simplicial maps of the order complexes (barycentric subdivisions). Their composites satisfy sigma subset G(F(sigma)) and I subset F(G(I)). The standard prism homotopy for pointwise comparable order-preserving maps gives homotopies of both composites to the identity; these homotopies commute with the involutions because the inclusions do. Thus the equivalence is equivariant.

N uses at most 2^n SIGNED MAGNITUDES (2^(n+1) signed vertices), compared with M=binom(n,2)(2^(n-2)-2) magnitudes for the direct tail/support alphabet. For n>=5 this is already smaller; asymptotically the reduction factor is n(n-1)/8. This removes the ordered-tail factor, not the remaining exponential dependence on n. No polynomial-size bound follows.

## Theorem 3: retain only maximal root profiles
Choose one actual root representative for every distinct inclusion-maximal L_x. Let p be the number retained, so p<=2^n. Every profile is contained in a retained profile. Consequently deleting the nonmaximal generating simplices leaves K EXACTLY unchanged. The nerve of the retained signed cover is still equivariantly homotopy equivalent to K and has p signed magnitudes.

In the full nerve this deletion can also be performed by paired strong folds. If L_x subset L_y and x!=y, every nerve face containing (x,+) can be enlarged by (y,+): any label witnessing the original intersection lies in L_x and hence L_y. The same holds for the two negative vertices. Mapping x+ to y+ and x- to y- is an equivariant retraction; every face together with its image remains a face, so affine contiguity gives an equivariant strong deformation retraction. Repeat toward selected maximal representatives.

Unlike the earlier edge-reachability graph reduction, this proof needs no symmetry of a directed reachability relation. It applies directly to the full ordered-three-face terminal-memory profiles.

## Exact applicability of the fixed-point toolkit
1. CLASSICAL TUCKER (C1): with p retained profiles, it suffices to build a triangulated p-ball and label vertices by signed retained roots, odd on the boundary, such that every domain edge maps to a nerve edge or a single vertex. Explicitly, for each edge vw, S_label(v) intersect S_label(w) must be nonempty. Tucker supplies labels +x and -x on an edge; their intersection gives the exact reversed-tail splice. No whole-simplex carrier condition is needed for this Tucker criterion.

2. BORSUK–ULAM (A2): if an equivariant continuous map S^p -> |N| can be established, closure follows. Indeed failure of closure makes N an invariant subcomplex of the boundary of the p-crosspolytope, yielding a forbidden equivariant map S^p -> S^(p-1). Equivalently work on K through the proved equivariant homotopy equivalence. The needed high-index map has NOT been constructed.

3. EULER / ACYCLIC SUFFICIENT CONDITIONS: odd Euler characteristic of N forces a fixed simplex, hence closure, because a fixed-point-free involution pairs all nonempty simplices dimension by dimension. In particular F_2-acyclicity suffices. Neither odd Euler characteristic nor acyclicity is claimed universally.

4. KKM: any use on this carrier must prove literal set intersections or a valid simplicial carrier. Replacing actual labels by their bit-vector convex hulls is insufficient; the earlier genuine doubled-Fano edge-reachability example already disproves that general relaxation. It is not a counterexample to the active three-face conjecture.

5. CUBICAL TUCKER / BINARY SPERNER / HEX: neutrality, one-bit legality on existing extensions, and connectedness remain weaker than the required witness without their extra carrier/extraction hypotheses. The signed-root nerve gives an exact opposite-pair target, making classical Tucker the cleanest currently rigorous fit. The partially verified multilabeled Hex entry D5 was not used.

## A precise limitation: singleton availability alone has zero topological force
For an abstract profile system, take every L_x to consist exactly of all labels (J,{i}), for all admissible J and i. For n>=5, |D_J|>=3, so singleton supports and their (|D_J|-1)-element complements are disjoint. K is then the disjoint union of two simplices exchanged by tau, and N likewise consists of the all-positive root simplex and the all-negative root simplex. It equivariantly retracts to S^0, has Euler characteristic 2, and has no opposite edge.

This is NOT asserted realizable by a NORI coloring. It proves only that the automatic one-window reachability data cannot itself provide the missing Tucker carrier or index bound. Any successful argument must exploit additional relations among longer reachable supports imposed by one common coloring.

## Research consequence
The fixed-point toolkit is applicable through an exact, color-free, equivariant root-profile nerve. Formal symmetrization repairs the support-involution mismatch at the carrier level; the nerve removes the tail/support multiplicity; maximal profiles give a further safe reduction. The remaining mathematical task is to prove a topological forcing property of this actual nerve (or construct a smaller admissible Tucker carrier) using the constraints tying the root profiles together. None of the constructions above alone proves grand closure.
