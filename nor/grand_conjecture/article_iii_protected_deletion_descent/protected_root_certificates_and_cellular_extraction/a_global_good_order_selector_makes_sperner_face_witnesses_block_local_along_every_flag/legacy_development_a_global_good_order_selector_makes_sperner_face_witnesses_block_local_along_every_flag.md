# A global good-order selector makes Sperner face witnesses block-local along every flag — preserved pre-item development

## A global good-order selector makes Sperner face witnesses block-local along every flag

Work in a minimum counterexample. Every proper nonempty coordinate subset S is a smaller instance and therefore has a NOR-good spanning order. Fix once and for all one such order

g(S)

for every proper nonempty S.

For every proper ordered-partition face

F=B_1|...|B_s

of the permutahedron, define its canonical block-good witness

pi_F = g(B_1) g(B_2) ... g(B_s).

Because every block is proper, each factor has at most one internal ternary status change. The ambient full order pi_F is bad, so the consecutive-change construction of roots §§155-156 supplies at least one isolated-band macro root crossing F-blocks.

### Codimension-one compatibility

Let F' be a codimension-one subface of F. Equivalently one block B of F is split into two consecutive blocks A|C in F', while every other block is unchanged.

Then

pi_F  = P · g(B) · Q,
pi_F' = P · g(A) g(C) · Q,

for exactly the same outside prefix P and suffix Q.

Hence the two canonical witness orders are identical outside the physical coordinate set B=A union C.

All ternary windows disjoint from B and from the two boundary layers adjacent to B are literally unchanged. Any discrepancy between the two face witnesses is confined to the proper subinstance on B together with the bounded splice windows at its two ends.

### General flags

For a barycentric flag

F_0 < F_1 < ... < F_k,

each step merges consecutive blocks. Therefore the canonical witness sequence changes one merged proper block at a time.

Thus the witnessed Sperner carrier can be chosen so that every face-to-face incompatibility is FIBERED: it lies inside one proper coordinate block, with the ambient outside order fixed.

### Consequence for extraction

The closing zero/path of root §156 no longer needs to compare arbitrary independently chosen full witness orders. With this global selector, consecutive face labels in its supporting flag differ only by replacing

g(A)g(C)

with

g(A union C)

inside one proper block.

Since A union C is itself a smaller NOR instance, both the existence of g(A union C) and all local Article III repair theorems may be applied while treating the outside order as frozen boundary data.

Therefore a closure proof may proceed by induction on the size of the active merged block:

- if the selected isolated-band label is unchanged by the merge, pass through the face step with no new gluing;
- if it changes, the first discrepancy is supported in the merged proper block plus its bounded two-sided splice packet;
- any genuinely global obstruction must therefore arise from repeated failure to glue these block-local replacements at their boundary windows, not from uncontrolled reordering of the whole carrier.

This strengthens the witnessed Sperner construction from a nested-face certificate to a nested sequence of proper-subinstance replacement cells. It does not yet prove that each replacement cell has a boundary-safe splice.
