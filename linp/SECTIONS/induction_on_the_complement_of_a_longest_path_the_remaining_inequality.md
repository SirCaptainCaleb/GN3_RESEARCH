# The remaining inequality

## Composition

The induction closes if the following statement is proved.

## Open problem

For every longest \(k\)-edge path \(P\) in a \(P_\ell^{(3)}\)-free linear \(3\)-graph \(H\), with
\[
X=V(P),\qquad Y=V(H)\setminus X,
\]
prove
\[
3e_X\le \binom{|X|}{2}+(\ell-k)|X|+D_Y, \tag{13}
\]
where
\[
D_Y=\ell |Y|-3|E(H[Y])|.
\]

The first term in (13) is exhausted by distinct pairs of vertices of \(X\). The second term is smaller when the longest path is close to length \(\ell\), so the case \(k=\ell-1\) is the most restrictive. The third term must account for the edge families that cannot be represented by distinct pairs of \(X\).

A sufficient statement would be the following: whenever the edges meeting \(X\) require \(r\) more units than can be represented by the first two terms of (13), prove
\[
D_Y\ge r. \tag{14}
\]
Lemmas 2–5 describe mechanisms by which missing edges in \(H[Y]\) can arise, but they do not yet prove (14).

## Metadata

- ID: induction_on_the_complement_of_a_longest_path_the_remaining_inequality
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/induction_on_the_complement_of_a_longest_path_the_remaining_inequality_subsection_a.md) (`induction_on_the_complement_of_a_longest_path_the_remaining_inequality_subsection_a`; development v1; composition v1; stale=False)
- [Subsection 2 — Open problem](../SUBSECTIONS/induction_on_the_complement_of_a_longest_path_the_remaining_inequality_subsection_b.md) (`induction_on_the_complement_of_a_longest_path_the_remaining_inequality_subsection_b`; development v1; composition vNone; stale=False)
