# The S-entrance pattern in the pure p=4 obstruction is impossible

## Statement

Pattern (A) in the three-pattern normal form 49c24605109f is impossible. Hence any pure p=4 obstruction must be of pattern (B) or (C), with S unused and T,U,V visible entrances.

## Body

In pattern (A), write
g_1={L,M,R}, g_2={R,S,T}, g_3={T,U,V},
with f_4 entered through V.
The S-slot is a visible entrance. By 0feaf8d8f358 its opposite terminal is a private vertex of g_1; after swapping L,M write
f_S={S,v,L}.

The T-slot is also a visible entrance in pattern (A), so phi(T)=3.

Now consider
g_1, f_S, f_4, g_3.
Consecutive intersections are
g_1∩f_S={L},
f_S∩f_4={v},
f_4∩g_3={V}.
The nonconsecutive pairs are disjoint:
g_1 is disjoint from f_4 and g_3 by the original path P, while f_S is disjoint from g_3 because f_S={S,v,L} and g_3={T,U,V}.
Thus this is a four-edge linear path.

Its last edge is g_3={T,U,V}, and the preceding edge f_4 meets g_3 at V. Therefore T is a last vertex of this four-edge path. Hence phi(T)>=4, contradicting phi(T)=3.

So pattern (A) cannot occur.
