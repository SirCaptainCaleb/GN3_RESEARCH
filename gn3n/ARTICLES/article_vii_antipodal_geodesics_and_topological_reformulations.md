# Article VII — antipodal geodesics, defect Helly theory, and topological compression

---

## Section — Spanning orders and defect Helly theory

<!-- section_id: spanning_orders_and_defect_helly -->

### Defect intervals and the exact Helly criterion


### Spanning orders and status words

Let \(H\) be a boundary \(3\)-tournament on vertex set \(V\), and let
\[
\pi=(v_1,\ldots,v_n)
\]
be a spanning order. Write
\[
\epsilon_i(\pi)=
\begin{cases}
1,&(v_i,v_{i+1},v_{i+2})\text{ is tight},\\
0,&(v_i,v_{i+1},v_{i+2})\text{ is non-tight},
\end{cases}
\qquad 1\le i\le n-2.
\]
The word
\[
\epsilon_1(\pi)\cdots \epsilon_{n-2}(\pi)
\]
is the status word of \(\pi\).

The two-cover problem is already visible in one status word. Put a cut between \(v_j\) and \(v_{j+1}\), where \(1\le j\le n-1\). Every consecutive triple wholly contained in either side must be tight if the two inherited blocks are to be tight paths. A non-tight triple centered at status position \(i\) is harmless precisely when the cut separates one of its two adjacent vertex pairs.

It is convenient to encode this in the defect line from [[defect_lines_and_spanning_order_compression_the_defect_line_identity]]. Let the possible cuts be the vertices
\[
1,\ldots,n-1,
\]
and for every non-tight status position \(i\) put the defect edge
\[
I_i=\{i,i+1\}.
\]
Thus the defect family is an interval family on a line.

### The exact Helly theorem

**Theorem 1 (defect-interval Helly criterion).** A spanning order \(\pi\) yields a spanning two-cover by one cut if and only if
\[
\bigcap_{\epsilon_i(\pi)=0} I_i\ne\varnothing.
\]
Equivalently, the defect-line graph has vertex-cover number at most one.

**Proof.** A cut \(j\) leaves a non-tight triple inside one of the two inherited blocks exactly when \(j\notin I_i\). Hence both inherited blocks are tight exactly when \(j\) belongs to every defect interval. This is the asserted intersection condition. The graph formulation is the same statement, because the defect intervals are precisely the edges of the defect line. \(\square\)

The theorem is order-relative. Quantifying over all spanning orders gives the exact existence formulation
\[
\boxed{
\operatorname{pc}(H)\le2
\iff
\exists\pi\text{ such that }\bigcap_{\epsilon_i(\pi)=0}I_i\ne\varnothing.
}
\]

Because intervals on a line are Helly, failure has an especially sharp witness.

**Corollary 2 (separated defect pair).** If \(\pi\) does not yield a two-cover, then there are two non-tight positions \(i<j\) with
\[
I_i\cap I_j=\varnothing.
\]
Equivalently,
\[
j\ge i+2.
\]

Thus every bad spanning order contains two separated defects. There is no need to retain the entire defect set merely to certify failure.

### Reversal and the antipodal defect pair

Let
\[
\pi^{\rm rev}=(v_n,\ldots,v_1).
\]
Boundary antisymmetry gives
\[
\epsilon_i(\pi^{\rm rev})
=
1-\epsilon_{n-1-i}(\pi).
\]
Thus reversal reflects the status positions and complements the colors.

Consequently a counterexample has two simultaneous interval statements. Every spanning order contains two separated non-tight defects, and its reverse contains two separated non-tight defects corresponding to two separated tight positions of the original order. In the Freudenthal language introduced in the next Section, every bad chamber therefore carries a separated defect pair, and the antipodal chamber carries the complementary pair.

This is the exact supported content of the earlier informal phrase that every bad Freudenthal simplex “contains a pair.” No stronger mysterious pair theorem is assumed.

### Extreme defects and switch coordinates

The separated pair can be compressed further by choosing extreme witnesses. When the status word contains both colors, let
\[
a(\pi)=\text{first switch position},
\qquad
b(\pi)=\text{last switch position}.
\]
Equivalently, \(a\) and \(b\) mark the first and last boundaries between monochromatic runs. The reflected terminal coordinate
\[
\bar b(\pi)=m-b(\pi),
\qquad m=n-2,
\]
is chosen so that reversal exchanges \(a\) and \(\bar b\).

These extreme coordinates lose information: they remember only the outermost failure of a one-run description, not the complete defect family. Their virtue is topological. They are the coordinates from which the later rook labels and root vectors are built.

This distinction will remain important throughout the article:

- the defect intervals encode the **exact two-cover condition**;
- extreme switch coordinates are a **compression** designed for topology.

The later topological argument is useful only if its compressed recurrence can ultimately be returned to the exact defect or support formulations.


---

## Section — The Norine–GN3 dictionary and Freudenthal geometry

<!-- section_id: norine_gn3_dictionary_and_freudenthal_geometry -->

### Geodesic chambers, memory, and the stronger general route


### Cube geodesics, permutations, and Freudenthal simplices

Let \(V\) be an \(n\)-element label set. Identify the vertices of the cube \([0,1]^V\) with subsets of \(V\). A monotone geodesic from \(\varnothing\) to \(V\) adds every label exactly once and is therefore specified by a permutation
\[
\pi=(v_1,\ldots,v_n),
\qquad
S_i=\{v_1,\ldots,v_i\}.
\]
The convex hull
\[
\Delta_\pi
=
\operatorname{conv}\{
\mathbf1_{S_0},\ldots,\mathbf1_{S_n}
\}
\]
is a maximal simplex of the standard staircase, or Freudenthal, triangulation of the cube. Conversely every maximal simplex arises in this way.

Thus
\[
\boxed{
\text{monotone antipodal cube geodesics}
\longleftrightarrow
\text{permutations}
\longleftrightarrow
\text{maximal Freudenthal simplices}.
}
\]

