# Sharp rootwise random cube geodesics by singleton-block second moments

# Rooted random cube geodesics and permutation overlap moments

Fix a cube vertex \(x\), a prescribed color \(\epsilon\), and an arbitrary antipodally odd coloring \(c_0\) of \(Q_n\). Independently flip both colors in each antipodal edge orbit with probability \(\rho\in(0,1/2]\), producing \(c\).

**Theorem (optimal rootwise noise threshold).** If \(n\rho\to\infty\), the probability that there is an \(\epsilon\)-monochromatic geodesic from \(x\) to \(\tau x\) tends to one, uniformly over \(c_0\). Put \(h=3e(\rho^{-1}-1)/n\). If \(h<1\), the failure probability is at most \(h\). The growth assumption \(n\rho\to\infty\) is necessary for the uniform fixed-root, fixed-color assertion.

**Lemma (shared-edge moment).** Fix a direction permutation \(\pi\), take \(\sigma\in S_n\) uniformly, and let \(s\) be the number of cube edges common to the two root-to-antipode geodesics. For every \(z\ge1\),
\[
\mathbb E z^s\le\sum_{t=0}^n\frac{[3(z-1)]^t}{(n)_t}
\le\sum_{t=0}^n\left(\frac{3e(z-1)}n\right)^t.
\tag{1}
\]

*Proof.* Relabel so that \(\pi=(1,\ldots,n)\). The edge at rank \(k\) is common precisely when the first \(k\) symbols of \(\sigma\) are \([k]\) and its next symbol is \(k+1\). This is a singleton component of its direct-sum permutation decomposition. Prescribing \(t\) such positions divides the other \(n-t\) entries into \(t+1\) consecutive blocks of sizes \(a_0,\ldots,a_t\). The number of compatible permutations is \(\prod_j a_j!\). Expanding \(z^s=(1+z-1)^s\) gives
\[
\mathbb E z^s=\frac1{n!}\sum_{t=0}^n(z-1)^t
\sum_{\substack{a_0+\cdots+a_t=n-t\\a_j\ge0}}\prod_j a_j!.
\]
For all \(m\ge0\), \(\sum_{j=0}^m j!(m-j)!=m!\sum_j\binom mj^{-1}\le3m!\), since the two extreme reciprocals are one and each interior reciprocal is at most \(1/m\). Convolution induction bounds the inner sum by \(3^t(n-t)!\), giving the first inequality. The inequality \((n)_t\ge(n/e)^t\), obtained by comparing the geometric means of the largest \(t\) integers among \(1,\ldots,n\) with \((n!)^{1/n}\ge n/e\), proves the second. \(\square\)

*Proof of the theorem.* Let \(A_\pi\) be the event that the path of direction permutation \(\pi\) is all color \(\epsilon\), and \(q_\pi=\Pr(A_\pi)\). A geodesic uses each direction once, so its edges lie in distinct antipodal orbits, and \(q_\pi=\prod_{f\in P_\pi}p_f\), where \(p_f=\Pr(c(f)=\epsilon)\in[\rho,1-\rho]\). Define
\[
Z=\sum_{\pi\in S_n}\frac{\mathbf1_{A_\pi}}{q_\pi};
\qquad\mathbb EZ=n!.
\]
For two geodesics \(P_\pi,P_\sigma\), their simultaneous all-\(\epsilon\) event has probability zero if an edge of one is antipodal to an edge of the other. Otherwise all orbit variables are independent except for common edges, each contributing a joint-to-product factor \(1/p_f\le1/\rho\). Consequently
\[
\frac{\mathbb EZ^2}{(\mathbb EZ)^2}
\le\mathbb E_{\pi,\sigma}\rho^{-|E(P_\pi)\cap E(P_\sigma)|}
\le\sum_{t=0}^n h^t\le(1-h)^{-1}.
\]
The second-moment inequality gives \(\Pr(Z>0)\ge1-h\), proving the quantitative claim and the limit. Conversely choose the initial coloring with all \(n\) edges at \(x\) colored \(1-\epsilon\), completing antipodal pairs consistently. With probability \((1-\rho)^n\), none of these root edges flips, so no \(\epsilon\)-monochromatic path starts at \(x\). This failure probability stays positive whenever \(n\rho\) is bounded. \(\square\)

The result concerns full geodesics under noise, and is uniform over the baseline coloring. The deterministic NORI1 conjecture remains open.

**Corollary (face smoothing).** Let \(F\) be an \(m\)-dimensional face of \(Q_n\), \(2\le m\le n\), and fix \(x\in F\) and a color \(\epsilon\). Independently flip the colors on full-cube antipodal edge pairs with probability \(\rho\). Then, uniformly in the initial antipodally odd coloring,
\[
\Pr(\text{no \(\epsilon\)-monochromatic geodesic in \(F\) between opposite face corners})
\le\frac{3e(\rho^{-1}-1)}m
\]
whenever the right side is below one. In particular, the failure probability is \(o(1)\) if \(m\rho\to\infty\).

*Proof.* A face geodesic uses each of its \(m\) free directions once, and hence meets distinct full-cube antipodal edge orbits. If \(F\) is proper, the full-cube antipodal translate of any edge of \(F\) lies outside \(F\), so two face geodesics can share an orbit only by using the same edge. In the full-face case, opposite edges between different geodesics produce incompatible prescribed-color events and contribute zero to their joint probability. Thus the weighted second-moment calculation and the permutation singleton-block bound of the theorem apply in either case, with \(m\) in place of \(n\). \(\square\)

