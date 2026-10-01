# Saturated blocker fan at the boundary q=δ

## Statement

Let H have minimum degree δ and let e={x,y,z} be an ascending nonspecial edge with q=φ(e)=δ. Let Q be a (q-1)-edge path ending at x and avoiding y,z, and let a be its opposite last vertex. If Q has no safe single-blocker rotation avoiding y,z, then d_H(a)=q. Moreover the number S of single-blocking edges through a besides the first edge of Q is 2 or 3, every such edge is exceptional (its blocker is x or it contains y or z), the number of double-blocking edges is D=q-1-S, and the blocker vertices used by these edges leave exactly S-2 vertices of V(Q)\g_1 unused.

## Body

Put t=q-1. The single-blocker surplus gives S>=2(d_H(a)-t)=2(d_H(a)-q+1). If there is no safe rotation, every single-blocking edge is exceptional: at most one can have blocker x, at most one can contain y, and at most one can contain z. Hence S<=3. Since d_H(a)>=δ=q, the displayed lower bound implies d_H(a)<=q, so d_H(a)=q. Therefore S+D=q-1. The blocker capacity is S+2D<=2t-2=2q-4. Substituting D=q-1-S gives 2q-2-S<=2q-4, hence S>=2; together with S<=3, S∈{2,3}. Finally the number of unused blocker vertices is (2q-4)-(S+2D)=(2q-4)-(2q-2-S)=S-2.