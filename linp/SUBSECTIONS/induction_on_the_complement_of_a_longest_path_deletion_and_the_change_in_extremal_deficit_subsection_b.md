# Lemma 2

## Metadata

- ID: induction_on_the_complement_of_a_longest_path_deletion_and_the_change_in_extremal_deficit_subsection_b
- Parent Section: induction_on_the_complement_of_a_longest_path_deletion_and_the_change_in_extremal_deficit
- Position: 2
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Let \(S\subseteq V(H)\), and let \(N_H(S)\) be the set of hyperedges meeting \(S\). Then
\[
r_d(H-S)
=
r_d(H)+|N_H(S)|-d|S|. \tag{8}
\]

#### Proof
Since
\[
|E(H-S)|=|E(H)|-|N_H(S)|,
\]
we have
\[
\begin{aligned}
r_d(H-S)
&=d(|V(H)|-|S|)-(|E(H)|-|N_H(S)|)\\
&=r_d(H)+|N_H(S)|-d|S|.
\end{aligned}
\]
∎

The identity is elementary, but it prevents a common error: deleting a vertex or a small set while preserving density does not by itself contradict minimality.

## Development

Let \(S\subseteq V(H)\), and let \(N_H(S)\) be the set of hyperedges meeting \(S\). Then
\[
r_d(H-S)
=
r_d(H)+|N_H(S)|-d|S|. \tag{8}
\]

#### Proof
Since
\[
|E(H-S)|=|E(H)|-|N_H(S)|,
\]
we have
\[
\begin{aligned}
r_d(H-S)
&=d(|V(H)|-|S|)-(|E(H)|-|N_H(S)|)\\
&=r_d(H)+|N_H(S)|-d|S|.
\end{aligned}
\]
∎

The identity is elementary, but it prevents a common error: deleting a vertex or a small set while preserving density does not by itself contradict minimality.
