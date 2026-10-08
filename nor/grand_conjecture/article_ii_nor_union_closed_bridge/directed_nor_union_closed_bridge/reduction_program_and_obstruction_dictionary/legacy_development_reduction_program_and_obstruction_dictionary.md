# Reduction program and obstruction dictionary — preserved pre-item development

## Reduction program: what a successful transformation must preserve

A genuine reduction should transform a counterexample to one conjecture into a counterexample to the other, or transform a theorem for one class into a theorem for the other without importing the desired conclusion by hand.

### Frankl to directed NOR

Given a union-closed family \(\mathcal F\subseteq2^V\), the canonical doubled-cube lift produces an antipodal vertex coloring
\[
G:Q_{V\cup\{\star\}}\to\{\pm1\}.
\]
To reduce Frankl to directed NOR one would need to convert this vertex coloring into a reversal-antisymmetric ordered-window coloring
\[
h(v_1,\ldots,v_r)
\]
such that a one-change antipodal geodesic forces
\[
f_i\ge |\mathcal F|/2
\]
for some \(i\).

The main obstacle is translation invariance. Directed NOR forgets the base vertex and remembers only the ordered flipped coordinates, whereas membership in a general union-closed family is highly basepoint-dependent. Any reduction must therefore encode the missing basepoint information into extra coordinates, extra window state, or a larger ordered tuple without destroying reversal antisymmetry.

This is a concrete encoding problem.

### Directed NOR to Frankl

Fix color \(\sigma\) and terminal ordered state \(S\). The feasible-support family
\[
\mathcal F_{\sigma,S}
=
\{A:\text{some ordering of }A,S\text{ is }\sigma\text{-tight}\}
\]
is always accessible.

If one could canonically enlarge or quotient this accessible family to a union-closed family
\[
\mathcal U_{\sigma,S}
\]
while retaining enough witness-order information that a frequent coordinate in \(\mathcal U_{\sigma,S}\) yields a fork augmentation, then Frankl would become a possible engine for NOR.

The obstruction is exact: support feasibility forgets the witness order. Minimal failure of union closure is localized on a top-missing Boolean square, and such a square can survive only through incompatible witness orders.

Thus a NOR-to-Frankl reduction must solve the witness-synchronization problem rather than merely take unions of feasible supports.

### Edge-ordered intermediary

For ternary labels arising from an edge ordering,
\[
h(a,b,c)=0\iff \lambda(ab)<\lambda(bc),
\]
the local feasible extension sets at a fixed center are nested suffixes of a total order. Hence the edge-ordered subclass retains strong local union closure.

This suggests an interpolation program:
\[
\text{edge-ordered / nested}
\subset
\text{union-closed or antimatroid-like}
\subset
\text{arbitrary directed NOR}.
\]

A successful reduction may first be obtainable on this intermediate class. The research question is then whether the reduction survives after replacing nestedness by accessibility plus reversal structure.

### Pedestrian collision formulation

The cube pedestrian lemma uses coordinate calls that permute pedestrians. Union maps
\[
T_B(A)=A\cup B
\]
instead merge pedestrians. For Frankl, if \(i\in B\), the map
\[
\mathcal F_i^0\to\mathcal F_i^1,\qquad A\mapsto A\cup B,
\]
has the correct direction but can collide.

Thus one concrete bridge problem is:

> Find a canonical collection of union maps, or a refinement of their targets, that restores enough injectivity to compare \(|\mathcal F_i^0|\) and \(|\mathcal F_i^1|\).

For accessible union-closed families this collision problem disappears once a feasible singleton \(\{i\}\) exists, because
\[
A\mapsto A\cup\{i\}
\]
is the ordinary cube matching. This is why antimatroid structure is especially relevant to NOR feasible-support families.
