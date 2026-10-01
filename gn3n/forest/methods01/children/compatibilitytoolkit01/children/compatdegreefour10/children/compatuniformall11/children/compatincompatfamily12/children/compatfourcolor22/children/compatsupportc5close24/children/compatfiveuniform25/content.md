# Five pairwise incompatible deletion covers force a uniform triple

## Statement

Let F_1,...,F_5 be deletion covers associated with five distinct labels in a boundary tournament H with at least one vertex outside those labels. If the five covers are pairwise incompatible, then some three of them have all three pairwise incompatibilities of the same broad type: either all three pairs are support-incompatible, or all three pairs are support-compatible but order-incompatible.

## Body

# Proof

Color each edge of K_5 red when the corresponding pair of covers is support-incompatible and blue when it is support-compatible but order-incompatible.

Suppose there is no monochromatic triangle. We first recall the elementary structure of a triangle-free two-coloring of K_5. At any vertex v, three incident edges cannot have the same color, since among their three opposite endpoints an edge of that same color would make a monochromatic triangle, while if all three opposite edges had the other color they would themselves contain a monochromatic triangle. Thus every vertex has red degree two and blue degree two. Hence each color class is a 2-regular graph on five vertices, so each is a 5-cycle.

In particular the blue edges form a 5-cycle of support-compatible pairs. By compatsupportc5close24, those five cyclic support compatibilities force all five covers to be pairwise support-compatible. Thus every edge is blue, contradicting the assumption that the blue graph is only a 5-cycle and, more directly, producing many blue triangles.

Therefore a monochromatic triangle exists. Red gives three pairwise support-incompatible covers; blue gives three pairwise support-compatible but order-incompatible covers.