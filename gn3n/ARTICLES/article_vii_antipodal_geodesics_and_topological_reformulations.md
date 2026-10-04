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
be a spanning order. The cases \(n\leq1\) have path-cover number at most one. Throughout the cut formulation assume \(n\geq2\), and interpret the intersection of an empty defect family as the full cut set \(\{1,\ldots,n-1\}\). Write
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


### Exact inversion-window criterion

### Exact inversion-window criterion

There is a sharper order-relative formulation of the two-cover problem than the extreme-switch compression.

Let
\[
\pi=(v_1,\ldots,v_n),\qquad m=n-2,
\]
with status word \(\epsilon_1,\ldots,\epsilon_m\). Define
\[
p(\pi)=\min\{i:\epsilon_i=0\},\qquad
q(\pi)=\max\{i:\epsilon_i=1\},
\]
using the conventions \(p=m+1\) if there is no zero and \(q=0\) if there is no one.

**Theorem (exact inversion-window criterion).**
\[
\boxed{\operatorname{pc}(H)\le2
\iff
\exists\pi\text{ with }q(\pi)\le p(\pi)+1.}
\]

**Proof.** Suppose first that \(q\le p+1\). Choose an integer cut \(j\) with
\[
q\le j\le p+1.
\]
Then every status wholly inside \(v_1,\ldots,v_j\), namely every \(\epsilon_i\) with \(i\le j-2\), equals \(1\), because \(j-2\le p-1\). Thus
\[
P=(v_1,\ldots,v_j)
\]
is tight. Every status wholly inside \(v_{j+1},\ldots,v_n\), namely every \(\epsilon_i\) with \(i\ge j+1\), equals \(0\), because \(j+1>q\). Boundary antisymmetry therefore makes
\[
Q=(v_n,\ldots,v_{j+1})
\]
tight. Hence \(P\mid Q\) is a spanning two-cover, with the evident empty-side convention at the ends.

Conversely, let \(P\mid Q\) be a spanning cover by at most two tight paths. Concatenate
\[
\pi=(P,Q^{\rm rev})
\]
and let \(j=|P|\). Every status with \(i\le j-2\) is \(1\), while every status with \(i\ge j+1\) is \(0\). Hence \(p\ge j-1\) and \(q\le j\), so \(q\le p+1\). \(\square\)

Thus a counterexample satisfies
\[
q(\pi)-p(\pi)\ge2
\]
for every spanning order. The quantity
\[
\delta(\pi)=q(\pi)-p(\pi)-1
\]
is an exact order-level two-cover deficiency: \(\delta\le0\) is already a certificate.

### Reversal coordinates for the exact obstruction

Put
\[
c(\pi)=m+1-q(\pi).
\]
Reversal-complement gives
\[
p(\pi^{\rm rev})=c(\pi),\qquad
c(\pi^{\rm rev})=p(\pi).
\]
Hence
\[
\psi(\pi)=e_{p(\pi)}-e_{c(\pi)}
\]
is an odd type-\(A\) root label:
\[
\psi(\pi^{\rm rev})=-\psi(\pi).
\]

Moreover
\[
\delta(\pi)=m-\bigl(p(\pi)+c(\pi)\bigr).
\]
Therefore the exact two-cover threshold is the anti-diagonal
\[
p+c\ge m,
\]
while every chamber of a counterexample lies strictly below it:
\[
p+c\le m-1.
\]

This exact inversion root retains substantially more theorem-relevant information than the first/last-switch root. Its tail is the first actual non-tight status, its head is the reflected last actual tight status, and the sum of the two root coordinates measures the exact distance from the two-cover window. It is therefore the natural root for a second pass through the barycentric balance argument.

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

### The stronger conclusion and the class of inputs

A function on ordered triples of distinct labels satisfying
\[
h(w,v,u)=1-h(u,v,w)
\]
is exactly a boundary \(3\)-tournament: declare \((u,v,w)\) tight when \(h(u,v,w)=1\). Conversely every boundary tournament gives such a function. The local tournament at a middle vertex \(v\) has arc \(u\to w\) precisely when \(h(u,v,w)=1\). This structure follows from the displayed identity; it is not an additional hypothesis.

**Candidate one-change conjecture.** Every boundary \(3\)-tournament admits a spanning order whose consecutive-triple word changes color at most once.

This strengthens the desired conclusion on the same class of inputs. It is not a generalization to a larger class of triple colorings. The candidate implies a two-cover directly: split the order between its two monochromatic portions, then reverse any portion with non-tight triples. The memory lift below makes the candidate a precise geodesic assertion.

There are also two directed versions, requiring respectively \(1^a0^b\) and \(0^a1^b\). Reversal of the vertex order reverses and complements the word, so it preserves each directed type. One cannot change the direction of the switch merely by reversing the order. Auxiliary exactification uses specifically the first type.

### A genuinely larger memory class

To allow more general local data, one may let the color depend on the previously used set:
\[
g(S;u,v,w)\in\{0,1\},\qquad S\subseteq V\setminus\{u,v,w\},
\]
with antipodal identity
\[
g(V\setminus(S\cup\{u,v,w\});w,v,u)
=1-g(S;u,v,w).
\]
A permutation reads these colors with \(S\) equal to the prefix preceding its three displayed directions. Boundary tournaments are precisely the subclass independent of \(S\). An arbitrary reversal-complement assignment of words to whole permutations is broader still; it need not satisfy any consistency between permutations sharing a triple.

