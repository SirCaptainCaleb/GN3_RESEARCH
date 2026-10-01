# Every interior U_11 color-terminal collision pays plus three or forces owner-to-hit source-path overlap

## Statement

Let
v_0v_1...v_k
be a rainbow terminal-pair path whose parent hyperedges
E_s={x_s,v_{s-1},v_s}
belong to U_11 and have nondecreasing edge ranks r_s. Let R_s be the chosen maximum source path ending at x_s.

For every interior color-terminal collision
  x_i=v_j,
at least one of the following holds:

(1) r_j+r_{j+1} >= r_i+3;

(2) x_j belongs to V(R_i), and consequently
    |V(R_i) intersect V(R_j)|>=2.

Thus the sole failure of the plus-three adjacent edge-rank-sum inequality is never geometrically free: it forces a multiple intersection between the colliding source path and the source path of the left parent edge adjacent to the hit terminal vertex.

## Body

Assume (1) fails. By the certified universal bound 867efd696575,
  r_j+r_{j+1}>=r_i+2,
so necessarily
  r_j+r_{j+1}=r_i+2.
The certified half-rank classification 9b023ed3d700 applies.

If r_i is odd, 9b00516e2965 states directly that the exact contact of E_j with R_i is its unique entrance x_j. Hence x_j belongs to V(R_i).

If r_i is even, f0f28f03b0d9 states that both exact contacts of E_j,E_{j+1} with R_i are unique entrances of their parent edges. In particular the exact contact of E_j is x_j, so again x_j belongs to V(R_i).

Now R_j is a maximum endpoint path whose last vertex is x_j, while R_i is a maximum endpoint path containing x_j and ending at the distinct vertex x_i. If x_j were their unique common vertex, the certified unique-intersection theorem 5854d853a44b would force x_j to be an internal aligned joint of R_j. But x_j is the last vertex of R_j. Therefore R_i and R_j have at least two common vertices.

This proves (2).
