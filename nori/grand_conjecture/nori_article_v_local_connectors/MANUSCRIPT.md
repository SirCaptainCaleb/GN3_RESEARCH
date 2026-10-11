# Article V — Local connectors and exchange geometry

## Article setting and orientation

Physical edge and ordered-face certificates yield genuine monochromatic four- and six-edge paths, dead-edge rigidity, bichromatic root hubs, root-square separators, and exact seam-splicing statements. These constructive results are independent of abstract pairwise coloring labels, and the surviving Subsections track their root, support and exterior-bit hypotheses explicitly.

Several large investigations primarily established that one-move descent, rooted short-path coverage, certified-square index, or oppositely colored terminal caps do not by themselves force a full good path. Their complete rigorous proofs and finite certificates are now consolidated in the research note associated with this Article. The formerly dedicated maximal-geodesic-exchange Section has consequently been retired from active manuscript composition, while retaining its historical composition in the database.

*Full Article composition: [source manuscript](../nori_article_v_local_connectors.md).*

## Local monochromatic connectors, certified squares, and dead-edge rigidity

The active Subsections establish physical connector-square certificates, actual six-edge hub paths under stated hypotheses, the resulting monochromatic edge shadows, and covered-root separator constraints. A certificate is a genuine four-edge monochromatic cube geodesic; formal shadow adjacency is not substituted for a physical window shift. These statements give reusable local geometry relevant to global splicing.

The inability of a particular certified-square carrier to force Tucker index two has been archived as a precise research note. The remaining material concerns affirmative structural consequences and their actual physical hypotheses, without claiming that local connector density alone settles unrestricted antipodal extraction.

*Full Section composition: [source manuscript](nori_local_connector_geometry.md).*

### Covered-root separators and live-edge antipodal carriers

# Covered-root separators and live-edge antipodal carriers

Certified physical squares cover parts of the cube and identify vertices through which genuine monochromatic four-path witnesses pass. The geometry of uncovered edges constrains root separators, while two-color witnesses can organize into antipodally invariant carriers. The purpose here is to pass from local certification counts to a genuine path-relevant global separator.

THEOREM A (RADIUS-THREE CONSTANCY ACROSS DIFFERENT DEAD DIRECTIONS). Let n>=5 and let c be an active NORI antipodal-reversal-odd coloring of ordered physical 3-faces. Let M be the set of DEAD physical cube edges, namely those traversed by no monochromatic directed 4-edge geodesic. M is a matching. For each vertex z incident to a dead edge e in coordinate i, denote by t(z) its unique DEAD-EDGE RIGIDITY BIT: all ordered three-faces through z omitting i, or having i in the middle, have color t(z), while those with i first or last have color 1-t(z). Both endpoints of the same dead edge have the same t. Then for ANY two dead-incident cube vertices z,w with d_H(z,w)<=3, one has t(z)=t(w), REGARDLESS of whether the two dead edges have the same or different directions.
PROOF. If both dead edges use the same direction i, their two projected positions in Q_(n-1) differ in at most 3 coordinates. Choose one endpoint of each edge with matching i-bit; the two endpoints lie in a physical three-face with free directions equal to their at-most-three exterior differing coordinates, padded to three distinct non-i directions as needed. The ordered color of this face at either endpoint is the respective dead rigidity bit (i omitted), so they are equal. If the dead edges use distinct directions i,j, the proved dead-direction separation theorem says their ENDPOINT SETS have distance >=3. In particular d_H(z,w)<3 is impossible. If d_H(z,w)=3, write S=supp(z xor w), |S|=3. If i∈S, the other endpoint z xor i of the i-dead edge lies at distance2 from w, forbidden. Thus i∉S. Similarly j∉S. Therefore the ordered physical 3-face with free triple S contains both z,w and omits both i,j, so its single color is both t(z) and t(w). QED.
THEOREM B (UNCONDITIONAL FULLY COVERED ROOT INDEX TWO). Let U={z∈Q_n:z is incident to NO dead physical cube edge}; each of its n incident edges lies on at least one actual monochromatic four-edge geodesic. Let X be the Freudenthal triangulation of the 3-dimensional cubical skeleton of the geometric n-cube boundary ∂[0,1]^n, centrally inverted by τ(z)=bar z. The quotient X/τ is the 3-skeleton of RP^(n-1) under its induced CW decomposition, and its double-cover class w satisfies w^3!=0. Define odd scalar vertex labeling f(z)=0 if z∈U and f(z)=(-1)^t(z) otherwise. By active NORI antipodal reversal, t(bar z)=1-t(z), so f(bar z)=-f(z). Extend affinely on Freudenthal simplices. Every simplex has its cube vertices in one physical 3-face, so all nonzero labels are equal-sign by Theorem A. Therefore its ZERO LOCUS is EXACTLY the simplicial subcomplex X[U] induced by REAL fully certified physical cube roots: no affine cancellation among opposite forced bits. The odd scalar zero-set index-drop lemma yields w1(X[U]/τ)^2!=0, or equivalently ind_Z2(X[U])>=2, for EVERY active NORI coloring, WITHOUT a common-dead-direction hypothesis.
In particular some component of X[U] is antipodally invariant, and there is an actual vertex chain z=z0,...,zr=bar z of fully certified roots with successive Hamming distances at most THREE (possibly using face diagonals as simplicial edges). The nonzero second power is strictly stronger than connectedness or the previously proved index-one two-skeleton carrier. If M is empty, f≡0, X[U]=X, so the same conclusion holds (in fact index>=3).
PHYSICAL LIMITATION. The adjacent root vertices in this chain have individually actual local four-geodesic witnesses, but those witnesses need not have the same color or the same ordered two-direction memory and steps of Hamming distance 2 or3 are not necessarily cube edges. The index-two topology does not alone imply a full antipodal geodesic with at most one color change. It is an exact globally equivariant certified-root carrier available in ALL dimensions and ALL active NORI colorings, improving the conditionally stated one-dead-direction variant in nori_fully_covered_root_vertex_two_skeleton_index_one_antipodal_20261008.

THEOREM (NEW DENSITY LOWER BOUND FOR COMPLETELY FOUR-WINDOW-CERTIFIED ROOTS). Let n>=5 and color actual physical ordered three-faces of Q_n with active NORI antipodal-reversal oddness. Let M be the matching of DEAD physical cube edges traversed by no genuinely monochromatic 4-edge directed geodesic. Let D be the set of cube vertices incident to dead edges (so |D|=2|M|), and U=Q_n\D the FULLY CERTIFIED vertices, each incident physical edge lying on at least one actual mono4 path. The strengthened universal dead-rigidity radius-three theorem implies a thickness-three antipodal separator: EVERY full antipodal directed n-geodesic starting in D encounters at least THREE CONSECUTIVE vertices of U.
In contrast, every full antipodal geodesic starting in U automatically contains at least TWO U vertices—its root x and its antipode bar x—because U is antipodally invariant. Choose the starting root uniformly among all 2^n cube vertices and the full coordinate permutation uniformly among n!. Let N(P) be the number of U vertices visited along the resulting full antipodal geodesic, counting both endpoints. Conditioning on the root type gives
 E[N(P)] >= (3|D|+2|U|)/2^n.
But each of the n+1 vertex positions of a uniform rooted full geodesic is UNIFORMLY distributed over Q_n, so exactly E[N(P)]=(n+1)|U|/2^n. Comparing and substituting |D|=2^n−|U| yields
 (n+1)|U| >=3(2^n−|U|)+2|U|,
 and hence
    BOXED |U| >= ceil(3*2^n/(n+2)).
Because U is antipodally paired, the sharper integral form is |U| >=2 ceil(3*2^(n−1)/(n+2)). Equivalently, the number of physical dead edges is bounded above by
    |M| <= 2^(n−1)*(n−1)/(n+2),
with the appropriate integer/even rounding.
This improves the earlier antipodal one-point hitting-set density bound |U|>=ceil(2^n/(n+1)) and is derived from a genuine three-vertex physical-separator constraint, not an abstract topological index or heuristic random choice. Every U vertex has n individually witnessed monochromatic-four-geodesic incident edges, so the bound guarantees an unconditional DIMENSION-DEPENDENT MINIMUM AMOUNT OF CERTIFIED LOCAL PATH GEOMETRY in any NORI coloring.
SCOPE. The three certified consecutive vertices on a path do not guarantee that their separate local mono4 certificates have matching ordered two-direction memories or one color. The theorem does not prove a full <=1-switch antipodal path; it quantitatively strengthens the physical substrate for a possible root-coupled connector construction.

## A six-comparison proof that a direction cannot be globally uncertified

This is an ALTERNATIVE SHORT PROOF of the global missing-direction exclusion already established in Item nori_certified_square_complex_connected_antipodal_one_class_20261008, Theorem 3. It avoids constructing or proving connectedness of the entire middle-direction window shift graph H_i. Together with that Item's independently proved seven-cycle/minimum-degree lemma, it yields its established connectedness theorem. It is NOT a new claim of connectedness.

Let n>=5, and c be a physical ordered-three-face coloring obeying c(bar F,reverse pi)=1-c(F,pi). Fix a coordinate i. Suppose there is no monochromatic centered four-edge connector whose two middle directions include i. Then for every physical hub z and distinct coordinates a,b,c,d with i in {b,c}, the actual face colors h_z(a,b,c) and h_z(b,c,d) are different.

**Exterior-bit independence.** Under this supposition, every ordered face containing i is independent of each of its exterior fixed bits. For an exterior direction d and distinct other directions a,b, use the following comparisons:
 (a,i,b) versus (i,b,d),
 (a,b,i) versus (b,i,d),
 (d,i,a) versus (i,a,b).
These are actual centered four-geodesic comparisons, each with i in the middle pair and hence with unequal colors. Change ONLY the hub bit z_d. The compared window having d FREE remains the SAME physical ordered face and retains its color; therefore the other window, which has d fixed, must also retain its color. This works for every d not in the triple and for all positions of i. Thus define h(a,b,c) as the physical-face-independent color on each ordered triple containing i. Active antipodal reversal now imposes h(c,b,a)=1-h(a,b,c).

**Six-comparison certificate.** Choose a,b,d,e pairwise distinct and outside i, and take
 T0=(i,a,b), T1=(d,i,a), T2=(b,d,i),
 T3=(d,i,e), T4=(i,e,b), T5=(a,i,e), T6=(b,a,i).
The six successive comparisons are respectively supplied (in either direction) by the actual four-direction words
 (d,i,a,b), (b,d,i,a), (b,d,i,e),
 (d,i,e,b), (a,i,e,b), (b,a,i,e).
Every four-word has i among its two middle coordinates, so each step flips the bit h. Six steps yield h(T0)=h(T6). Since T6 is EXACTLY the reverse of T0, the antipodal-reversal oddness says h(T6)=1-h(T0). Contradiction.

