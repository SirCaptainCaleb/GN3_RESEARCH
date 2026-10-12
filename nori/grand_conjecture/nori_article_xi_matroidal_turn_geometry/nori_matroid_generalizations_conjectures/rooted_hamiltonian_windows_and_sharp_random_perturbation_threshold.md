# Rooted Hamiltonian windows and sharp random perturbation threshold

# Rooted Hamiltonian windows and the sharp random perturbation threshold

Let \(V\) be an \(n\)-element set, \(n\ge4\), and let \(b_0:V_{\ne}^3\to\mathbb F_2\) satisfy \(b_0(c,v,a)=1-b_0(a,v,c)\). Independently flip both colors in each reversal orbit of ordered triples with probability \(\rho\in(0,1/2]\), obtaining \(b\). For an injective word \(P=(v_1,\dots,v_n)\), its windows are the ordered triples \((v_i,v_{i+1},v_{i+2})\), \(1\le i\le n-2\).

**Theorem 1 (optimal rooted Hamiltonian pattern universality).** Fix any ordered pair \((u,v)\) of distinct vertices and any predetermined binary word \(a=(a_1,\ldots,a_{n-2})\). Put
\[
h_n=\frac{e(1+2e)(\rho^{-1}-1)}{n-2}.
\]
If \(h_n<1\), then, uniformly over \(b_0\),
\[
\boxed{\Pr\bigl(\text{no Hamiltonian tight path starting with \(u,v\) has color word \(a\)}\bigr)\le h_n.}\tag{1}
\]
Consequently \(\rho_n n\to\infty\) implies that each preselected color word is realized from \((u,v)\) with probability \(1-o(1)\), uniformly in the word. Simultaneous realization of all color words is not asserted. Conversely, the assumption \(\rho_n n\to\infty\) is necessary for this assertion to hold uniformly over all baseline colorings.

The key input is a factorial-moment inequality for overlapping length-three windows.

**Lemma 2 (fixed-prefix window overlap).** Fix a permutation \(\pi=(1,\ldots,n)\), and choose \(\sigma\) uniformly among permutations beginning with \(1,2\). Let \(K(\pi,\sigma)\) count the reversal orbits of length-three windows appearing in both \(\pi\) and \(\sigma\). For \(z\ge1\), set \(y=z-1\). Then
\[
\boxed{\mathbb E_\sigma z^{K(\pi,\sigma)}
\le\sum_{t=0}^{n-2}\left(\frac{e(1+2e)y}{n-2}\right)^t.}\tag{2}
\]

*Proof.* Put \(N=n-2\). For a nonempty set \(S\subseteq[N]\), with \(|S|=t\), write \(c\) for its number of maximal runs of consecutive integers. Each selected triple window at rank \(i\) requires its two undirected path edges \(\{i,i+1\},\{i+1,i+2\}\) to occur as adjacent pairs in \(\sigma\). Their union is a path forest with \(t+c\) edges. Add the edge \(\{1,2\}\), which is already the prescribed first edge of \(\sigma\).

If \(1\in S\), the added edge is already present; the resulting forest has \(m=t+c\) edges and at most \(c\) nontrivial components. If \(1\notin S\), it has \(m=t+c+1\) edges and at most \(c+1\) components. For a forest with \(m\) edges and \(r\) nontrivial path components, one of which contains the required initial ordered edge \((1,2)\), the number of permutations beginning \(1,2\) that contain every forest edge as a consecutive adjacency is at most \(2^{r-1}(n-m-1)!\): the initial component has its order and position prescribed, each other path component admits two orientations, and the remaining blocks can be permuted. Dividing by the total \((n-2)!\) gives
\[
\Pr(S\text{ is contained in the common-window indices})\le
\begin{cases}
2^{c-1}/(N)_{t+c-1},&1\in S,\\
2^c/(N)_{t+c},&1\notin S,
\end{cases}\tag{3}
\]
where \((N)_j=N(N-1)\cdots(N-j+1)\). The bound holds because every shared triple imposes its two underlying path adjacencies.

