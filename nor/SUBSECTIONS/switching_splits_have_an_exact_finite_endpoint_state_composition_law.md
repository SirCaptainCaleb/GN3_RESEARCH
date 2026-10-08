# Switching splits have an exact finite endpoint-state composition law

## Metadata

- ID: switching_splits_have_an_exact_finite_endpoint_state_composition_law
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 333
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Switching splits have an exact finite endpoint-state composition law

Use the switching-normalized split of §332:
B -> z -> A -> x,
with every B vertex pointing to every A vertex.

Choose, independently inside B and A, switching representatives and directed Hamiltonian paths
P_B=(b_1,...,b_r),
P_A=(a_1,...,a_s).
Let sigma_B and sigma_A be switching bits relative to the split-normalized representative which realize those induced representatives.

Switching a subset of an induced block or its complement gives the same induced tournament. Hence we may complement all bits of sigma_B, if necessary, so that
sigma_B(b_r)=sigma_A(a_1).

Now extend the block switches to all of V and choose
sigma(z)=sigma_B(b_r)=sigma_A(a_1),
sigma(x)=sigma_A(a_s).

Then the full order
P_B, z, P_A, x
is a directed Hamiltonian path in the resulting global switching representative:
- b_r -> z because the old split has B->z and the endpoint switch bits agree;
- z -> a_1 because the old split has z->A and the switch bits agree;
- a_s -> x because the old split has A->x and those endpoint bits agree.
All internal path edges remain directed by construction.

Define the endpoint switching parities
epsilon_R(B)=sigma_B(b_{r-1}) xor sigma_B(b_r),
epsilon_L(A)=sigma_A(a_1) xor sigma_A(a_2),
epsilon_R(A)=sigma_A(a_{s-1}) xor sigma_A(a_s),
with endpoint clipping for blocks of size below two.

Let c_B,c_A be the internal alpha-words of the two directed paths.

Because alpha on a directed path is the backward distance-two edge bit, the three new boundary statuses are exactly:

1. alpha(b_{r-1},b_r,z)=epsilon_R(B);
2. alpha(b_r,z,a_1)=0;
3. alpha(z,a_1,a_2)=epsilon_L(A);

and the final status adjoining x is
alpha(a_{s-1},a_s,x)=epsilon_R(A).

Therefore the complete alpha-word is
c_B, epsilon_R(B), 0, epsilon_L(A), c_A, epsilon_R(A),
again with the obvious clipping.

Swapping the roles of the shortcut pair gives the companion split
A -> x -> B -> z
and the symmetric composition formula
c_A, epsilon_R(A), 0, epsilon_L(B), c_B, epsilon_R(B).

### Consequence

Recursive gluing across a shortcut-free switching split requires only finite endpoint data from each shore:
- its one-change internal word;
- the switching parity of its first path edge;
- the switching parity of its last path edge.

All higher-dimensional collar information disappears.

Thus the remaining split-composition theorem can be formulated as a finite-state closure problem for directed Hamiltonian NOR paths with two endpoint parity ports. This is a substantially smaller target for a Hartman/Sperner least-unreachable argument.

## Frontier

- Development version when composed: None
- Development version now: 1
