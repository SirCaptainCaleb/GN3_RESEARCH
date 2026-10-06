# A mutual four-cycle with Hamiltonian complement already gives a spanning two-cover

## Metadata

- ID: a_mutual_four_cycle_with_hamiltonian_complement_already_gives_a_spanning_two_cover
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 156
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## A mutual four-cycle with Hamiltonian complement already gives a spanning two-cover

Let H be any finite boundary tournament. Let B={a,b,c,d} and z be five distinct vertices. Suppose the mutual terminal-pair graph before z contains the cycle a-b-c-d-a:
h(u,v,z)=h(v,u,z)=1
for uv in {ab,bc,cd,da}.
The cycle need not be induced.

**Theorem.** If the induced tournament on V(H) minus (B union {z}) is Hamiltonian or empty, H has a spanning two-cover.

**Proof.** By [[a_mutual_terminal_pair_four_cycle_forces_a_hamiltonian_five_support]], H[B union {z}] has a Hamiltonian tight path. Use that path as one covering component and a Hamiltonian path of the complement as the other, omitting it when the complement is empty. Their supports partition V(H). QED.

### Exclusion in the no-two-cover branch

If H has no spanning two-cover, the complement of every such five-support must be non-Hamiltonian. This applies before any exit-status test or topological filling argument.

In particular consider the one-sided separated-window realization used in
[[arbitrary_terminal_pair_relations_occur_on_protected_zero_faces]]
and in the five-label enlargement results. Its four-label block B occupies the first four positions, followed by z,z_1,z_2,... . Every consecutive suffix triple starting with (z_1,z_2,z_3) has status zero. The entire complement of B union {z} is therefore a tight path in reverse order, since boundary antisymmetry turns each of those zero statuses into one.

Hence the four-cycle realization already gives a spanning two-cover of the full ambient tournament, whatever the exit values h(u,z_1,z_2) are. It cannot occur as a global no-two-cover obstruction in precisely that one-sided geometry.

This does not invalidate the local carrier obstructions: they remain genuine examples showing that local protectedness alone does not force a filling. It does show that the global no-two-cover hypothesis excludes this particular modeled sector without constructing any filling.

### Earlier placement in separator analysis

Let a pair reservoir have at most four labels before a fixed z, with a Hamiltonian complement to the five-label support whenever all four labels are used. In a no-two-cover tournament its mutual graph has no four-cycle. The terminal-pair classification then makes every nonempty connected component of its pair locus contractible: for at most four labels the sole noncontractible connected clique-complex type is a chordless four-cycle.

Thus in this sector there is no loop obstruction. Disconnected terminal-label sectors can still obstruct a natural carrier, and must be treated separately. If the pair relation is connected, its natural locus is already contractible.

The surviving global carrier-loop problem must therefore have a non-Hamiltonian complement to its Hamiltonian five-packet. In a positional model this can come from additional outer blocks, a second determining window, or different fixed boundary data. The remaining global forcing argument must account for that complement rather than trying to force exterior labels in the excluded one-sided model.

## Frontier

- Development version when composed: None
- Development version now: 1
