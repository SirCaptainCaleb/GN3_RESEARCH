# Frozen-window carriers and separator relabeling require precise invariants

## Metadata

- ID: frozen_window_carriers_and_separator_relabeling_require_precise_invariants
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 37
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## A protected frozen-window carrier and its exact compatibility condition

Fix a positive-word depth rule and an outward repair order \(\omega\). Let \(J\) be a positional interval containing every determining window of every witness edge of depth at most \(r\). Suppose \(\omega\) avoids the positive forbidden words internally on \(J\).

Fix one ambient source ordered-partition face \(F_*\). Let \(A_*\) consist of the active generators in those connected Coxeter components of \(F_*\) whose positions are disjoint from \(J\). For every subface \(G\subseteq F_*\), use the **inherited mask**
\[
A_G=S_G\cap A_*,
\qquad
K_J(G,\omega)=\{\omega w:w\in W_{A_G}\},
\]
including the full permutahedral face, not just its chamber vertices.

**Proposition.** Every chamber of \(K_J(G,\omega)\) is outward; each target face is contractible; and these faces are nested under inclusion of source subfaces.

**Proof.** Every retained generator fixes all positions of \(J\), so all target chambers have the same internal word there. Every at-most-depth-\(r\) determining window is inside \(J\) and absent. A parabolic orbit under adjacent generators is a product of permutahedra, hence a contractible face. For \(G\subseteq F\subseteq F_*\), we have \(S_G\subseteq S_F\), and thus \(A_G\subseteq A_F\). Therefore \(K_J(G,\omega)\subseteq K_J(F,\omega)\). \(\square\)

The inherited mask is essential. Recomputing “whole components disjoint from \(J\)” separately on each subface is not monotone: splitting a component that met \(J\) may create a new exterior component, introducing generators that the larger face collapsed. The first local draft of this addendum used that invalid recomputation; the proposition above corrects it by fixing the mask at the ambient face.

This construction excludes endpoint-crossing generators. They may be added only after proving that their whole parabolic orbit avoids every at-most-current-depth window. One-step safety does not alone prove that orbit statement. A normalized balanced cut may supply the additional protection, but the indices and both endpoint regimes must be checked.

Thus unbounded exterior factors pose no separate extension problem once a common normalization, base order, and inherited mask are fixed. Independent choices of \((J_F,\omega_F,A_F)\) on different ambient faces do not automatically agree on their intersections.

A sufficient global statement is an equivariant assignment \(F\mapsto C(F)\) on the zero-face poset satisfying
\[
C(F)\subseteq X_{r+1},\quad C(F)\ne\varnothing,\quad
C(F)\text{ contractible},\quad
G\subseteq F\Longrightarrow C(G)\subseteq C(F).
\]
These hypotheses give the continuous equivariant carrier extension. Homological acyclicity alone is not a continuous-map extension theorem without a separate chain-level/index argument.

Retaining the separator as the next free space and relabeling its vertices by outward chambers preserves the space's index, but requires a new invariant: every complementary event must localize to a protected source Coxeter edge, or another object with a proved surgery theorem. Arbitrary outward relabeling does not inherit the uniform-role property used by the earlier Ky Fan hole-sweeping proof. Those role labels are inherited under face inclusion; that property has not been proved for the proposed replacement labels.

The three directions consequently have distinct obligations. Compression must fix the polarity mismatch and treat positive reflected-double carriers. Frozen parabolic carriers need shared normalizations and inherited masks compatible across ambient-face intersections. Separator relabeling needs edge localization for its new labels. Local square/hexagon path independence alone supplies none of these missing invariants.

## Frontier

- Development version when composed: None
- Development version now: 2
