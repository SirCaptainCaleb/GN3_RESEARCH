# Signed type-B chambers as paired-symbol type-A Hamilton orders

# Signed type-B chambers as paired-symbol type-A Hamilton orders

Let \(Q_n\) have vertices \(x\in\mathbb F_2^n\). A full antipodal geodesic is determined by its root \(x\) and dimension permutation \(\pi=(i_1,\ldots,i_n)\). Define its signed word
\[
w(x,\pi)=(w_1,\ldots,w_n),\qquad w_j=(-1)^{x_{i_j}}i_j.
\tag{1}
\]
These words, containing one of \(\{+i,-i\}\) for each \(i\), are the chambers of the type-\(B_n\) reflection arrangement. In particular the free choice of cube root is encoded by the signs of a Coxeter chamber.

**Theorem 1 (paired-symbol type-A realization).** Let
\[
U=\{+1,-1,\ldots,+n,-n\},\qquad
L=\{z\in\mathbb R^U:z_{-i}=-z_{+i}\text{ for each }i\}.
\]
Then \(L\) is an \(n\)-dimensional subspace of \(W_U=\{z:\sum_{u\in U}z_u=0\}\). The restriction to \(L\) of the type-\(A_{2n-1}\) braid arrangement \(z_u=z_v\) is the type-\(B_n\) arrangement
\[
t_i=0,\qquad t_i=t_j,\qquad t_i=-t_j\quad (i\ne j),
\tag{2}
\]
where \(t_i=z_{+i}\). Moreover,
\[
\boxed{
(x,\pi)\longmapsto H(x,\pi)=(w_1,\ldots,w_n,-w_n,\ldots,-w_1)
}
\tag{3}
\]
is a bijection between full cube geodesics with specified roots and Hamilton orders of \(U\) satisfying \(H_{2n+1-j}=-H_j\) for every \(j\). Each of these orders has a type-A simple-root basis of \(W_U\); its Weyl chamber intersects \(L\) in a full-dimensional type-B chamber.

*Proof.* The equations defining \(L\) imply \(\sum_{u\in U}z_u=0\). Intersecting \(z_{+i}=z_{-i}\), \(z_{+i}=z_{+j}\), and \(z_{+i}=z_{-j}\) with \(L\) yields respectively \(t_i=0\), \(t_i=t_j\), and \(t_i=-t_j\). These exhaust the braid hyperplanes after restriction.

Given a signed word \(w\), choose a point of \(L\) with
\[
z_{w_1}>z_{w_2}>\cdots>z_{w_n}>0,\qquad z_{-w_j}=-z_{w_j}.
\tag{4}
\]
Such points exist by assigning decreasing positive magnitudes. The complete ordering of its \(2n\) entries is then
\[
z_{w_1}>\cdots>z_{w_n}>z_{-w_n}>\cdots>z_{-w_1},
\]
so (3) determines a type-A Weyl chamber whose intersection with \(L\) has nonempty interior. Conversely, an order satisfying the displayed symmetry consists of \(n\) signed entries followed by their negatives in reverse order. Its first half uses one member of every signed pair, and recovers \(x\) and \(\pi\) uniquely from (1). The \(2n-1\) consecutive roots \(e_{H_j}-e_{H_{j+1}}\) form a type-A simple-root basis, proving the claim. \(\square\)

Under cube complementation the signed word becomes \(-w\), while
\[
H(\bar x,\pi)=\operatorname{rev}H(x,\pi).
\tag{5}
\]
Thus vertex antipodality in the cube is represented by reversal of a paired-symbol Hamilton order.

**Theorem 2 (Coxeter rotation and color transport).** Define the operations on signed words
\[
T(w_1,\ldots,w_n)=(w_2,\ldots,w_n,-w_1),\qquad
R(w_1,\ldots,w_n)=(-w_n,\ldots,-w_1).
\tag{6}
\]
The map \(T\) is right multiplication by the signed cycle \((2,3,\ldots,n,-1)\), a Coxeter element of \(B_n\), and
\[
T^nw=-w,\quad T^{2n}w=w,\quad R^2w=w,\quad RTR=T^{-1}.
\tag{7}
\]
Let \(c\) be any binary undirected-edge coloring satisfying \(c(\bar e)=1-c(e)\), and let \(C(w)=(C_1(w),\ldots,C_n(w))\) be the edge-color word of the geodesic corresponding to \(w\). Then
\[
\begin{aligned}
C(Tw)&=(C_2(w),\ldots,C_n(w),1-C_1(w)),\\
C(-w)&=\mathbf1-C(w),\\
C(Rw)&=\operatorname{rev}C(w).
\end{aligned}
\tag{8}
\]

*Proof.* Right multiplication by the signed permutation sending \(j\) to \(j+1\) for \(j<n\) and \(n\) to \(-1\) has the action \(T\). It is a product of the adjacent-transposition simple reflections and a sign-changing simple reflection of \(B_n\). The algebraic identities (7) follow by substitution.

If \(w=w(x,\pi)\), then \(Tw\) represents the geodesic rooted at \(x\oplus e_{i_1}\) with dimension order \((i_2,\ldots,i_n,i_1)\). Its first \(n-1\) edges are the final \(n-1\) edges of the original geodesic, and its last edge is the antipodal image of the original first edge. This proves the first equality of (8). The signed word \(-w\) represents \((\bar x,\pi)\), giving the second equality by antipodal oddness. The word \(Rw\) represents \((\bar x,\operatorname{rev}\pi)\), which follows the original geodesic backward, giving the third. \(\square\)

Theorems 1–2 retain unrestricted NORI1 root choice while placing all its complete paths inside type-A Hamilton-order geometry. The type-B chamber sphere \(S(L)\cong S^{n-1}\) is an antipodal subsphere of the type-\(A_{2n-1}\) sphere \(S(W_U)\cong S^{2n-2}\). Thus root variation is an intrinsic sign dimension of the chamber representation, and root sliding is the signed Coxeter rotation (6).

This is a faithful embedding of the path geometry. To transfer the path-existence conjecture from ordinary boundary 3-tournaments one would additionally need a valid correspondence between the cube-edge word and a reversal-odd labeling of consecutive triples on the paired-symbol alphabet, or a selection theorem that applies to both label types. The chamber embedding by itself makes no such correspondence.
