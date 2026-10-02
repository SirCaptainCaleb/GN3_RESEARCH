# Deletion-cover compatibility graphs exclude K4 minors unconditionally

## Statement

Let H be a finite boundary 3-tournament with pc(H)>2. Choose one ordered two-cover F_d of H-d for each d in a set D of m distinct deletion labels. Join d,e when the covers induce the same ordered support partition on V(H)-{d,e}. The resulting full-compatibility graph G is K4-minor-free, hence 2-degenerate and 3-colorable. For m>=2 it has at most 2m-3 edges; at least (m-2)(m-3)/2 pairs are incompatible; and a subfamily of at least ceil(m/3) chosen deletion covers is pairwise incompatible. Every induced family of t>=3 covers has a cover incompatible with at least t-3 others. Any incompatible pair has an actual disagreement-witness pair of ground vertices whose labels separate its endpoints in G.

## Body


Let H be a finite boundary 3-tournament with pc(H)>2. Let D be a set of m distinct vertices such that, for every d in D, a particular two-cover F_d of H-d has been chosen, including the displayed order of each path. Define a simple graph G on D by joining d and e exactly when F_d and F_e are compatible on V(H)-{d,e}: their restrictions give the same partition into ordered blocks. Restrictions here mean restriction of the ordered partition; they need not themselves be tight paths after internal vertices are deleted.

**Theorem.** G has no K4 minor. In particular G is 2-degenerate and 3-colorable, and, for m>=2,

    |E(G)| <= 2m-3.

Consequently at least (m-2)(m-3)/2 unordered pairs of the chosen deletion covers are incompatible, and some subfamily of at least ceil(m/3) deletion covers is pairwise incompatible. Every induced subfamily of t>=3 covers contains a cover incompatible with at least t-3 of the others.

### Pair relations and propagation

For distinct u,v different from d, encode their relation in F_d by one of three values: different blocks; same block with u before v; same block with v before u. If de is an edge of G and neither d nor e belongs to {u,v}, the two covers give the same relation to u,v. Hence the relation of u,v is constant along every path in G-{u,v}, where ground vertices not in D remove nothing.

This also proves a useful witness statement. If F_d and F_e are incompatible, some pair u,v in their common domain has different relations in these covers. The set {u,v} intersect D separates d from e in G. The pair is an actual support/order disagreement witness, rather than an arbitrary graph separator. In particular, three internally vertex-disjoint d-e paths force F_d and F_e to be compatible.

### Four compatible covers reconstruct a two-cover

**Lemma.** Let d_1,d_2,d_3,d_4 be distinct deletion labels. If their chosen two-covers are pairwise compatible, then H has a spanning two-cover.

For each pair u,v of distinct ground vertices, choose a label d_i outside {u,v} and assign to u,v its relation in F_{d_i}. Pairwise compatibility makes this choice independent of i.

Declare two distinct vertices equivalent when their assigned relation places them in the same block, and declare every vertex equivalent to itself. Transitivity follows by considering any three vertices u,v,w and choosing a deletion label outside that triple: all three pair relations are then witnessed in one ordered partition F_{d_i}. The same argument shows that, within each equivalence class, the assigned precedence relation is a strict total order.

There are at most two equivalence classes. Otherwise choose one representative from each of three classes and a deletion label outside these representatives. Its two-cover would put the three representatives in three distinct blocks, a contradiction.

For every i, the restriction of this global ordered partition to H-d_i is exactly the ordered partition of F_{d_i}, since its pair relations are exactly those of F_{d_i}. Finally let u,v,w be any three consecutive vertices of one global block. Choose d_i outside this triple. The three remain consecutive in that block after deleting d_i, so they occur consecutively in a path of F_{d_i}. Thus (u,v,w) is tight. The one or two global ordered blocks are therefore tight paths and form a spanning two-cover. This proves the lemma.

The argument uses only the locality of tight-path constraints on triples and the bound of two blocks. It does not use minimal-counterexample assumptions or a lower bound on component sizes.

