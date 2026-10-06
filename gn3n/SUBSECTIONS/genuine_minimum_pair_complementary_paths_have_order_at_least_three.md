# Genuine minimum-pair complementary paths have order at least three

## Metadata

- ID: genuine_minimum_pair_complementary_paths_have_order_at_least_three
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 179
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## A genuine minimum-pair complement has no component of order one or two

Let
[
X={x,y}
]
be a minimum two-cover deletion pair in a boundary tournament (H) with no spanning two-cover, and write
[
H-X=Pmid Q.
]

Neither (P) nor (Q) can have order at most two.

A singleton component was already excluded: if
[
P={p},
]
then every three-vertex boundary tournament is Hamiltonian, so
[
{x,y,p}mid Q
]
is a spanning two-cover of (H).

Now suppose
[
P=(p_1,p_2)
]
has order two.

Minimum-hole four-end synchronization applies to each hole (zin{x,y}). Since the initial and terminal edge of (P) are the same two labels, it gives
[
h(p_2,p_1,z)=1
]
from the initial boundary and
[
h(z,p_2,p_1)=1
]
from the terminal boundary.

In particular
[
h(x,p_2,p_1)=1,
qquad
h(p_2,p_1,y)=1.
]
Therefore
[
(x,p_2,p_1,y)
]
is a tight Hamiltonian four-path on
[
{x,y,p_1,p_2}.
]

Its complement is exactly the Hamiltonian path (Q). Hence
[
(x,p_2,p_1,y)mid Q
]
is a spanning two-cover of (H), contradiction.

The argument for (Q) is symmetric.

Thus:

> **Order-three lower bound.** In every genuine minimum deletion-pair state with no spanning two-cover,
> [
> |P|,|Q|ge3.
> ]

This is an audit-safe consequence of the actual four-end synchronization identities. It does not use cyclic rotation or path reversal.

Consequently the original genuine two-deletion frame always has two genuine boundary layers on both complementary paths, so second-layer endpoint arguments may be applied there without a separate order-two exception.
