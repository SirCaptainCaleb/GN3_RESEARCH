# Introduction

Let \(H\) be a finite boundary \(3\)-tournament. A tight path is a sequence
\[
(v_1,\ldots ,v_m)
\]
of distinct vertices such that \((v_i,v_{i+1},v_{i+2})\) is a tight triple for every \(1\le i\le m-2\). A path cover is a collection of vertex-disjoint tight paths whose supports partition \(V(H)\), and \(\operatorname{pc}(H)\) denotes the minimum number of paths in a cover.

Assume throughout that \(H\) is a counterexample of minimum order to
\[
\operatorname{pc}(H)\le 2.
\]
Then \(\operatorname{pc}(H)=3\). For every \(x\in V(H)\), minimality gives a two-cover of \(H-x\). Neither path can be empty, and \(H-x\) cannot be Hamiltonian, since a Hamilton path of \(H-x\) together with the one-vertex path \(x\) would be a two-cover of \(H\). Thus every deletion cover at \(x\) consists of two nonempty paths.

For each \(x\in V(H)\), choose a deletion cover
\[
F_x=P_x\mid Q_x
\]
that minimizes \(|P_x|^2+|Q_x|^2\) among all two-covers of \(H-x\). Equivalently, choose a deletion cover whose two component orders have minimum possible imbalance.
