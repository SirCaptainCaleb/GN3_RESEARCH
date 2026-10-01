# A contact with a maximum endpoint path manufactures a balanced endpoint lens

## Statement

Let Q be a maximum a-edge path ending at x, so phi(x)=a. Let y be a vertex of Q distinct from x, and let P be any maximum b-edge path ending at y, so phi(y)=b.

Then Q and P have at least two common vertices. Moreover one can choose a common vertex z so that z,y are consecutive common vertices on the relevant y-side segments of Q and P, and the two z-to-y segments form a clean elementary lens with the same number of edges.

Thus every occurrence of a vertex y on a maximum endpoint path Q canonically yields a balanced endpoint lens between Q and any chosen maximum y-path.

## Body

Suppose first that V(Q) intersect V(P)={y}. By the universal unique-intersection theorem 5854d853a44b, the unique common vertex of two maximum endpoint paths must be an internal joint on both paths at the same index. But y is the designated last vertex of P, so y is not an internal joint of P. Contradiction. Hence Q and P have a second common vertex.

Choose z to be the next common vertex encountered from y along the Q-side and P-side after suppressing any common initial edge segment, so that the resulting z-to-y pieces are internally vertex-disjoint; these pieces form a clean elementary lens. Let A be the number of Q-edges on its z-to-y side and B the number of P-edges on its z-to-y side.

Replace the Q-side segment by the P-side segment. The resulting path still ends at x and has length a-A+B. Since Q is maximum at x,
a-A+B<=a,
so B<=A.

Conversely replace the terminal z-to-y segment of P by the Q-side segment. The resulting path still ends at y and has length b-B+A. Since P is maximum at y,
b-B+A<=b,
so A<=B.

Therefore A=B, and the elementary endpoint lens is balanced.