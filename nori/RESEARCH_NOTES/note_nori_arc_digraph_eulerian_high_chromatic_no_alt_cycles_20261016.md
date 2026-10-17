# Square-coherence obstruction: strongly connected unimodular shift countermodels

- Stable ID: note_nori_arc_digraph_eulerian_high_chromatic_no_alt_cycles_20261016
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, folded-cube, Eulerian, chromatic, counterexample, line-digraph
- Lifecycle: active
- Epistemic status: proved
- Current version: 5
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10917_3
- Updated session: session_nori_r10917_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_folded_cube_semieulerian_alternating_girth_equivalence_20261015

## Research note

Let H be a finite loopless directed graph in which every vertex has indegree and outdegree r>=1 and in which oppositely directed parallel arcs are absent. Form its directed line graph L(H): vertices are directed arcs e=(u,v) of H, with an arc (u,v)->(v,w) whenever these arcs concatenate. Let G be the underlying undirected graph, with the displayed Eulerian orientation.

THEOREM (Eulerian shift obstruction). G is 2r-regular, the displayed orientation has indegree=outdegree=r, and the oriented incidence bipartite graph with vertices e^+,e^- and edges e^+--f^- for every oriented arc e->f decomposes into |V(H)| connected components. For each v in H, the corresponding component is the complete bipartite graph K_(r,r) between { (u,v)^+:u->v } and { (v,w)^-:v->w }. Consequently no e^+ is connected to e^- by any incidence path, so G has no alternating odd closed walk with a single transit vertex, of any length.

Further, chi(G)>=log_2 chi(H). For every proper k-coloring f of G, assign to each v in H the set A_v={f((u,v)):u->v}. If u->v in H, f((u,v)) belongs to A_v but cannot belong to A_u, since (u,v) is adjacent in G to every (w,u) with w->u. Thus A_u differs from A_v, and v->A_v yields a proper coloring of the underlying H using at most 2^k colors. This proves chi(H)<=2^k.

COROLLARY (vertex-transitive countermodels of unbounded chromatic number). Let p be any prime congruent to 3 mod 4. Let H be the Paley tournament on F_p, with u->v iff v-u is a nonzero quadratic residue. It is r-in/r-out regular with r=(p-1)/2, and its underlying graph is K_p. Thus G=L(H) is (p-1)-regular and vertex-transitive, has an Eulerian orientation, satisfies chi(G)>=ceil(log_2 p), and contains no alternating odd closed walk with one transit vertex. Vertex transitivity follows because translations and multiplication by nonzero quadratic residues preserve Paley arcs and act transitively on them. Such primes p are unbounded, giving arbitrarily high chromatic number.

For p=7, G has 21 vertices, degree six and seven incidence components K_(3,3). For p=11, G has 55 vertices, degree ten and 11 components K_(5,5). A script checking the cyclic regular tournament (rather than Paley) verifies the same regularity and biclique component formula for p=5,7,11,15. Paley additionally supplies vertex transitivity.

COROLLARY (the sharp reason graph-only forcing fails). In the odd-dimensional folded-cube interpretation of NORI1, a red antipodal shortest path is an almost-alternating odd-girth cycle in an orientation. The construction above shows that Eulerianity, regular degree, arbitrarily large chromatic number, vertex transitivity, and nonbipartiteness, even in combination, cannot force such an orientation pattern in general graphs: the G above has none of any length. The special binary-circuit Cayley generators of the folded cube are indispensable for a universal result. This is an obstruction to a proposed general graph-theoretic proof, not a counterexample to NORI1.

POSITIVE CUBICAL CONTRAST (common-out-neighbor sparsity and quadratic minimum degree). Let d=2m+1>=5, and let D be the oriented adjacency matrix of the folded cube G_d from any nearly regular orientation (each outdegree m or m+1, hence each indegree m or m+1). Put H=DD^T and let C_D have vertex set V(G_d) and edges uv when u!=v and H_uv>0. Then:
(1) H_uv<=2 whenever u!=v. Indeed the folded cube is a Cayley graph of the even-bit vectors with generators a_i=1+e_i, and a_i+a_j=e_i+e_j. Two distinct vertices share neighbors only when they differ in two bits, and in that case have two common neighbors (indexed by swapping i,j). Thus no pair has more than two common outneighbors.
(2) The minimum degree of C_D satisfies
delta_min(C_D) >= ceil(m(m-1)/2).
Indeed at any u,
sum_(v!=u) H_uv = sum_(w in outneighbors(u)) (indegree(w)-1) >= m(m-1).
Every nonzero summand H_uv is at most two, giving at least ceil(m(m-1)/2) distinct common-outneighbor vertices v.
This estimate applies to every nearly regular folded-cube orientation. In the Eulerian Paley line-graph examples above, any two vertices represented by distinct arcs with the same head have r=(p-1)/2 common outneighbors, violating the cubical bound H_uv<=2 whenever p>=7. Therefore their failure mechanism cannot be transported to folded cubes while keeping the local Cayley support structure. The inequality is a substantial local constraint but does not force a length-m common-out path across a folded-cube edge; exponentially fragmented C_D examples already occur in the archive.


