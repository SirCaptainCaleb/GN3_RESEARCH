# A five-side at a local quadratic minimum forces endpoint six-set order disagreement

## Statement


Let H be a boundary tournament and let C=X|P|Q be a spanning three-cover that minimizes the quadratic potential Phi within its connected component of the pairwise-repartition graph. Assume X is a Hamiltonian path of order five and P=(p_1,...,p_m) has order m>=7. Then for each displayed endpoint e in {p_1,p_m}, the six-set K=V(X) union {e} is non-Hamiltonian and has at least four Hamiltonian one-vertex deletions. Consequently arbitrary Hamilton paths chosen on four such deletions contain a pair with relative-order disagreement; hence K contains one of the standard reversed-edge, reversing-triple, or tight-cycle witnesses.

Thus a five-side beside a path of order at least seven cannot occur order-neutrally at a local quadratic minimum.


## Body


Fix an endpoint e of P. If H[V(X) union {e}] were Hamiltonian, repartition the pair X|P as
(V(X) union {e}) | (P-e),
where P-e is the inherited endpoint truncation. The changed component orders are 5,m -> 6,m-1, so
Delta Phi = 6^2+(m-1)^2-[5^2+m^2] = 12-2m < 0
for m>=7. This is a legal pairwise repartition in the same connected component, contradicting local Phi-minimality. Hence K=H[V(X) union {e}] is non-Hamiltonian.

The certified four-of-six theorem in smallset01 says every six-vertex boundary tournament has at least four vertices d for which K-d is Hamiltonian. Apply astra004fourgooddisagree to K and any four such deletion labels. For arbitrary Hamilton paths chosen on those four Hamiltonian deletions, some two order two common vertices differently. The certified path-intersection calculus then yields a reversed common ordered edge, a tight triple reversing an ordered edge at an intersection, or a vertex-simple tight cycle.

The argument is identical for the other displayed endpoint of P. No minimum-counterexample, trappedness, or global-minimality hypothesis is used.
