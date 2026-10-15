# Random smoothing and the failure of global edge-order purification

# Random smoothing and the failure of global edge-order purification

Let \(V\) be a set of \(n\) vertices, \(n\ge3\). A reversal-odd coloring is a map \(b_0:V_{\ne}^3\to\{0,1\}\) satisfying \(b_0(c,v,a)=1-b_0(a,v,c)\). Fix \(0<\rho\le1/2\). Independently for each reversal class \(\{(a,v,c),(c,v,a)\}\), choose a Bernoulli random variable \(Z_{\{a,v,c\}}\) of parameter \(\rho\), and define
\[
b(a,v,c)=b_0(a,v,c)\oplus Z_{\{a,v,c\}}.
\tag{1}
\]
Thus \(b\) is again reversal-odd.

**Theorem 1 (near-spanning paths after independent perturbation).**
Fix an ordered pair \(u,v\) of distinct vertices, a color \(\epsilon\in\{0,1\}\), and \(0<\delta<1\). Put
\[
r=\left\lceil \rho^{-1}\log(n/\delta)\right\rceil .
\]
If \(r\le n-2\), then with probability at least \(1-\delta\), the coloring \(b\) admits a vertex-simple \(\epsilon\)-monochromatic tight path beginning with \(u,v\), using at least \(n-r\) vertices. In particular, when \(\rho n/\log n\to\infty\), with probability tending to one every ordered starting pair and each prescribed color admits such a path on \(n-O(\rho^{-1}\log n)\) vertices.

*Proof.* Build a sequence \(v_1=u,v_2=v,\ldots\) by greedily appending any unused \(w\) for which \(b(v_{i-1},v_i,w)=\epsilon\). To decide whether the next extension exists, reveal the colors of the triples \((v_{i-1},v_i,w)\) for unused \(w\). Every one of their reversal classes has middle vertex \(v_i\). The vertices \(v_i\) used as centers at successive stages are distinct, hence none of these classes has been queried at an earlier stage. Conditional on the complete past of the algorithm, the new bits are independent and each has probability at least \(\rho\) of yielding the desired color, whatever the deterministic values of \(b_0\). If \(k\) vertices remain unused, the conditional probability of failure is at most
\[
(1-\rho)^k\le e^{-\rho k}.
\]
Before \(n-r\) vertices have been used, \(k\ge r\), and there are at most \(n\) opportunities to fail. A union bound gives probability of failure at most \(ne^{-\rho r}\le\delta\). For the uniform assertion choose \(r=\lceil6\rho^{-1}\log n\rceil\), giving failure probability at most \(n^{-5}\) for each of fewer than \(2n^2\) starting-pair/color choices. A final union bound completes the proof. \(\square\)

A spanning subgraph \(G\subseteq K_V\) is called *comparison-orderable for \(b\)* if some strict total ordering of \(E(G)\) induces \(b(a,v,c)\) on every pair of incident edges \(av,vc\in E(G)\). Such a graph has a transitive induced subtournament on \(N_G(v)\) for every vertex \(v\): its local arc \(a\to c\) is defined by \(b(a,v,c)\), and a single ordering of the incident edges at \(v\) determines all its arcs.

**Lemma 2 (edge-disjoint triangle packing).** For any integer \(d\ge3\), the complete graph \(K_d\) contains at least \(d(d-1)/18\) triangles with pairwise disjoint edge sets.

*Proof.* Greedily select a triangle and remove every triangle sharing one of its three edges. Each selection removes at most \(3(d-2)\) triangles, while \(K_d\) originally contains \(\binom d3\) triangles. At least \(\binom d3/[3(d-2)]=d(d-1)/18\) selections are possible. \(\square\)

**Theorem 3 (uniform obstruction to comparison-orderable subgraphs).**
For every deterministic baseline \(b_0\), with probability tending to one as \(n\to\infty\), every comparison-orderable spanning subgraph \(G\subseteq K_V\), even allowing its edge ordering to depend on \(b\) and \(G\), satisfies
\[
\boxed{\quad
\Delta(G)<\left\lceil\frac{200\log n}{\rho}\right\rceil
\quad\text{whenever the right side is at most }n-1.\quad}
\tag{2}
\]
Consequently all such \(G\) satisfy
\[
\boxed{\quad |E(G)|=O\!\left(\frac{n\log n}{\rho}\right). \quad}
\tag{3}
\]
The implicit constant is absolute, independent of \(b_0\).

