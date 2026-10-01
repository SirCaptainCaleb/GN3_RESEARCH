# Potential-oriented local degree would close the zero residue equality layer

## Statement

Assume the potential-oriented local bound 50b6278b9537: for every vertex v, at most three ascending nonspecial edges e={x,v,u} with v terminal satisfy phi(u)>=phi(v). Then the ascending terminal-pair graph T_up is 3-degenerate. Consequently |E(T_up)|<3|V(T_up)|<=3|V(H)|. In particular, combined with exact-density accounting, this alone eliminates every equality-layer counterexample for ell≡0 mod3.

## Body

Let J be any nonempty subgraph of T_up. Choose v∈V(J) minimizing phi(v).

For every edge vu of J, the corresponding hyperedge is ascending nonspecial and has v,u as its two terminals. By minimality of phi(v) on V(J),
  phi(u)>=phi(v).
Thus every J-edge at v is potential-charged at v in the sense of 50b6278b9537.

Assuming that local bound, d_J(v)<=3. Since J was arbitrary, every nonempty subgraph of T_up has a vertex of degree at most three, so T_up is 3-degenerate. Therefore
  |E(T_up)|<=3|V(T_up)|-O(1)<3|V(H)|
for every nonempty finite graph.

Now in the exact-density equality layer with ell≡0 mod3, f7f7b7e447c8 gives
  A=|E(T_up)|>=3|V(H)|.
Contradiction.

Hence the potential-oriented local bound, even without the stronger mad(T_up)<=3 conjecture, suffices to settle the ell≡0 mod3 equality layer.
