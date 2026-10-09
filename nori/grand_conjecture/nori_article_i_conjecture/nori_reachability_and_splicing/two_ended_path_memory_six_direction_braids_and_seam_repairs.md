# Two-ended path memory, six-direction braids, and seam repairs

# Two-ended path memory, six-direction braids, and seam repairs

A full one-switch path decomposes at one transition into two monochromatic branches, but its seam contributes two ordered three-face windows. The terminal two-direction memory is therefore essential for both a precise reachability statement and legal concatenation. At rank six, two distinct traversal histories can first meet in the same reduced memory state, producing a braid whose links encode the missing exchange information.

## Exact boundary-memory quotient first identifies genuinely different geodesics at rank six

For ordered-three-face NORI, let B(P) be the EXACT two-ended boundary memory state of a directed k-edge geodesic P as previously established: oriented endpoints (x,y), its first two direction entries and last two direction entries (truncated when k<2), first and last three-window colors when k>=3, and total number of color changes clipped at 2. Endpoint XOR determines the unordered set S of its k used directions. Two directed segments are identified only if these memory states agree.

**Theorem 1 (injective through rank five).** For every coloring (and independently of NORI oddness), the map P->B(P) is INJECTIVE on segments of lengths k<=5. Proof: for k<=4 the first and last two direction entries jointly list the entire direction order; for k=5 they reveal p1,p2,p4,p5, while the sole missing entry p3 is the unique coordinate in S minus those four. The starting endpoint x then determines the directed segment uniquely. Shorter lengths have the evident truncated convention.

**Theorem 2 (actual ambiguity at rank six).** For n>=6, there exists a valid antipodal-reversal-odd ordered-three-face coloring and two DISTINCT directed rank-six segments P,P' with B(P)=B(P'). Take common starting root x=0^n and the direction orders
P=(1,2,3,4,5,6),
P'=(1,2,4,3,5,6).
They have the same endpoints and support S={1,...,6}, head=(1,2), tail=(5,6), but differ by a middle adjacent transposition. Assign color zero to all four ordered-three-face windows of P and to all four of P'. They then have equal first/last colors 0 and clipped change count 0, hence identical memory states. These finitely many ordered-face objects belong to distinct orbits of the NORI involution (F,pi)->(bar F,rev pi): where a free unordered triple is shared, the two displayed internal ordered triples are neither identical nor reversals on antipodal faces, and the other triples have different free coordinate sets. Thus all eight prescribed zeros are simultaneously consistent; extend to a full NORI coloring by choosing arbitrary colors on the remaining involution orbits and complementary colors on their mates. The two underlying paths remain distinct.

**Theorem 3 (exact finite-memory directed chains).** The predecessor/successor transitions by prepending or appending one unused direction are Markov on B(P): the new ordered three-window is computed solely from the relevant endpoint and the first/last two direction memories; changes and boundary colors update exactly. Therefore every sequence of legal boundary-state cover transitions from a realizable rank-zero state is represented by an ACTUAL chain of nested geodesic segments, even when several full histories have been merged into one state. This is proved by induction on the sequence length, using that every representative of a state admits the same named legal extension with the same resulting state. The involution Theta on states exchanges left and right transitions, reverses the two direction memories, and complements/swaps first and last colors; for n>=3 it remains free on the state vertices.

**Topological implication.** The full-history contiguous-segment order complex has equivariant index exactly one for EVERY hereditary admissibility rule: each higher segment has a contractible lower link and the whole complex collapses to its directed-edge graph. The exact boundary-memory quotient agrees with that full-history complex through rank five. Starting at rank six it can GLUE distinct histories with common continuation rules, so the former contractible-link collapse argument no longer automatically applies. This supplies a concrete place for higher-dimensional topology to appear while retaining actual geodesic-reachability labels.

