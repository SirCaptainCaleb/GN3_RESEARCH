# Random Hamiltonian absorption via transversal matroids

# Random Hamiltonian absorption via transversal matroids

Let \(b_0\) be an arbitrary reversal-odd coloring of distinct ordered triples from an \(n\)-element vertex set \(V\). Independently for each reversal pair of triples, flip both colors with probability \(\rho\in(0,1/2]\), producing \(b\).

**Theorem 1 (noise-forced Hamiltonian tight paths).** If
\[
\boxed{\rho_n^3 n/\log n\to\infty,}\tag{1}
\]
then uniformly in \(b_0\), with probability \(1-o(1)\) **every** prescribed initial ordered pair \((u,v)\) and prescribed color \(\epsilon\in\{0,1\}\) extend to an \(\epsilon\)-monochromatic vertex-simple tight Hamiltonian path.

The key deterministic construction is governed by a transversal matroid.

**Lemma 2 (separated-slot absorption).** Suppose \(P=(v_1,\ldots,v_\ell)\) is an injective \(\epsilon\)-monochromatic tight path and \(U=V\setminus V(P)\). Let \(I\subseteq\{2,\ldots,\ell-2\}\) be gap indices at pairwise distance at least five. Form a bipartite graph \(B\) with left vertices \(U\) and right vertices \(I\); declare \(z\in U\) adjacent to \(i\in I\) when
\[
b(v_{i-1},v_i,z)=b(v_i,z,v_{i+1})
=b(z,v_{i+1},v_{i+2})=\epsilon.\tag{2}
\]
If \(B\) has a matching saturating \(U\), then the original coloring has an \(\epsilon\)-monochromatic tight Hamiltonian path beginning with \((v_1,v_2)\).

*Proof.* For each matched pair \((z,i)\), insert \(z\) between \(v_i,v_{i+1}\). The insertion removes the two original triple windows meeting that gap and replaces them by the three windows in (2), all of the required color. Because selected gaps are separated by at least five positions, the changes at different gaps are disjoint. The resulting word uses all vertices once and retains its first two vertices. Matchable subsets of \(U\) are the independent sets of the transversal matroid determined by \(B\). \(\square\)

*Proof of Theorem 1.* Fix \(u,v,\epsilon\). Set
\[
t=\lceil12\rho^{-1}\log n\rceil,\qquad r=2t.
\]
Condition (1) implies \(t\log n=o(n)\), hence \(r=o(n)\). Beginning with \((u,v)\), repeatedly choose uniformly at random \(t\) of the unused vertices, expose the triples obtained by appending each candidate, and append one candidate with color \(\epsilon\), continuing until \(r\) vertices remain. At each step every newly queried reversal class has the current terminal vertex as its middle vertex. That vertex has never been the middle vertex of an earlier extension query, since the growing path is injective. Therefore the candidate colors are fresh independent random variables, each equal to \(\epsilon\) with probability at least \(\rho\). The chance that a step has no acceptable candidate is at most \((1-\rho)^t\le n^{-12}\). A union bound over fewer than \(n\) steps shows that, except with probability at most \(n^{-11}\), this process produces a monochromatic path \(P\) of length \(\ell=n-r\).

For each \(z\in V\), let \(Q_z\) be the number of stages whose random query set included \(z\). When \(k\) vertices are still unused, the conditional probability of such inclusion is at most \(t/k\), even given the entire earlier construction. Once \(z\) has been appended, its subsequent inclusion probability is zero. Therefore the moment-generating bound for adapted indicators gives
\[
\mathbb E e^{Q_z}
\le \exp\!\left((e-1)t\sum_{k=r+1}^{n-2}k^{-1}\right)
\le \exp((e-1)t(1+\log n)).
\]
By Markov's inequality,
\[
\Pr[Q_z>4t(1+\log n)]
\le\exp(-(5-e)t(1+\log n)).
\]
A union bound gives, with probability \(1-o(n^{-10})\),
\[
\boxed{\max_{z\in V}Q_z\le4t(1+\log n)=o(n).}\tag{3}
\]

Choose \(I=\{2,7,12,\ldots\}\cap\{2,\ldots,\ell-2\}\), so \(K=|I|=(1/5+o(1))n\). For any missing \(z\in U\), consider the three insertion comparisons at gap \(i\). The comparison centered at \(z\) has never been exposed, because \(z\) was never a terminal path vertex. The last comparison, centered at \(v_{i+1}\), also has not been exposed: when \(v_{i+1}\) was terminal during construction, every tested triple had \(v_i\) as one outer vertex, while \((z,v_{i+1},v_{i+2})\) has two different outer vertices. Only the first comparison, centered at \(v_i\), might have been exposed. This occurs at no more than \(Q_z\) gaps. Thus at least \(K-Q_z\) gap comparisons are fully fresh for each missing \(z\).

The reversal classes in the three comparisons for distinct eligible pairs \((z,i)\in U\times I\) are all different: the five-position gap spacing separates centers \(v_i,v_{i+1}\), the missing vertices \(z\) lie outside \(P\), and the remaining outer pairs identify the missing vertex and its gap. Conditional on the complete construction history, all eligible compatibility indicators are independent and have success probability at least \(\rho^3\).

We verify Hall's condition by a union bound. Let \(A\subseteq U\) be nonempty, with \(a=|A|\), and \(C\subseteq I\) have cardinality \(a-1\). If (3) holds, then for each \(z\in A\), at least
\[
K-Q_z-|C|\ge n/10
\]
gaps outside \(C\) retain three fresh comparisons, for all sufficiently large \(n\), since both \(r\) and the bound in (3) are \(o(n)\). The probability that no compatible edge joins \(A\) to \(I\setminus C\) is at most \(e^{-\rho^3 a n/10}\). The number of pairs \(A,C\) of these cardinalities is bounded by
\(\binom ra\binom K{a-1}\le n^{2a}\). Hence
\[
\Pr[\exists A\subseteq U:|N_B(A)|<|A|\mid\text{construction}]
\le\sum_{a=1}^{r}\exp\!\left(a(2\log n-\rho^3n/10)\right)
=n^{-\omega(1)}.\tag{4}
\]
By Hall's theorem, with overwhelming probability the bipartite compatibility graph has a matching saturating \(U\). Lemma 2 inserts every leftover vertex while preserving the complete monochromatic path. The error probabilities from the greedy stage, the exposure estimate, and Hall's estimate sum to \(o(n^{-3})\), allowing a final union bound over both colors and fewer than \(n^2\) ordered initial pairs. \(\square\)

**Scope and interpretation.** This proves a three-window, resource-preserving absorption theorem for ordinary boundary 3-tournaments and identifies its intrinsic transversal-matroid independence condition. The random perturbation assumption supplies the necessary compatible slots. It substantially strengthens near-spanning random smoothing, but it does not establish a deterministic spanning monochromatic path for arbitrary boundary colorings. For cube-edge colorings, inserting an unused coordinate at an interior position changes the edges along the entire remaining suffix, so an additional cubical exchange argument would be required for a parallel Hamiltonian result.
