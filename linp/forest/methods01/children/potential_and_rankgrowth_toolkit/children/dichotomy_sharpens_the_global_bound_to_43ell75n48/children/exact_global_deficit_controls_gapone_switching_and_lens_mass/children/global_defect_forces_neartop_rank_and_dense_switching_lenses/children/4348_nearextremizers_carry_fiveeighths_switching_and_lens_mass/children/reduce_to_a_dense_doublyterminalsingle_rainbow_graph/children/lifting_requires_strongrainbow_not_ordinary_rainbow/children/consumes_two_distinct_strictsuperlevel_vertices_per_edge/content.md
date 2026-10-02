# A clean common entrance consumes two distinct strict-superlevel vertices per edge

## Statement

Fix the globally chosen maximum endpoint path P_x at a vertex x. Let F_x be any family of ascending nonspecial edges
  e={x,u_e,v_e}
whose unique entrance is x and whose source incidence is clean relative to P_x, that is mu_x(e)=0.

Then the terminal pairs {u_e,v_e}, e in F_x, are pairwise disjoint, are disjoint from V(P_x), and lie in the strict potential superlevel
  V_{>phi(x)}={w:phi(w)>phi(x)}.
Consequently
  2|F_x| <= |V_{>phi(x)} minus V(P_x)|.

In particular, if c_11(x) counts U_11 edges colored by entrance x in the near-extremal terminal graph, then
  2c_11(x) <= |V_{>phi(x)} minus V(P_x)|.

## Body

Let p=phi(x). Since e is ascending with unique entrance x, phi(e)=p+1. A canonical longest e-ending path enters e through x, so either terminal u_e or v_e may be chosen as the last vertex. Hence phi(u_e),phi(v_e)>=p+1, so both terminals lie in V_{>p}. Because mu_x(e)=0, neither terminal meets the precursor of the chosen maximum x-ending path P_x. Neither can lie in the last edge of P_x either: that last edge contains x, while e also contains x, so a shared terminal would make the two distinct hyperedges share two vertices, contradicting linearity. Thus {u_e,v_e} is disjoint from V(P_x). Finally, for distinct e,f in F_x, the two hyperedges already share x. Linearity therefore makes their terminal pairs disjoint. The union of all terminal pairs has size exactly 2|F_x| and lies in V_{>p} minus V(P_x), proving the inequality. Every U_11 edge has a clean source incidence by definition of the 0-1-1 signature, so the final assertion is immediate.