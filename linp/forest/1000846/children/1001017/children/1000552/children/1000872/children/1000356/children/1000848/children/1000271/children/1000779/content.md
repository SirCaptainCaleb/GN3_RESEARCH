# Four mutually blocking high entrance rails force a two-vertex overlap

## Statement

Let h_i={y_i,v,z_i}, i=1,2,3,4, be four rank-(q+1) ascending nonspecial edges through one common terminal v, with phi(y_i)=q, and let Q_i be canonical q-edge entrance rails. Then some pair Q_i,Q_j has at least two distinct common vertices. The proof uses foreign-edge transversality, a pigeonhole on one target edge, and repeated unique-intersection alignment.

## Body

Let
  h_i={y_i,v,z_i}, i=1,2,3,4,
be four distinct ascending nonspecial edges of the same rank q+1 through common terminal v, with phi(y_i)=q. For each i let
  Q_i
be a canonical q-edge entrance rail ending physically at y_i and avoiding v,z_i.

By terminal adjacency 94c19ac52776, every Q_i meets every foreign high edge h_j, j!=i: if Q_i were disjoint from h_j, then Q_i,h_i,h_j would be a (q+2)-edge path ending in h_j, exceeding phi(h_j)=q+1.

Assume for contradiction that every pair of rails has at most one common vertex.

Look at h_1. Each of Q_2,Q_3,Q_4 meets h_1, and since these rails avoid v, each contact is one of the two vertices y_1,z_1. By pigeonhole, two rails, say Q_2,Q_3, contain the same vertex
  w in {y_1,z_1}.
Thus Q_2,Q_3 intersect. Under the standing assumption,
  V(Q_2) cap V(Q_3)={w}.

Apply the unique-intersection alignment theorem a15746990e9b to Q_2,Q_3. Besides aligning w as a same-index joint, its high-rail conclusion gives reciprocal terminal crossings
  z_3 in V(Q_2),
  z_2 in V(Q_3).                                      (1)

Now Q_4 meets h_2 and h_3. Its h_2-contact is y_2 or z_2; here y_2 lies on Q_2 while z_2 lies on Q_3 by (1). Likewise its h_3-contact is y_3 or z_3; y_3 lies on Q_3 while z_3 lies on Q_2.

If both Q_4 contacts land on Q_2, then they are distinct vertices because h_2,h_3 share only v, so Q_4 and Q_2 have at least two common vertices, contradiction. The same if both land on Q_3.

Hence one contact lies on Q_2 and the other on Q_3. Therefore Q_4 meets each of Q_2,Q_3. By the standing assumption each intersection is unique.

Apply a15746990e9b to Q_2,Q_4. It forces
  z_4 in V(Q_2).
Apply it to Q_3,Q_4. It forces
  z_4 in V(Q_3).

Thus z_4 is a common vertex of Q_2,Q_3 in addition to w. These vertices are distinct: w lies in h_1 while z_4 lies in h_4, and distinct star edges h_1,h_4 through v have disjoint non-v pairs by linearity. Contradiction.

Therefore some pair Q_i,Q_j has at least two distinct common vertices.
