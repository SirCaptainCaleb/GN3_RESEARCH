# Mobile exterior-coordinate cycle criterion and no-go for verbatim six-path lifting

## Development

Let \(S\) be the directions of a collection of based paths, each equipped with specified consecutive ordered-three-face windows. A comparison edge \(e=(r,\alpha;s,\beta)\) identifies a window of row \(r\) with one of row \(s\), either as the same ordered face (\(\epsilon_e=0\)) or as antipodal reversals (\(\epsilon_e=1\)). Suppose the comparison already holds on the \(S\)-coordinates.

**Mobile exterior-coordinate criterion.** Add one direction \(g\notin S\). In row \(r\), insert \(g\) at a cut leaving every compared three-direction window consecutive. Write \(t_{r,e}\in\mathbb F_2\) for whether \(g\) precedes the window incident with \(e\), and \(z_r\in\mathbb F_2\) for the initial \(g\)-bit of row \(r\). All comparison edges hold also at coordinate \(g\) if and only if
\[
 z_r\oplus z_s=\epsilon_e\oplus t_{r,e}\oplus t_{s,e}
 \qquad\text{for every comparison edge }e.
\]
Equivalently, on every cycle of the comparison multigraph, the XOR of its edge demands \(\epsilon_e\oplus t_{r,e}\oplus t_{s,e}\) vanishes. On each connected component a solution, when it exists, is unique up to simultaneously complementing all \(z_r\).

*Proof.* At the selected window, the fixed exterior \(g\)-bit is exactly \(z_r\oplus t_{r,e}\). Equality of two faces requires equality of these bits; antipodal reversal requires complementarity. This gives the displayed linear equations. Choose one initial bit per connected component and propagate along a spanning tree. The assignments satisfy all remaining edges precisely when every cycle has zero XOR demand. \(\square\)

**Specific six-path obstruction after insertion.** In the six-path forcing table of the dimension-six theorem, consider the three antipodal comparisons: row 1's second window with row 2's first, row 1's second with row 4's first, and row 2's last with row 4's last. Their three edge signs are 1. The cycle criterion becomes
\[
(t_{2,\mathrm{first}}\oplus t_{2,\mathrm{last}})
\oplus(t_{4,\mathrm{first}}\oplus t_{4,\mathrm{last}})=1.
\]
Suppose the original forcing proof must be preserved verbatim: row 2 needs its first, second, and last windows; row 4 needs its first, third, and last windows. For either row, the only cuts in a six-direction order preserving all three indicated triples are before the first move or after the sixth. In particular both parenthesized differences are zero, contradicting the cycle equation.

If one preserves only the endpoint comparison windows, then row 2 can remain an unchanged six-block and the holonomy can be repaired by inserting \(g\) centrally into row 4, between its third and fourth moves. This preserves row 4's first and last windows while toggling \(g\) between them. But row 4's original third window \(bfe\), which the forcing argument compares to row 6, is then destroyed: the augmented order is \(dcbgfea\). Thus mobile holonomy is algebraically repairable, while the existing six-path proof does not lift unchanged. Any dimension-raising forcing certificate must include genuinely new windows involving \(g\), or a revised comparison pattern.

The theorem concerns face-identification compatibility only; the color-word consequences of every full augmented path being bad require a separate proof.
