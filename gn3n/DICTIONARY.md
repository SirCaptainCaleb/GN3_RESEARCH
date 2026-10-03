## Canonical

boundary flip: Given any list, its boundary flip is the list obtained by swapping its first and last elements.
  Note: For an ordered r-tuple (v_1,...,v_r), the boundary flip is (v_r,v_2,...,v_{r-1},v_1).

boundary tournament: A boundary r-tournament is an r-uniform directed hypergraph such that for every ordered r-tuple e of distinct vertices, exactly one of e and its boundary flip is a hyperedge.
  Note: In GN3N, r=3 unless otherwise specified. For r=3, call hyperedges tight triples when natural.

bridge: An edge whose deletion increases the number of connected components of the graph under discussion.
  Note: Use only in the standard graph-theoretic sense unless a separately defined atomic technical term explicitly modifies it. Do not use bare bridge for a path segment, local connector, join window, or heuristic transport gadget.

comparison digraph: For a boundary 3-tournament H, the comparison digraph Gamma(H) has one vertex for each unordered pair {u,v} of vertices of H and, for distinct u,v,w, has the arc {u,v}->{v,w} exactly when (u,v,w) is a tight triple of H.
  Note: Its underlying graph is the line graph of the complete graph on V(H).

compatible: Two path covers of the same vertex set are compatible if every pair of vertices lies in the same path in both covers or in different paths in both covers, and every pair lying together in both covers occurs in the same relative order in the two path orders.
  Note: For covers on different ambient vertex sets, first restrict both covers to the vertex set being compared.

component: A connected component of a specified graph.
  Note: Always identify the graph when it is not already unambiguous. Do not use component for an arbitrary family or state class.

contiguous-path number: For a vertex ordering pi=(v_1,...,v_n), the contiguous-path number c(pi) is the minimum k for which {1,...,n} can be partitioned into k consecutive intervals, each interval inducing a tight path in the order inherited from pi.
  Note: This parameter belongs to an ordering pi, not directly to H.

cover: A path cover, unless another kind of cover is explicitly specified.
  Note: Project-wide convention: unqualified cover always means path cover. Qualify only when a different notion of cover is intended.

defect center: For a vertex ordering (v_1,...,v_n), an index i with 2<=i<=n-1 is a defect center if (v_{i-1},v_i,v_{i+1}) is a non-tight triple.
  Note: Indices refer to the stated ordering.

defect line: For an ordering (v_1,...,v_n), its defect line is the graph with vertex set {1,...,n-1} and edge {i-1,i} for every defect center i.
  Note: The vertices 1,...,n-1 represent the cuts between consecutive positions.

defect span: For an ordering with defect-center set D, its defect span is 0 when D is empty and max(D)-min(D)+1 otherwise.
  Note: The definition depends only on the stated ordering and its defect centers.

deletion cover: For a boundary tournament H and a vertex x, a deletion cover at x is a two-cover of H-x.
  Note: When x matters, write deletion cover at x or a two-cover of H-x.

dual slack: For a dual-feasible weighting w and a vertex set S that is the support of a tight path, the dual slack of S is 1-sum_{v in S} w(v).
  Note: Name S when more than one path support is under discussion.

edge: An edge is an unordered pair of distinct vertices.
  Note: Use edge in the ordinary graph-theoretic 2-uniform sense. In boundary-tournament mathematics, do not use edge for an ordered triple; use tight triple, hyperedge, or 3-edge.

edge-orderable: A boundary 3-tournament H is edge-orderable if there is a strict total order < on the edges of the complete graph on V(H) such that, for all distinct u,v,w, (u,v,w) is a tight triple of H exactly when {u,v}<{v,w}.
  Note: Here edge has its ordinary 2-uniform graph meaning. Equivalent to acyclicity of the comparison digraph.

fractional path cover: A fractional path cover of H assigns a nonnegative real number x_P to each tight-path support P so that, for every vertex v, the sum of x_P over supports P containing v is at least 1. Its mass is sum_P x_P.
  Note: tau*(H) denotes the minimum mass.

frozen: For a non-Hamiltonian vertex set R and x in R, R is frozen at x if H[R-{x}] is Hamiltonian and H[R-{y}] is non-Hamiltonian for every y in R-{x}.
  Note: Equivalently, x is the unique Hamiltonian deletion of R.

fully directed hypergraph: A fully directed hypergraph consists of a vertex set together with a collection of distinguished ordered lists of distinct vertices called hyperedges.
  Note: Use hyperedge, not edge, for these ordered lists.

good deletion [alias -> Hamiltonian deletion]: 
  Note: Use Hamiltonian deletion. Do not introduce good as a technical modifier.

Hamiltonian deletion: For a vertex set R and v in R, v is a Hamiltonian deletion of R if H[R-{v}] has a tight path containing every vertex of R-{v}.
  Note: This is a property of the pair (R,v).

hyperedge: In a directed 3-uniform hypergraph, a hyperedge is a distinguished ordered triple of distinct vertices.
  Note: In GN3N, tight triple is usually preferred when discussing the boundary tournament itself. The terms hyperedge and 3-edge are also permitted.

laminar: A family of vertex sets in which any two members are disjoint or one contains the other.
  Note: Use only in the standard set-system sense. In fractional-cover work, the relevant family is usually the path supports carrying positive weight.

