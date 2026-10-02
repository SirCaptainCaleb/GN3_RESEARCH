# Replacing one component by a path support h vertices smaller forces the dual complement-imbalance penalty

## Statement

Let A|B|C be a spanning three-cover minimizing Phi among all spanning three-covers of H, with |A|=a, |B|=b, |C|=c. Put s=b+c and d=|b-c|. Let 1<=h<a, let F be any path support of order a-h, and suppose H-F has a two-cover U|V with delta=||U|-|V||. Then delta^2 >= d^2+h(4a-2s-3h). In particular, whenever 4a>2s+3h, every such complementary cover is strictly more imbalanced than B|C.

## Body

Put u=|U| and v=|V|. Since F|U|V is a spanning three-cover and A|B|C is globally Phi-minimal,
a^2+b^2+c^2 <= (a-h)^2+u^2+v^2.          (1)

The old complementary sum is
s=b+c,
whereas
u+v=|V(H)|-(a-h)=b+c+h=s+h.

Write
d=|b-c|,
delta=|u-v|.
For any two nonnegative component orders with sum S and absolute difference D,
2(x^2+y^2)=S^2+D^2.
Thus
2(b^2+c^2)=s^2+d^2
and
2(u^2+v^2)=(s+h)^2+delta^2.

Multiply (1) by two and substitute:
2a^2+s^2+d^2
<=
2(a-h)^2+(s+h)^2+delta^2.
Rearranging gives
delta^2
>= d^2+2a^2+s^2-2(a-h)^2-(s+h)^2
= d^2+h(4a-2s-3h).

If 4a-2s-3h>0, the added term is positive, so delta^2>d^2 and therefore delta>d.

The argument uses only global quadratic minimality and the existence of the displayed complementary cover. It is the shrinking-side dual of the certified enlargement penalty 40c4a8aca820.

For h=1 this becomes
delta^2 >= d^2+4a-2b-2c-3.
Hence, whenever 4a>2b+2c+3, deleting either displayed endpoint of A and covering the complementary vertices forces strictly greater imbalance than the original pair B|C. In a counterexample minimal by order, those complementary two-covers exist for every nonempty proper endpoint truncation of A.