# The directed ordered-tuple one-change conjecture

## Metadata

- ID: the_higher_memory_one_change_geodesic_conjecture
- Parent Section: higher_memory_norine_geodesics
- Position: 1
- Row version: 5
- Development version: 3
- Composition version: 2
- Composition stale: True

## Composition


Fix \(k\ge1\). Color every ordered \((k+1)\)-tuple
\[
(X_0,\ldots,X_k)
\]
forming a \(k\)-edge cube geodesic segment. Impose only the antipodal-reversal rule
\[
\chi(\bar X_k,\ldots,\bar X_0)=1-\chi(X_0,\ldots,X_k).
\]

**Grand Conjecture \(N_k\).** Every such coloring admits an antipodal cube geodesic whose consecutive ordered-\(k\)-segment colors change at most once.

For \(k=1\), ordinary Norine edge colorings form the reversal-invariant subclass. For \(k=3\), every GN3 boundary tournament is a canonical subclass via
\[
\chi(X_0,X_1,X_2,X_3)=h(u,v,w),
\]
where \(u,v,w\) are the successive flipped coordinates. Every antipodal geodesic flips each coordinate exactly once, so its ordered-window word is exactly the GN3 status word of its flip order.


## Development


## Grand conjecture: directed ordered tuples

Let \(V\) be an \(n\)-element set and fix \(k\ge2\).

A directed ordered-\(k\)-tuple coloring is a binary function
\[
h(v_1,\ldots,v_k)\in\{0,1\}
\]
on ordered \(k\)-tuples of distinct elements of \(V\), satisfying reversal antisymmetry
\[
h(v_k,\ldots,v_1)=1-h(v_1,\ldots,v_k).
\]

For a permutation
\[
\pi=(v_1,\ldots,v_n),
\]
its induced word is
\[
h(v_1,\ldots,v_k),\,
h(v_2,\ldots,v_{k+1}),\ldots,
h(v_{n-k+1},\ldots,v_n).
\]

### Grand Conjecture \(N_k\)

For every \(n\ge k\) and every such directed coloring \(h\), there exists a permutation whose induced word changes value at most once.

Equivalently, some word is of the form
\[
0^*1^*
\quad\text{or}\quad
1^*0^*.
\]

### Cube formulation

Given an antipodal cube geodesic
\[
X_0,\ldots,X_n=\bar X_0
\]
with successive flipped coordinates
\[
v_1,\ldots,v_n,
\]
the directed tuple word is the word above.

Thus the coloring depends only on the ordered flipped coordinates, not on the absolute cube rank or starting vertex. Global XOR translation of the whole cube changes only the coordinate chart and leaves the directed tuple data unchanged.

Equivalently, \(N_k\) is the translation-invariant subclass of the larger ordered-window coloring problem.

### Relation to known subclasses

For \(k=2\), reversal antisymmetry is exactly a tournament orientation on unordered pairs, and a directed Hamilton path gives a constant word.

For \(k=3\), every GN3 boundary tournament embeds by
\[
h(u,v,w)\in\{0,1\},
\qquad
h(w,v,u)=1-h(u,v,w).
\]

The ordinary undirected Norine edge problem is a related lower-memory problem but is not literally the \(k=1\) case of this reversal-antisymmetric directed-tuple definition, since reversal fixes a one-entry tuple.

### Guardrail

A broader coloring of full cube windows
\[
\chi(X_0,\ldots,X_k)
\]
that may depend on the absolute base vertex \(X_0\) is a different problem. Rank-parity gives a counterexample to that broader class. It does not refute \(N_k\) as defined here.


## Uncompressed development

- Development has changed since this Subsection's current composition.