**Conclusion.** Every coordinate i occurs as the middle direction of an ACTUAL monochromatic four-edge connector somewhere in Q_n. Combining this with the existing seven-window proof that at most one direction is isolated in each certified-square link, and the cube isoperimetric equality classification, recovers the known global connectedness of the certified-square complex for all active NORI colorings, n>=5.

**Role.** A finite six-shift reversal certificate replaces the larger H_i connectivity-and-bipartition argument for excluding a globally missing coordinate. It does not force compatible long monochromatic paths, and does not improve the sharp equivariant index-one bound on the certified-square complex (Item nori_actual_nori_coloring_sharp_certified_square_index_one_20261008).

Even a densely covered antipodal carrier can have small cohomological index. Coverage and separation are useful only to the extent that their connecting edges preserve monochromatic path certificates.

### Connector square certificates and monochromatic edge shadows

# Connector square certificates and monochromatic edge shadows

A monochromatic four-geodesic passing through an edge or root square is a physical certificate: the neighboring ordered three-faces have equal color on one actual path. As those certificates are glued along their physical edges, a two-color shadow appears, with either a shared edge certified by both colors or a rigid one-color assignment. Local square combinatorics then constrains allowable extensions.

## Monochromatic six-edge hub geodesics from finite ordered-hypergraph Ramsey

Let \(c(F,\pi)\in\{0,1\}\) be ANY coloring of physical ORDERED three-dimensional faces in Q_n. We impose NO antipodal or reversal condition. Let \(N=R_3(6;64)\) denote any finite 64-color Ramsey number guaranteeing a monochromatic six-vertex subset in every 64-coloring of 3-element subsets of an N-element set.

**Theorem (unconditional six-edge monochromatic hub path).** For all \(n\ge N\), EVERY cube vertex z lies on a monochromatic cube geodesic of length SIX whose four ordered-three-face windows all contain z as a common physical vertex. In particular, for n>=N the maximum monochromatic-geodesic length is at least six, independently of the coloring.

**Proof.** Fix z and a fixed linear order on the n coordinate directions. To every 3-element set T={a<b<c}, assign its ordered-face **profile**
\[
\Phi_z(T)=\big(c(F(z;T),\pi):\pi\text{ ranges over all six permutations of }(a,b,c)\big)\in\{0,1\}^6.
\]
This gives at most 64 colors on triples of coordinate directions. By the definition of N, there is a six-element subset W={p1<...<p6} on which \Phi_z is constant on all C(6,3) three-subsets. In particular, for all increasing ordered triples of p's, the common ordered-face color is one fixed bit q.

Start at the cube vertex \(x=z\oplus\{p_1,p_2,p_3\}\), and traverse the six distinct coordinates in order p1,...,p6. The path is a six-edge geodesic, and after the first three edges it passes through z. Its four successive ordered-three-face windows have triples
\[
(p_1,p_2,p_3),\ (p_2,p_3,p_4),\ (p_3,p_4,p_5),\ (p_4,p_5,p_6).
\]
Each physical three-face contains z: the first ends at z, the last starts there, and the middle two pass through it. Hence all four are among the prescribed equal-color faces F(z;T), so every window color equals q. QED.

**Optimal hub-span observation.** All ordered three-edge windows of any L-edge geodesic share a common physical vertex precisely when their vertex-index intervals [0,3],[1,4],...,[L-3,L] have nonempty intersection. This requires L-3<=3, or L<=6. Thus the fixed-hub reduction to ONE ordered triple coloring can certify six-edge monochromatic paths but cannot by itself certify longer paths: an L>=7 path has no common vertex in all its three-face windows. Proving unbounded-length monochromatic geodesics therefore requires coherent color transport between distinct hub vertices, not merely a stronger Ramsey bound on one hub.

**General k-face extension.** For ordered k-face colorings, put N_k=R_k(2k;2^{k!}). If n>=N_k, every cube vertex z lies on a monochromatic 2k-edge geodesic with all k-edge windows passing through z. The proof labels each k-subset by its k!-entry ordered color profile and selects 2k coordinate directions with constant profile. The window intersection criterion is L<=2k.

**Relation to NORI.** For active ordered-three-face NORI, the resulting six-edge monochromatic path supplies an actual reachable terminal-two-tail support of size four from some root. This is a qualitative dimension-independent reachability-rank floor in very high dimensions, stronger than the universal four-edge seed. It does not force complementary reversed-tail support overlap and therefore does not prove grand closure.





## Dead-edge rigidity and extension constraints

Fix a binary coloring of ordered physical three-faces of Q_n. A physical cube edge is certified when some genuine monochromatic four-edge geodesic traverses it. Call an edge dead if no such geodesic exists. The following rigidity holds even without antipodal oddness.

Let e={z,z xor e_i} be dead. The dead-edge rigidity theorem forces a color q for all ordered physical three-faces through either endpoint whose three free directions avoid i, independently of their ordering. Consequently, any directed path of length 3<=k<=min(n-1,6) through one endpoint that uses k distinct directions avoiding i is monochromatic whenever that endpoint occurs at a vertex position j satisfying k−3<=j<=3 (with the usual endpoint truncations). Indeed every consecutive three-face window along the path contains that vertex and has its free directions outside i, so each has color q. In particular for n>=7, arbitrary six-direction orders avoiding i can be rooted to pass through a dead-edge endpoint and yield genuine monochromatic six-edge geodesics.

*Full Section composition: [source manuscript](nori_connector_dead_edge_geometry.md).*

### Dead-edge hub rigidity and forced short monochromatic geodesics

# Dead-edge hub rigidity and forced short monochromatic geodesics

Suppose a physical cube edge is absent from every monochromatic four-edge geodesic. This local failure is surprisingly rigid: the three-face colors around its endpoints become constrained uniformly in free triples avoiding its direction. Those constraints can be exploited to build much longer actual monochromatic paths through either endpoint, and to compare dead edges of different directions.

THEOREM. Let n>=5 and let c be ANY binary coloring of physical ordered three-faces of Q_n. Suppose an i-direction physical cube edge e={z,z xor e_i} is DEAD: no genuine monochromatic four-edge geodesic traverses it. Then the local dead-edge rigidity lemma gives a single bit t such that every physical ordered three-face through z OR z xor e_i whose free-coordinate triple does NOT contain i has color t, irrespective of the order of those three free directions.
Hence, for any integer 3<=k<=min(n-1,6), any k distinct directions p_1,...,p_k outside i, and any hub h in {z,z xor e_i}, there is an ACTUAL directed monochromatic k-edge cube geodesic using exactly this ordered direction list, passing through h at vertex index j with max(0,k-3)<=j<=min(3,k) (choose starting vertex h xor {p_1,...,p_j}). Every consecutive three-direction window of the path contains h, because its index interval [r,r+3] contains j for every r=0,...,k-3; since no free triple contains i, every window has color t. In particular for n>=7 the fixed dead-edge endpoints lie on monochromatic SIX-edge geodesics in arbitrary six directions avoiding i.
DIMENSIONAL COROLLARY. If 5<=n<=7 and an active NORI coloring has ANY dead edge, it has a full antipodal n-edge geodesic with at most ONE ordered-three-face color change. Proof: choose k=n-1 directions excluding the dead direction i. The exhibited (n-1)-edge geodesic is monochromatic. Append its sole unused coordinate i at either end. The resulting full antipodal n-edge path has precisely one added ordered-three-face window, hence at most one color change. Thus any counterexample on Q7 must have every physical cube edge traversed by some actual monochromatic four-edge geodesic. This is not a full Q7 proof, since dead-free colorings need separate treatment.
The six-edge hub mechanism reaches its inherent geometric limit at six: an ordered-three-face geodesic of k>=7 edges has consecutive length-three windows with NO common physical cube vertex, since the shared vertex index intersection is [k-3,3], empty for k>6. Therefore longer paths require genuinely global certificate transport.

THEOREM (UNCONDITIONAL DEAD-DIRECTION UNIQUENESS THROUGH DIMENSION EIGHT). Let c be any active NORI antipodal-reversal-odd binary ordered-three-face coloring of Q_n, 5<=n<=8. Let M be its set of physical cube edges that are traversed by no monochromatic directed four-edge geodesic. If M is nonempty, all its edges are PARALLEL: they have the same coordinate direction.
PROOF for n<=7: Two dead edges in different directions i,j have minimum endpoint distance d in exterior coordinates D=[n] minus {i,j}, and their antipodal partner has minimum endpoint distance |D|-d=n-2-d. The proved dead-edge direction-separation theorem says both distances >=3, which requires n>=8. Thus n<=7 impossible.
PROOF n=8: Here |D|=6 and both distances >=3 force d=3 and n-2-d=3. For two different dead directions i,j at this exterior distance3, choose endpoint hubs z,w matched in their i,j bits. They differ in exactly three exterior directions, so their shared physical ordered three-face FREE in those three directions but omitting i and j has color equal to BOTH local dead-edge hub bits t_i and t_j; hence t_i=t_j. Apply the same reasoning between the fixed i-dead edge and the ANTIPODAL PARTNER of the j-dead edge; its exterior distance is ALSO3. The latter partner has dead hub bit 1-t_j by active antipodal-reversal oddness. Therefore t_i=1-t_j, contradicting t_i=t_j. Hence different dead directions cannot coexist in n=8. QED.
COROLLARY (NO-CLOSURE STRUCTURAL TARGET n<=10). The earlier two-dead-hub splicing theorem proves that any active coloring in n=9 or10 with dead edges in two different directions has a full antipodal geodesic with at most one color change, and indeed n=9 gives a full monochromatic geodesic. Thus in ANY hypothetical counterexample in dimensions 5<=n<=10, if dead edges exist they must ALL share ONE direction. For n=8 this one-direction property is unconditional.
SCOPE. This is a genuine global compatibility condition between antipodal singular hubs, independent of computation. It does not show a full one-switch geodesic when all dead edges are parallel or when no dead edges exist.

