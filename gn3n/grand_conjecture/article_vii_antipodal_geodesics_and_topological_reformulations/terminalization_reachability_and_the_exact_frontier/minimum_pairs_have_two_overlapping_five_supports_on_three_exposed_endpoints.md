# Minimum pairs have two overlapping five-supports on three exposed endpoints

## Composition

(none yet)

## Development

## Four-of-six gives two overlapping hole-preserving five-supports

Let
[
X={x,y}
]
be a minimum two-cover deletion pair and let
[
H-X=Pmid Q,
]
where
[
P=(p_1,ldots,p_m),qquad Q=(q_1,ldots,q_t),
qquad m,tge2.
]

Put
[
U={x,y,p_1,p_m,q_1,q_t}.
]

By the four-of-six theorem, at least four of the six one-vertex deletions
[
U-{v}
]
are Hamiltonian five-sets.

Only two deletion labels, (x) and (y), remove a hole. Therefore at least two of the four exposed endpoint labels
[
ein{p_1,p_m,q_1,q_t}
]
satisfy
[
oxed{U-{e}	ext{ is Hamiltonian}.}
]

For each such endpoint (e), the support
[
S_e=U-{e}
]
contains both hole labels and three of the four exposed endpoints.

Moreover (H-S_e) is covered by at most two inherited contiguous path intervals. Indeed, removing three displayed endpoints from (P|Q) leaves, on each original path, either the whole path, a one-sided truncation, its interior, or the empty path.

Hence:

> **Two five-seed theorem.** Every genuine minimum deletion pair admits at least two distinct Hamiltonian five-supports containing both holes and three exposed endpoints of a displayed complementary two-cover, and each support has an inherited two-coverable complement.

The two supports differ by exchanging their omitted exposed endpoints and intersect in a four-set containing
[
{x,y}
]
and at least two exposed endpoints.

This strengthens the exposed-endpoint four-support theorem: the minimum-pair interface always has a pair of overlapping order-five admissible seeds, not merely one bounded support.

No cyclic rotation, path reversal, minimum-counterexample hypothesis, or computation is used.
