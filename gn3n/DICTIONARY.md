## ambiguous

barrier: 
  Note: Do not use barrier as a technical noun without an explicit local definition of the obstruction it denotes. Prefer stating the forbidden or forced extension property directly.
clean: 
  Note: Do not use clean as an unexplained technical modifier. State the property meant by clean directly.
crossing: 
  Note: Do not use crossing without naming the objects that cross and the precise crossing relation.
failed insertion: 
  Note: State the insertion position that fails. If every insertion position fails, use noninsertable.
kernel: 
  Note: Use kernel only with an explicit definition or in a standard mathematical sense already fixed in context. Prefer naming the vertex set and its property.
omission surface: 
  Note: Avoid this frame-carrying phrase. Describe the family of deletion or restoration states directly.
plateau: 
  Note: Do not use plateau without specifying the quantity that is constant and the moves under which it is constant.
positive support: 
  Note: When referring to a fractional path cover, write positive-weight path support for a path support P with x_P>0.
reconfiguration: 
  Note: State the objects forming the state space and the legal move relation before using reconfiguration as shorthand.
shell: 
  Note: Avoid shell as frame-carrying shorthand. State the family of vertex sets, covers, or states directly.
support exchange: 
  Note: State which vertex sets are changed and which path or Hamiltonicity property is preserved.
uncrossing: 
  Note: State the transformation explicitly. No generic uncrossing operation is assumed.

## canonical

3-edge [alias -> hyperedge]: 
  Note: Permitted synonym for a 3-uniform directed hyperedge. Prefer tight triple when the boundary-tournament structure is central.
block-faithful: Let P_1,...,P_k be specified ordered paths. A path cover is block-faithful relative to P_1,...,P_k if, for every i, all vertices of P_i occur consecutively, in the order of P_i, within a single path of the cover.
  Note: Always state the reference paths P_1,...,P_k.
boundary flip: Given any list, its boundary flip is the list obtained by swapping its first and last elements.
  Note: For an ordered r-tuple (v_1,...,v_r), the boundary flip is (v_r,v_2,...,v_{r-1},v_1).
boundary tournament: A boundary r-tournament is an r-uniform directed hypergraph such that for every ordered r-tuple e of distinct vertices, exactly one of e and its boundary flip is a hyperedge.
  Note: In GN3N, r=3 unless otherwise specified. For r=3, call hyperedges tight triples when natural.
bridge: An edge whose deletion increases the number of connected components of the graph under discussion.
  Note: Use only in the standard graph-theoretic sense unless a separately defined atomic technical term explicitly modifies it. Do not use bare bridge for a path segment, local connector, join window, or heuristic transport gadget.
comparison arc: An arc of the comparison digraph.
  Note: When orientation matters, name both unordered-pair endpoints of the arc.
comparison digraph: For a boundary 3-tournament H, the comparison digraph Gamma(H) has one vertex for each unordered pair {u,v} of vertices of H and, for distinct u,v,w, has the arc {u,v}->{v,w} exactly when (u,v,w) is a tight triple of H.
  Note: Its underlying graph is the line graph of the complete graph on V(H).
compatible: Two path covers of the same vertex set are compatible if every pair of vertices lies in the same path in both covers or in different paths in both covers, and every pair lying together in both covers occurs in the same relative order in the two path orders.
  Note: For covers on different ambient vertex sets, first restrict both covers to the vertex set being compared.
complete fan: A complete fan on the ordered pair (u,v) with pivot p is the fan consisting of the three hyperedges (p,u,v), (u,p,v), and (u,v,p).
  Note: The terse form complete (u,v)-fan is permitted when the pivot is clear from context.
complete reverse fan: A complete reverse fan on the ordered pair (u,v) with pivot p is the fan consisting of the three hyperedges (p,v,u), (v,p,u), and (v,u,p).
  Note: The terse form complete reverse (u,v)-fan is permitted when the pivot is clear from context. Equivalently, it is the complete fan obtained by reversing the designated ordered pair (u,v).
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
deletion label: The vertex x associated with a deletion cover of H-x.
  Note: Use only when treating several deletion covers indexed by their omitted vertices.
double-frozen: Let H-x=P|Q be a deletion cover. It is double-frozen if H[V(P) union {x}] is frozen at x and H[V(Q) union {x}] is frozen at x.
  Note: No additional trapping or minimality property is implied.
dual slack: For a dual-feasible weighting w and a vertex set S that is the support of a tight path, the dual slack of S is 1-sum_{v in S} w(v).
  Note: Name S when more than one path support is under discussion.
dual-feasible weighting: A dual-feasible weighting on H is a function w:V(H)->R_{>=0} such that sum_{v in V(P)} w(v)<=1 for every tight path P in H.
  Note: This is the dual feasibility condition for fractional path cover.
edge: An edge is an unordered pair of distinct vertices.
  Note: Use edge in the ordinary graph-theoretic 2-uniform sense. In boundary-tournament mathematics, do not use edge for an ordered triple; use tight triple, hyperedge, or 3-edge.
edge-orderable: A boundary 3-tournament H is edge-orderable if there is a strict total order < on the edges of the complete graph on V(H) such that, for all distinct u,v,w, (u,v,w) is a tight triple of H exactly when {u,v}<{v,w}.
  Note: Here edge has its ordinary 2-uniform graph meaning. Equivalent to acyclicity of the comparison digraph.
fan: A fan is a nonempty family of hyperedges that has a pivot.
  Note: Terse notation is permitted. If p is understood as the pivot, phrases such as an (u,v)-fan, a complete (u,v)-fan, a reverse (u,v)-fan, and a complete reverse (u,v)-fan may be used when the corresponding modifier is defined.
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
Hamiltonian support: A vertex set S is a Hamiltonian support if H[S] has a tight path containing every vertex of S.
  Note: This term records the vertex set, not a particular Hamilton path order.
Hamiltonian-support odd graph: Fix a boundary tournament H and an integer lambda with |V(H)|=2lambda+1. The Hamiltonian-support odd graph has as vertices the Hamiltonian lambda-subsets of V(H), with two such subsets adjacent exactly when they are disjoint.
  Note: The name refers to the induced subgraph of the ordinary odd graph on Hamiltonian lambda-subsets.
hyperedge: In a directed 3-uniform hypergraph, a hyperedge is a distinguished ordered triple of distinct vertices.
  Note: In GN3N, tight triple is usually preferred when discussing the boundary tournament itself. The terms hyperedge and 3-edge are also permitted.
inseparable pair: Let H admit at least one two-cover. Distinct vertices x,y are inseparable if x and y belong to the same path of every two-cover of H.
  Note: The existence assumption prevents vacuous truth.
laminar: A family of vertex sets in which any two members are disjoint or one contains the other.
  Note: Use only in the standard set-system sense. In fractional-cover work, the relevant family is usually the path supports carrying positive weight.
leaf: Relative to a pivot p of a fan F, a leaf is a vertex other than p contained in some member of F.
  Note: Leaf is relative to a chosen pivot when a fan has more than one pivot.
left fan: A left fan with pivot p is a fan in which every hyperedge has the form (p,u,v).
  Note: The vertices u and v may vary from hyperedge to hyperedge. The terse form left p-fan is permitted.
mandatory triple: Let H admit at least one two-cover. A tight triple (a,b,c) is mandatory if, in every two-cover of H, one path contains a,b,c consecutively in that order.
  Note: Call (a,b,c) a tight triple, not an ordered edge.
matching-block K4: An edge-ordered K4 in which the three opposite-edge perfect matchings occur as three strict consecutive two-edge blocks in the edge order.
  Note: By the certified four-vertex classification, these are exactly the edge-ordered K4s with no increasing Hamilton path.
non-edge: In an ordinary graph, a non-edge is an unordered pair of distinct vertices that is not an edge.
  Note: Do not use non-edge for an ordered triple that is absent from a boundary tournament; use non-tight triple or non-hyperedge.
non-tight triple: In a boundary 3-tournament, a non-tight triple is an ordered triple of distinct vertices that is not a hyperedge.
  Note: For every ordered triple, exactly one of it and its boundary flip is a tight triple.
noninsertable: Let P=(v_1,...,v_m) be a tight path and let x notin V(P). The vertex x is noninsertable into P if none of the m+1 sequences obtained by inserting x into P at one position is a tight path.
  Note: Noninsertability is relative to the specified path order P.
one-defect state: Let R,S partition a vertex set. Write ell(X) for the maximum number of vertices in a tight path of H[X]. The bipartition R|S is a one-defect state if (|R|-ell(R))+(|S|-ell(S))=1.
  Note: No minimum-counterexample or deletion-cover hypothesis is part of the definition.
order disagreement: Two ordered paths with at least two common vertices have an order disagreement if some two common vertices occur in opposite relative orders in the two paths.
  Note: The term concerns only relative order of common vertices.
