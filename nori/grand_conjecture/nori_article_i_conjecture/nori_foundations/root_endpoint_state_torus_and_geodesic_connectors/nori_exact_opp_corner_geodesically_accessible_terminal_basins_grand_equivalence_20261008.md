# Active NORI exactly equals intersection of two opposite-corner rooted monochromatic terminal basins

# Exact NORI grand closure as intersection of two antipodally corner-rooted geodesically accessible basins

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
