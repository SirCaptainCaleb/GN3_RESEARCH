# Polynomial monochromatic geodesics from sparse triplewise exterior support

# Polynomial monochromatic geodesics from sparse triplewise exterior support

## Theorem and structural significance

Let \(V\) be the \(n\) coordinate directions of \(Q_n\). A binary coloring \(c(F,(a,b,c))\) of **physical ordered three-faces** is *same-face reversal-odd* when
\[
c(F,(a,b,c))=1-c(F,(c,b,a))
\tag{R}
\]
for every physical face and distinct ordered free directions. The boundary-compatible NORI3 class additionally obeys \(c(\bar F,\pi)=c(F,\pi)\); together these are equivalent to the ordinary NORI antipodal-reversal law plus (R).

**Definition (triplewise exterior support).** For each *unordered* direction triple \(T\in\binom V3\), suppose there is an assigned subset \(S_T\subseteq V\setminus T\) such that, for each of the six ordered triples \(\pi\) of \(T\), the physical face color \(c(F,\pi)\) depends only on \(\pi\) and the fixed exterior bits in \(S_T\). The supports \(S_T\) are allowed to differ arbitrarily with \(T\). Assume \(|S_T|\le d\) for every \(T\). In particular, no common small global exterior-support set is required.

**Theorem (sparse-dependency extraction).** Suppose (R) holds and the coloring has triplewise exterior support of size at most \(d\), for \(n\ge4\). If \(d\ge1\), put
\[
p=\min\left\{1,\left(\frac{n}{4d\binom n3}\right)^{1/3}\right\},\qquad
M=\left\lceil\tfrac34np\right\rceil .
\tag{1}
\]
Then some monochromatic direction-distinct cube geodesic has at least
\[
\boxed{1+\sqrt{(M-1)/2}}
\tag{2}
\]
coordinate moves (understood with the usual integral rounding). In particular, whenever \(1\le d=o(n)\) and \(n\to\infty\), the guarantee is
\[
\boxed{L_{\max}(c)=\Omega((n/d)^{1/6})}.
\tag{3}
\]
For \(d=0\), the full direction set is flat and the sharper boundary-tournament guarantee
\[
L_{\max}(c)\ge1+\sqrt{(n-1)/2}
\tag{4}
\]
holds. These results hold even without antipodal invariance; with it, they apply to the proposed boundary-compatible subclass of legal NORI3 colorings.

**Stronger global-support corollary.** If there exists one set \(S\subseteq V\) of \(|S|=t\) whose fixed bits determine all ordered three-face colors whenever the free directions avoid \(S\), and if (R) holds, then there is a monochromatic geodesic on at least
\[
\boxed{1+\sqrt{(n-t-1)/2}}
\tag{5}
\]
distinct directions, for \(n-t\ge3\). This is substantially stronger than the purely two-color logarithmic guarantee under the same exterior-support hypothesis without (R). For a **legal** boundary-compatible coloring with \(|S_T|\le1\), antipodal invariance additionally implies every such one-bit function is constant (because \(f(z)=f(1-z)\)); hence it is direction-only, and (4) applies.

## Proof

**Step 1: Extract a large set of directions with no internal exterior dependencies.**
Build a 4-uniform hypergraph \(\mathcal H\) on \(V\): for every unordered triple \(T\) and \(u\in S_T\), insert the 4-element hyperedge \(T\cup\{u\}\). Its number of hyperedges is at most
\[
B=\sum_{T\in\binom V3}|S_T|\le d\binom n3.
\]
A random \(p\)-subset \(X\subseteq V\) has expected size \(np\) and contains at most \(Bp^4\) hyperedges in expectation. Our choice of \(p\) guarantees \(Bp^4\le np/4\). Consequently some \(X\) satisfies
\[
|X|-|E(\mathcal H[X])|\ge \tfrac34np.
\]
Delete one direction from each hyperedge remaining in \(\mathcal H[X]\), yielding an independent set \(D\subseteq X\) with
\[
|D|\ge M=\lceil3np/4\rceil.
\tag{6}
\]
By independence, \(S_T\cap D=\varnothing\) for every triple \(T\subseteq D\). Equivalently, *none of the exterior coordinates that can affect a three-face entirely supported in \(D\) will ever be traversed by a path using only \(D\)*.

