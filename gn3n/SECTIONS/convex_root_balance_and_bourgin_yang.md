# Convex root balance and Bourgin–Yang multiplicity

**Summary:** An explicit odd map yields a proper face in which every chamber root has a directed return cycle, with a rigorous switch-separation dimension bound.

## Statement

The explicit odd barycentric root map has strictly positive balance on every chamber of each zero's carrier face, so every occurring root lies on a directed cycle. Uniform first-to-last switch separation L gives zero-set dimension at least L+2, refined by the rank of the occurring roots.

## Body

## Balance, circulation, and multiplicity of zeros

### Convex balance is directed circulation

Let \(I\) be a finite coordinate set and let
\[
E\subseteq I\times I
\]
be a directed graph, allowing loops and regarding a loop as a cycle of length one. Set \(\operatorname{conv}(\varnothing)=\varnothing\). Associate to an arc \(i\to j\) the type-\(A\) root
\[
\rho_{ij}=e_i-e_j.
\]

**Proposition 4 (root-balance criterion).**
\[
\boxed{
0\in\operatorname{conv}\{\rho_{ij}:(i,j)\in E\}
\iff
E\text{ contains a directed cycle}.
}
\]

**Proof.** If
\[
i_1\to i_2\to\cdots\to i_k\to i_1
\]
is a directed cycle, then
\[
\sum_{\ell=1}^k
(e_{i_\ell}-e_{i_{\ell+1}})
=
0,
\]
so the origin lies in the convex hull after dividing by \(k\).

Conversely, suppose
\[
\sum_{(i,j)\in E}\lambda_{ij}(e_i-e_j)=0,
\qquad
\lambda_{ij}\ge0,
\qquad
\sum\lambda_{ij}=1.
\]
The coefficients form a nonzero nonnegative circulation: at every coordinate, total outgoing weight equals total incoming weight. Any finite nonzero circulation contains a directed cycle. \(\square\)

Thus a convex zero of the extreme-switch root map is not merely an analytic event. It is a finite directed recurrence among switch-front coordinates.

### Balanced faces of the Coxeter complex

A face of the permutahedron is an ordered partition
\[
B_1|\cdots|B_k.
\]
Its chamber vertices are the permutations obtained by ordering the vertices inside each block while retaining the block order.

Suppose a set of chambers in one such face has root labels whose convex hull contains the origin. By Proposition 4, after discarding zero coefficients the support contains a directed switch-front cycle
\[
x_1\to x_2\to\cdots\to x_t\to x_1.
\]

This is the basic combinatorial output of root topology.

The converse viewpoint is equally useful: a directed cycle is already a balanced convex configuration. Hence later arguments can work directly with a finite cycle rather than with a continuous map once a balanced face has been obtained.

### Borsuk–Ulam as the baseline

Let \(S^d\) be the antipodal Coxeter sphere or an antipodal subdivision of it. An odd continuous map
\[
f:S^d\to\mathbb R^q
\]
satisfies
\[
f(-x)=-f(x).
\]

When \(q\le d\), the Borsuk–Ulam theorem forces
\[
f^{-1}(0)\ne\varnothing.
\]

For the root program, one constructs such a map by assigning root data to chambers or face barycenters and extending over an antipodal cellular or barycentric subdivision. A zero means that the root labels of one carrier face balance at the origin.

This is already stronger than seeking a complementary edge on the chamber graph: a zero may be supported by several chambers around a cell.

But ordinary Borsuk–Ulam says only that at least one zero exists. The later program needed multiplicity.

### The Bourgin–Yang strengthening

We use the standard Bourgin–Yang dimension principle in the following form.

**Theorem 5 (Bourgin–Yang, dimension form).** Let
\[
f:S^d\to\mathbb R^q
\]
be continuous and odd, with \(q\le d\). Then the zero set
\[
Z=f^{-1}(0)
\]
has topological dimension at least
\[
d-q.
\]

The relevant feature is the lower bound on the **whole zero locus**, not merely nonemptiness.

Consequently, whenever the GN3 root construction is shown to take values in a \(q\)-dimensional linear subspace of a \(d\)-dimensional antipodal sphere, one obtains
\[
\dim Z\ge d-q.
\]

