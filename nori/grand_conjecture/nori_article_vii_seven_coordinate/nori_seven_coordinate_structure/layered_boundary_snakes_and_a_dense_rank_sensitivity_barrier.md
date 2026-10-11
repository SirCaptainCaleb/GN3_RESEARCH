# Layered boundary snakes and a dense rank-sensitivity barrier

# Layered boundary snakes and the dense rank-sensitivity barrier

## Main abstract theorem: one boundary tournament per step

Let \(V\) be an \(n\)-element set. For every \(j\ge0\), choose **arbitrary**, possibly unrelated functions \(h_j(a,b,c)\in\{0,1\}\) on distinct ordered triples satisfying same-middle reversal oddness \(h_j(c,b,a)=1-h_j(a,b,c)\). Then there exist \(L\ge1+\sqrt{(n-1)/2}\) **distinct** vertices \(v_1,\ldots,v_L\) with \(h_{i-1}(v_i,v_{i+1},v_{i+2})=1\) for all \(1\le i\le L-2\).

**Proof (correct step indexing).** Define a positive \(r\)-vertex path by requiring its triple at starting position \(i\) to be positive in \(h_{i-1}\). A two-vertex path is positive vacuously. For every unordered pair \(e=\{u,v\}\), select a longest such simple path ending either \(u,v\) or \(v,u\); write \(r(e)\in[2,L]\) for its maximum order and orient \(e\) toward its selected terminal vertex. This makes a tournament on \(V\). Choose \(v\) with incoming degree at least \((n-1)/2\). Let \(U_r\) be its incoming neighbors \(u\to v\) with \(r(\{u,v\})=r\), and put \(q=|U_r|\).

For \(u,w\in U_r\), orient \(u\to w\) iff \(h_{r-2}(u,v,w)=1\). (Appending to an \(r\)-vertex path creates the triple at window **position \(r-1\)**, which is evaluated by \(h_{r-2}\), not \(h_{r-1}\).) Reversal oddness makes this a tournament. Pick \(u\) with at least \((q-1)/2\) outneighbors, and a positive longest path ending \(u,v\) of order \(r\). Every such outneighbor \(w\) is already among the first \(r-2\) vertices of that path: otherwise append \(w\), obtaining an \((r+1)\)-vertex positive path ending \(v,w\), contradicting \(r(\{v,w\})=r\) with selected orientation \(w\to v\). Therefore \(q\le 2r-3\). Summing over \(r=2,\ldots,L\),
\[
(n-1)/2\le \sum_r |U_r|\le\sum_{r=2}^{L}(2r-3)=(L-1)^2.
\]
This proves the theorem; the resulting path is vertex-simple in \(V\), not merely a walk in the terminal-pair graph.

## Physical face transfer: all exterior bits may matter

Let \(c(F,\pi)\) color physical ordered 3-faces of \(Q_n\), obeying \(c(F,\operatorname{rev}\pi)=1-c(F,\pi)\). Suppose for each ordered triple \(\pi\) the color depends on the fixed exterior vector only through its **Hamming weight**:
\[
c(F,\pi)=h_{|z(F)|}(\pi).
\tag{1}
\]
The \(h_j\) are arbitrary and reversal-odd, with no bound on exterior support or linearity. Starting a direction-distinct cube geodesic at \(0^n\), its \(i\)-th 3-face window has precisely \(i-1\) exterior 1-bits (its earlier traversed directions). Its actual physical color is therefore \(h_{i-1}(p_i,p_{i+1},p_{i+2})\). The abstract theorem produces a **genuine monochromatic cube geodesic** with at least \(1+\sqrt{(n-1)/2}\) coordinate moves, all directions distinct, using one fixed root. There is no identification of nonmatching physical faces.

For legal NORI3, the combined antipodal-reversal law and separate same-face reversal oddness amount to antipodal invariance \(c(\bar F,\pi)=c(F,\pi)\). In (1) this holds precisely when \(h_j(\pi)=h_{n-3-j}(\pi)\). This defines a substantial subclass of boundary-compatible NORI3 allowing arbitrary nonlinear dependence on all \(n-3\) exterior coordinates. The sparse-triplewise-support theorem cannot address this subclass when the essential exterior support is full.

## Partial layered tournament and selective terminal-pair robustness

For \(j\in\{0,\ldots,n-3\}\), call an unordered direction triple \(T\) *rank-flat at layer \(j\)* if, for all six orderings of \(T\), the physical ordered-face color is identical over all exterior assignments with exactly \(j\) ones. Write \(B_j\) for the family of triples that are **not** rank-flat at layer \(j\). On rank-flat triples, define the constant chart \(h_j\); due to same-face reversal oddness this is a partial boundary tournament. Unavailable triples receive no orientations. For formal use beyond physical layer \(n-3\), extend charts arbitrarily to complete reversal-odd tournaments; no geodesic with distinct directions uses these extra layers.

