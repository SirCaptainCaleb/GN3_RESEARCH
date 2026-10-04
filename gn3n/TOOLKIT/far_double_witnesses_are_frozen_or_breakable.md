# Far symmetric witnesses are frozen or breakable

**Summary:** When reflected local-witness determining windows use disjoint sets of face blocks, absence of a single-sided witness forces both witness indicators to be constant across the entire face.

## Statement

Let F be a permutahedron face and let L,R be indicators of two reflected forbidden-pattern occurrences whose determining windows meet disjoint sets of face blocks. If F contains a chamber with L=R=1 and contains no chamber with exactly one of L,R equal to 1, then L=R=1 for every chamber of F.

## Body

The chamber set of a permutahedron face is the Cartesian product of the permutation sets of its blocks. If the left and right determining windows meet disjoint sets of blocks, then L depends only on one factor set X and R only on a disjoint factor set Y. Assume some chamber has L=R=1. Choose x_0 in X with L(x_0)=1 and y_0 in Y with R(y_0)=1. If L were not identically one, choose x_1 with L(x_1)=0. The product chamber (x_1,y_0) would have (L,R)=(0,1), a forbidden single-sided witness. Hence L is identically one. The same argument shows R is identically one. Thus a far symmetric double witness can avoid the single-sided branch only by being frozen on both sides throughout the face.

## Metadata

- ID: far_double_witnesses_are_frozen_or_breakable
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Limbo
