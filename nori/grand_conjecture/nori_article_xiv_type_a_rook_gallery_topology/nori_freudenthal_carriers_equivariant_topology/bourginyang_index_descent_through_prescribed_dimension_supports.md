# Bourgin–Yang index descent through prescribed dimension supports

# Bourgin–Yang index descent through prescribed dimension supports

Let \(X\) be a finite simplicial complex with a free involution \(R\), and write \(\alpha=w_1(X\to X/R)\). Suppose there is an odd piecewise-linear map \(s:X\to\mathbb R^t\), with zero set \(Z=s^{-1}(0)\). The cohomological index is measured by powers of \(\alpha\).

**Theorem 1 (zero-set index descent).** For any integer \(k\ge0\),
\[
\boxed{\alpha^{t+k}\ne0\quad\Longrightarrow\quad
\alpha_Z^k\ne0\text{ in }H^k(Z/R;\mathbb F_2),}
\tag{1}
\]
where \(\alpha_Z\) is the covering class restricted to \(Z\). For \(k=0\), the conclusion means \(Z\ne\varnothing\). Equivalently, if \(\alpha_Z^k=0\), then \(\alpha^{t+k}=0\).

*Proof.* Put \(B=X/R\), \(A=Z/R\), and \(U=B\setminus A\). The odd map \(s\) descends to a section of \(L^{\oplus t}\), where \(L\) is the real line bundle of \(X\to B\). The section is nowhere zero on \(U\), so its top Stiefel–Whitney class \(\alpha^t\) vanishes on \(U\). Thus \(\alpha^t\) lifts to a relative class \(e\in H^t(B,U;\mathbb F_2)\).

Assume \(\alpha_Z^k=0\). Choose a sufficiently small neighborhood \(V\) of \(A\) in \(B\) that deformation retracts onto \(A\). Then \(\alpha^k|_V=0\), so \(\alpha^k\) lifts to \(b\in H^k(B,V;\mathbb F_2)\). The relative cup product
\[
e\smile b\in H^{t+k}(B,U\cup V;\mathbb F_2)
\]
vanishes because \(U\cup V=B\). Its image in absolute cohomology is \(\alpha^{t+k}\), which must therefore vanish. This proves the contrapositive. \(\square\)

For a reversal-stable directed geodesic endpoint complex \(K\) as in the preceding unused-dimension section theorem, and a prescribed dimension set \(T\subseteq[n]\), let
\[
K_T=\text{the induced subcomplex on pairs }p=(u,v)
\text{ with }T\subseteq\{i:u_i\ne v_i\}.
\]
The canonical sign section \(s_T\) has rank \(|T|\) and zero set \(K_T\).

**Theorem 2 (support-index inheritance).** Let \(h\ge1\) with \(\alpha_K^h\ne0\). For every \(T\subseteq[n]\) with \(t=|T|\le h\),
\[
\boxed{\alpha_{K_T}^{h-t}\ne0.}
\tag{2}
\]
In particular, for \(t=h-1\), the subcomplex \(K_T\) has a connected component preserved by the reversal involution, not merely one vertex supporting \(T\).

*Proof.* Apply Theorem 1 to the odd section \(s_T\) with \(k=h-t\). For \(k\ge1\), nonvanishing of a degree-one covering class on a quotient component forces that component's double cover to be connected, yielding an \(R\)-invariant connected component of \(K_T\). \(\square\)

**Theorem 3 (one-component recursive saturation of the bi-monochromatic seam).** Let \(c\) be an antipodally odd coloring of \(Q_n\) with no monochromatic full antipodal geodesic. Put \(K=K_0(c)\cup K_1(c)\) and \(I=K_0(c)\cap K_1(c)\), both with their free reversal action. Suppose
\[
\boxed{\alpha_K^{h+1}\ne0\quad(h\ge1).}
\tag{3}
\]
Then one reversal-invariant connected component \(C\subseteq I\) has the following simultaneous property: for every \(T\subseteq[n]\) with \(|T|=t\le h\), the subcomplex \(C_T\) of its bi-monochromatic intervals using all dimensions in \(T\) satisfies
\[
\boxed{\alpha_{C_T}^{h-t}\ne0.}
\tag{4}
\]
In particular, for every \((h-1)\)-element set \(T\), a connected \(R\)-invariant subcomponent of \(C_T\) exists.

*Proof.* The seam transgression identity gives \(\alpha_K^{h+1}=\delta(\alpha_I^h)\), so \(\alpha_I^h\ne0\). Choose one connected quotient component on which \(\alpha_I^h\) remains nonzero, and let \(C\) be its inverse image. The inverse image must be a single connected \(R\)-invariant component, since a swapped pair of components would give a split double cover with vanishing positive-degree class. Apply Theorem 2 to the restricted action on \(C\), for every \(T\). The same \(C\) works for all choices of \(T\). \(\square\)

**Implication for dimension-simple chain transfers.** The earlier section theorem only forced the existence of individual red-and-blue geodesic intervals using prescribed dimension subsets. The present result preserves *residual index* after forcing those dimensions and, in particular, demands connected reversal-invariant families within all nearly maximal prescribed-support strata. This is a strictly stronger necessary condition for high covering index. It does not prove nonvanishing of any such index and does not settle NORI1.