This is the basic dictionary behind the Norine analogy. It is an exact identification, not a metaphor.

Every maximal simplex contains the long diagonal
\[
[\mathbf0,\mathbf1].
\]
The link of that diagonal consists of chains of nonempty proper subsets of \(V\). It is the barycentric subdivision of the boundary of an \((n-1)\)-simplex and hence an \((n-2)\)-sphere. Cube complementation
\[
A(x)=\mathbf1-x
\]
sends \(\Delta_\pi\) to \(\Delta_{\pi^{\rm rev}}\); on the link it is fixed-point-free. This is the type-\(A\) Coxeter sphere on which the later antipodal topology lives.

### One-step data and two-step memory

The shared geometry should not obscure a crucial difference in the local data.

For an ordinary antipodal cube-edge coloring, the color encountered along a geodesic is attached to one cube edge. It depends on the present coordinate step. This is one-step data.

For a boundary tournament, the local status is
\[
h(u,v,w)=
\begin{cases}
1,&(u,v,w)\text{ is tight},\\
0,&(u,v,w)\text{ is non-tight},
\end{cases}
\]
and along
\[
\pi=(v_1,\ldots,v_n)
\]
the word is
\[
h(v_1,v_2,v_3),\ldots,h(v_{n-2},v_{n-1},v_n).
\]
The color therefore depends on three successive directions, or equivalently on two steps of memory.

Boundary antisymmetry is
\[
h(w,v,u)=1-h(u,v,w).
\]
Thus reversal of a geodesic complements the local word exactly as antipodality should, but the coloring is not an ordinary edge coloring of the bare cube.

Geometrically, \(h(u,v,w)\) is naturally attached to the monotone three-step flag
\[
S
\subset
S\cup\{u\}
\subset
S\cup\{u,v\}
\subset
S\cup\{u,v,w\},
\]
and is independent of the base set \(S\). This translation invariance is one of the strongest formal distinctions from an arbitrary cube coloring.

### The stronger geodesic route is legitimate

There is a natural stronger problem suggested by the Norine analogy.

**Candidate memory-two geodesic conjecture.** Let \(V\) be finite and let
\[
h:\{(u,v,w)\in V^3:u,v,w\text{ distinct}\}\to\{0,1\}
\]
satisfy
\[
h(w,v,u)=1-h(u,v,w).
\]
Must there exist a permutation
\[
(v_1,\ldots,v_n)
\]
whose word
\[
h(v_1,v_2,v_3),\ldots,h(v_{n-2},v_{n-1},v_n)
\]
has at most one color change?

No assertion is made here that this conjecture is true. It is stated because it is the precise stronger theorem that the current topology repeatedly threatens to prove.

If it is true, that is not an undesirable outcome. It would be a genuine generalization of the strengthened Norine-style demand that the antipodal path be geodesic, hence use every coordinate exactly once. Boundary tournaments form a special subclass of these reversal-complement memory colorings, so the conjecture would immediately imply the one-change statement for \(H\). After the auxiliary exactification in the fourth Section, the same general theorem would imply the original two-cover conjecture itself.

Accordingly there are two legitimate research programs:

1. exploit GN3-specific structure and prove only what is needed for boundary tournaments;
2. formulate and prove a more general antipodal memory-geodesic theorem, then reduce GN3 to it.

The second route should not be discouraged merely because it is stronger. What must be avoided is only an **implicit** generalization in which the stronger theorem is never stated and the reduction to GN3 is never checked.

### What GN3 has that the general memory problem need not have

The boundary-tournament specialization supplies much more than reversal complementarity. For every unordered triple, fixing the middle vertex gives a local tournament on the other two vertices. Consequently a failed displayed triple has a specific reversed tight triple. Repeated failures generate:

- endpoint reversals;
- common exterior carriers;
- parallel-middle configurations;
- Hamiltonian four- and five-supports;
- strict repartition descents.

Those mechanisms are developed in Articles III–VI. They are exactly the additional leverage available if the general memory-geodesic conjecture proves too strong.

This distinction should guide the topology. A purely antipodal argument using only the Coxeter sphere and reversal-complement symmetry may naturally prove a theorem beyond GN3. A proof that invokes local tournaments or the forced reversal of a failed triple has crossed back into genuinely GN3-specific territory.

### A cochain viewpoint

There is a useful algebraic way to summarize the difference.

An ordinary cube-edge coloring may be treated as degree-\(1\) local data on oriented cube edges. The GN3 status behaves instead as a translation-invariant degree-\(3\) local datum on monotone three-edge flags: translating the base subset \(S\) does not change the value attached to the direction triple \(u,v,w\).

Along one chamber, the discrete derivative
\[
\epsilon_{i+1}-\epsilon_i
\]
records switch positions. Thus the switch pattern is the one-dimensional coboundary of the local color word along that chamber, while the underlying color itself comes from a higher-memory translation-invariant rule.

This language is not needed for the proofs below, but it deserves a numbered place because future topology may need to distinguish exactly these two levels: arbitrary antipodal edge data versus translation-invariant higher-memory data.

### Working principle

The topology of the chamber space is shared with Norine-style cube problems. The local algebra is not. Article VII will keep both routes open.

Whenever an argument uses only the shared chamber topology, we will ask whether it proves the candidate memory-two geodesic conjecture and, if so, state that stronger implication explicitly. Whenever it uses boundary antisymmetry beyond mere reversal complementarity, we will identify the GN3-specific mechanism that enters.

This separation lets a future proof pivot honestly in either direction.


---

## Section — The memory lift and exact antipodal geodesics

<!-- section_id: memory_lift_and_exact_antipodal_geodesics -->

### The memory lift, antipodality, and zero detour


### The memory-lift graph

The staircase triangulation identifies spanning orders with cube geodesics, but the GN3 color at one step depends on three successive directions. Introduce a ranked graph \(\Gamma_n\) that stores precisely this missing memory.

