# Mutual terminal-pair four-cycles force four overlapping Hamiltonian four-supports — preserved pre-item development

## Development

## A mutual terminal-pair four-cycle forces four overlapping Hamiltonian four-supports

Let
\[
B=\{a,b,c,d\}
\]
and let \(z\notin B\). Suppose the mutual terminal-pair graph before \(z\) contains the cycle
\[
a-b-c-d-a,
\]
that is,
\[
h(u,v,z)=h(v,u,z)=1
\]
for every cycle edge \(uv\in\{ab,bc,cd,da\}\).

Put
\[
Y=B\cup\{z\}.
\]

Then every four-subset of \(Y\) containing \(z\) and three vertices of \(B\) is Hamiltonian.

Indeed:

- On \(\{a,b,d,z\}\), the triples
  \[
  h(a,b,z)=h(a,d,z)=1
  \]
  exhibit \(b,d\) as two parallel middle vertices between the fixed endpoints \(a,z\). By the two-parallel-middle lemma, \(\{a,b,d,z\}\) has a Hamilton tight path.

- On \(\{b,c,d,z\}\), use
  \[
  h(c,b,z)=h(c,d,z)=1.
  \]

- On \(\{a,b,c,z\}\), use
  \[
  h(b,a,z)=h(b,c,z)=1.
  \]

- On \(\{a,c,d,z\}\), use
  \[
  h(d,a,z)=h(d,c,z)=1.
  \]

Thus
\[
\boxed{
Y-\{a\},\quad Y-\{b\},\quad Y-\{c\},\quad Y-\{d\}
\text{ are all Hamiltonian.}
}
\]

This strengthens [[a_mutual_terminal_pair_four_cycle_forces_a_hamiltonian_five_support]]: the forced Hamiltonian five-packet carries four overlapping Hamiltonian four-supports, all rooted through the fixed following label \(z\).

### Complement consequence

Let
\[
R=H-Y.
\]
For \(w\in B\),
\[
H-(Y-\{w\})=R\cup\{w\}.
\]

Therefore, if for some \(w\in B\)
\[
\operatorname{pc}(R\cup\{w\})\le2,
\]
then the Hamiltonian four-support \(Y-\{w\}\) has two-coverable complement and enters [[maximal_support_normalization_applies_directly_to_article_vii_bounded_outputs]].

Consequently, a terminal-pair \(C_4\) that survives both the spanning-two-cover branch and maximal-support entry must satisfy the stronger rigidity condition
\[
\boxed{
\operatorname{pc}(R\cup\{w\})\ge3
\qquad\text{for every }w\in B.
}
\]

Together with [[surviving_terminal_pair_four_cycles_have_complement_path_cover_at_least_three]], the genuinely new carrier-loop branch therefore has
\[
\operatorname{pc}(R)\ge3
\]
and remains path-cover-\(\ge3\) even after adjoining any one of the four cycle labels.

This converts the surviving loop from a purely topological obstruction into a fourfold one-vertex nonaugmentation state for the complement.
