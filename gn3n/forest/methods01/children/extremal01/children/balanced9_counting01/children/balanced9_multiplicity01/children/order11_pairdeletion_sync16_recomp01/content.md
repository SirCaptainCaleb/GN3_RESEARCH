# Order-eleven pair-deletion restoration synchronization

## Statement

Let H be an eleven-vertex boundary tournament with path-cover number greater than two, and fix distinct vertices x,y. Then H-{x,y} has at least twelve balanced Hamiltonian 4|5 covers A|B. Among these covers, at least three distinct covers satisfy one common obstruction type: (1) x is nonabsorbable into both A and B; (2) y is nonabsorbable into both A and B; (3) neither x nor y extends the four-side A Hamiltonianly; or (4) neither x nor y extends the five-side B Hamiltonianly. In case (3), H contains at least nine distinct Hamiltonian five-sets containing {x,y}. In case (4), there is at least one four-set D in H-{x,y} such that both D union {x} and D union {y} are Hamiltonian.

## Body

Apply balanced9_multiplicity01 to H-{x,y}; this gives at least twelve distinct Hamiltonian 4|5 covers A|B. For one such cover, form the bipartite absorption graph on {x,y} versus {A,B}, joining an omitted label to a displayed side when their union is Hamiltonian. A matching of size two would give two disjoint Hamiltonian supports partitioning V(H), hence a spanning two-cover, contrary to the hypothesis. Thus every absorption graph has matching number at most one, so its edges lie in a star and at least one of x,y,A,B has degree zero. Choose one zero-degree type per cover. By pigeonhole, one type occurs on at least three covers, giving alternatives (1)-(4).

Assume case (3). Let F be the family of at least three distinct four-sides A. For each A in F, both A union {x} and A union {y} are non-Hamiltonian. By two_bad_five_extensions_all_opposite01, every triple T=A-{a} gives a Hamiltonian five-set {x,y} union T. Hence the number of distinct such five-sets is at least the size of the 3-shadow of F. For three distinct four-sets, Kruskal-Katona gives shadow size at least 9 (3=C(4,4)+C(3,3)+C(2,2), so the lower shadow is at least C(4,3)+C(3,2)+C(2,1)=9). Thus case (3) yields at least nine distinct common-pair Hamiltonian five-sets.

Assume case (4). For each of the at least three distinct Hamiltonian five-sides B for which both B union {x} and B union {y} are non-Hamiltonian, apply 1000203 to obtain b in B such that D=B-{b} satisfies that D union {x} and D union {y} are Hamiltonian. Hence at least one such four-set D exists.
