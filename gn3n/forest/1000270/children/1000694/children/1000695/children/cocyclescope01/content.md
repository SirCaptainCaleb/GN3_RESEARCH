# The cocycle route needs an intermediate datum between support and full pair-state compatibility

## Statement

The deletion-cover cocycle brainstorm d4525c46b080 already has its two endpoint cases understood. If the proposed globally consistent local datum determines the full ordered pair state of every common vertex pair, then four deletion covers glue to a spanning two-cover by the certified compatibility theorem. If it determines only same-support relations, then a support-compatible family localizes to one critical support class but need not close. Therefore the brainstorm has new theorem content only if one defines an intermediate transport datum that is strictly weaker than full pair-state compatibility yet strong enough that trivial transport around deletion cycles forces full pair-state consistency. The currently suggested unordered endpoint-pair data do not by themselves meet either certified gluing threshold.

## Body

# Proof / route reduction

For a deletion cover F_d, the certified compatibility theory records, for every ordered pair of common vertices, one of three pair states:

- same path with the first preceding the second;
- same path with the reverse precedence;
- different paths.

Suppose a family of at least four deletion covers has globally consistent data strong enough to determine these pair states independently of the deletion label. Then the compatible-cover gluing theorem in d43a7c9e2f61 applies directly and produces a spanning cover by at most two tight paths. Thus the full-pair-state version of the proposed cocycle theorem is already established.

At the opposite level, suppose only the same-path/different-path relation is consistent. The support-compatible-family theorem in d43a7c9e2f61 then gives exactly the known localization: all deletion labels lie in one critical support class X, the complementary class Q is Hamiltonian and fixed, and every H[X-{d}] is Hamiltonian. Relative orders on X-{d} may still disagree. Therefore support consistency alone is not a gluing theorem.

The proposed unordered pair of path endpoint-pairs is weaker still: it records four boundary vertices but does not directly assign a same-support relation or a precedence state to arbitrary internal common vertices. Hence no existing gluing theorem can be invoked from endpoint data alone.

Consequently the cocycle route reduces to one precise missing definition/theorem. One needs a transport datum T(F_x,F_y) satisfying all three properties:

1. it is computable from substantially less than the full pair-state table;
2. trivial transport around deletion cycles can be forced from boundary-tournament structure; and
3. global triviality of T reconstructs enough pair-state information to reach full compatibility and hence the existing gluing theorem.

Without such an intermediate reconstruction theorem, endpoint consistency is only an organizational metaphor rather than a distinct closure mechanism.

This does not refute the cocycle idea; it identifies exactly where its genuinely new mathematics must lie.
