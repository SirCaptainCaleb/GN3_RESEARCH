# Two-vertex collective insertion couples adjacent blocker words

## Composition

In a pair-normalized square-path gauge with a→b, inserting (a,b) is equivalent to six staggered cross incidences: c_{i−1},c_i→a; c_i→b; a→c_{i+1}; b→c_{i+1},c_{i+2}. A simultaneous switch complement gives the complementary pattern. This strengthens individual insertion blockers but retains the ordered internal-edge prerequisite.

## Development

Let C=(c_1,...,c_m) be a compatible zero connector in path-normalized square-path gauge, and let a,b be two uncovered shore vertices. Choose switching states on a,b so that the ordered pair a,b is forward. This choice is unique up to complementing both switch bits simultaneously.

Insert the two-vertex zero block (a,b) between c_i and c_{i+1}. The enlarged order is a directed square-path exactly when the six cross edges
c_{i-1}->a,
c_i->a,
c_i->b,
a->c_{i+1},
b->c_{i+1},
b->c_{i+2}
all point forward.
No additional internal condition exists beyond a->b.

Thus if r^a_j records c_j->a and r^b_j records c_j->b in this pair-normalized gauge, legal insertion at gap i is exactly
r^a_{i-1}=r^a_i=r^b_i=1
and
r^a_{i+1}=r^b_{i+1}=r^b_{i+2}=0.
Complementing both outside switch bits gives the complementary legal pattern.

Reversing the ordered block exchanges a and b and gives the symmetric criterion.

Consequently support maximality imposes a genuinely collective restriction: for every uncovered pair {a,b}, in both possible internal orders, the two incidence words avoid this staggered six-bit transition at every gap. This condition is strictly stronger than the separate one-vertex avoidance of 0011/1100 and is the natural next object for a least-unreachable or exchange argument.