*Proof.* Fix a center \(v\) and a \(d\)-set \(S\subseteq V\setminus\{v\}\), where \(d=\lceil200(\log n)/\rho\rceil\le n-1\). For a triple \(\{a,c,e\}\subseteq S\), the restriction of the tournament \(b(\cdot,v,\cdot)\) to those three vertices is cyclic with probability at least \(\rho/4\). Indeed, if it is transitive in \(b_0\), flipping just the comparison between the first and last vertices in its transitive order produces a directed cycle, with probability \(\rho(1-\rho)^2\ge\rho/4\). If it is initially cyclic, keeping all three comparisons unchanged has probability \((1-\rho)^3\ge1/8\ge\rho/4\).

Choose the edge-disjoint triangle packing of Lemma 2 on \(S\). The corresponding cyclic-triangle events involve disjoint comparison variables and are therefore independent. Since there are at least \(d(d-1)/18\) such triangles,
\[
\Pr\bigl(b(\cdot,v,\cdot)|_S\text{ is transitive}\bigr)
\le\left(1-\frac{\rho}{4}\right)^{d(d-1)/18}
\le \exp\left(-\frac{\rho d(d-1)}{72}\right).
\]
The probability that some \(v\) and \(d\)-set \(S\) have a transitive induced local tournament is at most
\[
n\binom{n-1}{d}\exp\left(-\frac{\rho d(d-1)}{72}\right)
\le n\exp\left(d\log n-\frac{\rho d(d-1)}{72}\right)=o(1).
\tag{4}
\]
The last relation follows from \(d\ge200(\log n)/\rho\). On the complementary event, no comparison-orderable graph can have a vertex of degree at least \(d\), since that vertex's neighbor set contains such a transitive \(d\)-set. This proves (2). If \(d>n-1\), (3) is trivial from \(|E(G)|\le\binom n2\); otherwise use the degree bound. \(\square\)

**Corollary 4 (near-extremal coloring with almost-spanning paths but no dense orderable subgraph).**
There exist reversal-odd boundary colorings \(b_n\) on \(n\) vertices for which simultaneously
\[
\boxed{\frac{D(b_n)}{E_n}\ge \frac23-O(n^{-1/3}),}\tag{5}
\]
every ordered pair and both colors initiate a monochromatic tight path on \(n-O(n^{1/3}\log n)\) vertices, and every comparison-orderable subgraph \(G\subseteq K_n\) satisfies
\[
\boxed{|E(G)|=O(n^{4/3}\log n),\qquad
\Delta(G)=O(n^{1/3}\log n).}\tag{6}
\]
Here \(D(b)\) counts disagreeing edges of the legal-turn reversal quotient and \(E_n=n(n-1)(n-2)(n-3)/2\).

*Proof.* Randomly assign distinct real labels to \(E(K_n)\), and let \(b_0\) compare consecutive edge labels. Each legal turn \((a,b,c,d)\) involves three distinct edges with independent labels, so the probability of a changed comparison is \(2/3\). By averaging, there exists a deterministic edge order with \(D(b_0)/E_n\ge2/3\). Perturb this \(b_0\) as in (1) with \(\rho=n^{-1/3}\).

The two reversal classes involved in each legal turn are distinct, so their flips are independent. Write \(h=2\rho(1-\rho)\). The perturbed turn disagrees with probability \(h+(1-2h)d_0\), where \(d_0\in\{0,1\}\) is its original disagreement bit. Since \(1-2h=(1-2\rho)^2\ge0\),
\[
\frac{\mathbb E D(b)}{E_n}
=h+(1-2h)\frac{D(b_0)}{E_n}
\ge\frac23-\frac h3\ge\frac23-\frac23\rho.
\tag{7}
\]
There are \(N_n=n\binom{n-1}{2}\) independently perturbed reversal classes, and changing one flip changes \(D\) by at most \(2(n-3)\). The bounded-differences inequality therefore gives, for any \(t>0\),
\[
\Pr\left(\frac{D(b)}{E_n}<\frac{\mathbb E D(b)}{E_n}-t\right)
\le \exp(-t^2N_n/2).
\tag{8}
\]
Taking \(t=\rho\) proves (5) with probability tending to one. Theorem 1, with \(\delta=n^{-5}\) and a union bound over all starting ordered pairs and colors, gives the claimed paths. Theorem 3 gives (6). All three events occur simultaneously with probability tending to one, proving existence. \(\square\)

