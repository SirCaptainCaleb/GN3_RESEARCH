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
