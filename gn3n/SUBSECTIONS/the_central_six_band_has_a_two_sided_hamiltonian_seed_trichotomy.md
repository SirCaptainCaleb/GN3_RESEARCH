# The central six band has a two-sided Hamiltonian seed trichotomy

## Metadata

- ID: the_central_six_band_has_a_two_sided_hamiltonian_seed_trichotomy
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 145
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## The central six witness band has a two-sided Hamiltonian seed trichotomy

Let
\[
B=\{a,b,x,y,c,d\}
\]
be the central six-label band of a genuine minimum deletion pair, where
\[
(\ldots,a,b)=P,\qquad (\ldots,d,c)=Q
\]
are the corridor-facing ends of the complementary two-cover and \(x,y\) are the two holes.

Put
\[
K=\{b,c,x,y\},
\qquad
U_L=K\cup\{a\},
\qquad
U_R=K\cup\{d\}.
\]

Then at least one of the following holds.

1. **Middle-four seed.**
   \(K\) is Hamiltonian.

2. **Anchored five-seed.**
   At least one of \(U_L,U_R\) is Hamiltonian.

3. **Two-sided four-seed.**
   Both
   \[
   L=\{a,b,x,y\}
   \qquad\text{and}\qquad
   R=\{c,d,x,y\}
   \]
   are Hamiltonian.

Indeed, assume neither (1) nor (2). Then \(K,U_L,U_R\) are all non-Hamiltonian. Since a non-Hamiltonian five-set has at most one non-Hamiltonian four-subset by Section 7 of [[smallset01]], and \(K\) is already a non-Hamiltonian four-subset of \(U_L\), every other four-subset of \(U_L\) is Hamiltonian. In particular
\[
U_L-\{c\}=L
\]
is Hamiltonian. Applying the same argument to \(U_R\) gives
\[
U_R-\{b\}=R
\]
Hamiltonian.

Each output has a two-coverable complement in the full genuine two-deletion state:
- for \(K\), the complement is the two one-sided truncations of \(P,Q\);
- for \(U_L\) or \(U_R\), the complement is obtained by truncating one corridor side by two vertices and the other by one;
- for \(L\), the complement is \(P-\{a,b\}\mid Q\), and for \(R\) it is \(P\mid Q-\{c,d\}\).

Thus the two-sided branch supplies **two different Hamiltonian four-supports with two-coverable complements, sharing exactly the minimum pair \(\{x,y\}\)** and rooted at opposite corridor ends.

This is stronger than the existence statement in [[the_maximal_support_seed_lies_in_the_central_six_witness_band]]. The only case in which no middle or anchored-five seed exists automatically produces symmetric left/right four-supports. Hence the central-six bridge can be attacked through one of three concrete support geometries rather than an arbitrary bounded Hamiltonian subset.

## Frontier

- Development version when composed: None
- Development version now: 1