This is the rigorous span–multiplicity principle needed here. Any more specific numerical statement must come from a separately proved bound on \(q\).

### Switch span and dimension saving

Large first-to-last switch separation can force many root coordinates to be absent from the image. This is the source of the dimension saving contemplated in the brainstorm work.

The logical chain must be kept explicit:

1. prove a coordinate-subspace bound
   \[
   \phi(\mathcal C)\subseteq W,
   \qquad
   \dim W=q;
   \]
2. construct the odd continuous root map
   \[
   f:S^d\to W;
   \]
3. apply Bourgin–Yang to obtain
   \[
   \dim f^{-1}(0)\ge d-q;
   \]
4. separately convert this zero-set dimension into a statement about balanced faces or independent root circulations.

The next subsection supplies an explicit equivariant extension and a precise switch-span bound. The zero-set bound must still be distinguished from any assertion about the number of independent directed cycles.

### Why multiplicity matters

One balanced face may be accidental. A positive-dimensional balanced locus is qualitatively different.

A positive-dimensional zero set contains a family of balanced points. This does not by itself force multiple independent switch-front cycles, or even different cycle supports: many convex representations can use the same roots. Converting topological dimension into distinct combinatorial recurrences requires an additional argument.

That is the point at which topology becomes potentially useful to Articles III–VI. Those articles are strong at converting **repeated local obstruction** into:

- endpoint reversals;
- common carriers;
- parallel middles;
- bounded Hamiltonian supports;
- strict potential descent.

Bourgin–Yang is therefore not a replacement for the GN3 machinery. Its intended role is to supply enough recurrence for that machinery to act.

### The remaining conversion problem

Root balance and the exact theorem still live at different levels.

A balanced root face says that a convex combination of compressed extreme-defect vectors vanishes. It does not yet say that one actual spanning order has intersecting defect intervals, nor that one actual state lies in both reachability regions of the exactified memory lift.

The next Section records the strongest combinatorial consequences that can be extracted from a balanced face before invoking the GN3-specific local structure.


## Positive balance on every chamber and the switch-separation bound

### An explicit odd extension and its carrier faces

Assume that no spanning order has at most one color change. Put \(m=n-2\). Every status word then has at least two switches. Number a switch by the position immediately before it, and write \(a(\pi)<b(\pi)\) for the first and last switch positions. Thus \(1\leq a<b\leq m-1\). Let
\[
\bar b(\pi)=m-b(\pi),\qquad
\phi(\pi)=e_{a(\pi)}-e_{\bar b(\pi)}.
\]
The identities for reversal give \(\phi(\pi^{\rm rev})=-\phi(\pi)\).

Realize the centered permutahedron \(P\) in the hyperplane \(\sum_{v\in V}x_v=0\) by assigning to the vertex indexed by \(\pi=(v_1,\ldots,v_n)\) the coordinates
\[
x_{v_i}=i-\frac{n+1}{2}.
\]
Then \(-\pi=\pi^{\rm rev}\) as vertices of \(P\), and radial projection identifies \(\partial P\) equivariantly with \(S^{n-2}\). This boundary is dual to the Coxeter sphere used earlier; its vertices, rather than its maximal simplices, are indexed by permutations.

For every nonempty proper face \(F\) of \(P\), let \(\mathcal V(F)\) be its permutation vertices, and assign to its barycenter \(z_F\) the vector
\[
\Phi(z_F)=\frac1{|\mathcal V(F)|}
\sum_{\pi\in\mathcal V(F)}\phi(\pi).
\]
Extend affinely over each simplex of the barycentric subdivision of \(\partial P\). Nested faces determine these simplices, so the prescriptions agree on intersections. Negation sends \(z_F\) to \(z_{-F}\) and negates its assigned vector; hence \(\Phi\) is a continuous odd piecewise-linear map. In particular this construction needs no unproved rook-adjacency condition.

