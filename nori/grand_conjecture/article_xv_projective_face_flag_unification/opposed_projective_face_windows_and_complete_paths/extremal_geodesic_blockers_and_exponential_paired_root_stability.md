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

## Inclusion-minimal blockers with sparse roots and complete influence

The Hamming-layer activation example in the gauge research notes can be strengthened to an ordinary coloring with no monochromatic full geodesic, an inclusion-minimal one-colored blocker, and complete directed influence. Thus the obstruction to repair-root counting persists when every direction is nonconstant and all directions interact.

Fix \(r\ge1\), put \(m=2r+1\) and \(d=m+1\), and write vertices as \((x,h)\in Q_m\times Q_1\). Define the monotone antipodally odd Boolean function
\[
g(x,h)=\mathbf1_{\{|x|+2h\ge r+2\}},
\qquad
f_i(z)=g(z)+g(z\oplus e_i)\pmod2.
\tag{MB1}
\]
Let \(D=E_1(f)\).

**Theorem.** The coloring (MB1) has the following properties.

1. Both color classes meet every full antipodal geodesic. The set \(D\) is inclusion-minimal with this property.
2. Recoloring any nonempty subset of \(D\) zero creates a monochromatic full antipodal geodesic between \(0^d\) and \(1^d\). These two fixed roots are empty in the original coloring.
3. Every ordered pair of distinct directions is an influence arc.
4. The favorable and paired-root sets coincide and have the following description:
\[
\begin{aligned}
A_0(f)=A_1(f)=P(f)
={}&\{(x,0):|x|\in\{r,r+1,r+2\}\}\\
&\ \cup\{(x,1):|x|\in\{r-1,r,r+1\}\}.
\end{aligned}
\tag{MB2}
\]
Consequently,
\[
\boxed{
|D|=2(r+1)\binom{2r+1}{r},\quad
|P(f)|=2\left[\binom{2r+1}{r-1}
+2\binom{2r+1}{r}\right],
}
\tag{MB3}
\]
and
\[
\boxed{
\frac{|A_0(f)\cup A_1(f)|}{2^d}
\sim\frac{3}{\sqrt{\pi r}}\longrightarrow0.
}
\tag{MB4}
\]

*Proof.* The total weight in the threshold defining \(g\) is \(2r+3\). Complementing every bit sends its integer weighted sum \(t\) to \(2r+3-t\), so \(g(\bar z)=1-g(z)\). It follows that \(f(\bar e)=f(e)\).

Every full antipodal geodesic has an odd number of \(D\)-edges, because its \(g\)-values telescope from \(g(z)\) to \(1-g(z)\). Thus it cannot be all zero. Its length \(d=2r+2\) is even, so it cannot be all one either.

Each edge \(e\in D\) extends to a path that only changes bits from zero to one from \(0^d\) to \(1^d\). Along this path \(g\) is nondecreasing and changes once, at \(e\). Therefore \(e\) is the only \(D\)-edge on that full geodesic. This proves inclusion minimality and also proves the simultaneous repair assertion: for any nonempty repaired subset, choose any one of its edges and its private path. At both poles every incident edge has color zero. Every full path between the poles meets \(D\), so neither pole admits a monotone color word.

For a base direction \(i\), direct differentiation of (MB1) gives
\[
f_i(x,h)=1
\Longleftrightarrow
|x_{\setminus i}|+2h=r+1,
\qquad
f_h(x)=1
\Longleftrightarrow |x|\in\{r,r+1\}.
\tag{MB5}
\]
These equations show that each base direction reads every other base bit and the hub bit, and that the hub reads every base bit. For example, to see a base-to-base dependence, fix \(h=0\), set \(r\) of the other \(2r-1\) base bits to one, and toggle the remaining input bit. Hub dependence in a base function is witnessed by setting its other base bits all zero when \(r=1\), and to weight \(r-1\) generally. Hub-function dependence on a base input is witnessed by giving the other base bits weight \(r-1\). This proves the complete influence claim.

The vertices incident to \(D\) are precisely the right-hand side of (MB2), by (MB5). A vertex outside this set, and its antipode, have only zero incident edges. Every full path from one to the other contains a one, so its word begins and ends in zero with a one in between. Such a vertex is empty.

It remains to exhibit a monotone full word at every listed vertex. Since \(f\) is antipodally even, \(A_0(f)\) is antipodally invariant. Reversal therefore gives \(A_1(f)=A_0(f)\). It suffices to treat \(h=0\) and the three listed base weights; the other cases follow by antipodality. In the orders below, a downward base step toggles an initially one bit and an upward step toggles an initially zero bit; each chosen bit is used once.