THEOREM (extensive rank forced by the cubical codegree bound). Under the hypotheses of the cubical contrast theorem above, write N=2^(d-1)=2^(2m) for the number of vertices of the folded cube, and let D be its N-by-N oriented adjacency matrix. Then
rank_R(D) >= N (m+1/2)^2/(3m^2+m+1/2) > N/3.
Equivalently the adjacency matrix of the associated red subgraph of Q_d has rank exceeding 2^d/3. This holds for every near-regular orientation, without a symmetry, linearity, or locality assumption on the corresponding cube coloring.

*Proof.* Put H=DD^T, whose rank equals that of D. Every vertex has outdegree m or m+1. Summing outdegrees counts |E(G_d)|=N(2m+1)/2, so half of the N vertices have degree m and half have degree m+1. The same is true of indegrees. Thus
tr H=N(m+1/2),
sum_u H_uu^2=N(m^2+m+1/2),
and
sum_(u!=v) H_uv = sum_w indeg(w)(indeg(w)-1)=N m^2.
The preceding cubical codegree bound gives H_uv in {0,1,2} for u!=v and therefore H_uv^2<=2H_uv. Consequently
tr(H^2)=sum_(u,v)H_uv^2 <=N(3m^2+m+1/2).
By Cauchy-Schwarz on the positive eigenvalues of H,
rank H >=(tr H)^2/tr(H^2)
>=N(m+1/2)^2/(3m^2+m+1/2)>N/3.
The red adjacency matrix is [[0,D],[D^T,0]], so its rank is 2rank(D). QED.

In the regular-tournament arc graph with q vertices and r=(q-1)/2, the oriented adjacency D_arc is a product of the matrix recording an arc's head and the matrix recording the next arc's tail, so rank(D_arc)<=q although its dimension is qr. Hence its rank fraction is <=1/r, tending to zero. The cubical codegree constraint excludes this algebraic low-rank obstruction. Positive rank density is not by itself a geodesic-existence criterion: D may still be singular and its common-out-neighbor graph disconnected.


## Stronger odd-degree shift-matching countermodels and the sixteen-vertex rigidity boundary

**Theorem A (sharp failure of degree, girth, codegree and large rank as a collective criterion).** For every integer q>=7, define the directed graph D_q with
V(D_q)={ (t,u,s): t in {0,1}, u in Z/qZ, s in {1,2} }.
Its arcs are
(t,u,s) -> (t,u+s,r) for r in {1,2},
and (0,u,s) -> (1,u+s,s).
Let G_q be its undirected support. Then:
(i) G_q is connected and 5-regular on 4q vertices, with odd girth five; all vertices have in/out degree (2,3) or (3,2).
(ii) Every distinct pair of vertices of G_q has at most two common undirected neighbors. Consequently, the common-out-neighbor entries (D_q D_q^T)_{uv} are at most two for u!=v.
(iii) rank_R D_q=3q=(3/4)|V(G_q)|.
(iv) The bipartite alternating-incidence graph whose vertices are z^+,z^- for z in V(G_q) and whose edges are z^+--w^- for every arc z->w has q connected components. In particular z^+ and z^- are never in the same component. Hence G_q contains no almost-alternating odd closed walk having one transit vertex, of any length.

*Proof of degrees, connectivity, odd girth.* In each of the two layers, the arc (u,s) of the base Cayley digraph H_q: u->u+s has two possible successors (u+s,1),(u+s,2) and two possible predecessors (u-1,1),(u-2,2). Its directed line graph is strongly connected because steps of size one generate Z/qZ. Joining both connected layers by a perfect matching gives connected G_q. The matching gives an extra outgoing edge in layer zero and an extra incoming edge in layer one, giving the stated degrees. A triangle cannot traverse the matching between layers, since interlayer edges form a matching. An undirected triangle in a loopless directed line graph lacking directed two-cycles must correspond to a directed triangle in the base graph: any transitive orientation of the three line-graph adjacencies would force a loop in the base. But a directed three-cycle in H_q would require three numbers in {1,2} to sum to a multiple of q, impossible for q>=7. Finally the five vertices
(0,0,1), (0,-1,1), (0,0,2), (1,2,2), (1,1,1)
form a five-cycle in this displayed order, establishing odd girth five.

