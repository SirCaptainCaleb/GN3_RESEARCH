# One-eighth certificate payment splits into cycle packing or distinct progress outputs

## Statement

Let v be an active misaligned vertex with p=phi(v)>=8 and local defect eta_v. In the lens-free selected switching setup of 614c7d2d181a, let D be the number of doubly occupied interior cells and Y the number of paid occupied interior cells.

Then at least one of the following holds:
(1) D >= p/16-eta_v/2-O(1), and the hypergraph contains D pairwise edge-disjoint linear 3-cycles supported by the doubly occupied cells;
(2) Y >= p/16-eta_v/2-O(1), and there are Y distinct host output edges h_i, one for each paid cell, each satisfying at least one of
    (a) phi(h_i)>p;
    (b) phi(h_i)=p and h_i is special;
    (c) phi(h_i)=p, h_i is nonspecial nonascending, and its forward joint has vertex rank at least p.

In particular, eta_v=o(p) forces either (1/16-o(1))p pairwise edge-disjoint local triangles or (1/16-o(1))p distinct progress-output edges.

## Body

By 614c7d2d181a,
  D+Y >= p/8-eta_v-O(1).
Therefore max{D,Y} >= (D+Y)/2 >= p/16-eta_v/2-O(1).

If D is the larger term, 33be3532211b gives D pairwise edge-disjoint linear 3-cycles, one for each doubly occupied cell.

If Y is the larger term, every paid occupied cell has one of alternatives (a)-(c) by 9a6be27912e0. Distinct occupied cells have distinct standard output edges h_i=g_{i+2}, so the Y paid cells yield Y distinct progress-output edges.

The final asymptotic statement follows immediately when eta_v=o(p).
