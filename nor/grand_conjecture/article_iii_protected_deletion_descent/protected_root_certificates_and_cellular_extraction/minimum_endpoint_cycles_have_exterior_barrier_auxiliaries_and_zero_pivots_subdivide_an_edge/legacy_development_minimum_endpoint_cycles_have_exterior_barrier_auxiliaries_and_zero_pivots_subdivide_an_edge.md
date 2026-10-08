# Minimum protected-root cycles have exterior barrier auxiliaries and zero pivots subdivide an edge — preserved pre-item development

## Composition

(none yet)

## Development

## Minimum protected-root cycles have exterior barrier auxiliaries and zero pivots subdivide an edge

Work in the coboundary-flat alternating sector. Let
[
C:x_0	o x_1	ocdots	o x_{k-1}	o x_0
]
be a minimum-length directed cycle in the class of **actual realized protected roots**. Assume one edge
[
x_i	o x_{i+1}
]
is an endpoint-barrier root, witnessed by a normalized deletion order
[
O_i=(a_i,b_i,x_{i+1},d_i,ldots)
]
omitting (x_i). Prepending (x_i) gives the fully-curved barrier
[
(x_i,a_i,b_i,x_{i+1}).
]

### Both barrier auxiliaries lie outside the cycle support

By the complete (K_{2,2}) barrier square (§230), this same tetrahedron realizes
[
x_i	o b_i,qquad a_i	o x_{i+1}.
]

If (b_i) belonged to the cycle support, then (b_i
e x_i,x_{i+1}), so (x_i	o b_i) would be a directed chord. It closes with the old directed return segment from (b_i) to (x_i) to give a strictly shorter cycle of actual protected roots, contradicting minimality.

Likewise, if (a_i) belonged to the support, then (a_i	o x_{i+1}) would be a non-cycle directed chord and would again produce a shorter protected-root cycle.

Therefore
[
oxed{a_i,b_i
otin S(C)}
]
for every endpoint-barrier edge occurring in a minimum protected-root cycle.

### A zero first-pivot bit gives an actual support-expanding subdivision

Put
[
lambda_i=alpha(a_i,x_{i+1},d_i).
]
If (lambda_i=0), the endpoint pivot theorem (§113) gives a genuine one-change deletion witness omitting (b_i), whose endpoint root is
[
b_i	o x_{i+1}.
]

The original endpoint barrier already realizes
[
x_i	o b_i
]
as a (K_{2,2}) side root.

Hence the old cycle edge has the witness-supported factorization
[
oxed{x_i	o x_{i+1}
quadleadstoquad
x_i	o b_i	o x_{i+1}.}
]

Both factors are actual protected roots, and (b_i
otin S(C)). Replacing the edge therefore gives a simple directed protected-root cycle whose support is exactly
[
S(C)cup{b_i}.
]

The new cycle is longer, so this does not contradict minimum length. Its significance is support growth with complete provenance.

### Consequence

For endpoint-barrier edges inside the global protected-root circuit problem:

- the two barrier auxiliaries are forced outside any minimum protected circuit;
- a zero first-pivot bit subdivides the physical edge through a new exterior coordinate by two actual protected roots;
- a one first-pivot bit enters the stopped-pivot/root-ejection branch of §§119,125.

Thus endpoint pivots provide a canonical **circuit subdivision operation**. This supplies a concrete route from proper-support protected cycles toward larger-support mixed cycles without any endpoint square-lift assumption.
