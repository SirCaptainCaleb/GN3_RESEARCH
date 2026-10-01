# Switching edges inject into the half-potential superlevel

## Statement

Let H be a finite linear 3-graph and let v be an active misaligned vertex with p=phi(v)>=8. In the setup of b032348c1a8a, choose a maximum-rank ascending terminal anchor and let F_v be the resulting family of anchor-double / maximum-path-single switching edges. Then the unique entrance vertices of the edges in F_v are pairwise distinct and all have endpoint potential at least ceil(p/2). Consequently
  |V_{>=ceil(p/2)}| >= |F_v|
  >= beta(p)-eta_v-ceil((3q(v)-4)/4).
In particular,
  |V_{>=ceil(p/2)}| >= (5/8)p-eta_v-O(1).

Thus if eta_v=o(p), the half-potential superlevel contains at least (5/8-o(1))p vertices.

## Body

Write an edge f in F_v as
  f={x,v,u},
where x is its unique entrance and v,u are its terminals. Since f is ascending nonspecial and v is a terminal of potential p=phi(v), the certified terminal-potential/rank inequality a7b7670e955a gives
  p<=2phi(f)-2.
Hence
  phi(f)>=ceil((p+2)/2).
Because f is ascending,
  phi(x)=phi(f)-1>=ceil((p+2)/2)-1=ceil(p/2).           (1)

Distinct members of F_v have distinct entrance vertices. Indeed every member contains v, and if two distinct such hyperedges shared the same entrance x they would intersect in both v and x, contradicting linearity. Thus the map
  f -> entrance(f)
injects F_v into V_{>=ceil(p/2)}. Therefore
  |V_{>=ceil(p/2)}|>=|F_v|.                            (2)

By b032348c1a8a,
  |F_v|>=beta(p)-eta_v-ceil((3q(v)-4)/4).              (3)
Combining (2) and (3) proves the exact displayed estimate.

Since q(v)<=p-1 and the ceiling term is increasing,
  beta(p)-ceil((3q(v)-4)/4)
  >=beta(p)-ceil((3p-7)/4)
  =(5/8)p-O(1).
This yields
  |V_{>=ceil(p/2)}| >= (5/8)p-eta_v-O(1).

The argument deliberately does not distinguish entrance-retained from terminal-retained switchers. The entrance is visible on the host path in the first case and omitted in the second, but in both cases it is a distinct vertex of potential at least ceil(p/2).