Thus the useful distinction is between antipodal symmetry alone and a consistent, base-independent rule on ordered triples. Local reversals, endpoint transport, and repartitions exploit that consistency. They do not distinguish boundary tournaments from the function \(h\) already displayed above.

A theorem for the larger class would require its own statement and proof, including the prescribed poles and the desired switch direction. No such theorem is asserted here.

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

The chamber geometry is shared with cube-geodesic problems. The local data differ. We may seek the stronger one-change conclusion for boundary tournaments, or work only in the auxiliary extensions for which directed one-change existence is equivalent to a two-cover. A broader theorem for base-dependent memory is a separate possible generalization. These distinctions concern respectively the conclusion, the input subclass, and the input class.


### Further developments



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

These formulations concern the directed word \(1^a0^b\). The other direction uses opposite initial edges or a common initial vertex. Either common-terminal path may be a singleton.

One useful quantitative consequence is retained from [[antipodal_geodesics_and_complementary_path_supports]]: a one-change order on \(N\geq2\) vertices yields two tight paths sharing an edge, so their orders sum to \(N+2\). Hence at least one has
\[
\left\lceil\frac{N+2}{2}\right\rceil
\]
vertices. This helps explain why the one-change target on the original vertices may be stronger than a two-cover.

We now exactify the original theorem before developing these support formulations further.

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

Assume \(V(H)\ne\varnothing\). More precisely, directed one-change orders of \(H^+\) occur in reversal pairs and map two-to-one onto two-covers of \(H\). A cover is an unordered collection of individually ordered paths.

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
have directed form \(1^a0^b\). The possible triple with \(r\) in the middle may have either value without creating a second switch. For a one-path cover \(P\), the two orders are \((P,r)\) and \((r,P^{\rm rev})\); when deleting \(r\), discard an empty side. The two side orders are recoverable from the spanning order, proving the two-to-one assertion. \(\square\)

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
The common endpoint moves from \(v\) to \(w\). If \(B\) is nonempty with last vertex \(z\), tightness of the old second path gives \((z,w,v)\) tight, so the same rule returns to \(v\). The other orientation is symmetric.

If one path is the singleton \((v)\), write the other as \((A,u,v)\) and replace the pair by \((A,u)\) and \((v,u)\). These are tight, and the preceding rule returns to the old pair when \(A\) is nonempty; when \(A\) is empty the singleton rule itself returns. Thus the involution is defined on every common-terminal pair whose union has at least two vertices.

The involution explains why common-terminal states naturally occur in pairs. In \(H^+\), exactly one member of such a pair has common endpoint \(r\), which is another form of the exactification.

### The common-terminal counting identity

One useful identity from the earlier positive enumeration has a direct combinatorial proof. For a boundary tournament \(J\) on at least two vertices, let \(A(J)\) count spanning orders of directed form \(1^a0^b\), and let \(h(J)\) count ordered tight Hamilton paths. Let \(b(J)\) count a choice of vertex \(v\) and an unordered pair of nonempty tight paths partitioning \(V(J)\setminus\{v\}\), such that appending \(v\) to either path remains tight. Then
\[
\boxed{A(J)=h(J)+b(J).}
\]

**Proof.** Common-terminal pairs with a singleton member correspond to the \(h(J)\) Hamilton paths; pairs with both members nontrivial correspond to the \(b(J)\) certificates. The endpoint-moving involution groups all these pairs into two-element orbits, one for each unordered opposite-terminal-edge pair. Such an edge pair also gives exactly two directed one-change orders, exchanged by reversal. Conversely a directed word has a uniquely specified shared edge: if it contains \(a\) tight triples, use its vertices in positions \(a+1,a+2\). Thus both sides count twice the number of opposite-terminal-edge pairs. \(\square\)

This identity retains the earlier square-zero calculation's positive combinatorial content without requiring its transfer matrices. It concerns the directed one-change target on \(J\); it does not assert that an arbitrary two-cover of \(J\) gives such an order.

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


### Further developments



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

These rank-two cells describe the local relations of adjacent swaps. A proposed graph-level extension must check what the actual status labels do on these cells; their combinatorial shape alone does not prove that every square is harmless or that every exceptional hexagon produces a directed root cycle.

The explicit barycentric extension in the next Section avoids this extension problem: it averages all chamber roots on every face and is defined on all nested face chains. Squares and hexagons remain useful for local combinatorial analysis, but no unproved assertion about their label patterns is needed to define the odd map.

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

### Further developments



---

## Section — Convex root balance and Bourgin–Yang multiplicity

<!-- section_id: convex_root_balance_and_bourgin_yang -->

### Balance, circulation, and multiplicity of zeros

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


### Positive balance on every chamber and the switch-separation bound

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


---

## Section — From topological recurrence to local GN3 structure

<!-- section_id: topological_recurrence_to_local_gn3_structure -->

### From balanced recurrence to local reversal structure

### Determining positions and positive face balance

Let \(F=B_1|\cdots|B_k\) be a proper permutahedral face, with its blocks occupying consecutive positions. Assume its chamber roots admit a circulation strictly positive on every occurring root, as provided by [[convex_root_balance_and_bourgin_yang]]. Then every coordinate occurring as a first switch also occurs as a reflected last switch in the same face. Every chamber belongs to a directed root cycle, unless it has a zero root and is already an exact diagonal.

This is stronger than choosing just one cycle. The following deductions explain what can be extracted without assuming that convex balance is already a two-cover.

