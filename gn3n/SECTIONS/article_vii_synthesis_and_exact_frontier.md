# Synthesis and the exact topological frontier

**Summary:** Article VII ends with two legitimate closure routes: prove a stronger antipodal memory-geodesic theorem, or use GN3-specific local structure to convert topological recurrence into the exact reachability intersection.

## Statement

The two-cover conjecture has exact Helly, auxiliary-geodesic, complementary-support, and reachability formulations; topology supplies recurrence but must still be converted into an actual exactified intersection or into GN3-specific local structure.

## Body

## Two exact routes to closure


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

### Route A: prove the stronger geodesic theorem

The first legitimate closure route is to prove a theorem stronger than GN3.

The clean candidate is the memory-two geodesic conjecture from the second Section:

> Every finite reversal-complement coloring
> \[
> h(w,v,u)=1-h(u,v,w)
> \]
> of ordered triples of distinct labels admits a permutation whose consecutive-triple word has at most one color change.

Equivalently, every antipodally colored memory lift of this form has a one-change pole geodesic.

If this theorem is proved, then apply it to the auxiliary extension \(H^+\). The resulting directed one-change order gives a two-cover of \(H\) by Theorem 3.

Thus the reduction is precise:
\[
\boxed{
\text{memory-two geodesic conjecture}
\Longrightarrow
\text{grand GN3 two-cover conjecture}.
}
\]

A proof of the stronger theorem would therefore be a successful conclusion of the project, not an unwanted detour.

The same principle applies if the correct general theorem is formulated at another level—for example as a generalization of the strengthened Norine geodesic conjecture on a higher-memory antipodal complex. What matters is that the theorem be stated precisely and that the reduction to the exactified GN3 lift be checked explicitly.

### Route B: exploit the additional GN3 structure

The second closure route assumes that arbitrary reversal-complement memory colorings are too general.

Then the extra boundary-tournament structure becomes decisive. A failed triple has a forced reversed tight triple. Recurrent front motion therefore generates actual path structure rather than abstract bit changes.

Articles I–VI develop the resulting mechanisms:

- deletion-cover compatibility;
- quadratic-potential descent;
- defect-line compression;
- endpoint transport;
- longest-path reversal structure;
- equal-potential recurrence.

The handoff from Article VII should be viewed schematically as
\[
\boxed{
\text{topological recurrence}
\longrightarrow
\text{front motion / exact diagonal / repeated carrier}
\longrightarrow
\text{GN3 reversal structure}
\longrightarrow
\text{two-cover or strict descent}.
}
\]

This is precisely where GN3 departs from the unresolved general geodesic analogue.

### The actual remaining topological conversion

The central missing implication may now be stated without ambiguity:
\[
\boxed{
\text{balanced or recurrent extreme-switch data}
\quad\Longrightarrow?\quad
R\cap A(R)\ne\varnothing.
}
\]

There are two ways this implication could be achieved.

1. **Topologically:** show that an antipodally invariant neutral corridor is incompatible with the memory coloring itself.
2. **Combinatorially:** show that the recurrence required to support the corridor necessarily creates one of the GN3 configurations closed by Articles III–VI.

Bourgin–Yang is relevant to the first and second possibilities because multiplicity of zeros may prevent a corridor from remaining locally coherent. The giant-block and front-motion analysis is relevant because it converts multiplicity into explicit local motion.

The article does not claim that this conversion has been completed.

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

Articles I–VI develop the GN3-specific local and repartition machinery.

Article VII identifies the global obstruction as an antipodal-geodesic/topological phenomenon, gives exact Helly, geodesic, support, and reachability models of the theorem, and isolates the point at which global topology must either:

- prove a stronger general geodesic theorem; or
- hand recurrence back to the special boundary-tournament machinery.

This is the organizing principle for future work.

A successful worker need not decide in advance which route will win. If the topology naturally proves the stronger memory-geodesic conjecture, that route should be pursued and stated openly. If it fails exactly where GN3 supplies endpoint reversals or small supports, that extra structure should be exploited.

The frontier is no longer a vague analogy with the cube. It is a precise choice between two mathematically meaningful closure mechanisms.


## Metadata

- ID: article_vii_synthesis_and_exact_frontier
- Kind: section
- Version: 3
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — crystallized, version 3: Two exact routes to closure
- Subsection 2 — HOT, version 1: Further developments
