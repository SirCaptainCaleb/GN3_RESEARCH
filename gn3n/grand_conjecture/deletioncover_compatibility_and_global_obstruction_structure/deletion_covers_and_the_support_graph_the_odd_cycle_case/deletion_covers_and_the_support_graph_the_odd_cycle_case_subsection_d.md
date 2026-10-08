# 6.3 Incidence identities

Let \(C\) be the ordinary cycle on ground vertices \(d_0,\ldots ,d_{2k}\), with edge \(\{d_{i-1},d_i\}\). The support identities are
\[
\mathbf 1_{S_i}+\mathbf 1_{S_{i+1}}=\mathbf 1_V-\mathbf 1_{\{d_i\}},
\qquad
\sum_i\mathbf 1_{S_i}=k\mathbf 1_V.
\]

Let \(T\) be the support of a tight path that is a vertex cover of \(C\), and write \(|T|=k+r\). Define
\[
I(T)=\{i:d_{i-1},d_i\in T\}.
\]

**Lemma 11.** One has
\[
|I(T)|=2r-1,\qquad
\mathbf 1_T+\sum_{i\in I(T)}\mathbf 1_{S_i}=r\mathbf 1_V.
\]

**Proof.** Put \(t_i=\mathbf 1_T(d_i)\) and \(a_i=t_{i-1}+t_i\). Since \(T\) covers every edge of \(C\), \(a_i\in\{1,2\}\), and \(a_i-1\) is the indicator of \(I(T)\). Then
\[
\sum_i a_i\mathbf 1_{S_i}
 =\sum_j t_j(\mathbf 1_{S_j}+\mathbf 1_{S_{j+1}})
 =|T|\mathbf 1_V-\mathbf 1_T.
\]
Subtracting \(\sum_i\mathbf 1_{S_i}=k\mathbf 1_V\) gives the second identity. Summing the \(a_i\) gives
\[
2|T|=(2k+1)+|I(T)|,
\]
which gives the first. \(\square\)

If \(r=1\), Lemma 11 says that \(T\) and one selected support \(S_i\) are disjoint and cover \(V(H)\). Therefore a Hamiltonian vertex cover of the ground cycle of order \(k+1\) gives a two-cover of \(H\).