This does NOT prove that the quotient has index>1, nor that its quotient-induced order complex has no spurious simplices. To avoid phantom witness chains, define the finite-memory path complex with simplices consisting of states along actual Markov extension chains (or use the exact transition DAG's reachability-path realization), and exploit the inductive chain-lifting property above. The next genuinely new obligation is to determine whether the rank-six braid identifications create nontrivial equivariant relative homology or a Tucker-type carrier intersection that forces an accepting full-rank state.

## Rank-six braid-link circle detects and fills an actual physical square cycle

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

## Exact common-middle root square of a two-window NORI geodesic splice

Let c be ANY physical ordered-three-face coloring, and fix a genuine full direction-distinct geodesic word p=(p1,...,pn) with a cut after \ell directions, where 2<=\ell<=n−2. Write the two last prefix directions u=p_(ell−1),v=p_ell and the first two suffix directions w=p_(ell+1),t=p_(ell+2), all pairwise distinct. For any cube root x, set S={p1,...,p_ell}, y=x XOR S, and define its TWO physical crossing-window faces
  L_x=( F(y;{u,v,w}), (u,v,w) ),
  R_x=( F(y;{v,w,t}), (v,w,t) ).
These are exactly the ordered faces of the two windows straddling the cut in the full geodesic rooted at x.

**THEOREM (literal two-seam cubical flatness, and sharp dimension).** For ANY translation mask A⊆{v,w} and x'=x XOR A, the two ordered physical faces are literally IDENTICAL:
  L_(x')=L_x, R_(x')=R_x.
Consequently their ordered colors are identical for all FOUR physical roots x, x XOR v, x XOR w, x XOR v XOR w. In other words the two-seam color pair is constant on the full physical 2-cube whose free coordinate directions are exactly {v,w}, for ANY NORI coloring and even without antipodal oddness.

Conversely, suppose A⊆[n] is such that translating x by each individual direction a∈A leaves BOTH ordered physical face OBJECTS unchanged (not merely their colors, which may coincidentally be constant). Then A⊆{v,w}. Thus the two-dimensional root square above is the MAXIMAL full physical coordinate face on which BOTH crossing window objects stay literally fixed. This is sharp in every dimension and every direction order.

**Proof.** A physical ordered face F(y;U) is the cube face with free directions U and all other coordinate bits fixed to y outside U. Translating the starting root x by direction a changes the cut vertex y by the same direction a, so F(y;U) is unchanged iff a∈U. For the left and right crossing faces their free direction sets are U_L={u,v,w} and U_R={v,w,t}. Their intersection is EXACTLY {v,w}, since p has pairwise distinct directions. Hence BOTH faces remain unchanged precisely under flips in span{v,w}; in particular all four root-square vertices have the same two physical objects and colors. Any additional direction lies outside at least one free set, so changing its root bit changes that ordered physical face object, establishing sharpness. QED.

**JOINT CONNECTION WITH MULTIROOT TUCKER.** The root-square near-midpoint Tucker theorem nori_multiroot_near_midpoint_tucker_common_cut_root_square_20261008 supplies, for ANY preassigned physical two-coordinate root square, two packets of eight total actual full endpoint-opposed paths with a common near-middle support cut S (n>=11). To take advantage of THIS theorem's exact two-seam flatness, one must show that some packet's selected cross-splice has the two shared middle seam directions (v,w) EQUAL TO the two free directions of the preassigned root square. That self-consistent alignment is NOT supplied by Tucker merely from common S. More generally, the eight packet paths can have different last prefix and first suffix directions, so their two seam objects need not be identical across the square. Establishing this boundary-memory/root-square alignment, and then synchronizing monochromatic branches or reducing the switch count, is a precisely formulated missing combinatorial forcing lemma.

**STATUS.** This is a genuine physical cubical flatness theorem of the two crossing windows, not an unrestricted NORI closure theorem. It sharply identifies the maximal root-square dimension available for *literal* simultaneous seam invariance (two), explaining why a four-root packet is natural in ordered-three-face NORI.

The braid and root-square calculations demonstrate why pure endpoint reachability loses the needed geometry. A successful global repair must remember the two overlapping physical windows at each concatenation.
