# Cylindrical counterexample padding and sparse Grassmannian closure reduction

# Cylindrical counterexample padding and sparse Grassmannian closure reduction

This subsection connects the odd-dimensional reversal-index strengthening of Article XIV with the special-dimensional oriented-Grassmannian obstruction of Article XV. The key is a dimension-preserving projection of monochromatic full geodesics under a cylindrical extension of an arbitrary antipodally odd cube-edge coloring.

**Theorem 1 (counterexample padding).** Let \(n\ge2\) and \(k\ge1\). Every antipodally odd edge coloring \(c:E(Q_n)\to\mathbb F_2\) admits an antipodally odd extension
\[
\widetilde c:E(Q_{n+k})\to\mathbb F_2
\]
such that **every** monochromatic full antipodal geodesic of \(\widetilde c\) projects to a monochromatic full antipodal geodesic of \(c\). Consequently, if \(c\) is a counterexample to NORI1 in dimension \(n\), then \(\widetilde c\) is a counterexample in dimension \(n+k\).

*Proof.* Identify \(Q_{n+k}=Q_n\times Q_k\), with vertices \((x,y)\), \(x\in\{0,1\}^n\), \(y\in\{0,1\}^k\). For an edge in one of the first \(n\) directions, put
\[
\widetilde c(\{(x,y),(x\oplus e_i,y)\})
=c(\{x,x\oplus e_i\}).
\tag{1}
\]
This is independent of \(y\): every parallel \(Q_n\) face inherits the original coloring. For an edge in a new direction \(n+j\), put
\[
\widetilde c(\{(x,y),(x,y\oplus e_j)\})=x_1.
\tag{2}
\]
This is well-defined on undirected edges, since \(x\) remains fixed on a new-direction edge. Under global cube antipodality, an old-direction edge maps to the antipodal old-direction edge in \(Q_n\), so its color flips by the hypothesis on \(c\). A new-direction edge at \(x\) maps to a new-direction edge at \(\bar x\), and \((\bar x)_1=1-x_1\); thus its color also flips. Hence \(\widetilde c\) is legal.

Suppose a monochromatic full antipodal geodesic \(\widetilde P\) traverses every one of the \(n+k\) directions once. Delete from \(\widetilde P\) the \(k\) edges in new directions and project all remaining vertices onto \(Q_n\). The result is a path using the original \(n\) dimensions once each; deleting a new-direction edge does not change its \(Q_n\) projection. It therefore joins some \(x\) to \(\bar x\), is dimension-simple, and every one of its edge colors equals that of the corresponding edge of \(\widetilde P\) by (1). It is monochromatic. The contrapositive proves counterexample padding. \(\square\)

**Corollary 2 (unbounded-dimension reduction).** Let \(\mathcal D\subseteq\{2,3,\ldots\}\) be any unbounded set of dimensions. If NORI1 is proved in every dimension \(N\in\mathcal D\), then NORI1 holds in every dimension \(n\ge2\).

*Proof.* If a counterexample existed at \(n\), Theorem 1 would lift it to every \(N\ge n\), contradicting its absence at any \(N\in\mathcal D\) greater than \(n\). \(\square\)

In particular, it suffices to prove NORI1 on the exponentially sparse sequence
\[
\boxed{\mathcal D=\{2^r+1:r\ge2\}=\{5,9,17,33,\ldots\}.}
\tag{3}
\]

**Theorem 3 (sparse Grassmannian closure criterion).** For \(r\ge2\), set \(N=2^r+1\), \(m=N-1=2^r\), and let \(\Sigma_N\cong S^{N-2}=S^{m-1}\) be the type-\(A_{N-1}\) Coxeter flag sphere, with proper-subset complementation as its free involution. Let
\[
\mathcal G_m=\widetilde{\operatorname{Gr}}_2(\mathbb R^m)
\]
be the oriented two-plane Grassmannian, with involution reversing plane orientation.

Assume the following construction statement can be proved for every \(r\ge2\):

> For every antipodally odd coloring of \(Q_N\) having no monochromatic full antipodal geodesic, there exists a continuous equivariant map \(\Sigma_N\to\mathcal G_m\).

Then NORI1 holds in every dimension \(n\ge2\).

*Proof.* The Grassmannian covering-class computation proved earlier in Article XV gives
\[
\omega^{m-1}=0\quad\text{in }H^{m-1}(\operatorname{Gr}_2(\mathbb R^m);\mathbb F_2)
\tag{4}
\]
when \(m=2^r\), where \(\omega=w_1(\gamma_2)\) classifies the orientation double cover. By contrast, the class \(\alpha\) of \(\Sigma_N\to\Sigma_N/\mathbb Z_2\cong\mathbb RP^{m-1}\) has \(\alpha^{m-1}\ne0\). An equivariant map as stated would pull \(\omega\) back to \(\alpha\), contradicting (4). Thus no counterexample coloring exists at any \(N=2^r+1\). Corollary 2 then excludes counterexamples in every dimension. \(\square\)

**Corollary 4 (sparse half-dimensional chain-tower criterion).** With \(N=2^r+1\ge9\), suppose that for every legal coloring of \(Q_N\) lacking a monochromatic full antipodal geodesic one can construct an antipodal norm-boundary tower in its two-color endpoint complex through height
\[
\boxed{q_r=(N-3)/2=2^{r-1}-1.}
\tag{5}
\]
Then NORI1 holds in every dimension \(n\ge2\).

*Proof.* The odd-dimensional top-cohomology cancellation theorem of Article XIV shows that a hypothetical counterexample at \(N\ge7\) has \(\alpha_K^{q_r}=0\). The Smith-transfer equivalence shows that the asserted height-\(q_r\) tower would force \(\alpha_K^{q_r}\ne0\), a contradiction. Thus no counterexample exists at any \(N\ge9\) in the unbounded family, and Corollary 2 applies. \(\square\)

**Scope and warning.** Theorem 1 preserves the cube's original dimension-simple paths under projection, but says nothing about increasing or decreasing the switch count for arbitrary nonmonochromatic paths. Theorem 3 is a *conditional proof program*, not a proof that the color-sensitive equivariant Grassmannian map can be extended beyond the low-dimensional cells established in Article XV. Theorem 4 likewise assumes, rather than constructs, the missing chains. The reduction is specific to NORI1; no analogous inheritance theorem for unrestricted ordinary boundary 3-tournaments has been established here.

**Research significance.** All-dimensional NORI1 would follow from coherent Grassmannian extensions in the sparse odd dimensions \(2^r+1\), precisely where the strongest known orientation-cover obstruction is available. It is unnecessary to prove the Grassmannian extension separately for dimensions outside this sequence. Alternatively, only a half-dimensional antipodal chain tower through height \(2^{r-1}-1\) is needed in each of those sparse dimensions.
