# Facing component-end hooks force a Hamiltonian five-window or a reverse cross triple

## Statement

Let H be a minimum counterexample and let H-x=P|Q be a deletion two-cover, with displayed paths P=(p_0,...,p_m) and Q=(q_0,...,q_s), where both components have order at least three. For the facing pair consisting of p_0 and q_s, either (p_0,x,q_s) is tight and (p_1,p_0,x,q_s,q_{s-1}) is a Hamiltonian five-window whose complement is non-Hamiltonian of path-cover number two, or the reverse cross triple (q_s,x,p_0) is tight. For the other facing pair q_0,p_m, either (q_0,x,p_m) is tight and (q_1,q_0,x,p_m,p_{m-1}) is such a Hamiltonian five-window, or the reverse cross triple (p_m,x,q_0) is tight. No assertion is made for the two same-end pairs p_0,q_0 and p_m,q_s.

## Body

For the facing pair p_0,q_s, c38e8b5c48ee gives (p_1,p_0,x) and (x,q_s,q_{s-1}) tight. Boundary antisymmetry gives exactly one of (p_0,x,q_s) and (q_s,x,p_0) as tight. In the first case the three consecutive triples of (p_1,p_0,x,q_s,q_{s-1}) are tight, so it is a Hamilton path on the five-set W={p_1,p_0,x,q_s,q_{s-1}}. Since a minimum counterexample has order greater than ten, W is proper. If H-W were Hamiltonian, its Hamilton path together with this five-path would two-cover H; therefore H-W is non-Hamiltonian and minimum-counterexample calculus gives path-cover number two. In the second case the reverse cross triple is tight directly. The other facing pair is identical, using the universal hooks (q_1,q_0,x) and (x,p_m,p_{m-1}) and testing (q_0,x,p_m). These are the only two facing pairs for which the hook orientations concatenate through x without reversing a displayed path.
