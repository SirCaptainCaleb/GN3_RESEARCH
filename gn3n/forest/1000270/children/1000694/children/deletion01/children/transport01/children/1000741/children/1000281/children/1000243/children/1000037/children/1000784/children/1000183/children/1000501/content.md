# The perfect-matching shell has only two complementary 2-factor types

## Statement

In the setting of 3a833de66417, the unordered pair of complementary 2-factors {F_e,F_f} of K_6-M has exactly one of the following two forms:

(A) both F_e and F_f are six-cycles;

(B) one factor is the disjoint union of two triangles and the other factor is a six-cycle.

In particular two disjoint-triangle factors cannot occur simultaneously.

## Body

Each F-factor is a simple 2-regular graph on six vertices, so it is either a six-cycle or the disjoint union of two triangles.

Suppose F_e is the disjoint union of two triangles with vertex classes A and B, each of order three. Because F_e is edge-disjoint from the perfect matching M, no matching edge can have both endpoints in A or both in B: every such within-class pair is already an edge of F_e. Hence M is a perfect matching between A and B.

Now K_6-M-F_e consists exactly of the remaining cross edges between A and B, namely K_{3,3}-M. This graph is a six-cycle. But K_6-M-F_e=F_f by 3a833de66417. Therefore whenever one factor is two triangles, the other is a six-cycle.

If neither factor is two triangles, both are six-cycles. These are the only possibilities.
