# A U_11 collision gives adjacent rank sum, a host 3-cycle, or two repeated source-path intersections

## Statement

Let
v_0v_1...v_k
be a rainbow path in the terminal-pair graph whose parent hyperedges
E_s={x_s,v_{s-1},v_s}
belong to U_11 and have nondecreasing edge ranks r_s.
Let x_i=v_j be an interior color-terminal collision, so 1<=j<=i-2.

Let R_s denote the chosen maximum path with last vertex x_s used for the source incidence of E_s. Then at least one of the following holds:

(1) r_j+r_{j+1} >= r_i+3;

(2) there is an edge g of R_i such that g,E_j,E_{j+1} form a linear 3-cycle;

(3) both adjacent source paths meet R_i at least twice:
    |V(R_j) intersect V(R_i)|>=2
and
    |V(R_{j+1}) intersect V(R_i)|>=2.

Thus, below the adjacent-rank-sum threshold and in the absence of a host 3-cycle, a U_11 color-terminal collision forces repeated intersections of the colliding source path with both source paths adjacent to the hit terminal vertex.

## Body

Since E_i is ascending, phi(x_i)=r_i-1. Because E_i has source contact multiplicity zero in U_11, R_i is a maximum path with last vertex x_i and length p=r_i-1.

By 608468bb403b, each of E_j and E_{j+1} has exactly one contact with the precursor of R_i away from x_i. Call these contacts c_j and c_{j+1}; they are distinct. Each contact is either the unique entrance of its parent edge or the opposite terminal.

Suppose at least one of c_j,c_{j+1} is an opposite terminal. Consider their path-edge occurrence intervals on R_i.

If the two intervals are disjoint, the certified separated mixed-singleton lemma e9fc907b07c9 applies with host-path length p=r_i-1 and gives
  r_j+r_{j+1} >= p+4 = r_i+3,
which is (1).

If the two occurrence intervals overlap, some edge g of R_i contains both c_j and c_{j+1}. The edges E_j and E_{j+1} already meet at x_i, while linearity gives
  E_j intersect E_{j+1}={x_i},
  g intersect E_j={c_j},
  g intersect E_{j+1}={c_{j+1}}.
The three pairwise intersection vertices are distinct, so g,E_j,E_{j+1} form a linear 3-cycle. This is (2).

It remains to consider the case in which both contacts are unique entrances:
  c_j=x_j,   c_{j+1}=x_{j+1}.
Then x_j lies on both R_i and R_j, and x_{j+1} lies on both R_i and R_{j+1}. The last vertices x_i,x_j,x_{j+1} are pairwise distinct because the terminal-pair path is rainbow.

If V(R_i) intersect V(R_j) consisted only of x_j, the certified unique-intersection theorem 5854d853a44b would force x_j to be an internal aligned joint on R_j, contradicting that x_j is the last vertex of R_j. Therefore
  |V(R_i) intersect V(R_j)|>=2.
The same argument gives
  |V(R_i) intersect V(R_{j+1})|>=2.
This is (3).
