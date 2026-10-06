# A non-Hamiltonian four-set obstructs support-contained Gale carriers

## Metadata

- ID: a_non_hamiltonian_four_set_obstructs_support_contained_gale_carriers
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 234
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## A fixed local obstruction to support-contained topological transport

Use the support-pair poset P(H) and the moment-constraint sphere defined in [[hamiltonian_support_pairs_and_smith_chains_give_a_direct_closure_target]].

### A non-Hamiltonian four-set is sufficient

Let the six labels be 1,...,6 with t_i=i. Put A={2,5} and B={1,3,4,6}. Choose H[B] non-Hamiltonian. Such a choice is available from a matching-block edge-ordered K4.

For completeness, its three opposite-edge perfect matchings occur as three consecutive blocks in the edge order, and a triple is tight exactly when its first edge precedes its second edge. In any Hamilton path on four vertices the first and third edges are opposite, hence in the same matching block, whereas the middle edge belongs to a different block. Its rank cannot lie strictly between the first and third ranks. Thus there is no increasing Hamilton path on B.

Every subset of cardinality two or three is nevertheless Hamiltonian. The orientations of triples involving A can be arbitrary; they are irrelevant to the obstruction.

### The source cell is a quadrilateral

In L={sum x_i=sum i x_i=sum i^2 x_i=0}, consider the closed cone with positive coordinates confined to A and negative coordinates confined to B. Its relative interior is nonempty: take
x_2=x_5=1, x_1=x_6=-1/3, x_3=x_4=-2/3.
These coefficients satisfy all three constraints.

A nonzero vector has at least two signs of each kind. Since A has order two, both its coordinates are strictly positive throughout every nonzero face of this cone.

The extreme rays have negative support consisting of one vertex in I={3,4} and one in E={1,6}. Indeed a dependence on four moment-curve points has alternating signs in increasing order; positive positions 2 and 5 require exactly one intervening negative and one exterior negative. Each such pair gives a unique positive ray. There are four rays.

The cone has dimension three and is pointed. Its intersection with the unit sphere is a disk with four sides. The four corners have negative supports {i,e}, i in I, e in E; each side has negative support a three-subset of B. All four sides are nonempty. Thus its barycentric boundary cycle alternates four two-subsets and four three-subsets.

### The canonical boundary cannot be filled without exchanging sides

Map each boundary-face barycenter to its full signed support pair (A,D). All its negative supports D have order two or three, hence are Hamiltonian. This is a legitimate map of the subdivided boundary circle into K(H).

Now restrict possible fillings to pairs (A',B') with A' subseteq A and B' subseteq B, both of order at least two. Necessarily A'=A. The carrier is therefore the order complex of Hamiltonian subsets D of B of order at least two.

Because B is non-Hamiltonian, that poset consists of its six two-subsets and four three-subsets, ordered by inclusion. Its order complex is a graph. The source boundary maps to a simple eight-edge cycle in this graph. That cycle is nonzero in H_1(-;F_2): there are no two-simplices, and the cycle is a nonzero one-chain.

Consequently the canonical boundary map has no continuous disk extension in this support-contained carrier, and its one-cycle has no simplicial two-chain filling there.

### Scope and strategic consequence

This does not show that the loop is unfillable in the full K(H). Mixed pairs, with labels transferred between A and B, were deliberately excluded. Their adequacy is the unresolved transport obligation.

It also does not refute every possible boundary assignment: it refutes the natural full-sign-support assignment on this cell and any filling restricted to its original sides. No minimum-counterexample or small-order cutoff is used. The six-label example isolates a carrier obstruction; it is not a counterexample to two-coverability.

Thus a general realization theorem must allow support exchange, change the boundary assignment coherently, or use a genuinely different algebraic certificate. An arbitrary number of endpoint surgery lemmas confined to the two original supports cannot repair this particular carrier.

The matching-block four-set theorem applies earlier here as a homological obstruction. This gives a precise reason to seek chain fillings using dissimilar support pairs, rather than treating order disagreement or a bounded Hamiltonian support as a terminal result.

## Frontier

- Development version when composed: None
- Development version now: 1
