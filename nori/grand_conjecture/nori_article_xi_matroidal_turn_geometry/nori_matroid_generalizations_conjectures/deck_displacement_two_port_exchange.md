# Deck-displacement two-port exchange

Let \(\widetilde G\to G\) be a connected regular two-sheeted cover of finite simple graphs, with free deck involution \(\tau\). Assume every vertex of \(G\) has degree at least three and
\[
\delta=\min_{x\in V(\widetilde G)}\operatorname{dist}_{\widetilde G}(x,\tau x)\ge3.
\]
Put \(H=L(G)\), let \(\alpha\in H^1(H;\mathbb F_2)\) be the monodromy class of the induced line-graph cover, let \(\kappa\) be the canonical line-graph contact-curvature class, and put \(\lambda=\alpha+\kappa\). Define the bipointed binary matroid
\[
D^{(2)}=M\!\left(\begin{array}{c|cc}B_H&0&0\\
a&1&0\\\lambda&0&1\end{array}\right)^*,
\]
with distinguished monodromy port \(p\) and curvature port \(q\).

**Theorem 1 (universal deck-displacement sector exchange).** Both the least cocircuit size in the sector containing \(p,q\) and the least cocircuit size in the sector containing \(p\) but avoiding \(q\) equal \(\delta+2\). For every admissible deck-odd coloring, with color cycle \(X_d=\operatorname{supp}(d)\cup\{p\}\),
\[
\boxed{\min_{\substack{Y\in\mathcal C^*(D^{(2)})\\p,q\in Y,\ |Y|=\delta+2}}|X_d\cap Y|
=\min_{\substack{Y\in\mathcal C^*(D^{(2)})\\p\in Y,\ q\notin Y,\ |Y|=\delta+2}}|X_d\cap Y|.}
\tag{1}
\]

*Proof.* Let \(C\) be a simple cycle of \(H\) with monodromy one, of length \(r\), and let \(s(C)\) count stationary contacts of its lifted cyclic edge-state walk. Removing the stationary contacts gives a walk in \(\widetilde G\) from some vertex \(x\) to its deck mate \(\tau x\) using \(r-s(C)\) edges, so
\[
r-s(C)\ge\delta,\qquad \lambda(C)\equiv1+s(C)\pmod2.
\tag{2}
\]
Choose a shortest \(x\)-to-\(\tau x\) path of length \(\delta\), with \(x\) chosen to minimize that distance globally. Its projected edge-state orbits are pairwise distinct: if two path edges were deck mates, their intervening subpath would provide a shorter path joining a vertex to its mate, contrary to the choice of \(\delta\). Its projected base-vertex orbits have no repetitions except the terminal identification, by the same argument and ordinary path simplicity. The \(\delta\) cyclic turns of its edge states therefore give a simple monodromy-one turn cycle of length \(\delta\), without stationary contacts. Its orientation-port phase is \(\lambda=1\), and adjoining \(p,q\) gives a cocircuit of cardinality \(\delta+2\), minimal by (2).

In the sector \(\lambda=0\), equation (2) forces \(s(C)\) odd and at least one; therefore \(r\ge\delta+1\), giving the same size lower bound for a cocircuit with port \(p\) alone. The shortest turn cycle has odd color-turn weight (because its monodromy is one), hence contains a changed turn. That turn belongs to a star clique whose underlying base-graph vertex has degree at least three. Since a shortest deck-geodesic uses only its two consecutive edge states at that base vertex, a third, unused state \(b\) is available. Replacing the changed turn \(va\) by \(v-b-a\) gives a simple cycle of length \(\delta+1\), with the same monodromy, opposite curvature parity, and the same integer turn cost, since the two new binary turn labels sum to one. Its associated p-only cocircuit has size \(\delta+2\).

Conversely, every p-only cocircuit of size \(\delta+2\) has a turn cycle of length \(r=\delta+1\), and by (2) its stationary count is necessarily \(s=1\). Contracting that single stationary contact by the balanced star-triangle shortcut produces a length-\(\delta\) simple odd-monodromy cycle whose integer cost does not exceed the original. This gives both inequalities between the minimum intersection costs and proves (1). \(\square\)

For the antipodal cover \(Q_n\to Q_n/\tau\), \(\delta=n\). For the ordered-pair cover \(S_n\to L(K_n)\) of ordinary boundary 3-tournaments, \(\delta=3\). The latter gives a theorem about short, five-element cocircuits, not a long forward vertex-simple tight-path guarantee.