*Proof of codegree.* The undirected neighbors of a layer-zero vertex (0,u,s) are the four vertices
(0,u+s,1), (0,u+s,2), (0,u-1,1), (0,u-2,2),
plus (1,u+s,s). A layer-one vertex (1,u,s) has the analogous four same-layer neighbors and (0,u-s,s). Since the cross-layer edges form a matching, two vertices in one layer cannot share any cross-layer neighbor, and two vertices in different layers have at most one common neighbor in either layer, hence at most two altogether. Within one layer, common successors number two only when two distinct arcs share their head, and common predecessors number two only when they share their tail; both cannot occur at once. Each of the two crossed successor-predecessor types contributes at most one common neighbor. When two arcs share a head or a tail, crossed types would force a directed two-cycle in H_q and therefore contribute none. Thus their total common-neighbor count is at most two.

*Proof of rank.* Write E=Z/qZ x {1,2}, and let A be the line-graph adjacency on R^E. It acts by
(Af)(u,s)=f(u+s,1)+f(u+s,2).
Thus ker A consists of f with f(v,1)+f(v,2)=0 for every v and has dimension q. The image of A consists of functions of the head u+s and has dimension q. Let M be the cross-layer matching permutation, (Mf)(u,s)=f(u+s,s). The full matrix is
D_q = [[A,M],[0,A]].
If D_q(x,y)=0, then Ay=0 and My=-Ax belongs to im A. The latter condition means y(v,1)=y(v,2) for every v; combining with Ay=0 gives y=0 over R. We are left with Ax=0, a q-dimensional kernel. Hence rank D_q=4q-q=3q.

*Proof of alternating-incidence separation.* Give each plus copy (t,u,s)^+ the label u+s (its base arc's head), and each minus copy (t,u,s)^- the label u (its base arc's tail). Every horizontal directed edge joins a plus and minus copy with the same label; every vertical matching edge does so too. For each label v, the horizontal edges within either layer form a K_(2,2), and two vertical edges join the corresponding two layer components. Therefore every label class is connected and the bipartite incidence graph has q components. Since s is one or two and q>=7, the plus and minus copies of (t,u,s) have different labels and can never be joined by an incidence path. Such a path would be necessary for an almost-alternating odd closed walk with a single transit vertex. This proves (iv).

**The precise omitted cubical feature: square completion.** For every q>=7, the wedge centered at (0,0,1) with neighbors (0,1,1) and (0,-2,2) lies on no four-cycle; these two neighbors have only the center as a common neighbor. In contrast, every wedge of two distinct incident edges in the folded cube G_5 is contained in one four-cycle, because its five Cayley generators have independent pairwise sums.

**Theorem B (rigidity at the folded-five-cube order).** Let X be any triangle-free simple 5-regular graph on sixteen vertices, and assume every pair of distinct vertices has at most two common neighbors. Then X is isomorphic to the folded five-cube G_5 (the Clebsch graph).

*Proof.* Fix a vertex o and denote its five pairwise nonadjacent neighbors by a_1,...,a_5. There are ten other vertices B. The five a_i together have 5*4=20 incidences with B, since X is triangle-free. Every b in B has at most two neighbors among the a_i, by the common-neighbor bound with o. Since |B|=10, every b has two such neighbors. Each pair a_i,a_j already has common neighbor o and can share at most one more, so the ten vertices of B are identified bijectively with the ten two-element sets {i,j}, denoted b_ij. If b_ij and b_ik share an index, they are both adjacent to a_i, so triangle-freeness forbids an edge between them. Every b_ij has two neighbors among the a_i and none at o, hence requires three neighbors in B. There are only three two-subsets of [5] disjoint from {i,j}; all three must be adjacent to b_ij. Thus the entire graph is forced: o is adjacent to each a_i; a_i is adjacent to b_ij when i belongs to {i,j}; and b_ij is adjacent to b_kl precisely when their pairs are disjoint. This is the Clebsch graph, equivalently folded Q_5. QED.

**Interpretation and limitations.** Theorem A refutes graph-only closure hypotheses based simultaneously on near-balanced odd degree, odd girth equal to degree, undirected codegree at most two, and substantial directed adjacency rank. Such hypotheses do not force even a long almost-alternating closed walk. Theorem B proves that at the folded Q_5 vertex count, degree, triangle-freeness and codegree already enforce the correct cubical graph. The obstruction in Theorem A lies in the absent square-completion structure and, for dimension five, in its larger vertex count. These results do not refute NORI1.


