# Affine antipodal cube colorings force straddling top-cell Grassmannian obstructions

# Affine antipodal cube colorings obstruct canonical straddling top-cell fillings

This construction shows that the nonzero top-cell switch-plane degree from Article XV is realizable by **legal cube-edge colorings**, not only by boundary 3-tournament colorings. It occurs in every ambient cube dimension \(n\ge6\), including the sparse dimensions \(n=2^r+1\) relevant to the Grassmannian reduction.

Fix a partition \([n]=A\sqcup B\) with \(a=|A|\ge2\), \(b=|B|\ge2\), and choose fixed-point-free permutations \(\sigma_A\in S_A\), \(\sigma_B\in S_B\). Let \(\sigma=\sigma_A\sigma_B\). Define the affine edge coloring
\[
\boxed{c(\{x,x\oplus e_i\})=x_{\sigma(i)},\qquad i\in[n].}
\tag{1}
\]
The right-hand side is independent of the choice of endpoint because \(\sigma(i)\ne i\). Under global antipodality \(x\mapsto\bar x\), its bit is complemented, so (1) is antipodally odd.

Consider all \(a!b!\) complete cube geodesics rooted at \(0^n\) whose dimension orders list all members of \(A\) before all members of \(B\). Their permutations are the vertices of the top two-block dual Coxeter cell
\[
D(A|B)=P_a\times P_b,\qquad \dim D=n-2.
\]

**Theorem 1 (three compulsory switches in every two-block flag).** Every such geodesic has at least one color switch at a rank strictly between \(1\) and \(a-1\), a switch at rank \(a\), and at least one switch at a rank strictly between \(a+1\) and \(n-1\). In particular every cell vertex has at least three switches, with first switch rank \(p<a\) and final switch rank \(q>a\).

*Proof.* For every direction \(i\), its edge color is the value of the \(\sigma(i)\)-th bit immediately before direction \(i\) is toggled. Since the geodesic begins at \(0^n\) and uses each dimension once, this bit equals one if \(\sigma(i)\) has already appeared in the dimension order and zero otherwise. Because \(\sigma\) preserves each of \(A,B\), the first direction encountered in either block has color zero; its successor under \(\sigma\) belongs to the same block and has not yet been used. The last direction encountered in either block has color one, since its distinct \(\sigma\)-successor belongs to the same block and must already have been used. Thus each block's color subword begins with zero and ends with one, forcing an internal switch. At their common boundary the last \(A\)-edge has color one while the first \(B\)-edge has color zero, forcing a further switch. The first and final switch ranks lie strictly inside \(A,B\), respectively. \(\square\)

When \(a=b=3\) and both permutations are three-cycles, each three-letter block has precisely one internal switch, hence **all 36 rooted six-dimensional geodesics in \(D(A|B)\) have precisely three switches**, with their full color words of the form \(0,0,1,0,0,1\), \(0,1,1,0,1,1\), or the analogous combinations of the two block patterns.

**Theorem 2 (an explicit nonfillable Grassmannian boundary class).** Let \(n\ge6\) and use coloring (1). For each \(\pi\in D(A|B)^{(0)}\), let \(S_\pi\) denote its switch-prefix ranks. Let
\[
Z_j(\pi)=\sum_{h\le j}e_{\pi_h}-\frac jn\mathbf1,\quad
T=\mathbf1_A-\frac an\mathbf1,
\quad
\mathcal B(\pi)=\sum_{\substack{p<q\\p,q\in S_\pi}}Z_p(\pi)\wedge Z_q(\pi).
\]
The piecewise-affine boundary interpolation of
\[
\boxed{H(\pi)=\iota_T\mathcal B(\pi)\in T^\perp\cap W}
\tag{2}
\]
is nowhere zero and represents a map \(\partial D\to S(T^\perp\cap W)\cong S^{n-3}\) of degree \(\pm1\). Hence its oriented-plane lift
\[
\boxed{x\longmapsto
\bigl(\operatorname{span}^{+}\{T,H(x)\}\bigr)}
\tag{3}
\]
defines a nonextendible boundary map into \(\widetilde{\operatorname{Gr}}_2(W)\). Its obstruction is the nonzero generator of \(\mathbb Z\) for odd \(n\), and of \(\mathbb Z/2\) for even \(n\).

*Proof.* Theorem 1 supplies, at each vertex, a switch rank \(p<a\) and another \(q>a\). The universal full-quadratic switch-bivector degree theorem in the Hamilton-residue section of Article XV applies to any such family of nonempty switch sets. It proves that affine interpolation of (2) avoids zero on the entire boundary and has degree \(\pm1\). For the plane (3), the fixed vector \(T\) is independent of the coloring and \(H(x)\perp T\). Therefore its image lies in the \(T\)-containing plane sphere, identified with \(S^{n-3}\) by the positive-prefix Stiefel retraction of Article XV. The inclusion of this sphere into the oriented two-plane Grassmannian sends a degree-one generator to the generator of
\[
\pi_{n-3}(\widetilde{\operatorname{Gr}}_2(\mathbb R^{n-1}))
\cong\mathbb Z/\chi(S^{n-2})\mathbb Z.
\]
For \(n\ge6\), this is \(\mathbb Z\) when \(n\) is odd and \(\mathbb Z/2\) when \(n\) is even. Hence the boundary plane map cannot extend over the top ball \(D\). \(\square\)

