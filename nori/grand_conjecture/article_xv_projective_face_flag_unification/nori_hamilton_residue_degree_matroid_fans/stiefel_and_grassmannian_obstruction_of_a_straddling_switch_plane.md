# Stiefel and Grassmannian obstruction of a straddling switch plane

### The full Grassmannian homotopy obstruction of straddling switch planes

Let \(n=a+b\ge6\), with \(a,b\ge2\), \(A\sqcup B=[n]\), \(W=\{z\in\mathbb R^n:\sum z_i=0\}\), and \(D=P_a\times P_b\) the type-A dual top cell of Hamilton orders listing \(A\) before \(B\). Its dimension is \(d=n-2\), and \(W\cong\mathbb R^{d+1}\).

At every vertex \(\pi\in D\) choose ranks \(1\le k(\pi)<a\) and \(1\le\ell(\pi)<b\). Let
\[
x_\pi=Z_{k(\pi)}(\pi),\qquad
y_\pi=Z_{a+\ell(\pi)}(\pi).
\]
Interpolate the two vector assignments separately and affinely on any triangulation of \(D\) using its permutahedral vertices.

**Theorem 1 (canonical boundary plane obstruction).** The vectors \(x,y\) are independent on \(\partial D\). They therefore define an oriented 2-plane map
\[
\Psi:\partial D\cong S^{d-1}\longrightarrow\widetilde{\mathrm{Gr}}_2(W)
\]
and an orthonormal frame lift to \(V_2(W)\). The class of this map is a generator of
\[
\boxed{
\pi_{d-1}\bigl(\widetilde{\mathrm{Gr}}_2(\mathbb R^{d+1})\bigr)
\cong
\pi_{d-1}\bigl(V_2(\mathbb R^{d+1})\bigr)
\cong
\mathbb Z/\chi(S^d)\mathbb Z.
}
\tag{1}
\]
In particular this group is \(\mathbb Z\) for odd \(n\), and \(\mathbb Z/2\) for even \(n\); the class is nonzero in either case, and \(\Psi\) does not extend across \(D\). Its class is independent of the two rank-selection functions.

*Proof.* Set
\[
T=\sum_{i\in A}e_i-\frac an\mathbf1,\qquad
W\cap T^\perp=W_A\oplus W_B.
\]
At every vertex,
\[
x_\pi=\frac{k(\pi)}a T+u_\pi,\qquad
y_\pi=\frac{b-\ell(\pi)}b T+v_\pi,
\tag{2}
\]
where \(u_\pi\in W_A\) is the centered \(k(\pi)\)-prefix in \(A\) and \(v_\pi\in W_B\) is the centered \(\ell(\pi)\)-prefix in \(B\). The interpolated functions retain (2), with positive scalar coefficients \(\alpha,\beta\) and interpolated \(u,v\). On a boundary facet arising from a proper initial block \(S\subsetneq A\), the linear functional \(\sum_{i\in S}u_i\) is strictly positive on every vertex and therefore throughout that facet. Hence \(u\ne0\) there. On a facet arising from a proper initial block of \(B\), similarly \(v\ne0\). Since \(x=\alpha T+u\), \(y=\beta T+v\), with \(\alpha,\beta>0\), a dependence relation would force \(u=v=0\); this is impossible on \(\partial D\). Thus the boundary frame exists.

The first vector \(x\) is nowhere zero on the entire ball \(D\): \(\langle T,x\rangle>0\). It consequently extends into one open hemisphere of \(S(W)\), so the orthogonal complement bundle \(x^\perp\) on \(D\) has a trivialization canonically homotopic to the one obtained by projecting along \(x\) onto \(T^\perp\). The second-vector class in the fiber sphere can be represented by the nonzero boundary vector
\[
H=\iota_T(x\wedge y)
=\|T\|^2(\alpha v-\beta u)\in T^\perp.
\tag{3}
\]
On \(A\)-type facets the \(W_A\)-component of \(H\) has a strictly negative supporting sum, and on \(B\)-type facets the \(W_B\)-component has a strictly positive supporting sum. The radial boundary degree of \(H\) is therefore unchanged if all variable ranks are deformed linearly to any fixed interior ranks \(k_0,\ell_0\). For fixed ranks, (3) is a positive-weighted direct sum of the permutahedral prefix maps on \(P_a\) and \(P_b\), each of degree \(\pm1\) on its factor boundary. Their product has one zero with degree \(\pm1\), and hence the map \(H/\|H\|:\partial D\to S^{d-1}\) has degree \(\pm1\).

Finally consider the standard sphere fibration
\[
S^{d-1}\longrightarrow V_2(\mathbb R^{d+1})\longrightarrow S^d.
\]
Its long homotopy sequence gives
\[
\pi_d(S^d)\cong\mathbb Z
\xrightarrow{\ \partial\ }
\pi_{d-1}(S^{d-1})\cong\mathbb Z
\longrightarrow\pi_{d-1}(V_2)
\longrightarrow\pi_{d-1}(S^d)=0.
\]
The connecting map is multiplication by the Euler number of \(TS^d\), namely \(\chi(S^d)=1+(-1)^d\). Thus the image of the boundary fiber map of degree \(\pm1\) is a generator of the quotient group in (1). Since \(d\ge4\), the principal \(SO(2)\)-bundle \(V_2(W)\to\widetilde{\mathrm{Gr}}_2(W)\) induces an isomorphism on \(\pi_{d-1}\). The plane class is nonzero, proving nonextendibility. QED.

**Corollary 2 (unrestricted coloring application).** Suppose an unrestricted reversal-odd boundary 3-tournament has the property that, for every Hamilton order in the cell \(D(A|B)\), its first switch-prefix rank lies strictly inside \(A\), while its last switch-prefix rank lies strictly inside \(B\). The associated extreme-switch oriented plane labels possess the boundary interpolation of Theorem 1 and represent its nonzero homotopy class. This remains true when the switch ranks vary arbitrarily among the flags.

**Limitations and relation to the global obstruction.** This is a nonextendibility statement for a specified natural interpolation over one cell's boundary; other lower-dimensional fillings could alter its attaching class. It neither shows that every globally all-bad coloring has a straddling top cell nor rules out coherent alternative fillings over the full Coxeter sphere. The theorem upgrades the earlier contraction-degree obstruction: that degree is the integral fiber obstruction, whereas passage to the full oriented Grassmannian reduces it modulo the Euler number of the sphere tangent bundle.
