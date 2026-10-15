# Seam transgression for the two-color endpoint quotient

# Seam transgression for the two-color endpoint quotient

Let \(K_0,K_1\) be finite simplicial subcomplexes with a free simplicial involution \(R\) exchanging them. Put \(K=K_0\cup K_1\), \(I=K_0\cap K_1\), \(Q=K/R\), and \(J=I/R\). Freeness means no simplex is setwise fixed. Write \(p:K_0\to Q\) for the quotient restriction and \(i:J\hookrightarrow Q\) for inclusion. All cohomology below has coefficients in \(\mathbb F_2\).

**Theorem 1 (seam cochain sequence).** There is a short sequence of cochain complexes, with zero kernel and cokernel,
\[
\boxed{0\to C^*(Q)\xrightarrow{p^*}C^*(K_0)
\xrightarrow{T}C^*(J)\to0,}
\tag{1}
\]
where the second arrow is the orbit trace
\[
\boxed{(Tz)([\sigma])=z(\sigma)+z(R\sigma)}
\tag{2}
\]
for simplices \(\sigma\) of \(I\).

*Proof.* An orbit of simplices outside \(I\) meets \(K_0\) in one member, while an orbit in \(I\) meets \(K_0\) in two. The sequence (1) on each non-seam orbit is \(0\to\mathbb F_2\xrightarrow{=}\mathbb F_2\to0\); on a seam orbit it is
\[
0\to\mathbb F_2\xrightarrow{t\mapsto(t,t)}
\mathbb F_2^2\xrightarrow{(a,b)\mapsto a+b}
\mathbb F_2\to0.
\]
These are short sequences with zero kernel and cokernel. The arrows commute with coboundaries because face relations commute with \(R\). \(\square\)

Write \(\alpha=w_1(K\to Q)\) for the double-cover class, and \(\alpha_I=i^*\alpha=w_1(I\to J)\). Denote the connecting map in the long cohomology sequence of (1) by
\[
\delta:H^{j-1}(J)\to H^j(Q).
\]

**Theorem 2 (transgression of every covering-class power).** For all \(j\ge1\),
\[
\boxed{\alpha^j=\delta(\alpha_I^{j-1}).}
\tag{3}
\]
Moreover,
\[
\boxed{\alpha^j\ne0\iff
\alpha_I^{j-1}\notin\operatorname{im}
\bigl(T:H^{j-1}(K_0)\to H^{j-1}(J)\bigr).}
\tag{4}
\]

*Proof.* Choose a zero-cochain \(h\) on \(K_0\) that assigns complementary values to the two vertices in every \(R\)-orbit of vertices of \(I\). Set its values on other vertices arbitrarily. Then \(Th=1\), and \(T(dh)=0\). Hence \(dh=p^*\omega\) for a unique one-cochain \(\omega\) on \(Q\), representing \(\delta(1)\).

For each quotient vertex, choose a representative \(v\in K_0\), and choose the lift \(R^{h(v)}v\) in \(K\). For an orbit in \(I\), replacing \(v\) by \(Rv\) does not change the chosen lift because the assigned values are complementary. On every edge of \(Q\), represented by an edge in \(K_0\), the chosen endpoint lifts agree with one lifted edge if and only if the two \(h\)-values agree. Thus the edge transition bit is \((dh)(e)=\omega([e])\), proving \([\omega]=\alpha\). We have shown \(\delta(1)=\alpha\).

The trace satisfies the projection rule
\[
T(z\smile p^*b)=(Tz)\smile i^*b
\]
for cochains, since \(p^*b\) takes the same value on both members of an \(R\)-orbit. The connecting map therefore obeys
\(\delta(\gamma\smile i^*b)=\delta(\gamma)\smile b\).
Set \(\gamma=1\) and \(b=\alpha^{j-1}\), obtaining (3). The long cohomology sequence gives (4). When \(J\) is empty, interpret its cohomology and degree-zero unit as zero; the double cover then splits and the same formula holds. \(\square\)

**Corollary 3 (application to unrestricted NORI1).** Let \(n\ge5\), let \(c\) be antipodally odd, and suppose that there is no monochromatic full antipodal geodesic. Take \(K_a=\Delta P_a(c)\), the two monochromatic endpoint poset complexes, and \(R(u,v)=(\bar v,\bar u)\). The involution is free under this assumption: its fixed interval vertices would represent a full monochromatic geodesic, and ranks increase strictly within a simplex. The previously proved two-color comparison gap bounds the dimension of \(I=K_0\cap K_1\) by \(m-1\), where \(m=\lfloor(n-3)/2\rfloor\). Therefore
\[
\boxed{\alpha_I^m=0,\qquad \alpha^{m+1}=0.}
\tag{5}
\]
Theorem 2 recovers the half-dimensional covering-index bound directly from the seam, without requiring the constructed equivariant map to \(S^m\).

**Geometric scope and forward direction.** Every power of the reversal-cover class on \(K/R\) is controlled by a single-color-to-seam trace. Formula (4) identifies its nonvanishing with the failure of a particular seam cup-power to arise from \(K_0\). A chain-level Wu--Yang argument may therefore be phrased as a compatible nontransfer certificate at the two-color intersection, rather than as a continuous map from the punctured affine torus. This result is an identity for finite free involution complexes; it does not provide a source-to-\(K\) transfer and does not settle NORI1.

For colorings with full monochromatic antipodal geodesics, remove all rank-\(n\) vertices from \(K\) and their incident simplices. The resulting proper-rank complex has free \(R\)-action, so Theorems 1 and 2 apply without a no-closure hypothesis.
