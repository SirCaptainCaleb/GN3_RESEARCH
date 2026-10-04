# The Norine–GN3 dictionary and Freudenthal geometry

**Summary:** GN3 and Norine-style cube problems share the same antipodal geodesic chamber space, but GN3 colors three successive directions and has extra local tournament structure.

## Statement

Monotone antipodal cube geodesics, permutations, and maximal Freudenthal simplices are the same objects; GN3 supplies a two-step-memory antipodal coloring with additional boundary-tournament rigidity.

## Body

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


## Metadata

- ID: norine_gn3_dictionary_and_freudenthal_geometry
- Kind: section
- Version: 3
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — crystallized, version 3: Geodesic chambers, memory, and the stronger general route
- Subsection 2 — HOT, version 1: Further developments
