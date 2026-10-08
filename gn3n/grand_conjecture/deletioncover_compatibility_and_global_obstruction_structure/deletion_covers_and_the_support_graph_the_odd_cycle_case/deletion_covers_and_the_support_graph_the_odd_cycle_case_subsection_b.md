# 6.1 Consecutive double deletions

For each \(i\), let \(T_i\) be any two-cover of
\[
H-\{d_i,d_{i+1}\},
\]
which exists by minimality. Put
\[
K_i=S_i-\{d_{i+1}\}=S_{i+2}-\{d_i\}.
\]

**Lemma 9.** For some \(i\), either \(T_i\) has an edge joining two distinct nonempty path pieces obtained by deleting an internal exchanged label from one of the incident selected covers, or the two inherited covers of the double deletion have an order disagreement.

**Proof.** Suppose neither event occurs for any \(i\). Then each exchanged label is an endpoint of the relevant support path, and deleting \(d_i,d_{i+1}\) leaves the same ordered supports \(K_i,S_{i+1}\). Let \(\varepsilon_i\in\{L,R\}\) denote the end of \(K_i\) at which \(d_{i+1}\) is restored to obtain \(P_i\), equivalently the end at which \(d_i\) is restored to obtain \(P_{i+2}\).

If \(\varepsilon_{i+2}=\varepsilon_i\), the two successive restorations at that end force the next removed label to equal the preceding one, contradicting the distinctness of the cycle labels. Hence
\[
\varepsilon_{i+2}\ne\varepsilon_i
\]
for every \(i\). Addition by \(2\) is one cycle modulo \(2k+1\). Following it around the odd number of indices reverses the end an odd number of times and returns to the starting index with the opposite value, a contradiction. \(\square\)
