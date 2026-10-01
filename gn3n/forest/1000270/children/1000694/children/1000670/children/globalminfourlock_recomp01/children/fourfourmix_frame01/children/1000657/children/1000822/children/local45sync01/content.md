# A trapped quadratic minimum of profile 4|5|a has a synchronized four-side label

## Statement

Let H be a boundary tournament and let C=X|Y|P be a spanning three-cover. Suppose C minimizes the quadratic potential Phi within its connected component of the pairwise-repartition graph, and that component contains no two-cover. Assume |X|=4, |Y|=5, and P=(p_1,...,p_a) with a>=7. Then there exists x in V(X) such that both (V(X)-{x}) union {p_1} and (V(X)-{x}) union {p_a} are Hamiltonian, V(Y) union {x} is non-Hamiltonian, and at least three vertices y in V(Y) satisfy (V(Y)-{y}) union {x} Hamiltonian.

## Body

Let C=X|Y|P minimize Phi inside its connected component K of the pairwise-repartition graph, where K contains no two-cover, |X|=4, |Y|=5, and P=(p_1,...,p_a) with a>=7.

Fix an endpoint e in {p_1,p_a}. We first show that V(X) union {e} is non-Hamiltonian. Otherwise X|P has the pairwise repartition
(V(X) union {e}) | (P-e),
where P-e is the inherited endpoint truncation. The component orders 4,a become 5,a-1, so
Phi(C)-Phi(C')=16+a^2-[25+(a-1)^2]=2a-10>0.
This gives a lower-Phi state in K, contradicting the choice of C.

For e=p_1 and e=p_a, the five-set V(X) union {e} is therefore non-Hamiltonian, while deleting e leaves the Hamiltonian four-set V(X). By smallset01, a non-Hamiltonian five-set has at most one non-Hamiltonian four-vertex deletion. Hence for each endpoint e there are at least three vertices x in V(X) such that
(V(X)-{x}) union {e}
is Hamiltonian. Let I_1 and I_a be the corresponding subsets of V(X). Since |I_1|,|I_a|>=3 and |V(X)|=4, choose x in I_1 intersect I_a.

We next show that V(Y) union {x} is non-Hamiltonian. Suppose it were Hamiltonian. Repartition X|Y as
(X-x) | (V(Y) union {x}).
Every three-vertex boundary tournament is Hamiltonian, so this is legal. The pair orders 4,5 become 3,6, increasing Phi by
3^2+6^2-(4^2+5^2)=4.

Now use e=p_1. Since x lies in I_1, the set (V(X)-{x}) union {p_1} is Hamiltonian. Repartition the current three-vertex component X-x together with P as
((V(X)-{x}) union {p_1}) | (P-p_1).
This changes pair orders 3,a to 4,a-1 and decreases Phi by
3^2+a^2-[4^2+(a-1)^2]=2a-8.
Across the two legal pairwise repartitions the net change is therefore a decrease of
(2a-8)-4=2a-12>0
because a>=7. The resulting state lies in K, contradicting Phi-minimality. Thus V(Y) union {x} is non-Hamiltonian.

Finally apply the six-set Hamiltonian-deletion bound from smallset01 to V(Y) union {x}. At least four of its six five-vertex deletions are Hamiltonian. Deleting x leaves V(Y), which is Hamiltonian, so at least three distinct y in V(Y) satisfy
(V(Y)-{y}) union {x}
Hamiltonian.

Thus the global 4|5|a synchronization phenomenon persists at a quadratic minimum inside any trapped connected component of the pairwise-repartition graph.