leaf: Relative to a pivot p of a fan F, a leaf is a vertex other than p contained in some member of F.
  Note: Leaf is relative to a chosen pivot when a fan has more than one pivot.

matching-block K4: An edge-ordered K4 in which the three opposite-edge perfect matchings occur as three strict consecutive two-edge blocks in the edge order.
  Note: By the certified four-vertex classification, these are exactly the edge-ordered K4s with no increasing Hamilton path.

noninsertable: Let P=(v_1,...,v_m) be a tight path and let x notin V(P). The vertex x is noninsertable into P if none of the m+1 sequences obtained by inserting x into P at one position is a tight path.
  Note: Noninsertability is relative to the specified path order P.

order disagreement: Two ordered paths with at least two common vertices have an order disagreement if some two common vertices occur in opposite relative orders in the two paths.
  Note: The term concerns only relative order of common vertices.

path-cover number: The minimum number pc(H) of vertex-disjoint tight paths whose supports partition V(H).
  Note: Because cover means path cover project-wide, pc(H) is the cover number of H.

quadratic potential: For a path cover C=P_1|...|P_q, the quantity Phi(C)=sum_i |P_i|^2.
  Note: When Phi has been fixed locally, quadratic potential and Phi are interchangeable. The definition applies to any fixed number q of path-cover components.

reconfiguration: A reconfiguration is a finite sequence of path covers of the same vertex set in which each consecutive pair differs by a pairwise repartition.
  Note: State any additional restriction on the sequence, such as fixed component orders or constant quadratic potential. A neutral reconfiguration is one in which the quadratic potential is constant along the sequence.

repartition: Let C be a path cover and let C_0 be a subcollection of its paths. A repartition of C_0 replaces those paths by another path cover of the same union of vertex sets, leaving all paths outside C_0 unchanged.
  Note: Name the paths being replaced when this is not clear.

singleton lift: If H-x has a deletion cover P|Q, the singleton lift of that deletion cover is the three-cover P|Q|{x} of H.
  Note: No additional property is implied.

support: The support of a path is its vertex set.
  Note: For a path cover, the component supports are the vertex sets of its paths.

support-compatible: Two path covers of the same vertex set are support-compatible if they induce the same partition of the vertex set into path supports.
  Note: Relative order inside the supports is ignored.

three-cover: A three-cover is a path cover consisting of exactly three nonempty tight paths.
  Note: Do not use three-cover to mean a cover with at most three paths.

tight path: A tight path is a sequence (v_1,...,v_m) of distinct vertices such that (v_i,v_{i+1},v_{i+2}) is a tight triple for every 1<=i<=m-2.
  Note: Paths with one or two vertices are tight vacuously.

tight triple: In a boundary 3-tournament, a tight triple is an ordered triple of distinct vertices that is a hyperedge.
  Note: Its boundary flip is a non-tight triple; a cyclic rotation has no implied status.

two-cover: A two-cover is a path cover consisting of one or two nonempty tight paths.
  Note: The paths together contain every vertex by the definition of path cover.

uncrossing: For sets A and B in a set system with A intersect B, A minus B, and B minus A all nonempty, an uncrossing step replaces A,B by a specified pair drawn from A intersect B, A union B, A minus B, and B minus A, while preserving the feasibility or objective property stated in the theorem using the step.
  Note: The theorem invoking uncrossing must state which replacement pair is used and which feasibility or weight property is preserved. There is no unspecified generic uncrossing move.

## Prohibited

Astra component [prohibited; use component]: 
  Note: Avoid the project-name phrase. Use the ordinary graph-theoretic word component when its ambient graph is clear; otherwise name the graph explicitly.

barrier [prohibited]: 
  Note: Do not use barrier as a technical noun. State the specific forbidden insertion, extension, comparison, size condition, or other obstruction directly; introduce a narrower canonical term only after giving it a project-wide definition.

clean [prohibited]: 
  Note: Do not use clean as a technical modifier. State the property directly.

crossing [prohibited]: 
  Note: Do not use crossing as an unqualified technical noun or modifier. For an edge and a cut, say that the edge has endpoints on opposite sides of the named cut. For sets, use crossing sets only after the canonical set-theoretic relation is introduced.

exact [prohibited]: 
  Note: Do not use exact as a modifier for covers, deletion covers, path covers, or related spanning path-cover notions. In GN3N a cover is spanning by definition, so exact is redundant.

failed insertion [prohibited]: 
  Note: Do not use failed insertion as a technical phrase. Name the insertion position and state which required triple or comparison fails; if every insertion position fails, use noninsertable.

Hamiltonian deletion cover [prohibited; use deletion cover]: 
  Note: Do not use this phrase. Use deletion cover for a cover after deleting a vertex, and Hamiltonian deletion for a vertex whose deletion leaves the relevant induced subtournament Hamiltonian.

kernel [prohibited]: 
  Note: Do not use kernel as project shorthand. Name the vertex set or substructure and the property it satisfies. A future standard mathematical use requires its own canonical dictionary entry.

omission surface [prohibited]: 
  Note: Do not use omission surface. Describe the relevant deletion covers, singleton lifts, or restoration states directly.

plateau [prohibited]: 
  Note: Do not use plateau as project shorthand. State the invariant quantity and the allowed moves directly.

shell [prohibited]: 
  Note: Do not use shell as project shorthand. Name the vertex set, its cardinality, how it is formed, and the Hamiltonicity or cover property that matters.