**Lemma (opposite-chain edge exclusion).** Let \(P_\pi\) be the root-to-antipode geodesic given by a permutation \(\pi=(i_1,\ldots,i_n)\), and let \(P_{\pi^R}\) use its reverse permutation. Every root-to-antipode geodesic \(P_\sigma\) shares an edge with at most one of \(P_\pi,P_{\pi^R}\).

*Proof.* In used-direction-set notation relative to the root, the first path has edges between its consecutive prefix sets
\[
A_k=\{i_1,\ldots,i_k\},\qquad 0\le k\le n,
\]
whereas the second has edges between consecutive suffix sets
\[
B_j=\{i_{n-j+1},\ldots,i_n\},\qquad 0\le j\le n.
\]
If a nested direction-set chain contained an edge \(A_k\to A_{k+1}\) followed by an edge \(B_j\to B_{j+1}\), its sets would satisfy \(A_{k+1}\subseteq B_j\). But \(i_1\in A_{k+1}\) and \(i_1\notin B_j\), since \(j\le n-1\). If the suffix edge occurred first, the chain would require \(B_{j+1}\subseteq A_k\), contradicted by \(i_n\in B_{j+1}\) and \(i_n\notin A_k\). These exhaust the possible orders. \(\square\)

**Theorem (full edge-color profile universality).** Under the hypotheses of the rootwise smoothing theorem, fix an arbitrary predetermined word \(w=(w_1,\ldots,w_n)\in\{0,1\}^n\) and a root \(x\). There is a root-to-antipode geodesic whose consecutive edge colors form \(w\), with failure probability at most
\[
\boxed{\frac{2h}{1+h},\qquad
h=\frac{3e(\rho^{-1}-1)}n<1.}
\]
In particular this probability tends to one uniformly in the baseline coloring and prescribed word whenever \(n\rho\to\infty\). The growth condition is necessary for a uniform fixed-root, fixed-word assertion.

*Proof.* For every \(\pi\in S_n\), let \(A_\pi\) be the event that the sequence of colors along \(P_\pi\) is \(w\), let \(q_\pi=\Pr(A_\pi)>0\), and set \(Z=\sum_\pi\mathbf1_{A_\pi}/q_\pi\). Since each direction is used once, a single path visits distinct antipodal noise-variable orbits and \(\mathbb EZ=n!\).

A pair of paths may share a noise orbit through a common cube edge or through antipodal partner edges. When the two demands on a shared orbit conflict, their joint success probability is zero; otherwise that orbit contributes a joint-to-product factor at most \(\rho^{-1}\). Let \(K_+(\pi,\sigma)\) count edges common to \(P_\pi,P_\sigma\), and let \(K_-(\pi,\sigma)\) count edges common to \(P_{\pi^R},P_\sigma\). The antipodal image of the edge set of \(P_\pi\) is the edge set of \(P_{\pi^R}\), so \(K_++K_-\) counts shared noise orbits. By the opposite-chain exclusion lemma, \(K_+K_-=0\). Therefore, for \(z\ge1\),
\[
\begin{aligned}
\mathbb E_{\pi,\sigma}z^{K_++K_-}
&=1+\mathbb E(z^{K_+}-1)+\mathbb E(z^{K_-}-1)\\
&=2\mathbb E_{\pi,\sigma}z^{K_+}-1.
\end{aligned}
\]
The two overlap counts have identical marginal distributions under uniform permutations. Apply the singleton-block moment bound with \(z=\rho^{-1}\) to obtain
\[
\frac{\mathbb EZ^2}{(\mathbb EZ)^2}
\le2(1-h)^{-1}-1=\frac{1+h}{1-h}.
\]
Cauchy--Schwarz now yields \(\Pr(Z>0)\ge(1-h)/(1+h)\), proving the failure estimate. For necessity, prescribe the first edge color \(w_1\) and choose the initial coloring with all \(n\) root-incident edges of color \(1-w_1\). The probability that none flips is \((1-\rho)^n\), bounded away from zero when \(n\rho\) stays bounded. \(\square\)

On a proper \(m\)-face, no two of its edges lie in the same full-cube antipodal orbit. Hence the face corollary also holds for every prescribed length-\(m\) color word with its original failure bound \(3e(\rho^{-1}-1)/m\). The new theorem establishes a common fixed-pattern smoothing principle with the rooted boundary Hamiltonian-window theorem.

## Translated block networks amplify global smoothing

The face smoothing estimate can be amplified over many edge-orbit-disjoint networks. This permits a bounded value of \(n\rho\) for a global existence conclusion.

Fix a legal baseline coloring of \(Q_n\) and the same independent antipodal edge-orbit noise of rate \(0<\rho\le1/2\). Put
\[
C_\rho=3e(\rho^{-1}-1).
\]
Partition the directions into \(r\ge2\) nonempty blocks of sizes \(k_1,\ldots,k_r\), each greater than \(C_\rho\), and put \(K=\max_jk_j\). Starting at \(x\), traverse the blocks consecutively, using a full geodesic inside each block face, from its initial corner to its opposite corner. These faces form a network joining \(x\) to \(\bar x\).

**Theorem (global block smoothing).** Uniformly over the baseline,
\[
\boxed{
\Pr(\text{no zero full antipodal geodesic anywhere})
\le
\exp\!\left[
-\frac{2^n}{2\sum_{j=1}^r2^{k_j}}
\prod_{j=1}^r\left(1-\frac{C_\rho}{k_j}\right)
\right].
}\tag{GB1}
\]

