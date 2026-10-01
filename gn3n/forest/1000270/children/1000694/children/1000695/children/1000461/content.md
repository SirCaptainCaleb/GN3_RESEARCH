# Deletion-cover cocycle

## Statement

For a hypothetical minimum counterexample choose, for every vertex x, a two-path cover C_x of H-x. Conjecture that the family {C_x} cannot be globally pairwise incompatible: there exist distinct x,y such that the restrictions of C_x and C_y to H-{x,y} admit a common two-path refinement whose two inherited orders differ only on one contiguous block, and that block can be switched to absorb both omitted vertices and yield a spanning two-cover. View incompatibilities between deletion covers as signed transitions and seek a cocycle identity around triples of deleted vertices.

## Body

Why it might matter globally:
Minimum-counterexample calculus supplies a huge coherent family of deletion covers for free. A global consistency law on that family could force a spanning cover without privileging a longest path, a small residue, or one local endpoint configuration.

Plausible first attack:
Fix x,y,z and restrict chosen covers C_x,C_y,C_z to H-{x,y,z}. Encode for each surviving ordered vertex pair whether the two relevant path orders agree, disagree, or separate the vertices into different components. Derive the algebraic identities forced when passing x->y->z->x. Look for a parity or transitivity consequence implying one pair of deletion covers has a single localized disagreement block rather than dispersed incompatibility.