# Extremal geodesic blockers and exponential paired-root stability

### Extremal geodesic blockers and exponential paired-root stability

Let \(d\ge2\). A complete geodesic traverses each cube dimension once between antipodal vertices. For an arbitrary binary edge coloring \(f\), let \(A(f)\) denote roots admitting a complete path with word \(0^*1^*\), and \(P(f)=A(f)\cap\overline{A(f)}\). By reversing paths, a root is paired precisely when it admits both \(0^*1^*\) and \(1^*0^*\) orientations. Either color of monochromatic complete path certifies a paired root.

**Theorem 1 (minimum blocker rigidity).** An edge set \(S\) intersecting every full antipodal geodesic has \(|S|\ge2^{d-1}\), with equality precisely when it consists of the entire edge class of one direction.

*Proof.* A uniformly sampled rooted full geodesic uses every specified cube edge with probability \(2^{-(d-1)}\). Its expected \(S\)-count is \(|S|/2^{d-1}\), proving the bound. At equality all full geodesics contain one \(S\)-edge. On a square with cyclically ordered membership indicators \(a,b,c,e\), compare full paths beginning with the two dimensions from one corner and then from an adjacent corner. The two swaps give \(a+b=c+e\) and \(b+c=a+e\); hence \(a=c\), \(b=e\). All opposite edges of all squares have equal membership. Thus membership is constant on every direction class. Since every full path uses every direction once and hits \(S\) once, a single direction is selected. QED.

Fix direction \(i\). Let \(c_i\) color all \(i\)-edges one and all other edges zero. Every root has both oriented witnesses: putting \(i\) last produces \(0^{d-1}1\); putting it first produces \(10^{d-1}\).

**Theorem 2 (stability through the endpoint radius).** If any binary edge coloring \(f\) differs from \(c_i\) on at most \(2^{d-2}\) edges, then \(P(f)\ne\varnothing\).

*Proof.* Let \(F\) be the changed-edge set, and split the cube as \(Q_{d-1}\times Q_1\), using \(i\) vertically. For every root \(z=(y,s)\) and permutation \(\pi\) of the horizontal dimensions, take the two complete paths with \(i\) last and first. They are edge-disjoint and support the two desired orientations under \(c_i\). For uniform \(z,\pi\), each cube edge occurs in their union with probability \(2^{-(d-2)}\): for an \(i\)-edge the candidate horizontal positions are \(y\) and \(\bar y\); for a horizontal edge the same horizontal geodesic occurs in both vertical layers. Thus
\[
\mathbb E|F\cap(P_{\rm first}\cup P_{\rm last})|=|F|/2^{d-2}.
\tag{1}
\]
If \(|F|<2^{d-2}\), some path pair is untouched, giving a paired root.

Suppose \(|F|=2^{d-2}\) but there is no paired root. Every candidate path pair then hits \(F\) at least once. Equation (1) forces the hit count to be one **for every root and permutation**.

Let \(F_i(y)\) indicate the changed vertical edge at horizontal location \(y\). For a horizontal edge \(e\), define the nonnegative integer weight \(w(e)=F^0(e)+F^1(e)\in\{0,1,2\}\), the number of its two layer copies changed. For every horizontal root \(y\) and full horizontal geodesic \(G(y,\pi)\), the count-one identity reads
\[
F_i(y)+F_i(\bar y)+\sum_{e\in G(y,\pi)}w(e)=1.
\tag{2}
\]
For fixed \(y\), the weighted horizontal path sum is therefore independent of \(\pi\). Compare the two routes through a horizontal square from two neighboring corners, holding the remaining dimension order fixed. The resulting pair of equations forces opposite edges of the square to have equal \(w\)-weight, just as in Theorem 1. Hence \(w\) is constant on each horizontal direction class; this is also immediate when the horizontal cube has dimension one. Denote the constants \(w_j\), and let \(W_0=\sum_{j\ne i}w_j\). Equation (2) gives
\[
F_i(y)+F_i(\bar y)+W_0=1,
\]
so \(W_0\in\{0,1\}\).

If \(W_0=0\), all horizontal edges retain color zero and each antipodal pair of vertical edges has one changed member. From any root, taking the vertical edge first or last at its zero-colored location yields a full **monochromatic zero** geodesic. Every root is paired.

