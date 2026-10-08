# Incidence compression of turn defects preserves block localization — preserved pre-item development

## Development

## Incidence compression of turn defects

Fix coordinate-label arity \(r\ge 2\) in the directed translation-invariant sector on an \(n\)-element ground set \(V\). Under a counterexample hypothesis every coordinate permutation is bad.

For
\[
\pi=(v_1,\ldots,v_n)
\]
write its status word
\[
c_i=h(v_i,\ldots,v_{i+r-1}),\qquad 1\le i\le n-r+1.
\]
If the first and last changes occur at positions \(f<\ell\), let
\[
T_f=\{v_f,\ldots,v_{f+r}\},\qquad
T_\ell=\{v_\ell,\ldots,v_{\ell+r}\}
\]
be the underlying \((r+1)\)-sets of the first and last turn windows. Define
\[
D(\pi):=\mathbf 1_{T_f}-\mathbf 1_{T_\ell}
\in
W_V:=\left\{x\in\mathbb R^V:\sum_{v\in V}x_v=0\right\}.
\]

This is the incidence projection of the turn-window root \(e_{\tau_f}-e_{\tau_\ell}\).

### Lemma 1: reversal oddness survives incidence compression

\[
D(\pi^{\rm rev})=-D(\pi).
\]

Indeed, reversal swaps the first and last turn windows and does not change their underlying coordinate sets.

### Lemma 2: positive incidence balance still localizes the entire defect interval

Let
\[
F=C_1|\cdots|C_s
\]
be a proper face of the permutahedron, and write \(b(v)=j\) for \(v\in C_j\). If bad chambers \(\pi_1,\ldots,\pi_m\) refining \(F\) and coefficients \(\lambda_j>0\) satisfy
\[
\sum_j\lambda_jD(\pi_j)=0,
\]
then, for every participating chamber, all coordinate positions from its first turn window through its last turn window lie in one block of \(F\).

Use the linear functional
\[
\varphi_F(x)=\sum_{v\in V}b(v)x_v.
\]
For a turn window beginning at position \(i\), put
\[
\Psi_i=\sum_{t=0}^{r} b(v_{i+t}).
\]
Along every refinement of \(F\),
\[
\Psi_{i+1}-\Psi_i=b(v_{i+r+1})-b(v_i)\ge0.
\]
Hence
\[
\varphi_F(D(\pi))=\Psi_f-\Psi_\ell\le0.
\]
Applying \(\varphi_F\) to the positive zero relation forces equality term by term. Thus \(\Psi_i\) is constant from \(f\) through \(\ell\), so
\[
b(v_i)=b(v_{i+r+1})
\]
throughout that interval. Since the block-index sequence is nondecreasing, equality at distance \(r+1\) forces every intervening block index to be equal. Therefore
\[
v_f,v_{f+1},\ldots,v_{\ell+r}
\]
all lie in one block.

### Corollary 3: the compressed balance decomposes blockwise

After localization, both \(T_f\) and \(T_\ell\) lie in the same block \(C_j\), so \(D(\pi)\) is supported entirely on \(C_j\). Since distinct face blocks have disjoint coordinate supports, any positive zero relation among the \(D(\pi)\) splits as a direct sum of positive zero relations supported on individual blocks.

Thus the hereditary block-localization property of the full turn-window root survives the projection to the coordinate space \(W_V\).

### Dimensional significance

The uncompressed turn-root space has one basis vector for every reversal-orbit of an \((r+1)\)-window. The incidence compression lands instead in
\[
W_V,\qquad \dim W_V=n-1,
\]
independently of \(r\).

This removes almost all of the target-dimension obstruction in the topological route. The type-\(A\) Coxeter sphere of coordinate orders has dimension \(n-2\), so a direct Borsuk--Ulam zero is still one dimension short; however, any dimension-lift or relative/chain-level argument now needs to recover only one dimension, while retaining the same face-block descent mechanism.

### Audit

No injectivity of the incidence projection is claimed. The conclusion uses only a positive zero relation after projection. Once the block potential forces each participating defect interval into one block, disjoint coordinate support is enough to recover blockwise decomposition. The remaining one-dimensional mismatch is real and is not claimed closed here.
