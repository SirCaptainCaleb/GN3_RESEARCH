# Two-deletion reconstruction for partitions into linearly ordered blocks

**Summary:** Two-deletion reconstruction for partitions into linearly ordered blocks

## Statement

Let W be a finite set, and let R and S be two distinct structures on W, each consisting of a partition of W into blocks together with a linear order on every block. For an unordered pair {u,v}, its pair state records either that u,v lie in different blocks, or, if they lie in one block, which of u,v precedes the other. Let
Z={x in W : the restrictions of R and S to W-{x} have identical pair states}.
Then |Z|<=2. Moreover, if Z contains two distinct vertices x,y, then R and S have identical pair states on every unordered pair except possibly {x,y}; since R and S are distinct, in that case {x,y} is their unique disagreeing pair.

## Body

Because R and S are distinct, some unordered pair {u,v} has different pair state in the two structures.

If x is any vertex outside {u,v}, then the pair {u,v} survives in W-{x} with its pair state unchanged in each restriction. Hence the two restrictions to W-{x} still disagree. Therefore every x in Z belongs to {u,v}, proving |Z|<=2.

Now suppose Z contains two distinct vertices x,y. Let {a,b} be any unordered pair different from {x,y}. At least one of x,y is not in {a,b}; call that vertex z. Since z belongs to Z, the restrictions of R and S to W-{z} have identical pair states. The pair {a,b} survives that restriction, so R and S give it the same pair state.

Thus every pair except possibly {x,y} has the same state in R and S. Since R and S are distinct, {x,y} must indeed be their unique disagreeing pair. ∎

## Metadata

- ID: pairdeletionreconstruct01
- Kind: toolkit
- Version: 2
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Promoted
