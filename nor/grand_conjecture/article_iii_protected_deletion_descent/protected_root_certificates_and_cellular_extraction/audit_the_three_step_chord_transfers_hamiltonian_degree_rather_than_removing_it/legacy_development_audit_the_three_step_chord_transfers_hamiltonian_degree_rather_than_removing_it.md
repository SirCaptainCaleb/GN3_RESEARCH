# Audit: the three-step chord transfers Hamiltonian degree rather than removing it — preserved pre-item development

## Audit: the three-step chord transfers Hamiltonian degree; it does not remove it

This corrects §185 in light of the local-degree audit §184.

The three-step chord construction in §185 is valid through the following point.

For a Hamiltonian directed root circuit
C=(rho_1,...,rho_n)
and a 10 descent in the Hamiltonian coordinate order, the actual chord
sigma=e_{x_i}-e_{x_{i+3}}
forms a proper-support directed circuit with the complementary Hamiltonian arc, missing x_{i+1},x_{i+2}.

A stellar subdivision using sigma indeed concentrates one branch of the zero set onto that smaller circuit.

However the conclusion that the Hamiltonian circuit simplex can then be made zero-free relative to its original boundary is false.

The Hamiltonian root simplex is full-dimensional in W and contains 0 in its interior with nonzero local degree. Any modification fixing its boundary must retain total zero index plus or minus one. Removing the proper-support chord circuit merely transfers that index to another zero in the subdivided star.

Therefore §185 must NOT be used as a topological elimination theorem.

What survives and is useful is the combinatorial compression:

- every bad Hamiltonian cycle order exposes an actual three-step chord;
- that chord canonically selects the codimension-two subset
  V minus {x_{i+1},x_{i+2}};
- the complementary arc is a proper-support directed root circuit on that subset.

By minimum-counterexamplehood, that codimension-two subset has a spanning one-change order.

Hence the correct next use of the chord is not local degree cancellation. It is a two-vertex reinsertion problem for the skipped coordinates x_{i+1},x_{i+2}.

This interfaces directly with the codimension-two scan/pair-insertion theory §§157-161.
