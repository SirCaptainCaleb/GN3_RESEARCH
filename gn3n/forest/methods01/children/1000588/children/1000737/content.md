# Norine antipodal-coloring toolkit

## Statement

Norine's conjecture is now a theorem: every antipodal red--blue edge-coloring of Q_n, n>=2, has a monochromatic path joining a vertex to its antipode. For LINP the reusable pieces are the component-to-rook-labeling reduction, low-dimensional square/cube forcing, and the general antipodal obstruction.

## Body

Main theorem source: Hehui Wu and Ningyuan Yang, "A Chain-Level Borsuk--Ulam Obstruction Proof of Norine''s Antipodal-Coloring Conjecture", arXiv:2607.19276 (2026), https://arxiv.org/abs/2607.19276.

The 2026 proof is technically heavy. This branch deliberately separates its clean combinatorial front end from the chain-level machinery. The clean reduction is imported in a child node. The full general proof is summarized rather than recopied: a hypothetical counterexample gives a rook labeling; labels (a,b) are represented by roots e_a-e_b, with antipodal swap corresponding to negation. Freudenthal subdivision turns cubical faces into sums of monotone simplices, whose labels form rook galleries. Independent root sets are sent to spherical sections of their positive cones, dependent sets to zero. A mod-2 cancellation identity makes this into an equivariant, augmentation-preserving chain map to a sphere-like chain complex one dimension lower. An algebraic Borsuk--Ulam obstruction forbids such a map.

Why not copy the full proof? The radial polyhedral-chain construction, subdivision invariance, gallery rank bound, and norm-operator kernel=image verification are tightly interdependent and much less reusable than the reduction they serve. The linked paper is the right canonical source for those details.

Earlier cube work is retained separately because it exposes local forcing patterns that may transfer more directly to LINP than the final proof does.
