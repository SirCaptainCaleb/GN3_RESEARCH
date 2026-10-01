# Strict-rise clean U11 edges still violate four-edge spacing

## Statement

For every integer R>=43 there is a finite linear 3-graph with four ascending nonspecial edges
  e_i={x_i,v,u_i},  i=1,2,3,4,
having ordered edge ranks
  (R+1,R+1,R+7,R+7),
such that
  phi(v)=R+9,
  phi(u_i)=R+10  for every i.
Moreover the four chosen source paths are clean and every e_i is terminal-single on the chosen maximum paths at both terminals.

Thus all four edges have strict terminal-potential rise away from the common terminal v, yet
  2q_2=2R+2 < 2R+9=q_1+q_4+1.
Hence four-edge deficit-doubling is false even for source-clean, doubly-terminal-single, strict-rise ascending edges.

The construction still does not supply the genuine common-anchor selected-certificate hypothesis needed by the repaired post-43/48 target.

## Body

Start from the construction of 74d30147c051. Thus
  g_j={z_{j-1},b_j,z_j}, 1<=j<=R+9,
is the backbone, p=R+9, v=b_p,
  x_1=b_R, x_2=z_R, x_3=b_{R+6}, x_4=z_{R+6},
and
  e_i={x_i,v,u_i}.
Keep the same source positions and the same four e_i, but increase every private branch length by one:
  |B_1|=|B_2|=10,
  |B_3|=|B_4|=4.
Each B_i begins at x_i and ends at u_i; all other branch vertices are fresh.

The graph remains linear. As before, no branch can occur internally in a linear path that passes from its x_i end to u_i and then continues through e_i, because e_i meets the first and last branch edges at two nonconsecutive vertices.

Delete the first R-1 backbone edges. The remaining core now has
  10+2*10+2*4+4=42
edges, which is less than R. Hence every path relevant to a rank at least R may again be rooted at the full prefix g_1,...,g_R.

The rooted-path classification from 74d30147c051 changes only by the one extra available branch edge. After g_R:
- a low branch contributes at most 10 further edges, so the total is at most R+10;
- after continuing to g_{R+6}, a high branch contributes at most 4 edges, again giving at most R+10;
- after a low e_i, traversal backward along its own branch can use B_{i,10},...,B_{i,2}, namely 9 branch edges, giving R+10;
- after a high e_i, its own branch contributes at most 3 edges after e_i, again giving at most R+10;
- every host-reversal or two-e_i route has the same bound as before or increases by only one, hence is also at most R+10.
Thus every path has length at most R+10.

For the four branch endpoints, the backbone prefix through the source followed by the whole branch gives
  R+10
edges:
  R+10 for i=1,2,
  (R+6)+4=R+10 for i=3,4.
Hence
  phi(u_i)=R+10.

The full backbone still gives a p=R+9 edge path ending at v. A path ending at v through some e_i has length at most phi(e_i), which will be at most R+7; a path using a branch and then e_i through u_i can use at most the branch with its first edge deleted, hence has length at most 10. If g_p is preceded by an e_i, then v has already occurred in that predecessor and cannot be the last vertex. Therefore no R+10 edge path ends at v, and
  phi(v)=R+9.

The source-rank argument is unchanged. A low source can be a last vertex only on the ordinary backbone prefix, so
  phi(x_1)=phi(x_2)=R.
Likewise the ordinary prefix to g_{R+6} is still longest at each high source:
  phi(x_3)=phi(x_4)=R+6.
The added branch edges cannot improve these values because a branch is terminal and any reverse branch route to its source has length at most 10.

For a low e_i, every rooted path ending in e_i at length at least R must use it immediately after g_R, so
  phi(e_1)=phi(e_2)=R+1,
with unique entrance x_i.
For a high e_i, the ordinary prefix through g_{R+6}, followed by e_i, gives R+7 edges; all alternatives through a low e_j remain shorter, while a route from u_i along its branch toward e_i must omit the first branch edge containing x_i and has bounded length. Thus
  phi(e_3)=phi(e_4)=R+7,
again with unique entrance x_i.

Choose the same clean source paths, namely the backbone prefixes ending at x_i. Choose P_v to be the full backbone. Choose P_{u_i} to be the backbone prefix through x_i followed by all of B_i. Its length is R+10, it avoids v, and its sole off-u_i contact with e_i is x_i. Hence the four edges are source-clean and terminal-single at both terminals.

Now
  phi(e_i)<phi(v)=R+9<phi(u_i)=R+10
for every i, while the rank tuple remains
  (R+1,R+1,R+7,R+7),
which violates four-edge spacing.

The two common-v contact cells remain C_R and C_{R+6}. This modification does not create a common shorter anchor on which all four e_i are double, so it does not address the genuine common-anchor selected-certificate hypothesis of the repaired target.