**Corollary 2 (regular-cover stochastic domination).** If \(G\) is \(m\)-regular, the unique-stationary-contact contraction maps the \(p\)-only cocircuits of size \(\delta+2\) onto the both-port cocircuits of the same size, with \(\delta(m-2)\) children per parent. For a uniformly chosen both-port cocircuit \(A\) and a uniformly chosen \(p\)-only cocircuit \(B\), there is a coupling such that, for every admissible color cycle \(X_d\),
\[
\boxed{|X_d\cap A|\le |X_d\cap B|\le |X_d\cap A|+2.}
\tag{3}
\]
Consequently, for every integer \(u\),
\[
\boxed{\Pr(|X_d\cap A|\le u-2)\le
\Pr(|X_d\cap B|\le u)\le
\Pr(|X_d\cap A|\le u).}
\tag{4}
\]

*Proof.* Every shortest deck-geodesic meets each base-vertex star along its \(\delta\) cyclic turns using two incident edge-state orbits. Each turn has \(m-2\) unused states available for stationary insertion. Each child has a unique parent because it has one stationary contact; uniform sampling of the \(\delta(m-2)\) children per parent therefore gives a uniform parent. Replacing one turn by two turns either preserves the integer disagreement count or increases it by two. Adding the prescribed ports leaves total cocircuit cardinality fixed, proving (3) and (4). \(\square\)

**Necessity of the degree requirement.** For the connected antipodal two-cover \(C_{2\delta}\to C_\delta\), \(\delta\ge3\), the base has degree two. Its line graph is a cycle with one odd-monodromy turn cycle, of length \(\delta\) and no stationary contact. The both-port sector has a size-\(\delta+2\) cocircuit, but the \(p\)-only sector has none. Thus the hypothesis of minimum base degree at least three cannot be removed from Theorem 1.

## Boundary-tournament two-class conservation

Take the connected ordered-pair cover \(S_n\to L(K_n)\), for \(n\ge4\), and put \(h=n-2\). Its quotient base graph \(G=L(K_n)\) has degree \(2h\). The shortest monodromy-odd turn cycles have length \(\delta=3\). They correspond to the triangles of \(L(K_n)\) formed by three edges of \(K_n\) sharing a common vertex, and their number is
\[
\boxed{N=n\binom{n-1}{3}=\frac{n(n-1)h(h-1)}6.}\tag{5}
\]
The unique-stationary-contact map gives \(3(2h-2)N\) \(p\)-only cocircuits of size five.

At a vertex \(x=\{u,v\}\) of \(G=L(K_n)\), the \(2h\) incident edges split into two classes of size \(h\), according to whether their original \(K_n\) edges meet \(\{u,v\}\) at \(u\) or at \(v\). Fix a lifted star and let \(a_x,b_x\) be the numbers of color-one states in these two classes.

**Theorem 3 (boundary two-class conservation law).** For an arbitrary reversal-odd boundary coloring, the number of stationary-contact children whose integer turn cost is two greater than that of their shortest parent is
\[
\boxed{\sum_{x=\{u,v\}} M_h(a_x,b_x),}\tag{6}
\]
where
\[
\begin{aligned}
M_h(a,b)&=\left[\binom a2+\binom b2\right](2h-a-b)
+\left[\binom{h-a}2+\binom{h-b}2\right](a+b)\\
&=\frac{h-2}{2}(a+b)(2h-a-b)+\frac h2(a-b)^2.
\end{aligned}\tag{7}
\]
Consequently the proportion of cost-preserving children is
\[
\boxed{1-\frac{\sum_xM_h(a_x,b_x)}{3(2h-2)n\binom{n-1}{3}}.}\tag{8}
\]

*Proof.* An odd-monodromy three-cycle of the quotient turn graph corresponds to three original complete-graph edges incident at one vertex. At a fixed base vertex \(x=\{u,v\}\) of \(L(K_n)\), a local turn belongs to such a cycle if and only if its two incident edges arise from original edges meeting the same endpoint of \(\{u,v\}\). For each same-class pair, the third original edge of the triangle is determined, so its incidence multiplicity is one; cross-class pairs have multiplicity zero. For a same-colored class pair, a stationary insertion adds two disagreements precisely when the third inserted edge state is opposite-colored. There are \(a+b\) color-one states and \(2h-a-b\) color-zero states in the whole star. Counting equal-color pairs within each of the two classes, and then their opposite-colored insertion states, yields the first expression in (7). Algebraic expansion gives the second expression. Each such insertion yields a distinct stationary-contact child with a unique parent. Summing over all quotient base vertices gives (6), and dividing by the uniform child count \(3(2h-2)N\) proves (8). \(\square\)

This is an association-class counterpart to the constant pair-incidence formula for cubelike 2-designs. The extra statistic \((a_x-b_x)^2\) records how the two local endpoint-port classes correlate with the coloring. The theorem concerns the full-turn boundary matroid's shortest cocircuits; it does not guarantee a long, coherent, vertex-simple tight path.
