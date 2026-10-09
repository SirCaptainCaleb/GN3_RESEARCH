# Same-order endpoint-opposed geodesics simultaneously at antipodal roots for n≥8, via Kneser reversal-signature classes

# Simultaneous antipodal-root endpoint balance with ONE identical complete direction order

Let \(n\ge10\), let \(c\) color actual physical ordered 3-faces of \(Q_n\) and satisfy the active NORI law \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\). Let \(x_1,\ldots,x_t\) be ANY prescribed physical starting vertices (not necessarily distinct). Write \(\bar x_s=x_s\oplus[n]\). Define
\[
M_t=\frac{4^t+2^t}{2}.
\]
The theorem holds whenever \(n>3M_t\), and in particular for \(t=1\) in ALL \(n\ge10\), for \(t=2\) in ALL \(n\ge31\).

**Theorem (same-order antipodal root-pair synchronization).** Under \(n>3M_t\), there exists a **SINGLE full coordinate permutation**
\[
\pi=(p_1,\ldots,p_n)
\]
such that for EVERY \(s\in[t]\), BOTH actual full antipodal geodesics rooted at \(x_s\) and at \(\bar x_s\), using the IDENTICAL ordered directions \(\pi\), have OPPOSITE first and last ordered-three-face colors:
\[
w_1(x_s,\pi)\ne w_{n-2}(x_s,\pi),\qquad
w_1(\bar x_s,\pi)\ne w_{n-2}(\bar x_s,\pi).
\tag{1}
\]
More strongly, the initial three directions \(\alpha=(p_1,p_2,p_3)\) and final three directions \(\gamma=(p_{n-2},p_{n-1},p_n)\) can be fixed so that **EVERY** order of the other \(n-6\) directions works for all \(2t\) roots simultaneously. Thus an entire genuine \((n-7)\)-dimensional middle-order permutohedral face, with \((n-6)!\) actual permutations, has this endpoint-opposition property at all the selected antipodal root pairs.

**Proof: the exact endpoint colors.** For a root \(x\), let \(h_x(u,v,w)\) be the color of the physical ordered face **through \(x\)** with ordered free triple \((u,v,w)\). For any full order \(\pi\) with first triple \(\alpha\) and last triple \(\gamma\), actual physical face geometry and active NORI oddness imply
\[
w_1(x,\pi)=h_x(\alpha),\qquad
w_{n-2}(x,\pi)=1\oplus h_x(\operatorname{rev}\gamma).
\tag{2}
\]
The corresponding formulas at the ANTIPODAL root, using \(h_{\bar x}(\delta)=1\oplus h_x(\operatorname{rev}\delta)\), are
\[
w_1(\bar x,\pi)=1\oplus h_x(\operatorname{rev}\alpha),\qquad
w_{n-2}(\bar x,\pi)=h_x(\gamma).
\tag{3}
\]
Therefore both endpoints are oppositely colored for BOTH roots precisely when
\[
\boxed{h_x(\alpha)=h_x(\operatorname{rev}\gamma),\qquad
h_x(\operatorname{rev}\alpha)=h_x(\gamma).}
\tag{4}
\]

**A self-contained disjoint-3-set coloring lemma.** Partition the 3-subsets of \([n]\) into \(M\) types. If \(n>3M\) and \(n\ge10\), two DISJOINT 3-subsets necessarily have the same type. Indeed any family \(\mathcal F\) of pairwise intersecting 3-subsets has size at most \(\binom{n-1}{2}\). To see this without any external theorem, place the \(n\) directions uniformly at random on a circle and consider the \(n\) cyclic intervals of three consecutive positions. At most THREE of these intervals can belong to a pairwise-intersecting family: choose any one interval occupying positions \(0,1,2\); another intersecting it must start at \(-2,-1,0,1,\) or \(2\), and any four of these five starts include two separated by 3 or 4 positions, whose three-position intervals are disjoint for \(n\ge10\). Each fixed 3-subset is a cyclic interval with probability \(n/\binom n3\). Thus
\[
|\mathcal F|\,n/\binom n3\le3,\qquad
|\mathcal F|\le 3\binom n3/n=\binom{n-1}{2}.
\]
If no two 3-subsets of the same type were disjoint, every type class would be intersecting and hence
\[
\binom n3\le M\binom{n-1}{2}=M(3/n)\binom n3,
\]
contradicting \(n>3M\).

