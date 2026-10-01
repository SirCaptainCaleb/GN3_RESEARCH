# At the odd central boundary a four-single obstruction cannot occupy the right-private slot

## Statement

Let v have phi(v)=2q-3, q>=4, and suppose four assigned potential-charged ascending edges of ranks in {q,q+1} are all single-contact on a fixed maximum v-path P. In the seven-slot notation
 A,J_{q-3}; B,P_{q-2}; C,J_{q-2}; D,P_{q-1}; E,J_{q-1}; F,P_q; G,J_q,
the right-private slot F=private(g_q) cannot be occupied.

Together with 8d1adea102fe, every four-single odd-central obstruction is confined to the five slots A,B,C,D,E.

## Body

Assume F is occupied. By a01ddfa76dc8, F is entrance-only, hence it is the unique entrance of a rank-(q+1) edge h_F and phi(F)=q. By 08f894b8cb5e, the clean private entrance at F forbids a private single contact two path positions earlier, so B is unoccupied. By 8d1adea102fe, G is unoccupied.

Thus the other three contacts are chosen from A,C,D,E.

If both A and C are occupied, let h_A,h_C be their two star edges through v. Then
  g_1,...,g_{q-3},h_A,h_C,g_{q-1},g_q
is linear: h_A meets the prefix only at A; h_A,h_C meet at v; h_C meets g_{q-1} at C; the omitted edge g_{q-2} separates the inherited path pieces; and both star edges are single-contact. The path has
  (q-3)+2+2=q+1
edges and ends in g_q. Its predecessor g_{q-1} meets g_q at E, so the private vertex F is a last vertex. Hence phi(F)>=q+1, contradicting phi(F)=q.

Therefore A and C cannot both be occupied. Since three of A,C,D,E must be occupied, the only possible sets are {A,D,E} and {C,D,E}.

In the first case,
  g_1,...,g_{q-3},h_A,h_D,g_{q-1},g_q
is linear and has q+1 edges. Indeed h_A meets the prefix at A, h_A,h_D meet at v, h_D meets g_{q-1} at D, and all other P-contacts are excluded by single-contact. Again F is a last vertex, contradiction.

In the second case,
  g_1,...,g_{q-2},h_C,h_E,g_q
is linear and has
  (q-2)+2+1=q+1
edges. Here h_C meets the prefix at C, h_C,h_E meet at v, and h_E meets g_q at E. The final edge g_q is entered through E, leaving F as a last vertex. Again phi(F)>=q+1, contradiction.

Thus F cannot be occupied.
