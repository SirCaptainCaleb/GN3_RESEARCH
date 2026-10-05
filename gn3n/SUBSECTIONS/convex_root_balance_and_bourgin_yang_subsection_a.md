# Balance, circulation, and multiplicity of zeros

## Metadata

- ID: convex_root_balance_and_bourgin_yang_subsection_a
- Parent Section: convex_root_balance_and_bourgin_yang
- Position: 1
- Row version: 5
- Development version: 4
- Composition version: 2
- Composition stale: False

## Cold composition

### Root balance and zero-set dimension

Associate to a directed arc \(i\to j\) the type-\(A\) root \(e_i-e_j\).

**Root-balance criterion.**
For a finite directed graph \(E\),
\[
0\in\operatorname{conv}\{e_i-e_j:(i,j)\in E\}
\iff
E\text{ contains a directed cycle}.
\]
A convex zero is a nonzero nonnegative circulation, and every such circulation contains a directed cycle; the converse follows by summing the roots around a cycle.

We use the following standard dimension form of Bourgin--Yang. If
\[
f:S^d\to\mathbb R^q
\]
is continuous and odd with \(q\le d\), then
\[
\dim f^{-1}(0)\ge d-q.
\]
Accordingly, once a chamber-root map is shown to take values in a specified \(q\)-dimensional subspace, the dimension estimate applies to its whole zero locus. Any further combinatorial conclusion must be proved from the carrier faces supporting those zeros.

## Development

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