*Proof.* Every block face is proper. Its zero connection has probability at least \(1-C_\rho/k_j\), by the preceding face corollary. Different faces in a network use disjoint direction sets, and hence disjoint noise orbits, so their success events are independent. A network therefore succeeds with probability at least
\[
p=\prod_j(1-C_\rho/k_j).
\]
A successful network concatenates to a zero full antipodal geodesic.

Consider all \(2^n\) translations of this network. Two translates can share a noise orbit only through faces belonging to the same direction block. For that block \(I_j\), the translation difference must lie in its binary span or in the antipodal translate of that span: outside \(I_j\), the two faces must have identical or complementary fixed bits. There are at most \(2\sum_j2^{k_j}\) such translation differences.

Greedy packing supplies at least \(2^n/(2\sum_j2^{k_j})\) networks with pairwise disjoint noise-orbit sets. Their success events are independent, each of probability at least \(p\). Global failure implies that all packed networks fail. Use \((1-p)^t\le e^{-pt}\) to obtain (GB1). \(\square\)

**Corollary (global smoothing at a bounded reciprocal-dimension rate).** For every fixed \(A>6e\), if \(\rho=A/n\) for sufficiently large \(n\), then for some \(c_A>0\),
\[
\boxed{
\Pr(\text{no zero full antipodal geodesic anywhere})
\le\exp(-c_A2^{n/2}).
}\tag{GB2}
\]
The same conclusion holds whenever \(\liminf n\rho>6e\).

*Proof.* Use two blocks of sizes \(\lfloor n/2\rfloor,\lceil n/2\rceil\). Their failure bounds have limits at most \(6e/A<1\), so their joint success probability is uniformly bounded below by a positive constant. The packing size is at least \(2^{\lfloor n/2\rfloor-2}\). The same argument uses any fixed lower bound \(A>6e\) for \(n\rho\). \(\square\)

The root and direction order may depend on the perturbed coloring. The fixed-root threshold proved earlier remains \(n\rho\to\infty\); (GB2) is a global statement with a freely selected root. The constant \(6e\) is a sufficient bound from this calculation, with no optimality claim.

**Corollary (uniform random odd colorings have doubly exponentially small bad probability).** Under the uniform distribution on legal odd cube-edge colorings,
\[
\boxed{
\Pr(\text{no monochromatic full antipodal geodesic})
\le
\exp\!\left(-2^{\,n-O(n^{1/3})}\right).
}\tag{GB3}
\]

*Proof.* Take \(\rho=1/2\), so \(C_\rho=3e\) and the perturbed coloring is uniform over all legal colorings. Partition the directions into \(r=\lfloor n^{2/3}\rfloor\) blocks whose sizes differ by at most one. Then \(K=O(n^{1/3})\), while their minimum size tends to infinity. Using \(\log(1-u)\ge-2u\) for \(0\le u\le1/2\) gives
\[
p=\prod_j(1-3e/k_j)\ge \exp(-O(n^{1/3})).
\]
The packing size is at least \(2^{n-K-1}/r\). Their product is \(2^{n-O(n^{1/3})}\), proving (GB3). Legal antipodal oddness interchanges zero and one geodesics by antipodal translation, so absence of a zero full geodesic is equivalent to absence of both colors. \(\square\)

**Encoding interpretation.** The packed networks use disjoint edge-orbit bits. Given a bad coloring, retain the bits outside them and encode each network's assignment by its index among its failing local assignments, with a single mixed-radix code for the tuple. The baseline, supports and ordered local failure lists determine a decoder. At \(\rho=1/2\), this is an injective encoding saving \(2^{n-O(n^{1/3})}\) bits in logarithmic code-space size. The global entropy-amplification criterion (EA7) requires a saving proportional to \(n2^{n-2}\); that stronger bound remains open.

The corresponding fixed-gauge-phase theorem in the curvature manuscript uses odd block sizes to solve correlated vertex-gauge seam equations. It proves a bad fraction at most \(\exp(-2^{n-O(\sqrt n)})\) inside every individual invariant vertex-gauge orbit. The different exponents reflect the different independence structures of edge-orbit noise and vertex gauges.


## Independent sparse rounds give exponential face smoothing

Put \(B=3e^2\). The following amplification uses only the proved face second-moment estimate.

**Lemma (independent-round amplification).** Consider an ordinary \(k\)-cube whose edges are independently occupied with probabilities at least \(p\), where \(0<p\le1/2\). Fix opposite corners. The probability that no occupied geodesic joins them is at most
\[
\boxed{q_k(p)=\exp\!\left(-\left\lfloor\frac{kp}{B}\right\rfloor\right).}\tag{SR1}
\]
The assertion also applies when occupancy means matching a prescribed direction-indexed profile or a prescribed positional color word on paths between these corners.

*Proof.* If \(t=\lfloor kp/B\rfloor=0\), the bound is immediate. Otherwise \(k\ge B/p\ge2B\). Generate \(t\) independent edge-percolation rounds, each with occupation probability \(p_0=B/k\le1/2\). In each round, the earlier ordinary-face second-moment bound gives failure probability at most
\[
\frac{3e(p_0^{-1}-1)}{k}\le\frac{3e}{B}=\frac1e.
\]
Consequently all rounds fail with probability at most \(e^{-t}\). Their union has independent edge indicators, with common occupation probability
\[
1-(1-B/k)^t\le tB/k\le p.
\]
Couple this union below the given independent occupation field, adding occupied edges separately as necessary. Connection is increasing in the occupation field, which proves (SR1).

