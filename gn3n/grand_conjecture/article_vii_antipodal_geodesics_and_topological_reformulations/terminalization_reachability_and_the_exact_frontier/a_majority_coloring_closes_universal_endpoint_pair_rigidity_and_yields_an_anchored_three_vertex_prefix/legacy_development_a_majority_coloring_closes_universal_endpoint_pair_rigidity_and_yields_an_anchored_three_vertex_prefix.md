# A majority coloring closes universal endpoint-pair rigidity and yields an anchored three-vertex prefix — preserved pre-item development

## A functional-graph coloring lemma

Let F be a finite directed graph with no loops in which every vertex has outdegree zero or one. Then V(F) has a two-coloring with the following properties:
(1) no directed walk of two edges is monochromatic (the first and third vertices may coincide);
(2) every edge whose head has outdegree zero is bichromatic.

Proof. Each weak component is either a tree directed toward a vertex of outdegree zero, or consists of one directed cycle with trees directed toward that cycle. This follows by iterating the unique outgoing edge from each vertex.

For a component with a terminal vertex, color by parity of distance to that vertex. Every edge is then bichromatic.

For a cycle component, alternate colors along the cycle. If the cycle is even, every cycle edge is bichromatic. If it is odd, use alternating colors around all but the closing edge, leaving exactly one monochromatic cycle edge. Both neighboring cycle edges are bichromatic, so no two-edge cycle walk is monochromatic. A two-cycle is colored with opposite colors. Color each attached tree vertex opposite its parent. All noncycle edges are bichromatic, so they cannot create a monochromatic two-edge walk. There are no terminal vertices in a cycle component, so (2) is vacuous there. QED.

Consequently one color class has size at least ceil(|V(F)|/2). The lemma is a graph-theoretic coloring construction, not a small-order assertion.

## Majority augmentation under universal initial-pair rigidity

For a boundary 3-tournament H and a vertex b, the centered tournament T_b has arc u->v precisely when (u,b,v) is tight. A universal source a in T_b satisfies (a,b,z) tight for every z outside {a,b}.

Let r>=2 and n>=2r-1. Suppose every r-subset of V(H) is Hamiltonian. Choose one actual Hamilton order P_S of each r-subset S. Assume that for every chosen word
P_S=(a,b,...)
its first vertex a is a universal source of T_b.

Then H has a tight path of order r+1, constructed by a single endpoint extension of one of the chosen words.

Proof. Let D be the vertices occurring second in at least one chosen word. For b in D define f(b)=a, where a precedes b in such a word. This is well-defined: a tournament has at most one universal source. Also f(b)!=b.

Form the partial functional digraph with arc b->f(b) for every b in D, and no outgoing arc from vertices outside D. Apply the coloring lemma and choose a monochromatic r-set S inside a color class of size at least ceil(n/2)>=r. Write its chosen Hamilton order as (a,b,...). Then the arc b->a is monochromatic.

Property (2) implies a in D, since otherwise this edge would enter a vertex of outdegree zero. Put z=f(a). Property (1) implies z has the opposite color: the walk b->a->z cannot be monochromatic. Thus z is outside S (and z!=b).

By definition z is a universal source of T_a, so (z,a,b) is tight. Hence
(z,a,b,...)
is a vertex-simple (r+1)-path. Its only new triple is (z,a,b), and every other triple is inherited from P_S. QED.

In the odd uniform residue n=2r+1, the r-vertex complement of this path is Hamiltonian. Thus the universal initial-pair rigidity branch is closed by an ACTUAL spanning two-cover. The argument uses Hamilton orders on every r-subset and an ambient majority color class; it cannot be replaced by deletion-criticality of one (r+1)-set.

The terminal version is identical: if in every selected Hamilton word ending (...,b,a), the last vertex a is a universal sink of T_b, use arcs b->a and the same coloring. A monochromatic chosen word has z=f(a) outside its support and (b,a,z) tight, so append z.

## Consequence: a reversed initial pair has a genuine three-vertex prefix

Assume now the full odd uniform residue: n=2r+1, every r-set is Hamiltonian, and every (r+1)-set is non-Hamiltonian.

It is impossible that every Hamiltonian r-word begins (a,b,...) with a a universal source of T_b. Therefore there is an actual maximum word
P=(a,b,p_3,...,p_r)
and a vertex u outside {a,b} such that
(u,b,a)
is tight.

The vertex u need not be exterior to P. It cannot equal p_3, since (a,b,p_3) is tight and its boundary reverse is not. This is an anchored ordered prefix, not merely a Hamiltonian three-support.

Likewise there is a maximum word ending (...,b,a) and a vertex v outside {a,b} for which (a,b,v) is tight.

## A third positioned reversal obtained from the prefix

For r>=4, take P and u above. Choose an r-set B disjoint from V(P) union {u}, and display any Hamilton word
B=(b_1,...,b_r).
Such a support exists: if u is in P, there are r+1 exterior vertices to choose from; otherwise there are exactly r. Uniform Hamiltonicity supplies its order.

For every i the vertex b_i is exterior to P. Nonextension of the displayed maximum path P at its initial end forces (b_i,a,b) non-tight, so (b,a,b_i) is tight.

For 1<=i<=3, if (a,b_i,b_{i+1}) were tight, the word
(u,b,a,b_i,b_{i+1},...,b_r)
would be tight. Its triples are the prefix (u,b,a), the seam (b,a,b_i), the hypothesized seam (a,b_i,b_{i+1}), and the inherited B-tail triples. Its order is r+4-i>=r+1 and all its vertices are distinct. This would contradict maximality and would give a spanning two-cover after taking an (r+1)-vertex contiguous subpath.

Consequently
(b_2,b_1,a), (b_3,b_2,a), (b_4,b_3,a)
are all tight.

Thus the two-edge endpoint reversal from 292 can be strengthened to an existential three-edge reversal using the global uniform hypothesis, rather than assumed endpoint availability on a prescribed support. The prefix proof also states exactly which seam would give a longer path immediately.

## Audit boundary and remaining step

The coloring theorem closes the universal-source (and universal-sink) branch. It does NOT close the unrestricted odd residue: when an initial pair is not universally rigid, the algorithm returns the anchored prefix (u,b,a), and the tail test may force three reversed seams instead of producing an extension.

No claim of global progress is inferred from a bounded reversal fan alone. The useful retained information is the actual three-vertex prefix, its prescribed terminal pair, the disjoint maximum tail, and the checked augmentation word. A further proof must exploit that certificate to obtain a tight seam, increase an ordered prefix by a proved terminating process, or construct a different spanning two-cover. Those assertions are not proved here.
