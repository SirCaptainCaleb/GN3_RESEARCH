# Doubled-cube Frankl lift and antimatroid NOR supports

Formalize the doubled-cube idea for a union-closed family, correct the pedestrian analogy, and connect union closure to NOR feasible-support families.

## Follow-up: doubled cube, Fourier form of Frankl, and accessible NOR supports

### Correction to the first Frankl brainstorm

The cube pedestrian dimension sweep does not rely on commutativity of the coordinate matching swaps. Restricted coordinate matchings in a cube subgraph can fail to commute. Its key feature is instead that every called coordinate acts by a permutation (a product of disjoint transpositions and fixed points), so one pedestrian per vertex is preserved. By contrast, union maps \(T_B(A)=A\cup B\) commute and are idempotent but generally merge pedestrians. The collision problem is therefore the substantive difference.

### Antipodal doubled-cube lift of a set family

Let \(\mathcal F\subseteq2^V\), and define
\[
g(A)=
\begin{cases}
+1,&A\in\mathcal F,\\
-1,&A\notin\mathcal F.
\end{cases}
\]
On \(Q_{V\cup\{\star\}}\cong Q_V\times\{0,1\}\), define
\[
G(A,0)=g(A),\qquad
G(A,1)=-g(V\setminus A).
\]
Then the cube antipode \((A,0)\mapsto(V\setminus A,1)\) satisfies
\[
G(V\setminus A,1)=-G(A,0).
\]
Thus any set family has a canonical antipodal lift.

If \(\mathcal F\) is union-closed, the \(+\)-vertices in the lower layer are closed under coordinatewise join. Their antipodal \(-\)-vertices in the upper layer are the complements of members of \(\mathcal F\), hence are closed under coordinatewise meet.

So union closure becomes a join/meet constraint inside an antipodal coloring.

### Frankl is a first-level Fourier sign condition on the lift

For \(i\in V\), put
\[
x_i(A)=
\begin{cases}
+1,&i\in A,\\
-1,&i\notin A.
\end{cases}
\]
Let
\[
m=|\mathcal F|,\qquad
f_i=|\{A\in\mathcal F:i\in A\}|.
\]
Then
\[
\sum_{(A,b)\in Q_{n+1}}G(A,b)x_i(A)
=
4(2f_i-m).
\]
Equivalently, with normalized Fourier coefficients,
\[
\widehat G(\{i\})
=
\frac{2f_i-m}{2^{n-1}}.
\]

Hence Frankl's conjecture is exactly:

> For the antipodal lift of every nontrivial union-closed family, at least one old-coordinate first-level Fourier coefficient is nonnegative.

This is an exact bridge from union closure to antipodal cube coloring; the union-closed hypothesis is what must force the sign.

### NOR feasible-support families are automatically accessible

Fix a NOR color \(\sigma\) and ordered terminal \((r-1)\)-tuple \(S\). Let
\[
\mathcal F_{\sigma,S}
=
\{A\subseteq V\setminus S:
\text{some ordering }(a_1,\ldots,a_t,S)\text{ is }\sigma\text{-tight}\}.
\]
This family contains the empty set and is accessible: if \(A\ne\varnothing\) is feasible, choose a witnessing order
\[
(a_1,\ldots,a_t,S).
\]
Deleting \(a_1\) leaves a tight witness for \(A\setminus\{a_1\}\).

Therefore if \(\mathcal F_{\sigma,S}\) were union-closed, it would be an antimatroid (an accessible union-closed family).

Accessibility then completely resolves the union-map collision issue. Any nontrivial accessible family contains a feasible singleton \(\{x\}\). Union closure gives
\[
A\mapsto A\cup\{x\}
\]
from feasible sets avoiding \(x\) into feasible sets containing \(x\). This map is injective and is literally the ordinary \(x\)-coordinate matching of the Boolean cube. Thus \(x\) belongs to at least half the feasible supports.

So for NOR support families, union closure would restore exactly the occupancy-preserving pedestrian mechanism that arbitrary union maps lack.

### Research consequence

The important object is therefore not a generic Frankl analogy but the failure of antimatroid structure.

A closure-relevant target is:

1. determine whether some naturally chosen \(\mathcal F_{\sigma,S}\) in a minimum NOR counterexample must be union-closed;
2. failing that, choose a minimal pair of feasible supports \(A,B\) for which \(A\cup B\) is infeasible;
3. exploit accessibility to strip \(A,B\) down until this minimal failure becomes a local exchange obstruction.

Such a minimal non-union pair is a precise certificate of the branch-retention failure in the current tight-fork augmentation problem.

### Relation to the edge-ordered origin

For ternary coordinate labels coming from an edge ordering, fixing the center \(b\) makes the local extension sets nested suffixes of the total order on edges incident to \(b\). Nested families are union-closed. Thus the historical enlargement
\[
\text{edge-ordered monotone paths}\to\text{directed NOR}
\]
can be viewed as discarding a strong local closure property.

The possible intermediate program is therefore:
\[
\text{nested local feasibility}
\subset
\text{antimatroid / union-closed feasibility}
\subset
\text{arbitrary accessible NOR feasibility}.
\]
This may isolate exactly which part of the original edge-order structure was actually doing useful work.
