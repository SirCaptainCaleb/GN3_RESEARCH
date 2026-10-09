# Barycentric reachability carriers and antipodal boundary maps

# Barycentric reachability carriers and antipodal boundary maps

The Boolean cube admits a barycentric realization in which each directed geodesic appears as a chain of nested coordinate supports. Reachability simplices are honest only when their vertices share a single actual monochromatic path witness. This framework compares terminal labels, canonical midpoints, convex relaxations and antipodal boundary maps.

## Canonical face centers recognize every monochromatically reachable target exactly

In the n-dimensional diagonal-fiber cross X_n, let z,z' be any two physical vertices, and D={i:z_i neq z'_i}. Their affine fibers F_z and F_z' intersect in the coordinate constraints r_i=s_i=1/2 for i in D and s_j=(r_j XOR z_j) in the continuous affine sense for j outside D. Define the CANONICAL midpoint point
m(z,z')=(r,s), where
r_i=(z_i+z'_i)/2 and s_i=1/2 for i in D;
r_j=z_j=z'_j and s_j=0 for j outside D.
It satisfies m(z,z')=m(z',z) and belongs to F_z intersect F_z'. In the coordinate chart F_z, this is exactly the center of the |D|-dimensional face with supports S subseteq D, incident with the empty-support apex.

**Theorem (exact partial-target midpoint test).** For any q in {0,1},
m(z,z') belongs to K_q(z) iff there exists a monochromatic q-GEODESIC z->z'.
Consequently m(z,z') in K_q(z) iff it belongs to K_q(z'), and both hold precisely when z,z' are joined by a q-monochromatic geodesic. Thus the colored edge carriers are just the distance-one instances of an exact midpoint-overlap principle at EVERY distance.

*Proof.* A q-monochromatic geodesic z->z' has support exactly D. Its full prefix simplex in F_z contains the empty vertex and the D vertex, so it contains their midpoint m(z,z'). Reversing the geodesic gives the same midpoint in K_q(z').
Conversely suppose m(z,z') lies in one witnessed prefix simplex of K_q(z), corresponding to a chain of actual supports S_0 subset ... subset S_k. Since each s_j=0 outside D, any vertex of this chain contributing with positive barycentric weight has no directions outside D. Since each s_i=1/2 inside D, no contributing supports can all omit any such i or all contain any such i. By nestedness, a positive-weight minimal contributing support must be empty (otherwise some coordinate remains one in the entire positive support), and the maximal positive-weight support must be D (otherwise some coordinate remains zero). The witnessed monochromatic path therefore contains empty and full D support along its own order, yielding a monochromatic geodesic z->z'. More formally, the faces of a Freudenthal chain intersect the relative cube center only if the chain includes both its minimum and maximum support. QED.

**Corollary (face-barycenter labels).** For fixed z, all candidate reachable vertices z' are represented by the 2^n barycenters m(z,z') of cube faces containing the root apex in F_z. The full antipodal conjecture asks whether the barycenter m(z,bar z)=o of the ENTIRE fiber appears in some K_q(z). If z,z' differ by k coordinates, q-reachability to z' is literally the inclusion of the associated k-face barycenter in the witnessed path complex. These barycenter labels avoid false intersections of convex averages: each particular canonical midpoint has an exact shortest-path extraction theorem.

**Root-color symmetry.** Under physical antipodality alpha(r,s)=(1-r,s), one has alpha(m(z,z'))=m(bar z,bar z'); oddness sends K_q(z) to K_(1-q)(bar z). Both the midpoint representation and its witness test are fully antipodally equivariant.

**Limit.** Other points of F_z intersect F_z' may lie in K_q(z) and K_r(z') without monochromatic shortest paths between z,z'. The theorem singles out canonical midpoint points as the faithful labels; a general topological intersection theorem must force one of these certified points, rather than an arbitrary geometric crossing. For full antipodal targets, F_z intersect F_bar z={o}, so every intersection is automatically canonical.

## A color-free 2n-bit reachability holonomy graph: odd signed cycles force closure

Let c be an antipodally odd binary UNDIRECTED edge coloring of Q_n. Define the uncolored monochromatic-geodesic reachability relation
\[
\mathcal E=\{(x,S):x\in Q_n,\ \varnothing\ne S\subseteq[n],\ x\oplus S\in R(x)\}.
\]
These are exactly ROOT–SUPPORT states with n root bits plus n support bits. They are defined solely by the COLOR-FREE sets R(x). Associate a signed graph H_R to the states with THREE types of (undirected) edges:

(A) **Antipodal root flip**, sign 1:
\[
(x,S)\longleftrightarrow(\bar x,S).
\]
(B) **Endpoint reversal/root swap**, sign 0:
\[
(x,S)\longleftrightarrow(x\oplus S,S).
\]
(C) **Near-complementary supports at the same root**, sign 1:
\[
(x,S)\longleftrightarrow(x,T)
\quad\text{if } S\cap T=\varnothing,\ S\cup T=[n]\setminus\{i\}\text{ for some i}.
\]
All endpoints of all these edges are in \(\mathcal E\): (A) by odd coloring, (B) by undirected path reversal, and (C) by definition. Retain edge types if parallel edges arise.

**Theorem (odd-holonomy extraction).** If H_R contains a closed walk whose edge-sign sum is odd and that traverses at least one (C) edge, then c has a MONOCHROMATIC FULL ANTIPODAL GEODESIC. Conversely, in any hypothetical counterexample, every connected component of H_R containing a (C) edge carries a unique consistent binary vertex potential q such that
\[
q(\bar x,S)=q(x,S)\oplus1,\quad
q(x\oplus S,S)=q(x,S),\quad
q(x,T)=q(x,S)\oplus1
\]
on the corresponding edge types. Thus such a component has zero signed holonomy around every closed walk.

**Proof.** For a state (x,S), define \(C(x,S)\subseteq\mathbb F_2\) to be the NONEMPTY set of colors of all monochromatic geodesics joining x to x⊕S. This auxiliary witness-color set is used ONLY IN THE PROOF; it is absent from the state graph and reachability-label definition. Under (A), the antipodal copy complements edge colors exactly, giving C(bar x,S)=1-C(x,S). Under (B), reversal of an undirected edge path preserves each edge color, giving C(x⊕S,S)=C(x,S). At a (C) edge, if C(x,S) and C(x,T) shared any color q, their two q-geodesics would have disjoint coordinate supports covering n-1 coordinates. Their concatenation is a q-colored length-(n-1) geodesic. Its two end-extension edges are antipodal with opposite colors, so one completes it to a full q-geodesic. Therefore, in the absence of a full monochromatic antipodal geodesic, C(x,S) and C(x,T) are disjoint nonempty subsets of the two-element color set. They must be complementary SINGLETONS. The bijections in (A),(B) preserve singleton cardinality, so every state in a connected component containing a (C) edge has a unique witness color. The displayed potential q is then its unique element. Along any closed walk q must return to itself, requiring an even number of sign-1 edges. Hence an odd-signed closed walk implies closure. QED.

**No premature role for the colors.** The graph H_R and the existence of an odd signed cycle depend only on R(x), the cube's root/coordinate geometry, and the sign of three structural operations. The two color indices appear only inside the extraction proof to establish the obstruction. This is exactly an 'antipodal-label coincidence implies actual monochromatic witness' certificate with explicit extraction.

**Relation to odd-dimensional Kneser cycles.** Restrict to a single root x and the (C) edges. This recovers the near-complement graph \(\Gamma_x\). For n odd, middle-layer Kneser odd cycles give odd holonomy immediately. For n even, \(\Gamma_x\) is bipartite by support-cardinality parity, but root antipodality (A) and endpoint exchange (B) can create new cross-root signed cycles. This gives a unified dimension-independent target: force a NONTRIVIAL Z_2-holonomy cycle in the root-coupled reachable state graph.

**Scope and challenge.** A signed frustrated cycle is a SUFFICIENT condition, not asserted to exist for every coloring. Proving its existence from antipodal-odd edge incidence would establish the edge-geodesic conjecture. The graph may be balanced for some colorings that already have a monochromatic antipodal geodesic; the theorem is not an equivalence. One can also treat any reachable support S=[n] as immediate closure, independently of holonomy. Its value is a precise, color-free, topologically meaningful inconsistency criterion, with no small-dimension classification.

## Exact NORI grand closure as intersection of two antipodally corner-rooted geodesically accessible basins

Let c be the ACTIVE antipodal-reversal-odd binary ordered-three-face coloring on Q_n, n>=4. Fix distinct coordinates a,b and let J=(a,b), D=[n]\{a,b}. Fix any cube vertex y and define y^D=y⊕D, the complement in D directions ONLY (its a,b bits unchanged). Define the **COLOR-FREE monochromatic terminal basin**
\[
T_J(y)=\bigl\{x\in Q_n:\ \exists\text{ a directed MONOCHROMATIC ordered-three-face-window geodesic }x\to y
\text{ ending in ordered directions }(a,b)\bigr\}.
\]
Either monochromatic color is permitted, without recording it. Paths of length two with no three-face window are included vacuously; this makes the basin contain its natural base corner. All roots x lie in the (n-2)-dimensional physical facet
\[
H_y^{a,b}=\{x:x_a=1-y_a,\ x_b=1-y_b\}.
\]
Let
\[
b_0=y\oplus\{a,b\}\in H_y^{a,b},\qquad
b_1=b_0\oplus D\in H_y^{a,b}.
\]
These are antipodal vertices WITHIN the facet H_y^{a,b}. The second basin \(T_{\operatorname{rev}J}(y^D)\) lies in the SAME facet H_y^{a,b} and has natural base corner b_1.

**THEOREM 1 (exact two-basin intersection equivalence).** The grand NORI conjecture in Q_n holds if and only if there exist y and ordered tail J=(a,b) such that
\[
\boxed{T_{(a,b)}(y)\cap T_{(b,a)}(y^D)\ne\varnothing.}
\]
The regions are UNCOLORED monochromatic-geodesic reachability labels, and the intersection automatically splices into a full antipodal geodesic with at most one ordered-three-face color change; the colors of the two branch witnesses may agree or differ.

**Proof.** Suppose x is in the intersection. A directed monochromatic x-to-y geodesic A has terminal directions (a,b), and a directed monochromatic x-to-y^D geodesic B has terminal directions (b,a). Since x_a=1-y_a and x_b=1-y_b, both paths traverse a,b and their remaining direction supports are respectively
\[
U=\{i\in D:x_i\ne y_i\},\qquad
V=\{i\in D:x_i\ne (y^D)_i\}=D\setminus U.
\]
Thus their full supports intersect in exactly {a,b}, and their non-tail supports complement in D. Apply the previously proved exact reversed-two-tail splice theorem: truncate A before a,b, append the global antipodal reversal of B, and get a full antipodal geodesic with its first |U| windows of one monochromatic color and last |V| windows of the opposite of B's color. When both U,V are nonempty this is exactly the proof. In the boundary cases U or V empty, one of A/B is a FULL monochromatic n-edge geodesic because it traverses all n coordinates, which itself establishes closure. Conversely any full one-switch antipodal geodesic decomposes by the exact reversed-two-tail theorem into two such monochromatic branches from some common root x ending in opposite facet-antipodal vertices y and y^D with reversed ordered tails J and revJ, so x belongs to the intersection. QED.

**THEOREM 2 (strong rooted accessibility).** Each \(T_J(y)\subseteq H_y^{a,b}\) contains the base corner b_0 and ALL its d=n-2 neighbors inside the facet. More strongly, for EVERY x∈T_J(y), there exists a full Hamming-shortest path INSIDE \(T_J(y)\) from x to b_0; in particular T_J(y) induces a connected subgraph and is geodesically rooted at b_0. The second basin T_revJ(y^D) has the same properties with root b_1.

**Proof.** The length-two path from b_0 to y with direction word (a,b) has no three-face windows and is included by convention. For any i∈D, the three-edge path from b_0⊕e_i to y with word (i,a,b) has exactly one ordered-three-face window and is therefore automatically monochromatic: all d neighbors are included. For general x∈T_J(y), choose a monochromatic witnessing geodesic
\[
x\ \xrightarrow{u_1,\ldots,u_s,a,b}\ y,
\quad\{u_1,\ldots,u_s\}=\{i\in D:x_i\ne(b_0)_i\}.
\]
Trimming its first direction u_1 produces the suffix geodesic from x⊕e_{u_1} to y, with ordered terminal pair (a,b) and a subsequence of the original monochromatic windows. Thus x⊕e_{u_1} lies in T_J(y). Repeat through u_2,...,u_s to b_0. These vertices form a shortest path within the root facet H_y, since each step removes one disagreement coordinate with b_0. The analogous proof applies to revJ at the antipodal corner b_1. QED.

**Exact topological problem.** The grand NORI conjecture is equivalent to the impossibility of TWO DISJOINT geodesically corner-rooted terminal basins T_J(y) and T_revJ(y^D) for EVERY choice of y,a,b. This is a precise two-shore Hex/Hartman connector formulation:
- the opposite base corners b_0 and b_1 lie in a physical d-cube H;
- each basin contains its entire radius-1 star and is geodesically connected to its base;
- basin membership means ACTUAL monochromatic ordered-face-window geodesic reachability and records NO color;
- an intersection yields one genuine full good geodesic with no uncontrolled seam windows.

Importantly, two arbitrary rooted connected radius-one neighborhoods of opposite corners CAN be disjoint for d>=3; topology must use the coupling among basin families for different tails J and terminal vertices y. The next research goal is a simultaneous Sperner/KKM/Hex argument enforcing intersection across the collection of all such coupled accessible basins, not a false pointwise Helly assertion for a single pair.

The topology of an abstract target carrier cannot be used to infer a path unless its simplices satisfy the literal geodesic-certification rule. Several counterexamples here delimit that rule sharply.