If \(|x|=r\), traverse the hub first, then \(r\) downward/upward pairs, then the one remaining upward step. Equation (MB5) gives word \(1^{2r+1}0\).

If \(|x|=r+1\), take one downward step, traverse the hub, and then take \(r\) downward/upward pairs. The word is \(0\,1^{2r+1}\).

If \(|x|=r+2\), take \(r-1\) downward/upward pairs, three downward steps, and finally the hub. The word is \(1^{2r-1}0^3\). This includes \(r=1\), when the first block is empty.

All three orders use every direction once. They prove (MB2).

Counting (MB5) gives \(2m\binom{2r}{r-1}\) base edges and \(2\binom{2r+1}{r}\) hub edges in \(D\). The identity \(m\binom{2r}{r-1}=r\binom{2r+1}{r}\) gives (MB3). Counting the levels in (MB2) gives the root formula there. Finally,
\(\binom{2r+1}{r}/2^{2r+1}\sim1/\sqrt{\pi r}\) and
\(\binom{2r+1}{r-1}/\binom{2r+1}{r}=r/(r+2)\),
which prove (MB4). \(\square\)

**Consequence for the critical-repair route.** Inclusion minimality of a full-geodesic blocker, absence of monochromatic full geodesics, complete directed influence, and simultaneous healing of every nonempty minority repair are compatible with favorable-root density tending to zero. All minority-edge repairs can also activate the same originally empty antipodal root pair. A counting argument assigning repairs to newly favorable roots therefore requires additional information from paired-root absence in the original extremal facet. The family above has the paired roots displayed in (MB2), and every odd bridge extension of it satisfies NORI1 by the paired-root criterion.

An independent subset-state path evaluator verified (MB2), absence of both monochromatic full-path colors, the private pole-to-pole witness for every minority edge, and complete directed influence in dimensions four, six, and eight. The corresponding minority-edge counts were 12, 60, and 280, and the paired-root counts were 14, 50, and 182.


## Non-cut minimal geodesic blockers under two-sided blocking

For an arbitrary binary coloring of \(Q_d\), call \(D\subseteq E(Q_d)\) a **full-geodesic blocker** if every dimension-simple antipodal geodesic traverses an edge of \(D\). Call \(D\) inclusion-minimal if deletion of any one of its edges destroys the blocker property. An edge set is a **cut** when its indicator is of the form \(1_D(\{x,x+e_i\})=\phi(x)+\phi(x+e_i)\) for some Boolean vertex potential \(\phi\). A cut has even intersection parity with every cubical square.

**Theorem (dimension-uniform nonintegrable critical blockers).** For every \(d\ge4\), there is a coloring of \(Q_d\) with minority-colored edge class \(D_d\) such that:

1. Both \(D_d\) and its complement meet every full antipodal geodesic; hence the coloring has no monochromatic full geodesic of either color.
2. \(D_d\) is inclusion-minimal as a full-geodesic blocker. Every edge of \(D_d\) has a private full geodesic containing no other edge of \(D_d\).
3. \(D_d\) is not a cut: its indicator has odd sum on a cubical square.
4. \(|D_d|=13\cdot2^{d-4}\), and the coloring has \(|P(f)|=12\cdot2^{d-4}\) paired roots.

In particular, even the joint requirements of minority-blocker minimality and complementary-color geodesic blocking, valid in an imbalance-extremal hypothetical paired-root counterexample, do not force the minority edges to be a potential cut. The constructed colorings themselves are **not** paired-root counterexamples.

*Base coloring.* In \(Q_4\), encode an edge by \((i,x)\), where \(0\le i<4\), the \(i\)-th bit of \(x\) is zero, and the edge joins \(x\) to \(x+e_i\). Let
\[
\begin{split}
D_4=\{&(0,0),(0,2),\\
 &(1,0),(1,4),(1,5),(1,8),(1,9),(1,12),(1,13),\\
 &(2,1),(2,3),(3,1),(3,3)\}.
\end{split}\tag{NC1}
\]
Color these 13 edges one and the remaining 19 edges zero.

