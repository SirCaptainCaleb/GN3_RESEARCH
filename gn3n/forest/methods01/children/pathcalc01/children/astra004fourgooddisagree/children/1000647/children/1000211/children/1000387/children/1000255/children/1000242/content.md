# The matching-block reversed-edge kernel forces a three-order reverse fan

## Statement

In the edge-orderable non-Hamiltonian matching-block branch of 53005a4e0315, let uv be the displayed ordered edge and x the third vertex of the reversing triple. Regardless of whether the original reversing triple is (x,v,u) or (v,u,x), the three edge comparisons on {x,u,v} satisfy xv<uv<xu. Consequently all three ordered triples (x,v,u), (v,u,x), and (v,x,u) are tight. In particular the reversed ordered pair (v,u) is extended by the same witness x on both sides: both (x,v,u) and (v,u,x) are tight.

## Body

In the first orientation branch of 53005a4e0315, the unique matching-block order on X={x,u,v,b} is {xv,ub}<{xb,uv}<{xu,vb}. Restricting to the three edges on {x,u,v} gives xv<uv<xu. Tightness in an edge-orderable three-set is exactly increasing comparison along the two consecutive ordinary edges. Hence xv<uv gives (x,v,u), uv<ux gives (v,u,x), and xv<xu gives (v,x,u) tight. In the second orientation branch, the unique block order on X={a,u,v,x} is {au,vx}<{ax,uv}<{av,ux}, which again restricts to vx<uv<ux, i.e. xv<uv<xu. The same three tight orders follow. Thus the two matching-block orientation cases induce one identical reverse-fan structure on the three vertices x,v,u.
