# Exact deficiency equation at the fixed hole

## Statement

In the canonical loss-one two-cycle setting, let P be the rotated x-ending path of length q-2, let b be the fixed omitted vertex, and let g be the original path edge through b, whose other two vertices both lie on P. Among edges through b other than g, let C,R,D count those having respectively 0,1,2 non-b vertices on V(P). Then C+R+D=d_H(b)-1>=q-1, R+2D<=2q-5, and hence 2C+R>=3. If equality 2C+R=3 holds, then d_H(b)=q, every path vertex allowed by linearity is used by exactly one b-edge, and exactly one of the following occurs: (i) C=0,R=3,D=q-4; (ii) C=1,R=1,D=q-3.

## Body

The path P has 2(q-2)+1=2q-3 vertices. The omitted original edge g contains b and two vertices c,c' of P. Any other edge f through b cannot contain c or c', since then f and g would intersect in b and c (or c'), contradicting linearity. Distinct edges through b have disjoint non-b vertex pairs. Therefore the total number of P-contacts contributed by all edges through b other than g is R+2D, and these contacts are distinct vertices of V(P)\{c,c'}, a set of size 2q-5. Thus R+2D<=2q-5. Also C+R+D=d_H(b)-1>=q-1 because the minimum degree is q. Subtracting gives
2C+R=2(C+R+D)-(R+2D)>=2(q-1)-(2q-5)=3.
If equality holds, both preceding inequalities are equalities: d_H(b)=q and R+2D=2q-5, so all allowable P-vertices are saturated by b-edges. The nonnegative integer solutions to 2C+R=3 are (C,R)=(0,3) and (1,1). The degree equation then gives D=q-4 and D=q-3 respectively.