*Finite certificate.* Enumerate each starting vertex \(r\in\{0,\ldots,15\}\) and every permutation \(\pi\) of the four direction indices. At step \(t\), the edge is
\[
\left(\pi_t,\left(r\mathbin{\mathrm{xor}}\sum_{s<t}2^{\pi_s}\right)
\mathbin{\mathrm{and}}\neg 2^{\pi_t}\right).
\tag{NC2}
\]
All 384 rooted direction orders have between one and three edges of \(D_4\). Thus each color class is a blocker. An independent full-path dynamic program gives
\[
A_0(f)=\{0,2,4,5,6,7,8,9,10,11,12,13,14,15\}
\]
and
\[
P(f)=\{0,2,4,5,6,7,8,9,10,11,13,15\}.
\tag{NC3}
\]
To verify inclusion minimality without trusting any optimization solver, the following pairs \((e;\,r,\pi)\) give private witnesses: a rooted full geodesic starting at \(r\) and traversing directions \(\pi\) meets \(D_4\) only in edge \(e\):
\[
\begin{array}{c|c@{\qquad}c|c}
e&(r,\pi)&e&(r,\pi)\\
(0,0)&(3,1023)&(0,2)&(1,1023)\\
(1,0)&(0,1203)&(1,4)&(0,2103)\\
(1,5)&(0,2013)&(1,8)&(0,3102)\\
(1,9)&(0,3012)&(1,12)&(0,2310)\\
(1,13)&(0,2031)&(2,1)&(3,1203)\\
(2,3)&(1,1203)&(3,1)&(3,1302)\\
(3,3)&(1,1302)&&
\end{array}
\tag{NC4}
\]
The compact word \(1023\), for example, denotes the direction order \((1,0,2,3)\). The square in directions \(0,1\), based at \(x=0\), has four edges \((0,0),(1,0),(0,2),(1,1)\), precisely three of which belong to \(D_4\). Hence its parity is odd, so \(D_4\) is not a cut.

*All-dimensional extension.* For \(d>4\), identify \(Q_d=Q_4\times Q_{d-4}\). Color each first-four-direction edge according to \(D_4\), independently of its \(Q_{d-4}\) bit vector; color every remaining-direction edge zero. Let \(D_d\) be the resulting cylinder over \(D_4\). A full \(d\)-geodesic projects, after omitting steps outside the first four directions, to a full \(Q_4\) geodesic. It therefore uses both colors among those four steps, proving the two-sided blocking assertion.

To prove inclusion minimality, fix any lifted edge \((e,z)\in D_d\). Choose its private \(Q_4\) witness from (NC4), start with auxiliary bits \(\bar z\), traverse all auxiliary directions first, and then traverse the private \(Q_4\) path with auxiliary bits fixed at \(z\). There are no D-edges during the auxiliary prefix, and the \(Q_4\) segment has just the chosen lifted edge. This is a private full \(d\)-geodesic. The odd square persists in every four-bit fiber, proving non-cutness.

Finally, the coloring is the Cartesian product of the \(Q_4\) base coloring and constant-zero single-direction colorings. Paired-root sets multiply across independent factors, so (NC3) gives \(|P(f)|=12\cdot2^{d-4}\). The edge count follows from the cylinder construction. \(\square\)

**Closure consequence.** A paired-root-free extremal facet has a minimal minority geodesic blocker and a blocking majority complement. The theorem shows those two hypergraph conditions alone do not imply integrability into a vertex potential, even in unbounded dimension. The extra condition still unused in this construction is **paired-root absence**, which excludes (NC3). Any attempt to obtain a cut normal form for a hypothetical extremizer must exploit the full incompatibility of its rising and falling root certificates, rather than blocker minimality and two-sided monochromatic blocking alone.


## Antipodal private-witness compatibility uses paired-root absence

For a one-colored edge e of an ordinary coloring f, write Z_e for the roots z admitting a full path from z to bar z on which e is the sole one-colored edge. Equivalently, changing e to zero makes that path monochromatic zero.

**Theorem (antipodal private witnesses force four original paired roots).** If
\[
z\in Z_e\cap Z_{\bar e},
\]
then every endpoint of e and bar e belongs to P(f).

*Proof.* Orient the i-edge e as u to v according to the initial i-bit of z. Its antipodal edge is traversed in that same bit orientation as bar v to bar u. Choose private paths
\[
P:z\longrightarrow u\longrightarrow v\longrightarrow\bar z,\qquad
Q:z\longrightarrow\bar v\longrightarrow\bar u\longrightarrow\bar z.
\]
All segments other than the two displayed i-edges are zero. If S is the direction set before e in P, then the direction set before bar e in Q is T=[d]\setminus(S\cup\{i\}), because their starting points differ by the complement of all bits other than i.

From u, reverse the zero prefix of P, then follow the zero prefix of Q, then traverse bar e. These direction sets are S,T,{i}; the resulting full path to bar u has word 0^(d-1)1. Alternatively traverse e, then the zero suffix of P, then the reversed zero suffix of Q. Its word is 10^(d-1), again ending at bar u. Thus u is paired.

