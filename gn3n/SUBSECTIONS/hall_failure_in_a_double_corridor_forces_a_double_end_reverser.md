# Hall failure in a double corridor forces a double-end reverser

## Metadata

- ID: hall_failure_in_a_double_corridor_forces_a_double_end_reverser
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 60
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Hall dichotomy for the reflected span-two double corridor

Retain the exact corridor form of [[complete_positive_span_two_double_corridor_classification]]. Thus the protected determining span consists of two disjoint tight paths
\[
P=(p_1,\ldots,p_s),\qquad Q=(q_1,\ldots,q_t),
\]
with \(s,t\ge2\), and two exterior vertices \(x,y\), with the forced initial-edge reversals
\[
(p_2,p_1,x)\text{ tight},\qquad
(q_2,q_1,y)\text{ tight}.
\]

Define the terminal-attachment graph \(G\) with bipartition
\[
\{P,Q\}\sqcup\{x,y\},
\]
where
\[
Pe\in E(G)\iff (p_{s-1},p_s,e)\text{ is tight},
\]
and
\[
Qe\in E(G)\iff (q_{t-1},q_t,e)\text{ is tight}.
\]

By [[terminal_attachment_matching_gives_an_outward_repair_of_a_double_corridor]], a perfect matching in \(G\) yields an explicit spanning two-cover of the full determining span and therefore a positive-word outward repair.

The failure case has a sharper exact form.

**Lemma (Hall failure forces a doubly reversing endpoint).**
If \(G\) has no perfect matching, then at least one of the following holds:
\[
\begin{aligned}
&(p_2,p_1,x)\text{ and }(x,p_s,p_{s-1})\text{ are tight},\\
&(q_2,q_1,y)\text{ and }(y,q_t,q_{t-1})\text{ are tight}.
\end{aligned}
\]
Equivalently, one of the two distinguished exterior vertices reverses both displayed end edges of its associated corridor path.

**Proof.**
For a bipartite graph with two vertices on each side, failure of a perfect matching has one of two Hall forms.

First, some left vertex has degree zero. If \(P\) has degree zero, then
\[
(p_{s-1},p_s,x),\ (p_{s-1},p_s,y)
\]
are both non-tight. Boundary antisymmetry gives
\[
(x,p_s,p_{s-1}),\ (y,p_s,p_{s-1})
\]
tight. In particular \(x\) reverses the terminal edge of \(P\), while \((p_2,p_1,x)\) already reverses its initial edge. If \(Q\) has degree zero, the symmetric conclusion holds for \(y\).

Second, both left vertices have positive degree but
\[
|N(\{P,Q\})|=1.
\]
If the common neighborhood is \(\{x\}\), then \(y\) is adjacent to neither \(P\) nor \(Q\). Hence \((y,q_t,q_{t-1})\) is tight, and together with the forced \((q_2,q_1,y)\) this makes \(y\) a double-end reverser of \(Q\). If the common neighborhood is \(\{y\}\), the same argument makes \(x\) a double-end reverser of \(P\). ∎

Therefore the unbounded positive terminal branch has the exact dichotomy
\[
\boxed{
\text{reflected span-two double}
\Longrightarrow
\begin{cases}
\text{explicit outward two-cover repair},\\
\text{or a tight path with one exterior vertex reversing both end edges.}
\end{cases}}
\]

This is substantially narrower than the original two-path/two-endpoint interface. It identifies the remaining obstruction with the familiar double-end reversal geometry that also appears in longest-path and endpoint-transport arguments, but the present reduction uses no minimum-counterexample hypothesis.

No universal absorption theorem is asserted for the second branch. In particular, existing longest-path examples show that a vertex reversing both end edges of a path is genuine structure rather than an automatic Hamiltonian extension. The next repair must exploit the presence of the *second* corridor path and second exterior vertex, or use the protected-face variation, rather than attempting to absorb the doubly reversing vertex into its path in isolation.