Its vertices are poles \(s,t\) and states
\[
(\sigma,S,u,v),
\]
where \(\sigma\in\{0,1\}\), \(u\ne v\), and
\[
S\subseteq V\setminus\{u,v\}.
\]
Give such a state rank \(|S|+1\), with \(r(s)=0\) and \(r(t)=n\).

Join \(s\) to every state
\[
(\sigma,\varnothing,u,v).
\]
Join
\[
(\sigma,S,u,v)
\longrightarrow
(\sigma,S\cup\{u\},v,w)
\]
whenever
\[
w\notin S\cup\{u,v\},
\]
and join every rank-\((n-1)\) state to \(t\).

Color a source edge by \(\sigma\), an internal edge by
\[
h(u,v,w),
\]
and a terminal edge by \(1-\sigma\).

The underlying graph depends only on \(n\). The boundary tournament enters only through the internal edge colors.

### Antipodal involution and cube projection

Define
\[
A(s)=t,\qquad A(t)=s,
\]
and
\[
A(\sigma,S,u,v)
=
\bigl(
\sigma,\,
V\setminus(S\cup\{u,v\}),\,
v,u
\bigr).
\]
This is fixed-point-free.

An internal edge carrying \(u,v,w\), when mapped by \(A\) and read in increasing-rank direction, carries \(w,v,u\). Hence its color is complemented by
\[
h(w,v,u)=1-h(u,v,w).
\]
Source and terminal colors are also complementary.

There is an antipodal projection to the cube,
\[
p(s)=\varnothing,\qquad
p(t)=V,\qquad
p(\sigma,S,u,v)=S\cup\{u\}.
\]
Every edge projects to a cube edge and
\[
p(Ax)=V\setminus p(x).
\]

Thus \(\Gamma_n\) is a finite two-step-memory lift of the cube.

### Pole geodesics are spanning orders

Every edge changes rank by one, so
\[
d(s,t)\ge n.
\]
Given
\[
\pi=(v_1,\ldots,v_n)
\]
and \(\sigma\in\{0,1\}\), there is a length-\(n\) path
\[
s,\,
(\sigma,S_0,v_1,v_2),\,
(\sigma,S_1,v_2,v_3),\ldots,t,
\]
with the obvious indexing
\[
S_i=\{v_1,\ldots,v_i\}.
\]

Conversely, every \(s\)-\(t\) geodesic must increase rank at every step, so it chooses each label exactly once and therefore determines a unique permutation and copy index.

Hence pole geodesics are in bijection with pairs \((\sigma,\pi)\), and their color words are
\[
\sigma,\,
h(v_1,v_2,v_3),\ldots,
h(v_{n-2},v_{n-1},v_n),\,
1-\sigma.
\]

Therefore a spanning order whose internal word changes color at most once is exactly a pole geodesic with at most one internal change after choosing the appropriate copy.

### Geodesicity is the no-reuse condition

The strengthened Norine analogy becomes exact at this point.

For an arbitrary \(s\)-\(t\) walk \(W\), let \(m_v\) be the number of projected cube edges using coordinate \(v\). Since the projection joins antipodal cube vertices, every \(m_v\) is odd. Thus
\[
|W|
=
\sum_{v\in V}m_v
=
n+
2\sum_{v\in V}\frac{m_v-1}{2}.
\]

Consequently
\[
\boxed{
W\text{ is geodesic}
\iff
m_v=1\text{ for every }v.
}
\]

Zero detour is exactly the requirement that each original vertex, or each cube dimension, be used once.

This is the sharp distinction between the desired theorem and a generic antipodal-path theorem. A one-change antipodal walk that repeats a coordinate does not encode a spanning order. A theorem whose antipodal endpoints are allowed to vary likewise does not solve the distinguished-pole problem.

The topology must preserve simultaneously:

1. the prescribed poles;
2. geodesicity;
3. the two-step memory carried by the state.

### The stronger problem represented exactly

The memory lift gives an exact graph formulation of the stronger one-change spanning-order target:

\[
\boxed{
H\text{ has a one-change spanning order}
\iff
\Gamma_n(H)\text{ has a one-change pole geodesic}.
}
\]

This equivalence is useful but must not be confused with the original two-cover conjecture. A two-cover need not itself appear as a one-change spanning order of \(H\).

That distinction is the point at which the next Section begins.

> **Transition.** The memory lift makes one-change spanning orders into genuine one-change antipodal geodesics, but on \(H\) this remains potentially stronger than the two-cover conjecture. We now remove that discrepancy.


---

## Section — Auxiliary exactification and complementary path supports

<!-- section_id: auxiliary_exactification_and_complementary_supports -->

### Exactification before support-family development


### One-change orders and opposite-edge supports

Before exactifying the theorem, it is useful to record the support meaning of a one-change order.

For an ordered pair \(u,v\), let \(\mathcal F_{uv}\) consist of the sets
\[
X\subseteq V\setminus\{u,v\}
\]
for which some ordering of \(X\), followed by \(u,v\), is a tight path.

A spanning order with status word
\[
1^a0^b
\]
exists if and only if for some \(u\ne v\) there are
\[
X\in\mathcal F_{uv},
\qquad
Y\in\mathcal F_{vu}
\]
with
\[
X\sqcup Y=V\setminus\{u,v\}.
\]
Indeed, the tight prefix ends in \(u,v\), while reversing the non-tight suffix turns it into a tight path ending in \(v,u\). Conversely the two tight paths splice to a one-change order.

Equivalently, one may use two tight paths having one common terminal vertex. If
\[
P=(p_1,\ldots,p_\ell,v),
\qquad
Q=(q_1,\ldots,q_m,v),
\]
then
\[
(p_1,\ldots,p_\ell,v,q_m,\ldots,q_1)
\]
has at most one change. Conversely splitting a one-change order and reversing the non-tight side gives such a common-terminal pair.

These formulations describe the stronger one-change problem. We now exactify the original theorem before developing them further.

### Auxiliary-vertex exactification

