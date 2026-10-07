# Hamiltonian root circuits are removable by a three-step chord

## Metadata

- ID: hamiltonian_root_circuits_are_removable_by_a_three_step_chord
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 185
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Hamiltonian root circuits are removable by a three-step chord

Work in the pure alternating ternary sector and a minimum-coordinate counterexample.

By §181, after removing proper-support circuit zeros, any essential support-minimal top-cell root zero must be a directed Hamiltonian cycle

C:
x_1 -> x_2 -> ... -> x_n -> x_1,

with roots
rho_i=e_{x_i}-e_{x_{i+1}}
(indices cyclic).

We show that such a Hamiltonian circuit is also removable.

### The Hamiltonian cycle order produces an actual chord root

Consider the full coordinate order

pi_C=(x_1,x_2,...,x_n).

If its ternary word has no 10 occurrence, then the word is of the form 0^r1^s and pi_C is already a spanning NOR-good order. Thus in a counterexample pi_C has some 10 descent.

A 10 descent between the consecutive windows

(x_i,x_{i+1},x_{i+2})
and
(x_{i+1},x_{i+2},x_{i+3})

has actual window-slide root

sigma=e_{x_i}-e_{x_{i+3}}.

For n>=5 this is a chord of the Hamiltonian cycle, not one of its directed edges and not the reverse of one. (For n<=4 the ternary word has at most two windows, so NOR is immediate.)

Hence every hypothetical Hamiltonian essential circuit comes with a genuine actual three-step chord sigma from another chamber of the SAME top permutahedron cell.

### The chord cuts off a proper-support directed circuit

Let

P={rho_i,rho_{i+1},rho_{i+2}}

be the three-edge directed arc from x_i to x_{i+3}. Then

rho_i+rho_{i+1}+rho_{i+2}
=e_{x_i}-e_{x_{i+3}}
=sigma.

Let Q be the complementary directed arc of C from x_{i+3} back to x_i. Then

sigma + sum_{rho in Q} rho =0.

Thus sigma together with Q is a positive directed circuit.

Its endpoint support is

V minus {x_{i+1},x_{i+2}},

so it is a proper subset of V.

By §181, every such proper-support top-cell circuit is locally removable using a genuine transverse actual root.

### Stellar subdivision localizes every remaining zero to the smaller circuit

Now take the circuit simplex Delta_C whose root labels are the n Hamiltonian roots rho_1,...,rho_n and whose relative interior contains zero.

Introduce one interior subdivision vertex labeled by the actual chord sigma and cone it to every facet of Delta_C.

Consider a new cone simplex obtained by omitting one old cycle root rho_k. Its labels are

{sigma} union (C minus {rho_k}).

A nonnegative linear dependence among these labels is exactly a nonnegative circulation in the directed graph formed by the Hamiltonian cycle with edge rho_k deleted and chord sigma added.

There are two cases.

1. rho_k lies on the complementary arc Q.

Then Q is broken. The remaining graph contains the forward three-edge arc P and the chord sigma in the SAME direction from x_i to x_{i+3}, but no directed return path from x_{i+3} to x_i.

Hence the graph is acyclic as far as directed circulation is concerned, and the cone simplex is zero-free.

2. rho_k lies on the short arc P.

Then the only directed cycle in the new graph is

sigma + Q.

The broken P edges cannot carry positive circulation. Therefore every nonnegative zero in this cone simplex lies entirely in the common face

K=conv({sigma} union Q).

So after the stellar subdivision, ALL zeros in the old Hamiltonian circuit simplex have been concentrated onto the single proper-support circuit face K.

### Remove the common proper-support face

The face K is exactly the proper-support directed circuit established above.

Apply the proper-support top-cell removal theorem of §181 to K. This gives a further local refinement, using an actual window-slide root from the same top cell, which removes K without changing the already zero-free boundary of the local star.

Since every zero after the chord subdivision lay in K, the combined refinement removes the original Hamiltonian circuit zero completely.

### Theorem

Every support-minimal Hamiltonian positive circuit of actual ternary window-slide roots in the top permutahedron cell is locally removable.

Therefore the Hamiltonian case isolated in §181 is not essential.

The key point is that the coordinate order following the Hamiltonian cycle itself either:
- is already NOR-good; or
- exposes an actual three-step chord, and that chord compresses the Hamiltonian circuit zero to a proper-support circuit missing exactly the two skipped coordinates.

This uses only actual root labels and stays inside the top-cell carrier.

## Frontier

- Development version when composed: None
- Development version now: 1