For a direction-indexed profile, the required color of each edge is fixed by its direction. For a positional word, orient the face from its chosen initial corner; an edge joining ranks \(j-1,j\) has required color equal to the \(j\)-th word entry. Thus in both cases matching the prescription defines independent edge indicators of probabilities at least \(p\). \(\square\)

**Theorem (exponential fixed-root smoothing).** In the antipodal edge-orbit noise model, fix a root and either a positional length-\(n\) word or a direction-indexed binary profile. Uniformly over every legal baseline, the probability that no full geodesic from that root realizes the prescription is at most
\[
\boxed{
\exp\!\left(-\left\lfloor\frac{\lfloor n/2\rfloor\rho}{B}\right\rfloor\right)
+
\exp\!\left(-\left\lfloor\frac{\lceil n/2\rceil\rho}{B}\right\rfloor\right).
}\tag{SR2}
\]
In particular it is \(O(\exp[-n\rho/(2B)])\). For the fixed-root monochromatic assertion, the exponential order \(n\rho\) is optimal up to absolute constants.

*Proof.* Fix a partition into two nonempty direction blocks of sizes \(\lfloor n/2\rfloor,\lceil n/2\rceil\). Follow their two series faces from the prescribed root to its antipode. Both faces are proper, so within either face every edge uses a distinct full-cube antipodal noise orbit. Its prescribed-color occupation indicators are independent and each has probability at least \(\rho\). Apply (SR1) and a union bound. The positional prescription restricts to the corresponding consecutive segment in each face; a direction-indexed prescription restricts to its block. Successful face paths concatenate to the required full geodesic.

For the lower bound on the uniform monochromatic failure probability, take a baseline whose root-incident edges all have the opposite color. With probability \((1-\rho)^n\) none flips, preventing the first step. Since \(-\log(1-\rho)\) lies between \(\rho\) and \(2\rho\) for \(0<\rho\le1/2\), this obstruction has probability \(\exp[-\Theta(n\rho)]\). \(\square\)

Splitting into proper faces is essential to the argument: the occupation field on the whole cube has complementary values on antipodal edges. The independent-round construction is performed inside each proper face.

**Theorem (amplified global smoothing and polynomial-loss entropy bound).** For any partition into \(r\ge2\) nonempty blocks of sizes \(k_j\), put
\[
p_*=\prod_{j=1}^r(1-q_{k_j}(\rho)).
\]
Then
\[
\boxed{
\Pr(\text{no zero full antipodal geodesic anywhere})
\le
\exp\!\left[-\frac{2^n}{2\sum_j2^{k_j}}\,p_*\right].
}\tag{SR3}
\]
If \(n\rho\to\infty\), this implies, uniformly over the baseline,
\[
\boxed{
\Pr(\text{global failure})
\le
\exp\!\left[-2^{\,n-O(\rho^{-1}\log(n\rho)+\log n)}\right]
=
\exp[-2^{\,n-o(n)}].
}\tag{SR4}
\]
For uniform legal odd colorings, taking \(\rho=1/2\) improves (GB3) to
\[
\boxed{
\Pr(\text{NORI1 failure})
\le \exp[-2^{\,n-O(\log n)}]
=\exp[-2^n/n^{O(1)}].
}\tag{SR5}
\]

*Proof.* In the translated block-network proof of (GB1), replace each face-success lower bound by \(1-q_{k_j}(\rho)\) from (SR1). The faces of one network use disjoint direction sets and hence disjoint noise orbits. The same packing supplies at least \(2^n/(2\sum_j2^{k_j})\) mutually independent networks, proving (SR3).

Write \(a=n\rho\to\infty\) and choose
\[
k=\left\lceil\frac{2B\log a}{\rho}\right\rceil,\qquad r=\lfloor n/k\rfloor.
\]
For sufficiently large \(a\), one has \(k=o(n)\) and \(r\ge2\). Partition into \(r\) blocks with sizes differing by at most one. Their minimum size is at least \(k\), and maximum size \(K\le2k\). Hence
\[
q_{k_j}(\rho)\le e\,a^{-2},\qquad
\sum_jq_{k_j}(\rho)\le \frac{e}{2B\,a\log a}=o(1).
\]
The product bound \(p_*\ge1-\sum_jq_{k_j}(\rho)\) gives \(p_*\ge1/2\) eventually. Also \(\sum_j2^{k_j}\le r2^K\), so the exponent in (SR3) is at least \(2^{n-K-2}/r\). This proves (SR4), and its specialization gives (SR5). \(\square\)

**Simultaneous global profile universality.** Under the assumptions of (SR4), with probability at least
\[
1-2^{n+1}\exp\!\left[-2^{\,n-O(\rho^{-1}\log(n\rho)+\log n)}\right],
\]
every direction-indexed binary profile occurs on some full geodesic, and every positional binary word occurs on some full geodesic. Roots and orders may vary with the prescription. Indeed (SR3) applies to each prescribed profile or word by using its induced edge demands on every translated face network; a union bound covers the two lists, each of size \(2^n\).