Adjoin a new vertex \(r\) to \(H\). Retain every old triple and impose
\[
h(u,v,r)=1,
\qquad
h(r,v,u)=0
\]
for distinct \(u,v\in V(H)\). Values of
\[
h(u,r,v)
\]
may be chosen arbitrarily subject to boundary reversal.

Every spanning order of the extension is uniquely
\[
(L,r,R).
\]

**Theorem 3 (exact one-change extension).**
\[
\boxed{
\operatorname{pc}(H)\le2
\iff
H^+\text{ has a spanning order of directed form }1^a0^b.
}
\]

More precisely, directed one-change orders of \(H^+\) occur in reversal pairs and map two-to-one onto two-covers of \(H\).

**Proof.** Suppose
\[
(L,r,R)
\]
has directed form \(1^a0^b\). If \(|L|\ge2\), the last two vertices of \(L\) followed by \(r\) form a tight triple by construction. Hence every earlier triple on the left belongs to the initial tight run, so \(L\) is a tight path. Likewise a triple beginning at \(r\) is non-tight, forcing the entire right side into the non-tight run; therefore \(R^{\rm rev}\) is a tight path. Removing \(r\) gives
\[
L\mid R^{\rm rev}.
\]

Conversely, from a two-cover
\[
P\mid Q
\]
the two orders
\[
(P,r,Q^{\rm rev}),
\qquad
(Q,r,P^{\rm rev})
\]
have directed form \(1^a0^b\). The possible triple with \(r\) in the middle may have either value without creating a second switch. \(\square\)

This theorem is the conceptual pivot of the article. From here onward the geodesic and support formulations model the **actual conjecture**, not merely a stronger surrogate.

### Exact geodesic form

Apply the memory lift to \(H^+\) and keep the copy with source color \(1\). Its pole-geodesic words begin in \(1\) and end in \(0\). Therefore
\[
\boxed{
\operatorname{pc}(H)\le2
\iff
\Gamma(H^+)\text{ has a directed one-change pole geodesic}.
}
\]

The switch is normalized near \(r\). If
\[
P=(p_1,\ldots,p_k),
\qquad
Q=(q_1,\ldots,q_\ell),
\]
then the order
\[
(P,r,Q^{\rm rev})
\]
changes in the junction containing \(r\). There is no separate search for the switch position.

Similarly, in the opposite-edge support formulation for \(H^+\), the shared oppositely directed edge necessarily contains \(r\). In the common-terminal formulation, the endpoint-moving involution has a unique representative whose common endpoint is \(r\). Deleting \(r\) from that normalized state recovers the two-cover.

### Complementary tails in the exactified problem

The support-family language can now be read without ambiguity.

A directed one-change order of \(H^+\) is equivalent to two tight paths
\[
P=(X,u,v),
\qquad
Q=(Y,v,u)
\]
whose union is \(V(H^+)\), whose intersection is the ordinary edge \(uv\), and whose remaining supports are complementary.

Because the exactification forces
\[
r\in\{u,v\},
\]
this is an exact support encoding of a two-cover of \(H\).

Equivalently, normalize the paired common-terminal state so that both paths end at \(r\):
\[
P=(P_H,r),
\qquad
Q=(Q_H,r).
\]
Then
\[
P_H\mid Q_H
\]
is a two-cover of \(H\).

Thus the unresolved support problem may be stated as a complementary-tail problem **with a distinguished root** rather than as an arbitrary opposite-endpoint problem. This positional normalization is important: many topological arguments naturally produce support abundance, but the theorem needs the correct root and the correct endpoint order.

### The endpoint-moving involution

For completeness, common-terminal pairs on a fixed support carry a fixed-point-free involution.

Suppose
\[
P=(A,u,v),
\qquad
Q=(B,w,v).
\]
Exactly one of
\[
(u,v,w),
\qquad
(w,v,u)
\]
is tight. If the first is tight, replace the pair by
\[
(A,u,v,w),
\qquad
(B,w).
\]
The common endpoint moves from \(v\) to \(w\). Applying the same rule again returns to \(v\). The other orientation is symmetric.

The involution explains why common-terminal states naturally occur in pairs. In \(H^+\), exactly one member of such a pair has common endpoint \(r\), which is another form of the exactification.

### Positive factorization

Work in the square-zero algebra
\[
\mathcal A
=
\mathbb Q[x_v:v\in V]/(x_v^2:v\in V).
\]
Let
\[
F_H
=
\sum_{P\text{ nonempty tight in }H}x_{V(P)},
\]
counting distinct path orders separately.

For \(S\subseteq V\), let \(m_r(S)\) be the number of directed one-change orders on \(S\cup\{r\}\). Applying the exact extension to every induced subtournament gives
\[
\boxed{
\sum_{S\subseteq V}m_r(S)x_S
=
(1+F_H)^2.
}
\]

The constant term is the singleton order \(r\); the term \(2F_H\) places one nonempty tight path on either side of \(r\); and \(F_H^2\) records two disjoint nonempty tight paths. Square-zero multiplication removes intersecting supports with no cancellation.

In particular
\[
m_r(V)
=
2[x_V]\left(F_H+\frac12F_H^2\right).
\]

This factorization does not itself prove positivity. Its value is conceptual: it confirms that the auxiliary one-change model counts exactly the original one- and two-path covers.

The first half of Article VII is therefore exact:
\[
\text{two-cover}
\longleftrightarrow
\text{rooted one-change order}
\longleftrightarrow
\text{rooted one-change geodesic}
\longleftrightarrow
\text{rooted complementary supports}.
\]
The second half asks what antipodal topology can force inside these exact models.


---

## Section — From antipodal labels to cellular root topology

<!-- section_id: antipodal_labels_and_cellular_root_topology -->

### From rook labels to cellular roots


### Extreme-switch labels

Return first to the unexactified permutation sphere, where the local topology is easiest to see. For a spanning order whose status word contains at least two runs, let
\[
a(\pi)=\text{first switch position},
\qquad
b(\pi)=\text{last switch position},
\]
and put
\[
m=n-2,
\qquad
\bar b(\pi)=m-b(\pi).
\]

