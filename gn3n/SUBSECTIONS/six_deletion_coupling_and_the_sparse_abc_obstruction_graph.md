# Six-deletion coupling and the sparse abc-obstruction graph

## Metadata

- ID: six_deletion_coupling_and_the_sparse_abc_obstruction_graph
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 22
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Six-deletion coupling in the maximal braid

Work in the residual order-eleven configuration
\[
V=T\sqcup\{a,b,c\},\qquad |T|=8.
\]
For each triple \(C\in\binom{T}{3}\), let
\[
k(C)=\#\{P\in\{ab,ac,bc\}: C\cup P\text{ is non-Hamiltonian}\}.
\]
Define a graph \(R\) on \(T\) by
\[
xy\in E(R)\iff \{x,y,a,b,c\}\text{ is non-Hamiltonian}.
\]

**Lemma (six-deletion coupling).** For every \(C\in\binom{T}{3}\),
\[
k(C)+e_R(C)\le 2.
\]

**Proof.** Apply the four-of-six theorem to the six-set \(U=C\cup\{a,b,c\}\). Its six five-vertex deletions are exactly the three braid targets \(C+ab,C+ac,C+bc\) and the three sets \((C-\{x\})+abc\), \(x\in C\), which are non-Hamiltonian exactly for the three edges of \(R[C]\). At most two of the six deletions are non-Hamiltonian. ∎

Let
\[
\mathcal F_0=\{C\in\binom{T}{3}:T\setminus C\text{ is non-Hamiltonian}\}.
\]
If the common-core braid lemma fails, every \(C\notin\mathcal F_0\) has \(k(C)\ge1\).

The family \(\mathcal F_0\) has pair-codegree at most two: fixing \(Q\in\binom{T}{2}\), the triples of \(\mathcal F_0\) containing \(Q\) correspond to non-Hamiltonian five-deletions of the six-set \(T\setminus Q\).

Hence under failure of the common-core lemma:
1. \(R\) is triangle-free.
2. Every triple spanning two edges of \(R\) lies in \(\mathcal F_0\).
3. Every edge \(uv\in E(R)\) satisfies \(d_R(u)+d_R(v)\le4\).

Indeed, for an edge \(uv\), triangle-freeness makes the triples \(\{u,v,w\}\) with \(w\in(N(u)-v)\cup(N(v)-u)\) distinct two-edge triples, hence all lie in \(\mathcal F_0\). Pair-codegree at most two gives \((d(u)-1)+(d(v)-1)\le2\).

Thus every component of \(R\) is a path, a cycle of length at least four, or a star \(K_{1,3}\), and \(|E(R)|\le8\).

This is an audit-safe auxiliary reduction independent of the external-gauge shortcut. The endpoint-exclusion proof now closes the maximal braid more directly, but this lemma remains a fallback structural reduction for any future re-audit of that step.
