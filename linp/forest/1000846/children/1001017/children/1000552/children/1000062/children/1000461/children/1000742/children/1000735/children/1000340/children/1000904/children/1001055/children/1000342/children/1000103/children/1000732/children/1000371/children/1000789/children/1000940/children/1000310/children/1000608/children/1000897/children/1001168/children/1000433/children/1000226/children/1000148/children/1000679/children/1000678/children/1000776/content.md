# The odd tight U_11 collision reduces to a cycle, multiple source-path overlap, or reciprocal terminal exchange

## Statement

Retain the odd tight color-terminal collision of 9b00516e2965. Thus
  r_i=2m+1,
  r_j=m+1,
  r_{j+1}=m+2,
the chosen maximum path
  R_i=(g_1,...,g_{2m})
ends at x_i=v_j,
  x_j=g_m intersect g_{m+1},
and the exact contact c_{j+1} of E_{j+1} with R_i lies on g_m.

Let
  Q=(g_1,...,g_m),
so Q is a maximum m-edge path with last vertex x_j.
Let R_j and R_{j+1} be the chosen maximum source paths of E_j and E_{j+1}, ending at x_j and x_{j+1} respectively.

Then at least one of the following holds:

(1) Q union R_j contains a linear cycle;

(2) R_j and R_{j+1} have at least two common vertices;

(3) all of the following hold:
    (a) g_m is the last edge of R_j;
    (b) c_{j+1}=v_{j+1};
    (c) E_{j+1} intersect V(R_j)={v_{j+1}};
    (d) E_j intersect V(R_{j+1})={v_{j-1}};
    (e) R_j and R_{j+1} have exactly one common vertex, which is an internal joint at the same path-edge index on both paths.

Thus the hard residue of the odd half-rank collision is a reciprocal terminal-terminal exchange between the two adjacent source paths.

## Body

The path Q has m edges and last vertex x_j. Since E_j is ascending of edge rank m+1, phi(x_j)=m, so Q is maximum at x_j. The chosen source path R_j is another maximum m-edge path ending at x_j.

The two paths cannot meet only at x_j: by 5854d853a44b a unique common vertex of two maximum endpoint paths must be an aligned internal joint, whereas x_j is the last vertex of both Q and R_j. Hence Q and R_j have at least two common vertices.

Apply 41100a9882dd with A=Q, P=R_j, u=x_j. Either Q union R_j contains a linear cycle, giving (1), or the last edge of R_j is an edge of Q. In the latter case that shared edge must be g_m, because x_j belongs to no other edge of Q. Hence (3a) holds whenever (1) fails.

Assume from now on that (1) fails. Because c_{j+1} lies on g_m, the edge E_{j+1} meets R_j at c_{j+1}. If c_{j+1}=x_{j+1}, then x_{j+1} lies on R_j and is the last vertex of R_{j+1}. By 5854d853a44b the two source paths cannot have x_{j+1} as their unique common vertex, so (2) holds. Therefore, if (2) also fails,
  c_{j+1}=v_{j+1}.
The source path R_j avoids the common terminal v_j=x_i, and x_{j+1} is absent by the preceding argument. Hence
  E_{j+1} intersect V(R_j)={v_{j+1}},
proving (3b,c).

Now apply f831721c17f8 to the consecutive-rank source-clean edges E_j,E_{j+1}, which share terminal x_i. It gives
  E_j intersects V(R_{j+1}).
The path R_{j+1} avoids x_i. Thus the contact is x_j or v_{j-1}. If x_j lies on R_{j+1}, then x_j is the last vertex of R_j, so 5854d853a44b again forces at least two common vertices of R_j,R_{j+1}, giving (2). Therefore, outside (2), the contact is v_{j-1}. Since x_j and x_i are absent from R_{j+1},
  E_j intersect V(R_{j+1})={v_{j-1}},
proving (3d).

Finally 0c885137ea8c guarantees that the two canonical source paths R_j,R_{j+1} have a common vertex. Since (2) fails, they have exactly one. The unique-intersection theorem 5854d853a44b then identifies this vertex as an internal joint occurring at the same path-edge index on both paths. This is (3e).