Reversal exchanges the two extreme coordinates:
\[
a(\pi^{\rm rev})=\bar b(\pi),
\qquad
\bar b(\pi^{\rm rev})=a(\pi).
\]

A natural first label is therefore the ordered pair
\[
q(\pi)=\bigl(a(\pi),\bar b(\pi)\bigr).
\]
Adjacent transpositions change only a bounded neighborhood of the status word. In particular, away from singular cases the two coordinates behave like a rook move: one coordinate is retained while the other changes locally.

This was the source of the Tucker and Ky Fan attempts.

### Why graph-level Tucker is insufficient

The temptation is to seek a theorem saying that an antipodal rook labeling of the permutahedron graph must contain a complementary edge or a diagonal label. That statement is false in this generality.

Indeed, for a permutation
\[
\pi=(v_1,\ldots,v_n)
\]
consider the purely combinatorial label
\[
Q(\pi)=(v_1,v_n).
\]
Reversal swaps the two coordinates:
\[
Q(\pi^{\rm rev})=(v_n,v_1).
\]
An adjacent transposition either occurs internally, leaving \(Q\) unchanged, or touches one endpoint and changes only one coordinate. Thus adjacent labels share a coordinate exactly as a rook condition would require.

Therefore antipodality plus rook adjacency on the \(1\)-skeleton is not enough to force a contradiction.

The same lesson persists for signed variants. One can build antipodal signed labels with very few magnitudes that avoid complementary labels on every permutahedron edge. Any successful Tucker argument must therefore use higher-dimensional consistency, not merely the graph.

This negative result is worth preserving. It explains why the later cellular topology is necessary.

### Tucker and Ky Fan as guides

A Tucker-style conclusion would ideally produce two compatible chambers carrying complementary extreme data. A Ky Fan-style conclusion would be stronger: an alternating simplex or chain could carry several coordinated switch-front witnesses at once.

The difficulty is not the absence of powerful antipodal theorems. The difficulty is representing the chamber data on a dimension-correct antipodal triangulation while preserving the positional meaning of the labels.

A naive triangulation of the permutahedron introduces diagonals between chambers that need not differ by adjacent transpositions. The local status word can then change in ways not controlled by the rook calculation. Conversely, a labeling confined to chamber vertices remembers the correct local swaps but does not satisfy the hypotheses of the simplicial theorem.

This is the reason Tucker and Ky Fan remain in the article as diagnostic tools rather than claimed closure theorems.

### Rank-two cells: squares and hexagons

The Coxeter complex supplies a canonical cellular repair.

Two independent adjacent transpositions commute. Their four chambers form a square. Adjacent transpositions at neighboring positions satisfy the braid relation
\[
s_is_{i+1}s_i=s_{i+1}s_is_{i+1},
\]
and their six chambers form a hexagon.

These are the rank-two cells controlling all local ambiguity in the chamber graph.

For the extreme-switch data, commuting squares are benign: the two changes are spatially separated and the resulting root labels can be joined without forcing an uncontrolled complementary diagonal.

Braid hexagons are the genuinely interesting cells. The same three local directions are reordered in all six possible ways, so the status data can wind. The exceptional cellular behavior is naturally encoded by a directed \(3\)-cycle in root space.

Thus the progression
\[
\text{Tucker}
\longrightarrow
\text{failure on the graph}
\longrightarrow
\text{cellular squares and hexagons}
\]
is not historical ornament. It identifies the correct scale on which the antipodal labeling is coherent.

### The extreme-switch root

Replace the ordered pair \(q(\pi)\) by the vector
\[
\phi(\pi)
=
e_{a(\pi)}-e_{\bar b(\pi)}.
\]
This vector lies in the type-\(A\) root space. Reversal is odd:
\[
\phi(\pi^{\rm rev})
=
-\phi(\pi).
\]

The vector is zero exactly at an exact diagonal
\[
a(\pi)=\bar b(\pi).
\]
Otherwise it is an oriented edge of the complete directed graph on the switch-coordinate set.

The root has two advantages over the rook pair.

First, convex combinations make sense. A family of chamber labels may balance at the origin even when no single chamber is diagonal.

Second, the rank-two cellular relations become algebraic relations among roots. A square expresses commuting local changes; an exceptional braid hexagon can support a directed root cycle.

This is the point at which the topology stops asking for one complementary edge and starts asking for **balanced recurrence**.

### From the Helly witnesses to the root

The root coordinates should be read back through the first Section.

The exact two-cover obstruction is a family of defect intervals. The root discards almost all of that family and remembers only the first and reflected-last switch fronts. It is therefore a topological compression of the Helly failure.

This compression is useful because it produces an odd map into a linear representation. It is dangerous because a zero of the compressed data need not itself be the exact two-cover state.

The rest of Article VII is devoted to that gap:
\[
\text{topological balance of extreme witnesses}
\quad\Longrightarrow?\quad
\text{exact combinatorial intersection}.
\]


---

## Section — Convex root balance and Bourgin–Yang multiplicity

<!-- section_id: convex_root_balance_and_bourgin_yang -->

### Balance, circulation, and multiplicity of zeros


### Convex balance is directed circulation

Let \(I\) be a finite coordinate set and let
\[
E\subseteq I\times I
\]
be a directed graph. Associate to an arc \(i\to j\) the type-\(A\) root
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

The article deliberately does **not** compress this into an unaudited slogan such as
\[
L\mapsto L+2\mapsto L+3\text{ cycles}.
\]
Earlier research notes contained several such normalizations, but the constants depend on exactly which switch coordinates, sphere dimension, and carrier subdivision are used.

The durable theorem is the dimension principle above. Concrete switch-span corollaries should be inserted only after their coordinate count and their conversion to circulation rank are independently checked.

### Why multiplicity matters

One balanced face may be accidental. A positive-dimensional balanced locus is qualitatively different.