If \(W_0=1\), all vertical edges retain color one; all horizontal directions except one, say \(j\), retain color zero. The \(j\)-edge colors may vary without affecting the argument. From every root, listing all dimensions other than \(i,j\), then \(j\), then \(i\) gives a \(0^*1^*\) word. Listing \(i\), then \(j\), then the remaining dimensions gives a \(1^*0^*\) word. Every root is again paired. Both cases contradict the premise. QED.

**Corollary 3 (separation of hypothetical counterexamples).** If \(P(f)=\varnothing\), then \(f\) has at least \(2^{d-1}+1\) edges of each color, and its Hamming distance to every one-direction reference coloring \(c_i\), as well as to its global complement, exceeds \(2^{d-2}\).

*Proof.* A coloring without paired roots contains no monochromatic complete path of either color. Each color class therefore blocks all such paths and has size at least \(2^{d-1}\), by Theorem 1. Equality would make one class a full direction class, giving paired roots. The Hamming separation follows from Theorem 2 and global color complementation. QED.

**Closure perspective.** The minimum transversals of the full geodesic system are rigid direction classes. A substantial Hamming neighborhood around every such extremizer is paired-root-safe. To complete NORI1 through this strategy one needs a stability theorem forcing a minimal paired-root-free coloring near an extremizer, or an exchange argument coupling its repaired witnesses; neither follows merely from the bound here. This route respects dimension-simpleness and avoids reliance on favorable-root density, which can decay exponentially under Cartesian products.

## Quantitative stability of all near-minimum antipodal geodesic blockers

Write \(M=2^{d-1}\), so each direction of \(Q_d\) contains \(M\) undirected edges. For a blocker \(S\subseteq E(Q_d)\) of all full antipodal geodesics, put \(|S|=M+t\), \(t\ge0\).

**Theorem 4 (square-pivot/Poincaré stability).** There exists a union \(U\) of whole direction edge classes such that
\[
\boxed{|S\mathbin{\triangle}U|\le 2d(d-1)t.}
\tag{3}
\]
When \(t\le M/(4d(d-1))\), \(U\) consists of just one direction class and the corresponding characteristic coloring \(f=\mathbf1_S\) has a paired root.

*Proof.* Choose a uniform cube root \(z\), a uniform ordered pair of distinct directions \(i,j\), and a uniform ordering \(\rho\) of the remaining directions. Form four full geodesics: from \(z\), traverse \(i,j,\rho\) or \(j,i,\rho\); from \(z\oplus e_i\), traverse \(j,i,\rho\) or \(i,j,\rho\). Each of these four geodesics, considered marginally, is uniformly distributed over all rooted dimension-ordered complete geodesics, so each has expected \(S\)-count
\[
\mu=|S|/M=1+t/M.
\]
Every count is at least one, whence each path has probability at most \(t/M\) of having two or more \(S\)-edges. With probability at least \(1-4t/M\), all four geodesics have \(S\)-count one.

Denote the cyclically consecutive membership indicators of the initial \(i,j\) square by \(a,b,c,e\), so \(a,c\) are opposite \(i\)-edges and \(b,e\) are opposite \(j\)-edges. When the two full paths rooted at \(z\) both have count one, their shared suffix cancels and yields \(a+b=c+e\). When the two full paths rooted at \(z\oplus e_i\) both have count one, their shared suffix cancels and yields \(b+c=a+e\). Therefore, outside a probability at most \(4t/M\), the square satisfies \(a=c,b=e\).

For each direction \(i\), let \(f_i:\{0,1\}^{d-1}\to\{0,1\}\) indicate membership in \(S\) of its edges. Define the direction influence
\[
I_{ij}=\Pr_{z}\bigl(f_i(z)\ne f_i(z\oplus e_j)\bigr),\qquad i\ne j.
\]
A uniformly sampled ordered pair \(i,j\) and square root \(z\) has
\[
\mathbb E\bigl[
\mathbf1_{f_i(z)\ne f_i(z\oplus e_j)}
+\mathbf1_{f_j(z)\ne f_j(z\oplus e_i)}
\bigr]
=\frac{2}{d(d-1)}\sum_{i\ne j}I_{ij}.
\]
The summand is zero when both square equalities hold, and is at most two otherwise. Hence
\[
\boxed{\sum_{i\ne j}I_{ij}\le 4d(d-1)\frac tM.}
\tag{4}
\]

