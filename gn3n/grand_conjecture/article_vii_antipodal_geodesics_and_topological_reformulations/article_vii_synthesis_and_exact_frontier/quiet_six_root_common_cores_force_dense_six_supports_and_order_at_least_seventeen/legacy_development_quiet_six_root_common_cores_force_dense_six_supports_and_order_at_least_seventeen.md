# Quiet six-root common cores force dense six-supports and order at least seventeen — preserved pre-item development

## Development

## A quiet six-root common core forces dense Hamiltonian six-supports and complement order at least twelve

Retain the robust common-core state of [[surviving_terminal_pair_four_cycles_force_a_six_root_robust_common_core]]:

- \(Y=B\cup\{z\}\) is the five-packet forced by a mutual terminal-pair \(C_4\);
- \(R=H-Y\);
- \(C=Y-\{b_*\}\) is a Hamiltonian four-core;
- \(E\subseteq R\), \(|E|\ge6\);
- \(C\cup\{y\}\) is Hamiltonian for every \(y\in E\).

Define a graph \(\Gamma\) on \(E\) by
\[
xy\in E(\Gamma)
\quad\Longleftrightarrow\quad
C\cup\{x,y\}\text{ is Hamiltonian}.
\]

Take any three distinct roots \(x,y,w\in E\). Apply the three-extension common-core calculus to the Hamiltonian five-sets
\[
C+x,\qquad C+y,\qquad C+w.
\]

Unless a bounded order-theoretic disturbance already occurs—order disagreement, a positioned reversing triple, or a Hamiltonian four-support—the calculus produces a Hamiltonian six-support \(C+\{u,v\}\) for some pair among the three roots.

By [[bounded_order_disagreement_reduces_to_reversal_or_hamiltonian_support]], order disagreement may itself be compressed to a positioned reversal or bounded Hamiltonian support. Therefore, after excluding bounded disturbance outputs, every three-set in \(E\) contains an edge of \(\Gamma\). Equivalently,
\[
\alpha(\Gamma)\le2.
\]

Thus the complement of \(\Gamma\) is triangle-free. Mantel's theorem gives
\[
|E(\Gamma)|
\ge
\binom{|E|}{2}
-
\left\lfloor\frac{|E|^2}{4}\right\rfloor.
\]
For \(|E|\ge6\), this is at least six.

Hence a quiet robust common-core state contains at least six Hamiltonian supports of order six,
\[
C\cup\{x,y\}.
\]

For such an edge \(xy\),
\[
H-(C\cup\{x,y\})
=
(R-\{x,y\})\cup\{b_*\}.
\]

If this complement had path-cover number at most two, the Hamiltonian six-support would enter the maximal-support normalization. Therefore a carrier loop surviving both bounded disturbance and maximal-support entry must satisfy
\[
\operatorname{pc}\bigl((R-\{x,y\})\cup\{b_*\}\bigr)\ge3
\]
for every edge \(xy\in E(\Gamma)\).

Each such complement has order
\[
|R|-1.
\]
By [[ten_vertex_boundary_tournaments_have_two_cover]], path-cover number at least three forces
\[
|R|-1\ge11.
\]
Therefore
\[
\boxed{|R|\ge12.}
\]

### Dichotomy

A surviving mutual terminal-pair four-cycle therefore has one of two outputs:

1. a bounded Hamiltonian/reversal disturbance on a common four-core with exterior roots; or
2. a quiet common-core state with a dense family of Hamiltonian six-supports, each having path-cover-\(\ge3\) complement, and necessarily
   \[
   |H|\ge |Y|+|R|\ge5+12=17.
   \]

This is again independent of cyclic rotation, path reversal, and minimum-counterexample arguments.
