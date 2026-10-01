# Two-hole gap-three collisions rotate the wrong-entrance state

## Statement

Let Q=(p_1,...,p_s) be a linear 3-uniform path ending at a prescribed last vertex x, with holes a,b outside V(Q). Suppose f={a,r,w} and g={b,w,t} are edges with r,w,t distinct on Q. Put i=max{j:r∈p_j} and k=min{j:t∈p_j}, and suppose every occurrence of w lies strictly between i and k. Then
  (p_1,...,p_i,f,g,p_k,...,p_s)
is a linear path of length s+3-(k-i), ending at x.
In particular:
(1) k-i=2 gives an (s+1)-edge path;
(2) k-i=3 gives another s-edge path with the same terminal suffix and hence the same prescribed final-edge entrance.
For an alternate wrong-entrance witness s=ell-2, case (1) is an immediate contradiction and case (2) is a length-preserving rotation within the wrong-entrance two-hole state space.

## Body

The intersection check is the same as in de0c1d15d897 and does not depend on the exact value of k-i.

Because i is the last path-edge index containing r, f meets the retained prefix p_1,...,p_i only at r in p_i. By hypothesis all occurrences of w lie in the omitted interval, so the w-contact of f and g creates no further retained-path intersection.

Similarly, since k is the first index containing t, g meets the retained suffix p_k,...,p_s only at t in p_k. The edges f and g meet exactly at w by linearity. All other nonconsecutive intersections are inherited from Q. Thus the displayed sequence is linear.

Its edge count is
  i+2+(s-k+1)=s+3-(k-i).
The suffix from p_k through p_s is unchanged, so the final edge and its entrance are unchanged.

If k-i=2, the new path has length s+1. If s=ell-2 and Q already ends in the fixed top-rank nonspecial edge through a wrong entrance, this is an (ell-1)-edge wrong-entrance witness, contradiction.

If k-i=3, the new path has the same length s and the same wrong entrance. Since an s-edge 3-uniform linear path has the same number of vertices as Q and now contains the old holes a,b, it omits exactly two vertices formerly on Q. Hence it is another state of precisely the same two-hole type.