**Theorem 6.1 (positive balance on a carrier face).** For every \(x\in\Phi^{-1}(0)\), the unique face \(F\) of \(P\) whose relative interior contains \(x\) admits numbers
\[
\lambda_\pi>0\quad(\pi\in\mathcal V(F)),\qquad
\sum_{\pi\in\mathcal V(F)}\lambda_\pi=1,
\]
such that
\[
\sum_{\pi\in\mathcal V(F)}\lambda_\pi\phi(\pi)=0.
\]
Consequently every nonzero root occurring in \(F\) lies on a directed cycle of roots occurring in \(F\). A zero root is a loop and is already an exact diagonal.

**Proof.** Let the smallest barycentric simplex containing \(x\) have face chain
\[
F_0\subsetneq\cdots\subsetneq F_s=F.
\]
Its barycentric coefficients \(t_0,\ldots,t_s\) at \(x\) are all positive. Expanding the definition of \(\Phi\), assign
\[
\lambda_\pi=
\sum_{j:\,\pi\in\mathcal V(F_j)}
\frac{t_j}{|\mathcal V(F_j)|}.
\]
Every vertex of \(F\) receives at least \(t_s/|\mathcal V(F)|>0\). The weights sum to one and give the required balance. The assertion that \(x\) lies in the relative interior of \(F\) follows likewise from its positive barycentric coefficient at the interior point \(z_F\).

After grouping equal roots, these weights form a circulation that is strictly positive on every occurring arc. To see that an arc \(i\to j\) is on a directed cycle, let \(U\) be all vertices reachable from \(j\). If \(i\notin U\), no arc leaves \(U\), while the arc \(i\to j\) brings positive flow into \(U\). Summing conservation over \(U\) is a contradiction. Thus there is a directed path from \(j\) back to \(i\). \(\square\)

The conclusion is stronger than the existence of a single cycle among some labels. In particular,
\[
\{a(\pi):\pi\in\mathcal V(F)\}
=
\{\bar b(\pi):\pi\in\mathcal V(F)\}.
\]
Every first-switch coordinate realized in the face also occurs as a reflected last-switch coordinate, and conversely. More precisely, every weakly connected component of the directed root graph of \(F\) is strongly connected: an edge between distinct strongly connected components could not lie on a directed cycle.

### The dimension bound with all constants specified

**Theorem 6.2 (switch separation and zero-set dimension).** Suppose that
\[
b(\pi)-a(\pi)\geq L\geq1
\]
for every spanning order, and put \(K=m-L\). Then the map just constructed has
\[
\dim\Phi^{-1}(0)\geq L+2.
\]
More precisely, let \(G\) be the undirected graph on \(I=\{1,\ldots,K-1\}\) whose edges are the pairs supporting nonzero roots \(\phi(\pi)\), and let \(c(G)\) count all its connected components, including isolated vertices. Then
\[
\dim\Phi^{-1}(0)
\geq n-2-|I|+c(G).
\]
Every zero has the positive-balance conclusion of Theorem 6.1 in a proper face.

**Proof.** For each permutation,
\[
a(\pi)+\bar b(\pi)
=m-(b(\pi)-a(\pi))\leq K.
\]
Both summands are positive, so every root coordinate belongs to \(I\). Thus the image lies in the sum-zero subspace of \(\mathbb R^{K-1}\), whose dimension is
\[
K-2=n-L-4.
\]
The hypotheses imply \(L\leq m-2\), so this dimension is nonnegative. The barycentric averages and affine extensions remain in that subspace. The Bourgin–Yang theorem stated above now gives
\[
(n-2)-(n-L-4)=L+2
\]
as the lower bound for the dimension of the zero set.

For the refinement, the span of the occurring roots has dimension \(|I|-c(G)\). Indeed, all roots sum to zero on each connected component of \(G\). Conversely, a spanning tree in each component supplies edge differences spanning its entire sum-zero subspace, by summing differences along tree paths. This proves the asserted rank and the refined Bourgin–Yang bound. If every root is zero, the image subspace is zero-dimensional and the whole boundary is the zero set. \(\square\)

