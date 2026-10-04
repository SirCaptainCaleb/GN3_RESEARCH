# Antipodal geometry of permutation space

**Summary:** The space of spanning orders has a natural antipodal simplicial geometry, but the tournament color lives on triples of successive directions rather than ordinary cube edges.

## Statement

Monotone cube geodesics are permutations; the staircase triangulation packages them into an antipodal type-A sphere after taking the link of the long diagonal, while boundary-tournament triple colors become antipodally complemented local data on three successive directions.

## Body

## Permutation simplices and monotone geodesics

Let \(V\) be an \(n\)-element label set. A monotone geodesic from \(\varnothing\) to \(V\) in the \(n\)-cube adds every label exactly once, hence is specified by a permutation
\[
\pi=(v_1,\ldots,v_n),\qquad S_i=\{v_1,\ldots,v_i\}.
\]
The simplex
\[
\Delta_\pi=\operatorname{conv}\{\mathbf 1_{S_0},\ldots,\mathbf 1_{S_n}\}
\]
is one maximal simplex of the standard staircase triangulation of \([0,1]^V\). Its region is
\[
1\ge x_{v_1}\ge \cdots\ge x_{v_n}\ge0.
\]
Thus the maximal simplices are exactly the monotone pole-to-pole geodesics, and adjacent permutation simplices meet along faces obtained by tying coordinate inequalities.

This is the geometric realization of the spanning-order space used throughout the geodesic approach.

## The antipodal link of the long diagonal

Every maximal staircase simplex contains the long diagonal \([\mathbf0,\mathbf1]\). The simplicial link of that diagonal consists of chains of nonempty proper subsets of \(V\), hence is the barycentric subdivision of the boundary of an \((n-1)\)-simplex and therefore an \((n-2)\)-sphere.

Cube complementation \(A(x)=\mathbf1-x\) sends \(\Delta_\pi\) to \(\Delta_{\pi^{\rm rev}}\). On the link it sends a subset chain to its complementary reversed chain and is fixed-point-free. In centered coordinates it is realized by negation on
\[
\mathbf1_S-\frac{|S|}{n}\mathbf1.
\]
So the permutation complex carries the standard antipodal action of the type-\(A\) Coxeter sphere.

This identifies the right topological carrier. Working on the whole cube is too coarse: every odd map has the automatic zero at the cube center, which does not select a distinguished permutation. Any Borsuk-Ulam/Tucker/Sperner-style argument must use the link or an equivalent pole-relative object.

## Triple colors as antipodal local data

Write
\[
h(u,v,w)=
\begin{cases}
1,&(u,v,w)\text{ is tight},\\
0,&(u,v,w)\text{ is non-tight}.
\end{cases}
\]
Boundary reversal is
\[
h(w,v,u)=1-h(u,v,w).
\]
For \(\pi=(v_1,\ldots,v_n)\), the consecutive-triple word is
\[
h(v_1,v_2,v_3),\ldots,h(v_{n-2},v_{n-1},v_n).
\]

The color at a triple of successive directions \(u,v,w\) belongs naturally to the tetrahedral face
\[
S,\quad S\cup\{u\},\quad S\cup\{u,v\},\quad S\cup\{u,v,w\}
\]
of the staircase triangulation and is independent of the base subset \(S\). Complementation reverses the successive directions to \(w,v,u\) and therefore complements the color.

This is the precise common structure with antipodal cube-coloring problems such as the Norine line of ideas: geodesics are permutations, opposite geodesics are reversals, and the local datum flips under the antipode. The important difference is that our color is attached to three consecutive directions, not directly to an ordinary cube edge. Any imported antipodal-path theorem must therefore survive this memory requirement rather than silently forgetting it.

## Metadata

- ID: antipodal_permutation_geometry
- Kind: section
- Version: 9
- Math version: 3
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — crystallized, version 4: Permutation simplices and monotone geodesics
- Subsection 2 — crystallized, version 4: The antipodal link of the long diagonal
- Subsection 3 — HOT, version 3: Triple colors as antipodal local data