From v, follow the suffix of P, then the reversed suffix of Q, then traverse bar e backward. This gives 0^(d-1)1 to bar v. Traversing e backward and then the reversed prefix of P and the prefix of Q gives 10^(d-1) to bar v. Thus v is paired. Reversal supplies the same conclusion at bar u and bar v. QED.

**Corollary (rootwise antipodal exclusion for zero repairs).** In a paired-root-free coloring,
\[
Z_e\cap Z_{\bar e}=\varnothing
\]
for every antipodal edge pair whose two members are one-colored. For any fixed root, at most one member of each such pair can be a zero-repair witness. In particular, if a one-colored class D is itself antipodally invariant, each root activates at most |D|/2 of its single-edge zero repairs.

This uses paired-root absence in the original coloring, rather than only two-sided blocking or minimality. It explains why the sparse-root threshold example above can have all private repairs at the same poles: its boundary endpoints are already paired.

**Corollary (antipodally invariant minimal blockers have paired boundary).** Suppose D is an antipodally invariant full-geodesic blocker that is inclusion-minimal among antipodally invariant blockers. Color D one and its complement zero. Every vertex incident with D is paired.

*Proof.* For e in D, deleting the orbit {e,bar e} destroys blocking. A witnessing full path meets D only within that orbit. Since both edges have direction i and a full path uses i once, it meets precisely one member, say e. Antipodally translate this private path and reverse it. Antipodal invariance preserves all colors, so the resulting path starts at the same root and has bar e as its sole one. Apply the theorem. Every orbit has such a witness. QED.

The corollary does not assert that an arbitrary paired-root-free extremizer is an antipodally invariant minimal blocker. Odd bridge facets are arbitrary ordinary colorings, and minimum one-count among paired-root-free colorings guarantees healing to paired roots rather than healing to a monochromatic zero path. A repair may create only one previously missing monotone orientation at a root that already supported the other. Those cases must remain in the global implication argument.

**Independent check.** Full direction-order enumeration checked the theorem for all ordinary colorings in dimensions two and three, and for 300 random colorings in dimension four and 100 in dimension five. Among 4512 colorings there were 21952 ordered root/edge private-witness incidences with the antipodal mate also private at the same root. All four endpoints were paired in every case. The proof above is dimension-uniform and does not rely on this computation.

**Current closure plan.** The one-direction completion formula in the adjacent 2-SAT subsection retains the rising and falling full-path witnesses at every root. A complete proof would derive a variable and its negation in one strongly connected implication component for every exterior coloring. Square exchanges must be applied with their path endpoints; rootwise support projection alone is insufficient. The theorem above disposes of a specific shared-root antipodal zero-repair configuration. A general argument forcing a contradictory implication cycle, including repairs that create only a missing orientation, remains unproved.


### Joint antipodal paired repairs transport exclusive orientations

Let f have no paired root, and let e,bar e both have color one. Write f_e and f_(bar e) for the separate zero repairs. If a root z lies in P(f_e) intersect P(f_(bar e)), then z was originally exclusive: it belonged to precisely one of A_0(f),A_1(f).

Moreover orient e=u to v according to z's initial bit in its direction, so its mate is bar v to bar u. If z originally belonged to A_1(f), then
\[
u,\bar v\in A_0(f)\setminus A_1(f),\qquad
v,\bar u\in A_1(f)\setminus A_0(f).
\]
If z originally belonged to A_0(f), the two displayed orientation labels are interchanged.

*Proof.* If z was originally empty, both repaired orientations must use the changed edge. Write their common edge displacement from z as S. The prefix before that edge of the repaired ascending path is zero. The suffix after that edge of the repaired descending path is zero. Joining these two segments through the changed edge gives a full zero path after repair, since their direction sets are S, the changed direction, and its remaining complement. Thus z belongs to both Z_e and Z_(bar e), contrary to the preceding theorem and paired-root absence.

Suppose z originally belonged only to A_1. In each repair choose its newly created ascending path. The segment before the changed edge is zero. These two prefix direction sets are complementary within all directions other than the changed direction. Reversing the first prefix and following the second gives a zero path from u to bar v using all other directions. Appending bar e, which is one in f, yields an original ascending full path from u. Reversing the roles gives an ascending full path from bar v. Reversal gives the descending certificates at their antipodes v and bar u. Paired-root absence makes each membership exclusive. If z originally belonged only to A_0, use the zero suffixes of the newly created descending paths instead; they give ascending certificates at v and bar u and descending certificates at u and bar v. QED.

This condition retains orientation information that disappears when repairs are counted only by their root locations. It does not yet exclude shared repairs at an exclusive root. Nor does criticality force the requisite overlap between antipodal repair-root sets; a one-colored class may contain no antipodal edge pair. Closing the general implication graph requires additional compatibility across different directions.