A positive-dimensional zero set forces the balancing phenomenon to persist through neighboring cells. Combinatorially, this means there are multiple compatible switch-front recurrences rather than one isolated cycle.

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


---

## Section — From topological recurrence to local GN3 structure

<!-- section_id: topological_recurrence_to_local_gn3_structure -->

### From balanced recurrence to local reversal structure


### Directed switch-front cycles

Let
\[
F=B_1|\cdots|B_k
\]
be an ordered-partition face whose extreme-switch roots balance at the origin. By the circulation criterion of the preceding Section, the support contains a directed cycle
\[
x_1\to x_2\to\cdots\to x_t\to x_1.
\]

An arc
\[
x\to y
\]
means that some chamber of \(F\) has first switch coordinate \(x\) and reflected last switch coordinate \(y\).

There are two qualitatively different possibilities.

1. **Exact diagonal:** some chamber has
   \[
   x=y.
   \]
2. **Winding:** every root is nonzero and the support contains a directed cycle of distinct or repeated coordinates.

The diagonal is already a strong positional statement. The winding case is where the face structure becomes useful.

### Block separation

The determining data for a first switch at coordinate \(x\) live in a bounded prefix window; the determining data for a reflected last switch at the same coordinate live in the symmetric suffix window.

Suppose an ordered-partition boundary of \(F\) separates these two determining windows. Because permutations inside different blocks are independent, one may take the block orders realizing the left witness from one chamber and the block orders realizing the right witness from another. The combined chamber then realizes both witnesses simultaneously and produces
\[
q=(x,x),
\]
an exact diagonal.

Therefore, in the no-diagonal branch, no face-block boundary may separate the two mirror determining windows for any coordinate on the directed cycle.

This is the block-separation principle. It uses only the product structure of an ordered-partition face; no hypothesis that the face has only a few blocks is needed.

### The canonical giant block

Let
\[
r=\min\{x_i:1\le i\le t\}.
\]
If the mirror corridor for \(r\) is nonempty, block separation forces that entire corridor into one block \(B\) of the ordered partition.

For every other cycle coordinate \(x_i\ge r\), its mirror corridor is nested inside the corridor for \(r\). Hence the same block \(B\) contains every nonempty mirror corridor occurring on the cycle.

Thus the winding branch has one **canonical giant block**. Different switch coordinates do not require unrelated large blocks.

If the minimum mirror corridor is empty, the switch coordinates are forced into a near-central bounded configuration. The strongest later reductions show that these near-central words fall back into compact switch windows and the existing small-support/repartition machinery. The article therefore treats the giant-block regime as the only genuinely nonlocal winding geometry.

### Cross-intersecting determining families

Inside the canonical block \(B\), let \(\mathcal L_x\) be the family of vertex sets that can occupy the left determining positions for first switch \(x\), and let \(\mathcal R_x\) be the corresponding right determining family.

If
\[
L\in\mathcal L_x,
\qquad
R\in\mathcal R_x
\]
were disjoint, the block permutation could place \(L\) and \(R\) simultaneously in their two determining windows. Together with the frozen outer blocks this would create the exact diagonal \(q=(x,x)\).

Hence
\[
\boxed{
L\cap R\ne\varnothing
\quad
\text{for every }
L\in\mathcal L_x,\ R\in\mathcal R_x.
}
\]

The topology has therefore become a cross-intersection problem inside one ordinary finite set.

From here one may extract small transversals and private witnesses. If a small set \(T\subseteq B\) is an inclusion-minimal transversal of one determining family, then for every
\[
v\in T
\]
there is an opposite witness meeting \(T\) only in \(v\). These private witnesses are useful carriers for the local GN3 arguments, but the transversal formalism is secondary; it is not another topological layer.

### Front motion

There is an even more direct consequence.

Fix a chamber realizing one of the two extreme fronts and vary the permutation of the giant block \(B\). The adjacent-transposition graph of the permutations of \(B\) is connected.

If every adjacent swap in \(B\) preserved that extreme front, then every permutation of \(B\) would preserve it. One could then choose the left and right determining sets independently, and because the two determining windows fit inside \(B\), choose them disjoint. That would create an exact diagonal, contrary to the no-diagonal assumption.

Therefore some adjacent swap in \(B\) **moves the front**.

If the swap lies close to the old front, the disturbance is confined to a bounded local window. If it lies deeper in a monochromatic region, the old and new fronts are separated by a long monochromatic corridor.

This is the strongest useful conclusion of the giant-block analysis:
\[
\boxed{
\text{exact diagonal}
\ \vee\
\text{front displacement}
\ \vee\
\text{bounded local configuration}.
}
\]

### Where GN3-specific structure enters

Up to this point the argument has used mostly antipodal geometry, switch words, and the product structure of permutation faces. The next conversion is specifically GN3.

A moved front or a long monochromatic corridor is not merely a changed bit. Because a failed triple has a forced boundary flip, local front motion produces actual tight reversal triples. Repeated front motion can therefore create:

- an exterior vertex reversing a displayed end edge;
- one carrier reversing two disjoint displayed edges;
- parallel-middle vertices;
- a Hamiltonian four- or five-support;
- a path disturbance suitable for repartition;
- strict decrease of the quadratic potential.

The reusable mechanisms are developed in
[[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]],
[[endpoint_transport_and_small_support_gluing_the_remaining_lemma]],
and
[[defect_lines_and_spanning_order_compression_the_remaining_lemma]].

The conceptual division is now clean:

\[
\boxed{
\text{topology produces recurrence;}
\qquad
\text{boundary antisymmetry converts recurrence into structure.}
}
\]

This is precisely the point where GN3 may be easier than the general memory-two geodesic conjecture.

### The stronger-route alternative remains open

Nothing in this Section says that the GN3-specific conversion is the only possible closure.

A sufficiently strong antipodal memory-geodesic theorem could bypass the giant-block and local-reversal analysis entirely. If such a theorem is proved, Article VII should be rewritten to state it as the main result and the reduction through auxiliary exactification should be used directly.

