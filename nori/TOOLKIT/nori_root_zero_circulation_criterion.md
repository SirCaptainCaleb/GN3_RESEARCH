# Convex zero certificates: directed cycles and oriented-tree cancellation

## Statement

Directed roots: convex zero iff a directed cycle

## Body

# Exact convex cancellation certificates

**Directed-cycle criterion.** Let D be a finite directed graph and label each arc i→j by e_i−e_j. Then 0 lies in the convex hull of the arc labels if and only if D contains a directed cycle. A directed cycle gives a positive equal-weight zero sum. Conversely a convex zero yields nonnegative arc weights of total 1 with inflow equal to outflow at every vertex. Starting with any arc of positive weight and following positive arcs gives a directed cycle in the finite support.

**Oriented-tree cancellation.** Let T be a finite tree. Choose a linearly independent edge basis u_e for its underlying unoriented edges; label orientations of e by ±u_e. In a strictly positive convex combination of such labels summing to zero, every underlying edge occurring in the support must occur in BOTH orientations. Indeed the e-coordinate cancels independently of all others. This is a coordinatewise basis claim, NOT a directed-cycle criterion applied to the tree.

**NORI extraction limit.** Both lemmas are exact algebraic certificates. Applying either to odd cellular-map zeros requires proving that the resulting arc or edge labels correspond to jointly realizable colored physical paths with the requisite root/support memory.

**Consolidation provenance.** Incorporates oriented_tree_balance_pairs_every_used_edge; its original proof is retained in the archived source.

## Metadata

- ID: nori_root_zero_circulation_criterion
- Kind: toolkit
- Version: 3
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted
