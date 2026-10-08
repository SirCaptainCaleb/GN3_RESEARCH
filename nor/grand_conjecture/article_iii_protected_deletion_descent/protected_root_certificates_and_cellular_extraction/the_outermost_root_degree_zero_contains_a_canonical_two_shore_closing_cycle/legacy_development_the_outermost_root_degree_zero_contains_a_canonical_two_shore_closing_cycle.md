# The outermost-root degree zero contains a canonical two-shore closing cycle — preserved pre-item development

## Development

## The outermost-root degree zero contains a canonical two-shore closing cycle

Use the root-valued boundary carrier
\[
D(\pi)=e_{v_p}-e_{v_{q+3}}
\]
from §243, where \(p<q\) are the first and last change positions of a bad ternary order.

Fix an arbitrary bad full order \(\pi_0\) and use
\[
r_0=D(\pi_0)=e_s-e_t
\]
as the top-face/apex label. Cone the zero-free nonzero-degree proper-face carrier to this apex. A zero occurs in some cone simplex:
\[
\lambda_0 r_0+\sum_{i=1}^k\lambda_i r_i=0,
\qquad \lambda_i>0,
\]
where the boundary labels \(r_i=D(\pi_{F_i})\) come from a nested proper-face flag
\[
F_1<\cdots<F_k=G.
\]

Write
\[
r_G=e_a-e_b
\]
for the label of the largest face \(G\).

### Largest-face orientation

Let \(\beta_G\) be a block-rank functional for \(G\), increasing strictly from left to right across its ordered blocks.

Every boundary witness \(\pi_{F_i}\) refines \(G\). Hence its outermost root is weakly forward:
\[
\langle\beta_G,r_i\rangle\le 0.
\]
The largest-face root strictly crosses \(G\)-blocks, so
\[
\langle\beta_G,r_G\rangle<0.
\]

Pairing the zero relation with \(\beta_G\) gives
\[
\langle\beta_G,r_0\rangle>0.
\]
Thus the apex root is strictly backward across \(G\).

### Cycle decomposition

Interpret a root \(e_x-e_y\) as the directed edge \(x\to y\). A positive type-A dependence is a positive circulation, hence decomposes into directed simple cycles.

Every boundary edge is weakly forward in the \(G\)-block order. Therefore no directed cycle consisting only of boundary edges can contain a strictly forward edge: block rank could never decrease enough to close the cycle.

Since \(r_G\) is strictly forward, every cycle component carrying positive mass from \(r_G\) must also contain the unique backward source available in the cone support, namely the apex edge \(r_0\). Consequently there is a directed simple cycle
\[
s\to t=x_0\to x_1\to\cdots\to x_m=s
\]
whose first edge is \(r_0=s\to t\), whose remaining edges are boundary outermost roots, and which contains \(r_G\).

Equivalently, after deleting the apex edge, there is a directed boundary closing path
\[
t=x_0\to x_1\to\cdots\to x_m=s
\]
from the target of \(r_0\) back to its source, containing \(r_G\).

### Two-shore localization

Choose any boundary between two consecutive \(G\)-blocks that is crossed by \(r_G\), and coarsen \(G\) to the facet
\[
H=L|R
\]
at that boundary.

Every boundary root on the closing path is weakly forward across \(H\). The apex root is backward. Hence the boundary path crosses from \(L\) to \(R\) exactly once. That unique transverse edge can be taken to be \(r_G\) after choosing a boundary crossed by \(r_G\) and, if necessary, the first such boundary along its block span.

Thus the forced degree zero yields:

1. one backward apex outermost root \(r_0=s\to t\);
2. one forward transverse outermost root \(r_G=a\to b\);
3. a directed root path inside \(L\) from \(t\) to \(a\);
4. a directed root path inside \(R\) from \(b\) to \(s\).

Every edge is witnessed by an actual full coordinate order; every boundary witness comes from the canonical proper-subinstance selector.

### Consequence

The root-valued carrier has the same two-shore extraction architecture as the one-band carrier of §156, with a simpler algebraic support: the forced object is already a directed cycle of single physical roots. No macro-root expansion or Abel summation is required.

The remaining closure task is purely realizational: splice the witnessed outermost-root path across the unique block-good transverse witness, or use the first failed splice to obtain a spanning NOR-good order or a strict protected improvement.
