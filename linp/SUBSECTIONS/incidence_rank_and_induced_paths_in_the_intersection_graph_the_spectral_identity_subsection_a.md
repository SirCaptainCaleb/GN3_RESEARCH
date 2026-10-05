# Lemma 3

## Metadata

- ID: incidence_rank_and_induced_paths_in_the_intersection_graph_the_spectral_identity_subsection_a
- Parent Section: incidence_rank_and_induced_paths_in_the_intersection_graph_the_spectral_identity
- Position: 1
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: True

## Cold composition

(none yet)

## Development

\[
N^{T}N=3I_m+A(F). \tag{4}
\]
Consequently
\[
\operatorname{rank}N
=
m-\operatorname{mult}_F(-3), \tag{5}
\]
where \(\operatorname{mult}_F(-3)\) is the multiplicity of the adjacency eigenvalue \(-3\).

#### Proof
The \((e,f)\)-entry of \(N^TN\) is \(|e\cap f|\). It is \(3\) when \(e=f\), \(1\) when \(e\ne f\) and the two hyperedges intersect, and \(0\) otherwise. This proves (4).

Over \(\mathbb R\),
\[
\ker(N^TN)=\ker N.
\]
Thus \(N\) and \(N^TN\) have the same rank. Since \(3I+A(F)\) is symmetric, its nullity equals the multiplicity of \(-3\) as an eigenvalue of \(A(F)\), proving (5). ∎

Therefore the one-third problem is equivalently a bound on the \(-3\) eigenspace inside the realizable class of Lemma 2.
