## Canonical Terms

antipodal: For vertices, bitwise complements within the containing cube or face. For a face, complement every fixed coordinate while retaining its free directions.
  Note: The antipode within a face complements just that face's free coordinates.

block: A member B of a stated partition of a coordinate set.
  Note: Blocks are pairwise disjoint and cover that set.

boundary 3-tournament: A function b on ordered triples of distinct vertices with b(c,b,a)=1−b(a,b,c).
  Note: No global ordering of graph edges is required.

corresponding: Vertices in parallel cube faces are corresponding when their projections onto the common free-coordinate set agree.
  Note: They may differ in the other coordinates.

edge-orderable: Describes a boundary 3-tournament b for which some total order of unordered vertex pairs has b(a,b,c)=1 exactly when {a,b}<{b,c}.
  Note: Equivalently, its comparison digraph is acyclic.

equitable balancing: Let G=(L union R,E) be a bipartite multigraph. Assign to each incidence (v,e) a fixed sign s(v,e) in {-1,+1}. An equitable balancing is a choice z(e) in {-1,+1} for every edge e such that the discrepancy D(v)=|sum_{e incident to v} s(v,e)z(e)| is at most 1 at every vertex, except for explicitly permitted exceptional vertices, where D(v) is at most 2.
  Note: For the one-sided signed balancing theorem in Article X, exceptions are permitted only on one specified side, with at most one exceptional vertex per connected component having all degrees even; components with an odd-degree vertex have no exceptions. Without such an exception allowance, all discrepancies are at most 1.

long: A path in a cube face is long if its initial and terminal vertices are antipodal within that face.
  Note: Longness is relative to the specified containing face and is determined by the endpoints. A long geodesic traverses each free-coordinate direction of the face exactly once.

one-sided: An equitable balancing is one-sided when exceptions are allowed on only one of the two sides of its bipartite incidence graph; every vertex on the other side must satisfy D(v)<=1.
  Note: In Article X, the exceptional side has at most one vertex of discrepancy 2 in each all-even-degree component. Either side may be designated as exceptional.

ordered k-face: A k-dimensional cube face F together with an ordering pi=(i_1,...,i_k) of its k free-coordinate directions.
  Note: No traversal starting vertex is specified by an ordered k-face.

parallel: Two cube faces are parallel if their spanned direction sets are comparable by inclusion, including equality.
  Note: Faces need not be nested as vertex sets.

signed: For an incidence multigraph, assigns a sign in {-1,+1} independently to each vertex-edge incidence.
  Note: A balancing with edge signs z_e then uses signed sums sum_(e incident to v) sigma_(v,e) z_e.

splice: A joining of consecutive monochromatic segments into a geodesic, with disjoint coordinate-direction supports.
  Note: The k-splice convention refers to at most k+1 monochromatic segments on a long geodesic.

switch: A change of color between consecutive entries of an edge-color word.
  Note: The k-switch convention means exactly k such changes on a long geodesic. 'At most k switches' allows fewer.

tight path: A sequence (v_1,…,v_m) of distinct vertices such that every consecutive ordered triple is a hyperedge of the specified directed 3-uniform hypergraph.
  Note: Distinctness is in the original vertex set.

## Forbidden

actual [prohibited]: 
  Note: Rhetorical modifier in compositions; express the mathematical claim instead.

concrete [prohibited]: 
  Note: Avoid redundant emphasis in mathematical compositions.

exact [prohibited]: 
  Note: Filler modifier in compositions; specify the equation or hypothesis instead.

genuine [prohibited]: 
  Note: Avoid redundant emphasis in mathematical compositions.

literally [prohibited]: 
  Note: Avoid redundant emphasis in mathematical compositions.

NORI conjecture [prohibited]: 
  Note: Ambiguous historical name for the refuted NORI3 one-switch conjecture; specify the exact statement.

NORI odd coloring [prohibited]: 
  Note: Ambiguous historical model name; specify NORI1, NORI2, NORI3 or the window model.

physical [prohibited]: 
  Note: Redundant modifier in compositions; name the face, edge, or path in the definition.

really [prohibited]: 
  Note: Avoid redundant emphasis in mathematical compositions.

truly [prohibited]: 
  Note: Avoid redundant emphasis in mathematical compositions.

## Notation

D(B,x;t): For a coordinate block B, cube vertex x and shift t, D(B,x;t)=|sum_(i in B)(-1)^(x_i xor t_i)|.
  Note: Block imbalance; D_B(x;t) is equivalent notation. If t=0, write D(B,x).

E_r(d): For binary edge coloring d of Q_m, E_r(d)={x in Q_m : f_d(x)<=r}.
  Note: Set of terminals of long geodesics with at most r switches; closed under vertex complementation.

f_d(x): Minimum number of switches among long geodesics in Q_m terminating at x, for an undirected-edge coloring d.
  Note: Reversing the geodesic gives the equivalent minimum over geodesics rooted at x.

k-splice: A long geodesic in an edge-colored cube decomposable into at most k+1 consecutive monochromatic geodesic segments, equivalently a long geodesic having at most k switches.
  Note: Unless another path length is explicitly specified, k-splice refers to a long geodesic relative to its containing face. The constituent segments have disjoint direction supports.

k-switch: A long geodesic in an edge-colored cube whose edge-color word has exactly k changes.
  Note: Unless a different path length is explicitly specified, k-switch refers to a long geodesic relative to its containing face. At most k switches allows fewer changes.

NORI1: The k=1 case of NORI_K: binary colorings of cube edges with c(bar e)=1−c(e). The open NORI1 full-geodesic conjecture asserts that every such coloring of Q_n admits a monochromatic antipodal geodesic.
  Note: The coloring class NORI1 and the conjecture about it are distinct.

NORI2: The k=2 case of NORI_K: binary colorings of ordered two-faces (F,π) satisfying c(bar F,rev π)=1−c(F,π).
  Note: NORI2 designates the class, not any proposed path-length or switch bound.

NORI3: The k=3 instance of NORI_K: binary colorings c(F,π) of three-dimensional faces with ordered free coordinates and c(bar F,rev π)=1−c(F,π).
  Note: NORI3 names this class, not a conjecture. The original universal assertion that some full antipodal geodesic has at most one color change was refuted in Q9. More strongly, some NORI3 colorings have no monochromatic coordinate-distinct geodesic longer than O(log n), by the two-sentinel antichain theorem valid for each fixed k≥3.

NORI_K: For 1≤k≤n, the class of binary colorings c(F,π) of pairs comprising a k-dimensional face F of Q_n and an ordering π of its k free coordinate directions, satisfying c(bar F,rev π)=1−c(F,π). A length-n antipodal geodesic has n−k+1 consecutive ordered k-face windows.
  Note: NORI_K names the coloring class, not a conjecture. The discarded universal 2-cp assertion concerns the k=3 case. For every fixed k≥3 and n≥k+2, the two-sentinel antichain construction supplies a coloring with no monochromatic coordinate-distinct geodesic longer than 3m+3k−4, where m=min{d≥2: binom(d,floor(d/2))≥n−2}=O(log n). Its proof is preserved in the foundational Section of Article I.

R(a): For a cube vertex a, the set of endpoints of monochromatic geodesics rooted at a, in either color; include a via the empty geodesic.
  Note: Use R^r(a) for length r and R(a;i), R^r(a;i) when requiring color i.
