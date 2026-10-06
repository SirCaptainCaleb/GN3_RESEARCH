# Proposition 3

## Metadata

- ID: terminal_pair_cycles_and_rotations_cycle_rank_as_a_sufficient_parameter_subsection_a
- Parent Section: terminal_pair_cycles_and_rotations_cycle_rank_as_a_sufficient_parameter
- Position: 1
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Suppose
\[
\beta(T)\le Cs+Dn \tag{3}
\]
for constants \(C,D\ge0\). Then
\[
m\le
\frac{(C+1)(2\ell-3)+D+1}{2C+3}\,n. \tag{4}
\]

#### Proof
Let \(b=m-s\) be the number of nonspecial edges. Since \(T\) is simple and \(|E(T)|=b\),
\[
b=|V(T)|-\kappa(T)+\beta(T)\le n+\beta(T).
\]
Using (3),
\[
b\le Cs+(D+1)n.
\]
Hence
\[
m=b+s\le (C+1)s+(D+1)n,
\]
so
\[
s\ge \frac{m-(D+1)n}{C+1}.
\]
Substitute this in (2) and rearrange. ∎

In particular, \(\beta(T)=O(n)\) gives the two-thirds leading coefficient. The central question is therefore whether the independent cycles of \(T\) force enough new path structure to bound \(\beta(T)\).

## Frontier

- Development version when composed: None
- Development version now: 1
