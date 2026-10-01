# Frozen sides force disagreement on every deletion

## Statement

Let H-x=P|Q be an exact deletion two-cover in a minimum counterexample. If P union {x} is frozen with x as its unique Hamiltonian deletion, then for every p in P every exact two-cover of H-p lies in a crossing or relative-order-disagreement branch of the deletion-state trichotomy; the clean replacement/swap branch is impossible. If both enlarged sides are frozen, this holds for every vertex other than x. In the order-thirteen mu=6 shell, every such non-x deletion cover is 6|6 and both components genuinely mix the two inherited support classes.

## Body

# Frozen sides force disagreement on every deletion

Let H be a minimum counterexample and let

H-x = P | Q

be an exact two-path cover. Say that the enlarged side P union {x} is frozen at x when P is Hamiltonian but, for every p in P, the set

(P-{p}) union {x}

is non-Hamiltonian. Equivalently, x is the unique Hamiltonian deletion of P union {x}.

## Theorem

If P union {x} is frozen at x, then for every p in P and every exact two-cover F_p of H-p, the clean branch of the appropriate deletion-state trichotomy is impossible. Hence F_p exposes either support crossing or relative-order disagreement with the inherited deletion state.

If Q union {x} is frozen at x as well, the same conclusion holds for every y in V(H)-{x}.

## Proof

Write P=(p_0,...,p_m).

First let p=p_i be internal, 1<=i<=m-1. Apply the internal-deletion trichotomy to an arbitrary exact two-cover F_p of H-p relative to the fixed deletion cover H-x=P|Q. Its third, clean alternative is exactly the same-slot replacement

(p_0,...,p_{i-1},x,p_{i+1},...,p_m) | Q.

But its first component would be a Hamilton path on (P-{p}) union {x}, contradicting freezing. Therefore only the trichotomy's crossing or relative-order-disagreement alternatives can occur.

Now let p be an endpoint, p_0 or p_m. Apply the endpoint-state trichotomy. In its clean omission-swap alternative, x is restored at the same end of the same component of H-{x,p} at which p is restored in H-x=P|Q. Consequently the corresponding component of H-p is a Hamilton path on (P-{p}) union {x}, again contradicting freezing. Thus the endpoint deletion also lies in a crossing or relative-order-disagreement branch.

This proves the assertion for every p in P. Interchanging P and Q gives the second assertion. ∎

## Order-thirteen corollary

Assume in addition that |V(H)|=13 and mu=6, so every exact two-cover of every vertex deletion has orders 6,6. Suppose H-x=P|Q is a 6|6 deletion cover and P union {x} is frozen.

Fix p in P and put U=(P-{p}) union {x}. For any exact cover H-p=A|B, neither component can have support Q: if one did, the other six-vertex support would be U, which is non-Hamiltonian. Likewise neither component can have support U. Since |A|=|B|=|U|=|Q|=6, no component can even be contained in one inherited class without equaling it. Therefore both A and B meet both U and Q.

If both P union {x} and Q union {x} are frozen, this full support mixing holds for every deletion y != x, with the evident inherited bipartition obtained by replacing y with x on its original side.

Thus a genuine double-frozen order-thirteen state is not locally featureless: all twelve other vertex deletions are forced into crossed 6|6 support geometry, together with the stronger crossing/order-disagreement conclusion above.
