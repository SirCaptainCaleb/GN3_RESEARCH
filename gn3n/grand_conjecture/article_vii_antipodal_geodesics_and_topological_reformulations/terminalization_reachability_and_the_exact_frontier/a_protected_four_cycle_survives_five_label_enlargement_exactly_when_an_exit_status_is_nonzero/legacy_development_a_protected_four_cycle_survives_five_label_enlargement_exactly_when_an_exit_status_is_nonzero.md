# A protected four-cycle survives five-label enlargement exactly when an exit status is nonzero — preserved pre-item development

## Composition

(none yet)

## Development

## Exact five-label obstruction for the protected four-cycle

Let B={a,b,c,d}, with mutual terminal-pair graph the chordless cycle a-b-c-d-a before a fixed label z. Thus h(u,v,z)=h(v,u,z)=1 exactly on mutual cycle edges; a diagonal may have a one-way admissibility relation, but is not mutual.

Let T=B union {z}. Give each w in T an exit value delta(w) in {0,1}, with delta(z)=1. In the permutahedron P(T), call a chamber (t_1,...,t_5) outward exactly when
delta(t_5)=0 or h(t_3,t_4,t_5)=1.
Let D be the subcomplex of faces all of whose chamber vertices are outward. Let F be the facet ending in z, and D_0=D intersect F. The terminal-pair classification gives D_0 homotopy equivalent to a circle.

This is precisely the five-label enlargement in the separated positive-word model: delta(w)=h(w,z_1,z_2), all statuses farther into the fixed suffix are zero, and the selected word is h(t_3,t_4,t_5), h(t_4,t_5,z_1), delta(t_5). The enlarged face is protected for every choice of delta.

**Theorem.**
1. If delta(a)=delta(b)=delta(c)=delta(d)=0, D is contractible.
2. If at least one of these four values is one, the inclusion D_0 -> D induces a split injection on integral first homology. In particular the old circle is not null-homotopic anywhere in the whole five-label outward locus.

**Proof of (1).** Apply [[one_exception_endpoint_enlargements_have_contractible_outward_loci]] with exceptional label z.

**Proof of (2).** Relabel the cycle so that delta(a)=1, and use its edge ab. Define an integer cellular 1-cochain omega on D as follows. It is supported on the two edges
(c,d,a,b,z) -- (c,d,b,a,z),
(d,c,a,b,z) -- (d,c,b,a,z).
These edges exist because ab is mutual. Give a supported directed edge value +1 when its fourth label changes from a to b, value -1 in the reverse direction, and zero to every other edge.

We show omega is a cocycle by checking every possible two-dimensional face incident with a supported edge. Permutahedral two-faces are squares from two disjoint adjacent swaps, or hexagons from two neighboring adjacent swaps.

A supported edge swaps positions 3 and 4. The only disjoint swap is positions 1 and 2. In that square the two supported edges have opposite boundary contributions, so their sum is zero.

A hexagon on positions 2,3,4 would permute three labels from B while keeping final label z fixed. If the whole hexagon belonged to D, every ordered pair of those three labels would be admissible before z. They would form a mutual triangle containing ab, impossible in a chordless four-cycle.

A hexagon on positions 3,4,5 would permute {a,b,z}. It contains a chamber with suffix (z,b,a). But
h(z,b,a)=1-h(a,b,z)=0
and delta(a)=1. This chamber is not outward, so this hexagon does not belong to D.

There are no other incident two-face types. Thus omega vanishes on every cellular two-boundary and defines a homomorphism H_1(D;Z) -> Z.

For completeness, the following closed edge path lies in D_0; each successive step is an adjacent swap:
abcdz,
bacdz,
bcadz,
cbadz,
cbdaz,
cdbaz,
dcbaz,
dcabz,
dacbz,
adcbz,
adbcz,
abdcz,
abcdz.
Every displayed terminal pair before z is a cycle edge. This loop traverses exactly one supported edge, from dcbaz to dcabz, with value +1. Under the terminal-pair nerve equivalence its changing terminal labels travel once around a-b-c-d-a, up to the choice of starting point. It therefore represents a generator of H_1(D_0;Z)=Z, and omega evaluates to one on its image in D.

The homomorphism induced by omega is a left inverse to the inclusion on this generator. The inclusion is therefore split injective. QED.

### Consequence for the remaining carrier cases

For the chordless four-label carrier loop, moving only the following label z fills the old loop if and only if all four reservoir exit values are zero. Even one nonzero exit value preserves an infinite-order homology class.

This is stronger than the earlier obstruction to merging each old outward face into a whole outward face. It excludes every continuous filling inside the full five-label outward locus, regardless of the unspecified internal triples or the triples with middle label z.

Hence a repair in these remaining cases must leave this five-label face: for example by enlarging the movable label set further or changing the fixed boundary data. A Hamiltonian five-support on the same labels, supplied by [[a_mutual_terminal_pair_four_cycle_forces_a_hamiltonian_five_support]], does not remove this obstruction.

This is an obstruction to a specified local protected carrier, not a counterexample to the grand conjecture. The initial finite diagnostic suggested the cocycle; the theorem above is a direct proof for every compatible boundary tournament and does not rely on enumeration.
