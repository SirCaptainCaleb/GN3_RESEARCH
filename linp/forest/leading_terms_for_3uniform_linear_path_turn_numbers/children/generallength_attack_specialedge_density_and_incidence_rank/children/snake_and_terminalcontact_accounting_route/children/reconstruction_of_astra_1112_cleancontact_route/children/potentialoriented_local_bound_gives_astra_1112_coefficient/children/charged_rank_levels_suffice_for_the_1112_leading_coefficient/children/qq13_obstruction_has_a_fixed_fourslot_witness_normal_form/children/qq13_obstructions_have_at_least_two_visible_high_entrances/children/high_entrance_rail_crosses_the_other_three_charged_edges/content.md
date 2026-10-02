# Every visible high entrance rail crosses the other three charged edges

## Statement

In a q,(q+1)^3 charged configuration at terminal v, let h_i be a rank-(q+1) high edge and R_i any canonical q-edge entrance rail for h_i. Then the low rank-q edge e meets one of the final q-2 edges of R_i, and each of the other two rank-(q+1) high edges meets R_i. Thus every visible high entrance yields a q-edge rail simultaneously transversal to all three other charged edges.

## Body


Let e={x,v,u} be an ascending nonspecial edge of rank q with v terminal. Let
  h_1,h_2,h_3
be distinct ascending nonspecial edges of rank q+1, all terminal at v.

Fix i and suppose the entrance y_i of h_i is under consideration. Let
  R_i=(r_1,...,r_q)
be a canonical q-edge entrance path ending physically at y_i and avoiding the two terminals v,z_i of h_i, so R_i,h_i is a longest (q+1)-edge path ending in h_i through y_i and may be ordered with physical last vertex v.

First, e meets the final q-2 precursor edges of R_i. Apply the terminal tail-blocker lemma c0798e59ef02 to the rank-q nonspecial edge e, terminal v, against the snake-incoming last edge h_i of rank q+1. Therefore e meets one of
  r_3,...,r_q.
Since R_i avoids v, this contact is x or u.

Second, each other high edge h_j (j!=i) meets R_i. If h_j were disjoint from R_i, then
  R_i,h_i,h_j
would be a linear path of length q+2: h_i and h_j meet exactly at v, while R_i avoids v and is disjoint from h_j by assumption. This exceeds phi(h_j)=q+1, contradiction. Hence h_j intersects R_i.

Thus R_i simultaneously meets:
- the low edge e, in its final q-2 rail edges;
- h_j for each j!=i.

In particular, in a q,(q+1)^3 configuration every canonical entrance rail of every visible high edge is a three-target transversal for the other charged edges. If at least two high entrances are visible, there are at least two such mutually constrained rails.
