# The trapped-negative top matching graph has a vertex of degree at least two kappa plus five

## Statement

In the exceptional two-layer charge state of 76c961f0dc48, with notation
  a=kappa+2,
  N={v:k_v<0},
  R=sum_{v∈N}(-k_v),
and top matching graph G supported on S=V(G),
one has
  average_degree(G)>2a.
Consequently
  Delta(G)>=2a+1=2kappa+5.

Thus some top-layer vertex u with phi(u)=ell-1 is terminal on at least 2kappa+5 distinct rank-(ell-1) ascending nonspecial edges whose unique entrances are distinct negative-charge vertices of potential ell-2 and whose opposite terminals also lie in the top layer.

## Body

For each negative vertex v∈N of mass r=-k_v, 76c961f0dc48 gives a color class in G of size at least
  a+r.
Summing over colors,
  |E(G)|
  >= a|N| + R.                                      (1)

By 1ecaca9f1fc7,
  R>=a|S|,
so
  |S|<=R/a.                                          (2)

Therefore
  average_degree(G)
  =2|E(G)|/|S|
  >=2(a|N|+R)/(R/a)
  =2a + 2a^2|N|/R
  >2a.

Since graph degrees are integers, some vertex has degree at least
  2a+1=2kappa+5.

Every G-edge incident with such a vertex u comes, by construction, from a rank-(ell-1) ascending nonspecial hyperedge whose source color lies in N and whose two terminals lie in T={phi=ell-1}. Proper coloring implies the incident edges have distinct source colors. This gives the stated hypergraph interpretation.
