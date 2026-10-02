# Every threshold color supplies many private-to-private forest connectors

## Statement

Assume the color-complete path-forest normal form c15cf7354428. Let F=H[X] have m edges and c nonempty path components. Then F has r=m+2c vertices of forest-degree one and j=m-c joint vertices of forest-degree two. For each color d in D, the d-colored matching on X saturates all r forest-degree-one vertices, and therefore contains at least ceil(3c/2) edges whose two endpoints both have forest-degree one.

## Body

A t-edge linear 3-uniform path has 2t+1 vertices. Exactly t-1 of them are path joints, each lying in two path edges, so the remaining t+2 vertices have path degree one. Summing over the c path components of F gives
  r=m+2c
degree-one vertices and
  j=m-c
degree-two joint vertices.

Fix a color d. By c15cf7354428, the d-colored edges form a matching M_d on X that saturates every one of the r degree-one vertices.

Let a be the number of M_d edges joining two degree-one vertices and b the number joining a degree-one vertex to a joint. Since every degree-one vertex is saturated exactly once,
  2a+b=r.
Because M_d is a matching, its b degree-one-to-joint edges use b distinct joint vertices, so b<=j. Hence
  2a >= r-j = (m+2c)-(m-c)=3c,
and therefore
  a>=ceil(3c/2).

Thus every threshold color supplies at least ceil(3c/2) direct connectors between private rail vertices.