**Closure status.** At \(\rho=1/2\), the disjoint-network failure-list encoder now saves \(2^{n-O(\log n)}\) edge-orbit bits in logarithmic code-space size. This is a polynomial-loss improvement on the earlier \(2^{n-O(n^{1/3})}\) saving. The entropy-amplification closure criterion requires a saving \(\varepsilon n2^{n-2}\) for some fixed \(\varepsilon>0\). That remaining step asks for additional compatibility among overlapping failed networks. Independent sparse rounds settle the sharp exponential order of fixed-root noise smoothing; they do not establish deterministic NORI1.


## A limitation of marginal entropy bounds on orbit-simple supports

Call a cube-edge subgraph \(K\) *orbit-simple* if it contains at most one edge from each full-cube antipodal edge pair. It need not be connected, induced, or a series of faces. Let \(S(K)\) be its set of edge orbits and \(s=|S(K)|\). For uniform legal odd colorings, let \(F_K\) be the set of assignments on these \(s\) independent bits for which \(K\) contains no zero full antipodal geodesic, allowing every root and direction order in \(K\). Define its local entropy deficit by
\[
D_K=s-\log_2|F_K|.
\]

**Theorem (direction-blocking bound).** For every orbit-simple \(K\),
\[
\boxed{D_K\le \min_i|E_i(K)|\le s/n.}\tag{SR6}
\]

*Proof.* Choose any direction \(i\). Set every direction-\(i\) edge of \(K\) to color one. These are \(|E_i(K)|\) independent conditions, because \(K\) contains no antipodal partner edges. They admit \(2^{s-|E_i(K)|}\) assignments, all belonging to \(F_K\): a zero full geodesic would need a direction-\(i\) edge. Hence \(D_K\le |E_i(K)|\). Minimize and use \(\sum_i|E_i(K)|=s\). If a direction is missing, the deficit is zero. \(\square\)

The same argument applies to any chosen smaller family of candidate full geodesics in \(K\), and to a fixed direction-indexed profile after whole-direction color complements.

**Corollary (marginal failure-list compression cannot supply a fixed entropy deficit).** Put \(L=n2^{n-2}\). Suppose one bounds global bad colorings using only local failure-list cardinalities for orbit-simple supports. Neither disjoint-support coding nor the weighted Shearer bound can certify a saving greater than \(L/n\) bits.

*Proof.* For disjoint supports, retain the outside bits and index each local assignment in its failure list. The logarithmic code-space saving is \(\sum_KD_K\le\sum_K|S(K)|/n\le L/n\).

For a weighted Shearer argument, assign nonnegative weights \(w_K\) whose supports cover each of the \(L\) edge-orbit variables with total weight at least one. The resulting upper bound on logarithmic bad-set cardinality is
\[
U=\sum_K w_K\log_2|F_K|.
\]
By (SR6),
\[
U\ge(1-1/n)\sum_Kw_K|S(K)|\ge(1-1/n)L.
\]
Thus this upper-bound expression cannot certify a larger saving. If the constraints are indexed by smaller candidate path families, their failure lists are larger and the conclusion persists. \(\square\)

Every translated series-face network used above is orbit-simple. Within one face this follows from properness; different block faces have disjoint direction sets. The corollary therefore limits this entire marginal-counting architecture even if all face probabilities and packing constants were improved. It is a limitation of these entropy estimates, rather than a lower bound on the cardinality of their joint failure set. Joint reconstruction from overlapping constraints may yield further savings.

**Implication for closure.** The fixed entropy-deficit criterion requires \(\varepsilon L\) saved bits for a dimension-independent \(\varepsilon>0\). A proof through local constraints must therefore exploit their joint compatibility more strongly than marginal failure-list counting, or use supports containing both representatives of some antipodal edge pairs. The antipodal dependence that disappears on proper faces must enter the closing argument.


## Sparse global noise simultaneously realizes every direction profile and every positional color word

Fix any legal antipodally odd coloring \(c_0\) of the undirected edges of \(Q_n\). Flip each antipodal edge-pair variable independently with probability \(\rho=A/n\), where \(A>6e\) is fixed and \(n\) is sufficiently large that \(\rho\le1/2\). Write \(c\) for the resulting legal coloring. Let \(\mathcal W_{\rm dir}(c)\) be the set of full-geodesic edge-color vectors indexed by coordinate direction, and \(\mathcal W_{\rm pos}(c)\) the set of consecutive edge-color words, both ranging over all roots and full direction permutations.

**Theorem (sparse-noise simultaneous profile universality).** For each fixed \(A>6e\) there is \(b_A>0\) such that, uniformly in the baseline \(c_0\),
\[
\boxed{
\Pr\!\left(
\mathcal W_{\rm dir}(c)\ne\mathbb F_2^n
\text{ or }
\mathcal W_{\rm pos}(c)\ne\mathbb F_2^n
\right)
\le 2^{n+1}\exp\!\bigl(-b_A 2^{\lfloor n/2\rfloor}\bigr).
}
\tag{SPU1}
\]
One can take
\[
b_A=\tfrac14\left(\frac{1-6e/A}{2}\right)^2
\]
for all sufficiently large \(n\). Thus at an edge-orbit flip probability of order \(1/n\), the perturbation simultaneously realizes *every* prescribed direction-indexed color profile and *every* prescribed chronological color word, with probability tending to one uniformly in \(c_0\).