### Block separation with explicit determining windows

A first switch at \(x\) is determined by the first \(x+1\) statuses and hence by vertex positions
\[
1,\ldots,x+3.
\]
A reflected last switch at \(x\) is determined by the last \(x+1\) statuses and hence by positions
\[
n-x-2,\ldots,n.
\]

**Lemma 7.1.** Suppose \(F\) has a chamber with first switch \(x\), a chamber with reflected last switch \(x\), and a block boundary after position \(j\) such that
\[
x+3\leq j\leq n-x-3.
\]
Then \(F\) contains a chamber with root zero.

**Proof.** Use the block orders from the first witness in every block up to the boundary, and those from the second witness after it. Both determining windows remain unchanged. The resulting chamber has \(a=\bar b=x\). \(\square\)

Consequently, if \(F\) contains no diagonal and the displayed interval of possible boundaries is nonempty, all positions
\[
x+3,\ldots,n-x-2
\]
lie in a single block. Its size is at least \(n-2x-4\).

**Corollary 7.2.** Under strictly positive face balance and absence of a diagonal, let \(r\) be the least switch coordinate occurring in any chamber root of \(F\). If \(n\geq2r+6\), one block contains positions \(r+3,\ldots,n-r-2\). It also contains every nonempty corridor of this form for any larger occurring coordinate.

**Proof.** Positive balance supplies both kinds of witness for \(r\), so Lemma 7.1 excludes all boundaries in its corridor. Corridors for larger coordinates are nested inside it. \(\square\)

This gives a single block for all occurring root coordinates, not only those of a selected cycle. If \(n<2r+6\), this separation lemma gives no block conclusion. Near-central coordinates must be treated by a separate argument; their numerical location alone does not prove a bounded-support descent.

### Cross-intersecting determining families

Fix the orders of all blocks other than a chosen block \(B\), and fix a coordinate \(x\) whose two determining windows are disjoint. Let \(\mathcal L_x\) consist of the sets of labels of \(B\) occupying its positions in the left window in some chamber with first switch \(x\). Define \(\mathcal R_x\) analogously for reflected last switch \(x\). Witness orders of these sets inside the corresponding positions are retained when combining them.

**Lemma 7.3.** If no chamber with these fixed outside orders has root zero, then every \(L\in\mathcal L_x\) intersects every \(R\in\mathcal R_x\).

**Proof.** If the sets were disjoint, place each in its own determining positions using its witness order, and fill the remaining positions of \(B\) arbitrarily. The disjoint windows and the fixed outside orders preserve both witnesses. This produces a diagonal. \(\square\)

The qualification about outside orders is essential: face balance supplies witnesses somewhere in \(F\), not automatically witnesses with every prescribed choice of outside block orders.

If both families are nonempty, any member of \(\mathcal L_x\) is a transversal of \(\mathcal R_x\). An inclusion-minimal transversal \(T\) contained in it has, for each \(v\in T\), a member of \(\mathcal R_x\) meeting \(T\) exactly at \(v\); otherwise \(v\) could be removed. This preserves the private-witness mechanism without asserting an absolute bound on \(|T|\). Such a bound would require a bound on the number of determining positions inside \(B\).

### Front motion with the witness hypotheses retained

**Lemma 7.4.** Fix all outside block orders. Suppose a permutation of \(B\) realizes first switch \(x\), another realizes reflected last switch \(x\), and no permutation of \(B\) realizes a diagonal. Then an adjacent transposition within \(B\) changes the first switch coordinate.

**Proof.** In the second witness, the first switch cannot equal \(x\). The adjacent-transposition graph of the permutations of \(B\) is connected. Along a path between the two witnesses, at least one swap changes the first switch. \(\square\)

