# Terminal local witness blocks have at most four vertices

**Summary:** In a disjoint-window terminal local-witness configuration, the bridging block contributes at most two positions to each determining window and therefore has order at most four.

## Statement

Assume a terminal single-sided configuration with disjoint left and right determining windows. Let alpha,beta be the numbers of positions of the bridging face block B in those windows. Then |B|=alpha+beta and alpha,beta<=2; hence |B|<=4.

## Body

By [[terminal_local_block_bound]], |B|<=alpha+beta. A chamber simultaneously fills alpha left-window positions and beta right-window positions with distinct vertices of B, so |B|>=alpha+beta; hence equality. Fix the outside block orders and fix a partition of B into the alpha vertices used on the left and the beta used on the right. Orders of those two sets vary independently. Terminality says exactly one of the two reflected witness states occurs for every pair of orders. Therefore, for this fixed support partition, the left witness indicator is constant over all orders of the alpha-set and the right indicator is constant over all orders of the beta-set. Both values occur for suitable support partitions because the carrier contains both witness orientations. Suppose a support with left witness value one had alpha>=3. Since B crosses the central side of the left determining window, its alpha positions form the inward suffix of that window; the final three positions form one whole consecutive triple whose status is prescribed by the forbidden pattern. Swap the first and third vertices of that triple. This preserves the support partition and all face constraints, but boundary antisymmetry flips that required status, so the same witness cannot remain present. Contradiction. Thus alpha<=2 whenever the left state occurs; applying the same argument to a right-state support gives beta<=2. Since both orientations occur, alpha,beta<=2 globally and |B|<=4.

## Metadata

- ID: terminal_local_block_sharpens_to_four
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: passed
- Refutation: unrefuted
- Toolkit status: Limbo