THEOREM (SAME-DIRECTION DEAD-HUB SPLICING). Let n>=5 and let an arbitrary binary ordered-three-face coloring of Q_n have two different dead physical edges in the SAME direction i. Choose one endpoint z of the first and one endpoint w of the second with matching i-bit, so their difference set T subset D=[n] without {i} has size d>=1. Let m=n-1. Their dead-edge rigidity bits are t_z,t_w. If d<=3 then t_z=t_w, since a physical ordered three-face containing both hubs and omitting i exists: choose three free directions containing T. More generally if t_z=t_w, d<=4, and d>=n-7 (i.e. m-d<=6), then a MONOCHROMATIC full length-m geodesic inside their common i-facet exists. Append i at one endpoint to obtain a full n-edge antipodal geodesic with AT MOST ONE window color change. Proof: choose an ordered partition D minus T=A disjoint union B with p=|A|<=3 and ell=|B|<=3 (possible iff m-d<=6). Start at x=z xor A, traverse A to reach z at index p, traverse all d directions of T to reach w at index p+d, then traverse B. Among the m-2 consecutive three-face windows, window-start indices k in [p-3,p] contain z and hence have color t_z; those in [p+d-3,p+d] contain w and have color t_w. Since p,ell<=3, these intervals cover both ends; since d<=4, they overlap (d<=3) or are adjacent (d=4), and therefore cover ALL windows. All free triples avoid i, so all are monochromatic t_z=t_w. Appending i creates precisely one additional ordered-three-face window; the complete n-geodesic has at most one color change. QED.
APPLICATION TO ACTIVE NORI ODDNESS AND LOW DIMENSIONS. Under c(bar F,rev pi)=1-c(F,pi), the antipodal mate of a dead i-edge is dead with bit 1-t. The projected dead-edge positions form an antipodally invariant subset S of Q_m, and in any hypothetical counterexample all dead edges share one direction for n<=10 by the earlier different-direction-splice theorems.
(i) n=8, m=7: for any pair of distinct projected dead positions that are NOT antipodal, replace the second by its antipode if needed to obtain distance d=min(d0,7-d0) in {1,2,3}. Rigidity forces equal local bits, and n-7=1, so the mono m-facet splice closes NORI. Therefore any hypothetical Q8 counterexample has EITHER no dead edges OR exactly ONE antipodal orbit of two parallel dead physical edges; |M|<=2.
(ii) n=9,m=8: for two projected dead positions at distance d0 with 2<=d0<=6, if d0=4 choose either position or its antipode so its local color matches the first dead bit (the distance remains 4). Otherwise choose whichever gives d=min(d0,8-d0) in {2,3}; at distance<=3 the rigidity bits necessarily agree. In every case 2<=d<=4 and d>=n-7=2, so the mono m-facet splice closes NORI. Therefore in a hypothetical Q9 counterexample, any two projected dead positions belong either to the SAME antipodal orbit or to orbits at projected distance 1 (equivalently 7). Fix one orbit {a,bar a}. Every other dead orbit must be represented by a neighbor a xor e_j. Two different such neighbors have Hamming distance2 and would force closure, so at most ONE further orbit exists. Consequently all dead edges are parallel and |M|<=4; if |M|=4 their projected positions are exactly {a,bar a,a xor e_j,bar a xor e_j} for one direction j outside i.
(iii) n=10,m=9: any two parallel dead i-edges at projected distance3, or4 with matching dead bits, force grand closure by the same lemma (n-7=3). Other configurations are not covered.
These are unconditional implications of honest physical face color rigidity and exact geodesic splice geometry. They are structural restrictions under a hypothetical counterexample, NOT a full Q8 or Q9 proof when no dead edge exists.

Dead-edge rigidity is therefore a positive path-construction mechanism, not merely a negative certificate. Its local span reaches complete low-dimensional cubes under the stated hypotheses, but higher-dimensional closure still requires a compatible continuation beyond the hub.

### Dead-edge transposition descent and terminal normal forms

# Dead-edge transposition descent and terminal normal forms

Let the switch defect of a full geodesic be the number of changes in its consecutive ordered-three-face color word. At a dead physical edge, swapping adjacent travel directions can change only a controlled set of windows. The resulting local exchange inequalities allow a variational descent in the order/root space while preserving the full geodesic property.

## Bichromatic hub: all mixed-class ordered faces are forced by middle-edge shadow

