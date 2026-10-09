# Root-profile carrier is an equivariant suspension of its mixed complementary-branch interface

# Mixed-profile interface: an exact suspension reduction for reversed-tail NORI

Sources: nori_reversed_tail_root_profile_nerve_tucker_label_reduction_20261008; nori_exact_color_free_reversed_two_tail_complement_reachability_grand_equivalence_20261008. This is a structural theorem and a conditional forcing criterion.

## Definitions
For an ordered pair J=(a,b), let D_J=[n]\{a,b}. The alphabet Omega consists of (J,U) with empty != U proper subset D_J, and tau(J,U)=(rev J,D_J\U). A root profile L_x records either-color monochromatic branch witnesses from x ending with J. Write
 A = union_x Delta(L_x),
 K = A union tau A,
 C = A intersect tau A.
These are finite ABSTRACT simplicial complexes with the same label vertices; intersections are literal simplicial intersections.

Let S be the set of all singleton-support labels (J,{i}). Every root admits every such label, since a three-edge path has one ordered-three-face window. Thus S subset L_x for EVERY x.

## 1. Both halves are contractible
Adjoining any chosen s in S to any face of A stays within the same profile simplex Delta(L_x). Hence A is a cone with apex s, and indeed
 A = Delta(S) * B,
where B is the induced subcomplex of A on non-singleton labels (including the empty face in the join convention). The reflected half tau A is also a cone.

This is stronger than separate contractibility of the physical terminal-basins: the ENTIRE union of positive root-profile simplices is a cone. Its high topology is supplied by its overlap with its reflected half.

## 2. Exact description and extraction of the interface
 C = union_(x,y) Delta(L_x intersect tau L_y).
The involution maps the (x,y) intersection simplex to the (y,x) intersection simplex.

For a vertex u=(J,U) of C there are actual roots x,y such that u in L_x and tau u in L_y. Thus it certifies complementary reversed-tail branches at POSSIBLY DIFFERENT roots.

Grand closure holds iff |C| has a tau-fixed point. In fact it holds iff C has an edge {u,tau u}. To prove the converse, a face of C lies in one L_x intersect tau L_y. If it contains u and tau u, BOTH labels lie in L_x, yielding the exact same-root splice. To prove the forward direction, an opposite pair in L_x lies both in A and tau A, hence gives such an edge in C.

Thus the cross-root interface has an exact fixed-point extraction into a same-root witness. Separate availability at x,y is insufficient by itself; a tau-invariant simplex forces the needed single root.

## 3. Ordinary and equivariant suspension reduction
If C is nonempty, K is homotopy equivalent to the unreduced suspension Sigma C. The equivalence can be made tau-equivariant, where tau on the suspension sends (c,t) to (tau c,-t) and exchanges its two poles.

Proof. Replace the union A union_C tau A by its double mapping cylinder P:
 A <- C -> tau A,
with C times [-1,1] joining the two copies. The inclusions are finite simplicial cofibrations; collapsing the cylinder onto C gives P -> K a homotopy equivalence. Contracting the two disjoint contractible end subcomplexes A and tau A to two poles gives P -> Sigma C another homotopy equivalence. Choose the two contractions as involutive images of one another. Homotopy extension for the paired subcomplexes makes the construction equivariant. On fixed-point sets the mapping-cylinder comparison is the identity on C^tau (at t=0), and collapsing the exchanged ends changes no fixed points. This also verifies the equivariant comparison.

In particular, for nonempty C,
 reduced H_i(K;F2) = reduced H_(i-1)(C;F2) for i>=1,
 K is connected,
 chi(K)=2-chi(C).
If C is empty, K consists of two disjoint contractible halves exchanged by tau and equivariantly retracts to S^0.

This moves the topology question into a smaller, explicit interface rather than requiring separate topological analyses of all root-profile facets.

## 4. Support restrictions under hypothetical failure
Suppose grand closure fails, and n>=5. Every root profile omits all co-singleton labels (J,D_J\{i}). Indeed the corresponding branch has n-1 edges and extends by its remaining coordinate to a full path with at most one switch. Equivalently its complementary reversed-tail singleton is always in the same root profile, so the exact splice already gives closure.

Consequently every positive profile label has
 1 <= |U| <= n-4.
For labels in tau A, the reflected bound is |U|>=2. Therefore every interface vertex satisfies
 2 <= |U| <= n-4.
C is then free under tau. The universal singleton simplex S occurs only in A, and tau S only in tau A.

All but one vertex of S, together with their reflected partners, can be deleted by paired strong folds: every face containing a singleton can be enlarged by the retained singleton inside the same L_x. This preserves the carrier equivariantly and removes the redundant universal apices. It leaves two cone poles and the longer-branch data.

At n=5, the displayed interval is empty. Under failure K retracts to S^0; the universal centered-five-window pentagon supplies a monochromatic four-edge branch, which is already n-1 edges, contradicting failure. This recovers the established Q5 closure in these terms; it is a consistency check on the interface reduction.

## 5. Closure criterion and next mathematical target
If C is nonempty and reduced-H_*(C;F2)=0, then chi(C)=1 and chi(K)=1. A free involution on a finite complex pairs every simplex and has even Euler characteristic. Thus acyclicity of C implies grand closure. More generally odd chi(C) suffices.

The outstanding statement is a forcing property of the ACTUAL mixed-profile interface imposed by the shared physical-face coloring. We have not proved universal acyclicity or odd Euler characteristic of C. The independent singleton-profile model has C empty, so longer-window relations must supply the information. The known disjoint fixed-pair terminal basins do not settle this all-root interface.

The suspension description also permits recursive index arguments: an equivariant sphere mapping into C suspends to an equivariant sphere of one higher dimension mapping into K. Producing such a map still requires actual carrier compatibility. No continuous convex-label balancing is used in the construction or its extraction.
