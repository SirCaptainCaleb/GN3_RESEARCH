# Polynomial monochromatic geodesics from sparse triplewise exterior support

# Long monochromatic NORI3 geodesics under sparse triplewise exterior dependence

## Theorem

Let \(V\) be the \(n\) coordinate directions of \(Q_n\). Let \(c(F,(a,b,c))\in\{0,1\}\) color *physical ordered three-faces*. Assume **same-face reversal oddness**
\[
c(F,(a,b,c))=1-c(F,(c,b,a))
\tag{R}
\]
for every ordered physical face. For each unordered triple \(T\subset V\), suppose there exists a set of exterior coordinates \(S_T\subset V\setminus T\) of size at most \(d\), such that all six ordered-face colors with free set \(T\) depend only on their free-direction order and the fixed bits on \(S_T\). These support sets are allowed to vary arbitrarily with \(T\).

**Theorem (sparse exterior-support boundary-snake transfer).** For \(1\le d\le n-3\), as \(n/d\to\infty\), the coloring has a monochromatic *genuine coordinate-distinct geodesic* of length
\[
\boxed{\Omega((n/d)^{1/3})}.
\tag{1}
\]
The explicit estimate \(L_{\max}(c)\ge1+(n/d)^{1/3}/2100\) holds whenever \(n/d\ge32^{3/2}\).

If \(d=0\), then \(c\) is direction-only, and the full Devine–Milans boundary-tournament snake theorem gives
\[
L_{\max}(c)\ge1+\sqrt{(n-1)/2}.
\tag{2}
\]
If all ordinary triples outside a *common* set \(S\) of \(t\) directions depend only on their exterior bits in \(S\), the same theorem directly yields
\[
L_{\max}(c)\ge1+\sqrt{(n-t-1)/2}\quad(n-t\ge3).
\tag{3}
\]

Condition (R) is exactly the additional same-face reversal symmetry proposed for **boundary-compatible NORI3**. When the ordinary NORI law \(c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi)\) also holds, (R) is equivalent to the additional antipodal invariance \(c(\bar F,\pi)=c(F,\pi)\). No antipodal hypothesis beyond (R) is needed for the theorem.

## Lemma: robust boundary snake with selectively discarded terminal pairs