**Corollary 3 (the sparse power-of-two-plus-one obstruction is realized by legal cube colorings).** For every \(r\ge3\), the dimension \(n=2^r+1\) admits a legal affine coloring (1) and a two-block Coxeter top cell whose canonical full-quadratic switch-plane boundary map represents a nonzero **integral** Grassmannian homotopy class. One may take \(|A|=3\), \(|B|=n-3\), and cyclic derangements on both blocks.

**Scope and distinction.** These are **local** cell nonextension examples. The affine coloring (1) is not asserted to lack a monochromatic full antipodal geodesic globally; for example, in the \(3+3\) case it has one from an appropriately chosen nonzero root. Thus the result does not refute the conditional global Grassmannian criterion for NORI1. It does refute any strategy claiming that legal antipodal oddness and the absence of a good **flag inside a chosen top cell**, by themselves, make the canonical switch-plane boundary nullhomotopic. A global proof must exploit compatibility across multiple cells, alter lower-cell fillings coherently, or use some feature peculiar to a global counterexample that the present local colorings do not possess.

## Signed straddling degree as a product of root-zonotope carriers

Write \(D=P_A\times P_B\) for the two-block permutahedral cell, with \(|A|=a\ge2\), \(|B|=b\ge2\), and orient it by \(W_A\oplus W_B\). For any connected graph \(G\) on a block \(E\), write
\[
z_G(\pi)=\tfrac12\sum_{\{i,j\}\in E(G),\,i<j}
\epsilon_{ij}(\pi)(e_i-e_j)
\]
for its oriented graphical-zonotope label. For any nonempty proper first subset \(S\subset E\), all refining permutations satisfy
\[
\boxed{\sum_{i\in S}z_G(\pi)_i=|\partial_G S|/2>0.}
\tag{4}
\]

**Theorem 3 (straddling-degree homotopy).** Let \(H(\pi_A,\pi_B)\in W_A\oplus W_B\) be the contracted *full quadratic switch bivector* in the preceding Article XV theorem, assuming every two-block flag has switch ranks strictly inside both \(A\) and \(B\). For **any connected graphs** \(G_A,G_B\) on the blocks, put
\[
\boxed{\mathcal R(\pi_A,\pi_B)=
-z_{G_A}(\pi_A)\oplus z_{G_B}(\pi_B).}
\tag{5}
\]
The piecewise-affine boundary maps \(H,\mathcal R:\partial D\to W_A\oplus W_B\setminus\{0\}\) are joined by a zero-free straight-line homotopy. Their radial maps have the same signed Brouwer degree; with the product orientation this degree is
\[
\boxed{\deg(H/\|H\|)=(-1)^{a-1}.}
\tag{6}
\]

*Proof.* The full-quadratic switch sign-cone theorem gives \(\sum_{i\in S}H_i<0\) on every facet \(F_S\times P_B\), and \(\sum_{i\in U}H_i>0\) on every facet \(P_A\times F_U\). The cut identity (4) gives the same strict signs for \(\mathcal R\), using its negative \(A\)-component. Therefore on each boundary facet both families of labels and their straight-line interpolations remain in one common strict halfspace. All piecewise-affine boundary maps in this homotopy avoid zero.

Deform each connected graph label to the complete-graph permutahedral label:
\[
z_{G,t}=z_G+t z_{K_E\setminus G},\qquad 0\le t\le1.
\]
Every nonempty proper cut continues to satisfy the strict positive cut inequality, so the corresponding product boundary maps remain nonzero. At \(t=1\), the product map is the linear reflection \((u_A,u_B)\mapsto(-u_A,u_B)\) of the original product permutahedron. Its determinant sign, and thus its boundary degree, is \((-1)^{\dim W_A}=(-1)^{a-1}\). Homotopy invariance proves (6). \(\square\)

**Corollary 4 (block-cycle affine colors).** For the legal affine colorings of the preceding two-block obstruction theorem, choose a single permutation cycle on each block (each of length at least three). The monochromatic root selector of Article XIV, followed by the linear incidence transformation of each cycle, gives \(z_{C_A}\) and \(z_{C_B}\). The local switch-plane obstruction is therefore homotopic, after its standard contraction, to the product of two degree-one root transports, with the \(A\)-factor sign reversed.

**Scope.** Once every flag straddles the cut, the signed local degree depends only on the block size \(a\), not on the switch positions or the coloring. Even colorings with many monochromatic full paths exhibit this local obstruction. Global closure must therefore constrain how the blockwise degree carriers fit together under exchanges and root mobility; isolated top-cell nonextendibility cannot by itself establish NORI1.