The number of \(t\)-subsets of \([N]\) with \(c\) runs and containing \(1\) is
\[
\binom{t-1}{c-1}\binom{N-t}{c-1},
\]
and the number avoiding \(1\) is
\[
\binom{t-1}{c-1}\binom{N-t}{c}.
\]
Use \((N)_j\ge(N/e)^j\), \(\binom{N-t}{j}\le N^j/j!\), and \(1/j!\le1\). The sum of probabilities in (3) over all \(t\)-subsets is at most
\[
\begin{aligned}
&\left(\frac eN\right)^t
\sum_{c=1}^t\binom{t-1}{c-1}
\left(\frac{(2e)^{c-1}}{(c-1)!}
+\frac{(2e)^c}{c!}\right)\\
&\hspace{30mm}\le
\left(\frac eN\right)^t(1+2e)^t.\tag{4}
\end{aligned}
\]
Finally expand \(z^K=(1+y)^K=\sum_{S\subseteq\mathrm{CommonWindows}}y^{|S|}\), average, and insert (4), proving (2). \(\square\)

*Proof of Theorem 1.* Let \(\mathcal P\) be the \((n-2)!\) permutations of \(V\) starting with \(u,v\). Let \(A_P\) be the event that the consecutive triple-color word of \(P\) equals \(a\), and let \(q_P=\Pr(A_P)>0\). Their reversal orbits are distinct because their middle vertices are distinct, so
\[
q_P=\prod_{t\in\mathrm{Windows}(P)}p_t,\qquad p_t\in[\rho,1-\rho].
\]
Define
\[
Z=\sum_{P\in\mathcal P}\frac{\mathbf1_{A_P}}{q_P},
\qquad \mathbb E Z=(n-2)!.
\]
If two words \(P,Q\) require opposing colors on the same reversal orbit, their joint all-\(\epsilon\) event has probability zero. Otherwise independence of distinct orbit-noise variables shows that the ratio \(\Pr(A_P\cap A_Q)/(q_Pq_Q)\) is a product of \(p_t^{-1}\le\rho^{-1}\) over their shared window orbits. Hence
\[
\frac{\mathbb EZ^2}{(\mathbb EZ)^2}
\le\mathbb E_{P,Q}\rho^{-K(P,Q)}
\le\sum_{t=0}^{n-2}h_n^t
\le(1-h_n)^{-1}.
\]
By Cauchy--Schwarz, \(\Pr(Z>0)\ge(\mathbb EZ)^2/\mathbb EZ^2\ge1-h_n\), giving (1).

For necessity, choose \(b_0(u,v,w)=1-a_1\) for every \(w\in V\setminus\{u,v\}\), assign the reverse triples their complementary color, and fill the remaining reversal orbits arbitrarily. With probability \((1-\rho)^{n-2}\), no triple \((u,v,w)\) is flipped, and no Hamiltonian tight path starting with \(u,v\) can realize \(a\). This failure probability stays bounded away from zero if \(n\rho\) remains bounded. \(\square\)

**Common witness-overlap principle.** The theorem and the rootwise cube-geodesic theorem of the preceding Subsection both use a family of full-resource paths, with a distinct independent noise variable for each edge or window constraint within a path. For any such finite family \(\mathcal W\), let \(q_W>0\) be the probability that \(W\) satisfies its prescribed monochromatic constraints, and let \(K(W,W')\) count shared unoriented noise-variable orbits. With \(Z=\sum_W\mathbf1_{\{W\text{ succeeds}\}}/q_W\), the same argument gives
\[
\boxed{
\Pr(Z>0)\ge
\left(\mathbb E_{W,W'}\rho^{-K(W,W')}\right)^{-1}.}\tag{5}
\]
Oppositely oriented shared constraints make joint success impossible and only strengthen the estimate. In both canonical applications, the overlap sets form subforests of underlying path bases; their factorial moments decay sufficiently rapidly to produce the common optimal rootwise smoothing condition \(n\rho\to\infty\).

The theorem concerns independent random perturbations of arbitrary reversal-odd colorings and applies to each prescribed window pattern, including monochromatic, one-switch, and alternating words. It strengthens the earlier transversal-matroid absorption theorem, which supplies simultaneous guarantees for all ordered starting pairs under a larger perturbation rate. Neither theorem establishes a deterministic boundary-tournament selector or unrestricted NORI1.