Write \(p_i=\mathbb E f_i\), and let \(u_i\in\{0,1\}\) be a majority value of \(f_i\). The Boolean-cube Poincaré inequality gives
\[
p_i(1-p_i)\le\frac14\sum_{j\ne i}I_{ij}.
\]
Since \(\min(p_i,1-p_i)\le2p_i(1-p_i)\), the number of direction-\(i\) edge labels differing from \(u_i\) is at most \((M/2)\sum_{j\ne i}I_{ij}\). Let \(U\) be the union of those whole direction classes with \(u_i=1\). Summing and using (4) gives (3).

Now suppose \(t\le M/(4d(d-1))\). Then \(k=|S\triangle U|\le M/2\), whereas \(|S|=M+t\) and \(t\le M/8\). Since the size of \(U\) is a multiple of \(M\), the inequality \(\bigl||U|-|S|\bigr|\le k\) rules out \(|U|=0\) and \(|U|\ge2M\). Thus \(|U|=M\): \(U\) is one full direction class. Theorem 2 then supplies a paired root, since \(k\le M/2=2^{d-2}\). QED.

**Corollary 5 (uniform exponential excess in every paired-root counterexample).** If an arbitrary coloring \(f\) of \(Q_d\) has no paired root, then both its color classes obey
\[
\boxed{|E_c(f)|>2^{d-1}\left(1+\frac{1}{4d(d-1)}\right),
\qquad c\in\{0,1\}.}
\tag{5}
\]

*Proof.* A paired-root-free coloring has no monochromatic full antipodal geodesic. Thus each color class is a blocker as in Theorem 4. If either had cardinality no more than the threshold in (5), Theorem 4 applied to that class (with the two color values exchanged if necessary) would supply a paired root, contradiction. QED.

**Closure implication and caution.** This supplies a rigorous quantitative bridge from the cardinality of a complete-geodesic transversal to the bridge-theorem paired-root goal. It does not show that an arbitrary minimal paired-root-free coloring has color-class size near the minimum, so the unrestricted conjecture remains open. The product-factorization counterexamples to favorable-root density make such an isoperimetric or critical-repair step essential rather than automatic. The proof uses only complete dimension-simple geodesics and commuting square exchanges.

## Abundance of paired roots under Hamming perturbations

**Theorem 6 (paired-root loss bounded by four per edited edge).** Let \(c_i\) be the reference coloring with all direction-\(i\) edges one and every other edge zero. For any binary edge coloring \(f\) at Hamming distance \(k\) from \(c_i\),
\[
\boxed{|P(f)|\ge\max\{0,\,2^d-4k\}.}
\tag{6}
\]
In particular at most \(2k\) antipodal pairs of roots can fail to be paired when measured against this reference witness construction.

*Proof.* For each root \(z\) and permutation \(\pi\) of the other \(d-1\) dimensions, take the pair of complete geodesics that places \(i\) first or last, as in Theorem 2. If neither path contains a changed edge, both one-switch orientations remain valid from \(z\), so \(z\in P(f)\). Thus for every nonpaired root \(z\), each of the \((d-1)!\) paired witness choices has at least one changed edge in its union. Summing over all roots and permutations, we obtain
\[
(2^d-|P(f)|)(d-1)!
\le \sum_{z,\pi}|F\cap(P_{\rm first}(z,\pi)\cup P_{\rm last}(z,\pi))|.
\]
Every edge belongs to \(4(d-1)!\) of these indexed witness unions by the uniform incidence calculation in Theorem 2. Hence the right side equals \(4k(d-1)!\), proving (6). Since \(P(f)\) is antipodally symmetric by definition, its complement consists of antipodal root pairs. QED.

**Corollary 7 (paired-root abundance close to minimum blockers).** If a full-geodesic blocker \(S\) has cardinality \(2^{d-1}+t\), and the nearest union-of-directions approximation \(U\) from Theorem 4 consists of one direction, then its characteristic coloring obeys
\[
\boxed{|P(\mathbf1_S)|\ge\max\{0,\,2^d-8d(d-1)t\}.}
\]
In particular, the paired-root set occupies almost the entire cube whenever the blocker excess is small compared with \(2^d/d^2\).

*Proof.* Use Theorem 4 to obtain \(|S\triangle U|\le2d(d-1)t\), and apply Theorem 6 with \(k=|S\triangle U|\). QED.

**Interpretation.** The stability theorem is not purely existential. Each unit of Hamming perturbation can spoil the chosen two-orientation witness pairs at at most four root vertices, measured by uniform fractional path incidence. This abundance statement may be useful when attempting to couple the repaired roots of two critical edge recolorings.

