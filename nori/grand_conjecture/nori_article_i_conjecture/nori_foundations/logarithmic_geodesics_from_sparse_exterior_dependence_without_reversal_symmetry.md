# Logarithmic geodesics from sparse exterior dependence without reversal symmetry

# Logarithmic monochromatic cube geodesics from sparse exterior dependence, without reversal symmetry

## Statement and implication for the unrestricted NORI3 frontier

Let \(V\) be the \(n\)-element direction set of \(Q_n\), \(n\ge4\), and let \(c(F,\pi)\) be **any** binary coloring of ordered physical three-faces, with traversal-corner independence as usual. No antipodal law and no same-face reversal symmetry are needed for this result.

For each unordered triple \(T\in\binom V3\), let \(S_T\subseteq V\setminus T\) be a set of exterior coordinates such that, for each ordering \(\pi\) of \(T\), the color on a physical face with free set \(T\) is determined entirely by \(\pi\) and the exterior bits indexed by \(S_T\). A canonical choice is the union, over all six orderings, of the essential-variable sets of their Boolean face-color functions. The **total exterior-dependence incidence** and **average support** are
\[
B=\sum_{T\in\binom V3}|S_T|,\qquad
\bar d=B/\binom n3.
\]
No common support set is assumed; the \(S_T\) can be unrelated.

**Theorem A (sparse-dependence bound).** When \(B>0\), set
\[
p=\min\left\{1,\left(\frac{n}{4B}\right)^{1/3}\right\},
\quad M=\left\lceil\frac{3np}{4}\right\rceil.
\tag{1}
\]
There exists a monochromatic coordinate-geodesic of length \(L\) (number of distinct coordinate moves) with
\[
\boxed{L\ \ge\ 1+\tfrac12\log_2 M}
\tag{2}
\]
whenever \(M\ge2\), and in all cases a path with at least \(\max\{3,\lceil1+\frac12\log_2 M\rceil\}\) moves for \(n\ge3\). For \(B=0\), one can take \(M=n\).

In particular, if \(\bar d\ge1\), using \(B\le\bar d\,n^3/6\) in (1) yields
\[
\boxed{L\ \ge\ 1+\tfrac16\log_2(n/\bar d)-O(1)}
\tag{3}
\]
with an absolute additive constant. If \(\bar d=O(n^{1-\epsilon})\) for a **fixed** \(\epsilon>0\), then
\[
\boxed{L=\Omega_\epsilon(\log n)}.
\tag{4}
\]
For \(\bar d=O(1)\), the lower bound is \(\Omega(\log n)\), even if the supports \(S_T\) differ arbitrarily from triple to triple.

**Theorem B (near-linear essential-support barrier).** Let \(L_{\max}(c)\) be the maximum monochromatic geodesic length of \(c\). If
\[
4^{L_{\max}(c)-1}<3n/4,
\]
then the canonical total essential-variable incidence \(B\) satisfies
\[
\boxed{B\ge\frac{27n^4}{256\,64^{L_{\max}(c)-1}}}
\tag{5}
\]
and hence
\[
\boxed{\bar d\ge\frac{81n}{128\,64^{L_{\max}(c)-1}}}.
\tag{6}
\]
In particular, an unrestricted NORI3 family with \(L_{\max}(c_n)=o(\log n)\) **must** have
\[
\bar d(c_n)\ge n^{1-o(1)}.
\tag{7}
\]
Thus a sublogarithmic obstruction, if one exists, cannot be based on low- or moderately sparse exterior sensitivity on average: for asymptotically almost linear (in exponent) numbers of ordinary directions, triple face colors must depend essentially on many other coordinates, averaged across triples.

## Proof: removing all internal exterior dependencies

Create the 4-uniform hypergraph \(\mathcal H\) on \(V\), including hyperedge \(T\cup\{u\}\) for each unordered triple \(T\) and \(u\in S_T\). Repeated hyperedges are allowed conceptually but can be discarded; in either case the number of distinct edges is at most \(B\).

For \(p\) from (1), choose a random subset \(X\subseteq V\) by retaining each direction independently with probability \(p\). Then
\[
\mathbb E|X|=np,\qquad
\mathbb E e(\mathcal H[X])\le Bp^4\le np/4.
\]
Therefore a particular \(X\) satisfies \(|X|-e(\mathcal H[X])\ge3np/4\). By removing at most one vertex from each edge of \(\mathcal H[X]\) (using the original finite edge list), one obtains an independent direction set \(D\subseteq V\) with
\[
|D|\ge \left\lceil3np/4\right\rceil=M.
\tag{8}
\]
Independence means, for every three-set \(T\subseteq D\),
\[
S_T\cap D=\varnothing. \tag{9}
\]
This is **not** a common-global-support hypothesis: the sets \(S_T\) may be disjoint, overlapping, nonlinear, and nonuniform. It asserts only that no exterior coordinate capable of affecting a face supported on \(D\) is itself traversed inside \(D\).

