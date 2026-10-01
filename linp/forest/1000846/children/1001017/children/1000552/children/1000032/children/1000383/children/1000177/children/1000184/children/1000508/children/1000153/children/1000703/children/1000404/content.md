# Three critical high entrance rails force a two-vertex overlap

## Statement

In a q,(q+1)^3 charged configuration at a common terminal v, let
   h_i={y_i,v,z_i},  i=1,2,3,
be the three rank-(q+1) high edges, and let Q_i be arbitrary canonical q-edge entrance rails ending at y_i.

Then some pair Q_i,Q_j has at least two distinct common vertices.

## Body

Assume for contradiction that every pair of high rails has at most one common vertex.

By 21dfd53c201f, the low rank-q edge
   e={x,v,u}
meets each Q_i. Every Q_i avoids v, so each such contact lies in {x,u}. With three rails and only two gate vertices, two rails, say Q_1,Q_2, contain a common gate
   w∈{x,u}.
By assumption this is their unique common vertex.

Apply a15746990e9b to Q_1,Q_2. Besides showing that w is an aligned same-index joint, it gives the reciprocal terminal crossings
   z_2∈V(Q_1),   z_1∈V(Q_2).                (1)

Now Q_3 meets h_1 and h_2 by 21dfd53c201f. Since Q_3 avoids v, its h_1-contact is y_1 or z_1, and its h_2-contact is y_2 or z_2.

Using (1):
- y_1 lies on Q_1, while z_1 lies on Q_2;
- y_2 lies on Q_2, while z_2 lies on Q_1.

If the two contacts of Q_3 with h_1,h_2 both land on Q_1, then they are two distinct vertices (the non-v vertex pairs of distinct edges through v are disjoint by linearity), so Q_3 and Q_1 already have at least two common vertices, contradiction. The same holds if both contacts land on Q_2.

Hence one contact lands on Q_1 and the other on Q_2. Therefore Q_3 meets each of Q_1,Q_2. Under the standing assumption, each intersection is unique.

Apply a15746990e9b to Q_1,Q_3. Their unique intersection forces the reciprocal terminal crossing
   z_3∈V(Q_1).
Apply it to Q_2,Q_3. Their unique intersection likewise forces
   z_3∈V(Q_2).

Thus z_3 is a second common vertex of Q_1 and Q_2, distinct from w because h_3 and e are distinct edges through v and hence share no non-v vertex. This contradicts the assumption that Q_1∩Q_2={w}.

Therefore some pair of high entrance rails has at least two distinct common vertices.