# Root-coupled topology and physical good-window carriers

# Root-coupled antipodal topology and genuine good-window carriers

Let \(c\) satisfy the ordered-three-face NORI law
\[
c(\bar F,\operatorname{rev}\pi)=1+c(F,\pi)
\]
on \(Q_n\). For a full rooted path \(P=(x,p_1,\ldots,p_n)\), denote its window word by \(w(P)=(w_1,\ldots,w_{n-2})\). At a fixed root \(x\), direction permutations form the vertices of the \((n-1)\)-dimensional permutohedron \(P_n\), whose boundary is an antipodal \((n-2)\)-sphere under reversal of the full direction order.

## Actual centered colors from full-sphere topology

Fix a distinguished direction \(i\), and two other directions \(a,b\). Put \(T=[n]\setminus\{i,a,b\}\), \(|T|=n-3\). For a full \(x\)-rooted direction order \(p\), let the projected \(i\)-edge position bit in direction \(j\in T\) be
\[
v_i(p)_j=x_j+\mathbf1_{\{j\text{ occurs before }i\}}.
\]
Under reversal of the full order this changes from \(v_i(p)_j\) to \(1-v_i(p)_j\). Define an actual central-face scalar
\[
h(p)=
\begin{cases}
2w_m(p)-1,&n=2m+1,\\
w_{m-1}(p)+w_m(p)-1,&n=2m.
\end{cases}
\]
Here the addition defining \(h\) is ordinary integer addition. Antipodal reversal of the full path reverses and complements the window word, so \(h(\operatorname{rev}p)=-h(p)\).

**Theorem 1 (genuine two-cap central-color packet).** On the boundary sphere, the odd map obtained by linearly extending
\[
\bigl((v_i(p)_j-\tfrac12)_{j\in T},h(p)\bigr)
 \in\mathbb R^{n-2}
\]
has a zero. This yields at most \(n-1\) actual full \(x\)-rooted geodesics in one common proper permutohedron face, with positive weights balancing every \(j\in T\) before and after \(i\) and balancing the central scalar. That carrying face has a one- or two-direction endpoint cap drawn from \(\{a,b\}\).

**Proof.** Both position and scalar components negate under central permutation reversal; affine extension on every proper face therefore defines an odd continuous map on the \((n-2)\)-sphere. Borsuk–Ulam forces a zero. A point in a proper permutohedron face is a convex combination of its vertices; applying Carathéodory in \(\mathbb R^{n-2}\) gives at most \(n-1\) full original orders. The weighted position equations say the positive-weight packet contains orders putting each \(j\in T\) on either side of \(i\). A proper permutohedron face has a common nonempty proper prefix support \(S\). If \(i\in S\), every \(j\in T\) must also be in \(S\), else \(j\) would be forced after \(i\); hence its terminal complement is a nonempty subset of \(\{a,b\}\). If \(i\notin S\), no \(j\in T\) can lie in \(S\), else \(j\) would be forced before \(i\); hence \(S\subseteq\{a,b\}\). This proves the endpoint-cap property. \(\square\)

For odd \(n\), central scalar balance supplies actual central physical ordered three-faces of both colors in the packet. Conditioning on the two color classes, each distinguished position bit has complementary conditional probabilities. Independent opposite-color packet choices then differ in each \(j\in T\) with probability at least \(1/2\); some pair has projected \(i\)-edge locations differing in at least \(\lceil(n-3)/2\rceil\) of those coordinates. These witnesses are genuine complete paths. Their central faces may occupy different physical positions and need not splice to a good path.

## Moving physical seam squares

Two full geodesics with the same root and the same prefix support \(S\) meet at the actual vertex \(y=x\oplus\chi_S\). Splicing the prefix of one to the suffix of the other creates exactly two new three-face windows, of ordered direction triples \((u,v,w)\) and \((v,w,t)\). The two physical faces share the free directions \(\{v,w\}\). Varying the starting root over the physical \(\{v,w\}\)-square leaves **both physical face objects** fixed, while exchanging adjacent directions at the seam changes their orders and the cut vertex. This gives a concrete two-dimensional seam-repair geometry.

Fixing the two seam directions ahead of the topological argument destroys the requisite antipodal index: the permutohedral cut complex forcing a prescribed pair to separate has an odd sign recording which direction comes first, mapping equivariantly to \(S^0\). Hence a viable fixed-point argument must let the physical square directions move with its carrying order. In addition, actual legal \(Q_9\) examples show that two paths with opposite median labels and a common central vertex can both have three changes, while both exchanged hybrid paths still have three changes. Opposite Tucker signs and a physical meeting do not by themselves imply defect descent.

## Path-certified good-window topology

Define \(W_c\) with vertices all ordered physical three-face windows. A set is a simplex precisely when one *actual* geodesic with at most one switch contains all its windows. Antipodal reversal \(\tau\) acts freely. Let \(m(F)\in\{0,\tfrac12,1\}^n\) be the physical face center and set
\[
d(u,v)=\|m(F_u)-m(F_v)\|_1.
\]
For two windows at positions \(r<s\) along one direction-distinct path, the center moves by exactly one unit in \(\ell^1\) under each consecutive window shift. Each physical coordinate moves monotonically, so \(d(u,v)=s-r\).

