# Lemma 2 — preserved pre-item development

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