*Proof.* Split the \(n\) dimensions into two nonempty blocks \(I_1,I_2\) of sizes \(k_1=\lfloor n/2\rfloor\) and \(k_2=\lceil n/2\rceil\). Put
\[
C_\rho=3e(\rho^{-1}-1)=3e(n/A-1),\qquad
\beta_A=\frac{1-6e/A}{2}>0.
\]
The previously proved face-smoothing theorem applies on any proper \(k_j\)-face, for a prescribed direction-indexed profile on its free directions or a prescribed chronological word of length \(k_j\). It gives failure probability at most \(C_\rho/k_j\), which is at most \(1-\beta_A\) for all sufficiently large \(n\). In either case, therefore, every block face succeeds with probability at least \(\beta_A\), uniformly in the baseline coloring, face location and prescribed profile or word. The argument is legitimate under antipodal orbit noise because a proper face contains at most one edge from each full-cube antipodal edge orbit, and the desired color for each direction-indexed (respectively rank-indexed) face edge is predetermined independently of the noise.

Choose any root and traverse the two direction blocks consecutively, allowing arbitrary order *within* each block. For a prescribed direction-indexed word \(w\), require the first block's geodesic to realize \(w|_{I_1}\) and the second to realize \(w|_{I_2}\). For a prescribed positional word \(w\), require respectively its first \(k_1\) and last \(k_2\) entries. In either case successful face geodesics concatenate to a full geodesic realizing \(w\). The two face events are independent because their edge-orbit variables belong to disjoint direction blocks, so each two-block network succeeds with probability at least \(\beta_A^2\).

Now translate this fixed two-face network by each of the \(2^n\) cube translations. Two translated networks can share an antipodal edge-pair orbit only if the corresponding faces belong to the *same* direction block \(I_j\); their translation difference must be zero or all-one outside \(I_j\). For each \(j\) there are at most \(2^{k_j+1}\) such translation differences. Greedy packing therefore gives at least
\[
M\ge\frac{2^n}{2(2^{k_1}+2^{k_2})}
\ge 2^{\lfloor n/2\rfloor-2}
\]
translated networks using pairwise disjoint collections of noise variables. Their success events are independent. Consequently, for any fixed prescribed word \(w\), of either type,
\[
\Pr(w\text{ is not realized})
\le (1-\beta_A^2)^M
\le \exp\!\left[-\frac{\beta_A^2}{4}2^{\lfloor n/2\rfloor}\right].
\]
A union bound over the \(2^n\) direction-indexed words and \(2^n\) chronological words yields (SPU1), with \(b_A=\beta_A^2/4\). \(\square\)

**Corollary (vanishing-relative-distance full-profile completion).** For every legal \(c_0\) on \(Q_n\), there exists a legal coloring \(c_1\) that realizes every direction-indexed and every positional color word on a full antipodal geodesic and differs from \(c_0\) on at most
\[
\boxed{
(6e+o(1))\,2^{n-2}
}
\tag{SPU2}
\]
antipodal edge-pair variables, uniformly in \(c_0\) as \(n\to\infty\). Since there are \(n2^{n-2}\) such variables, this is at most a \((6e+o(1))/n\) fraction of the legal-coloring variables.

*Proof.* Take \(A_n=6e+1/\log n\) and \(\rho_n=A_n/n\). The above proof remains valid with \(\beta_n=\Theta(1/\log n)\): its failure estimate is at most
\[
2^{n+1}\exp\!\left[-\Omega\!\left(2^{\lfloor n/2\rfloor}/(\log n)^2\right)\right]=o(1).
\]
The total number \(X\) of flipped antipodal edge-pair variables is binomial with parameters \(n2^{n-2}\) and \(A_n/n\), hence mean \(\mu_n=A_n2^{n-2}\). A standard binomial Chernoff bound with relative error \(1/\log n\) shows
\[
\Pr\{X>(1+1/\log n)\mu_n\}=o(1),
\]
since \(\mu_n/(\log n)^2\to\infty\). Both full-profile universality and this flip-count bound therefore occur simultaneously with positive probability, giving (SPU2). \(\square\)

**Scope and limitation.** The result is valid for arbitrary nonlinear direction functions and any initial legal coloring. It is a deterministic metric-density consequence of the existing random-face and translated-block theorems, strengthened to simultaneous *full* profile surjectivity. The \(o(1)\) relative perturbation does **not** prove unrestricted NORI1: a bad coloring, if one exists, could lie immediately adjacent to successful colorings in edge-pair Hamming distance. The theorem instead establishes that the full-profile-surjective legal colorings form a vanishing-relative-radius covering family in the ambient legal-coloring Boolean cube.


## Hereditary profile universality on every moderately large face

The preceding sparse-noise theorem can be made simultaneous over exponentially many faces. For a face \(F\subseteq Q_n\), let \(m=\dim F\). Regard the restriction of a full-cube legal coloring to \(F\) as an ordinary binary coloring of the \(m\)-cube; it need not be antipodally odd relative to the face's own antipodal map. Let \(\mathcal W_{\rm dir}(F)\subseteq\mathbb F_2^{\operatorname{free}(F)}\) be its full face-geodesic profiles indexed by free directions, and \(\mathcal W_{\rm pos}(F)\subseteq\mathbb F_2^m\) its consecutive face-geodesic color words, with arbitrary starting face corner and free direction order.