**Theorem 2 (exact grand extraction).** There exists a full good antipodal geodesic if and only if \(W_c\) has an edge \(uv\) with \(d(u,v)=n-3\).

**Proof.** The first and last ordered three-face windows of a full good path give such an edge. Conversely any edge has a genuine good-path certificate. Trimming that certificate between the specified windows gives \(3+d(u,v)=n\) distinct-coordinate moves, hence a full good path. \(\square\)

The intrinsic edge parity \(\beta(uv)=d(u,v)\bmod2\) is a cocycle: in any triangle of \(W_c\), a single certified path puts its three windows in positions \(r<s<t\), and
\[
\beta(uv)+\beta(vw)+\beta(uw)
=(s-r)+(t-s)+(t-r)=0\pmod2.
\]
Let \(\bar\beta\) denote its class on \(Y=W_c/\tau\), and let \(w\in H^1(Y;\mathbb F_2)\) classify the antipodal cover. Every five-direction cyclic physical window arrangement contains the mandatory five shift edges of an odd \(\beta\)-pentagon, lifted closed under \(\tau\). The number of compatible extra chord–triangle pairs in that local induced complex is precisely \(2\), \(4\), or \(5\), dictated by cyclic binary color alternation; each pair collapses to the original pentagon. Thus the two degree-one classes are genuine and independent, while abundant local triangles alone furnish no higher cup product.

**Theorem 3 (sharp cohomological degree).** For \(n\ge6\),
\[
\operatorname{ind}_{\mathbb Z_2}(W_c)\le n-4,
\qquad
\operatorname{ind}_{\mathbb Z_2}(W_c)\le n-5
\quad\text{if grand closure fails}.
\]
**Proof.** In a maximum-size simplex listing all consecutive windows of a good path of length \(k\ge5\), delete any internal window. The remaining consecutive ordered triples overlap in at least one direction. A direction appears exactly once in any geodesic, so these overlaps determine their original position differences and force the deleted triple. The extreme retained physical faces determine the root bits up to directions free in every face, which do not change any of the physical windows. Thus the deleted-window codimension-one face has a unique maximum-simplex extension: it is free. These free-face collapses can be performed in antipodal pairs, lowering the maximum dimension by one from the bound \(k-3\). Always \(k\le n\), and under failure \(k\le n-1\), yielding dimensions \(n-4\) and \(n-5\), respectively. \(\square\)

In particular any *nonzero degree-\((n-4)\) cohomology class on \(Y\)*, such as \(w^{n-4}\) or \(\bar\beta\smile w^{n-5}\), forces a full good path. The previous proposed target degree \(n-3\) is too high for \(W_c\) even when grand closure succeeds.

## The missing topological transition theorem

A concrete sufficient two-dimensional certificate is a path-certified annulus transporting an odd physical window pentagon \(P\) around a genuine path \(Q\) connecting one of its windows to its antipodal mate. If the homotopy \(P\simeq Q*(\tau P)*Q^{-1}\) is made of simplices certified by actual good paths, it descends to a torus in \(Y\). On that torus, \(\bar\beta\) and \(w\) pull back to \(a+\varepsilon b\) and \(b\), hence \(\bar\beta\smile w\) pulls back to \(a\smile b\ne0\). Existence of this annulus for arbitrary NORI colorings is not proved, and its degree-two class reaches the required degree only in dimension six. Independently, the static two-sided root-sheet Helly nerve has exact antipodal index three under grand failure for \(n\ge8\); accumulating static short-path witnesses cannot substitute for moving physical seams.

The central remaining task is a certificate-preserving map or dynamic repair construction that couples the honest full-permutohedral packets, moving seam squares, and cross-root good-window simplices strongly enough to force degree \(n-4\) or the equivalent distance-\((n-3)\) edge of \(W_c\). The unrestricted conjecture remains open.

## The passage from odd maps to physical certified simplices

The topology here has two separate layers. Full rooted direction orders live on an antipodal permutohedral boundary of dimension \(n-2\). Odd maps formed from actual central ordered-face colors and projected coordinate positions force genuine full-path packets; Carathéodory bounds their size and the carrying face leaves only one or two endpoint cap directions. This is a theorem about *actual geodesics*, but it does not ensure that two members share a repairable physical seam.

In contrast, the path-certified good-window complex \(W_c\) has a simplex only when one good geodesic contains all its ordered physical windows. Its intrinsic \(\ell^1\) face-center distance detects grand closure exactly through an edge of length \(n-3\). Under failure of grand closure the equivariant complex collapses to dimension at most \(n-5\), so a nonzero quotient cup class in degree \(n-4\) would force closure. The temporal cocycle and antipodal first Stiefel–Whitney class provide natural candidate factors, but a guaranteed global annulus and high-degree cup product have not been constructed.

The new Helly and root-sheet results show why merely raising the index of an ambient static witness space cannot fill this gap: an incompatible selector can have high index even while the genuine two-sided intersection remains empty. A moving physical seam complex, rather than a fixed pair of abstract central directions, is the appropriate remaining topological target.