### A subdivision of K4 forces four compatible covers

Suppose G contains a subdivision K of K4, with branch vertices d_1,d_2,d_3,d_4. After deleting any two vertices of K, all surviving branch vertices remain in one connected component. Here is the complete verification.

* If both deleted vertices are branch vertices, the subdivided edge between the other two survives.
* If one is a branch vertex and the other is internal, the triangle on the three remaining branch vertices loses at most one subdivided edge and still connects those vertices.
* If neither is a branch vertex, at most two subdivided edges are interrupted. Deleting at most two edges from K4 leaves it connected, so all four branch vertices remain connected.

Deleting zero or one vertex is included by the same argument; ground vertices outside K have no effect.

Fix two branch labels d_i,d_j and any ground pair u,v in their common domain. They are surviving branch vertices of K-{u,v}, so a compatibility path connects them while avoiding u,v. Propagation makes their relation on u,v identical. Since the pair was arbitrary, F_{d_i} and F_{d_j} are compatible. Thus the four branch covers are pairwise compatible, contradicting the reconstruction lemma and pc(H)>2. Therefore G contains no subdivision of K4.

For K4, having a minor is equivalent to having a subdivision: in a minor model, each of the four disjoint connected branch sets has only three required attachment vertices. Prune each branch set to a minimal tree joining those attachments, and use its unique branching point (possibly one attachment) to obtain internally disjoint arms. Together with the six inter-branch edges, these arms form a subdivision. Consequently G is K4-minor-free.

### Elementary derivation of the graph consequences

We record the standard graph argument for completeness. A 3-connected graph on at least four vertices contains a subdivision of K4. Indeed, fix a vertex v, choose a cycle in the 2-connected graph G-v, and use the vertex form of Menger's theorem to find three internally disjoint paths from v to three distinct vertices of the cycle, meeting the cycle only at their ends. Their union with the cycle contains the required subdivision.

We next prove by induction that, in a 2-connected K4-minor-free graph J with at least three vertices, for any specified edge xy there is a vertex outside {x,y} of degree two. The claim is immediate for three vertices. For more vertices J is not 3-connected, so it has a separator {a,b}. Since xy is an edge, there is a component C of J-{a,b} containing neither x nor y outside the separator. Put J'=J[C union {a,b}]+ab. Every component of J-{a,b} attaches to both a and b, since J is 2-connected. An a-b path through another component can therefore be contracted to show that J' is a minor of J. The graph J' is 2-connected: any path outside C can be replaced by the edge ab, and after deleting a or b connectivity follows from that of J-a or J-b. It has fewer vertices than J. Apply induction with specified edge ab. It gives z in C with degree two in J'; all neighbors of z in J lie in C union {a,b}, so z has degree two in J as well, and z is outside {x,y}.

Any nonempty K4-minor-free graph has a vertex of degree at most two. For a graph that is not 2-connected, take an end block: an edge end block gives a degree-one vertex; in a 2-connected end block use the preceding assertion with an edge incident to its possible cut vertex. The resulting degree-two vertex is not the cut vertex and has no neighbors outside that block. The connected graph consisting of one block, isolated vertices, and disconnected graphs are immediate variants. Apply this argument to every induced subgraph to obtain 2-degeneracy.

Deleting a vertex of degree at most two repeatedly, down to two vertices, gives |E(G)|<=2(m-2)+1=2m-3. Greedy coloring in reverse deletion order uses at most three colors. One color class has size at least ceil(m/3) and is a pairwise incompatible family of deletion covers. The same degeneracy statement on any t-vertex induced subgraph supplies a cover compatible with at most two, and hence incompatible with at least t-3, of the other selected covers. Finally,

    binom(m,2)-(2m-3)=(m-2)(m-3)/2

is the stated incompatible-pair bound.


Scope: no absence-of-order-disagreement hypothesis, longest-path assumption, or minimal-counterexample hypothesis is used. This does not prove existence of a K4 minor for any choice of covers and does not close the grand conjecture. The live conditional degree-four result remains a complementary statement.