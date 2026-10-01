# Replacing one component by a Hamiltonian set h vertices larger forces a complement-imbalance penalty

## Statement

Let C=X|P|Q be a spanning three-cover of a boundary tournament that minimizes Phi=sum |C_i|^2 among all spanning three-covers. Write |X|=c, |P|=m, |Q|=r, set s=m+r and d=|m-r|. Let h>=1, let F be any Hamiltonian vertex set of order c+h, and suppose H-F has a two-component cover U|V. Put delta=||U|-|V||. Then
delta^2 >= d^2 + h(2s-4c-3h).
In particular, whenever 2s>4c+3h, every such complement cover is strictly more imbalanced than P|Q.

## Body

Write u=|U| and v=|V|. Since F|U|V is a spanning three-cover and X|P|Q is globally Phi-minimal,
c^2+m^2+r^2 <= (c+h)^2+u^2+v^2.        (1)

The old two-component sum is
s=m+r,
and the new complementary sum is
u+v=|V(H)|-(c+h)=m+r-h=s-h.

Let
d=|m-r|,
delta=|u-v|.
For any two numbers with sum S and absolute difference D,
2(a^2+b^2)=S^2+D^2.
Hence
2(m^2+r^2)=s^2+d^2
and
2(u^2+v^2)=(s-h)^2+delta^2.

Multiply (1) by two and substitute these identities:
2c^2+s^2+d^2
<=
2(c+h)^2+(s-h)^2+delta^2.

Therefore
delta^2
>=
d^2+2c^2+s^2-2(c+h)^2-(s-h)^2
=
d^2+h(2s-4c-3h).

If 2s-4c-3h>0, the added term is positive, so delta^2>d^2 and therefore delta>d. Thus every two-component cover of the complement of F is strictly more imbalanced than the original pair P|Q.

No boundary-orientation property beyond the existence of the displayed covers enters the proof. The statement is pure quadratic-potential calculus and applies to any route that enlarges one component support while replacing the other two components by a cover of the complementary vertices.

For c=4 and h=1 this gives
delta^2 >= d^2+2(m+r)-19,
which is the imbalance estimate appearing in the global four-vertex-component route.
