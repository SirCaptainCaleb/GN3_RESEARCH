# The Norine–GN3 dictionary and Freudenthal geometry

**Summary:** The cube geometry is shared, while the triple rule carries two steps of memory. The one-change candidate strengthens the conclusion on the same input class.

## Statement

Monotone cube geodesics are permutations and Freudenthal simplices. A base-independent reversal-complement triple rule is exactly a boundary tournament; base-dependent memory is a genuinely larger class.

## Cold composition

## Geodesic chambers, memory, and the stronger general route

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


## Proof-transfer meta-conjecture

The present GN3 problem and Norine-type antipodal cube-geodesic problems share the same global Freudenthal/Coxeter chamber geometry but differ in their local data.

For GN3, the geodesic status comes from a base-independent two-memory rule
[
h(u,v,w)in{0,1},
qquad
h(w,v,u)=1-h(u,v,w).
]
A broader bounded-memory cube model may allow
[
g(S;u,v,w)
]
to depend on the current base set (S), subject to the corresponding antipodal reversal-complement identity. Ordinary Norine edge colorings belong naturally to the lower-memory side of that broader class.

This motivates an independent meta-conjecture:

> Whatever arguments ultimately close the boundary-tournament conjecture should contain a substantial portable core which, after suitable reformulation, seeds a proof of a generalized Norine geodesic conjecture.

The most plausible portable ingredients are the chamber topology, antipodal symmetry, local witness-tree compression, carrier recurrence, and a relative-index/terminalization argument. The steps most likely to remain GN3-specific are the strong face-permutation arguments that use translation invariance of (h(u,v,w)), especially endpoint swaps and blockwise splicing.

Accordingly the final proof should be decomposed after closure into:
1. purely chamber-topological arguments;
2. bounded-memory local arguments;
3. genuinely GN3-specific translation-invariant arguments.

The independent brainstorm [[meta_conjecture_gn3_closure_should_seed_generalized_norine]] records this research program. It is not required for the present conjecture, but it should remain visible while the terminalization theorem is developed.

## Metadata

- ID: norine_gn3_dictionary_and_freudenthal_geometry
- Kind: section
- Version: 7
- Math version: 4
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — Geodesic chambers, memory, and the stronger general route](../SUBSECTIONS/norine_gn3_dictionary_and_freudenthal_geometry_subsection_a.md) (\`norine_gn3_dictionary_and_freudenthal_geometry_subsection_a\`; development v4; composition v1; stale=False)
- [Subsection 2 — Proof-transfer meta-conjecture](../SUBSECTIONS/norine_gn3_dictionary_and_freudenthal_geometry_subsection_b.md) (\`norine_gn3_dictionary_and_freudenthal_geometry_subsection_b\`; development v3; composition vNone; stale=True)