## Every direction-uniform coloring has the same protected paired-root radius

Let \(d\ge2\), \(M=2^{d-1}\), and let \(c\) be any cube edge coloring **constant on each dimension class**, with a partition \([d]=A\sqcup B\): all \(A\)-edges have color zero and all \(B\)-edges have color one. Either part may initially be empty.

**Theorem 8 (universal directional-template stability).** If an arbitrary binary cube-edge coloring \(f\) has Hamming distance
\[
\boxed{\operatorname{dist}(f,c)\le M/2=2^{d-2},}
\tag{7}
\]
then \(f\) has a paired root. The assertion holds for **every** direction-uniform template \(c\), not just those with one exceptional dimension.

*Proof.* If \(A\) or \(B\) is empty, \(c\) is monochromatic. Were \(f\) to lack a paired root, it would in particular lack a monochromatic full geodesic of the template color. Its altered-edge set would then meet every full geodesic, and the minimum-blocker theorem would force at least \(M\) altered edges, contrary to (7).

Suppose \(a=|A|,b=|B|\) are positive. Write vertices as \((u,v)\in Q_A\times Q_B\). For any root \((u,v)\), an arbitrary full \(A\)-geodesic \(P_A\) from \(u\) to \(\bar u\), and an arbitrary full \(B\)-geodesic \(P_B\) from \(v\) to \(\bar v\), form the following two full paths:
\[
P_{01}= (P_A\text{ at }v)\,\cdot\,(P_B\text{ at }\bar u),\qquad
P_{10}= (P_B\text{ at }u)\,\cdot\,(P_A\text{ at }\bar v).
\tag{8}
\]
They are edge-disjoint and have words \(0^a1^b\) and \(1^b0^a\) under \(c\). Let \(F\) be the edges on which \(f\ne c\), with \(k=|F|\). Sampling the root and the two blockwise dimension orders uniformly, each edge of \(Q_d\) belongs to the union in (8) with probability \(2/M\), because each path is marginally a uniformly translated complete direction-simple path. Thus
\[
\mathbb E|F\cap(P_{01}\cup P_{10})|=2k/M.
\tag{9}
\]
If \(k<M/2\), some rectangle is untouched and supplies a paired root.

Now suppose \(k=M/2\) and, toward contradiction, that \(f\) has no paired root. Every rectangle (8) must contain an altered edge, so (9) implies it contains **precisely one altered edge for every root and both blockwise orders**.

