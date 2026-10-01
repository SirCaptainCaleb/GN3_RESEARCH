# Exact saturated-fan normal form at the boundary q=δ

## Statement

In the setting of e5859985e51b, let e={x,y,z} be ascending nonspecial with q=φ(e)=δ, let Q=(g_1,...,g_{q-1}) be a maximum path ending at x and avoiding y,z, let a be the opposite last vertex, and assume Q has no safe single-blocker rotation avoiding y,z. Then the blocker sets of the q-1 edges through a other than g_1 are pairwise disjoint subsets of V(Q)\g_1 of sizes one or two. If S=2, they partition V(Q)\g_1 exactly; the two single blockers occupy exactly two of the three exceptional types {blocker x, contains y, contains z}. If S=3, they cover all but one vertex of V(Q)\g_1, and the three single blockers are exactly one of each exceptional type.

## Body

By e5859985e51b, d_H(a)=q, the number S of single-blocking edges is 2 or 3, the number of double-blocking edges is D=q-1-S, and exactly S-2 vertices of V(Q)\g_1 are unused by blocker incidences. Distinct edges through a have disjoint blocker vertices outside a by linearity, so the blocker sets form pairwise disjoint one- or two-element subsets of V(Q)\g_1. Therefore when S=2 there are no unused blocker vertices and these sets partition V(Q)\g_1; when S=3 exactly one vertex is uncovered.

Every single-blocking edge is exceptional: its unique blocker is x, or it contains y, or it contains z. These three types are mutually exclusive. Indeed an edge through a containing x and y would intersect e in both x and y, impossible by linearity; similarly for x and z, and an edge containing both y and z would intersect e in both y and z. Also by linearity there is at most one single blocker of each type. Hence with S=3 all three types occur exactly once, while with S=2 exactly two of the three types occur.
