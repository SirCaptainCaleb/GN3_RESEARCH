# Five-set fence: bare complement witnesses are not closure

## Statement

In a minimum counterexample, every six-set contains at least four Hamiltonian five-sets whose complements are non-Hamiltonian. Therefore bare existence of a Hamiltonian five-set with non-Hamiltonian complement is automatic and cannot by itself exclude a branch or constitute proof compression.

## Body

# Five-set fence

Let H be a minimum counterexample.

Every six-set E contains at least four Hamiltonian five-subsets K by the small-set structure theorem. For each such K, H-K is non-Hamiltonian: otherwise a Hamilton path on K and one on H-K would form a spanning two-cover.

Therefore the bare configuration

- K is Hamiltonian;
- H-K is non-Hamiltonian

is ubiquitous in every minimum counterexample. A disjunction of the form “either such a K exists, or B” gives no information about B.

A five-set conclusion becomes useful only when it retains additional structure that another argument can consume: prescribed labels, a specified Hamilton order, endpoint data, a common insertion gap, or synchronization across several deletion covers.

There is also an important orientation distinction. A **non-Hamiltonian five-vertex exterior set with Hamiltonian complement** is a genuinely restrictive codimension-five configuration. It is not the same assertion as a Hamiltonian five-set with non-Hamiltonian complement.

This is a logical fence, not merely terminology: forgetting the synchronization data can turn a meaningful obstruction into an automatic fact.

## Metadata

- ID: fivefence01
- Kind: toolkit
- Version: 2
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Promoted