## Strongly connected unimodular countermodels with cubic codegree

**Theorem (balanced strongly connected invertible shift models).** For every integer q>=7 there exists a connected simple 5-regular graph G_q with 4q vertices and odd girth five, carrying an orientation D_q such that:
(i) every vertex has in- and out-degree two and three, in some order;
(ii) D_q is strongly connected;
(iii) distinct vertices of G_q have at most two common neighbors;
(iv) det D_q=(-1)^q and hence the oriented adjacency matrix is unimodular and nonsingular;
(v) there is no almost-alternating odd closed walk with one transit vertex, of any length.
Nevertheless, G_q fails the unique-square-completion property of the folded five-cube. These are countermodels to sufficiency of degree, girth, codegree, directed strong connectivity, and even integral adjacency invertibility, in combination.

*Construction.* Take vertices (t,u,s), with t in {0,1}, u in Z/qZ, s in {1,2}. Insert all intralayer arrows
(t,u,s) -> (t,u+s,r), r in {1,2}.
For the interlayer matching, insert arrows
(0,u,1) -> (1,u+1,1)
and
(1,u,2) -> (0,u+2,2).
The displayed cross edges form a perfect matching: on s=1 they run from layer zero to one, and on s=2 they run from layer one to zero.

*Proof of regularity, connectivity and girth.* Each intralayer vertex has two successors and two predecessors. The cross matching adds one in- or out-edge, giving undirected degree five and the semidegrees in (i). Each intralayer directed line graph is strongly connected: the underlying base arcs u->u+s have a directed path between any two endpoints because unit steps generate Z/qZ; every required terminal arc can be appended. Since one family of cross arcs travels from layer zero to one and the other travels back, the full orientation is strongly connected. There are no triangles inside a layer: a triangle in a directed line graph of a loopless digraph without directed two-cycles would give a directed triangle in its base, but the sum of three increments from {1,2} cannot vanish modulo q>=7. The interlayer edges form a matching, so no triangle meets both layers. The five vertices
(0,0,1), (0,1,1), (0,2,1), (0,0,2), (0,-2,2)
form a pentagon in that cyclic order. Thus odd girth is five.

*Proof of the common-neighbor bound.* In a fixed layer, two vertices representing arcs of the base digraph share at most two undirected line-graph neighbors. Equal heads give precisely two common successors and no mixed common neighbor because the base has no directed two-cycles; equal tails similarly give two common predecessors. If both heads and tails differ, there are no common successors or predecessors, and at most one neighbor of each of the two mixed types. Cross matching gives no additional common neighbor to vertices within one layer. For vertices in different layers, a common neighbor must use one cross matching edge; at most one such neighbor lies in each layer. Hence the total common-neighbor count is at most two.

*Proof of unimodularity.* Group the directed adjacency matrix by layers and then s=1,2. Fourier-transform the cyclic u-variable, and write z for a complex q-th root of unity. The Fourier-mode block is
D(z)=
[[z,z,z,0],
 [z^2,z^2,0,0],
 [0,0,z,z],
 [0,z^2,z^2,z^2]].
Direct determinant expansion gives det D(z)=-z^6. Therefore
det D_q= product_{z^q=1}(-z^6)=(-1)^q,
since (product_{z^q=1} z)^6=1. Thus D_q is invertible over the integers.

*Proof of alternating-walk obstruction.* Assign labels a(t,u,s)=u+s and b(t,u,s)=u in Z/qZ. Every displayed directed edge v->w obeys a(v)=b(w), whereas a(v)!=b(v) for every vertex since s in {1,2}. The alternating-incidence graph joining v^+ to w^- whenever v->w has a constant label along each edge, but the two copies v^+ and v^- have different labels. Hence no alternating incidence walk connects the two copies of any vertex, excluding every almost-alternating odd closed walk with a single transit. In fact the incidence graph has q connected components, one for each label value.

*Explicit missing square.* The wedge through (0,0,1) whose other vertices are (0,1,1) and (0,-2,2) belongs to no quadrangle: these endpoints have only the center as common neighbor. A folded five-cube has one quadrangle for every such wedge. Consequently these countermodels cannot inherit the globally commuting binary-circuit structure proved for folded cubes in the companion rigidity note.

*Finite checks.* Direct graph and integer-rank computations at q=7 and q=11 return 28 and 44 vertices, odd girth five, undirected common-neighbor maximum two, strongly connected orientations, incidence-component counts 7 and 11, and full adjacency ranks 28 and 44. The determinant proof covers every q>=7. The result does not refute NORI1: its host graphs omit compulsory cubical quadrangles.