Let \(n\ge6\) and \(c\) satisfy active NORI antipodal-reversal oddness. Consider the **no-common-edge alternative B** of Item \`nori_center_square_bichromatic_edge_or_antipodally_odd_edge_shadow_20261008\`: no physical cube edge is certified by monochromatic centered four-edge geodesics of **both** colors. Then every certified physical cube edge \(e\) has a unique square-witness color \(\sigma(e)\in\{0,1\}\).

By Item \`nori_antipodal_square_connectedness_forces_bichromatic_connector_hub_20261008\`, some center vertex \(z\) supports centered monochromatic four-geodesics of both colors. Let \(A=A(z)\subset[n]\) consist of cube coordinate directions \(b\) for which the physical edge \(\{z,z\oplus e_b\}\) has square-witness color \(0\), and \(B=B(z)\subset[n]\) those whose edge has witness color \(1\). Both \(|A|\) and \(|B|\) are at least 2, because every connector square involves two distinct middle directions. There is at most one remaining isolated direction by the certified minimum-degree \(n-1\) theorem.

For any ordered triple \((a,b,c)\) of distinct directions, write
\[
h_z(a,b,c)=c(F_z(a,b,c),(a,b,c)),
\]
where \(F_z(a,b,c)\) is the **physical three-face through \(z\)** with those free directions.

**Theorem (mixed-middle rigidity at a bichromatic hub).** Under the above no-common-edge alternative, for every ordered triple \((a,b,c)\) with \(b\in A\cup B\) and at least one of its neighboring directions \(a,c\) in the *opposite* class to \(b\),
\[
\boxed{h_z(a,b,c)=
\begin{cases}
0,&b\in A,\\
1,&b\in B.
\end{cases}}
\tag{1}
\]
Thus every ordered face through a bichromatic hub whose direction triple crosses the two shadow color classes has its color determined **solely by the color of its middle coordinate edge**. This is an honest physical-face identity, not an abstract coloring of permutations. No condition is claimed for a triple entirely within one color class, or for a triple involving the at-most-one isolated direction as the middle coordinate.

**Proof.** If \(b\in A\), \(c\in B\), then no centered four-edge connector with middle pair \(\{b,c\}\) can be monochromatic at \(z\). Such a connector would certify both physical edges in directions \(b,c\) with a common color, contradicting their already distinct singleton colors. For the ordered middle pair \((b,c)\), write
\[
I_a=h_z(a,b,c),\quad O_d=h_z(b,c,d)
\]
for outer directions \(a,d\notin\{b,c\}\). For every \(a\ne d\), \(I_a\ne O_d\). Since \(n-2\ge4\), for any \(a,a'\) choose a \(d\) distinct from both, giving \(I_a=I_{a'}\). Similarly the outgoing \(O_d\) are all equal and opposite the common incoming value. Thus there is a bit \(K_{bc}\) such that
\[
h_z(a,b,c)=K_{bc},\qquad h_z(b,c,d)=1-K_{bc}
\tag{2}
\]
for **every** allowed outer \(a,d\). There is an analogous bit \(K_{cb}\) for the reverse orientation \((c,b)\). Formula (2) holds for every cross pair of \(A,B\), in either order.

Now for \(b\ne b'\in A\), \(c\in B\), evaluate the triple \((b,c,b')\) twice, using the outgoing half of the \((b,c)\) constraint and the incoming half of the \((c,b')\) constraint:
\[
1-K_{bc}=K_{cb'}.
\tag{3}
\]
Likewise for \(c\ne c'\in B\), \(b\in A\), the triple \((c,b,c')\) gives
\[
1-K_{cb}=K_{bc'}.
\tag{4}
\]
Since \(|A|,|B|\ge2\) and \(n\ge6\) with at most one isolated coordinate, **at least one** class has size at least 3. If \(|A|\ge3\), fixing \(c\in B\) and comparing (3) for two distinct \(b,b'\) using a third \(b''\) shows all \(K_{bc}\) are equal as \(b\) varies. Then (3)-(4) show the common value is also independent of \(c\). If \(|B|\ge3\), the symmetric calculation first makes all reverse-oriented \(K_{cb}\) independent of \(c\) and then (3)-(4) make the forward-oriented \(K_{bc}\) constant as well. Thus one bit \(K\) satisfies
\[
K_{bc}=K\quad(b\in A,c\in B),\qquad
K_{cb}=1-K\quad(c\in B,b\in A).
\tag{5}
\]

Choose any existing color-0 connector at \(z\); its two middle directions \(b,b'\) belong to \(A\). Choose **distinct** outer directions \(a,d\in B\), which is possible because \(|B|\ge2\). Equations (2),(5) give
\[
h_z(a,b,b')=K,\qquad h_z(b,b',d)=K.
\]
Hence the centered path with ordered directions \((a,b,b',d)\) is monochromatic of color \(K\) and certifies the same physical middle square \(\{b,b'\}\) already certified in color 0. Alternative B forbids two colors on any physical edge of this square. Therefore \(K=0\), and (5) gives \(K_{cb}=1\).

Finally, take any triple \((a,b,c)\) with the asserted mixed-class adjacency. If \(b\in A,c\in B\), apply the first half of (2) to \((b,c)\) and get \(h_z=K=0\). If \(a\in B,b\in A\), apply the outgoing half of the constraint for \((a,b)\), where \(K_{ab}=1\), and get \(h_z=1-K_{ab}=0\). The cases with \(b\in B\) are symmetric and give 1. This proves (1). \(\square\)

**Consequences and exact research frontier.** A bichromatic hub in shadow alternative B carries a **locally reversal-even middle-coordinate selector** on all mixed-color ordered face triples. (Reversing a mixed triple preserves its middle direction, hence its value in (1).) This is substantial rigidity: the physical face coloring is forced on every triple crossing the two certified direction classes, though the remaining same-class triples can contain genuine defects. Antipodal reversal exchanges the certified 0/1 direction classes at \(\bar z\), so the local rule remains consistent with active global oddness. A possible route to eliminating alternative B is to propagate these mixed-triple identities along certified root moves, using the fact that the underlying physical faces are unchanged when any free direction is toggled. The missing theorem is **coherent propagation of the two direction partitions between different bichromatic hubs**; (1) alone does not imply a common opposite-color square or a full one-change antipodal geodesic.

The statement does not assert all faces depend only on their middle direction; it is precisely restricted to physically witnessed *mixed-class* triples.

THEOREM (ANTIPODAL FOUR-SPACING OF DEAD EDGES). Let n>=5 and let c satisfy the ACTIVE NORI c(bar F,reverse pi)=1-c(F,pi) on ordered physical three-faces of Q_n. Let M be the set of physical cube edges traversed by NO genuinely monochromatic four-edge geodesic. The proved local rigidity theorem says that any TWO dead edges in DISTINCT coordinate directions have physical endpoint-set Hamming distance at least THREE; also M is invariant under cube antipodality.
Fix any FULL directed n-edge antipodal geodesic P(x,p) with physical edges e_1,...,e_n, where each coordinate direction occurs once. Complete it to the simple symmetric 2n-edge belt by following the antipodal translates bar e_1,...,bar e_n in the SAME coordinate order. The dead-edge status of each belt edge is antipodally repeated, so its 2n-bit indicator is (d_1,...,d_n,d_1,...,d_n), where d_k=1 iff e_k is dead.
If two different positions k,l in [n] are both dead, their coordinate directions differ. Write their CYCLIC index distance s=min(|k-l|,n-|k-l|). If s<=3, there are two dead belt edges of distinct directions at cyclic edge-index separation s<=3: choose e_k and e_l if |k-l|=s, or e_l and bar e_k if n-|k-l|=s. On the 2n-edge cube belt the nearest endpoints of these two edges are joined by a segment containing at most s-1<=2 cube edges. Thus their physical endpoint-set Hamming distance is <=2, contradicting the different-direction dead-edge separation theorem. Therefore
  min(|k-l|,n-|k-l|)>=4
for every pair of dead positions k,l.
COROLLARIES. The dead positions form a 4-separated code on the cyclic n-position set, so their number is at most floor(n/4) (for n<8, at most one). This is strictly stronger than the matching-only bound ceil(n/2). When a hypothetical active NORI counterexample in dimensions <=10 has any dead edges, the separately proved mixed-dead-direction extraction theorem forces all dead edges to lie in ONE coordinate direction. Every full antipodal geodesic uses that direction exactly once; hence in a hypothetical counterexample on Q_5,...,Q_10 every full geodesic has AT MOST ONE dead physical edge.
The rule is an all-dimensional COLOR-INDEPENDENT packing fact once dead-edge rigidity and active antipodal reversal are in place. It does not imply the full one-switch conjecture, but it removes complex multi-dead configurations from each root/permutation chamber, narrowing the cyclic-seam and adjacent-swap descent analysis.

THEOREM (SHARP Q8 DEAD-HUB POLARITY BOOTSTRAP). In EVERY binary coloring of the physical ORDERED three-dimensional faces of Q8, with NO antipodal/reversal constraint assumed, if some physical cube edge e_i={z,z xor i} belongs to NO genuinely monochromatic directed four-edge geodesic, then Q8 has a FULL antipodal eight-edge geodesic with AT MOST ONE color change among its six ordered-three-face windows. Consequently any hypothetical active NORI Q8 counterexample is COMPLETELY DEAD-EDGE-FREE. This strengthens the earlier Q8 at-most-one-antipodal-dead-pair obstruction to NO dead edges.
PROOF. The exact dead-edge rigidity theorem assigns one bit t such that EVERY ordered three-face containing z and whose free triple omits i has color t (similarly at z xor i). Set D=[8] minus {i}, |D|=7. Argue by contradiction: suppose EVERY full eight-edge geodesic has at least two window-color changes.
STEP 1 (FORCED ONE-SHELL ANTIPOLARITY). Fix ANY r in D and ordered distinct (a,b,c) in D minus {r}. Let (u,v,w) be the other three directions of D, excluding {r,a,b,c}. Consider the full eight-coordinate order (u,v,w,r,a,b,c,i), starting from x=z xor {u,v,w}, so after the first three moves the path reaches z. Its FIRST FOUR ordered-three-face windows, (u,v,w),(v,w,r),(w,r,a),(r,a,b), ALL contain z, have no free direction i, and are therefore color t. Its FIFTH face window is (a,b,c), through the vertex z xor r; its SIXTH is (b,c,i), of arbitrary color. For the full word (t,t,t,t,X,Y) to have >=2 changes, it is NECESSARY that X=1-t and Y=t. Since r,a,b,c were arbitrary, this forces
  for EVERY r in D and ALL ordered distinct a,b,c in D minus {r}: c(F(z xor r;{a,b,c}),(a,b,c))=1-t.
STEP 2 (SECOND HUB MAKES A GOOD PATH). Choose distinct r,s in D. Choose any six directions q1,...,q6 giving an order of D minus {r}, with q4=s; write q5=a,q6=b. Put y=z xor r, and start a directed full eight-edge path at y xor {q1,q2,q3} using order (q1,q2,q3,s,a,b,r,i). Its first SIX edges are centered at y after three moves, and their FIRST FOUR ordered-three-face windows are all through y and omit r and i, so by the one-shell polarity from Step1 they have color 1-t. Its FIFTH ordered window has directions (a,b,r) and is a physical face through the vertex y xor s=z xor {r,s}. Because r is a FREE coordinate of this window, the same physical face contains z xor s. Its ordered free triple (a,b,r) excludes i and s, so Step1 with hub z xor s says its color is ALSO 1-t. The SIXTH, final window has arbitrary color. Therefore the full eight-edge antipodal geodesic has window word (1-t,1-t,1-t,1-t,1-t,Y), with at most ONE color change, contradiction. QED.
GEOMETRIC MECHANISM. A dead-edge hub yields a monochromatic star on all ordered faces avoiding its direction. Failure of one-switch closure forces the next outer coordinate shell to have COMPLEMENTARY uniform color on triples not containing the shell direction. This forced shell is itself rich enough to produce a new monochromatic six-edge hub geodesic whose first extension window is physically IDENTICAL to a face on a neighboring shell hub, contradicting the putative necessary color flip. The proof is fully face-geometric and does not use numerical enumeration or the active NORI parity condition.
SCOPE. It leaves arbitrary DEAD-FREE ordered-three-face colorings of Q8 unresolved by this argument. In dimensions larger than 8, six-window hub propagation leaves more than two uncontrolled tail windows and requires an additional memory-boundary forcing lemma.

The descent yields a terminal normal form and sharp constraints on its remaining caps. It does not by itself force zero or one switch in every dimension; the residual plateau requires an additional cross-root or cap comparison.

### Dead-hub facet lifting and live-edge completion constraints

# Dead-hub facet lifting and live-edge completion constraints

A monochromatic hub certificate occupying a bounded set of directions can be embedded in a larger cube facet. For each such lifting one must preserve actual exterior-coordinate bits and the order of the newly created windows at the facet boundary. The following results quantify the dimension-dependent strength of dead-edge hub lifting and show how live parallel-edge completion interacts with antipodal parity.

THEOREM (FACET-LOCAL VERSION OF Q8 POLARITY BOOTSTRAP). Let n>=8 and c be ANY binary coloring of physical ORDERED three-faces of Q_n. Suppose a physical edge e_i is DEAD, meaning no monochromatic directed four-edge cube geodesic traverses it. Then for EVERY physical 8-dimensional coordinate face H of Q_n that contains e_i, the restricted coloring on ordered physical three-faces of H admits a FULL eight-edge antipodal H-geodesic with AT MOST ONE ordered-window color change. Reason: a dead edge globally remains dead in the restricted 8-face, and the independent Q8 polarity-bootstrap theorem applies to every binary ordered face coloring, with no antipodal oddness required. Thus this is a UNIFORM RANK-EIGHT REACHABILITY SEED around EVERY dead edge, in arbitrary ambient dimensions.
COROLLARY (SHARPENED FULL GLOBAL SWITCH BOUND CONDITIONAL ON ONE DEAD EDGE). For every n>=8, an arbitrary binary ordered-three-face coloring having a dead edge admits a FULL n-edge antipodal Q_n geodesic with at most n-7 color changes. Proof: choose any H as above, its good eight-edge geodesic P has six ordered-three-face windows and <=1 change. Append the n-8 unused coordinate directions in any order. The full n-edge path has n-2 windows, thus n-8 additional window colors; each extension adds at most one change, yielding D<=1+(n-8)=n-7. In particular n=8 closes with <=1, n=9 yields <=2, n=10 <=3, and beyond n>=8 this improves the earlier single-dead-edge n-6 bound by one. The endpoint inside H is its H-antipode, so appending each unused direction produces a genuine full antipodal cube geodesic.
LIMITATION. An 8-dimensional face good path is not necessarily MONOCHROMATIC, and the additional coordinates can generate new switches. Exact extraction to one switch in unrestricted n>8 still requires compatible extensions or multi-face topological forcing. No claim is made that an arbitrary face avoiding a dead edge has the rank-eight guarantee.

THEOREM (FULLY REALIZABLE TOPOLOGICAL CONNECTIVITY NO-GO, ALL n>=9). For each n>=9 there exists an ACTIVE NORI binary coloring of PHYSICAL ordered three-dimensional faces of Q_n obeying c(bar F,rev pi)=1-c(F,pi) such that for a fixed physical cube direction i, the projected graph L_i of i-parallel edges traversed by some GENUINE monochromatic four-edge geodesic is DISCONNECTED. More precisely, L_i has a connected component which is exactly a projected TWO-DIMENSIONAL CUBE SQUARE: four i-parallel physical edges, each with exactly two live projected neighbors, all outside neighbors dead. It also has at least one distinct live projected edge outside that square, and its antipodal mirror contains another isolated live square. Thus antipodal symmetry, physical face consistency, and the actual monochromatic four-path certificates DO NOT force each coordinatewise live-position carrier to be connected. This is NOT a NORI grand counterexample.
EXPLICIT CONSTRUCTION. Number directions i=0, a=1,b=2, and put E={3,...,n-1}, of size r=n-3>=6. Project along i onto Q_(n-1). Let C be the 2-dimensional square of positions with E-bits all zero and arbitrary a,b bits, namely C={0,e_a,e_b,e_a+e_b}. Define the lower OUTER BOUNDARY B={v xor e_j:v in C,j in E}; this has 4r projected positions with exactly one E-bit1. Let bar B be its projected antipodal complement, having exactly r-1 E-bits1. Prescribe every i-parallel edge at positions in B to be DEAD with rigidity bit t=0, and every antipodal mate at positions in bar B to be DEAD with bit t=1. To realize this, at both physical endpoint hubs of EACH such edge prescribe EVERY physical ordered three-face color by the exact local dead-edge template: color t if i is absent or in the middle of its ordered free triple, and color 1-t if i occupies either end.
PRESCRIPTION CONSISTENCY. Within B all prescriptions have the SAME rigidity bit; within bar B they have complementary bit. Between B and bar B, projected E-coordinate Hamming distance is at least (r-1)-1=r-2>=4, so no physical ordered 3-face can contain hubs from BOTH groups: a 3-face changes at most3 projected coordinates if i is absent, and at most2 if i is free. Antipodal reversal interchanges B with bar B and complements all template colors (middle stays middle, end swaps with end, absent remains absent). Thus the prescribed partial colors are mutually consistent and active-NORI compatible. Extend to all remaining ordered three-face involution orbits arbitrarily, assigning each mate its complementary bit. Every B/bar B i-edge is genuinely DEAD, since the local color template makes every four-edge geodesic through that edge bichromatic.
FORCE THE CENTRAL SQUARE LIVE. The physical ordered 3-face whose free triple is (a,i,b) and whose fixed E-bits are ALL ZERO is untouched by the dead templates; assign it color1. (Its antipodal-reversed mate with free order (b,i,a) and all E-bits one automatically gets color0.) For EACH projected v in C, consider the genuine four-edge geodesic with direction order (a,i,b,3), rooted at the physical cube vertex having E-bits zero and projected a,b position v xor e_a (with i-bit0). Its first ordered three-face (a,i,b) is the newly assigned color1. Its second ordered three-face (i,b,3) includes the hub at projected v xor e_3 in B, so dead template t=0 forces color1 (i in FIRST position). Hence this honest directed four-step geodesic is monochromatic color1 and traverses the physical i-edge at v. ALL FOUR vertices v of C therefore lie in L_i. Every projected neighbor of C outside C is in B and DEAD, so C is a WHOLE CONNECTED COMPONENT of Q_(n-1)[L_i], a genuine live square. Its antipodal square bar C is likewise fully live by the active NORI involution, and separated from C since r>=6.
AN OUTSIDE LIVE EDGE (independent verification). Put w=e_3+e_4+e_5 in the projected cube (physical bits in directions 3,4,5). The physical ordered 3-face with free order (i,4,6) through the hub at w is untouched by the boundary templates: its projected E-bit weight ranges between2 and4 as the two free exterior directions4,6 vary, while B has weight1 and bar B has weight r-1>=5. Assign this face color0, with its antipodal-reversed mate complementary. The four-edge geodesic rooted at physical position w xor e_3, with direction word (3,i,4,6), traverses the i-edge at w: its first ordered 3-face (3,i,4) contains the low dead projected hub e_5∈B, forcing color0 since i is MIDDLE; its second ordered 3-face (i,4,6) is the explicitly assigned color0. Thus the path is genuinely monochromatic0, so w∈L_i, while w lies outside C and bar C. No conflicting prescription occurs. This makes the disconnection explicit even without appealing to antipodal symmetry.
CONSEQUENCES. The projected live-edge carrier L_i need not be connected, even though its graph has unconditional minimum degree >=2 (proved separately). Thus a fixed-root permutohedral or cubical fixed-point proof cannot assume coordinatewise four-window reachability sheets are connected purely from NORI oddness and local certificate coverage. One must use higher memory, a compatible long-path nerve, or a stronger relative connector theorem. The construction is a REAL VALID active NORI coloring, but its existence says nothing against the grand <=1-switch conjecture (it may have many good full geodesics).

THEOREM (EXACT TWO-COORDINATE TUCKER EXTRACTION FROM PHYSICAL NORI CERTIFICATES). For every active NORI coloring c of Q_n (n>=5) and every coordinate direction i, let L_i be the positions of i-parallel physical edges traversed by a genuinely monochromatic directed four-edge geodesic. Let X_i be the Freudenthal simplicial LIVE subcomplex of the antipodal projected three-skeleton ∂[0,1]^(n-1) built in theorem nori_dead_live_projected_three_skeleton_tucker_index_two_20261008. This is a FREE antipodal simplicial complex with w1(X_i/τ)^2 !=0.
For each projected live vertex v, choose one ACTUAL directed monochromatic four-edge path P_v that traverses the physical i-edge at v. Do so τ-EQUIVARIANTLY on antipodal v-pairs: choose an arbitrary P_v for one representative, and define P_(bar v)=ΘP_v, the physical antipodally complemented path with REVERSED direction order and complemented window color. Record its genuine color q(v)∈{0,1}, and traversal role r(v)∈{1,2,3,4} of coordinate i in its four-edge ordered word. The antipodal rule gives q(bar v)=1−q(v), r(bar v)=5−r(v).
Define a TWO-ABSOLUTE-VALUE signed Tucker label λ(v)∈{±1,±2} by λ(v)=(-1)^(q(v)) * h(r(v)), with h(r)=1 for r∈{1,4} (OUTER/EXTREME traversal) and h(r)=2 for r∈{2,3} (MIDDLE traversal, which certifies the physical middle square containing the i-edge). Then λ(bar v)=−λ(v).
THEOREM CONCLUSION. There are two DIFFERENT ACTUAL LIVE projected vertices v,w that lie in one common physical projected cube face of dimension≤3, and their selected real four-path witnesses P_v,P_w have OPPOSITE monochromatic colors q(v)!=q(w) but matching centrality h(r(v))=h(r(w)). In particular d_H(v,w)<=3. More precisely, either BOTH witnesses traverse their respective i-edges as a middle (second or third) edge and hence BOTH i-edges have genuine monochromatic CENTER-SQUARE certificates in opposite colors, or BOTH witness edges occur as outer (first or fourth) steps. The forced pair depends on the equivariant selection, but the existence holds for EVERY such choice.
PROOF. Suppose NO simplex edge of X_i joins complementary signed λ-labels. Send each vertex with label +j to e_j∈R² and each label −j to −e_j, and extend linearly over every Freudenthal simplex of X_i. Since no simplex contains ±e_j simultaneously, every simplex maps into a face of the crosspolytope boundary not containing zero; equivalently each coordinate has at most one appearing sign, so 0 is not in the affine convex hull. Normalizing gives an antipodally equivariant continuous map X_i→S¹. But such a map would annihilate the square of w1(X_i/τ), whereas the previously proved live-carrier theorem has w1² !=0. Contradiction. Therefore a complementary-label edge exists. Its endpoints are real live positions in one 3-face; equality of |λ| and opposition of signs give matching traversal class and opposite actual mono4 colors.
LIMITATION. The two true four-edge witnesses may have different ordered middle pairs and different starting roots; their physical i-edges merely lie within a common projected 3-face. An antipodally valid TuckER pair is not yet the SAME-root complementary reversed-terminal-tail witness required for NORI grand closure. The theorem replaces virtual sign-neutrality by a genuine bounded-distance, equal-memory-class, opposite-color certificate pair, which is a concrete target for a four-face local repair theorem.

Facet-level success is not synonymous with full-dimensional success. Where the local bounds leave more than one switch, exact exterior-bit and terminal-memory conditions remain an explicit obligation.

## Root hubs, midpoint witnesses and terminal caps

A bichromatic hub supports genuine short monochromatic cube geodesics of both colors. The surviving manuscripts quantify certified two-color six-edge connections and describe explicit splicing at real midpoint vertices with the two ordered seam windows tracked separately. The four-way splice calculation is exact for a common physical midpoint and complementary travel-direction supports; whether some combination has the required colors is an additional mathematical question.

The extensive obstruction theory for incompatible opposite-color terminal caps and same-root reversed-tail diamonds is now preserved in a research note. That methodological failure does not invalidate the constructive hub lemmas, nor does it supply a global full-path theorem.

*Full Section composition: [source manuscript](nori_connector_root_hubs.md).*

### Bichromatic six-move hubs and two-color connector density

# Bichromatic six-move hubs and two-color connector density

A vertex supporting monochromatic four-geodesics in both colors is a bichromatic hub. Its incoming and outgoing directions support many genuine six-edge paths that are at most one switch away from monochromaticity. Quantifying those paths reveals forced root packets and separators under the additional hypothesis that no physical edge is certified in both colors.

## The unrestricted NORI root-chart gap has TWO logically independent missing obligations

The proved nonlinear fault robustness theorem nori_quadratic_nonlinear_triple_fault_robust_antipodal_chart_closure_20261008 is substantial, but DOES NOT itself approach arbitrary NORI through chart connectivity alone. Its exact proof requires TWO separate parity-reference features, both unavailable for an arbitrary active ordered-three-face coloring:

**(I) PREFIX POLARIZATION / SUFFIX FORCING.** Fix an ordered list p of outside directions D=[n]\K and a root x where its D-prefix is monochromatic. To force the three exceptional terminal windows to ALTERNATE under hypothetical grand failure, the proof flips ONE K-coordinate s_1 which is free in each of the last three windows, hence does not change their actual physical ordered-face colors. What is ALSO necessary is that this same bit flip sends ALL preceding D-only window colors from q to 1−q, keeping the preceding block monochromatic. Full exterior parity supplies precisely this property: each early face has s_1 as an exterior coordinate, so toggling its root bit flips every early color. An arbitrary NORI coloring need not have this property. NORI oddness only relates (F,π) to (bar F,rev π), not two D-only faces differing in a SINGLE outside K-bit at the same orientation.

**(II) ANTIPODAL CHART CONNECTIVITY.** Even if a root-specific antipodally odd suffix bit t(S) is successfully manufactured, to contradict it one needs a chain of ACTUAL monochromatic-prefix reachability witnesses whose first exceptional physical ordered faces agree and whose roots connect S to bar S. The clean parity baseline gives the six-periodic root code S_{p_{j+3}}=1−S_{p_j}, whose middle-layer chart graph has this connectivity. For arbitrary c, the set of monochromatically reachable prefixes and their physical face incidence may be sparse, disconnected, or lack this root-coupled structure. Connectedness of the separate physical certified-four-square complex does NOT automatically imply connectivity of a terminal-memory-compatible root chart.

**THEOREM (safe abstract two-obligation NORI extraction).** Fix K of size3, D its complement. Suppose a collection \mathscr P of D-direction geodesic witnesses possesses all the following genuine properties:
(a) For every outside root S in a set G invariant under complementation, there is a selected D-order p and K-root assignment with a monochromatic D-prefix, and for EACH of the 6 orders of K the corresponding first three exceptional windows refer to the actual physical colored faces.
(b) Each selected D-order witness is **polarized**: there exist two K-root choices yielding identical actual exceptional three-window colors but opposite uniform monochromatic prefix bits. Consequently under no full good geodesic the last three exceptional windows have at least2 internal changes, hence alternate.
(c) The six-order/reversal physical-face comparisons align these alternating suffixes into one well-defined label t:G→F2, independent of selected p, with t(bar S)=1−t(S).
(d) The graph on G linking selected root witnesses with IDENTICAL actual first exceptional physical ordered faces has a component containing S and bar S.
Then the full NORI one-switch conclusion follows.

**Proof.** Under no full good path, (b) forces the alternating suffix for each selected witness by comparing opposite prefix colors against the SAME suffix. Conditions (c) and (d) make t locally constant along a certified chain from S to bar S, while antipodal oddness makes it complementary at the two endpoints. Contradiction. QED.

**CAUTION.** The theorem is a modular, CONDITIONAL extraction theorem. Conditions (b) and (c) are NOT inherent to arbitrary monochromatic-prefix reachability and must be genuinely proved from each new construction; condition (d) is a separate topological forcing obligation. Simply declaring an uncolored reachability set R(x), an antipodal involution, or a connected lower-dimensional certified square complex does NOT discharge either obligation. An alternative global strategy is to target the already proved EXACT color-free reversed-two-tail complementary-support intersection, which bypasses the need for these polarization hypotheses entirely and automatically splices a full one-switch path.

**Main direction after latest robust closure.** Seek a topological connector theorem on actual reversed-terminal-memory reachability basins that forces complementary supports, rather than extrapolating the reference-dependent parity-root synchronization to unrestricted face colors.

## Every bichromatic hub has a local common-edge or uniform-cap alternative

Let \(n\ge6\) and let \(c\) satisfy the active NORI physical ordered-three-face axiom \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\). Let \(X_c\) be the genuine certified-middle-square complex of NORI. At a cube vertex \(z\), let \(K_z(i)\subseteq\{0,1\}\) be the set of colors \(q\) of actual centered monochromatic four-edge connectors whose middle-pair square contains the **incident physical cube edge** \(\{z,z\oplus e_i\}\). Every incident certified square carries the same certificate color at each of its four vertices; by the centered-link theorem all but at most one \(K_z(i)\) are nonempty.

Call \(z\) **bichromatic** if \(\bigcup_i K_z(i)=\{0,1\}\). Every valid active NORI coloring has at least one bichromatic \(z\), by the proved connected-certified-square topological overlap theorem.

**Theorem (local hub dichotomy, without any global shadow restriction).** For **every** bichromatic \(z\), one of the following alternatives holds.

**(I) A local color-overlap edge.** There exists a direction \(i\) such that \(K_z(i)=\{0,1\}\). This is an actual physical edge at \(z\), lying in two genuine centered monochromatic-connector squares of opposite colors.

**(II) A locally rigid two-color direction partition.** All nonempty \(K_z(i)\) are singleton sets. Put
\[
A_z=\{i:K_z(i)=\{0\}\},\quad B_z=\{i:K_z(i)=\{1\}\}.
\]
Then \(|A_z|,|B_z|\ge2\), \(|A_z|+|B_z|\ge n-1\), and for **every** actual ordered three-face through \(z\) with distinct ordered free directions \((u,v,w)\), when \(v\in A_z\cup B_z\) and one of \(u,w\) belongs to the opposite class,
\[
\boxed{c(F_z(\{u,v,w\}),(u,v,w))=\mathbf1_{\{v\in B_z\}}.}
\tag{1}
\]
In particular, for every mixed omission \(a\in A_z,\ b\in B_z\), every \(i\notin\{a,b\}\), and every choice of the omitted two starting bits above the projected \(U\)-root \(r=z|_U\), \(U=[n]\setminus\{a,b\}\), the actual cap labels are **uniform**:
\[
\boxed{c(F(x;\{a,b,i\}),(a,b,i))=1,\quad
c(F(x;\{a,b,i\}),(b,a,i))=0.}
\tag{2}
\]
Consequently, **a single monochromatic \(U\)-spanning geodesic from any of those four parallel-facet roots directly yields a full NORI geodesic with at most one color change**. Under hypothetical grand failure, all \(4|A_z||B_z|\) such root/bundle choices are free of any monochromatic \(U\)-spanning geodesic, with at least \(2(n-3)\) distinct forbidden mixed omission pairs.

**Proof.** If (I) is false, the sets \(A_z,B_z\) are disjoint. Each of the two certified monochromatic four-path colors at \(z\) certifies a physical square and hence at least two distinct incident coordinate directions; thus both classes have size at least two. At most one direction is isolated by the established \(n-1\) certified-degree theorem, giving \(|A_z|+|B_z|\ge n-1\). Every cross middle pair \(v\in A_z,w\in B_z\) is **uncertified at \(z\)**: any monochromatic middle-square certificate of color \(q\) would place the same bit in both already oppositely certified edge-label sets \(K_z(v)=\{0\}\) and \(K_z(w)=\{1\}\).

For a fixed ordered cross pair \((v,w)\), write \(I_t=c(F_z(\{t,v,w\}),(t,v,w))\), \(O_s=c(F_z(\{v,w,s\}),(v,w,s))\) for distinct outer \(t,s\notin\{v,w\}\). Since every centered four-path \((t,v,w,s)\), \(t\ne s\), is nonmonochromatic, \(I_t\ne O_s\). At least three outer coordinates exist since \(n\ge6\); comparing values using a common third outer direction forces every \(I_t\) to equal one bit \(K_{vw}\) and every \(O_s=1-K_{vw}\). Repeating this for the reverse cross orientation gives \(K_{wv}\). Shared physical ordered-face triples with two \(A_z\) and one \(B_z\), or vice versa, yield exactly the compatibility equations
\[
K_{wv'}=1-K_{vw}\quad(v,v'\in A_z,\ w\in B_z,\ v\ne v'),
\]
\[
K_{v w'}=1-K_{wv}\quad(w,w'\in B_z,\ v\in A_z,\ w\ne w').
\]
Since both classes have size at least two and at least one has at least three, elementary elimination of these equations gives a common bit \(K\) on all \(A\to B\) cross pairs and bit \(1-K\) on all \(B\to A\) cross pairs. Choose a genuine color-0 certified middle square at \(z\) with middle pair \(v,v'\in A_z\). Choose distinct outer \(w,w'\in B_z\). The ordered four-path \((w,v,v',w')\) has both window colors \(K\) by the cross-pair constraints, so it is a monochromatic certificate of color \(K\) on the SAME physical square that was already certified color 0. Since (I) is false, \(K=0\). The resulting incoming/outgoing cross-triple formulas yield (1), by whether the middle coordinate is in \(A_z\) or \(B_z\).

For \(a\in A_z,b\in B_z\), the ordered cap triples \((a,b,i)\), \((b,a,i)\) have their middle direction respectively in \(B_z\), \(A_z\), and an opposite-class adjacent direction. Thus their colors at \(z\) are 1 and 0. The physical face has both \(a,b\) free, so varying those two bits does not alter its identity, proving (2) simultaneously in all four parallel facets.

If \(P\) is a monochromatic full \(U\)-geodesic from one such facet root, color \(q=0\), prepend \((a,b)\) starting at the appropriately shifted full root. The new first cap has color 1 and the first original face color is 0; the one intermediate new window has arbitrary color, so the resulting full word has exactly one change. If \(q=1\), append \((b,a)\), whose final cap is \(1-c(F(x;\{a,b,j\}),(a,b,j))=0\) by the active antipodal-reversal law, and again there is exactly one change regardless of the intermediate color. Thus either monochromatic \(P\) forces grand closure.

Finally if \(|A_z|=p, |B_z|=q\), \(p,q\ge2\), \(p+q\ge n-1\), then \(pq\ge2(n-3)\). This counts distinct mixed omission pairs. \(\square\)

**Strength over earlier results.** Previously the mixed-direction selector theorem and uniform-cap blockade were stated inside global square-edge shadow alternative B, where *no* physical edge anywhere in the cube has both certification colors. The proofs actually use only **lack of a doubly certified incident edge at the chosen bichromatic center**. This local theorem therefore applies even in colorings where alternative A occurs elsewhere. It supplies a site-by-site topological obstruction to combine with genuine opposite-color edge overlaps, without an artificial global case split.

**Remaining closure obligation.** The theorem does not guarantee a monochromatic near-spanning \(U\)-geodesic for any prescribed projected root. To prove full NORI, one would need a fixed-point/connector principle forcing, for some bichromatic hub, either (I) an opposite-color common-edge configuration whose witnesses can be extended compatibly, or (II) one of the many forbidden near-spanning monochromatic cores. An opposite-color shared edge alone is also not yet a full-geodesic certificate. The new statement is exact and dimension independent, not grand closure.

## Topological global consequence: monochromatic six-geodesic hubs meet every certified antipodal path in the unique-color edge-shadow regime

Let n>=10 and let c be an ACTIVE NORI binary coloring of physical ordered three-faces. Assume the GLOBAL unique-color certified-square edge-shadow case B: no physical cube edge receives square certificates from monochromatic centered four-edge connectors of both colors. Let X_c be the genuine certified-center-square complex, let G_c=X_c^(1) be its spanning cube subgraph, and write M=E(Q_n)\E(G_c). By proved NORI theorems, M is an antipodally invariant matching, G_c is connected, and every vertex has certified-center degree at least n−1. Define the bichromatic hub set
\[
B=\{z: \text{genuine centered monochromatic four-edge connectors of BOTH colors exist at z}\},
\]
and the MONOCHROMATIC SIX-HUB set
\[
H_6=\{z: \text{there exists an ACTUAL monochromatic six-edge cube geodesic with ALL FOUR ordered-three-face windows physically containing z}\}.
\]

**THEOREM 1 (unavoidable monochromatic six-hub separator).** Under the stated assumptions,
\[
\boxed{B\subseteq H_6.}
\]
Moreover every G_c-graph path from any cube vertex x to its antipode bar x intersects H_6. In particular, for EVERY root x∈Q_n there exists a FULL antipodal n-edge cube geodesic from x to bar x (whose edges all belong to G_c) that passes through at least ONE vertex z∈H_6.

**Proof.** At each bichromatic hub z, the no-common-edge assumption splits the incident certified directions into two classes A,B, each of size at least2, of total size at least n−1. Since n>=10, the larger class has cardinality at least5. The proved five-majority odd-cycle theorem (Item nori_majority_five_bichromatic_hub_odd_cycle_forces_monochromatic_six_20261008) constructs a genuine monochromatic six-edge geodesic through z. Thus B⊆H_6.

The separate, unconditional bichromatic-hub antipodal separator theorem (Item nori_bichromatic_mono_four_hubs_hit_every_certified_antipodal_path_density_20261008) states that EVERY G_c-path from x to bar x meets B, since physical square certificates share a common monochromatic color across each G_c-edge, but the hub singleton color label flips under antipodality. Such a path consequently meets H_6.

Finally the general cube matching-avoidance theorem (Item nori_matching_avoidance_every_root_full_geodesic_20261008) says any cube matching that is NOT the entire set of parallel edges of one coordinate can be avoided by SOME full antipodal geodesic from ANY prescribed root x. Our matching M cannot be that entire parallel matching because G_c is CONNECTED and would otherwise split into opposite coordinate facets. Therefore from every x there is a full M-avoiding geodesic P(x), which is a G_c-path. It meets H_6. QED.

**THEOREM 2 (quantitative density of monochromatic six-hubs).** The same model satisfies
\[
\boxed{|H_6|\ge |B|\ge
\frac{2^n-2|M|}{n+1}.}
\]
Both hub sets are antipodally invariant. In the special case M=∅, at least a fraction 1/(n+1) of all Q_n vertices are centers of GENUINE monochromatic six-edge geodesics:
\[
|H_6|\ge 2^n/(n+1).
\]

**Proof.** Apply B⊆H_6 to the existing quantitative bichromatic-hub separator bound. Global antipodal reversal carries every monochromatic six-edge path through z to a complementary-color monochromatic six-edge path through bar z; hence H_6 is antipodally invariant. QED.

**Conceptual topological result.** This produces, in one structural branch of arbitrary ACTIVE NORI colorings, a physical Q_n antipodal hitting set of ACTUAL SIX-edge monochromatic paths. Its strength is global and root-mobile: the center of such a path is encountered by a fully spanning antipodal route from EVERY starting cube root, but the mono-six direction word may not match the route's entering/leaving used-direction support, and the route's unrelated local certificates need not share the mono-six color. The unproved GRAND-EXTRACTION step is to synchronize at least one of these mono-six hubs with a full legal root/terminal-memory geodesic so that its entire ordered-three-face word has <=1 switch. This theorem does not assert such synchronization.

Hub abundance is a robust local theorem. Extending those six-move witnesses to a full n-move geodesic without accumulating extra window defects is the outstanding global problem.

### Near-midpoint hub witnesses and concrete splice-failure tests

# Near-midpoint hub witnesses and concrete splice-failure tests

High-index permutation arguments force authentic endpoint-opposed geodesics and central physical-face interactions near the midpoint of the cube. The core question is whether such witnesses can be cut and reassembled along a common actual vertex without creating too many new window-color changes. The local connector calculations below keep all four possible splices, not just an abstract sign coincidence.

## A genuine two-seam splicing law at a common physical hub; locally rigid bichromatic hubs automatically repair both seams

Let n>=6, and let c be ANY binary coloring of physical ORDERED three-faces of Q_n. Let P and Q be two genuine full directed antipodal cube geodesics rooted at SAME physical vertex x, with direction words
\[
P=(a_1,\ldots,a_\ell,b_1,\ldots,b_{n-\ell}),\qquad
Q=(a'_1,\ldots,a'_\ell,b'_1,\ldots,b'_{n-\ell}),
\]
for some 3<=ell<=n-3, and suppose their first-ell used-direction sets coincide:
\[
\{a_1,\ldots,a_\ell\}=\{a'_1,\ldots,a'_\ell\}=S.
\]
Thus BOTH pass at time ell through the SAME physical cube vertex y=x⊕S. ALL FOUR paths obtained by choosing either prefix and either suffix are genuine full antipodal geodesics, because the first block uses S and second block uses its coordinate complement.

**THEOREM 1 (exact physical two-window splice).** Given any prefix A with last directions (u,v) and any suffix B with first directions (w,t), the ordered-three-face color word of their full splice A B is
\[
\boxed{\operatorname{Int}_3(A),\
c(F(y;\{u,v,w\}),(u,v,w)),\
c(F(y;\{v,w,t\}),(v,w,t)),\
\operatorname{Int}_3(B).}
\]
Here \operatorname{Int}_3(A) is the actual color word of the ell-2 ordered three-face windows entirely inside A, and \operatorname{Int}_3(B) is the actual color word of the n-ell-2 windows entirely inside B, preserving each branch's physical face identities. In particular BOTH NEW splice windows are actual ordered physical three-faces THROUGH THE SAME PHYSICAL INTERMEDIATE VERTEX y; they are not virtual/interpolated colors.

**Proof.** All windows wholly before/after the cut preserve precisely the same physical exterior bits, because both choices of prefix reach the same y. There are exactly two crossing windows of ordered directions (u,v,w) and (v,w,t). Their physical first vertices lie respectively at y⊕u⊕v and y⊕v, so each corresponding free-face contains y. This is the displayed formula. QED.

**THEOREM 2 (automatic seam compatibility at a locally rigid bichromatic hub).** Assume additionally that y is a bichromatic hub in the LOCAL UNIQUE-CERTIFIED-COLOR case of Item nori_every_bichromatic_hub_local_shared_edge_or_uniform_mixed_cap_dichotomy_20261008. Let A_y,B_y be its genuine certified incident direction color classes, with assigned bits h(i)∈{0,1}. Suppose the LAST prefix direction v belongs to A_y∪B_y, the FIRST suffix direction w belongs to A_y∪B_y, and their certified bits differ:
\[
h(v)\ne h(w).
\]
Then regardless of the neighboring directions u,t, the two actual crossing window colors are
\[
\boxed{c(F(y;\{u,v,w\}),(u,v,w))=h(v),\quad
c(F(y;\{v,w,t\}),(v,w,t))=h(w).}
\]
This follows DIRECTLY from the proved local mixed-middle selector at y: in each ordered triple, the MIDDLE direction has a neighboring free direction in the opposite certified color class.

**COROLLARY 3 (actual full one-switch extraction from compatible monochromatic branches).** Under Theorem2, suppose A is a genuinely MONOCHROMATIC ell-edge geodesic from x to y of ordered-window color h(v), and B is a genuinely MONOCHROMATIC (n−ell)-edge geodesic from y to bar x of ordered-window color h(w). Then their full concatenation P=A B is a full antipodal directed geodesic with ordered-face window-color word
\[
h(v)^{\ell-1}\ h(w)^{n-\ell-1},
\]
and hence has EXACTLY ONE change. It works regardless of the direction order in the rest of A or B.

**COROLLARY 4 (exact additive defect formula for nonmonochromatic branches).** Under Theorem2, suppose the LAST internal ordered window of A has color h(v), and the FIRST internal ordered window of B has color h(w), but their other windows may change. Let d_A,d_B be the number of changes in their respective internal window-color words. Then the full spliced word has
\[
\boxed{D(A B)=d_A+d_B+1.}
\]
Indeed the two new splice windows match their adjacent internal side colors and differ exactly once from one another. Thus local hub certification supplies a ZERO-EXCESS connector: there are NO uncontrolled seam changes. In particular, if d_A=d_B=0, grand closure is immediate.

**RELATION TO THE TOPOLOGICAL TUCKER PAIR.** Item nori_odd_dimension_permutohedral_tucker_common_vertex_opposite_mirror_switch_pair_20261008 proves unconditionally, in EVERY odd n>=7 and at EVERY root x, TWO actual endpoint-opposed full paths P,Q sharing some proper interior vertex y and carrying opposite mirrored switch labels. Theorem1 now turns this topologically forced common vertex into an ACTUAL two-seam geodesic rectangle, with both seam colors lying in physical faces through y. If y is a locally rigid bichromatic hub and the boundary directions of one of the four splice combinations cross the certified A_y/B_y cut with matching adjacent window colors, then Corollaries3-4 give exact switch-controlled extraction/defect bookkeeping. Such additional properties of y or the splice do not follow automatically from the Tucker pair theorem and remain the outstanding GLOBAL COMBINATORIAL task.

**Scope.** Theorem1 uses no NORI antipodal law; Theorem2 uses physical hub rigidity proved under ACTIVE NORI. The topological pairing and the one-switch extraction are both rigorous but their unconditional conjunction is NOT proved. No claim of unrestricted grand closure is made.

## Kneser forces a same-root, same-center, two-sided reversal square of genuine six-edge geodesics

Let n>=8 and let c be ANY binary coloring of actual physical ORDERED 3-faces of Q_n, not necessarily satisfying antipodal oddness. Fix ANY physical cube vertex z. For each ordered triple alpha=(a,b,c) of distinct direction names, define h_z(alpha) to be the physical color of the ordered 3-face through z with ordered free directions alpha.

**Theorem (unconditional centered six-edge two-sided reversal square).** There exist DISJOINT unordered direction triples A,B with ordered orientations alpha=(a1,a2,a3) on A and gamma=(b1,b2,b3) on B, and two bits q,r∈{0,1}, such that
\[
h_z(\alpha)=h_z(\operatorname{rev}\gamma)=q,\qquad
h_z(\operatorname{rev}\alpha)=h_z(\gamma)=r.
\tag{1}
\]
Consequently from the ONE SAME ROOT x=z XOR A to the ONE SAME ENDPOINT y=z XOR B there exist FOUR ACTUAL six-edge direction-distinct geodesics:
\[
P_{00}=(\alpha,\operatorname{rev}\gamma),\quad
P_{01}=(\alpha,\gamma),\quad
P_{10}=(\operatorname{rev}\alpha,\operatorname{rev}\gamma),\quad
P_{11}=(\operatorname{rev}\alpha,\gamma).
\tag{2}
\]
All four traverse the SAME physical hub z at their midpoint after three moves, and ALL FOUR physical ordered-three-face window faces of EVERY path contain z. Their initial/final ordered-window color pairs are the complete two-by-two table
\[
\begin{array}{c|cc}
 &\operatorname{rev}\gamma&\gamma\\
\hline
\alpha&(q,q)&(q,r)\\
\operatorname{rev}\alpha&(r,q)&(r,r)
\end{array}.
\tag{3}
\]
In particular the two diagonal paths P00 and P11 each have either ZERO or EXACTLY TWO ordered-window color changes (since their four-window color words begin and end with the same bit). The other two have opposite endpoint colors precisely when q≠r. NO conclusion is asserted about the two interior window bits or the existence of a monochromatic/one-switch SIX-edge path.

**Proof.** Associate to each unordered 3-set T the pair (h_z(alpha_T),h_z(rev alpha_T)), for an arbitrarily selected orientation alpha_T. Orientation reversal interchanges the two bits. Up to this interchange there are exactly THREE orbit types: 00,11,{01,10}. Thus the unordered 3-subsets of [n] are colored with THREE types. The classical Kneser chromatic theorem gives chi(KG(n,3))=n-4>3 for n>=8, so two DISJOINT triples A,B have the same orbit type. Reorient alpha and gamma so that the second triple signature is the SWAPPED signature of the first, yielding precisely the two equations (1). For n>=10 one may avoid the named Kneser input and instead use the elementary cyclic-interval disjoint-triple count already proved in Item nori_same_order_antipodal_root_pairs_endpoint_opposition_disjoint_triple_orbits_20261008.

Every word in (2) uses the same six distinct directions A union B, first the A directions then B, so from root x=z XOR A each reaches z after 3 moves and then ends at y=z XOR B. The four length-three free-coordinate windows begin at path positions1,2,3,4. In window1 the already fixed directions outside the first triple are still at their z-bits, because root differs from z only in the three FREE A bits. In windows2,3 the remaining untraversed A directions are still the only differing bits from z and are FREE in the window. After the third move the path is at z; window4 is the B-face through z. Hence ALL four physical face windows contain z. Their first and last ordered free triples are just the selected A and B orientations; (1) gives their color pairs (3). An even-parity number of changes follows for a four-bit word whose first/last bits agree, so the diagonal words have 0 or2 changes. \(\square\)

**Topology-first significance.** This creates at EVERY physical hub a literal four-vertex square in the space of genuine SAME-root/SAME-endpoint six-edge paths, indexed by two INDEPENDENT reversals of 3-direction prefix/suffix blocks. Unlike a fixed-root pair of unrelated endpoint-balanced full paths, these four certificates have a COMMON midpoint z and complete agreement of their used support. The input is a TOPLOGICAL Kneser coloring obstruction with only three signature orbits. Under active NORI oddness the four-path square also has the usual physically antipodal mate centered at bar z with complemented-reversed ordered windows.

The unresolved step is to transport this certified six-edge square through the other n−6 directions, using physical face incidence/root slides, so that an equivariant fixed-point collision produces a complete n-edge path with ≤1 change. The diagonal endpoint-equality condition alone is weaker than monochromaticity, and cannot be inflated to a global grand result without controlling the two middle seam windows and later exterior-bit changes.


## Exact moving-hub shift representation and its certified root squares

**Setting.** Let n>=5. For any binary coloring C of physical ordered three-faces of Q_n, define its hub table h_z(a,b,c)=C(F(z;{a,b,c}),(a,b,c)), where z is a cube vertex and a,b,c are distinct coordinate directions.

**Theorem 1 (complete hub coordinates).** The tables satisfy h_(z xor e_t)(a,b,c)=h_z(a,b,c) for t in {a,b,c}. Conversely any family with these invariances defines a unique physical ordered-three-face coloring. Its active NORI antipodal oddness is precisely h_(bar z)(c,b,a)=1-h_z(a,b,c).

Proof: toggling a free coordinate leaves its physical face unchanged, and any two points of a face differ only in free coordinates. The antipodal face contains bar z and reverses the ordered free tuple under the axiom.

**Theorem 2 (EXACT PATHWISE moving-hub identity).** For ANY full rooted geodesic (x,p), p=(p_1,...,p_n), let z_i=x xor e_(p_1) xor ... xor e_(p_i) and t_i=(p_i,p_(i+1),p_(i+2)) for i=1,...,n-2. If w_i denotes its ACTUAL physical ordered-three-face window color then
  w_i=h_(z_i)(t_i),
  h_(z_i)(t_(i+1))=h_(z_(i+1))(t_(i+1)),
and consequently each switch indicator is
  w_i xor w_(i+1)=h_(z_i)(p_i,p_(i+1),p_(i+2)) xor h_(z_i)(p_(i+1),p_(i+2),p_(i+3)),  i=1,...,n-3.
These are pointwise equations for EACH path, independent of any averaging or choice of a different witness.

Proof: the i-th physical window, with free directions t_i, contains both z_(i-1) and z_i, so its color is h_(z_i)(t_i). The hubs z_i,z_(i+1) differ in p_(i+1), which belongs to the free set of t_(i+1), so invariance gives the second identity.

**Exact admissible zigzag model.** Use states (z,t), z a cube vertex and t an injective ordered triple. Horizontal arrows at fixed z shift (a,b,c) to (b,c,d), d distinct; vertical arrows flip a coordinate in the fixed triple t, preserving h exactly. Each genuine full n-edge geodesic yields the zigzags
 (z_i,t_i) -> (z_i,t_(i+1)) -> (z_(i+1),t_(i+1))
for i=1,...,n-3, where the second arrow flips p_(i+1). Its switches are precisely its color-changing horizontal arrows. A valid zigzag must also come from one globally injective length-n direction word and coherent root x; arbitrary walks in this enlarged graph do not automatically encode cube geodesics. Grand closure is exactly existence of an admissible full zigzag with <=1 color-changing horizontal arrow.

**Theorem 3 (two certified commuting root directions).** The switch bit s_z(a,b,c,d):=h_z(a,b,c) xor h_z(b,c,d) is unchanged when z is toggled in coordinate b, c, or both. Thus each horizontal arrow has a geometrically certified square of four parallel horizontal comparisons over the 2-dimensional root face on {b,c}, with identical switch values. Toggling a changes the physical (b,c,d)-face while leaving the (a,b,c)-face fixed, and toggling d changes the physical (a,b,c)-face while leaving the (b,c,d)-face fixed; the geometry alone imposes no analogous invariance for a or d.

Proof: the two ordered triples share exactly their middle two directions {b,c}. Invariance of both face colors under toggling either shared coordinate proves the equalities. The remaining toggles change exactly one of the two actual physical faces; its color can be independently prescribed (with antipodal reversed mates fixed by the NORI axiom).

**Corollary (a rigorous limitation on automatic pentagon annuli).** A centered physical shift pentagon on five distinct coordinates p_0,...,p_4 uses ordered face triples t_i=(p_i,p_(i+1),p_(i+2)) modulo five. Their five free sets have EMPTY intersection. Therefore no nonzero coordinate toggle is guaranteed by the physical-face invariance to preserve every vertex color of the pentagon at once. Merely tensoring a centered pentagon with a fixed root-direction edge is not a universally certified product annulus; any successful antipodally transported good-window annulus must allow nonuniform root/order repair with literal shared path certificates. This is a limitation of the automatic face-preserving operation, not a theorem forbidding other annuli.

**Theorem 4 (exact full-switch mean equals same-hub graph cut energy).** Define
 A(C)=[2^n*(n)_4]^{-1} sum_{z in Q_n} sum_{(a,b,c,d) injective} 1{h_z(a,b,c)=h_z(b,c,d)},
where (n)_4=n(n-1)(n-2)(n-3).
For a uniform root X and uniform direction permutation P,
  E[D(X,P)]=(n-3)*(1-A(C)),
where D is the number of color changes among its n-2 physical window colors. Moreover A(C)>=1/5 for any binary physical ordered-three-face coloring, without NORI oddness.

Proof: for every fixed switch position i, (z_i,p_i,p_(i+1),p_(i+2),p_(i+3)) is uniform over all cube vertices and injective ordered quadruples: conditioned on P, the map X->z_i is a bijection. The pathwise identity makes the probability of an equality exactly A(C), independent of i. Summation gives the expectation. To prove the lower bound, at each fixed hub z form the directed shift graph G_n: vertices are injective ordered triples and arcs are injective ordered quadruples (a,b,c,d) from (a,b,c) to (b,c,d). Every cyclic ordered 5-tuple of distinct directions yields a directed odd pentagon, necessarily containing at least one equal-color arc. There are (n)_5/5 distinct directed pentagons and each arc belongs to n-4 of them. Hence at least (n)_4/5 arcs are equal-colored at each hub, so A(C)>=1/5. This recovers the team's universal E[D]<=4(n-3)/5 theorem by an exact moving-hub graph calculation.

**Research frontier.** The pointwise hub identities and the 2-direction commuting root squares are genuine, dimension-independent local chart transitions. They give a concrete means to seek coherent moving-hub higher cells, linking the physical pentagon parity cocycle and the exact same-root complementary reversed-two-tail extraction. The full proof still requires a global certificate-preserving selection/holonomy/descent that synchronizes horizontal equalities along ONE admissible n-coordinate zigzag. The mean and the local commuting squares alone do not provide that selection; unrestricted grand NORI closure remains open.

**Theorem 5 (a universal genuine ROOT-MOVING essential seven-cycle).** Fix ANY five distinct directions (a,b,c,d,e), ANY physical hub z and ANY physical ordered-three-face coloring in n>=5. In the actual good-window shift graph (hence inside W_good) there is the following SEVEN-VERTEX SIMPLE CYCLE. Write [T;y] for the actual ordered face with ordered free triple T passing through hub y:
 u_0=[(a,b,c);z],
 u_1=[(b,c,d);z],
 u_2=[(c,d,e);z xor b],
 u_3=[(d,e,a);z xor b xor d],
 u_4=[(e,a,b);z xor b],
 u_5=[(a,b,c);z xor e],
 v=[(b,c,e);z].
Then
  u_0 - u_1 - u_2 - u_3 - u_4 - u_5 - v - u_0
is a cycle of SEVEN DISTINCT actual ordered physical windows. EVERY edge is the pair of consecutive ordered windows of an actual directed four-edge cube geodesic and therefore is genuinely certified as a W_good edge for EVERY coloring. It contains BOTH ordered (a,b,c)-faces with exterior e-bit differing by one.

Proof (literal intermediate hubs). For the first five edges the common actual hubs are, in order:
 z, z xor b, z xor b xor d, z xor b, z xor b xor e.
The ordered triple pairs are respectively
 (abc,bcd), (bcd,cde), (cde,dea), (dea,eab), (eab,abc).
Every pair shares the last two directions of the first tuple with the first two of the second, and its two face objects really pass through the stated common hub. Invariance in the free directions verifies all displayed hub representatives agree. For the last two edges, [(a,b,c);z xor e] and [(b,c,e);z] both pass through z xor e on their respective physical faces (e is free for the latter), and [(b,c,e);z] and [(a,b,c);z] share hub z. Their order as undirected shift edges is legitimate. Every such pair has the explicit four-edge certificate with direction order of the corresponding shift, starting at hub XOR its first direction. All listed vertices are pairwise distinct: the only repeated ordered direction triple is (a,b,c), and those two ordered physical faces differ in exterior bit e. QED.

**Nontrivial integral-mod-two temporal homology.** Every edge in this literal seven-cycle has physical face-center L1-distance one, so the established intrinsic temporal cocycle beta(edge)=distance mod2 evaluates to 7=1 in F2. Since beta extends as a genuine 1-cocycle on all W_good simplices, this cycle C_7 is NOT a boundary of any 2-chain in W_good and is nonzero in H_1(W_good;F2). Likewise the same-color connector cocycle alpha=beta+delta(color) evaluates to 1. In active NORI, the cycle projects to a closed path in W_good/tau with beta_bar=1 and covering voltage w=0 (it already closes upstairs).

**Exact exterior sensitivity parity.** Let E_j be the equality indicator (1 for equal colors, 0 otherwise) on the seven consecutive edges. Telescoping the endpoint color differences around the FIVE-edge segment u_0 -> ... -> u_5 yields
 sum_{j=0}^{4} E_j = 1 + h_z(a,b,c) + h_(z xor e)(a,b,c)   (mod 2).
Along the TWO-edge bridge u_5 -> v -> u_0, one has
 E_5+E_6 = h_z(a,b,c)+h_(z xor e)(a,b,c) (mod 2).
The sum around all seven edges is therefore 1, as required. This makes a cross-root physical-face derivative visible through a genuine five-window transport, while its two-edge shortcut canonically closes an odd homology cycle. The seven-cycle itself is a graph 1-cycle and DOES NOT supply a certified two-dimensional annulus, a cup product, or a full n-geodesic.

**Suggested next implication to prove.** Search for actual W_good triangles allowing two such exterior-bit seven-cycles on distinct coordinates d,e to commute through good-window path homotopies. Any resulting certified annular transport around an antipodal root loop would activate the team's proved beta_bar cup w forcing criterion. The current theorem provides explicit, universally valid root-mobile one-dimensional cycles and common physical hubs for that search, but does not establish commuting homotopies or grand closure.


**Audit addendum (physical good-window quotient, 2026-10-09).** The "certified root squares" in Theorem 3 are squares ONLY in the redundant hub-coordinate PARAMETER graph. Toggling either shared free direction b or c fixes BOTH underlying ordered physical faces, so the four hub-chart comparisons all project to ONE and the SAME edge of the actual good-window complex W_good. Therefore these squares are DEGENERATE after physical-face identification and must NEVER be counted as nondegenerate 2-cells, an annulus, or evidence for a mixed cup product in W_good. The first genuine exterior-root transport (toggle a direction e outside {a,b,c,d}) is the six-window hexagon completely classified in proved Item nori_exterior_root_transport_hexagon_exact_good_triangles_rigidity_dichotomy_20261009. Its local triangles may fail simultaneously; when present they collapse across free chord edges and leave an induced S1. This addendum sharpens the precise scope of the earlier state-space observation while preserving its pointwise identities and averaging theorem.


The explicit bad rectangles show that a common midpoint and opposite central colors alone are not a closure certificate. The repair complex must also control physical seam windows and their root-bit dependence.
