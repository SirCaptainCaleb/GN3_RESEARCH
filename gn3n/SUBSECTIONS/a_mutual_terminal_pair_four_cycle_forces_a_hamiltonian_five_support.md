# A mutual terminal-pair four-cycle forces a Hamiltonian five-support

## Metadata

- ID: a_mutual_terminal_pair_four_cycle_forces_a_hamiltonian_five_support
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 135
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## A terminal-pair four-cycle forces a Hamiltonian five-support

Let a,b,c,d,z be distinct vertices of a boundary tournament. Suppose both orientations of each cycle edge are admissible before z:
\[
h(u,v,z)=h(v,u,z)=1
\]
for uv in {ab,bc,cd,da}.

**Theorem.** The induced boundary tournament on {a,b,c,d,z} has a Hamilton tight path.

**Proof.** Suppose it is non-Hamiltonian. By the non-Hamiltonian-five-set theorem in smallset01, it has an edge-order representation. Choose the least of the four ordinary cycle edges. Relabel cyclically so that this edge is ab. Then ab<bc and ab<ad, whence
\[
h(a,b,c)=h(b,a,d)=1.
\]
The cycle admissibility conditions also give
\[
h(b,c,z)=h(a,d,z)=1.
\]
Exactly one of h(c,z,d), h(d,z,c) is 1 by boundary antisymmetry. In the first case (a,b,c,z,d) is tight; in the second case (b,a,d,z,c) is tight. Either is a Hamilton five-path, contradiction. ∎

The conclusion needs a cycle, not necessarily an induced cycle; extra mutual edges do not invalidate the proof. The proof uses edge-orderability only under the assumption of non-Hamiltonicity. It does not assert that an arbitrary boundary tournament is edge-orderable.

## Application to the Article VII carrier loop

When terminal-pair admissibility is h(u,v,z)=1, a chordless four-label cycle in the mutual-pair graph forces the Hamiltonian five-support consisting of its four labels and the fixed following vertex z.

Thus the finite topological obstruction itself exposes an actual Hamiltonian five-support. This links the carrier-loop interface to the five-component interface in the compressed Article VII, without first finding exterior labels.

A Hamilton five-support does not by itself fill the loop or concatenate to a corridor tail. Its tight order may move z and alter the inward boundary statuses. The new theorem supplies a genuine common combinatorial object for the two interfaces; protectedness and tail attachment remain separate obligations.
