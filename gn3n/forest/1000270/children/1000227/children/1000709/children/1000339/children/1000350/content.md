# Small deletion sides admit a clean support exchange

## Statement

Let H be a minimum counterexample and H-x=P|Q an exact deletion two-cover with 3<=|P|<=5. Then there exists p in V(P) such that both H[V(P)-{p}] and H[(V(P)-{p}) union {x}] are Hamiltonian. Consequently H-p has an exact two-cover P_prime|Q in which the small support is obtained from V(P) by the one-for-one exchange p->x, while the opposite path Q is unchanged.

## Body

# Small deletion sides admit a clean support exchange

Let H be a minimum counterexample and let

H-x = P | Q

be an exact two-path cover with 3<=|P|<=5. Then there exists p in V(P) such that both

H[V(P)-{p}]

and

H[(V(P)-{p}) union {x}]

are Hamiltonian.

Consequently, choosing any Hamilton path P' on (V(P)-{p}) union {x}, one has an exact deletion cover

H-p = P' | Q.

Thus the omitted vertex x can replace a Hamilton-removable vertex of the small support while the opposite path Q stays fixed.

## Proof

Put

C = V(P) union {x}.

The set C is non-Hamiltonian: if it were Hamiltonian, a Hamilton path on C together with Q would two-cover H.

### Case |P|=3

For every p in V(P), the set V(P)-{p} has order two and is Hamiltonian, while (V(P)-{p}) union {x} has order three and is Hamiltonian. Any p works.

### Case |P|=4

Now C has order five and is non-Hamiltonian. A non-Hamiltonian five-set has at most one non-Hamiltonian four-vertex deletion, so at least four vertices y of C have C-{y} Hamiltonian. Since x is one such good deletion because C-{x}=V(P) is Hamiltonian, at least one p in V(P) is also good. For this p,

C-{p}=(V(P)-{p}) union {x}

is Hamiltonian, while V(P)-{p} has order three and is automatically Hamiltonian.

### Case |P|=5

Now C has order six and is non-Hamiltonian. Let

G={d in C : C-{d} is Hamiltonian}.

The four-of-six theorem gives |G|>=4, and x belongs to G because C-{x}=V(P) is Hamiltonian.

We prove that some p in G-{x} also satisfies C-{x,p}=V(P)-{p} Hamiltonian.

Assume not. Since C-{x}=V(P) is a Hamiltonian five-set, and a Hamiltonian five-set has at most three non-Hamiltonian four-subsets, the assumption forces |G|=4. Write

G={x,p_1,p_2,p_3},

and let a,b be the two vertices of C-G.

For i=1,2,3, the four-set

C-{x,p_i}
=
{a,b} union ({p_1,p_2,p_3}-{p_i})

is non-Hamiltonian by assumption.

Fix the pair {a,b}. Partition {p_1,p_2,p_3} into

X_+={v:(a,v,b) is tight},
X_-={v:(b,v,a) is tight}.

Boundary antisymmetry gives a partition. If two distinct vertices u,v lie in X_+, then (a,u,b) and (a,v,b) are tight. The parallel-middle lemma gives a Hamilton tight path on {a,b,u,v}. Hence a non-Hamiltonian four-set {a,b,u,v} can only have u,v in opposite classes. The same is true in X_-.

Therefore the graph on {p_1,p_2,p_3} in which uv is an edge exactly when {a,b,u,v} is non-Hamiltonian is bipartite with bipartition X_+|X_-.

But the three assumed bad four-sets say that all three pairs p_1p_2, p_1p_3, p_2p_3 are edges, giving a triangle. Contradiction.

Hence some p in G-{x} makes V(P)-{p}=C-{x,p} Hamiltonian. Since p in G, the exchanged support (V(P)-{p}) union {x}=C-{p} is Hamiltonian as well.

This proves all cases.

Finally choose a Hamilton path P' on the exchanged support. The sets (V(P)-{p}) union {x} and V(Q) partition V(H)-{p}, so P'|Q is the asserted exact cover of H-p. ∎

## Reconfiguration consequence

For every deletion-cover side of order three, four, or five, support-level omission exchange is not merely possible in the abstract D=1 state graph: there is a one-for-one exchange x<->p through a common Hamiltonian core V(P)-{p}, with the opposite component unchanged.

Thus any genuine trapping mechanism for the one-defect route must either begin at side order at least six or forbid the use of this clean exchanged deletion state by additional mixed-support constraints.
