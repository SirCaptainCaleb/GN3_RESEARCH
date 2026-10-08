# Exact formulations and the pre-compression frontier — preserved pre-item development

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
