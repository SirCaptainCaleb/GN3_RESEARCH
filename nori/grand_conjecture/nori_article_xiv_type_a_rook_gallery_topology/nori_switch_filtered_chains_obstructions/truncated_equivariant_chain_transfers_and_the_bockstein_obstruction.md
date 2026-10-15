# Truncated equivariant chain transfers and the Bockstein obstruction

# Bockstein obstruction for truncated equivariant chain transfers

Put \(G=\mathbb Z_2=\{1,\tau\}\) and \(R=\mathbb F_2[G]\). For a finite free \(G\)-simplicial complex \(X\), its simplicial chain complex \(C_*(X;\mathbb F_2)\) consists of free \(R\)-modules. Call an \(R\)-linear chain map *augmented* if it preserves the standard augmentation to \(\mathbb F_2\).

**Theorem 1 (index naturality without a continuous map).** Suppose \(f:C_*(X)\to C_*(Y)\) is an augmented \(G\)-equivariant chain map between finite free \(G\)-complexes. If \(\alpha_X\) and \(\alpha_Y\) are the classes in \(H^1(X/G;\mathbb F_2)\) and \(H^1(Y/G;\mathbb F_2)\) classifying their respective double covers, then the induced cohomology map satisfies
\[
\boxed{f^*(\alpha_Y^j)=\alpha_X^j\quad(j\ge0).}
\tag{1}
\]
Consequently \(\alpha_X^q\ne0\) and \(\alpha_Y^q=0\) prohibit such a chain map.

*Proof.* The group algebra has a non-split short sequence of \(R\)-modules
\[
0\longrightarrow\mathbb F_2
\xrightarrow{1\mapsto1+\tau}R
\xrightarrow{\varepsilon}\mathbb F_2
\longrightarrow0.
\tag{2}
\]
The connecting morphism \(\delta_X\) of the induced cohomology long sequence on \(\operatorname{Hom}_R(C_*(X),-)\) equals cup product with the covering class: \(\delta_X(z)=\alpha_X\smile z\). This follows by identifying (2) as the pullback of the universal degree-one extension class from \(B\mathbb Z_2\). The same holds for \(Y\).

The modules \(C_i(X)\) and \(C_i(Y)\) are free over \(R\), so Hom applied to (2) is a short sequence of cochain complexes. The equivariant chain map \(f\) gives commuting connecting morphisms \(f^*\delta_Y=\delta_Xf^*\). Augmentation preservation gives \(f^*(1)=1\) in degree zero. Consequently
\[
f^*(\alpha_Y^j)=f^*(\delta_Y^j1)
=\delta_X^j f^*(1)=\delta_X^j1=\alpha_X^j.
\]
No multiplicative cochain map or underlying space map is needed. \(\square\)

Let \(\Sigma_n\) be the type-\(A_{n-1}\) Coxeter complex. Its vertices are the proper nonempty subsets \(S\subset[n]\), and its simplices are strict chains of those subsets. Complementation \(S\mapsto[n]\setminus S\) is the antipodal involution on \(|\Sigma_n|\cong S^{n-2}\). The quotient is \(\mathbb RP^{n-2}\), up to equivariant homeomorphism. Its \(q\)-skeleton \(\Sigma_n^{(q)}\) is invariant under this involution and has
\[
\boxed{\alpha_{\Sigma_n^{(q)}}^q\ne0\quad(0\le q\le n-2).}
\tag{3}
\]
Indeed the inclusion of the quotient \(q\)-skeleton into the entire quotient is injective on degree-\(q\) cohomology: both cellular complexes have the same degree-\(q\) cochains and the same incoming coboundary. The restriction of the nonzero projective class remains nonzero.

**Theorem 2 (half-dimensional truncated-chain criterion for NORI1).** Let \(n\ge5\) and let \(c\) be an antipodally odd coloring of \(Q_n\). Put
\[
K_a(c)=\Delta P_a(c),\quad K(c)=K_0(c)\cup K_1(c),
\quad m=\left\lfloor\frac{n-3}{2}\right\rfloor,\quad
q=m+1=\left\lfloor\frac{n-1}{2}\right\rfloor.
\tag{4}
\]
The involution on \(K(c)\) is \(R(u,v)=(\bar v,\bar u)\), which interchanges red and blue endpoint complexes.

If \(c\) has no monochromatic full antipodal geodesic, then **no** augmented \(G\)-equivariant chain map
\[
\boxed{
C_*(\Sigma_n^{(q)};\mathbb F_2)
\longrightarrow
C_*(K(c);\mathbb F_2)
}
\tag{5}
\]
exists. Hence a construction of (5) for every hypothesized counterexample would prove NORI1 in dimension \(n\).

*Proof.* By the two-color rank-jump theorem in Article XIV, the no-closure hypothesis produces an equivariant map \(K(c)\to S^m\). Therefore the covering class \(\alpha_K\) satisfies \(\alpha_K^{m+1}=0\). The involution on \(K(c)\) is free: its fixed interval vertices would represent full antipodal monochromatic geodesics, while interval ranks increase strictly within each chain. On the source, (3) implies \(\alpha_{\Sigma_n^{(q)}}^q\ne0\) because \(q\le n-2\). Since \(q=m+1\), Theorem 1 prohibits (5). \(\square\)

**Smallest required skeleton.** The proof criterion uses chains only through dimension \(q=\lfloor(n-1)/2\rfloor\), not the entire Coxeter sphere of dimension \(n-2\). For \(n=5,6\), \(q=2\); for \(n=7,8\), \(q=3\); and for \(n=9,10\), \(q=4\). This specifies the degree at which any hypothetical compatible chain assignment must fail.

**Connection to the new matroid-Sperner toolkit entry.** On the signed-direction partition matroid with parallel classes \(\{i^+,i^-\}\), independent sets use each dimension at most once and flats are unions of complete classes. Ordered maximal chains of its Boolean lattice of flats form the same type-A Coxeter complex \(\Sigma_n\). This is the natural ordered-flat-chain *source* supplied by the 2015 Andrade–Rodríguez Rey–Ruiz Sandoval construction. The matroid theorem does **not** itself construct (5): independent dimension labels do not force compatible monochromatic ordered paths. The target \(K(c)\) retains such path witnesses, and the missing argument must choose coherent, augmented, equivariant chains across rank exchanges.

**Interpretation.** The full punctured affine torus and a continuous transfer map are sufficient but unnecessary for a chain-level Wu–Yang argument. The stronger, smaller target is a support-respecting mod-two transfer through a half-dimensional skeleton of one type-A Coxeter sphere. The square and polar three-cell obstructions previously found in Article XIV identify possible early failure mechanisms; this theorem supplies a precise cohomological obstruction degree but does not yet construct the transfer or prove NORI1.
