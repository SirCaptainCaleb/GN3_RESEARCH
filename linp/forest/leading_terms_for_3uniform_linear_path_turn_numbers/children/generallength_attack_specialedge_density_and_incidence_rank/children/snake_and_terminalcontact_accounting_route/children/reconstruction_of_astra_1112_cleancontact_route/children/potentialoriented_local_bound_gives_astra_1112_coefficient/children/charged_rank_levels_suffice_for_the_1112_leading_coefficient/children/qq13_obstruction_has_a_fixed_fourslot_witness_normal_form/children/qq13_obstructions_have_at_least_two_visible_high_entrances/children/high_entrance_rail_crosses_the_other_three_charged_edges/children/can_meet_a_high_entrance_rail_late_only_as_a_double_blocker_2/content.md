# A competing high edge can meet a high entrance rail late only as a double blocker

## Statement

Let h_i={y_i,v,z_i} and h_j={y_j,v,z_j} be distinct ascending nonspecial edges of rank q+1 through the common terminal v, with phi(y_i)=phi(y_j)=q. Let Q_i=(r_1,...,r_q) be a canonical q-edge entrance path ending at y_i and avoiding v,z_i.

Assume h_j meets V(Q_i) in exactly one vertex w, and let k be the last path-edge index containing w. Then k<=q-2. Equivalently, a one-contact competing high edge cannot meet either of the final two edges r_{q-1},r_q of Q_i.

## Body

Suppose h_j has exactly one contact w with Q_i, and let k be the last path-edge index containing w.

Consider
  r_1,...,r_k,h_j,h_i.

Because h_j has no other contact with Q_i, it meets the retained prefix only at w. The edges h_j and h_i meet exactly at v by linearity. The path Q_i avoids v and z_i, while y_i is a last vertex of r_q; in particular y_i is not in h_j because h_j and h_i already share v. Thus the displayed sequence is linear.

Its length is k+2. Its last edge is h_i. The predecessor h_j meets h_i at v, so the entrance y_i is a last vertex of the displayed path.

Since phi(y_i)=q,
  k+2<=q,
hence
  k<=q-2.

Thus any competing rank-(q+1) high edge that reaches the final two cells of Q_i must do so with at least two contacts on Q_i.