**Step 2: Construct one direction-only boundary tournament in a genuine physical cube fiber.**
Fix *any* cube root \(x\in Q_n\). For any three directions of \(D\), the exterior bits in \(S_T\) remain equal to those of \(x\) under every path using only directions in \(D\), because \(S_T\cap D=\varnothing\). Define
\[
b_x(a,b,c)=c(F,(a,b,c))
\]
for any physical face \(F\) with free set \(\{a,b,c\}\subseteq D\) and fixed \(S_T\)-bits inherited from \(x\). The triplewise exterior-support hypothesis makes this well defined, *independently of every other exterior bit within \(D\)*. Hypothesis (R) gives
\[
b_x(c,b,a)=1-b_x(a,b,c).
\]
Thus \(b_x\) is exactly a **boundary 3-tournament** on \(|D|\) distinct coordinate directions. This construction is valid even though the original coloring may vary nonlinearly with many exterior bits and the sets \(S_T\) are all different.

**Step 3: Apply the snake-digraph terminal-pair theorem and realize its path physically.**
The Devine–Milans antisymmetric boundary-tournament theorem (scrapbook, “Antisymmetric Tournaments” and “Boundary Tournaments”) gives a monochromatic tight path (in its directed-edge convention, color 1) of order at least
\[
1+\sqrt{(|D|-1)/2}\ge1+\sqrt{(M-1)/2}.
\]
Let its distinct direction sequence be \((u_1,\ldots,u_\ell)\subseteq D\). Traverse those directions in that order, starting at the selected cube vertex \(x\). This is a genuine cube geodesic: no direction repeats. At its \(j\)th ordered three-window, all \(S_T\)-bits equal \(x|_{S_T}\) and the **physical ordered face** has color
\[
c(F_j,(u_j,u_{j+1},u_{j+2}))
=b_x(u_j,u_{j+1},u_{j+2})=1.
\]
Thus the entire actual physical cube geodesic is monochromatic. There is no tacit identification of faces from different roots and no need to transport a maximal terminal path between incompatible cube fibers. This proves (2).

For \(d\ge1\), equation (1) simplifies for \(n\ge4\) to \(p^3=3/[2d(n-1)(n-2)]\) (unless capped by 1). Hence \(M=\Omega((n/d)^{1/3})\), and (2) yields (3). When \(d=0\), simply take \(D=V\), proving (4). If a **single common** support \(S\) works for all ordinary triples avoiding \(S\), take \(D=V\setminus S\) directly without random deletion, obtaining (5). \(\square\)

## Relation to existing results and sharp limitations

The established *Sharp logarithmic monochromatic geodesics under bounded exterior support* proves an \(\Omega(\log(n-t))\) lower bound without reversal oddness and has a legal one-sentinel matching construction. **The present theorem has a different, indispensable hypothesis (R)**: for one common exterior support the lower bound improves all the way to \(\Omega(\sqrt{n-t})\); for *different sparse supports per triple* it remains polynomial, \(\Omega((n/d)^{1/6})\). It therefore identifies a concrete quantitative joint role for local reversal antisymmetry and sparse exterior dependence. It does not settle the fully unrestricted boundary-compatible class, where the support of one direction triple can have size \(\Theta(n)\).

The antichain-rank two-sentinel short-path NORI3 construction violates (R) (its two reversed triples can have equal color on the same physical face), and so is not a counterexample. The boundary snake mechanism operates only **after** an independent direction set eliminates all relevant exterior dependencies. Arbitrary globally dependent physical colorings need not admit such a large flat direction set by this argument.

For a legal coloring satisfying (R), antipodal invariance is automatic from the two reversal laws. In particular, for \(|S_T|\le1\) every induced dependence on that lone bit is constant, so the full coloring is direction-only; this is a useful strengthening for the first nontrivial parameter. For \(|S_T|\ge2\), genuinely varying antipodally invariant XOR-type dependence is possible, and the polynomial extraction proof applies.

**Sources:** Devine–Milans scrapbook, “Antisymmetric Tournaments” and “Boundary Tournaments,” for the terminal-pair \(\sqrt n\) theorem; existing NORI foundational manuscript *Sharp logarithmic monochromatic geodesics under bounded exterior support* for the comparison without (R).
