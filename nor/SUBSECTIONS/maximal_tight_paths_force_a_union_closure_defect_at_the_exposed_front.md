# Maximal tight paths force a union-closure defect at the exposed front

## Metadata

- ID: maximal_tight_paths_force_a_union_closure_defect_at_the_exposed_front
- Parent Section: directed_nor_union_closed_bridge
- Position: 8
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Every directed NOR counterexample exposes a canonical union-closure defect at the front of each inclusion-maximal monochromatic tight path. If P is sigma-tight, F its exposed first (r-1)-tuple, and X the omitted vertices, maximality forces every singleton {x}, x in X, to lie in the opposite-color family F_{1-sigma,F}; yet X itself cannot lie there, because a witness for X spliced onto P would give a spanning one-change order. Hence the restricted front family is accessible, contains all singleton omitted vertices, and omits their total union. Full union closure is therefore sufficient for NOR, and the remaining bridge problem is exactly to resolve this missing union while preserving witness order.

## Development

## Maximal tight paths force a union-closure defect at the exposed front

Fix coordinate arity \(r\ge 2\), a reversal-antisymmetric binary label \(h\), a color \(\sigma\), and a terminal ordered \((r-1)\)-tuple \(S\). Let
\[
\mathcal F_{\sigma,S}
=
\{A\subseteq V\setminus S:\text{some ordering of }A,S\text{ is }\sigma\text{-tight}\}.
\]

Choose an inclusion-maximal support \(M\in\mathcal F_{\sigma,S}\), and choose a witnessing \(\sigma\)-tight order
\[
P=(p_1,\ldots,p_t,S)
\]
on \(M\cup S\). Let \(F\) be the first ordered \((r-1)\)-tuple of \(P\), and put
\[
X=V\setminus(M\cup S).
\]

### Theorem
For every \(x\in X\),
\[
\{x\}\in\mathcal F_{1-\sigma,F}.
\]
Moreover, if
\[
X\in\mathcal F_{1-\sigma,F},
\]
then the NOR conclusion holds: there is a spanning coordinate order whose color word changes at most once.

### Proof
If \(x\in X\) satisfied
\[
h(x,F)=\sigma,
\]
then prepending \(x\) to \(P\) would give a \(\sigma\)-tight witness for \(M\cup\{x\}\) ending at the same terminal state \(S\), contradicting the inclusion-maximality of \(M\). Hence
\[
h(x,F)=1-\sigma
\]
for every omitted vertex \(x\), which is exactly
\[
\{x\}\in\mathcal F_{1-\sigma,F}.
\]

Now suppose \(X\in\mathcal F_{1-\sigma,F}\). Choose a \((1-\sigma)\)-tight witness
\[
Q=(x_1,\ldots,x_m,F)
\]
for \(X\). Write
\[
P=(F,T),
\]
where \(T\) is the suffix of \(P\) following its first \(r-1\) entries. Concatenate along the common ordered tuple \(F\):
\[
W=(x_1,\ldots,x_m,F,T).
\]
The entries of \(W\) are precisely all vertices of \(V\), each once. Every \(r\)-window wholly inside \(Q\) has color \(1-\sigma\), while the next window and every later window are the corresponding windows of \(P\), hence have color \(\sigma\). Therefore the color word of \(W\) changes at most once. \(\square\)

### Counterexample consequence
In a counterexample, for every inclusion-maximal tight witness \(P\) with nonempty omitted set \(X\), the restricted family
\[
\mathcal G(P)
=
\{A\subseteq X:A\in\mathcal F_{1-\sigma,F}\}
\]
is accessible, contains \(\varnothing\) and every singleton \(\{x\}\) for \(x\in X\), but omits \(X\). Consequently \(\mathcal G(P)\) is not union-closed.

Thus every counterexample canonically exposes a union-closure defect at the front of every maximal monochromatic tight path. The defect is stronger than a generic failure of closure: all singleton branches are already feasible, while their total union is infeasible.

### Corollary: antimatroid front criterion
If every feasible-support family \(\mathcal F_{\tau,T}\) is union-closed, then directed NOR holds.

Indeed, take any inclusion-maximal tight witness \(P\). Its opposite-color front family contains all singleton omitted vertices by the theorem. Union closure then puts their union \(X\) in that family, and the splice above gives the desired spanning one-change order.

More generally, full union closure is unnecessary. It suffices that for the opposite-color family exposed by one maximal tight witness, the union of its omitted singleton supports is feasible.

### Relation to the union-closed bridge
This identifies the precise role that union-closed structure can play in NOR. Frankl-type frequency information is not yet enough by itself: what the splice needs is witness-preserving union of the blocked singleton branches. But if a canonical NOR-to-union-closed transformation can preserve those singleton witnesses and certify their total union, NOR closes immediately.

Accordingly, the bridge problem can be sharpened from “find an abundant coordinate” to:

> Given the accessible family at the exposed front of a maximal tight path, explain why its simultaneously feasible singleton branches admit a common feasible union, or else exploit a minimal obstruction to that union.

This is the direct higher-arity analogue of tournament insertion: at arity two, the feasible-support families are antimatroids and the obstruction cannot occur.
