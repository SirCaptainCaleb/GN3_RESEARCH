# Prescribed endpoint subsets of a permutahedron give contractible outward loci

## Metadata

- ID: prescribed_endpoint_subsets_of_a_permutahedron_give_contractible_outward_loci
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 105
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

## A contractible locus for one varying boundary vertex

Let B be a nonempty finite set, let P(B) be its permutahedron, and let S subset B. Define C_S to be the subcomplex consisting of faces every one of whose chamber orders ends in a vertex of S.

For a face B_1|...|B_t, this condition is exactly B_t subset S: every vertex of the last block can be last in some chamber.

**Lemma.** C_S is empty when S is empty, and is contractible whenever S is nonempty.

**Proof.** If S=B, the locus is the entire convex permutahedron. Suppose emptyset is a proper subset of S and S is a proper subset of B. For every nonempty A subset S, let
\[
F_A=(B-A)|A
\]
be the corresponding facet. Every face whose last block is contained in S lies in F_A for A equal to that last block, and every F_A lies in C_S. Thus C_S is the union of these facets.

Two such facets meet exactly when their suffix sets are comparable by inclusion. More generally a family of them has a nonempty intersection exactly when its suffix sets form a chain; that intersection is a convex face. The finite convex-set nerve lemma identifies the homotopy type of C_S with the order complex of the nonempty subsets A subset S. This poset has a greatest element S, so its order complex is a cone and is contractible. The same holds for C_S. ∎

Reversal gives the identical statement for faces every one of whose chamber orders begins in S.

## Application to one determining window

Suppose a protected source face has one free block B meeting a fixed determining window in exactly one variable vertex position, which is an endpoint of the block. All other determining positions are fixed throughout the face. The occurrence indicator is then a function f:B->{0,1}. Let S={v in B:f(v)=0}.

The subcomplex in which that occurrence is absent in every chamber is C_S or its first-position counterpart, times all neutral permutahedral factors. It is therefore contractible whenever nonempty, regardless of |B|.

This theorem does not identify C_S with a small-rank Coxeter quotient. Its proof uses all suffix-subset facets and their nerve. Thus it accommodates the participation of arbitrarily many vertex labels noted in [[tuple_dependence_does_not_by_itself_give_a_bounded_rank_coxeter_quotient]].

The hypothesis of one variable boundary vertex is essential here. If an indicator depends on an ordered triple from a free three-block, the corresponding locus can consist of three isolated vertices, as in [[separated_window_outward_loci_are_products_and_can_be_disconnected]]. No contractibility assertion for arbitrary ordered-tuple conditions is being made.
