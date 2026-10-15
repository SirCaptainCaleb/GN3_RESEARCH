# Full quadratic switch bivectors preserve straddling unit degree

### Universal face signs for the complete quadratic switch bivector

Let \(n=a+b\), with \(a,b\ge2\), and let \(A\sqcup B=[n]\). The top dual Coxeter cell \(D=P_a\times P_b\) consists of the Hamilton orders \(\pi\) listing \(A\) before \(B\). Write \(Z_p(\pi)=\sum_{h\le p}e_{\pi_h}-(p/n)\mathbf1\in W\) and \(T=\mathbf1_A-(a/n)\mathbf1\).

**Lemma 1 (sign cone for every prefix wedge).** For any \(1\le p<q<n\), put \(H_{pq}=\iota_T(Z_p\wedge Z_q)\in T^\perp\). Let \(S\subsetneq A\) and \(R\subsetneq B\) be nonempty. On every order whose \(A\)-suborder begins with \(S\),
\[
\sum_{i\in S}(H_{pq})_i\le0.
\tag{1}
\]
On every order whose \(B\)-suborder begins with \(R\),
\[
\sum_{i\in R}(H_{pq})_i\ge0.
\tag{2}
\]
If \(p<a<q\), both inequalities are strict.

*Proof.* Decompose \(W=\mathbb RT\oplus W_A\oplus W_B\). For \(p<a\) write \(Z_p=(p/a)T+u_p\), with \(u_p\in W_A\) the centered first-\(p\)-subset indicator; for \(q>a\) write \(Z_q=((n-q)/b)T+v_{q-a}\), with \(v\in W_B\), and note \(Z_a=T\).

Fix \(S\subsetneq A\) of size \(s\), and define \(h_s(j)=\min(j,s)-js/a>0\) for \(1\le j<a\). If \(p<q<a\), then the sum over \(S\) in \(H_{pq}/\|T\|^2\) is
\[
\frac pa h_s(q)-\frac qa h_s(p)
=\frac{p\min(q,s)-q\min(p,s)}a\le0
\]
because \(\min(j,s)/j\) is nonincreasing. If \(p<a\le q\), the same sum is \(-((n-q)/b)h_s(p)<0\). If \(a\le p\), it vanishes. This proves (1).

Similarly fix \(R\subsetneq B\) of size \(t\), and put \(g_t(j)=\min(j,t)-jt/b\). For \(a<p<q\), write \(r=p-a\), \(s=q-a\). The sum over \(R\) in \(H_{pq}/\|T\|^2\) equals
\[
\frac{b-r}{b}g_t(s)-\frac{b-s}{b}g_t(r)\ge0,
\]
since \(g_t(j)/(b-j)\) is nondecreasing: it increases for \(j\le t\) and is constant thereafter. If \(p\le a<q\), that sum is \((p/a)g_t(q-a)>0\). Otherwise it vanishes. QED.

**Theorem 2 (unit degree of the full quadratic switch map).** For each vertex \(\pi\) of \(D\), select a set of ranks \(S_\pi\subseteq\{1,\ldots,n-1\}\) having at least one member below \(a\) and at least one above \(a\). Form
\[
\mathcal B(\pi)=\sum_{p<q,\ p,q\in S_\pi}Z_p(\pi)\wedge Z_q(\pi).
\]
The piecewise-affine interpolation of \(\iota_T\mathcal B(\pi)\) on \(\partial D\) never vanishes, and its radial normalization has degree \(\pm1\).

*Proof.* On a boundary facet from the \(A\)-factor, every pair contributes a nonpositive value to the supporting functional from Lemma 1; at least one selected pair crosses the cut and contributes strictly negatively. On a facet from the \(B\)-factor, every pair contributes nonnegatively and a crossing pair contributes strictly positively. Hence every boundary facet has all its vertex labels in a common strict open halfspace, proving zero-avoidance after affine interpolation.

Let \(E(\pi)=Z_{\min S_\pi}\wedge Z_{\max S_\pi}\). Its contracted labels satisfy the same strict inequalities, and by the variable-rank permutahedral product theorem their normalized boundary map has degree \(\pm1\). The straight-line homotopy between the contracted \(\mathcal B\) and \(E\) labels remains in the corresponding strict halfspace on every facet. Thus their degrees agree. QED.

**Corollary 3 (nonnegative pair weights).** The same conclusion holds for \(\sum_{p<q}w_{pq}Z_p\wedge Z_q\), with arbitrary nonnegative weights, provided at least one pair \(p<a<q\) has positive weight at each vertex.

This gives a color-sensitive degree theorem for the *entire* reversal-odd quadratic switch bivector, not merely its first-and-last-switch summand, whenever all flags of a two-block cell have switches on opposite sides of the block cut. It does not assert existence of a straddling cell for every coloring, nor supply coherent fillings across different top cells.