**Theorem (simultaneous universality on all large faces).** Fix \(A>6e\). Let \(m_0=m_0(n)\) be integers with \(m_0\to\infty\), \(m_0\le n\), and set \(\rho=A/m_0\le1/2\) for large \(n\). From any legal antipodally odd coloring \(c_0\) of \(Q_n\), independently flip each full-cube antipodal edge-pair color variable with probability \(\rho\), producing \(c\). There exists \(b_A>0\) such that
\[
\boxed{
\Pr\!\left(
\exists\,F\subseteq Q_n,\ \dim F\ge m_0:
\ \mathcal W_{\rm dir}(F)\ne\mathbb F_2^{\operatorname{free}(F)}
\text{ or }\mathcal W_{\rm pos}(F)\ne\mathbb F_2^{\dim F}
\right)
\le
2\cdot6^n\exp\!\bigl(-b_A\,2^{\lfloor m_0/2\rfloor}\bigr).
}
\tag{HPS1}
\]
The estimate is uniform in \(c_0\).

*Proof.* Fix a face \(F\) of dimension \(m\ge m_0\) and one prescribed free-direction-indexed profile or chronological word of length \(m\). Divide the \(m\) free directions into two blocks of sizes \(\lfloor m/2\rfloor,\lceil m/2\rceil\). The existing arbitrary-face smoothing estimate applies to each block face. For each required color pattern, the event that any particular edge matches its assigned color has probability at least \(\rho\). The pertinent noise variables on a proper subface are independent because no two edges of a proper full-cube face can be antipodal. The block success probability is at least \(1-3e(\rho^{-1}-1)/\lfloor m/2\rfloor\), which for all sufficiently large \(m_0\) is bounded below by a fixed \(\beta_A>0\), since \(\rho m\ge A>6e\). (For example take \(\beta_A=(1-6e/A)/2\).) Different direction blocks use disjoint edge-orbit variables and their geodesics concatenate into the prescribed full face profile or word.

Translate the two-block network by all \(2^m\) translations within \(F\). Two translated networks can share an antipodal edge orbit only through the same direction block \(I_j\), and then their translation difference must be all-zero or all-one outside \(I_j\). There are at most \(2^{|I_j|+1}\) such differences. Greedy packing therefore supplies at least \(2^{\lfloor m/2\rfloor-2}\) networks using pairwise disjoint full-cube edge-orbit variables. Their successes are independent, each with probability at least \(\beta_A^2\). Thus the prescribed profile or word is absent from \(F\) with probability at most
\[
\exp\!\left(-\frac{\beta_A^2}{4}2^{\lfloor m/2\rfloor}\right)
\le \exp\!\left(-b_A2^{\lfloor m_0/2\rfloor}\right),
\]
where \(b_A=\beta_A^2/4\). Union-bound over at most \(2^{m+1}\le2^{n+1}\) prescribed profile and positional words for each face. The number of all nonempty cube faces is \(\sum_{m=0}^n\binom nm2^{n-m}=3^n\). The resulting estimate is (HPS1). \(\square\)

**Corollary (logarithmic face-size saturation under vanishing-density perturbation).** Fix \(\epsilon>0\) and \(A>6e\), put
\[
m_0=\left\lceil(2+\epsilon)\log_2 n\right\rceil,\qquad \rho=A/m_0.
\]
Then with probability \(1-o(1)\), **every face of dimension at least \(m_0\)** realizes every free-direction color profile and every positional color word on some full face-geodesic, uniformly in the baseline coloring. Only an \(O(1/\log n)\) fraction of the full-cube edge-pair variables are changed in expectation, and with high probability their fraction is \((A+o(1))/m_0\).

*Proof.* With this \(m_0\), \(2^{\lfloor m_0/2\rfloor}=\Omega(n^{1+\epsilon/2})\), so (HPS1) tends to zero. The number of independent edge-pair variables is \(n2^{n-2}\), and the flip count is binomial of mean \(\rho n2^{n-2}\); Chernoff concentration gives the stated fraction. \(\square\)

**Corollary (macroscopic face saturation after \(O(1/n)\) noise).** Fix \(\alpha\in(0,1]\) and \(B>6e/\alpha\). Under full-cube noise rate \(\rho=B/n\), with probability \(1-\exp[-\Omega(2^{\alpha n/2})]\), every face of dimension at least \(\alpha n\) realizes all its direction-indexed full-geodesic profiles and all its chronological color words.

*Proof.* Set \(m_0=\lceil\alpha n\rceil\) and \(A=\rho m_0\), bounded away from \(6e\) for large \(n\). Apply (HPS1), absorbing the factor \(2\cdot6^n\) into the doubly exponential failure bound. \(\square\)

These are *free-root* statements: for each face and each pattern the starting corner may depend on the face, pattern and perturbed coloring. They do not assert rooted profile surjectivity for every corner, which is obstructed at bounded \(\rho m\) by the sharp rooted noise threshold. In particular hereditary random smoothing does not establish the zero-perturbation deterministic NORI1 conjecture.


## Robust simultaneous profile certificates after sparse noise

The preceding independent translated block networks provide a packing theorem, not merely existence. Two geodesics are *edge-orbit-disjoint* if no undirected edge of one equals an edge of the other or its full-cube antipodal translate. The witnesses below may depend on the prescribed direction profile or chronological word.

**Theorem (exponentially robust full-profile surjectivity).** Fix \(A>6e\), and set \(\rho=A/n\) in the antipodal edge-orbit noise model on \(Q_n\), starting from any legal coloring \(c_0\). There exist constants \(\gamma_A,b_A>0\), depending only on \(A\), such that with probability at least
\[
\boxed{1-2^{n+1}\exp(-b_A2^{\lfloor n/2\rfloor})}
\tag{RPC1}
\]
the perturbed legal coloring \(c\) has the following property *simultaneously* for every \(w\in\mathbb F_2^n\):