A **partial boundary 3-tournament** on \(N\) vertices has a set of available unordered triples. For every available triple, exactly one ordering of each same-middle reversal pair is a positive directed triple; unavailable triples have no positive orderings. For an unordered pair \(e=\{u,v\}\), let \(b(e)\) be the number of unavailable triples containing \(e\). Fix \(b\ge0\), call \(e\) *clean* when \(b(e)\le b\), and let
\[
\alpha=\frac{\#\{\mathrm{clean\ unordered\ pairs}\}}{\binom N2}.
\]
If \(L\ge2\) is the maximum vertex order of a vertex-simple positive directed tight path, then
\[
\boxed{\alpha\frac{N-1}{2}\le(L-1)^2+b(L-1).}
\tag{4}
\]

**Proof.** For each *clean* unordered pair \(\{u,v\}\), find a longest positive directed tight path ending either in \(uv\) or in \(vu\), giving a terminal order \(r(\{u,v\})\in[2,L]\). Orient the pair toward the endpoint of the chosen path, breaking ties arbitrarily. Orienting only the clean pairs produces a partial tournament on the \(N\) vertices with \(\alpha\binom N2\) arcs. Hence some vertex \(v\) has at least \(\alpha(N-1)/2\) incoming clean pairs.

For \(r=2,\ldots,L\), let \(U_r\) be its incoming clean neighbors having terminal order \(r\), and put \(q=|U_r|\). For distinct \(u,w\in U_r\), whenever \(\{u,v,w\}\) is available, direct the comparison \(u\to w\) precisely when \((u,v,w)\) is positive. Same-middle reversal oddness makes this a partial tournament. Since the terminal pair \(\{u,v\}\) is clean for every \(u\in U_r\), each \(u\) participates in at most \(b\) missing comparisons. The induced comparison tournament therefore has at most \(bq/2\) missing edges, and some \(u\in U_r\) has outdegree at least \((q-1-b)/2\).

Take a longest positive \(r\)-vertex path \(P\) ending \(uv\). Each outneighbor \(w\) in the comparison tournament must already belong to \(P\), or \((u,v,w)\) extends \(P\) to a positive \((r+1)\)-vertex path ending \(vw\), contradicting that the clean pair \(\{v,w\}\) is oriented \(w\to v\) and has terminal order exactly \(r\). There are at most \(r-2\) such outneighbors. Thus \(q\le2r+b-3\), and
\[
\alpha(N-1)/2\le\sum_{r=2}^L|U_r|
\le \sum_{r=2}^L(2r+b-3)
=(L-1)^2+b(L-1).
\]
This proves (4). The positive tight path is *vertex-simple in the original \(N\)-vertex hypergraph*, not merely a directed path in a line graph. \(\square\)

When \(b=0,\alpha=1\), (4) recovers the scrapbook's \(L\ge1+\sqrt{(N-1)/2}\). This robust version is useful even when many triples are unavailable, provided most terminal pairs have few unavailable extensions.

## Random extraction: retain good triples and clean pairs

Assume \(d\ge1\). Choose each original direction independently with probability
\[
p=(d^2n)^{-1/3},\qquad \mu=np=(n/d)^{2/3}.
\]
Let \(X\) be the selected direction set, of size \(N\). Call \(T\subseteq X\) **bad** if \(S_T\cap X\ne\varnothing\), and let \(B(X)\) count bad unordered triples. Every bad triple is witnessed by a four-element inclusion \(T\cup\{u\}\subseteq X\) for some \(u\in S_T\). By linearity of expectation,
\[
\mathbb E B(X)\le d\binom n3p^4
\le\frac16\mu^{5/2}.
\tag{5}
\]
Markov gives \(\Pr(B(X)>\mu^{5/2})\le1/6\), and Chernoff gives \(\Pr(N<\mu/2)\le e^{-\mu/8}<1/6\) whenever \(\mu\ge32\). Consequently some \(X\) satisfies
\[
N\ge\mu/2,\qquad B(X)\le\mu^{5/2}.
\tag{6}
\]

Construct a partial boundary tournament on \(X\) by declaring each *good* unordered triple \(T\) (those with \(S_T\cap X=\varnothing\)) available. Define its orientations using one fixed exterior cube root \(x_0\), as explained below; (R) guarantees exactly one orientation in each reversal pair. For each unordered pair \(\{u,v\}\subseteq X\), let \(b(\{u,v\})\) count bad triples containing it. Since each bad triple contributes to exactly three unordered pairs,
\[
\sum_{\{u,v\}\subset X}b(\{u,v\})=3B(X).
\]
Choose the clean-pair threshold \(b=128\sqrt\mu\). There are at most \(3\mu^2/128\) dirty pairs. Because \(N\ge\mu/2\ge16\),
\[
\binom N2\ge N^2/4\ge\mu^2/16.
\]
Therefore dirty pairs constitute at most \(3/8\) of all pairs, and the clean proportion obeys \(\alpha\ge5/8\). Lemma (4) implies
\[
\frac{N-1}{4}\le(L-1)^2+128\sqrt\mu(L-1).
\tag{7}
\]
Put \(z=L-1\). If \(z\ge\sqrt\mu\), the claimed bound follows. Otherwise \(z^2\le z\sqrt\mu\), and \(N\ge\mu/2\), \(\mu\ge32\) imply
\[
\mu/16\le(N-1)/4\le129z\sqrt\mu,
\qquad z\ge\sqrt\mu/2064>\sqrt\mu/2100.
\]
Since \(\sqrt\mu=(n/d)^{1/3}\), this proves the explicit estimate in (1).

## Exact physical-fiber realization and root consistency

Fix a single cube vertex \(x_0\in Q_n\) BEFORE orienting any available triple. For every good triple \(T\subseteq X\), the support \(S_T\) lies outside \(X\), so none of its influential fixed exterior bits ever changes along *any* cube path using directions from \(X\). Thus for every ordering \(\pi\) of \(T\), all actual physical faces with free directions \(T\) encountered by such paths have exactly the color determined by \(\pi\) and \(x_0|_{S_T}\), regardless of other exterior-coordinate bits. This defines one direction-only same-face reversal-odd tournament chart on the good triples. Omit the bad triples altogether.

By the robust snake lemma, there is a positive directed tight path \(u_1,\ldots,u_L\) of DISTINCT vertices/directions using only good triples. Starting at \(x_0\), traverse the actual cube coordinates in this order. The resulting cube path is a genuine direction-distinct geodesic; its successive physical ordered 3-faces have the precisely matched good-triple colors and are all positive. There is no incompatible-root transfer, no abstract physical-face substitution, and no repeated cube direction.

For \(d=0\), take \(X=V\) and apply the complete Devine–Milans snake theorem. For a common exterior support \(S\), choose \(X=V\setminus S\), freeze \(S\)-bits at \(x_0\), and apply the complete theorem on \(n-t\) directions. This proves (2)–(3). \(\square\)

## Consequences, prior improvements, and boundary of applicability

This resolves a nontrivial intermediate structural class: **polynomial-length monochromatic paths survive both same-face reversal oddness and arbitrary triple-specific exterior interactions of bounded support**, even though no global exterior support is available. The earlier hypergraph-independent-set proof supplied only exponent \(1/6\). A first robust snake bound controlling missing triples per vertex improved it to \(1/4\). The selective-terminal-pair lemma above gives the current strongest exponent \(1/3\), making the earlier arguments valid but superseded.

For legal boundary-compatible NORI3, complement invariance implies that a face color depending on at most ONE exterior bit cannot genuinely depend on that bit; such colorings are direction-only, so (2) holds for \(d\le1\). Genuine nonconstant complement-invariant dependencies first appear with \(d\ge2\). In unrestricted boundary-compatible NORI3, a triple can depend on \(\Theta(n)\) exterior bits, where (1) gives no growing bound. Likewise this does not settle unrestricted NORI3's universal \(\Omega(\log n)\) question: the antichain and self-dual constructions avoiding that structural hypothesis have \(O(\log n)\) maximum monochromatic geodesics. The problem of improving the exponent \(1/3\) within the sparse-support class is separately open; no sharpness claim is made.

**Source attribution.** The complete boundary-tournament \(1+\sqrt{(N-1)/2}\) terminal-pair bound is from R. C. Devine and K. G. Milans, *Tight paths in fully directed hypergraphs*, the supplied scrapbook, sections “Antisymmetric Tournaments” and “Boundary Tournaments.” The partial-tournament clean-pair lemma, probabilistic extraction, and physical-face transfer giving exponent \(1/3\) above are new to this manuscript.
