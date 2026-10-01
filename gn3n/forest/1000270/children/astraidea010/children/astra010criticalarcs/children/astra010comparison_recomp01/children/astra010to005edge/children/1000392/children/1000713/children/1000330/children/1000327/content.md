# Every proper path interval meeting the mandatory triple has non-Hamiltonian complement

## Statement

Let H have a mandatory ordered tight triple T, and let A|B be a spanning two-cover with T consecutive on the displayed path A and |A| minimum. If Y is any nonempty proper contiguous subpath of the displayed path A and V(Y) meets V(T), then the induced subtournament H-V(Y) is non-Hamiltonian. In particular, deleting any one vertex of T leaves a non-Hamiltonian subtournament.

## Body

The contiguous segment Y is itself a tight path. Suppose H-V(Y) were Hamiltonian, with Hamilton path Q. Then Y|Q would be a spanning two-cover.

If Y contains all three vertices of T, then Y contains T consecutively in the inherited order and |Y|<|A| because Y is proper. This contradicts the minimal choice of the T-containing component A.

If Y contains at least one but not all vertices of T, then the vertices of T are split between the two supports V(Y) and V(H)-V(Y). Hence neither component can contain all of T consecutively, contradicting mandatoryness.

Therefore H-V(Y) is non-Hamiltonian for every proper contiguous Y meeting T. Taking Y to be any singleton vertex of T gives the final assertion. ∎
