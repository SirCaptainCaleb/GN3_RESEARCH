# Sharp logarithmic monochromatic paths under bounded exterior support

# Sharp logarithmic monochromatic geodesics under bounded exterior support

## Main theorem and its sharpness

Let \(V\) be the \(n\) coordinate directions of \(Q_n\), let \(S\subseteq V\) be a distinguished set of size \(t\), and put \(D=V\setminus S\), of size \(m=n-t\). Consider **any** binary coloring \(c(F,(a,b,d))\) of genuine physical ordered three-faces satisfying:

**Exterior-support hypothesis ES3(S):** If the three free directions belong to \(D\), the color of their ordered physical face depends only on their ordered directions and on the fixed exterior coordinate bits in \(S\), with no dependence on any other fixed exterior bits. Colors of ordered faces meeting \(S\) are completely unrestricted.

**Theorem 1 (uniform logarithmic lower bound).** If \(m\ge3\), some monochromatic coordinate geodesic, traversing only directions from \(D\), has at least
\[
\boxed{L\ \ge\ 1+\tfrac12\log_2 m}
\tag{1}
\]
coordinate moves. More precisely, if \(L\) denotes the longest monochromatic *increasing-direction* geodesic length after fixing any total order of \(D\), and any fixed \(S\)-bit vector, then
\[
m\ \le\ \binom{2L-2}{L-1}.
\tag{2}
\]
The proof assumes **neither** antipodal-reversal oddness nor reversal symmetry; it is a self-contained ordered-Ramsey argument for colored consecutive triples.

**Corollary 2 (sharp order for one or finitely many sentinels).** Let \(\mathcal C_t(n)\) consist of all legal antipodal-reversal-odd physical ordered-three-face colorings admitting some support \(S\) of size at most \(t\) satisfying ES3(S), and define
\[
\Lambda_t(n)=\min_{c\in\mathcal C_t(n)}
\max_{\text{monochromatic coordinate geodesics }P}|E(P)|.
\]
For every fixed \(t\ge1\),
\[
\boxed{\Lambda_t(n)=\Theta_t(\log n)}\qquad(n\to\infty).
\tag{3}
\]
The lower bound follows from Theorem 1 using \(m\ge n-t\). For the upper bound, the established self-dual Devine--Milans \((3,3)\)-tournament physical one-sentinel lift belongs to \(\mathcal C_1(n)\subseteq\mathcal C_t(n)\) and forces
\[
\max_P|E(P)|\le2\lceil\log_2(n-1)\rceil+6
\tag{4}
\]
for every monochromatic coordinate geodesic, including arbitrary roots and orders. Thus the logarithmic obstruction and lower bound **match in this substantial face-dependent subclass**. This does *not* establish a universal logarithmic lower bound for unrestricted NORI3.

## 1. Ordered-triple Ramsey lemma with explicit counting

Let \(W=\{1,\ldots,m\}\) be linearly ordered, and assign an arbitrary binary color \(h(i,j,k)\) to every increasing triple \(1\le i<j<k\le m\). An *increasing monochromatic tight path* is a sequence \(v_1<\cdots<v_\ell\) such that the consecutive triple colors \(h(v_i,v_{i+1},v_{i+2})\) are all equal. As customary, a sequence of two vertices is vacuously a monochromatic tight path.

**Lemma 3 (two-color ordered tight-path bound).** Let \(L\ge2\) be the maximum number of vertices in such a path. Then
\[
m\le\binom{2L-2}{L-1}\le4^{L-1}.
\tag{5}
\]

**Proof.** For each ordered pair \(i<j\), let \(A(i,j)\) be the maximum order of a color-0 increasing tight path ending with \(i,j\), and \(B(i,j)\) the analogous maximum for color 1. Both lie in \(\{2,\ldots,L\}\).

If \(i<j<k\) and \(h(i,j,k)=0\), appending \(k\) to any longest 0-path ending in \(i,j\) preserves strict increase and distinctness, so
\[
A(j,k)\ge A(i,j)+1.
\tag{6}
\]
For color 1, correspondingly \(B(j,k)\ge B(i,j)+1\). At least one of these two inequalities applies to **every** \(i<j<k\).

Define, for each vertex \(j\), the downset
\[
I_j=\bigcup_{i<j}
\bigl\{(a,b)\in\{2,\ldots,L\}^2:
a\le A(i,j),\ b\le B(i,j)\bigr\}.
\tag{7}
\]
This is an order ideal of the square grid poset \(\{2,\ldots,L\}^2\). We claim the \(m\) ideals \(I_j\) are **pairwise distinct**. Fix \(i<j\), and set \(q=(A(i,j),B(i,j))\). By definition \(q\in I_j\). If \(q\in I_i\), some \(h<i\) would satisfy
\[
A(h,i)\ge A(i,j),\quad B(h,i)\ge B(i,j).
\]
But the color of the increasing triple \((h,i,j)\), by (6) applied either to \(A\) or to \(B\), forces its corresponding coordinate at \((i,j)\) to be **strictly greater** than that at \((h,i)\), contradiction. Thus \(q\notin I_i\), and \(I_i\ne I_j\).

