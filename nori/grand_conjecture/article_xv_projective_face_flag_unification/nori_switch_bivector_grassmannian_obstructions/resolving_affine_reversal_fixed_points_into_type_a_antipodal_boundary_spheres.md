# Resolving affine reversal fixed points into type-A antipodal boundary spheres

### Resolving affine reversal fixed points into type-A antipodal boundary spheres

The endpoint-symmetric affine chamber torus constructed in the preceding Subsection realizes the cube's color-complementing, order-reversing flag involution \(R(x;\pi)=(x;\pi^{\mathrm{rev}})\) geometrically, but \(R\) has isolated fixed points. Resolving these points yields a **free involution with the full projective cohomological index restored**. The new boundary spheres carry precisely the type-A dimension-order chambers arising at fixed cube roots. This offers an equivariant source in which both root changes and rooted type-A opposition are visible.

Fix \(n\ge3\) and write \(\mathbb T_n=(\mathbb R/2\mathbb Z)^n\), with its endpoint-symmetric affine chamber decomposition. As above, \(R(t)=\mathbf1-t\) and chambers are labeled by root signs \(x\in\mathbb F_2^n\) and magnitude permutations \(\pi\in S_n\).

**Theorem 1 (fixed points and their Coxeter links).** The involution \(R\) has precisely \(2^n\) fixed points, naturally indexed by cube roots \(x\):
\[
\boxed{p_x=\bigl((-1)^{x_i}/2\bigr)_{i=1}^n\pmod{2\mathbb Z^n}.}\tag{1}
\]
Near \(p_x\), let \(u_i=(-1)^{x_i}(t_i-(p_x)_i)\). The local chamber walls are
\[
\boxed{u_i=u_j\qquad(1\le i<j\le n),}\tag{2}
\]
the braid arrangement. The induced decomposition of a sufficiently small linking sphere \(S^{n-1}\) is the suspension of the type-\(A_{n-1}\) Coxeter sphere
\[
\boxed{S\bigl(\{u:\sum_i u_i=0\}\bigr)\cong S^{n-2}.}\tag{3}
\]
The involution acts as \(u\mapsto-u\) on this link, and as permutation reversal on its \(n!\) equatorial Coxeter chambers.

*Proof.* The fixed point equation \(t=\mathbf1-t\pmod2\) is \(2t_i=1\pmod2\) in each component, yielding the representatives \(t_i=\pm1/2\) and hence (1). Each lies away from the sign walls \(|t_i|=0,1\). For \(t\) close to \(p_x\), one has \(|t_i|=1/2+u_i\), so the only chamber walls through \(p_x\) are the equalities (2). The common intersection of these hyperplanes is the diagonal line \(\mathbb R\mathbf1\); in the perpendicular hyperplane \(W=\{u:\sum_i u_i=0\}\), they form the essential type-A braid arrangement. The unit link \(S^{n-1}=S(\mathbb R\mathbf1\oplus W)\) is the suspension of \(S(W)\), and its arrangement decomposition is the suspension of the braid-arrangement sphere. Finally \(R(p_x+\delta)=p_x-\delta\), so its derivative is negation. A chamber labeled by increasing \(u_{\pi_1}<\cdots<u_{\pi_n}\) is carried to the reversed-order chamber. \(\square\)

**Theorem 2 (a free reversal carrier).** Choose disjoint sufficiently small open Euclidean balls \(B_x\) around the points \(p_x\), invariant under \(R\). Define
\[
\boxed{M_n=\mathbb T_n\setminus\bigcup_{x\in\mathbb F_2^n}B_x.}\tag{4}
\]
Then \(M_n\) is a connected compact \(n\)-manifold with \(2^n\) spherical boundary components. The involution \(R\) is free on \(M_n\), acts antipodally on each boundary sphere, and preserves the truncated full-path chamber decomposition. Its quotient \(N_n=M_n/R\) is a compact \(n\)-manifold whose \(2^n\) boundary components are
\[
\boxed{\partial_xN_n\cong\mathbb RP^{n-1}.}\tag{5}
\]
Each \(\partial_xM_n\) contains an invariant type-A Coxeter equator \(S^{n-2}\) with the usual antipodal action and dimension-order chamber labels.

*Proof.* The fixed point set is the finite set (1). Small balls in the flat torus can be chosen disjoint and invariant under the point-reflection \(R\), since it acts as \(-I\) in their centered local charts. All fixed points are removed by (4), making the action free. Every boundary is a small unit sphere on which \(R\) is antipodal; its quotient is \(\mathbb RP^{n-1}\). Removing finitely many disjoint open balls from a connected \(n\)-torus leaves it connected for \(n\ge2\). The chamber walls are linear near the removed centers by (2), so truncating their cells yields a compatible chamber decomposition whose maximal regions retain their original labels \((x;\pi)\). The equator and its opposition are supplied by Theorem 1. \(\square\)

Let \(\alpha\in H^1(N_n;\mathbb F_2)\) classify the connected double cover \(M_n\to N_n\).

**Theorem 3 (full restoration of projective index).** For every \(0\le k\le n-1\),
\[
\boxed{\alpha^k\ne0\ \text{in }H^k(N_n;\mathbb F_2),\qquad
\alpha^n=0.}\tag{6}
\]
Moreover the integral Bockstein is nonzero:
\[
\boxed{\beta(\alpha)\ne0\ \text{in }H^2(N_n;\mathbb Z).}\tag{7}
\]
Consequently there is no \(R\)-equivariant continuous map
\[
\boxed{M_n\longrightarrow S^{n-2}}\tag{8}
\]
with the antipodal action on the target. The highest nonzero power of the covering class is \(n-1\), matching the projective index of a free antipodal \((n-1)\)-sphere.

