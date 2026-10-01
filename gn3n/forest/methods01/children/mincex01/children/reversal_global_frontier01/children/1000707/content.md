# A matching-block reversal four-set always extends to a Hamiltonian four- or five-set

## Statement

Let H be a minimum counterexample and let X be the non-Hamiltonian edge-orderable matching-block four-set arising from the reversed-edge classification. Let T be any tight three-vertex path contained in X; in particular one may take the complete reverse-fan triple supplied by 4f2ce6135f9c. Then for every vertex y outside X, at least one of T union {y} and X union {y} is Hamiltonian.

Consequently the matching-block complete reverse fan alternative of reversal_global_frontier01 always yields a proper Hamiltonian induced set W of order four or five whose complement is non-Hamiltonian with path-cover number two. Thus that alternative is not a separate terminal frontier.

## Body

Fix y outside X.

If T union {y} is Hamiltonian, take W=T union {y} and we are done.

Assume T union {y} is non-Hamiltonian. Suppose for contradiction that the five-set X union {y} is also non-Hamiltonian. By smallset01, every non-Hamiltonian five-vertex boundary tournament is edge-orderable. Hence there is one edge order on the complete graph over X union {y} that represents all tight triples of this induced boundary tournament.

In that single edge order, the two four-sets
X
and
T union {y}
are both non-Hamiltonian and meet in the three-set T. Apply smallset01 Section 4.2: two non-Hamiltonian four-sets meeting in three vertices inside one edge-ordered complete graph force their five-vertex union to have an increasing Hamilton path. Their union is exactly X union {y}, contradicting its assumed non-Hamiltonicity.

Therefore X union {y} is Hamiltonian whenever T union {y} is not. This proves the local four-or-five alternative for every y outside X.

In a minimum counterexample |V(H)|>10, so a vertex y outside X certainly exists and either resulting support W is proper. If H-W were Hamiltonian, Hamilton paths on W and H-W would form a spanning two-cover of H. Thus H-W is non-Hamiltonian. Minimality gives path-cover number at most two, so it is exactly two.

No cyclic permutation or path reversal is used.
