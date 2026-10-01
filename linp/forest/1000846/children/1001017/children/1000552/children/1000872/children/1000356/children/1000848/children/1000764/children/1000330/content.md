# At the odd central boundary four single contacts cannot occupy both rightmost slots

## Statement

Let v have p=phi(v)=2q-3 with q>=4, and fix a maximum p-edge path P=(g_1,...,g_p) ending at v. Suppose four assigned potential-charged ascending edges of ranks in {q,q+1} are all single-contact relative to P.

Write the seven rank-(q+1) central slots as
 A=g_{q-3}∩g_{q-2},
 B=private(g_{q-2}),
 C=g_{q-2}∩g_{q-1},
 D=private(g_{q-1}),
 E=g_{q-1}∩g_q,
 F=private(g_q),
 G=g_q∩g_{q+1}.

Then F and G cannot both be occupied by the four single contacts.

## Body

By a01ddfa76dc8, terminal-only rank-(q+1) singles cannot occupy F or G, and rank-q edges have no witness in F or G. Hence if F and G are occupied, both contacts are visible unique entrances of rank-(q+1) edges. Write their edges h_F={F,v,z_F} and h_G={G,v,z_G}. Then phi(F)=phi(G)=q.

Because G is a clean joint entrance at g_q∩g_{q+1}, eac2e3da3eea forbids any other single contact whose first-contact cell is q-1. Thus D and E are unoccupied.

Because F is a clean private entrance on g_q, 08f894b8cb5e forbids a private single contact two path positions earlier, so B is unoccupied.

Therefore the other two contacts must occupy A and C.

If C were a visible entrance, then C is the clean joint g_{q-2}∩g_{q-1}; applying eac2e3da3eea would forbid first-contact cell q-3, hence forbid A. Therefore C must be terminal-only. Let e_C={x_C,v,C}, where x_C is its entrance and x_C is absent from P. Since the incidence at C is single-contact, the third vertex besides v,C is also absent from P.

Now consider
  g_1,...,g_{q-2}, e_C, h_F, g_q.

This is linear. The prefix meets e_C only at C on its final edge g_{q-2}; e_C and h_F meet exactly at v; h_F meets g_q only at F; h_F has no other P-contact; and g_q is disjoint from the prefix because g_{q-1} is omitted.

Its length is
  (q-2)+3=q+1.

Its final edge is g_q. Since its predecessor h_F meets g_q at the private vertex F, and g_{q+1} is omitted, the joint
  G=g_q∩g_{q+1}
is a last vertex. Hence phi(G)>=q+1.

But G is the entrance of h_G, whose rank is q+1, so phi(G)=q. Contradiction.
