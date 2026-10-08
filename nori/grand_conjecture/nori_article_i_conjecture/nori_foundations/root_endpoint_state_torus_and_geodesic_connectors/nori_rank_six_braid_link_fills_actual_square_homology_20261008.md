# Accepted rank-six memory braid fills a nontrivial physical square cycle

# Rank-six braid-link circle detects and fills an actual physical square cycle

Keep n=6 and the same valid NORI coloring and accepted monochromatic memory state b merging
P=(1,2,3,4,5,6), P'=(1,2,4,3,5,6)
from root 000000. Let C_<6 be the order complex of all admitted directed geodesic segments of rank<=5, ordered by oriented contiguous inclusion. Because boundary-memory states are unique through rank five, this is also the exact memory quotient subcomplex below b. Let L_b subset C_<6 be the rank-six merged state's lower link, previously proved homotopy equivalent to S^1.

**Theorem 1 (canonical start-point map to the physical edge graph).** For ANY hereditary directed-segment complex, there is a continuous map
f_start:|C| -> |Q_n^(1)|
sending a segment P to its first physical vertex and each simplex of nested contiguous segments to the corresponding piecewise-linear physical path of starting vertices along its maximal segment.

Proof. On a chain P_0<...<P_m, write the start of each P_j as vertex v_(a_j) of P_m=(v_0,...,v_k), so k>=a_0>=a_1>=...>=a_m=0. Send a point with barycentric coefficients lambda_j to the point at continuous arclength t=sum_j lambda_j a_j along the edgewise linear path v_0->...->v_k in the abstract cube edge graph. The coefficients a_j decrease along chains, so this is continuous on the simplex and maps to the physical edge-graph path. If a face of the simplex removes its maximal element, all retained segments lie in the new maximal subsegment; replacing the original indices by indices relative to this subsegment merely translates their arclength origin, preserving the same physical point. Thus the simplex maps agree on overlaps and define a continuous global map. QED.

**Theorem 2 (the circular link survives in preattachment H_1).** Choose the two common lower-link components represented by the common two-edge PREFIX A=P[0,2]=P'[0,2] and common two-edge SUFFIX Z=P[4,6]=P'[4,6]. In the lower link L_P of P there is a path
A < P[0,5] > P[1,5] < P[1,6] > Z.
In L_P' there is the analogous path with P' in place of P. They share their endpoints A,Z, and their union represents the generator of H_1(L_b;F2).

Under f_start, the first path follows the physical route from vertex 000000 through directions 1,2,3,4 to the common physical vertex v_4={1,2,3,4}, while the second path follows directions 1,2,4,3 to the same v_4. Their difference is the closed FOUR-EDGE physical square at base v_2={1,2}, with free directions 3,4:
v_2 -> v_2 XOR e_3 -> v_2 XOR{3,4} -> v_2 XOR e_4 -> v_2.
This square cycle represents a nonzero class in H_1(|Q_6^(1)|;F2), since the target is a graph and its edges appear exactly once in the cycle. Consequently the generator of H_1(L_b;F2) maps NONTRIVIALLY into H_1(C_<6;F2). In particular it is not already killed by any lower-rank path-state simplices.

**Theorem 3 (real rank-six relative filling).** Adjoining the accepted memory-state vertex b and all its incident nested-chain simplices attaches the cone b*L_b to C_<6. The relative homology of the attachment contains
H_2(b*L_b,L_b;F2) ~= H_1(L_b;F2) = F2.
The boundary of this relative class is the NONZERO preexisting physical square-cycle class described in Theorem 2. Thus this actual rank-six braid identification KILLS a genuine H_1 class of the lower-rank reachability complex by attaching a two-dimensional filling; it is not a homotopically trivial cone over a contractible link.

Under complemented reversal Theta, b has a distinct partner state Theta(b), whose link is another circle. Its physical square under the corresponding start-point map is the ANTIPODAL {3,4}-square: originally exterior bits outside directions3,4 are (1,2)=(1,1),(5,6)=(0,0), while the reversed-complemented paths swap 3,4 after directions (6,5), giving exterior bits (1,2)=(0,0),(5,6)=(1,1). Hence the two homological fillings occur in an antipodally paired fashion.

**Research interpretation.** This is an explicit, genuinely higher-dimensional, COLOR-COMPATIBLE topological repair mechanism within the honest reachable-target construction. The canonical segment-poset complex alone collapses to a graph, but exact memory-state merging creates antipodally paired square fillings corresponding to reordering internal coordinates. A global proof would have to show that the necessary system of such fillings (and higher braid analogues) cannot be completed without at least one accepting full antipodal state. The theorem itself is an example for a valid coloring, not universal existence of such a state and not a proof of NORI grand closure.
