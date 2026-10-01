# Opposite component-end hooks force a Hamiltonian five-window or a reverse cross triple

## Statement

Let H be a minimum counterexample and let H-x=P|Q be a deletion two-cover, with displayed paths P=(p_0,...,p_m) and Q=(q_0,...,q_s), where both components have order at least three. For the facing endpoint pair p_0,q_s, exactly one of the following holds. (1) (p_0,x,q_s) is tight; then (p_1,p_0,x,q_s,q_{s-1}) is a tight Hamilton path on a proper five-set W, and H-W is non-Hamiltonian with path-cover number two. (2) (p_0,x,q_s) is non-tight; then boundary antisymmetry forces the tight reverse cross triple (q_s,x,p_0). The analogous statement holds for the other facing pair q_0,p_m. No assertion is made here for the same-end pairs p_0,q_0 or p_m,q_s.

## Body

The endpoint-hook theorem c38e8b5c48ee gives (p_1,p_0,x) and (x,q_s,q_{s-1}) tight. Boundary antisymmetry gives exactly one of (p_0,x,q_s) and (q_s,x,p_0) as tight.

If (p_0,x,q_s) is tight, then the three consecutive triples of
(p_1,p_0,x,q_s,q_{s-1})
are precisely (p_1,p_0,x), (p_0,x,q_s), and (x,q_s,q_{s-1}), so this is a tight Hamilton path on W={p_1,p_0,x,q_s,q_{s-1}}. A minimum counterexample has order greater than ten, so W is proper. If H-W were Hamiltonian, its Hamilton path together with this five-path would form a spanning two-cover of H. Hence H-W is non-Hamiltonian, and minimum-counterexample calculus gives path-cover number two.

If (p_0,x,q_s) is non-tight, boundary antisymmetry gives the reverse cross triple (q_s,x,p_0) tight.

The same argument applies to the other facing pair q_0,p_m, using the hooks (q_1,q_0,x) and (x,p_m,p_{m-1}). It does not assert an analogous five-window for the same-end pairs p_0,q_0 or p_m,q_s.