order-incompatible: Two support-compatible path covers are order-incompatible if some pair of vertices lying in one common component support occurs in opposite relative orders in the two corresponding path orders.
  Note: This is stronger than support compatibility and does not change the support partition.
pairwise repartition: A pairwise repartition of a path cover replaces exactly two paths by a path cover of the union of their vertex sets and leaves every other path unchanged.
  Note: State the two paths being repartitioned.
path-cover number: The minimum number pc(H) of vertex-disjoint tight paths whose supports partition V(H).
  Note: Because cover means path cover project-wide, pc(H) is the cover number of H.
pivot: A pivot of a nonempty family F of hyperedges is a vertex contained in every member of F.
  Note: A family may have more than one pivot.
quadratic potential: For a path cover C=P_1|...|P_q, the quantity Phi(C)=sum_i |P_i|^2.
  Note: When Phi has been fixed locally, quadratic potential and Phi are interchangeable. The definition applies to any fixed number q of path-cover components.
r-digraph: An r-digraph is an r-uniform fully directed hypergraph, so every hyperedge is an ordered r-tuple of distinct vertices.
  Note: Canonical abbreviation for r-uniform fully directed hypergraph.
r-k-tournament: An r-k-tournament is an r-digraph in which every induced sub-r-digraph on r vertices has exactly k hyperedges.
  Note: Use hyperedge rather than edge for the r-uniform directed objects.
relative-order disagreement [alias -> order disagreement]: 
  Note: Use order disagreement.
repartition: Let C be a path cover and let C_0 be a subcollection of its paths. A repartition of C_0 replaces those paths by another path cover of the same union of vertex sets, leaving all paths outside C_0 unchanged.
  Note: Name the paths being replaced when this is not clear.
reverse fan: A reverse fan on the ordered pair (u,v) with pivot p is a fan containing both (p,v,u) and (v,u,p).
  Note: The terse form reverse (u,v)-fan is permitted when the pivot is clear from context. Reverse refers to reversing the designated ordered pair (u,v) to (v,u).
right fan: A right fan with pivot p is a fan in which every hyperedge has the form (u,v,p).
  Note: The vertices u and v may vary from hyperedge to hyperedge. The terse form right p-fan is permitted.
singleton lift: If H-x has a deletion cover P|Q, the singleton lift of that deletion cover is the three-cover P|Q|{x} of H.
  Note: No additional property is implied.
support: The support of a path is its vertex set.
  Note: For a path cover, the component supports are the vertex sets of its paths.
support compatibility [alias -> support-compatible]: 
  Note: Use support-compatible when describing two path covers.
support-compatible: Two path covers of the same vertex set are support-compatible if they induce the same partition of the vertex set into path supports.
  Note: Relative order inside the supports is ignored.
support-incompatible: Two path covers of the same vertex set are support-incompatible if they induce different partitions of the vertex set into path supports.
  Note: This is the negation of support-compatible.
three-cover: A three-cover is a path cover consisting of exactly three nonempty tight paths.
  Note: Do not use three-cover to mean a cover with at most three paths.
tight path: A tight path is a sequence (v_1,...,v_m) of distinct vertices such that (v_i,v_{i+1},v_{i+2}) is a tight triple for every 1<=i<=m-2.
  Note: Paths with one or two vertices are tight vacuously.
tight triple: In a boundary 3-tournament, a tight triple is an ordered triple of distinct vertices that is a hyperedge.
  Note: Its boundary flip is a non-tight triple; a cyclic rotation has no implied status.
two-cover: A two-cover is a path cover consisting of one or two nonempty tight paths.
  Note: The paths together contain every vertex by the definition of path cover.
two-cover inseparability [alias -> inseparable pair]: 
  Note: Use inseparable pair for a pair of vertices. If discussing the resulting relation, define that relation explicitly.

## prohibited

Astra component [prohibited; use component]: 
  Note: Avoid the project-name phrase. Use the ordinary graph-theoretic word component when its ambient graph is clear; otherwise name the graph explicitly.
exact [prohibited]: 
  Note: Do not use exact as a modifier for covers, deletion covers, path covers, or related spanning path-cover notions. In GN3N a cover is spanning by definition, so exact is redundant.
Hamiltonian deletion cover [prohibited; use deletion cover]: 
  Note: Do not use this phrase. Use deletion cover for a cover after deleting a vertex, and Hamiltonian deletion for a vertex whose deletion leaves the relevant induced subtournament Hamiltonian.
