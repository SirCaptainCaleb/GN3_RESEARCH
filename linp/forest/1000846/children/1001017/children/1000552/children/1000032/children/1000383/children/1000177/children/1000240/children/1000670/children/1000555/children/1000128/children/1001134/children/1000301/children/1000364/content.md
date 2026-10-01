# Endpoint-retaining repeated intersections force a cycle or adjacent source-path last-edge containment

## Statement

Let x_i=v_j be an interior color-terminal collision on a simple rainbow terminal-pair path, and let R_i,R_j,R_{j+1} be the chosen maximum source paths ending at x_i,x_j,x_{j+1}. Assume
  x_j in V(R_i),
  x_{j+1} in V(R_i),
and
  |V(R_i) intersect V(R_j)|>=2,
  |V(R_i) intersect V(R_{j+1})|>=2.
Let h_j and h_{j+1} be the last edges of R_j and R_{j+1}.

For each s in {j,j+1}, either R_i union R_s contains a linear cycle, or h_s belongs to E(R_i).

Consequently, if neither union contains a linear cycle, then R_i contains both h_j and h_{j+1}. If in addition there is no linear 3-cycle consisting of E_j,E_{j+1} and one edge of R_i, then h_j!=h_{j+1}.

## Body

For s=j, the last vertex x_j of R_j lies on R_i by hypothesis, and R_i,R_j have another common vertex. Apply 41100a9882dd with A=R_i, P=R_j, and u=x_j. It gives either a linear cycle in R_i union R_j or h_j in E(R_i). The same argument with s=j+1 gives either a linear cycle in R_i union R_{j+1} or h_{j+1} in E(R_i).

Assume neither union contains a linear cycle, so both last edges lie on R_i. Suppose h_j=h_{j+1}=h. Because R_j is the chosen source path for E_j, it avoids the two terminals of E_j, hence h meets E_j at x_j and not at x_i=v_j or v_{j-1}. Similarly, R_{j+1} avoids the two terminals of E_{j+1}, so h meets E_{j+1} at x_{j+1} and not at x_i or v_{j+1}. The vertices x_i,x_j,x_{j+1} are distinct by rainbowness and the parent-edge definitions. Therefore
  E_j intersect E_{j+1}={x_i},
  h intersect E_j={x_j},
  h intersect E_{j+1}={x_{j+1}},
so h,E_j,E_{j+1} form a linear 3-cycle. Thus exclusion of such a 3-cycle forces h_j!=h_{j+1}.