# The selected-terminal cycle-neighbor rail cannot pierce a certificate-anchor lens

## Statement

Retain residual case (4) of d0a41dede20a for a selected strict-gap chord
  e={x,v,u}
with source rail R_e and selected certificate anchor precursor A at terminal v. Let f be the fundamental-cycle neighbor of e that shares terminal v, and let R_f be a canonical source rail of f.

Then R_f intersects both R_e and A.

Consequently at least one of the following holds:

(i) |V(R_f) intersect V(R_e)|>=2;
(ii) |V(R_f) intersect V(A)|>=2;
(iii) both intersections are unique aligned joints, say
     V(R_f) intersect V(R_e)={s},
     V(R_f) intersect V(A)={t},
and no clean lens between R_e and A has s in the interior of its R_e-side and t in the interior of its A-side.

In particular, after excluding multiple-overlap outcomes, the cycle-neighbor rail cannot pierce any clean certificate-anchor/source-rail lens: its two unique gates must lie outside, on the boundary of, or on the same side of every such lens.

## Body

The first intersection is part of residual case (4) of d0a41dede20a: R_f meets R_e in a unique aligned joint there. Independently, f and the selected anchor hyperedge are distinct ascending nonspecial edges terminal at the same vertex v. Their canonical source rails R_f and A therefore intersect by 0c885137ea8c.

If either rail pair has at least two common vertices, (i) or (ii) holds. Assume both intersections are unique. By 5854d853a44b, each unique common vertex is an aligned internal joint on the corresponding pair of maximum endpoint paths.

Suppose for contradiction that some clean lens L between R_e and A has s in the interior of its R_e-side and t in the interior of its A-side. Since R_f meets R_e only at s and A only at t, the R_f-subpath from s to t has interior disjoint from both full paths R_e and A. Thus it is a clean third-path crossing from the interior of one side of L to the interior of the other.

This is forbidden by the certified no-piercing theorem 6cb0d0ddee15. Therefore no such lens exists, proving (iii).

The result does not assume that R_e and A automatically form a genuine lens. It only constrains every clean lens that actually occurs between them, so it is compatible with the endpoint-lens counterexample 23fac5740304.
