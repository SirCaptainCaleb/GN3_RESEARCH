# Minimum-hole synchronization

## Metadata

- ID: topological_recurrence_to_local_gn3_structure_subsection_d
- Parent Section: topological_recurrence_to_local_gn3_structure
- Position: 4
- Row version: 6
- Development version: 6
- Composition version: 1
- Composition stale: False

## Cold composition

Minimum deletion holes synchronize all omitted vertices as common reversers of the same two terminal edges; proof to follow.

Proof. Because X has minimum cardinality, H-X cannot be Hamiltonian: otherwise adding any one x in X as a singleton would two-cover H-(X minus {x}). Likewise neither P nor Q can have order at most two, because adjoining x to such a component produces a Hamiltonian set of order at most three and again yields a two-cover after deleting only X minus {x}. Hence both displayed paths have order at least three.

Fix x in X and put J=H-(X minus {x}). By minimality of X, pc(J)>2, while J-x=P|Q. Consider the order obtained by writing P, then x, then Q in reverse. All statuses internal to P are tight and all statuses internal to the reversed Q are non-tight. If r=|P|, the first non-tight status is no earlier than r-1 and the last tight status is no later than r+1. Therefore its exact deficiency is at most one. Since J has no two-cover, the inversion-window criterion forces the deficiency to be at least one. Equality follows.

Equality pins the first and last junction positions. Therefore every x in X reverses both terminal edges, as claimed. This completes the proof.

For each x in X, the middle triple on the two exposed endpoints has exactly one tight orientation. Combining it with the two reversal triples gives a Hamiltonian four-support through x. Removing that four-support and then deleting X without x leaves prefixes of P and Q as a two-cover. Hence the two-cover deletion distance of the complement drops by at least one.

## Development

Minimum deletion holes synchronize all omitted vertices as common reversers of the same two terminal edges; proof to follow.

Proof. Because X has minimum cardinality, H-X cannot be Hamiltonian: otherwise adding any one x in X as a singleton would two-cover H-(X minus {x}). Likewise neither P nor Q can have order at most two, because adjoining x to such a component produces a Hamiltonian set of order at most three and again yields a two-cover after deleting only X minus {x}. Hence both displayed paths have order at least three.

Fix x in X and put J=H-(X minus {x}). By minimality of X, pc(J)>2, while J-x=P|Q. Consider the order obtained by writing P, then x, then Q in reverse. All statuses internal to P are tight and all statuses internal to the reversed Q are non-tight. If r=|P|, the first non-tight status is no earlier than r-1 and the last tight status is no later than r+1. Therefore its exact deficiency is at most one. Since J has no two-cover, the inversion-window criterion forces the deficiency to be at least one. Equality follows.

Equality pins the first and last junction positions. Therefore every x in X reverses both terminal edges, as claimed. This completes the proof.

For each x in X, the middle triple on the two exposed endpoints has exactly one tight orientation. Combining it with the two reversal triples gives a Hamiltonian four-support through x. Removing that four-support and then deleting X without x leaves prefixes of P and Q as a two-cover. Hence the two-cover deletion distance of the complement drops by at least one.
