# A deletion-critical non-Hamiltonian six-set exists

## Metadata

- ID: a_deletion_critical_non_hamiltonian_six_set_exists
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 283
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

A direct binary feasibility search followed by exhaustive verification gives a genuine six-vertex boundary tournament which is non-Hamiltonian although every vertex deletion is Hamiltonian. This refutes the proposed scale-independent shortcut that every deletion-critical non-Hamiltonian support has order at most five.

Use vertices 0,...,5. Index the 60 independent reversal-pair variables lexicographically by triples (m,u,w) with u<w, u,w distinct from m. Bit 1 means (u,m,w) is tight and bit 0 means its boundary reverse (w,m,u) is tight. The 60-bit orientation word, padded on the left to hexadecimal, is

fc74480c068482c.

Exhaustive verification over all 6!=720 orders finds zero Hamiltonian six-paths. The numbers of Hamiltonian paths in the five-vertex deletions H-v, for v=0,...,5, are respectively

8, 10, 5, 5, 2, 2.

Explicit witnesses are:
H-0: (2,3,5,1,4);
H-1: (2,3,4,0,5);
H-2: (0,1,5,4,3);
H-3: (1,5,2,0,4);
H-4: (1,5,2,0,3);
H-5: (2,4,1,0,3).

Therefore full deletion-criticality of one bad support, even at order six, is not enough to eliminate the odd uniform residue. Any closure of that residue must use its ambient uniform threshold / complementary balanced supports / universal double-noninsertion, not merely the fact that each bad (r+1)-set has all r-deletions Hamiltonian.

## Frontier

- Development version when composed: None
- Development version now: 1
