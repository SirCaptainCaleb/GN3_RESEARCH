# Two second-type pivots on disjoint paths force a mixed four-path or doubled cross barrier, including boundary gaps

## Statement

Let Q=(q_1,...,q_m) and R=(r_1,...,r_s) be vertex-disjoint tight paths in a boundary tournament, and let x lie outside both. Suppose alternative 2 of the failed-insertion normal form from insert01 holds for x on Q at any path gap q_i|q_{i+1}, 1<=i<m, and on R at any path gap r_j|r_{j+1}, 1<=j<s; the first and last gaps are allowed. Then either (q_{i+1},x,q_i,r_j) or (r_{j+1},x,r_j,q_i) is a tight four-vertex path, or both cross triples (r_j,q_i,x) and (q_i,r_j,x) are tight. Thus the mixed-Hamiltonian-four-set versus doubled-cross-barrier dichotomy of 0b012e2e3816 does not require interior pivots.

## Body

Alternative 2 of insert01 always supplies the reverse-through-gap tight triple (q_{i+1},x,q_i), including at the first or last path gap; likewise it supplies (r_{j+1},x,r_j). These are the only features of the pivot locations used in the proof of 0b012e2e3816. If (x,q_i,r_j) is tight, it concatenates with (q_{i+1},x,q_i) to give the tight four-path (q_{i+1},x,q_i,r_j). If (x,r_j,q_i) is tight, it concatenates with (r_{j+1},x,r_j) to give (r_{j+1},x,r_j,q_i). If neither mixed triple is tight, boundary antisymmetry gives their reverses (r_j,q_i,x) and (q_i,r_j,x), yielding the doubled cross barrier. No predecessor or successor beyond the displayed gap endpoints is used, so no interior-gap hypothesis is needed.