Thus failure of the one-change target always yields a zero set of dimension at least three, by taking \(L=1\). In particular a proper face with the positive balance of Theorem 6.1 exists. This argument uses only reversal-complement symmetry of the permutation words. The consistent triple rule must still enter when converting these witnesses to tight paths.

### What the stronger balance permits, and what it does not

Within a carrier face supplied above, an arbitrary chamber may now be chosen: its first and reflected last switch belong to a return cycle supported in that same face. This removes the need to restrict attention to the chambers of one preselected circulation. It supplies a uniform version of the input to block-separation arguments in [[topological_recurrence_to_local_gn3_structure]], although those arguments still require their stated separation of determining positions.

The dimension bound is not a lower bound on the number of independent cycles. For a fixed nonzero root \(\rho\), the odd map \(x\mapsto x_1\rho\) on \(S^d\) has a zero set \(S^{d-1}\), although its image spans only the one line through \(\rho\) and \(-\rho\). This illustrates the logical limitation, not a boundary-tournament counterexample. The new discrete conclusion comes instead from the strictly positive coefficients on every chamber of a carrier face.

Neither theorem produces a one-change order or a reachability intersection. The remaining task is to use the simultaneous return witnesses, together with the base-independent triple rule or the auxiliary vertex, to obtain an actual directed one-change geodesic.


### Automatic switch separation in a genuine counterexample

For the original switch root, the numerical hypothesis of Theorem 6.2 improves automatically under the actual two-cover obstruction.

**Proposition 6.3.** If \(\operatorname{pc}(H)>2\), then every spanning-order status word satisfies
\[
b(\pi)-a(\pi)\ge3.
\]

**Proof.** If the word has at most one switch, the usual cut-and-reverse argument gives a two-cover. Suppose it has at least two switches and \(b-a\le2\). If \(b=a+1\), cut between \(v_{a+1}\) and \(v_{a+2}\). All status positions wholly inside the two resulting blocks have the same color, namely the color outside the isolated middle run. If \(b=a+2\), cut between \(v_{a+2}\) and \(v_{a+3}\); again all statuses wholly inside the two blocks have one common color. If that color is \(1\), the displayed blocks are tight; if it is \(0\), reverse both blocks. Either way they form a spanning two-cover, a contradiction. \(\square\)

Thus in a genuine counterexample the switch-root map of Theorem 6.2 may be used with \(L=3\), and
\[
\dim\Phi^{-1}(0)\ge5.
\]
This strengthens the amount of recurrence available from the switch compression, although it remains a compressed invariant.

### Exact inversion roots

The exact inversion-window criterion in [[spanning_orders_and_defect_helly]] supplies a second odd root map that is tied directly to the theorem rather than to the stronger one-change target.

Assume \(\operatorname{pc}(H)>2\), put \(m=n-2\), and for every spanning order define
\[
p(\pi)=\min\{i:\epsilon_i=0\},\qquad
q(\pi)=\max\{i:\epsilon_i=1\},\qquad
c(\pi)=m+1-q(\pi).
\]
A counterexample has both colors in every status word and satisfies
\[
\delta(\pi):=q(\pi)-p(\pi)-1
=m-\bigl(p(\pi)+c(\pi)\bigr)\ge1.
\]
Define the **exact inversion root**
\[
\psi(\pi)=e_{p(\pi)}-e_{c(\pi)}.
\]
Reversal exchanges \(p\) and \(c\), so
\[
\psi(\pi^{\rm rev})=-\psi(\pi).
\]

Use the same centered permutahedron and barycentric subdivision as above. For each nonempty proper face \(F\), assign its barycenter
\[
\Psi(z_F)=\frac1{|\mathcal V(F)|}\sum_{\pi\in\mathcal V(F)}\psi(\pi),
\]
and extend affinely along nested face chains.

**Theorem 6.4 (positive balance for the exact obstruction).** The map
\[
\Psi:\partial P\longrightarrow \mathbb R^m
\]
is continuous and odd. For every \(x\in\Psi^{-1}(0)\), if \(F\) is the unique face whose relative interior contains \(x\), there are coefficients
\[
\lambda_\pi>0\qquad(\pi\in\mathcal V(F)),\qquad
\sum_{\pi\in\mathcal V(F)}\lambda_\pi=1,
\]
such that
\[
\sum_{\pi\in\mathcal V(F)}\lambda_\pi\psi(\pi)=0.
\]
Consequently every exact inversion root occurring among the chambers of \(F\) lies on a directed cycle of exact inversion roots occurring in \(F\).

