# Every facing endpoint pair lies in a positioned Hamiltonian four- or five-window

## Statement

Let H be a minimum counterexample and let H-x=P|Q be a deletion two-cover, with P=(p_0,...,p_m) and Q=(q_0,...,q_s), where both components have order at least three. For the facing endpoint pair p_0,q_s, at least one of the following three sets is Hamiltonian: W_5={p_1,p_0,x,q_s,q_{s-1}}, W_L={p_1,p_0,x,q_s}, or W_R={p_0,x,q_s,q_{s-1}}. In every case the chosen support contains x,p_0,q_s and its complement is non-Hamiltonian with path-cover number two. The symmetric statement holds for the other facing pair q_0,p_m.

## Body

Endpoint hook forcing c38e8b5c48ee gives the tight triples (p_1,p_0,x) and (x,q_s,q_{s-1}). Boundary antisymmetry gives exactly one of (p_0,x,q_s) and (q_s,x,p_0) as tight. If (p_0,x,q_s) is tight, then (p_1,p_0,x,q_s,q_{s-1}) is a tight Hamilton path on W_5, and we are done.

Assume instead that the reverse cross (q_s,x,p_0) is tight. Put X={p_1,p_0,x,q_s} and S=X union {q_{s-1}}. If H[X] is Hamiltonian, choose W_L=X. If H[X] is non-Hamiltonian but H[S] is Hamiltonian, choose W_5=S. Finally suppose both H[X] and H[S] are non-Hamiltonian. Certified smallset01 says that a non-Hamiltonian five-set has at most one non-Hamiltonian four-subset. Since X=S-{q_{s-1}} is already non-Hamiltonian, every other four-subset of S is Hamiltonian. In particular W_R=S-{p_1}={p_0,x,q_s,q_{s-1}} is Hamiltonian. Thus one of the three displayed supports is always Hamiltonian.

Each support is proper because a minimum counterexample has order greater than ten. If the complement of the chosen Hamiltonian support were Hamiltonian, the two Hamilton paths would form a spanning two-cover of H. Hence its complement is non-Hamiltonian; minimum-counterexample calculus gives path-cover number two. Reversing the roles of the two displayed components and using their opposite facing endpoints proves the q_0,p_m statement. No cyclic rotation or path reversal is used.