If positions \(j,j+1\) are swapped, only triple positions \(j-2,\ldots,j+1\) can change, clipped to \(1,\ldots,m\). Consequently only switch positions \(j-3,\ldots,j+1\) can change. If two resulting first-switch coordinates \(a<a'\) differ, the earlier coordinate \(a\) lies in this five-position interval; the word with first switch \(a'\) is constant through position \(a'\). Thus a long displacement has a monochromatic interval, while the cause of the displacement is local. The same statement holds for last switches by reversal.

### The conversion problem after face recurrence

Boundary antisymmetry turns each specified non-tight triple into its reversed tight triple. By itself, however, the preceding face geometry does not yet synchronize arbitrary left and right witnesses: a moved front need not already be one exterior vertex reversing two required end edges, and witnesses with different outside block orders need not have disjoint exposed edges.

The next subsection resolves precisely this issue without trying to synchronize two arbitrary chambers. Instead one minimizes switch span inside the carrier face and transports the **same physical carrier** to the two extreme fronts of a single chamber. The common-block conclusion above keeps both tests inside the face, while minimality prevents inward front motion. This produces the required local reversal structure and removes the formerly global synchronization problem.

The local path-cover mechanisms used after that compression are recorded in [[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]], [[endpoint_transport_and_small_support_gluing_the_remaining_lemma]], and [[defect_lines_and_spanning_order_compression_the_remaining_lemma]].


### Recurrent-face and minimum-span compression


### Compact switch span

For a spanning order
\[
\pi=(v_1,\ldots,v_n)
\]
whose status word has first switch \(a\) and last switch \(b\), put
\[
d(\pi)=b-a.
\]

**Lemma 7.5 (compact switch span).** If \(d(\pi)\le 2\), then \(H\) has a spanning two-cover.

**Proof.** Cut the order after \(v_{a+2}\). Every status internal to the left block has index at most \(a\), hence has the first-run color. Every status internal to the right block has index at least \(a+3>b\), hence has the last-run color. A monochromatic block is a tight path in its displayed orientation when its color is tight, and in the reverse orientation when its color is non-tight. Thus the two blocks can be oriented as tight paths. \(\square\)

The same cut calculation gives a useful next range.

**Lemma 7.6 (small middle from span at most five).** If
\[
3\le d(\pi)\le5,
\]
then \(H\) has a spanning three-cover
\[
L\mid M\mid R
\]
in which
\[
|M|=d(\pi)-2\le3.
\]

**Proof.** Put
\[
L=(v_1,\ldots,v_{a+2}),\qquad
M=\{v_{a+3},\ldots,v_b\},\qquad
R=(v_{b+1},\ldots,v_n).
\]
All internal statuses of \(L\) have the first-run color and all internal statuses of \(R\) have the last-run color, so each outer block has a tight orientation. The middle has order at most three and is therefore Hamiltonian: orders one and two are vacuous, and on three vertices one of the two reverse orders is tight by boundary antisymmetry. \(\square\)

### A recurrent carrier face has no large global residue

Let
\[
F=B_1|\cdots|B_k
\]
be a carrier face supplied by Theorem 6.1, so every chamber root occurring in \(F\) lies on a directed root cycle unless it is zero. Assume first that \(F\) contains no zero root.

Choose a chamber
\[
\pi=(v_1,\ldots,v_n)\in\mathcal V(F)
\]
for which \(d=b-a\) is minimum among the chambers of \(F\). Put
\[
m=n-2,\qquad c=m-b,
\]
so the root of \(\pi\) is the arc
\[
a\longrightarrow c.
\]

Because this arc lies on a directed root cycle, choose a simple such cycle and let \(r\) be its least coordinate. Every arc \(x\to y\) on the cycle comes from a chamber with
\[
x+y=m-d(\text{that chamber})\le m-1.
\]

If
\[
n<2r+6,
\]
then \(m\le2r+3\). For a neighbor \(s\) of \(r\) on the cycle,
\[
2r\le r+s\le m-1\le2r+2.
\]
There are no loops because \(F\) has no zero root, so \(s-r\in\{1,2\}\). The chamber realizing \(r\to s\) has switch span
\[
m-r-s\le2,
\]
and Lemma 7.5 gives a two-cover.

Hence, in a counterexample,
\[
n\ge2r+6.
\]
Corollary 7.2 then gives one block \(B\) of \(F\) containing the whole corridor
\[
r+3,\ldots,n-r-2=r+3,\ldots,m-r.
\]
Since \(a,c\ge r\), whenever \(d=b-a\ge6\) the position interval
\[
a+4,\ldots,b-1
\]
lies inside this same block.

This allows one physical vertex to be tested at both extreme fronts without leaving the face.

**Theorem 7.7 (one-carrier compression in a recurrent face).** Suppose \(H\) has no spanning two-cover. Suppose \(F\) has positive balance on every chamber and contains no zero root. Let \(\pi\in\mathcal V(F)\) minimize switch span in \(F\). If \(d(\pi)\ge6\), then \(H\) contains a Hamiltonian support of order four or five.

**Proof.** Let
\[
W=\{v_{a+4},\ldots,v_{b-1}\}.
\]
Then \(|W|=d-4\ge2\), and all these positions lie in the single face block \(B\).

Fix \(w\in W\). First permute only positions \(a+4,\ldots,b-1\) inside \(B\) so that \(w\) occupies position \(a+4\). This preserves both extreme switches: the first switch is determined through position \(a+3\), while the last switch \(b\) is determined by positions \(b,\ldots,n\). Now swap positions \(a+3,a+4\). No switch before \(a\) can be created, and \(b\) is outside the affected window. If the first switch moved to the right, the new chamber of \(F\) would have smaller switch span, contrary to the choice of \(\pi\). Therefore the first switch remains \(a\).

Let \(\alpha\) be the first-run color. If \(\alpha=1\), the preceding statement says that \(w\) reverses the terminal edge of the tight-oriented left outer block. If \(\alpha=0\), the left outer block is tight after reversal and the same statement says that \(w\) reverses its initial edge.

Independently restart from \(\pi\), place the same \(w\) at position \(b-1\), and swap positions \(b-1,b\). The first switch is now outside the affected window. If the last switch moved left, the switch span would decrease. Hence the last switch remains \(b\). Writing \(\omega\) for the last-run color, \(w\) reverses the terminal edge of the tight-oriented right outer block when \(\omega=0\), and its initial edge when \(\omega=1\).

The two exposed edges are vertex-disjoint because \(d\ge6\).

If \(\alpha\ne\omega\), the two reversals have the same endpoint type: terminal-terminal for \((\alpha,\omega)=(1,0)\), and initial-initial for \((0,1)\). A common reverser of two disjoint same-type end edges gives a Hamiltonian four-support. For completeness, in the terminal-terminal case, if the two tight paths end in \(x_0,x_1\) and \(y_0,y_1\), then
\[
(w,x_1,x_0),\qquad(w,y_1,y_0)
\]
are tight. Exactly one of
\[
(x_1,w,y_1),\qquad(y_1,w,x_1)
\]
is tight. In the first case
\[
(x_1,w,y_1,y_0)
\]
is a tight four-path; in the second
\[
(y_1,w,x_1,x_0)
\]
is. The initial-initial case is symmetric.

Suppose now that \(\alpha=\omega\). The two reversals have mixed endpoint type. Up to symmetry write the tight-oriented exposed edges as
\[
\ldots,a_0,a_1
\qquad\text{and}\qquad
p_1,p_2,\ldots
\]
so that
\[
(w,a_1,a_0),\qquad(p_2,p_1,w)
\]
are tight. Exactly one of
\[
(p_1,w,a_1),\qquad(a_1,w,p_1)
\]
is tight. The first alternative gives the Hamiltonian five-path
\[
(p_2,p_1,w,a_1,a_0).
\]
In the second alternative \(w\) is a parallel middle between \(a_1\) and \(p_1\).

There are at least two choices of \(w\in W\). If neither gives a Hamiltonian five-support, choose distinct \(w,w'\) with
\[
(a_1,w,p_1),\qquad(a_1,w',p_1)
\]
tight. Exactly one of
\[
(w,a_1,w'),\qquad(w',a_1,w)
\]
is tight. Accordingly
\[
(w,a_1,w',p_1)
\quad\text{or}\quad
(w',a_1,w,p_1)
\]
is a tight four-path. Thus a Hamiltonian support of order four or five always occurs. \(\square\)

The proof deliberately uses the same physical carrier and two exposed edges from one chamber. It therefore does not require the false implication that two distinct reversers of one common edge force a four-support, and it does not require exposed edges belonging to two different witness orders to be disjoint.

Combining Lemmas 7.5–7.6 with Theorem 7.7 gives the non-diagonal face conclusion:
\[
\boxed{
\begin{array}{c}
\text{positively balanced carrier face with no zero root}
\\[2mm]\Longrightarrow\\[2mm]
\text{two-cover}
\ \vee\
\text{spanning three-cover with a component of order }\le3
\ \vee\
\text{Hamiltonian support of order }4\text{ or }5.
\end{array}}
\]

Thus the coordinated face structure eliminates the genuinely global giant-block residue. A nonzero recurrent chamber cannot remain trapped in an unbounded front-motion configuration.

### The diagonal branch is absorbed by global minimum span

A zero root need not itself be a two-cover, so it must not be silently identified with the exact target. There is, however, a face-independent version of the preceding carrier argument which absorbs this branch as well.

**Theorem 7.8 (global minimum-span compression).** Let \(H\) be a boundary \(3\)-tournament with no spanning two-cover. Choose a spanning order \(\pi\) with globally minimum switch span \(d=b-a\). Then exactly one of the following local outcomes occurs:

1. \(3\le d\le5\), and \(H\) has the spanning three-cover of Lemma 7.6 with a component of order at most three;
2. \(d\ge6\), and \(H\) contains a Hamiltonian support of order four or five.

**Proof.** A counterexample has no order with at most one switch, because such an order already splits into two monochromatic tight orientations. Lemma 7.5 excludes \(d\le2\).

For \(3\le d\le5\), apply Lemma 7.6.

Assume \(d\ge6\). Now the interval
\[
a+4,\ldots,b-1
\]
may be permuted freely in the full permutation space, rather than merely inside one face block. Repeat verbatim the two carrier tests from Theorem 7.7. If either extreme front moved inward, the resulting spanning order would have smaller switch span, contradicting global minimality. Thus the same carrier reverses the two disjoint exposed end edges. The same-end and mixed-end arguments above give a Hamiltonian support of order four or five. \(\square\)

This theorem is stronger as a compression statement than the topology needs: once a counterexample is assumed, large switch span is already impossible as an independent geodesic obstruction.

### Closure of the geodesic/topological branch

The root topology and the global geodesic extremal argument now meet at one precise interface.

Theorem 6.1 upgrades a convex zero to recurrence for every chamber of a carrier face. Theorem 7.7 converts every nonzero recurrent branch into a two-cover or bounded local GN3 structure. A zero-root chamber is not itself declared solved; Theorem 7.8 instead shows that the diagonal branch cannot retain an independent global geodesic obstruction either.

Consequently Article VII has no remaining unbounded permutahedral or antipodal-geodesic residue. In a hypothetical counterexample the output of the entire geodesic program is already local:
\[
\boxed{
\text{small-middle spanning three-cover}
\quad\vee\quad
\text{Hamiltonian }4\text{- or }5\text{-support}.
}
\]

This is a handoff, not a proof of the grand conjecture. In particular it does not assert
\[
R\cap A(R)\ne\varnothing.
\]
What has been closed is the specifically geodesic/topological conversion problem: balanced recurrence no longer needs to be synchronized into a global reachability state. Its only surviving consequences are the bounded GN3 configurations handled by the local path-cover machinery.


### Exact-deficiency sharpening: the one-hole four-support handoff


### Exact deficiency one in a minimum counterexample

The exact inversion coordinates from [[spanning_orders_and_defect_helly]] sharpen the minimum-span conclusion further. For a spanning order \(\pi\), write
\[
p(\pi)=\min\{i:\epsilon_i=0\},\qquad
q(\pi)=\max\{i:\epsilon_i=1\},
\]
and
\[
\delta(\pi)=q(\pi)-p(\pi)-1.
\]
By the exact inversion-window criterion,
\[
\operatorname{pc}(H)\le2
\iff
\exists\pi\text{ with }\delta(\pi)\le0.
\]
Thus every spanning order of a counterexample has \(\delta\ge1\).

**Theorem 7.9 (minimum exact deficiency is one).** Let \(H\) be a minimum counterexample to the two-cover conjecture. Then
\[
\min_\pi\delta(\pi)=1.
\]
More precisely, for every \(x\in V(H)\) and every displayed two-cover
\[
H-x=P\mid Q
\]
with \(P=(p_1,\ldots,p_r)\) and \(Q=(q_1,\ldots,q_s)\), the spanning order
\[
\pi=(p_1,\ldots,p_r,x,q_s,\ldots,q_1)
\]
has \(\delta(\pi)=1\).

**Proof.** First \(r,s\ge3\). Indeed, if one deletion-cover component had order at most two, adjoining \(x\) would give a set of order at most three, hence a Hamiltonian tight path; together with the other displayed component this would two-cover \(H\).

In \(\pi\), every status wholly inside \(P\) is \(1\), while every status wholly inside \(Q^{\rm rev}\) is \(0\). Hence only the three junction statuses
\[
(p_{r-1},p_r,x),\qquad
(p_r,x,q_s),\qquad
(x,q_s,q_{s-1})
\]
can interrupt the pattern \(1^*0^*\). Consequently
\[
p(\pi)\ge r-1,\qquad q(\pi)\le r+1,
\]
so
\[
\delta(\pi)=q(\pi)-p(\pi)-1\le1.
\]
Since \(H\) is a counterexample, the exact inversion-window criterion gives \(\delta(\pi)\ge1\). Therefore \(\delta(\pi)=1\). \(\square\)

Equality forces
\[
p(\pi)=r-1,\qquad q(\pi)=r+1.
\]
Thus the first and third junction statuses are forced:
\[
(p_{r-1},p_r,x)\text{ is non-tight},
\qquad
(x,q_s,q_{s-1})\text{ is tight}.
\]
By boundary reversal,
\[
(x,p_r,p_{r-1})
\]
is tight as well. Hence the omitted vertex \(x\) reverses the displayed terminal edge of each deletion path:
\[
(x,p_r,p_{r-1}),\qquad
(x,q_s,q_{s-1})
\quad\text{are tight}.
\]

This is exactly the deficiency-one instance of the canonical partial-cover construction in [[convex_root_balance_and_bourgin_yang]]: the exact root carries a two-path cover with one missing vertex, and the missing vertex controls both exposed terminal edges.

### The exact geodesic handoff is a four-support

The preceding double reversal has an immediate bounded consequence.

**Corollary 7.10 (canonical four-support from exact deficiency one).** Let \(H\) be a minimum counterexample. For every deletion cover
\[
H-x=P\mid Q,
\]
the terminal edges of \(P\) and \(Q\), together with \(x\), contain a Hamiltonian four-support. Its complement is non-Hamiltonian and has path-cover number exactly two.

**Proof.** Write the terminal edges of the displayed tight paths as
\[
\ldots,a_0,a_1,
\qquad
\ldots,b_0,b_1.
\]
Theorem 7.9 gives
\[
(x,a_1,a_0),\qquad(x,b_1,b_0)
\]
tight. Exactly one of
\[
(a_1,x,b_1),\qquad(b_1,x,a_1)
\]
is tight. In the first case
\[
(a_1,x,b_1,b_0)
\]
is a tight Hamiltonian four-path; in the second,
\[
(b_1,x,a_1,a_0)
\]
is.

Let \(K\) be this four-set. It is proper, since otherwise \(H\) itself would be Hamiltonian. By minimality, \(H-K\) has path-cover number at most two. It cannot be Hamiltonian, because a Hamilton path on \(H-K\) together with the displayed Hamilton path on \(K\) would two-cover \(H\). Hence
\[
\operatorname{pc}(H-K)=2
\]
and \(H-K\) is non-Hamiltonian. \(\square\)

This sharpens the minimum-counterexample endpoint of the geodesic investigation. The width-three switch-span formulation remains useful for arbitrary counterexamples and for the recurrent-face compression, but after minimum-counterexample induction the exact inversion coordinate removes the mixed-end ambiguity entirely:
\[
\boxed{
\text{minimum counterexample}
\Longrightarrow
\text{canonical Hamiltonian four-support with non-Hamiltonian two-coverable complement}.
}
\]

Thus no synchronization of an entire directed root cycle is needed to finish Article VII's own task. The exact-root coordinate already reaches the bounded local interface. What remains after this point is the local four-support/path-cover analysis, not an antipodal-geodesic obstruction.


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

Every increasing pole-to-pole path starts in \(R\), ends in \(A(R)\), and therefore must meet \(N\). Such paths exist from the permutation construction, so \(N\ne\varnothing\). This is separation for increasing paths; the argument does not exclude an undirected edge whose lower endpoint is in \(A(R)\) and upper endpoint in \(R\).

The interface colors are forced:

- every increasing edge from \(R\) to \(N\) has color \(0\);
- every increasing edge from \(N\) to \(A(R)\) has color \(1\).

The antipode exchanges these two frontiers.

Thus failure produces an antipodally invariant set separating every increasing pole geodesic, with prescribed colors at the two directed interfaces. Conversely, disjointness of these particular reachability regions is exactly failure of the directed one-change target.

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

A universal directed one-change theorem for boundary tournaments would apply to the auxiliary extension. The undirected one-change conjecture permits either switch direction; it implies the grand conjecture by application to H itself and the cut-and-reverse construction. It does not automatically select the directed target in an individual extension.

Alternatively, work only with the auxiliary extensions and exploit their special vertex together with the consistent triple rule. Antipodal symmetry of arbitrary chamber words alone does not encode that rule.

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


### Further developments



---

## Section — Synthesis and the exact topological frontier

<!-- section_id: article_vii_synthesis_and_exact_frontier -->

### Exact formulations and the pre-compression frontier

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

### Route A: prove the stronger one-change conclusion

The candidate from the second Section asks whether every boundary tournament has a spanning order with at most one color change. A reversal-complement function on ordered triples is exactly a boundary tournament, so the candidate concerns the same input class with a stronger desired conclusion.

If this candidate holds, apply it to \(H\) itself and split into monochromatic blocks, reversing the non-tight block. This gives a two-cover. A universal theorem specifically producing \(1^a0^b\) could instead be applied to \(H^+\) and Theorem 3. Reversal preserves the direction of the switch, so these two reductions must be distinguished.

The one-change sufficient condition also gives a tight path on at least \(\lceil(n+2)/2\rceil\) vertices. This quantitative consequence, the endpoint involution including singleton paths, and the positive square-zero enumeration remain part of the support formulation.

A genuinely broader input class is provided by the base-dependent memory rule in the second Section. Any theorem about that class would need a separate proof and a precise reduction.

### Route B: prove only the exact auxiliary target

The alternative is to prove directed one-change existence only for the extensions \(H^+\). This is exactly equivalent to the grand conjecture. One may use the forced endpoint behavior of the auxiliary vertex and the local tournament structure supplied by the triple rule.

Articles I–VI develop deletion-cover compatibility, quadratic-potential descent, defect-line compression, endpoint transport, longest-path reversal structure, and equal-potential recurrence. Article VII seeks to turn topological balance into hypotheses to which those arguments apply. Neither balanced roots nor a moved switch front alone establishes that the full hypotheses of a closing repartition are satisfied.

These are two routes distinguished by the strength of the conclusion and by whether the auxiliary vertex is used, not by a nonexistent distinction between boundary tournaments and reversal-complement triple functions.

### The apparent exact-reachability conversion

Before the minimum-span compression of Section 7, the natural missing implication was
\[
\boxed{
\text{balanced or recurrent extreme-switch data}
\quad\Longrightarrow?\quad
R\cap A(R)\ne\varnothing.
}
\]

That implication is still not proved, and proving it directly would prove the grand conjecture. The neutral-corridor formulation therefore remains a valid optional route to the theorem.

It is no longer, however, the frontier of Article VII. Section 7 shows combinatorially that the recurrence needed to support the balanced face already collapses to bounded local GN3 structure: one minimizes switch span and transports one physical carrier to both extreme fronts. The explicit Bourgin--Yang dimension bound remains a genuine topological statement, but no further conversion of its zero set into a reachability intersection is required for the geodesic investigation itself.

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

Article VII retains the exact Helly, auxiliary-geodesic, complementary-support, and directed-reachability formulations, together with the Coxeter geometry, the failure of graph-only labeling arguments, the explicit barycentric root construction, Bourgin--Yang multiplicity, and carrier-face recurrence.

Its specifically geodesic contribution is now complete at the correct level: recurrent nonzero face geometry and global minimum switch span eliminate every unbounded permutahedral obstruction and hand the problem to bounded local GN3 structure. The article does **not** prove the grand two-cover conjecture, and it does not claim the exact intersection \(R\cap A(R)\ne\varnothing\). Those stronger statements remain equivalent or sufficient routes to the global theorem, while the false cyclic two-component strengthening stays excluded by the balanced-cut obstruction above.


### Closure: width-three mixed-end handoff


### Article VII closure theorem

The exact formulations established earlier remain unchanged:
\[
\operatorname{pc}(H)\le2
\]
is equivalent to the defect-Helly cut condition, to a directed \(1^*0^*\) order in the auxiliary exactification, to the corresponding directed one-change pole geodesic, to the complementary-support formulation, and to
\[
R\cap A(R)\ne\varnothing
\]
in the exact memory lift.

The new compression in Section 7 changes the role of the topological route. It is no longer necessary to synchronize an arbitrary collection of balanced face witnesses into one global reachability state.

**Theorem 9.1 (geodesic compression to a local GN3 interface).** If a boundary \(3\)-tournament \(H\) has no spanning two-cover, then a globally minimum-switch-span spanning order has one of the following forms:

1. its switch span \(d\) satisfies \(3\le d\le5\), and it yields a spanning three-cover with a middle component of order \(d-2\le3\);
2. \(d\ge6\), and \(H\) contains a Hamiltonian support of order four or five.

Moreover, for the positively balanced carrier face of Theorem 6.1, the same conclusion already holds on every non-diagonal recurrent branch: minimum span within the face and one physical carrier eliminate the giant-block/front-motion residue.

Thus all unbounded permutahedral behavior has disappeared. The exact reachability formulation remains mathematically equivalent to the conjecture, but the topology no longer carries an independent unresolved global obstruction.

### Minimum counterexamples have exact width three

There is a sharper consequence in the setting relevant to the grand conjecture.

**Corollary 9.2.** Let \(H\) be a minimum counterexample to the two-cover conjecture. Then the minimum switch span over all spanning orders of \(H\) is exactly three.

**Proof.** Fix \(x\in V(H)\). By minimality,
\[
H-x=P\mid Q
\]
for two tight paths \(P,Q\). Insert \(x\) between their displayed orders:
\[
P,\ x,\ Q.
\]
Every status except the three junction statuses meeting \(x\) is inherited from \(P\) or \(Q\) and is tight. Hence all switches lie across a window of three consecutive variable statuses, so the first-to-last switch span is at most three.

A counterexample has no spanning order with at most one switch, and Lemma 7.5 excludes switch span at most two. Therefore the global minimum is exactly three. \(\square\)

For a minimum-span order with
\[
b=a+3,
\]
Lemma 7.6 becomes especially concrete:
\[
L\mid\{z\}\mid R,
\qquad
z=v_{a+3},
\]
where \(L\) and \(R\) have tight orientations.

The first-switch condition says that \(z\) reverses one exposed end edge of the tight-oriented \(L\); the last-switch condition says that the same \(z\) reverses one exposed end edge of the tight-oriented \(R\). Let \(\alpha,\omega\) be the first and last status colors.

- If \(\alpha\ne\omega\), the two reversals have the same endpoint type. Since the two exposed edges are disjoint, the common-reverser argument gives a Hamiltonian four-support.
- If \(\alpha=\omega\), the reversals have mixed endpoint type. Writing the tight-oriented exposed edges, up to symmetry, as
  \[
  \ldots,a_0,a_1
  \qquad\text{and}\qquad
  p_1,p_2,\ldots
  \]
  gives
  \[
  (z,a_1,a_0),\qquad(p_2,p_1,z)
  \]
  tight. Exactly one of
  \[
  (p_1,z,a_1),\qquad(a_1,z,p_1)
  \]
  is tight. The first gives the Hamiltonian five-path
  \[
  (p_2,p_1,z,a_1,a_0),
  \]
  while the second is the parallel-middle relation
  \[
  (a_1,z,p_1)\ \text{tight}.
  \]

Therefore the geodesic route has a single genuinely local terminal form after bounded Hamiltonian supports are separated off:

\[
\boxed{
\text{width-three singleton carrier with mixed-end parallel-middle data}.
}
\]

This is precisely a local GN3 configuration, not an antipodal-topology problem.

### Final status of the two topological formulations

The root-space formulation and the exact reachability formulation now have different roles.

The root-space topology is **closed as a compression mechanism**: positive balance on every chamber, block separation, and minimum-span carrier transport reduce every nonzero recurrent branch to a two-cover or bounded local structure, while global minimum span absorbs the diagonal branch.

The exact reachability statement
\[
R\cap A(R)\ne\varnothing
\]
remains an exact reformulation of the grand conjecture, not an independently proved theorem. A direct topological proof of that intersection would still solve the conjecture, but Article VII no longer needs such a proof in order to finish its own geodesic investigation. Any hypothetical failure is already compressed to the width-three local interface above.

Accordingly, no further continuation of the antipodal-geodesic, carrier-face, Tucker/Ky Fan, Bourgin--Yang, or neutral-corridor machinery is presently justified. The unresolved mathematics lies in the local GN3 handoff, which belongs to the other articles' path-cover and small-support arguments rather than to Article VII.


### Exact-deficiency sharpening of the terminal handoff


### Exact-deficiency sharpening of the terminal handoff

The exact inversion-window coordinates sharpen the minimum-counterexample conclusion one final step. For
\[
\delta(\pi)=q(\pi)-p(\pi)-1,
\]
the exact criterion of Section 1 says that \(\delta\le0\) is already a two-cover certificate. If \(H\) is a minimum counterexample and
\[
H-x=P\mid Q,
\]
then the order
\[
(P,x,Q^{\rm rev})
\]
has all statuses away from the three \(x\)-junctions equal to \(1\) on the left and \(0\) on the right. Hence \(\delta\le1\); counterexamplehood forces
\[
\delta=1.
\]

The deficiency-one canonical partial cover from Section 6 therefore has a single hole, namely \(x\). Its two displayed tight paths are exactly \(P\) and \(Q\), and \(x\) reverses the terminal edge of both. A common terminal-edge reverser of two disjoint tight paths gives a Hamiltonian four-support. By minimum-counterexample induction its complement is non-Hamiltonian with path-cover number exactly two.

Accordingly the sharp terminal statement of Article VII is
\[
\boxed{
\text{minimum counterexample}
\Longrightarrow
\text{canonical Hamiltonian four-support }K
\text{ with }\operatorname{pc}(H-K)=2
\text{ and }H-K\text{ non-Hamiltonian}.
}
\]

This strictly sharpens the earlier width-three \(4/5\)-support or mixed-end description. The width-three and recurrent-face theorems remain the correct global compression statements for an arbitrary no-two-cover boundary tournament; the exact-deficiency argument is the stronger endpoint available after minimum-counterexample induction.

It also resolves the specific synchronization question raised by the coordinated-face program at the level needed by this article. One may still study directed cycles of exact roots, but Article VII does not need to turn a whole cycle into one reachability intersection. The exact inversion coordinate collapses a minimum counterexample to a one-hole deletion cover before that synchronization is necessary, and the one hole already forces the canonical four-support handoff.

The direct reachability assertion
\[
R\cap A(R)\ne\varnothing
\]
remains equivalent to the grand conjecture and is not proved here. Article VII is closed more modestly and more sharply: the global geodesic/topological obstruction has been eliminated, and the surviving minimum-counterexample state is a single bounded four-support interface.
