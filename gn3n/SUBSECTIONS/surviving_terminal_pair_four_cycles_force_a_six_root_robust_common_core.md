# Surviving terminal-pair four-cycles force a six-root robust common core

## Metadata

- ID: surviving_terminal_pair_four_cycles_force_a_six_root_robust_common_core
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 91
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## A surviving terminal-pair four-cycle forces a six-root robust common four-core

Let
\[
B=\{a,b,c,d\},\qquad Y=B\cup\{z\},
\]
and suppose the mutual terminal-pair graph before \(z\) contains the cycle
\[
a-b-c-d-a.
\]
Let
\[
R=H-Y.
\]

Assume the carrier loop survives the previously closed branches, so in particular
\[
\operatorname{pc}(R)\ge3
\]
by [[surviving_terminal_pair_four_cycles_have_complement_path_cover_at_least_three]].

By [[ten_vertex_boundary_tournaments_have_two_cover]], every boundary tournament on at most ten vertices has path-cover number at most two. Hence
\[
\boxed{|R|\ge11.}
\]

For each exterior label \(y\in R\), consider the six-set
\[
U_y=Y\cup\{y\}.
\]
The deletion \(U_y-\{y\}=Y\) is Hamiltonian. By four-of-six, at least four one-vertex deletions of \(U_y\) are Hamiltonian. Among the remaining five deletion labels, at most one is \(z\). Therefore at least two labels \(b\in B\) satisfy
\[
(Y-\{b\})\cup\{y\}
\quad\text{Hamiltonian.}
\]

Define
\[
I_y=\{b\in B:(Y-\{b\})\cup\{y\}\text{ is Hamiltonian}\}.
\]
Then
\[
|I_y|\ge2
\qquad(y\in R).
\]

Count incidences
\[
\{(b,y):b\in I_y\}.
\]
There are at least \(2|R|\) incidences across four labels \(b\in B\). Hence some
\[
b_*\in B
\]
satisfies
\[
|\{y\in R:b_*\in I_y\}|
\ge
\left\lceil\frac{|R|}{2}\right\rceil
\ge6.
\]

Put
\[
C=Y-\{b_*\}.
\]
By [[mutual_terminal_pair_four_cycles_force_four_overlapping_hamiltonian_four_supports]], \(C\) is Hamiltonian. Thus there is a set
\[
E\subseteq R,\qquad |E|\ge6,
\]
such that
\[
C\cup\{y\}
\]
is Hamiltonian for every \(y\in E\).

### Robust survivor consequence

For \(y\in E\),
\[
H-(C\cup\{y\})
=
(R-\{y\})\cup\{b_*\}.
\]

If for some \(y\in E\)
\[
\operatorname{pc}\bigl((R-\{y\})\cup\{b_*\}\bigr)\le2,
\]
then the Hamiltonian five-support \(C\cup\{y\}\) has two-coverable complement and enters [[maximal_support_normalization_applies_directly_to_article_vii_bounded_outputs]].

Therefore a carrier loop that survives both the global two-cover branch and maximal-support entry must satisfy
\[
\boxed{
\operatorname{pc}\bigl((R-\{y\})\cup\{b_*\}\bigr)\ge3
\qquad(y\in E),
}
\]
for at least six distinct exterior labels \(y\).

Hence the genuinely new topological residue is not merely a Hamiltonian five-packet with path-cover-\(\ge3\) complement. It contains a Hamiltonian four-core \(C\) with at least six exterior Hamiltonian extensions, all of whose complementary graphs remain path-cover-\(\ge3\).

This is an audit-safe replacement for the withdrawn second-layer propagation route: it uses only four-of-six, the proved four overlapping cycle deletions, and the ten-vertex two-cover theorem. No cyclic rotation, path reversal, or minimum-counterexample argument occurs.

## Frontier

- Development version when composed: None
- Development version now: 1
