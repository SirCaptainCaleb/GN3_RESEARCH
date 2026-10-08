# Quiet six-root states grow to seven-supports or are exactly order seventeen — preserved pre-item development

## The quiet six-root state either grows to a seven-support or is the exact order-seventeen two-triangle case

Retain the quiet common-core state of [[quiet_six_root_common_cores_force_dense_six_supports_and_order_at_least_seventeen]]:

- \(Y=B\cup\{z\}\);
- \(R=H-Y\);
- \(C=Y-\{b_*\}\) is a Hamiltonian four-core;
- \(E\subseteq R\), \(|E|\ge6\);
- \(C+y\) is Hamiltonian for every \(y\in E\);
- the graph \(\Gamma\) on \(E\) has
  \[
  xy\in E(\Gamma)\iff C+\{x,y\}\text{ is Hamiltonian},
  \]
  and, after excluding bounded disturbance outputs,
  \[
  \alpha(\Gamma)\le2.
  \]

Assume also that no Hamiltonian support produced below has two-coverable complement; otherwise the state enters maximal-support normalization.

### Degree at least three forces a Hamiltonian seven-support

Suppose some \(x\in E\) has three distinct neighbors \(y_1,y_2,y_3\) in \(\Gamma\). Put
\[
A=C\cup\{x\}.
\]
Then \(A\) is Hamiltonian, and each
\[
A\cup\{y_i\}=C\cup\{x,y_i\}
\]
is Hamiltonian by definition of \(\Gamma\).

Apply [[three_compatible_one_vertex_extensions_have_a_common_endpoint_normal_form]] to the common core \(A\) and roots \(y_1,y_2,y_3\).

Its order-disagreement, positioned-reversal, and Hamiltonian-four-support outputs are already bounded disturbances. If the three roots all occupy one common endpoint gap, the corresponding end edge of a Hamilton order on \(A\) has three common hooks; the ordered-anchor three-hook theorem again produces a bounded Hamiltonian four- or five-support. Hence in the quiet branch the only remaining output is a Hamiltonian support
\[
A\cup\{y_i,y_j\}
=
C\cup\{x,y_i,y_j\}
\]
of order seven.

Its complement is
\[
(R-\{x,y_i,y_j\})\cup\{b_*\},
\]
of order
\[
|R|-2.
\]
By the standing quiet assumption this complement still has path-cover number at least three. The ten-vertex two-cover theorem therefore gives
\[
|R|-2\ge11,
\]
so
\[
\boxed{|R|\ge13.}
\]

### If no degree-three vertex exists, the state is exactly \(K_3\sqcup K_3\)

Assume instead
\[
\Delta(\Gamma)\le2.
\]
A graph of maximum degree at most two is a disjoint union of paths and cycles. Since
\[
\alpha(\Gamma)\le2
\]
and \(|E|\ge6\), \(\Gamma\) cannot be connected: every path or cycle on at least six vertices has independence number at least three.

It also cannot have three components, since choosing one vertex from each gives an independent three-set. Thus it has exactly two components. Each component must have independence number one, hence must be a clique; with maximum degree at most two, each has order at most three. Since the total order is at least six,
\[
\boxed{|E|=6,\qquad \Gamma=K_3\sqcup K_3.}
\]

But [[surviving_terminal_pair_four_cycles_force_a_six_root_robust_common_core]] gives
\[
|E|\ge\left\lceil\frac{|R|}{2}\right\rceil,
\]
so \(|E|=6\) implies
\[
|R|\le12.
\]
The preceding six-support theorem already gives \(|R|\ge12\). Therefore
\[
\boxed{|R|=12,\qquad |H|=17.}
\]

### Dichotomy

A quiet surviving carrier loop therefore has one of two sharply separated forms:

1. **Growth:** it contains a Hamiltonian seven-support whose complement still has path-cover number at least three, and necessarily \(|R|\ge13\); or
2. **Exact bounded exception:**
   \[
   |H|=17,\qquad |R|=12,\qquad |E|=6,\qquad \Gamma=K_3\sqcup K_3.
   \]

Thus order seventeen is the unique no-degree-three obstruction to the next common-core growth step. This gives an explicit finite target for the nongrowing branch without using cyclic rotation, path reversal, or unrestricted minimum-order reasoning.