Conversely, if the general theorem is false, the present Section identifies the extra hypotheses that GN3 contributes and therefore the correct place to exploit them.

The two routes are complementary research programs, not competitors.


---

## Section — Antipodal reachability and the neutral corridor

<!-- section_id: antipodal_reachability_and_neutral_corridor -->

### Exact reachability and the neutral corridor


### Reachability in the exactified memory lift

Return now to the auxiliary extension \(H^+\) from the fourth Section and work in the single memory-lift copy whose source color is \(1\). Orient every edge from lower rank to higher rank.

Let \(R\) be the set of states reachable from the source pole \(s\) by an increasing path using only color \(1\).

Because the antipodal involution reverses rank and complements color, the antipodal image \(A(R)\) has an exact dual interpretation.

**Proposition 6.** A state \(x\) lies in \(A(R)\) if and only if there is an increasing color-\(0\) path from \(x\) to the target pole \(t\).

**Proof.** A color-\(1\) increasing path from \(s\) to \(y\) maps under \(A\) to a color-\(0\) decreasing path from \(t\) to \(A(y)\). Reversing that path gives a color-\(0\) increasing path from \(A(y)\) to \(t\). The converse is the same argument reversed. \(\square\)

Hence
\[
\boxed{
R\cap A(R)\ne\varnothing
\iff
\Gamma(H^+)\text{ has a directed one-change pole geodesic}.
}
\]

If
\[
x\in R\cap A(R),
\]
concatenate a color-\(1\) increasing path from \(s\) to \(x\) with a color-\(0\) increasing path from \(x\) to \(t\). Rank increases at every step, so the concatenation has pole distance and is automatically geodesic.

Together with auxiliary exactification,
\[
\boxed{
\operatorname{pc}(H)\le2
\iff
R\cap A(R)\ne\varnothing.
}
\]

This is an exact state-space formulation of the original theorem.

### The neutral corridor

Assume
\[
R\cap A(R)=\varnothing
\]
and put
\[
N
=
V(\Gamma)\setminus\bigl(R\cup A(R)\bigr).
\]
Then
\[
A(N)=N.
\]

There is no increasing edge directly from \(R\) to \(A(R)\). Such an edge cannot have color \(1\), since its upper endpoint would then lie in \(R\). It cannot have color \(0\), since its lower endpoint would then have a color-\(0\) route through the upper endpoint to \(t\), placing it in \(A(R)\).

Since the ranked graph connects the poles, every pole-to-pole path must therefore meet \(N\). In particular \(N\ne\varnothing\).

The interface colors are forced:

- every increasing edge from \(R\) to \(N\) has color \(0\);
- every increasing edge from \(N\) to \(A(R)\) has color \(1\).

The antipode exchanges these two frontiers.

Thus a counterexample is equivalent to the existence of an antipodally invariant separating corridor with prescribed opposite colors on its lower and upper boundary.

### Convex balance and actual intersection are different zeros

This distinction is the sharpest way to state the present frontier.

The root construction asks for a convex zero:
\[
0\in\operatorname{conv}\{\phi(\pi):\pi\in\mathcal C\}.
\]
Such a zero says that compressed extreme-defect vectors balance. Through the circulation criterion, it produces recurrence among switch fronts.

Reachability asks for an actual state-space intersection:
\[
x\in R\cap A(R).
\]
Such a point is not an average. It is one concrete memory state simultaneously reachable from the source by one color and from which the target is reachable by the other.

Therefore
\[
\boxed{
\text{root balance}
\neq
\text{reachability self-intersection}
}
\]
without an additional conversion theorem.

The unresolved topological problem may be phrased precisely as:

> Convert the multiplicity or recurrence forced by antipodal root topology into one actual state of the exactified memory lift lying in \(R\cap A(R)\), or into GN3-specific local structure that Articles III–VI can close.

This is more precise than asking vaguely for “a Borsuk–Ulam proof.”

### What a purely topological closure must preserve

Any theorem acting directly on the exactified memory lift must preserve three features simultaneously:

1. **distinguished poles:** the relevant antipodal pair is \(s,t\);
2. **geodesicity:** rank increases at every step, so no original label is reused;
3. **memory:** edge color records three successive cube directions.

A theorem producing an arbitrary antipodal path may fail the first two conditions. A theorem on ordinary cube-edge colorings may fail the third.

The candidate memory-two geodesic conjecture from the second Section is one clean way to package all three requirements. If it is proved, the corridor is impossible in every reversal-complement memory coloring, not merely in GN3.

The alternative is to prove that the corridor cannot coexist with the additional local tournament structure of a boundary tournament.

### How the older topology fits

The earlier Tucker, root, and Bourgin–Yang programs should now be interpreted as candidate mechanisms for attacking the corridor.

- Tucker sought a local complementary state.
- Cellular root topology replaced one complementary edge by balanced recurrence.
- Bourgin–Yang sought enough balanced recurrence to make avoidance impossible.
- GN3-specific compression seeks to turn recurrence into a local reversal or support.

The reachability picture supplies the exact endpoint of that program: all of those mechanisms are useful only insofar as they force
\[
R\cap A(R)\ne\varnothing
\]
or a combinatorial contradiction to the existence of \(N\).

This is the exact topological frontier.


---

## Section — Synthesis and the exact topological frontier

<!-- section_id: article_vii_synthesis_and_exact_frontier -->

### Two exact routes to closure


### The exact equivalence chain

The purpose of Article VII is not to replace the local GN3 theory of Articles I–VI. It is to identify the global obstruction geometrically and to translate the original conjecture into exact antipodal models.

The exact chain is
\[
\boxed{
\begin{aligned}
\operatorname{pc}(H)\le2
&\iff
\exists\pi\text{ whose defect intervals admit one common cut}\\
&\iff
H^+\text{ has a directed one-change spanning order}\\
&\iff
\Gamma(H^+)\text{ has a directed one-change pole geodesic}\\
&\iff
\text{the rooted complementary-support condition holds}\\
&\iff
R\cap A(R)\ne\varnothing.
\end{aligned}}
\]

