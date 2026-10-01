# Every deletion state reduces to a Hamiltonian four-window, the universal cyclic four-kernel, or a doubled cross barrier

## Statement

Let H be a minimum counterexample and let H-x=P|Q be any one-vertex deletion two-cover. Then at least one of the following three bounded frontiers occurs.

(1) H contains a Hamiltonian four-vertex induced set W containing x; its complement is non-Hamiltonian of path-cover number two.

(2) H contains the universal cyclic non-Hamiltonian four-kernel X containing x arising from a first-type failed-insertion obstruction; every one-vertex exterior extension X union {d} is Hamiltonian and the certified cyclic-kernel exchange/deletion-stability conclusions apply.

(3) There are path gaps p_i|p_{i+1} in P and q_j|q_{j+1} in Q such that both failed-insertion obstructions are second-type and the doubled cross triples
(q_j,p_i,x) and (p_i,q_j,x)
are tight.

Thus every deletion state collapses to a four-vertex Hamiltonian support, one rigid universal four-kernel, or one doubled cross-barrier configuration; no separate boundary-pivot or nine-vertex residual is needed.

## Body

Apply the certified failed-insertion normal form to x on P and Q.

If either obstruction is first-type, apply 0425e03e2aa3. Its four-window is either Hamiltonian, giving (1) and the standard minimum-counterexample complement conclusion, or it is exactly the universal cyclic non-Hamiltonian four-kernel, giving (2).

Otherwise both obstructions are second-type. Apply 4efbe05b945a, which is valid for arbitrary pivot gaps including the first and last. It yields either a mixed tight four-path, whose support is Hamiltonian and gives (1), or both cross triples between the two pivot-side labels and x are tight, giving (3).

These alternatives exhaust the two failed-insertion types on both components. The boundary matching-block classification and the older interior-only pivot-pivot clauses are therefore subsumed by this stronger second-type coupling theorem.