Fix any root \(x\in Q_n\). For each ordered triple \(\pi=(a,b,c)\) of distinct directions in \(D\), define \(h_x(a,b,c)\) as the color of any physical face with free set \(\{a,b,c\}\) whose fixed bits on \(S_{\{a,b,c\}}\) agree with \(x\). By the support condition this is well-defined, independent of all other exterior bits. By (9), every geodesic using only directions in \(D\), starting at \(x\), maintains the relevant \(S_T\)-bits unchanged at every ordered-three-face window. Therefore every such path's actual physical color word is *exactly* its consecutive-triple color word under this single direction-only function \(h_x\).

Choose an arbitrary strict total order on \(D\). The two-color ordered-tight-path Ramsey lemma (proved independently in the sibling manuscript *Sharp logarithmic monochromatic geodesics under bounded exterior support*) says that for any binary coloring of increasing triples on \(m=|D|\) vertices, there is an increasing monochromatic tight path on \(L\) distinct vertices with
\[
m\le\binom{2L-2}{L-1}\le4^{L-1}. \tag{10}
\]
For completeness, label each pair \(i<j\) by the two maximum orders of color-0 and color-1 increasing tight paths ending in \((i,j)\). Along each triple, the coordinate corresponding to that triple's color strictly increases between its first and second pair. For every \(j\), form the downwards-closed ideal in the \((L-1)\times(L-1)\) grid generated by incoming pair labels \((i,j)\). For \(i<j\), the label of \((i,j)\) belongs to the ideal of \(j\) but cannot belong to that of \(i\), by the strict increase. Thus all \(m\) vertex ideals are distinct, and the square grid has precisely \(\binom{2L-2}{L-1}\) ideals. This proves (10).

Read the resulting increasing path \(p_1,\ldots,p_L\) as a sequence of *distinct cube directions*. Starting at the fixed root \(x\), traverse them once each. Equation (9) guarantees that every actual ordered physical window has exactly the prescribed \(h_x\)-color. Hence the cube geodesic is monochromatic, and (10) gives (2). When \(B=0\), all supports are empty, one may simply take \(D=V\), giving \(M=n\). This proves Theorem A. \(\square\)

## Proof: quantitative barrier for prospective sublogarithmic examples

Let \(L=L_{\max}(c)\). Suppose \(4^{L-1}<3n/4\). Theorem A would give \(L\ge1+\frac12\log_2(3n/4)\) if \(B\le n/4\), a contradiction, so \(B>n/4\) and
\(p=(n/(4B))^{1/3}<1\). Combining (8)–(10),
\[
4^{L-1}\ge M\ge\frac{3n}{4}\left(\frac{n}{4B}\right)^{1/3}.
\]
Cubing and rearranging gives
\[
64^{L-1}\ge\frac{27n^4}{256B},
\]
establishing (5). Since \(\binom n3\le n^3/6\), dividing by \(\binom n3\) gives (6). If \(L=o(\log n)\), the premise \(4^{L-1}<3n/4\) holds for all sufficiently large \(n\), while \(64^{L-1}=n^{o(1)}\), yielding (7). \(\square\)

## Why this changes the frontier

The previously established fixed-common-exterior-support theorem gives a sharp \(\Theta(\log n)\) guarantee for one set of finitely many special directions, with no reversal assumption. The previous *Polynomial monochromatic geodesics from sparse triplewise exterior support* gives a **stronger polynomial** guarantee for \(d=o(n)\), but **requires same-face reversal oddness** in order to invoke the Devine–Milans boundary-tournament square-root path theorem.

The present theorem has neither restriction. Its supports can vary with the triple and its coloring can violate same-face antisymmetry maximally. For all physical ordered-three-face colorings, including legal unrestricted NORI3, it pins any potential sublogarithmic construction to the near-linear average essential-support regime. The established legal one-sentinel Devine–Milans construction has \(\bar d\le1\) and all monochromatic paths \(O(\log n)\), so (4) is **asymptotically sharp** for legal colorings with bounded *average triplewise* support, even though these need not admit a fixed common support.

The method deliberately does not establish the universal conjectural \(\Omega(\log n)\) lower bound for arbitrary physical colorings: if \(\bar d=\Theta(n)\), the support hypergraph may be complete, and the independent-set extraction need yield only constantly many directions. A fundamentally different *exterior-fiber coherence* argument would be needed in that regime.

There is also no immediate implication that \(\bar d=n^{1-o(1)}\) is **sufficient** for sublogarithmic examples. Theorems A–B give necessity only.