**Proof.** Oddness is the reversal identity above. The positive-coefficient argument is identical to Theorem 6.1: expand a zero in its smallest barycentric face chain. The top face contributes positive weight to every one of its chamber vertices. Grouping equal roots produces a nonzero nonnegative circulation strictly positive on every occurring arc, so every arc has a directed return path. \(\square\)

This gives precisely the coordinated-face structure sought for the actual two-cover obstruction: **every chamber of one proper face participates in a directed cycle whose tail is its first non-tight position and whose head is its reflected last tight position.**

### Exact deficiency and Bourgin--Yang

The dimension saving now has an exact combinatorial meaning.

**Theorem 6.5 (deficiency multiplicity).** Suppose
\[
\delta(\pi)\ge D\ge1
\]
for every spanning order. Then
\[
\dim\Psi^{-1}(0)\ge D+2.
\]

**Proof.** The inequality \(\delta\ge D\) is
\[
p(\pi)+c(\pi)\le m-D.
\]
Both coordinates are positive, hence every exact root uses only
\[
I_D=\{1,\ldots,m-D-1\}.
\]
Therefore the image of \(\Psi\) lies in the sum-zero subspace of
\(\mathbb R^{I_D}\), of dimension
\[
|I_D|-1=m-D-2=n-D-4.
\]
Bourgin--Yang on \(\partial P\cong S^{n-2}\) gives
\[
\dim\Psi^{-1}(0)\ge(n-2)-(n-D-4)=D+2.
\]
As in Theorem 6.2, the target dimension may be sharpened to the rank of the undirected support graph of the occurring exact roots. \(\square\)

In particular every counterexample has an exact-root zero set of dimension at least three. If the best spanning order still leaves a larger uniform deficiency, the zero locus grows by exactly the same amount.

### The canonical partial two-cover carried by one exact root

The exact deficiency is not merely a numerical gap. It counts uncovered vertices in a canonical pair of tight paths.

For a spanning order \(\pi=(v_1,\ldots,v_n)\), define
\[
P_\pi=(v_1,\ldots,v_{p+1}),
\qquad
Q_\pi=(v_n,v_{n-1},\ldots,v_{q+1}).
\]
The path \(P_\pi\) is tight because every status before \(p\) is \(1\). The path \(Q_\pi\) is tight because every status after \(q\) is \(0\), so reversal makes all its consecutive triples tight. They are disjoint in a counterexample, and the uncovered vertices are exactly
\[
v_{p+2},\ldots,v_q,
\]
whose number is
\[
q-p-1=\delta(\pi).
\]

Thus
\[
\boxed{\text{an exact root }p\to c\text{ is a canonical two-path cover with a }\delta\text{-vertex hole}.}
\]

At deficiency one, write \(x=v_{p+2}=v_q\). Then
\[
H-x=P_\pi\mid Q_\pi
\]
is an explicit deletion two-cover. Moreover
\[
(x,v_{p+1},v_p)
\quad\text{and}\quad
(x,v_{q+1},v_{q+2})
\]
are tight: the first follows from \(\epsilon_p=0\) by boundary reversal, while the second is exactly \(\epsilon_q=1\). Hence the omitted vertex \(x\) reverses the displayed terminal edge of **both** canonical paths.

The exact-root circulation therefore coordinates not abstract switch fronts but a family of partial two-covers. Its lowest nontrivial stratum consists of deletion covers with a single omitted vertex simultaneously controlling the two exposed ends. This is the natural discrete object to synchronize in the next Section.


## Metadata

- ID: convex_root_balance_and_bourgin_yang
- Kind: section
- Version: 7
- Math version: 5
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — crystallized, version 4: Balance, circulation, and multiplicity of zeros
- Subsection 2 — HOT, version 3: Positive balance on every chamber and the switch-separation bound
