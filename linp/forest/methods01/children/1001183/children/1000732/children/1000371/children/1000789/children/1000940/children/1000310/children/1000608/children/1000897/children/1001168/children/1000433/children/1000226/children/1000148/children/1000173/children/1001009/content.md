# Tight-collision rotation outputs split into rank rise, rank-p special/nonascending, or one exact ascending entrance

## Statement

Retain outcome (B) of 259bdff45872 and put
  p=r_i-1.
Let h be the last edge of the p-edge rotated path, and let y,z be the two distinct vertices of h that can be chosen as last vertices of that rotation. Then
  phi(h)>=p,
  phi(y)>=p,
  phi(z)>=p.

Consequently exactly one of the following holds:

(1) phi(h)>p;

(2) phi(h)=p and h is special;

(3) phi(h)=p, h is nonspecial and nonascending;

(4) phi(h)=p and h is ascending nonspecial. In this case neither y nor z is the unique entrance of h. The third vertex w of h is the unique entrance and
    phi(w)=p-1.

In alternatives (2) and (3), every vertex of h has vertex rank at least p. In alternative (4), h has exactly two vertices of vertex rank at least p, namely y,z, and one unique entrance w of vertex rank p-1.

For the smallest parity-boundary cases in which h is also the last edge of the original path R_i, the third vertex is x_i and already has vertex rank p; hence alternative (4) cannot occur there.

## Body

The inequalities for h,y,z are exactly the rotation-packet conclusion of 259bdff45872.

If phi(h)>p we are in (1), so assume phi(h)=p. The edge is either special or nonspecial. If special, every vertex t in h satisfies phi(t)>=phi(h)=p, because t is terminal at h in the snake-digraph sense. This is (2).

Suppose h is nonspecial and let w_0 be its unique entrance. If h is nonascending, then
  phi(w_0) != p-1.
Deleting h from a longest p-edge path ending in h gives phi(w_0)>=p-1, so nonascending implies phi(w_0)>=p. The other two vertices are terminal at h and therefore also have vertex rank at least p. This is (3).

Finally suppose h is ascending. Its unique entrance has vertex rank exactly p-1. Since y and z both have vertex rank at least p, neither can be the unique entrance. Thus the third vertex w is the unique entrance and phi(w)=p-1, proving (4).

If h is also the last edge of the original source path R_i, then the third vertex outside the two rotation endpoints is x_i, whose vertex rank is
  phi(x_i)=r_i-1=p.
It cannot be the unique entrance of an ascending rank-p edge, so alternative (4) is excluded in that boundary case.