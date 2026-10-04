# Terminal local block bound

**Summary:** A terminal bridging block has size at most the total number of positions it contributes to the two local determining windows.

## Statement

If a terminal carrier block contributes alpha positions to the left determining window and beta positions to the right, and every chamber realizes exactly one of the two local states while both sides occur somewhere, then the block has size at most alpha+beta.

## Body

The left state depends on an ordered alpha-tuple from the block and the right state on an ordered beta-tuple. Compatible tuples are disjoint. If the block had at least alpha+beta+1 vertices, the bipartite disjointness graph on these ordered tuples would be connected. The identity that exactly one side occurs on every compatible pair would then force both state functions to be constant, contradicting occurrence of both sides. Hence the block has size at most alpha+beta.

## Metadata

- ID: terminal_local_block_bound
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Limbo