The number of order ideals in a product of two chains of length \(L-1\) is exactly \(\binom{2L-2}{L-1}\), obtained by identifying the staircase boundary of an ideal with a monotone lattice path having \(L-1\) horizontal and \(L-1\) vertical steps. We have \(m\) distinct ideals, yielding the first inequality in (5). The elementary bound \(\binom{2d}{d}\le2^{2d}=4^d\) gives the second. Taking base-two logarithms proves \(L\ge1+\tfrac12\log_2m\). \(\square\)

**Remark.** This is the exact terminal-*ordered*-pair/ideal-counting mechanism behind the classical ordered Ramsey bound for two-colored 3-uniform monotone tight paths. Unlike the scrapbook's boundary-tournament \(\sqrt n\) theorem, it assumes neither antisymmetry nor a tournament condition. Its price is the weaker logarithmic conclusion.

## 2. Transfer to physical cube geodesics

**Proof of Theorem 1.** Fix any cube vertex \(x\) and any strict total ordering of the ordinary directions \(D\). Put \(\beta=x|_S\). For every ordered triple \(a<b<d\) of *ordinary directions*, exterior support ES3(S) makes
\[
h_\beta(a,b,d)=c(F,(a,b,d))
\tag{8}
\]
well defined for **every** physical face \(F\) whose free directions are \(a,b,d\) and whose fixed \(S\)-coordinates equal \(\beta\). The bits of \(F\) outside \(S\cup\{a,b,d\}\) are immaterial, by the hypothesis.

Apply Lemma 3 to \(h_\beta\), obtaining a strictly increasing list of \(L\) distinct ordinary coordinate directions \(p_1<\cdots<p_L\) with all its consecutive \(h_\beta\)-triples colored by one bit.

Starting at the chosen cube vertex \(x\), traverse the \(L\) directions \(p_1,\ldots,p_L\) exactly once each. This is a genuine coordinate geodesic with \(L\) edges. Every ordered-three-face window along it is a genuine physical face, and since no direction in \(S\) is ever traversed, its fixed \(S\)-bit vector is still \(\beta\). By (8), the actual physical colors of the consecutive windows equal
\[
h_\beta(p_i,p_{i+1},p_{i+2})
\]
and are monochromatic. This proves both the path assertion and the explicit bound (2), with no root changes during the argument. The directions are distinct because they are strictly increasing, and physical face consistency is ensured by ES3(S). \(\square\)

## 3. Matching construction, scope, and failure of unrestricted transfer

The Devine--Milans one-sentinel lift is legal and has \(S=\{s\}\). For every face avoiding \(s\), its color depends solely on ordered free directions and the fixed exterior bit \(z_s(F)\); all other exterior bits are ignored. It therefore satisfies ES3(S) and has logarithmically bounded longest monochromatic geodesics in *both* colors, by complement-reversal self-duality. Combining with Theorem 1 proves (3) even though the lift also colors arbitrary faces meeting \(s\).

For **unrestricted** legal NORI3 colorings the reduction (8) generally fails: at different windows of the same cube geodesic, the exterior ordinary bits reflect different previously traversed directions. A single ordered triple may consequently be assigned different colors on different physical faces with the same ordered free directions and the same \(\beta\). No fixed \(h_\beta\) can represent all those windows. In particular **neither** the \((3,3)\)-tournament lower-bound mechanism nor the ordered-Ramsey proof above transfers without an additional coherence/transport hypothesis. The theorem is exactly sharp as a conclusion for fixed-size exterior support; it is deliberately not promoted to a universal bound.

**Further scope.** The same argument applies if one can find a subset \(D\) of \(m\) directions and a fixed exterior fiber for which all ordered physical three-faces on \(D\) are independent of the other \(D\)-exterior bits (regardless of how the coloring behaves elsewhere). It also applies to *nonlegal* binary ordered physical-face colorings: the lower bound is a purely combinatorial consequence of exterior-bit flatness.

## Consequential research implication

The logarithmic extremal scale is settled **within the bounded-exterior-support class**. An unrestricted counterexample to \(\Omega(\log n)\) cannot have bounded exterior-coordinate support, and any successful universal theorem must handle changes of the induced ordered-triple coloring as ordinary coordinates are traversed. Thus the remaining problem is fundamentally an *exterior-fiber coherence problem*, not merely a better path theorem for fixed \((3,3)\)-tournaments.

**Cross-reference.** The established manuscript *Logarithmic monochromatic NORI3 paths from a self-dual (3,3)-tournament* supplies (4). The present proof of Lemma 3 is independent of published literature and can be checked directly.

## Consolidated independent proof: sparse-dependence theorem

Previous Subsection `logarithmic_geodesics_from_sparse_exterior_dependence_without_reversal_symmetry`, exact original composition version 1.

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
