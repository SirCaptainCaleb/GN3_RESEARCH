# A rooted five-side has a root-preserving common endpoint core or a two-pair root-exchange split

**Summary:** For a rooted Hamiltonian five-set with two bad endpoint extensions, either one common endpoint replacement preserves the root, or the root is the unique common removable label and the other four labels split into two endpoint-specific pairs.

## Statement

Let X be a Hamiltonian five-set with distinguished root x, and let a,b be vertices outside X such that X∪{a} and X∪{b} are non-Hamiltonian. For u∈{a,b}, let G_u={t∈X:(X-{t})∪{u} is Hamiltonian}. Then |G_a|,|G_b|≥3. Hence either some t≠x belongs to G_a∩G_b, giving a common Hamiltonian endpoint-replacement core that still contains x, or G_a∩G_b={x}, x∈G_a∩G_b, and the four non-root vertices split into two disjoint pairs G_a-{x} and G_b-{x}.

## Body

Let X be a Hamiltonian set of order five, let x in X be distinguished, and let a,b be vertices outside X. Assume X union {a} and X union {b} are both non-Hamiltonian.

For u in {a,b}, define
G_u={t in X : (X-{t}) union {u} is Hamiltonian}.

Consider the non-Hamiltonian six-set X union {u}. By the four-of-six theorem, at least four of its five-vertex deletions are Hamiltonian. Deleting u leaves X, which is Hamiltonian. Therefore at least three deletions by vertices t in X are Hamiltonian, and hence
|G_u|>=3.

If there is t in (G_a intersect G_b)-{x}, then both
(X-{t}) union {a}
and
(X-{t}) union {b}
are Hamiltonian and their common four-vertex core X-{t} still contains the distinguished root x. This is the root-preserving alternative.

Assume no such non-root t exists. Then
(G_a-{x}) intersect (G_b-{x})=emptyset.
Since X-{x} has four vertices, the lower bounds |G_a|,|G_b|>=3 force x to belong to both G_a and G_b: otherwise one of G_a-{x},G_b-{x} would have size at least three while the other has size at least two, impossible for disjoint subsets of a four-set.

Thus each of G_a-{x} and G_b-{x} has size at least two. They are disjoint subsets of the four-set X-{x}, so each has size exactly two and together they partition X-{x}. Consequently
G_a intersect G_b={x},
G_a={x} union A,
G_b={x} union B,
where A,B are disjoint two-sets with A union B=X-{x}.

Hence failure of a root-preserving common endpoint core has a unique form: the root x is the unique common removable label, and the remaining four labels split into two endpoint-specific exchange pairs.

## Metadata

- ID: toolkit_common_endpoint_core_or_a_two_pair_root_exchange_split
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
