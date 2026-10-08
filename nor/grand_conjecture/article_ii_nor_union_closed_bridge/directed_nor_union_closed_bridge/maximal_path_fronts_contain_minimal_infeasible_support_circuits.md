# Maximal-path fronts contain minimal infeasible support circuits

## Composition

(none yet)

## Development

## Minimal infeasible front circuits are the exact obstruction exposed by a maximal tight path

Fix coordinate arity \(r\ge2\), a reversal-antisymmetric binary label \(h\), and a color \(\sigma\). Let
\[
P=(p_1,\ldots,p_t,S)
\]
be an inclusion-maximal \(\sigma\)-tight path with ordered terminal \((r-1)\)-tuple \(S\). Let
\[
F=(p_1,\ldots,p_{r-1})
\]
be its exposed front and let
\[
X=V\setminus V(P).
\]

The maximal-path front theorem gives, for every \(x\in X\),
\[
h(x,F)=1-\sigma.
\]
Hence every singleton \(\{x\}\) is feasible in the opposite-color fixed-tail family
\[
\mathcal G(P)
=
\{A\subseteq X:
\text{some ordering of }A,F\text{ is }(1-\sigma)\text{-tight}\}.
\]
The same theorem shows that \(X\notin\mathcal G(P)\) in a counterexample.

### Definition
A **front circuit** for \(P\) is an inclusion-minimal set
\[
U\subseteq X
\]
with
\[
U\notin\mathcal G(P).
\]

### Theorem
Every maximal monochromatic tight path in a counterexample has a front circuit \(U\) satisfying:

1. \(|U|\ge2\).
2. Every proper subset of \(U\) belongs to \(\mathcal G(P)\).
3. In particular, for every \(x\in U\), the deletion support
   \[
   U\setminus\{x\}
   \]
   has a \((1-\sigma)\)-tight witness ending at the same ordered tail \(F\).
4. For every such witness \(W_x\), the omitted vertex \(x\) is blocked at its exposed front. If \(E_x\) is the first ordered \((r-1)\)-tuple of \(W_x\), then
   \[
   h(x,E_x)=\sigma.
   \]

### Proof
Because \(X\notin\mathcal G(P)\) and \(X\) is finite, choose an inclusion-minimal infeasible subset \(U\subseteq X\). Every singleton of \(X\) is feasible, so \(U\) cannot have size one. Minimality gives feasibility of every proper subset, proving (1)--(3).

For (4), let \(W_x\) be a \((1-\sigma)\)-tight witness for \(U\setminus\{x\}\) ending at \(F\). If
\[
h(x,E_x)=1-\sigma,
\]
then prepending \(x\) to \(W_x\) would give a \((1-\sigma)\)-tight witness for all of \(U\), contrary to infeasibility. Hence
\[
h(x,E_x)=\sigma.
\]
\(\square\)

### Why this is stronger than a top-missing square
A minimal failure of union closure only supplies
\[
C,\ C+a,\ C+b\text{ feasible},\qquad C+a+b\text{ infeasible}.
\]
A front circuit supplies all proper subsets of one obstruction as feasible simultaneously.

Thus the obstruction exposed by maximality is not merely a missing Boolean-square top. It is a finite deletion-complete infeasible support:
\[
U\notin\mathcal G(P),
\qquad
U-\{x\}\in\mathcal G(P)\ \text{for every }x\in U.
\]

This is the fixed-tail analogue of a minimum-counterexample reduction. The ambient counterexample produces a smaller local object with deletion witnesses for every vertex, all sharing the same terminal state \(F\), but whose full support has no monochromatic witness.

### Ternary specialization
For \(r=3\), write
\[
F=(f_1,f_2),\qquad \tau=1-\sigma.
\]
Every \(x\in U\) satisfies
\[
h(x,f_1,f_2)=\tau.
\]

If \(|U|=2\), say \(U=\{a,b\}\), infeasibility is equivalent to
\[
h(a,b,f_1)=h(b,a,f_1)=\sigma.
\]
Indeed the only two possible witnesses on \(U\) are
\[
(a,b,f_1,f_2),\qquad (b,a,f_1,f_2),
\]
and their second windows already have color \(\tau\). Thus a two-element front circuit is exactly the local sandwich
\[
\sigma,\tau
\]
in either ordering.

If \(|U|=3\), every pair support is feasible, so for each unordered pair \(\{a,b\}\subset U\) at least one of
\[
h(a,b,f_1),\qquad h(b,a,f_1)
\]
equals \(\tau\). The failure of the three-element support then imposes an additional residual-triple obstruction on every pair orientation that could serve as the last pair of a witness. This is the smallest setting in which the common-tail deletion-cycle phenomena can arise.

### Closure program suggested by front circuits
The grand conjecture would follow from any theorem ruling out front circuits in a reversal-antisymmetric tight-path system.

A more realistic next target is a circuit-elimination principle: show that two front circuits sharing a vertex can be combined, using reversal and blocked-front recentering, to produce a strictly smaller front circuit or a spanning one-change order. Such an elimination law would replace witness synchronization by a finite obstruction calculus and would be directly analogous to the role of circuits in matroid-style exchange theory.

No circuit-elimination statement is asserted here. The theorem above is the reduction: every counterexample canonically contains one of these deletion-complete local obstructions at the exposed front of every maximal monochromatic path.
