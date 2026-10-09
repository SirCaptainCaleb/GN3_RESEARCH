# Exact odd-zero extraction on the root-probability interface; deleted-product dimension and homology forcing

# Root-probability interface: exact odd-zero extraction and a (p-2)-dimensional model

Inputs: nori_reversed_tail_root_profile_nerve_tucker_label_reduction_20261008; nori_reversed_tail_mixed_profile_interface_equivariant_suspension_20261008; literature_fixed_point_theorems.

Retain p actual root representatives r_1,...,r_p for the distinct inclusion-maximal profiles L_i=L_(r_i). Their generating simplices give the SAME positive carrier A as all roots. Put C=A intersect tau A.

## 1. A genuine product-cell carrier
Let Delta^(p-1) be the simplex of probability vectors on the RETAINED ROOT INDICES, with coordinates e_1,...,e_p. For nonempty I,J subset [p], allow the product cell
 Delta(I) times Delta(J)
precisely when
 Q_(I,J) = intersection_(i in I) L_i intersect intersection_(j in J) tau L_j
is nonempty. Let Z be the union of these allowed product cells, as a subcomplex of Delta times Delta. Faces remain allowed, because removing a root constraint enlarges Q.

A point (a,b) in Z comes with an ACTUAL common label u=(ordered tail,U): u is reachable at every positive-support root of a, and tau u is reachable at every positive-support root of b. Neither physical cube-bit convexification nor an averaging of unrelated label coordinates is used.

The involution exchanges the two probability vectors:
 tau_Z(a,b)=(b,a).
Indeed tau sends Q_(I,J) to Q_(J,I).

## 2. Equivariant equivalence to the mixed-profile interface
The complexes C and Z are equivariantly homotopy equivalent.

Proof on nonempty face posets. For a face sigma of C, put
 I_sigma={i: sigma subset L_i},
 J_sigma={j: sigma subset tau L_j}.
Both sets are nonempty. Map sigma to the product cell (I_sigma,J_sigma). Conversely map an allowed product cell (I,J) to the simplex Q_(I,J), considered as a face of C. Both maps reverse inclusion. Their composites enlarge the original face or cell. Pointwise comparable poset maps induce homotopies to the identity on barycentric subdivisions by the prism construction. The maps and homotopies commute with tau, which swaps the two index sets and applies tau to labels. QED.

The subdivision of the product-cell face poset is the barycentric subdivision of Z, so this proves an equivalence of actual realizations.

## 3. Exact odd-vector-field zero
Define
 V(a,b)=a-b in E={v in R^p: sum_i v_i=0},
a real vector space of dimension p-1. Then V is continuous and odd.

Grand closure holds iff V has a zero on Z, equivalently iff Z has an involution-fixed point.

If a=b, choose an index i in their common nonempty support. The smallest product face supporting (a,b) is allowed and supplies an actual label u in L_i intersect tau L_i. Thus u and tau u both belong to the SAME root profile, giving the reversed-tail grand splice. Conversely any overlap L_i intersect tau L_i permits (e_i,e_i) in Z and gives a zero.

The root-index simplex is essential. Equal probability distributions have equal support on actual ROOT IDENTITIES. A zero therefore yields a literal diagonal root witness. Equality of convex averages of physical n-bit roots would be a weaker condition.

## 4. Dimension bound under hypothetical failure
If closure fails, every allowed (I,J) has I intersect J empty. Otherwise an index in the intersection and a label in Q_(I,J) already give closure.

Therefore Z lies in the deleted product
 D_p={(a,b) in Delta times Delta: supp(a) intersect supp(b)=empty}.
For p>=2, D_p is equivariantly homeomorphic to S^(p-2). An explicit map is
 (a,b) -> (a-b)/||a-b||_2.
Its image lies on the unit sphere in E. Conversely, for v on that sphere, put
 t=sum_i max(v_i,0)=sum_i max(-v_i,0)>0,
 a_i=max(v_i,0)/t,
 b_i=max(-v_i,0)/t.
These are disjoint-support probability vectors and inverse the radial map. Swapping a,b corresponds to v->-v.

An allowed cell has dimension |I|+|J|-2<=p-2. Thus under failure the mixed interface C has an equivariantly homotopy equivalent finite free cell complex of dimension at most p-2. For p=1 the deleted product is empty, so a nonempty interface already forces closure.

## 5. Finite homology and connectivity forcing criteria
If C is nonempty and
 reduced H_j(C;F2)=0 for every 0<=j<=p-2,
then closure holds. Under failure, Z would be a nonempty F2-acyclic finite complex (its higher homology vanishes by the dimension bound) carrying a free involution. Acyclicity gives Euler characteristic 1, whereas a free involution pairs all cells and gives even Euler characteristic. Contradiction.

In particular (p-2)-connectivity of C implies closure. There is also a direct Borsuk-Ulam proof: (p-2)-connectivity lets one construct an equivariant map S^(p-1)->C by extending over one hemisphere successively and defining the other by tau. Transporting it to Z and applying V gives an odd map S^(p-1)->R^(p-1); its forced zero is the exact same-root witness.

The small-profile cases are:
 p=1: nonempty C forces closure.
 p=2: connected C forces closure.
 p=3: connected C with H_1(C;F2)=0 forces closure.
These are general profile-count criteria, with no restriction on cube dimension.

Equivalently, any hypothetical failure with nonempty C requires a nonzero reduced homology group H_j(C;F2) for some j<=p-2. Thus the number of maximal profiles bounds the degree of a necessary topological obstruction.

## 6. An elementary two-profile check
Under failure with two retained profiles,
 C=Delta(L_1 intersect tau L_2) union Delta(L_2 intersect tau L_1),
since both diagonal intersections are empty. The displayed simplices are reflected partners and have disjoint vertex sets: a shared label u would lie in L_1 intersect tau L_1. Hence C is either empty or two disjoint contractible components. This directly verifies the connectedness forcing criterion without homotopy machinery.

## Research frontier
We now have a continuous odd vector field whose zero provides a literal NORI witness, and a proven dimension reduction for its no-zero carrier. The remaining existence task is to force a zero using the interdependence of profiles from one physical-face coloring, for example by establishing the stated interface homology or connectivity bounds, or an admissible equivariant sphere carrier. No such universal forcing property has yet been proved. The grand conjecture remains open.