*Proof.* Restrict the double cover to any boundary component \(\partial_xN_n\cong\mathbb RP^{n-1}\). By Theorem 2, it is the standard antipodal cover \(S^{n-1}\to\mathbb RP^{n-1}\). Thus \(\alpha\) restricts to the canonical generator \(a\in H^1(\mathbb RP^{n-1};\mathbb F_2)\). The ring \(H^*(\mathbb RP^{n-1};\mathbb F_2)=\mathbb F_2[a]/(a^n)\) has \(a^k\ne0\) for \(0\le k\le n-1\). Therefore \(\alpha^k\) is nonzero on \(N_n\) in each of these degrees. Since \(N_n\) is connected, compact, and has nonempty boundary, its absolute top mod-two cohomology vanishes, so \(\alpha^n=0\).

For \(n\ge3\), the Bockstein of \(a\) for \(0\to\mathbb Z\xrightarrow{\times2}\mathbb Z\to\mathbb F_2\to0\) is the nonzero element of \(H^2(\mathbb RP^{n-1};\mathbb Z)\). Naturality of the Bockstein gives \(\beta(\alpha)|_{\partial_xN_n}=\beta(a)\ne0\), establishing (7).

An equivariant map in (8) would induce a quotient map \(N_n\to\mathbb RP^{n-2}\) pulling back the latter's universal degree-one class to \(\alpha\). But the \((n-1)\)-st power of that class vanishes in \(\mathbb RP^{n-2}\), contradicting \(\alpha^{n-1}\ne0\). \(\square\)

**Comparison with the unmodified endpoint torus.** The free translation \(J(t)=t+\mathbf1\), which reverses an original undirected full cube path, has a torus quotient and zero Bockstein, as shown in the preceding Subsection. The color-complementing reversal \(R(t)=\mathbf1-t\), after removing its isolated fixed points, instead has the full nonzero projective index of Theorem 3. These are distinct involutions and their covering classes behave differently.

**Theorem 4 (an explicit odd reference map).** Let \(s(t)=\min_{k\in\mathbb Z}|t-2k|\in[0,1]\) for \(t\in\mathbb R/2\mathbb Z\), and define
\[
\Omega(t)=\bigl(s(t_1)-\tfrac12,\ldots,s(t_n)-\tfrac12\bigr)\in\mathbb R^n.
\]
Then \(\Omega(Rt)=-\Omega(t)\), and its zero set consists precisely of the \(2^n\) fixed points (1). Thus
\[
\boxed{\Phi(t)=\frac{\Omega(t)}{\|\Omega(t)\|}:M_n\longrightarrow S^{n-1}}\tag{9}
\]
is a continuous odd map. On each newly introduced boundary sphere it has degree \(\pm1\), and its restriction to the canonical type-A equator is, after choosing the local signed tangent variables, the identity of \(S^{n-2}\). In particular the obstruction in Theorem 3 is sharp with respect to target sphere dimension: an odd map to \(S^{n-1}\) exists, while one to \(S^{n-2}\) does not.

*Proof.* For every circle component \(s(1-t)=1-s(t)\), hence \(\Omega(Rt)=-\Omega(t)\). The simultaneous equations \(s(t_i)=1/2\) have the points (1) as their solutions. Therefore \(\Omega\) is nonzero on \(M_n\), and its normalization is odd. In local variables near \(p_x\), \(s(t_i)-1/2=u_i\). Its normalized restriction to a centered boundary sphere is consequently the identity in the \(u\)-chart, or a diagonal sign change in the original flat chart; it has degree \(\pm1\). The braid equator \(\sum_i u_i=0\) is preserved by normalization, which acts as the identity there. \(\square\)

**Corollary 5 (signed root-degree cancellation).** Orient each small linking sphere by the outward orientation of its removed ball, using the standard orientation of the flat torus. The reference map \(\Phi\) of Theorem 4 has
\[
\deg\bigl(\Phi|_{\partial B_x}\bigr)=(-1)^{\sum_i x_i},
\qquad
\boxed{\sum_{x\in\mathbb F_2^n}\deg\bigl(\Phi|_{\partial B_x}\bigr)=0.}\tag{10}
\]
*Proof.* In flat variables \(\delta_i=t_i-(p_x)_i\), the differential of \(\Omega\) near \(p_x\) is diagonal with entries \((-1)^{x_i}\). Its determinant sign is \((-1)^{\sum_i x_i}\), which gives the local sphere degree. Summing over roots yields \((1-1)^n=0\). \(\square\)

This cancellation is compatible with the nonzero mod-two covering index of Theorem 3: each individual projective boundary detects the covering class, while the signed degrees of all root-boundary maps sum to zero. A global degree-counting argument must therefore use color-sensitive information beyond the reference map.

**Proof-search consequence and limitations.** The carrier \(M_n\) makes the full collection of cube roots into \(2^n\) type-A equatorial boundary spheres, while all endpoint root exchanges remain represented in its interior chamber geometry. The type-A equators have the same chamber opposition as the spherical carrier for Hamilton orders in ordinary boundary tournaments; the ambient free reversal realizes the complemented-reversal law for chiral cube turns from earlier in this Article. Thus a common dimension-simple chain construction can be sought on an explicit high-index equivariant space that includes the root-gluing exchanges.

Theorem 3 is topological and holds independently of any coloring. To deduce NORI1 or the unrestricted boundary-tournament conjecture, one still needs to construct a color-sensitive equivariant map into a low-dimensional target under the assumption that every complete path has excessive switches. The new equatorial boundary spheres provide a precise place for local rank-exchange data and for the required obstruction to meet; they do not supply that map or prove a one-switch path.