- at least \(\lfloor\gamma_A2^{\lfloor n/2\rfloor}\rfloor\) pairwise edge-orbit-disjoint full antipodal geodesics have **direction-indexed** color profile \(w\);
- at least the same number of pairwise edge-orbit-disjoint full antipodal geodesics have **chronological** color word \(w\).

Consequently the full direction-profile set and the full chronological-word set both remain all of \(\mathbb F_2^n\) after **any** further modification of fewer than \(\lfloor\gamma_A2^{\lfloor n/2\rfloor}\rfloor\) antipodal edge-pair variables.

For instance put \(\beta_A=(1-6e/A)/2>0\). For all sufficiently large \(n\) one can take
\[
\gamma_A=\beta_A^2/8,\qquad b_A=\beta_A^2/32.
\tag{RPC2}
\]

*Proof.* Use the same two direction blocks and greedily packed translated networks as in (SPU1). There are at least \(M=2^{\lfloor n/2\rfloor-2}\) networks with pairwise disjoint underlying edge-orbit-variable sets. For any fixed target \(w\), whether direction-indexed or chronological, each network succeeds with probability at least \(p=\beta_A^2\). These Bernoulli events are independent because their underlying variable sets are disjoint. Their sum stochastically dominates \(\operatorname{Bin}(M,p)\). The lower-tail Chernoff inequality gives
\[
\Pr\{\text{fewer than }pM/2\text{ successful networks}\}
\le \exp(-pM/8)
\le\exp\!\left[-(\beta_A^2/32)\,2^{\lfloor n/2\rfloor}\right].
\]
Every successful network supplies a full antipodal geodesic with the prescribed profile or word. Since the underlying network orbit supports are pairwise disjoint, these geodesics are edge-orbit-disjoint. The bound \(pM/2\ge\gamma_A2^{\lfloor n/2\rfloor}\) proves the packing claim. Apply a union bound over \(2^n\) targets of each of the two types to get (RPC1).

Now alter fewer than \(K=\lfloor\gamma_A2^{\lfloor n/2\rfloor}\rfloor\) antipodal edge-pair variables arbitrarily. For any fixed target, at most that many of its \(K\) orbit-disjoint geodesics can have an edge affected; hence at least one geodesic of each target type and each word survives. The same set of adversarial alterations is permitted for every word simultaneously. \(\square\)

**Theorem (robust hereditary face saturation).** Fix \(A>6e\) and integers \(m_0=m_0(n)\to\infty\), \(m_0\le n\), and perturb with \(\rho=A/m_0\). With probability at least
\[
\boxed{1-2\cdot6^n\exp(-b_A2^{\lfloor m_0/2\rfloor})}
\tag{RPC3}
\]
every face \(F\subseteq Q_n\) of dimension \(m\ge m_0\) simultaneously possesses, for every prescribed free-direction profile and every positional color word, at least
\[
\boxed{K_m=\left\lfloor\gamma_A2^{\lfloor m/2\rfloor}\right\rfloor}
\tag{RPC4}
\]
pairwise full-cube-edge-orbit-disjoint full geodesics *inside \(F\)* realizing the target. The property for all such faces persists after arbitrary modifications of fewer than
\[
\boxed{K_{m_0}=\left\lfloor\gamma_A2^{\lfloor m_0/2\rfloor}\right\rfloor}
\tag{RPC5}
\]
full-cube antipodal edge-pair variables.

*Proof.* For each face \(F\) of dimension \(m\ge m_0\), apply the preceding two-block packing and binomial lower-tail argument using translations only within \(F\). The proper block faces have the requisite independent edge-orbit variables, and each block-face success probability is at least \(\beta_A\) because \(\rho m\ge A>6e\). This provides at least \(K_m\) orbit-disjoint witnesses for each of its \(2^{m+1}\) target conditions, except with probability at most \(2^{m+1}\exp(-b_A2^{\lfloor m/2\rfloor})\). Sum over the at most \(3^n\) faces of \(Q_n\) and use \(m\le n\) and \(m\ge m_0\), obtaining (RPC3). Any \(K_{m_0}-1\) adversarial orbit flips can destroy at most that number of the disjoint witness geodesics for any particular face and target; at least one remains for every condition. \(\square\)

**Corollary (robust logarithmic-scale universality).** For each fixed \(\epsilon>0\), take \(m_0=\lceil(2+\epsilon)\log_2n\rceil\) and perturb with \(\rho=A/m_0\), \(A>6e\). With probability \(1-o(1)\), every face of dimension at least \(m_0\) is direction-profile and positional-word universal, and this remains true after any additional \(o(n^{1+\epsilon/2})\) edge-pair flips bounded by \(K_{m_0}-1=\Theta(n^{1+\epsilon/2})\). The initial perturbation changes an \(O(1/\log n)\) fraction of all legal edge-pair variables with high probability.

*Proof.* The hereditary failure bound tends to zero because \(2^{m_0/2}=\Omega(n^{1+\epsilon/2})\gg n\). The packing lower bound is of order \(2^{m_0/2}\), and the perturbation size follows from binomial concentration. \(\square\)

This converts sparse-noise **existence** into simultaneous quantitative *adversarial robustness*, directly linking random face smoothing to the orbit-disjoint path-packing program. The deterministic conjecture at zero noise remains open; this result cannot be specialized to \(\rho=0\).