**Apply the lemma to the NORI order-reversal signatures.** For each UNORDERED 3-set \(T\subset[n]\), choose one ordered orientation \(\alpha_T\) arbitrarily and form its actual binary **paired-root reversal signature**
\[
H(T)=\bigl(h_{x_s}(\alpha_T),h_{x_s}(\operatorname{rev}\alpha_T)\bigr)_{s=1}^t\in\{0,1\}^{2t}.
\tag{5}
\]
Let \(\iota\) exchange the two bits within EACH ordered pair; this is the action on \(H\) induced by reversing the ordered triple. Among \(2^{2t}=4^t\) possible signatures, exactly \(2^t\) are fixed by \(\iota\). Thus the number of \(\iota\)-orbits is
\[
\frac{4^t+2^t}{2}=M_t.
\]
Color each unordered 3-set \(T\) by the \(\iota\)-orbit of \(H(T)\). Since \(n>3M_t\), the disjoint-set lemma produces **disjoint** triples \(A,B\) having the same orbit type. Choose ordered orientations \(\alpha\) of \(A\) and \(\gamma\) of \(B\) such that
\[
H(\alpha)=\iota H(\gamma).
\]
This can always be done because signatures in the same orbit differ by at most \(\iota\), and reversing the orientation of either triple applies \(\iota\). The equality is exactly the TWO equations (4) for every \(x_s\) simultaneously. Put \(\alpha\) in positions 1,2,3, put \(\gamma\) in positions \(n-2,n-1,n\), and order the remaining \(n-6\) distinct directions arbitrarily. Equations (2)-(4) show that this **identical full order** has endpoint-opposed color words at all \(x_s,\bar x_s\), for every possible middle order. \(\square\)

**Corollary (an actual shared-support Boolean corridor at antipodal roots).** For every cut rank \(\ell\in\{3,\ldots,n-3\}\), the above synchronized path packet contains EVERY prefix support
\[
S=A\cup R,\quad R\subseteq[n]\setminus(A\cup B),\quad |R|=\ell-3.
\]
Thus the actual intermediate physical vertices of all certified endpoint-opposed paths, from root \(x_s\), comprise the entire rank-(\(\ell-3\)) layer of a genuine \((n-6)\)-coordinate cube translated by \(x_s\oplus A\); from \(\bar x_s\) they are the ANTIPODES of these vertices, using the SAME full order choices. This is a literal antipodal root-coupled Boolean corridor of genuine FULL geodesics, not an interpolated zero-level cover or an abstract common face.

**Why this is stronger and what remains missing.** The previous multi-root Borsuk–Ulam theorem guarantees, for any \(t\le n-2\) roots, different endpoint-opposed permutations in one common permutohedral face. The current theorem instead guarantees the **same permutation and an entire middle-order permutohedral face** for every root and its antipode, under the indicated logarithmic-in-\(n\) number of root pairs. It uses a simple cyclic disjoint-triple count, not a new literature assumption. But endpoint-opposed full paths can have three or more internal switches. The common order/corridor gives exact geometric compatibility across many roots, not yet the complementary MONOCHROMATIC reversed-tail support collision required for unrestricted NORI closure. The correct next step is to exploit actual interior-face overlaps as the two synchronized antipodal rooted paths traverse this complete Boolean corridor.

## Topological Kneser strengthening: the sharp dimension threshold \(n\ge8\)

The self-contained cyclic-interval proof above needs \(n>3M_t\). A stronger bound follows immediately from the **classical Kneser chromatic theorem**
\[
\chi(KG(n,k))=n-2k+2\qquad(n\ge2k),
\]
where \(KG(n,k)\) has k-subsets as vertices and edges joining disjoint subsets. This is an established topological combinatorics result, invoked here as a named theorem **without a new literature search**; it is NOT proved in this Item.

**Corollary (Kneser-topological optimal alphabet bound).** With the identical definitions of roots, reversal signatures and orbit-types, the same-direction-order simultaneous endpoint-opposition conclusion holds whenever
\[
\boxed{n-4>M_t=\frac{4^t+2^t}{2},\quad\text{i.e.}\quad n\ge M_t+5.}
\tag{6}
\]
In particular:
\[
\begin{array}{c|c|c}
t\text{ prescribed root/antipode pairs}&M_t&\text{sufficient dimension}\\\hline
1&3&n\ge8,\\
2&10&n\ge15,\\
3&36&n\ge41,\\
4&136&n\ge141.
\end{array}
\]
The assertion for \(t=1,n\ge8\) is especially relevant: **EVERY antipodal physical root pair in active NORI admits one IDENTICAL full ordered-direction permutation with opposite first/last face colors at BOTH roots**, and all \((n-6)!\) middle-order permutations between a suitable fixed first ordered triple and last ordered triple work simultaneously.

**Proof.** The proof above colors all unordered 3-direction sets by one of the \(M_t\) orbits of their paired-root reversal signatures. If no two DISJOINT triples had the same orbit color, it would be a proper \(M_t\)-coloring of \(KG(n,3)\). But the classical Kneser chromatic formula gives \(\chi(KG(n,3))=n-4>M_t\), a contradiction. The resulting two disjoint same-orbit triples supply, word for word, the same oriented first/last triple packet as in the self-contained proof. \(\square\)

**Sharpness as a pure orbit-coloring consequence.** The inequality \(n-4>M_t\) is the precise threshold at which the *arbitrary* \(M_t\)-coloring of the Kneser graph MUST possess a monochromatic edge. It is NOT claimed to be the sharp dimension threshold for active NORI itself when additional physical-face constraints are exploited: the h-signature orbit coloring might have extra structure. The corollary is a legitimate use of a genuine **topological fixed-point-derived chromatic theorem**, making the earlier disjoint-triple synchronization part of the topology-first research program rather than isolated pigeonhole counting. The original self-contained n>3M_t theorem remains available without invoking Kneser's theorem.
