# Oriented-tree balance pairs every used edge

**Summary:** Positive balance of oriented tree-edge labels forces both orientations of every used tree edge.

## Statement

Orient the edges of a fixed tree and represent each orientation by its signed edge-incidence basis vector. In any strictly positive convex combination summing to zero, every tree edge occurring in the support occurs in both orientations.

## Body


Let \(T\) be a finite tree. Choose one basis vector \(u_e\) for each unoriented edge \(e\). Label the two orientations of \(e\) by \(+u_e\) and \(-u_e\).

Suppose
\[
\sum_{x\in C}\lambda_x\,\ell(x)=0,
\qquad
\lambda_x>0,
\]
where every \(\ell(x)\) is an oriented edge label of \(T\).

The vectors \(u_e\) are linearly independent. Therefore cancellation occurs separately in every edge coordinate. If \(+u_e\) occurs but \(-u_e\) does not, the \(e\)-coordinate of the sum is strictly positive; similarly in the opposite direction.

Hence every tree edge represented among the labels occurs in both orientations.

Combined with an odd cellular map whose chamber labels are oriented edges of a fixed tree, this converts a positive zero carrier into paired local witnesses edge by edge.


## Metadata

- ID: oriented_tree_balance_pairs_every_used_edge
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