For an unordered direction pair \(e\), define its maximal *rank-nonflat codegree*
\[
\beta(e)=\max_{0\le j\le n-3}\bigl|\{w\notin e:e\cup\{w\}\in B_j\}\bigr|.
\]
Fix \(b\ge0\). Call \(e\) *clean* if \(\beta(e)\le b\), and let \(\alpha\) be the proportion of clean pairs among all \(\binom n2\) unordered pairs.

**Theorem (selectively pruned layered snake).** If \(L_{\max}(c)\) is the maximum length of a monochromatic direction-distinct cube geodesic, then
\[
\boxed{\alpha\frac{n-1}{2}\le (L_{\max}(c)-1)^2+b(L_{\max}(c)-1).}
\tag{2}
\]
The estimate remains true without imposing antipodal invariance, but requires same-face reversal oddness.

**Proof.** Define positive paths by their consecutive *rank-flat* triples, using chart \(h_{i-1}\) at window starting position \(i\). Every such distinct-direction path is a genuine physical monochromatic cube geodesic when traversed from \(0^n\), because its \(i\)-th window has exterior Hamming weight \(i-1\). Let \(L_+\le L_{\max}(c)\) be their maximum order.

For **clean** unordered terminal pairs \(e\), orient \(e\) by its maximum positive simple terminal-path order \(r(e)\), as in the abstract proof (paths may use dirty pairs elsewhere). The clean-pair graph has \(\alpha\binom n2\) oriented edges, so some vertex \(v\) has at least \(\alpha(n-1)/2\) incoming clean edges. Partition these neighbors into \(U_r\), with \(q=|U_r|\), by maximum terminal-path order \(r\).

For \(u,w\in U_r\), use rank-\(r-2\) chart \(h_{r-2}(u,v,w)\) to orient \(u\to w\) whenever the triple \(\{u,v,w\}\) is rank-flat at that layer. Since each pair \(\{u,v\}\) is clean, it is incident to at most \(b\) missing comparisons at this layer. Thus this partial tournament on \(U_r\) has at least \(q(q-1-b)/2\) arcs, and some \(u\) has outdegree at least \((q-1-b)/2\). As before, each comparison outneighbor must already occur on a longest \(r\)-vertex positive path ending \(u,v\), or appending it contradicts the maximal terminal order of the **clean** pair \(\{v,w\}\). Therefore \(q\le2r+b-3\). Summation yields
\[
\alpha(n-1)/2\le (L_+-1)^2+b(L_+-1)
\le (L_{\max}(c)-1)^2+b(L_{\max}(c)-1).
\]
This proves (2). Setting \(\alpha=1\) yields the explicit robust bound
\[
L_{\max}(c)\ge1+\frac{\sqrt{b^2+2(n-1)}-b}{2}.
\]
In particular \(b=O(\sqrt n)\) still forces \(L_{\max}=\Omega(\sqrt n)\), with arbitrary physical exterior dependence on the exceptional triple faces.

## Consequential obstruction for hypothetical logarithmic boundary-compatible colorings

Rearrange (2):
\[
\boxed{\frac{\#\{e:\beta(e)\le b\}}{\binom n2}
\le \frac{2((L_{\max}-1)^2+b(L_{\max}-1))}{n-1}.}
\tag{3}
\]
If a family of *boundary-compatible* legal physical NORI3 colorings has \(L_{\max}=O(\log n)\), then for **every** threshold \(b(n)=o(n/\log n)\), (3) implies
\[
\#\{e:\beta(e)\le b(n)\}=o(n^2).
\]
In words: for all but \(o(n^2)\) unordered direction pairs \(e\), there must be **some exterior Hamming-weight layer**, potentially depending on \(e\), at which more than \(b(n)\) choices of third direction yield genuinely rank-nonflat physical triples. For instance one may take \(b(n)=n/(\log n\log\log n)\). Thus any logarithmic obstruction preserving boundary tournaments must have **widely distributed identity-sensitive exterior dependence**, rather than merely global dependence on the number of exterior ones or sensitivity concentrated around a few pairs. This necessity does NOT construct such an obstruction or resolve unrestricted boundary-compatible NORI3.

## Several exterior coordinate types

If the directions are partitioned into \(t\) classes and the colors of faces with three free directions in each class depend on exterior bits only through **counts of ones per class**, choose the largest class \(D\), with \(m\ge\lceil n/t\rceil\). A cube geodesic starting at \(0^n\) using only \(D\) leaves other classes at exterior count zero and increases the active class exterior count by one at every triple window. The abstract layer theorem applied to \(D\) gives a genuine monochromatic path of length
\[
\boxed{1+\sqrt{(\lceil n/t\rceil-1)/2}}.
\]
This again permits dependence on arbitrarily many exterior bits.

**Attribution and scope.** The complete boundary-tournament terminal-pair snake bound is the Devine–Milans scrapbook result. The layer-varying extension, the physical rank-homogeneous transfer, the selectively pruned layer-defect inequality, and the dense rank-nonflatness necessity are proved here. The independent sparse-support \(\Omega((n/d)^{1/3})\) result covers a different class. No claim of a universal square-root bound for fully arbitrary physical boundary-compatible NORI3 is made.
