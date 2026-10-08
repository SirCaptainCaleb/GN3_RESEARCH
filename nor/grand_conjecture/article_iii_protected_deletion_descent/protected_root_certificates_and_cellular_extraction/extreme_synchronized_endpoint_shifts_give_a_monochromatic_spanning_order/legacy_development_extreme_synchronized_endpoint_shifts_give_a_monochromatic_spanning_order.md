# Extreme synchronized endpoint shifts give a monochromatic spanning order — preserved pre-item development

## Development

## Extreme synchronized endpoint shifts give a monochromatic spanning order

Consider the endpoint rank-two protected cycle

rho_i=e_{x_i}-e_{x_{i+1}}

of length k. Assume the physical cycle is Hamiltonian on the whole ambient coordinate set, so

V={x_0,...,x_{k-1}}.

Suppose the partner assignment is synchronized:

a_i=x_{i+r}

for one fixed offset r in {2,...,k-1}, with cyclic indices.

Each endpoint witness begins

(a_i,b_i,x_{i+1},...)

and prepending the omitted x_i produces the endpoint transition

alpha(x_i,a_i,b_i)=1,
alpha(a_i,b_i,x_{i+1})=0,

supported on the fully-curved tetrahedron

{x_i,a_i,b_i,x_{i+1}}.

For a fully-curved 1->0 tetrahedron, the off-diagonal face satisfies

alpha(x_i,a_i,x_{i+1})=0.

### Offset r=2

Now a_i=x_{i+2}. Hence

alpha(x_i,x_{i+2},x_{i+1})=0.

Swap the final two entries. Alternation gives

alpha(x_i,x_{i+1},x_{i+2})=1

for every i.

Therefore the cyclic physical order

(x_0,x_1,...,x_{k-1})

has every consecutive ternary window of color 1. In particular its linear version is a spanning monochromatic order, proving NOR.

### Offset r=k-1

Now a_i=x_{i-1}. The endpoint identity gives

alpha(x_i,x_{i-1},x_{i+1})=0.

Swap the first two entries:

alpha(x_{i-1},x_i,x_{i+1})=1.

Relabel i-1 as j. Again

alpha(x_j,x_{j+1},x_{j+2})=1

for every j.

Thus the physical cycle order is monochromatic and gives a spanning NOR order.

### Consequence

In the square-lift/bubble-sort reduction of root §108, a Hamiltonian synchronized residue can be terminal only for an interior offset

3 <= r <= k-2.

The two boundary offsets r=2 and r=k-1 close the grand conjecture immediately.

This uses actual endpoint full-curvature provenance, not abstract cut geometry. It does not apply when the physical endpoint cycle omits ambient coordinates; Hamiltonicity is essential for the spanning conclusion.