The first line is the quantified defect-Helly theorem. The second is auxiliary exactification. The third is the memory lift. The fourth is the opposite-edge/common-terminal support dictionary normalized at \(r\). The fifth is the reachability criterion.

Every arrow in this chain is exact.

### What topology currently supplies

The root-topological route does not yet prove one of these exact conditions directly. What it supplies is structure:

- the Coxeter sphere of spanning orders;
- antipodal extreme-switch labels;
- cellular square and braid-hexagon constraints;
- the odd root map
  \[
  \phi(\pi)=e_a-e_{\bar b};
  \]
- balanced faces and directed root circulations;
- potentially positive-dimensional balanced loci via Bourgin–Yang;
- block separation, giant-block recurrence, cross-intersection, and front motion.

These are genuine mathematical outputs. They should not be discarded merely because they stop one step short of the theorem.

But they are compressed outputs. The exact target remains one concrete intersection or one exact complementary-support state.

### Route A: prove the stronger geodesic theorem

The first legitimate closure route is to prove a theorem stronger than GN3.

The clean candidate is the memory-two geodesic conjecture from the second Section:

> Every finite reversal-complement coloring
> \[
> h(w,v,u)=1-h(u,v,w)
> \]
> of ordered triples of distinct labels admits a permutation whose consecutive-triple word has at most one color change.

Equivalently, every antipodally colored memory lift of this form has a one-change pole geodesic.

If this theorem is proved, then apply it to the auxiliary extension \(H^+\). The resulting directed one-change order gives a two-cover of \(H\) by Theorem 3.

Thus the reduction is precise:
\[
\boxed{
\text{memory-two geodesic conjecture}
\Longrightarrow
\text{grand GN3 two-cover conjecture}.
}
\]

A proof of the stronger theorem would therefore be a successful conclusion of the project, not an unwanted detour.

The same principle applies if the correct general theorem is formulated at another level—for example as a generalization of the strengthened Norine geodesic conjecture on a higher-memory antipodal complex. What matters is that the theorem be stated precisely and that the reduction to the exactified GN3 lift be checked explicitly.

### Route B: exploit the additional GN3 structure

The second closure route assumes that arbitrary reversal-complement memory colorings are too general.

Then the extra boundary-tournament structure becomes decisive. A failed triple has a forced reversed tight triple. Recurrent front motion therefore generates actual path structure rather than abstract bit changes.

Articles I–VI develop the resulting mechanisms:

- deletion-cover compatibility;
- quadratic-potential descent;
- defect-line compression;
- endpoint transport;
- longest-path reversal structure;
- equal-potential recurrence.

The handoff from Article VII should be viewed schematically as
\[
\boxed{
\text{topological recurrence}
\longrightarrow
\text{front motion / exact diagonal / repeated carrier}
\longrightarrow
\text{GN3 reversal structure}
\longrightarrow
\text{two-cover or strict descent}.
}
\]

This is precisely where GN3 departs from the unresolved general geodesic analogue.

### The actual remaining topological conversion

The central missing implication may now be stated without ambiguity:
\[
\boxed{
\text{balanced or recurrent extreme-switch data}
\quad\Longrightarrow?\quad
R\cap A(R)\ne\varnothing.
}
\]

There are two ways this implication could be achieved.

1. **Topologically:** show that an antipodally invariant neutral corridor is incompatible with the memory coloring itself.
2. **Combinatorially:** show that the recurrence required to support the corridor necessarily creates one of the GN3 configurations closed by Articles III–VI.

Bourgin–Yang is relevant to the first and second possibilities because multiplicity of zeros may prevent a corridor from remaining locally coherent. The giant-block and front-motion analysis is relevant because it converts multiplicity into explicit local motion.

The article does not claim that this conversion has been completed.

### A cyclic guardrail

One attractive strengthening should be recorded only as a warning.

It is sufficient to find a spanning cyclic order whose transition-color word has at most two monochromatic components, but this is not necessary for a two-cover. There are edge-orderable boundary tournaments with
\[
\operatorname{pc}(H)=2
\]
for which every spanning cycle has at least four monochromatic transition components.

The correct cyclic invariant is not the number of runs.

For an oriented Hamilton cycle
\[
Z=(v_1,\ldots,v_n,v_1),
\]
let the cycle-edge positions be
\[
e_i=\{v_i,v_{i+1}\}.
\]
Construct a defect graph \(D_Z\) on these positions by joining
\[
e_{i-1},e_i
\]
exactly when
\[
(v_{i-1},v_i,v_{i+1})
\]
is non-tight.

A set of cut edges turns the cycle into tight inherited paths exactly when it meets every edge of \(D_Z\). Therefore
\[
\operatorname{pc}(H)
=
\min_Z\max\{1,\tau(D_Z)\}.
\]

In particular,
\[
\operatorname{pc}(H)\le2
\iff
\exists Z\text{ with }\tau(D_Z)\le2.
\]

This exact cyclic formulation may still be useful, but the false two-component-cycle strengthening is not part of the main route.

### Article thesis

Articles I–VI develop the GN3-specific local and repartition machinery.

Article VII identifies the global obstruction as an antipodal-geodesic/topological phenomenon, gives exact Helly, geodesic, support, and reachability models of the theorem, and isolates the point at which global topology must either:

- prove a stronger general geodesic theorem; or
- hand recurrence back to the special boundary-tournament machinery.

This is the organizing principle for future work.

A successful worker need not decide in advance which route will win. If the topology naturally proves the stronger memory-geodesic conjecture, that route should be pursued and stated openly. If it fails exactly where GN3 supplies endpoint reversals or small supports, that extra structure should be exploited.

The frontier is no longer a vague analogy with the cube. It is a precise choice between two mathematically meaningful closure mechanisms.