For an \(A\)-direction edge \(e\) in the \(A\)-cube, fix \(v\in Q_B\) and define its paired-layer weight
\[
w_A(e;v)=\mathbf1_F(e,v)+\mathbf1_F(e,\bar v)\in\{0,1,2\}.
\]
Similarly, for a \(B\)-direction edge \(e'\) in \(Q_B\) and \(u\in Q_A\), put
\[
w_B(e';u)=\mathbf1_F(u,e')+\mathbf1_F(\bar u,e').
\]
The one-hit identity is
\[
\sum_{e\in P_A}w_A(e;v)+\sum_{e'\in P_B}w_B(e';u)=1
\quad\text{for all }u,v,P_A,P_B.
\tag{10}
\]
Holding \(u,v,P_B\) fixed, every complete \(A\)-geodesic from \(u\) has the same total \(w_A\)-weight. Exchanging the first two directions around an arbitrary \(A\)-square, and repeating the exchange from an adjacent root, shows that opposite \(A\)-square edges have equal weights. Hence for fixed \(v\), \(w_A(e;v)\) depends only on the direction \(i\in A\), say \(\alpha_i(v)\in\{0,1,2\}\). The same square argument in \(Q_B\) yields direction constants \(\beta_j(u)\in\{0,1,2\}\) for \(j\in B\). For one-dimensional factors this direction constancy holds without exchanges.

Consequently (10) becomes
\[
\sum_{i\in A}\alpha_i(v)+\sum_{j\in B}\beta_j(u)=1
\quad\text{for every }u,v.
\tag{11}
\]
Since the two nonnegative integer sums depend on disjoint arguments, they are constants \(r,s\ge0\), with \(r+s=1\). Thus one is zero and the other one.

If \(r=0\), no \(A\)-edge was altered anywhere. For each fixed \(u\), the relation \(\sum_{j\in B}\beta_j(u)=1\) says that all \(B\)-edges are unaltered except possibly those of one direction \(j(u)\), since \(\beta_j(u)=0\) means neither of the two \(u,\bar u\) copies was altered. From root \((u,v)\), traverse every \(A\)-direction first, placing the possibly exceptional \(B\)-direction first among the \(B\)-steps at \(\bar u\); the word is \(0^*1^*\). For the opposite orientation traverse the \(B\)-directions first at \(u\), placing the possibly exceptional one last within \(B\), followed by all \(A\)-directions; the word is \(1^*0^*\). Thus **every root is paired**.

If \(s=0\), no \(B\)-edge was altered, and for each fixed \(v\) at most one \(A\)-direction can contain altered edges there. Take all \(A\)-directions first with that exceptional direction last, then all \(B\)-directions: the word is \(0^*1^*\). For the reverse orientation put all \(B\)-directions first, then the possibly exceptional \(A\)-direction first among the \(A\)-steps, followed by the remaining \(A\)-directions: the word is \(1^*0^*\). Again every root is paired. This contradicts the premise and proves the theorem. QED.

**Corollary 9 (a square-variation necessary condition for counterexamples).** For each \(i\in[d]\), write \(f_i(x)\) for the color of the direction-\(i\) edge at \(x\), independent of the \(i\)-th bit, and for \(j\ne i\) define
\[
I_{ij}(f)=\Pr_{x\in Q_d}[f_i(x)\ne f_i(x\oplus e_j)].
\]
If \(f\) has no paired root, then
\[
\boxed{\sum_{i\ne j}I_{ij}(f)>1.}
\tag{12}
\]
Equivalently, more than \(2^{d-2}\) total incidences of disagreeing opposite-edge comparisons must occur over all cubical squares, counting separately the two directions of each square.

*Proof.* Let \(p_i=\Pr f_i=1\) and let \(c_i\in\{0,1\}\) be the majority color of direction-\(i\) edges. Then the nearest direction-uniform template \(c\) differs from \(f\) on
\[
k=M\sum_i\min(p_i,1-p_i).
\]
By the Boolean-cube Poincaré inequality, \(p_i(1-p_i)\le\frac14\sum_{j\ne i}I_{ij}\), and \(\min(p_i,1-p_i)\le 2p_i(1-p_i)\). Hence
\[
k\le\frac M2\sum_{i\ne j}I_{ij}.
\]
Theorem 8 forces \(k>M/2\) for any paired-root-free \(f\), yielding (12). For each unordered pair of dimensions and each of its \(2^{d-2}\) squares, the two opposite-edge disagreements contribute once each to the sum multiplied by \(2^{d-2}\); this is the equivalent integer statement. QED.

**Consequence for the closure plan.** A minimum paired-root-free coloring must be Hamming-far from *every* direction-uniform template, not only the one-direction blockers. It must also have total transverse square variation exceeding one in normalized units. This is a color-sensitive restriction based solely on commuting-square interactions and uses no small-dimension assumption. It is not sufficient by itself to prove paired-root existence.

## Two arbitrary exceptional directions still force many paired roots

For a binary edge coloring \(f\) of \(Q_d\), say that a dimension \(i\) is *uniform* if every edge of direction \(i\) has the same color, independent of its location. No restriction is imposed on the coloring of the remaining directions.

**Lemma 10 (square favorability).** For any coloring \(g\) of the four edges of \(Q_2\), the set \(A_0(g)\) of roots admitting a complete two-edge path with nondecreasing color word has size at least three. The same is true of the set \(A_1(g)\) of roots admitting a nonincreasing word.

*Proof.* A root \(x\) fails to lie in \(A_0(g)\) only if both possible two-step paths beginning at \(x\) have color word \(10\). Thus both edges incident with \(x\) must have color one and both incident with its antipode must have color zero. This pins down all four square-edge colors and makes every other root favorable. Hence at most one root is excluded. Swapping zero and one gives the nonincreasing assertion. QED.

**Theorem 11 (two-exception paired-root theorem).** If at most two dimensions of an arbitrary binary edge coloring \(f\) of \(Q_d\) are nonuniform, then
\[
\boxed{|P(f)|\ge 2^{d-1}.}
\tag{13}
\]
If at most one direction is nonuniform, every root is paired. The lower bound with two exceptional directions is attained by Cartesian-product colorings.

*Proof.* Let \(S\) contain all nonuniform directions, extending it to two dimensions if necessary. Partition the remaining directions into \(A\) (uniform color zero) and \(B\) (uniform color one), so \([d]=A\sqcup S\sqcup B\). Write a root as \((u,x,v)\in Q_A\times Q_S\times Q_B\).

To construct a \(0^*1^*\) complete path from this root, first traverse all \(A\)-directions, reaching outside configuration \((\bar u,v)\); next traverse the two \(S\)-directions along a nondecreasing two-edge path in the corresponding \(S\)-fiber; finally traverse all \(B\)-directions. The resulting full word is nondecreasing whenever
\[
x\in A_0\bigl(f^{(\bar u,v)}_S\bigr).
\]
For a \(1^*0^*\) path, traverse all \(B\)-directions first, then a nonincreasing two-edge path in the \(S\)-fiber at outside configuration \((u,\bar v)\), then all \(A\)-directions. This requires
\[
x\in A_1\bigl(f^{(u,\bar v)}_S\bigr).
\]
The two restricted square colorings are entirely arbitrary and need not agree. By Lemma 10, each of these favorable-root sets has at least three members among the four \(S\)-roots. Their intersection therefore contains at least two members. For every choice of the \(d-2\) outside-root bits \((u,v)\), at least two values of \(x\) give both orientations at the **same root**. Hence \(|P(f)|\ge2\cdot2^{d-2}=2^{d-1}\).

If at most one direction is nonuniform, take \(S\) with one element. Every path in its one-dimensional fiber is monochromatic, so both orientation requirements hold from both roots; the same concatenation shows \(P(f)=V(Q_d)\).

To see sharpness for two exceptions, take the square coloring \(h\) with \(A_0(h)=\{01,10,11\}\), \(P(h)=\{01,10\}\) from the Cartesian-factorization Subsection. Form \(f=h\boxtimes g\), where \(g\) is any direction-uniform coloring on the other \(d-2\) dimensions. The factorization of paired-root sets gives
\[
|P(f)|=|P(h)|\,|P(g)|=2\cdot2^{d-2}=2^{d-1}.
\]
QED.

**Corollary 12 (at least three variable direction classes).** Any hypothetical coloring of \(Q_d\) with no paired root must have at least three nonuniform dimension classes. This is stronger than interaction-graph connectedness alone: nonuniformity is allowed to depend on all remaining dimensions, yet two exceptional classes can never obstruct paired roots.

**Closure significance.** The proof needs neither antipodal oddness nor a bound on the number of nonuniform edges within the two exceptional direction classes. It converts paired-root compatibility into an intersection property for favorable-root sets of arbitrary fiber colorings. This suggests a possible general proof scheme through cross-intersection of feasible-root families on higher-dimensional fibers. The square case is strong enough to force intersection because each favorable set has density at least three quarters. Cartesian products show that such favorable-root density need not remain above one half in arbitrarily high fiber dimension, so a higher-dimensional argument must exploit more than a uniform cardinality bound.

## Three arbitrary nonuniform directions force paired roots

We strengthen the preceding two-exception theorem by proving a sharp three-cube favorability bound without enumeration.

**Lemma 13 (same-parity two-root certificate in a colored three-cube).** For every arbitrary binary coloring of the edges of \(Q_3\), any two distinct root vertices of the same Hamming parity cannot both fail to admit a complete \(0^*1^*\) geodesic. Consequently
\[
\boxed{|A_0(g)|\ge6,\qquad |A_1(g)|\ge6.}
\tag{14}
\]
Both bounds are sharp.

*Proof.* Every pair of distinct three-bit vertices of the same parity has Hamming distance two. By a cube automorphism we may take the roots to be \(000\) and \(110\), using bit positions \((0,1,2)\). Denote the following seven undirected cube edges by letters:
\[
\begin{array}{lll}
a=000\!-\!100,& b=100\!-\!110,&c=100\!-\!101,\\
d=101\!-\!111,&e=001\!-\!101,&f=000\!-\!001,\\
g=110\!-\!111.& &
\end{array}
\]
Here the symbols \(a,\ldots,g\) also denote their edge-color bits. The following six length-three, dimension-simple full paths start at one of our two roots:
\[
(a,b,g),\quad(a,c,d),\quad(f,e,d);
\qquad
(b,a,f),\quad(b,c,e),\quad(g,d,e).
\tag{15}
\]
For bits \(x,y\), the descending-comparison indicator is \(x(1-y)\). A binary length-three word is not of type \(0^*1^*\) precisely when it contains a descent, and such a word contains at most one descent. Summing the numbers of descents in the six paths (15), and maximizing independently over their three internal edge bits \(c,f,g\), bounds the sum from above by
\[
\boxed{
(a\oplus b)+(d\oplus e)+
\max(a,1-e)+\max(b,1-d)+
\max(a+b,2-d-e).
}
\tag{16}
\]
Indeed, the comparisons \(a\leftrightarrow b\) and \(d\leftrightarrow e\) yield the two XOR terms; the two-comparison chains \(a\to f\to e\) and \(b\to g\to d\) produce the next two maxima; the comparisons \(a\to c,b\to c,c\to d,c\to e\) give the final maximum. Expression (16) never exceeds five: if \(d=e=0\), it is \(4+(a\oplus b)\le5\); if \(d=e=1\), it is \((a\oplus b)+2(a+b)\le4\); and if \(d\ne e\), direct consideration of the four choices for \((a,b)\) gives maximum five. Hence at least one of the six paths has no descent. So two same-parity roots cannot both be unfavorable.

There are four roots of each Hamming parity. Each parity class has at most one unfavorable root, proving \(|A_0|\ge6\). Interchanging the two colors proves the identical bound for \(A_1\).

To witness sharpness, take the two-cube coloring \(h\) with \(A_0(h)=\{01,10,11\}\) from the Cartesian-factorization Subsection, and form \(g=h\boxtimes q\), where \(q\) colors the edges of the one-cube uniformly. Product factorization gives \(|A_0(g)|=3\cdot2=6\). QED.

**Theorem 14 (three-exception paired-root theorem).** Let \(f\) be an arbitrary binary coloring of \(Q_d\), \(d\ge3\). If all but at most three dimension classes have colors independent of location, then
\[
\boxed{|P(f)|\ge2^{d-1}.}
\tag{17}
\]
The bound is sharp. Consequently any hypothetical paired-root-free coloring must have at least **four nonuniform direction classes**.

*Proof.* Extend the collection of nonuniform directions to a three-element set \(S\), and partition the others into \(A\) (uniformly zero) and \(B\) (uniformly one). Every root has form \((u,x,v)\in Q_A\times Q_S\times Q_B\), with \(x\in Q_3\). Traverse all \(A\)-dimensions first, then a complete nondecreasing \(0^*1^*\) geodesic in the \(S\)-fiber with outside location \((\bar u,v)\), and finally all \(B\)-dimensions. This yields a \(0^*1^*\) full path provided \(x\in A_0(g_{\bar u,v})\). Traverse all \(B\)-dimensions first, then a nonincreasing \(1^*0^*\) path in the \(S\)-fiber with outside location \((u,\bar v)\), then all \(A\)-dimensions. This yields the opposite path orientation provided \(x\in A_1(g_{u,\bar v})\).

The two fiber colorings need not be related. Nevertheless Lemma 13 guarantees that each of the two feasible-root sets in \(Q_3\) has at least six of the eight vertices. Their intersection has at least four elements. Thus for each fixed outside configuration \((u,v)\), at least four values of \(x\) make the same root paired. There are \(2^{d-3}\) outside configurations, giving (17).

Sharpness follows from \(f=h\boxtimes q\) on three dimensions, where \(h\) is the preceding extremal two-cube coloring and \(q\) is a monochromatic one-cube; by the previously proved factorization \(|P(f)|=2\cdot2=4=2^{3-1}\). Add any number of uniform-factor dimensions to preserve the paired-root fraction one half. QED.

**Proof-search consequence.** The paired-root exclusion threshold for the number of nonuniform edge-direction classes rises from three to **four**, with no assumption on how any exceptional class depends on other vertex bits. The underlying structural ingredient is a two-source descent-count certificate in \(Q_3\), which is small but powers an unrestricted all-dimensional theorem. Extending this fiber method to four or five arbitrary exception dimensions requires a suitable cross-intersection statement for their nondecreasing and nonincreasing feasible-root families, not a general density bound in arbitrarily many dimensions.

## Four unrestricted exceptional directions by a finite computer-assisted lemma

Define
\[
m_k=\min_{g:E(Q_k)\to\{0,1\}}|A_0(g)|,
\]
where \(A_0(g)\) is the set of roots admitting a full \(0^*1^*\) geodesic.

**Theorem 15 (general fiber-transfer principle).** If a binary edge coloring \(f\) of \(Q_d\) has at most \(k\) nonuniform direction classes, then
\[
\boxed{|P(f)|\ge2^{d-k}\max(0,2m_k-2^k).}
\tag{18}
\]

*Proof.* Enlarge the nonuniform direction set to a \(k\)-element block \(S\), and partition the remaining directions into uniform zero block \(A\) and uniform one block \(B\). For each outside root \((u,v)\in Q_A\times Q_B\), a nondecreasing full path is formed by all \(A\)-steps, then a nondecreasing full path in the \(S\)-fiber at \((\bar u,v)\), then all \(B\)-steps. The opposite orientation is formed by all \(B\)-steps, then a nonincreasing full path in the \(S\)-fiber at \((u,\bar v)\), then all \(A\)-steps. Each of these two arbitrary fiber colorings has a favorable-root set of size at least \(m_k\); interchange zero and one to cover the second orientation. Their intersection has size at least \(\max(0,2m_k-2^k)\), and there are \(2^{d-k}\) outside roots. QED.

The preceding analytical lemmas give \(m_1=2,m_2=3,m_3=6\). We next give a finite computational evaluation at four dimensions.

**Lemma 16 (computer-assisted four-cube root minimum).** Every binary coloring of the 32 undirected edges of \(Q_4\) has at least nine roots admitting a full nondecreasing color word, and this bound is attained:
\[
\boxed{m_4=9.}
\tag{19}
\]

*Reproducible binary-integer certificate.* Introduce binary edge colors \(x_e\) for the 32 cube edges. For each ordered consecutive-edge pair \((e,f)\) appearing on any rooted four-step full geodesic, introduce a binary variable \(y_{ef}\) with the three constraints
\[
y_{ef}\le x_e,\quad y_{ef}+x_f\le1,\quad x_e-x_f-y_{ef}\le0.
\tag{20}
\]
Thus \(y_{ef}\) is one precisely at a descent from color one to color zero. Introduce a binary variable \(b_v\) at each of the sixteen roots. For all \(24\) direction permutations \(\pi\), impose
\[
b_v\le\sum_{j=1}^{3}y_{e_j(v,\pi),e_{j+1}(v,\pi)}.
\tag{21}
\]
Maximize \(\sum_v b_v\). This binary integer program contains 32 edge-color bits, 192 distinct directed comparison bits, 16 unfavorable-root bits, and 960 linear inequalities. The integer solver HiGHS via SciPy reported a certified optimizer objective of seven unfavorable roots, a matching branch-and-bound dual bound of seven, a zero optimality gap, and 328 explored nodes. An independent path-evaluation routine checked a returned feasible assignment and counted nine favorable roots.

All input coefficients in (20)-(21) are integers, and the indexing is explicit: enumerate the 32 cube edges by direction \(i=0,1,2,3\), followed by vertex integers \(v=0,\ldots,15\) with bit \(i\) zero; edge \(e=(v,v\oplus2^i)\). Enumerate roots in integer order and the 24 permutations of the four directions. The displayed constraints can therefore be reproduced using any binary integer-programming implementation. An attaining coloring without a solver is \(h\boxtimes h\), the product of two square colorings \(h\) each with \(|A_0(h)|=3\), giving \(|A_0(h\boxtimes h)|=9\) by Cartesian factorization.

The lemma is labeled **computer-assisted**. A pen-and-paper certificate for the lower bound would be preferable for a final publication; the integer solver's dual bound is the computational evidence for the exhaustive optimum.

**Corollary 17 (four-exception paired-root theorem, computer-assisted).** Any coloring of \(Q_d\), \(d\ge4\), with at most four nonuniform dimension classes satisfies
\[
\boxed{|P(f)|\ge2^{d-3}.}
\tag{22}
\]
Thus a hypothetical paired-root-free coloring requires at least **five** nonuniform direction classes.

*Proof.* Substitute \(m_4=9\) into Theorem 15. QED.

**Limitation of cardinality-only transfer.** The \(r\)-fold Cartesian product of the extremal square coloring has \(m_{2r}\le3^r\). For \(k=6\), this gives \(m_6\le27<32\), so the numerical intersection term in (18) need not be positive once six arbitrary direction classes are permitted. Further progress toward full NORI1 requires structural compatibility, not just favorable-root cardinalities.
