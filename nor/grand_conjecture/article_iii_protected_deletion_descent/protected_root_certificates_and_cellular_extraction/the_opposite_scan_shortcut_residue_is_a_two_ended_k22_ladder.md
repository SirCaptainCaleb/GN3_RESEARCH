# The opposite-scan shortcut residue is a two-ended K22 ladder

## Composition

(none yet)

## Development

## The opposite-scan shortcut residue is a two-ended K22 ladder

Continue from §§299–301. Let
[
O=(w_1,ldots,w_m)
]
be a good order of (Vsetminus{x,z}) with word (0^p1^q). In the sole unresolved shortcut residue normalize
[
alpha(x,w_1,w_2)=0,qquad
alpha(z,w_1,w_2)=1,
]
[
alpha(w_{m-1},w_m,x)=1,qquad
alpha(w_{m-1},w_m,z)=0.
]

Thus both
[
xO,qquad Ox
]
are NOR-good deletion witnesses omitting (z), and both have the same inherited internal switch as (O).

### Pair insertion forces the x-z end bits

Put
[
c_L=alpha(x,z,w_1).
]
For the full order
[
z,x,O
]
the first two statuses are
[
1-c_L, 0,
]
followed by the old zero phase.

If (c_L=1), these statuses are (0,0), so the whole full order remains one-change, contradiction. Hence
[
oxed{alpha(x,z,w_1)=0.}
]

Similarly put
[
c_R=alpha(x,z,w_m)=alpha(w_m,x,z)
]
by cyclic invariance.

For
[
O,x,z
]
the terminal statuses are
[
1, c_R.
]
If (c_R=1), the old one phase extends monotonically and NOR closes. Therefore
[
oxed{alpha(x,z,w_m)=0.}
]

### The left endpoint barrier

Prepend (z) to the good deletion witness (xO):
[
(z,x,w_1,w_2,ldots).
]
Its first two statuses are
[
alpha(z,x,w_1)=1,qquad
alpha(x,w_1,w_2)=0.
]
Since (xO) is good and the ambient instance is a counterexample, this endpoint transition is fully curved by the standard endpoint theorem.

Hence the four-set
[
(z,x,w_1,w_2)
]
realizes the complete protected (K_{2,2}) square
[
{z,x}longrightarrow{w_1,w_2}.
]

### The right endpoint barrier

Append (z) to the other good deletion witness (Ox):
[
(ldots,w_{m-1},w_m,x,z).
]
Its last two statuses are
[
alpha(w_{m-1},w_m,x)=1,qquad
alpha(w_m,x,z)=0.
]
Again the endpoint transition is fully curved.

Thus
[
(w_{m-1},w_m,x,z)
]
realizes the complete protected square
[
{w_{m-1},w_m}longrightarrow{x,z}.
]

### Theorem

Every surviving certified-shortcut failure (x	o z) has the rigid form
[
oxed{
{x,z}	o{w_1,w_2}
quad|quad
O	ext{ with one fixed switch}
quad|quad
{w_{m-1},w_m}	o{x,z}.
}
]

The distinguished pair ({x,z}) is the source shore of a fully-curved barrier at the left end and the target shore of a fully-curved barrier at the right end.

This is a closed two-ended (K_{2,2}) ladder around one good middle carrier. The remaining shortcut problem is therefore to propagate one protected branch from the left barrier through the single switch of (O) to the right barrier, or obtain NOR closure.
