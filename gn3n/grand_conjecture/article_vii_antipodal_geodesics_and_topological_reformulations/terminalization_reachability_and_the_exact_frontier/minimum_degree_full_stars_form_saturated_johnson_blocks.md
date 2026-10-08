# Minimum-degree full stars form saturated Johnson blocks

## Composition

## Minimum-degree full stars form uniform Johnson blocks

Retain a minimum-degree full-star source D from [[minimum_degree_full_stars_force_uniform_exterior_polarity]], with |D|=d.

Call y outside D exchangeable when it has Type II (lower) polarity. Then for every x in D,
D-x+y
is another full-star source of degree d.

Let F be the family of all degree-d full-star sources reachable from D by one-element exchanges.

### Exchangeability is invariant across the reachable family

Suppose y is exchangeable from D and put
D'=D-x+y.
Let z be another label outside D'.

If z was exchangeable from D, then z is exchangeable from D'.

Indeed, D'-y+z=D-x+z is already a full-star source. If z had Type I polarity relative to D', then every one-exchange set D'-u+z would be Hamiltonian, in particular the set obtained with u=y. That would make D-x+z Hamiltonian, contradicting that it is a full-star source and hence non-Hamiltonian.

Similarly, if z has Type I polarity relative to D, it cannot become exchangeable relative to D': if it did, exchanging y out of D' would make D-x+z a full-star source, whereas Type I relative to D makes D-x+z Hamiltonian.

Thus the partition into exchangeable and nonexchangeable exterior labels is invariant under every allowed Johnson exchange.

### Uniform Johnson block

Let U be D together with all labels exchangeable from D.

By repeated exchanges, every d-subset F of U is a full-star source. Conversely no d-set obtained from such an F by replacing one element with a label outside U is a full-star source; that replacement is Hamiltonian by Type I polarity.

Therefore:
1. every d-subset of U is non-Hamiltonian;
2. every (d-1)-subset of U is Hamiltonian.

For (2), given R subset U with |R|=d-1, choose u in U-R and set F=R+u. Since F is a full-star source, F-u=R is Hamiltonian.

Moreover, for every y outside U and every (d-1)-subset R of U,
R+y
is Hamiltonian: choose u in U-R, let F=R+u, and apply Type I polarity of y relative to F.

Thus U is a saturated bad Johnson block:
- the entire layer binom(U,d) is non-Hamiltonian;
- the preceding layer binom(U,d-1) is Hamiltonian;
- replacing any one member of a bad d-set by a label outside U makes the resulting d-set Hamiltonian.

This identifies the global minimum-counterexample cubical obstruction with the late missing-facet/Johnson obstruction. The latter is not merely a local homological artifact: it is forced by any surviving minimum-degree cubical core.

### Immediate low-rank eliminations

If d=4 and |U|>=5, this is impossible because a five-set cannot have all five of its four-subsets non-Hamiltonian; the audited five-set theorem gives at least three Hamiltonian four-subsets. Hence d=4 forces |U|=4.

If d=5 and |U|>=6, this is impossible by the four-of-six theorem: every six-set has at least four Hamiltonian five-subsets. Hence d=5 forces |U|=5.

For higher d the remaining question is scale-independent: can a boundary tournament contain a saturated Johnson block with every (d-1)-subset Hamiltonian and every d-subset non-Hamiltonian? The minimum-counterexample obstruction has now been reduced exactly to this structure, together with the uniform Type I behavior of all labels outside U.

## Development

## Minimum-degree full stars form uniform Johnson blocks

Retain a minimum-degree full-star source D from [[minimum_degree_full_stars_force_uniform_exterior_polarity]], with |D|=d.

Call y outside D exchangeable when it has Type II (lower) polarity. Then for every x in D,
D-x+y
is another full-star source of degree d.

Let F be the family of all degree-d full-star sources reachable from D by one-element exchanges.

### Exchangeability is invariant across the reachable family

Suppose y is exchangeable from D and put
D'=D-x+y.
Let z be another label outside D'.

If z was exchangeable from D, then z is exchangeable from D'.

Indeed, D'-y+z=D-x+z is already a full-star source. If z had Type I polarity relative to D', then every one-exchange set D'-u+z would be Hamiltonian, in particular the set obtained with u=y. That would make D-x+z Hamiltonian, contradicting that it is a full-star source and hence non-Hamiltonian.

Similarly, if z has Type I polarity relative to D, it cannot become exchangeable relative to D': if it did, exchanging y out of D' would make D-x+z a full-star source, whereas Type I relative to D makes D-x+z Hamiltonian.

Thus the partition into exchangeable and nonexchangeable exterior labels is invariant under every allowed Johnson exchange.

### Uniform Johnson block

Let U be D together with all labels exchangeable from D.

By repeated exchanges, every d-subset F of U is a full-star source. Conversely no d-set obtained from such an F by replacing one element with a label outside U is a full-star source; that replacement is Hamiltonian by Type I polarity.

Therefore:
1. every d-subset of U is non-Hamiltonian;
2. every (d-1)-subset of U is Hamiltonian.

For (2), given R subset U with |R|=d-1, choose u in U-R and set F=R+u. Since F is a full-star source, F-u=R is Hamiltonian.

Moreover, for every y outside U and every (d-1)-subset R of U,
R+y
is Hamiltonian: choose u in U-R, let F=R+u, and apply Type I polarity of y relative to F.

Thus U is a saturated bad Johnson block:
- the entire layer binom(U,d) is non-Hamiltonian;
- the preceding layer binom(U,d-1) is Hamiltonian;
- replacing any one member of a bad d-set by a label outside U makes the resulting d-set Hamiltonian.

This identifies the global minimum-counterexample cubical obstruction with the late missing-facet/Johnson obstruction. The latter is not merely a local homological artifact: it is forced by any surviving minimum-degree cubical core.

### Immediate low-rank eliminations

If d=4 and |U|>=5, this is impossible because a five-set cannot have all five of its four-subsets non-Hamiltonian; the audited five-set theorem gives at least three Hamiltonian four-subsets. Hence d=4 forces |U|=4.

If d=5 and |U|>=6, this is impossible by the four-of-six theorem: every six-set has at least four Hamiltonian five-subsets. Hence d=5 forces |U|=5.

For higher d the remaining question is scale-independent: can a boundary tournament contain a saturated Johnson block with every (d-1)-subset Hamiltonian and every d-subset non-Hamiltonian? The minimum-counterexample obstruction has now been reduced exactly to this structure, together with the uniform Type I behavior of all labels outside U.
