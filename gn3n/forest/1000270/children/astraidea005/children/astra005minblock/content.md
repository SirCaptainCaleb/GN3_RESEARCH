# Minimal prescribed-separation failures have doubly blocked deletion covers

## Statement

Assume Astra idea 005 is false, and choose a counterexample (H;s,t) of minimum order: s and t are distinct vertices of H and no spanning two-cover separates them. Then for every v outside {s,t} and every separating two-cover P|Q of H-v with s in P and t in Q, both components have order at least three, and both induced enlargements H[V(P) union {v}] and H[V(Q) union {v}] are non-Hamiltonian. Consequently v is noninsertable into every position of every displayed Hamilton order on P and on Q.

## Body

Fix v outside {s,t}. By minimality of H, the proper induced subtournament H-v satisfies the prescribed-separation statement for s,t, so choose a separating two-cover P|Q with s in V(P) and t in V(Q). If, say, |P|<=2, then V(P) union {v} has at most three vertices and therefore has a Hamilton tight path. Replacing P by that path while leaving Q unchanged gives a spanning two-cover of H that still separates s and t, contradiction. Thus |P|,|Q|>=3. Now if H[V(P) union {v}] were Hamiltonian, a Hamilton path on that support together with Q would again be a spanning two-cover of H separating s and t. Hence H[V(P) union {v}] is non-Hamiltonian; symmetrically H[V(Q) union {v}] is non-Hamiltonian. In particular no insertion of v into any displayed Hamilton order on P or Q can succeed, since such an insertion would itself Hamiltonize the corresponding enlarged support.
