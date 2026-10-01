# Three-pattern normal form for the pure p=4 obstruction

## Statement

Assume phi(v)=4 and four potential-charged ascending nonspecial edges through v all have rank four. Fix a longest path P=(g_1,g_2,g_3,f_4) ending in f_4 at v, and write
g_1={L,M,R}, g_2={R,S,T}, g_3={T,U,V},
with V=g_3∩f_4 the entrance of f_4. Then T is necessarily the entrance of one of the other charged edges. Up to swapping L,M, exactly one of the following three patterns holds:
(A) S,T,V are visible entrances; the fourth entrance is absent from P and its opposite terminal is R; U is unused as a charged witness.
(B) R,T,U,V are the four entrances; S is unused as a charged witness.
(C) T,U,V are visible entrances; the fourth entrance is absent from P and its opposite terminal is R; S is unused as a charged witness.
Moreover in every case the T-entrance edge has opposite terminal one of L,M.

## Body

By the five-slot witness localization, the four charged edges have four distinct witnesses among R,S,T,U,V, with f_4 using V. Hence exactly three of R,S,T,U are selected.

By f9e64ea63be0, among the other three charged edges at most one entrance is absent from P, and if an entrance is absent then its witness is the opposite terminal R. Therefore any selected witness among S,T,U is necessarily the entrance of its edge; R is either an entrance or the terminal witness of the unique absent-entrance edge.

At least one of S,T is selected, because three of the four slots R,S,T,U are selected.

Suppose S is selected. Then S is an entrance. By 0feaf8d8f358 its opposite terminal is a private vertex of g_1, say L, so the charged edge is f_S={S,v,L}.

The path
g_3,f_4,f_S,g_1
is linear: its consecutive intersections are V,v,L, while all nonconsecutive pairs are disjoint. The last edge g_1 can have R as a last vertex, so phi(R)>=4.

Likewise
g_1,f_S,f_4,g_3
is linear, with intersections L,v,V, and the last edge g_3 can have U as a last vertex. Hence phi(U)>=4.

Every visible entrance of a rank-four ascending edge has potential exactly three. Therefore neither R nor U can be a visible entrance.

Since three slots among R,S,T,U must be selected, U cannot be selected at all: it cannot be an entrance, and an absent-entrance edge can only use R as its witness. Thus the selected slots are R,S,T. The slot T is therefore a visible entrance. The slot R cannot be a visible entrance because phi(R)>=4, so it is the witness of the unique absent-entrance edge. This is pattern (A).

Now suppose S is not selected. Then the selected slots are R,T,U. Both T and U are selected and cannot be absent-entrance witnesses, so both are visible entrances. The slot R is either also a visible entrance, giving pattern (B), or is the opposite-terminal witness of the unique absent-entrance edge, giving pattern (C).

In all three patterns T is a visible entrance. By 0feaf8d8f358, the opposite terminal of the T-entrance edge is a private vertex of g_1, i.e. one of L,M.
