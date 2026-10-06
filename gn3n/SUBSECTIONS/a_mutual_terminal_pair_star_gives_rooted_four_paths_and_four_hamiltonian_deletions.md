# A mutual terminal-pair star gives rooted four-paths and four Hamiltonian deletions

## Metadata

- ID: a_mutual_terminal_pair_star_gives_rooted_four_paths_and_four_hamiltonian_deletions
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 160
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Rooted four-paths supplied by a mutual terminal-pair star

Let v,r,s,z be distinct vertices of a boundary tournament. Suppose
h(v,r,z)=h(v,s,z)=1.

**Lemma.** Exactly one of
(v,r,z,s), (v,s,z,r)
is a tight path, according as h(r,z,s) is one or zero. In either case the Hamiltonian four-path starts at v and has z in its penultimate position.

**Proof.** The first required triple of each displayed path is prescribed tight. Their second triples are (r,z,s) and (s,z,r), which are boundary flips, so exactly one is tight. No cyclic rotation or path reversal is used. QED.

### The four-cycle supplies four Hamiltonian deletions with prescribed initial vertices

Let B={a,b,c,d} have the mutual cycle a-b-c-d-a before z. Put S=B union {z}. Define
t=h(b,z,d),  e=h(a,z,c).

Each cycle-label deletion is Hamiltonian, with the following explicit rooted order:
- S-a: (c,b,z,d) if t=1; (c,d,z,b) if t=0.
- S-c: (a,b,z,d) if t=1; (a,d,z,b) if t=0.
- S-b: (d,a,z,c) if e=1; (d,c,z,a) if e=0.
- S-d: (b,a,z,c) if e=1; (b,c,z,a) if e=0.

Thus deleting a cycle vertex leaves a Hamiltonian four-path starting at its opposite vertex. The orders for deletions a and c share the same ordered terminal pair, either (z,d) or (z,b). The orders for deletions b and d share another ordered terminal pair, either (z,c) or (z,a).

Only the two independent statuses t,e are needed to determine all four orders. Internal triples entirely in B play no role.

This strengthens the attachment information supplied by [[a_mutual_terminal_pair_four_cycle_forces_a_hamiltonian_five_support]]. The five-support S is Hamiltonian by that theorem, but here its four cycle-label deletions come with explicit usable orientations. In particular they do not merely expose an unspecified endpoint of a Hamilton path.

### Orientation limitation

The lemma prescribes an initial vertex, not a terminal one. Reversing any displayed tight order would reverse all of its triple statuses and is not permitted.

Nor must deleting z leave B Hamiltonian: the triple orientations inside B are independent of the displayed mutual-pair prescriptions and may be chosen to realize a non-Hamiltonian four-set. Thus all four cycle-label deletions are available, but a fifth Hamiltonian deletion at z is not asserted.