The contrast is structural: even when an unrestricted boundary coloring is arbitrarily close in normalized disagreement density to the extremal value \(2/3\), and supports near-spanning monochromatic paths, a subgraph on which *any* total edge ordering realizes all its local comparisons may have only \(O(n^{4/3}\log n)\) edges. Resource-simple paths can navigate mutually incompatible comparisons globally, so an exchange theorem seeking long paths must retain only the comparisons used by the evolving witness rather than insist upon one global edge-order representation.

**Theorem 5 (near-geodesic smoothing of antipodally odd cube colorings).**
Let \(Q_n\) be the \(n\)-dimensional cube, let \(c_0:E(Q_n)\to\{0,1\}\) satisfy \(c_0(\tau e)=1-c_0(e)\), where \(\tau\) is antipodal reversal, and fix a root vertex \(x\) and color \(\epsilon\). Independently for each antipodal pair of cube edges \(\{e,\tau e\}\), flip both assigned colors with probability \(\rho\), where \(0<\rho\le1/2\). Put \(r=\lceil\rho^{-1}\log(n/\delta)\rceil\) for \(0<\delta<1\). If \(2\le r\le n-1\), with probability at least \(1-\delta\) there is an \(\epsilon\)-monochromatic path beginning at \(x\) that uses \(n-r\) distinct coordinate directions, and hence is a geodesic of length \(n-r\). If \(\rho n/\log n\to\infty\), such a path has length \(n-o(n)\) with probability tending to one, for each prescribed root and color.

*Proof.* Identify vertices relative to \(x\) with subsets \(S\subseteq[n]\), and regard the directed edge \(e(S,i)\) from \(x^S\) to \(x^{S\cup\{i\}}\), \(i\notin S\), as a possible increasing-resource move. Greedily select an unused coordinate \(i\) whenever \(c(e(S,i))=\epsilon\). We show that, as long as \(|S|\le n-2\), all candidate antipodal edge orbits at the current step are distinct and have never been queried at an earlier step.

Indeed, let \(T\subsetneq S\) be a previously visited coordinate set, and let \(e(T,j)\) have been queried at that step. The current edge \(e(S,i)\) cannot equal \(e(T,j)\), since these two edges have different lower endpoints. If \(e(S,i)=\tau e(T,j)\), comparison of the endpoints with their ranks in the Boolean lattice gives
\[
S=[n]\setminus(T\cup\{j\}),\qquad
S\cup\{i\}=[n]\setminus T.
\]
Thus \(i=j\) and \(S\cap T=\varnothing\). Since \(T\subseteq S\), we have \(T=\varnothing\), and then \(S=[n]\setminus\{i\}\), contradicting \(|S|\le n-2\). Distinct current candidate coordinates also represent distinct antipodal edge orbits. This proves freshness until the final coordinate.

Consequently, conditional on all previously queried colors, when \(k=n-|S|\ge2\) unused coordinates remain, the candidate colors are independent, each with probability at least \(\rho\) of equaling \(\epsilon\). The conditional chance that all \(k\) extensions fail is at most \(e^{-\rho k}\). Until length \(n-r\) has been reached, at least \(r\ge2\) coordinates remain. At most \(n\) stages are tested, so the total failure probability is at most \(ne^{-\rho r}\le\delta\). Each selected coordinate is used once, so the resulting path is a geodesic. \(\square\)

**Common probabilistic mechanism.** Theorem 1 and Theorem 5 both exploit a graded extension system in which each extension consumes a new resource and its local candidates belong to noise variables unexposed at previous stages. For boundary tournaments the new resource is the next terminal vertex, giving a previously unused middle vertex for every new triple comparison. For cube geodesics the new resource is the next coordinate, and antipodal edge-orbit collisions are excluded until the final step by the Boolean-lattice complement relation. This common mechanism gives near-full-length single-color paths under independent perturbations, while the deterministic problem demands a zero-defect selection under arbitrary signatures; the cube theorem makes no claim about extending the last \(r\) coordinates in the prescribed color.
