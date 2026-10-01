# A one-backward cycle has a free forward arc and a two-coverable shifted defect

## Statement

Refine the normalization by minimizing, after backward-count, the span of the unique backward comparison. Assume b=1 and write the monotone cycle as e_r->e_0 together with e_0->e_1->...->e_r. At least one forward cycle comparison beta=e_k->e_{k+1} is unused by the fixed three-cover F. Reversing both the backward comparison and beta preserves F, leaves exactly one backward comparison, and strictly decreases its span. Therefore the resulting boundary tournament has path-cover number at most two.

## Body

The chordless cycle has star, triangle, or vertex-simple ordinary-cycle geometry. Its forward comparisons cannot all be used by the vertex-disjoint paths of F: in the ordinary-cycle cases that would repeat the initial ordinary vertex in one path, while in the star case the required path segments overlap at the common center. Choose an unused beta. Reversing the old backward comparison makes it forward; reversing beta makes beta backward. Neither is used by F, so F survives. Along the monotone return path the endpoints of beta lie strictly between those of the old backward comparison, so its order-span is smaller. A path-cover-three result would contradict the refined extremal choice. Hence the shifted tournament is two-coverable.
