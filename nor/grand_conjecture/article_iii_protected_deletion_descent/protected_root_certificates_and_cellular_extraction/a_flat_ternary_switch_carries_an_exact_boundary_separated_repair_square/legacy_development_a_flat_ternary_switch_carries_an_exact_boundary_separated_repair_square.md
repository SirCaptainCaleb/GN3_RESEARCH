# A flat ternary switch carries an exact boundary-separated repair square — preserved pre-item development

## Composition

(none yet)

## Development

## A flat ternary switch carries an exact boundary-separated repair square

Work in the coboundary-flat alternating ternary sector. Let four consecutive coordinates

(a,b,c,d)

carry a flat transition

alpha(a,b,c)=x,
alpha(b,c,d)=1-x.

Flatness gives the two endpoint-repair faces

alpha(a,b,d)=x,
alpha(a,c,d)=1-x.

Consider the two disjoint adjacent transpositions

L: swap a,b,
R: swap c,d.

They commute as permutations, so they generate an actual four-state square of full coordinate orders with the same outside order.

### The four local words

Original state:
(a,b,c,d)
has word
(x,1-x).

Right repair:
(a,b,d,c)
has statuses
alpha(a,b,d)=x,
alpha(b,d,c)=1-alpha(b,c,d)=x,
so its local word is
(x,x).

Left repair:
(b,a,c,d)
has statuses
alpha(b,a,c)=1-alpha(a,b,c)=1-x,
alpha(a,c,d)=1-x,
so its local word is
(1-x,1-x).

Opposite corner:
(b,a,d,c)
has statuses
alpha(b,a,d)=1-alpha(a,b,d)=1-x,
alpha(a,d,c)=1-alpha(a,c,d)=x,
so its local word is
(1-x,x).

Thus the exact square is

(a,b,c,d):      x,1-x
(a,b,d,c):      x,x
(b,a,c,d):      1-x,1-x
(b,a,d,c):      1-x,x.

The two side corners are precisely the two endpoint repairs, each absorbing the switch into one of its neighboring colors; the opposite corner carries the reversed transition.

### Boundary separation

The R move changes only the order of c,d and leaves the entire prefix through the ordered pair (a,b) fixed.

The L move changes only a,b and leaves the entire suffix beginning with the ordered pair (c,d) fixed.

Consequently:
- all windows sufficiently far to the left are identical on the two R-related edges;
- all windows sufficiently far to the right are identical on the two L-related edges;
- both moves preserve the outside coordinate order;
- the only interaction between L and R is inside the bounded window packet meeting {a,b,c,d}.

Hence this is an honest boundary-separated gluing cell, not merely an abstract Coxeter square.

### Transport-complex consequence

A one-sided flat transport flag chooses one of the two side vertices according to which boundary must be repaired outward. If two compatible transport trajectories diverge at the same flat switch by choosing opposite endpoint repairs, their first divergence is contained in this realized four-state square.

Therefore the first branching cell of the flat transport complex needs no missing-corner realization theorem: its fourth order already exists and retains both outside tails. Any failure to glue the two branches is entirely a bounded central-window compatibility issue.

Combined with the zero-free single-flag theorem, this localizes the first possible topological interaction of two opposite repair directions to an explicit four-coordinate square. The next extraction step is to classify the target/violation labels on this square and show that a complementary label event gives either a threshold improvement or one of the already-controlled A3/Tucker repair packets.
