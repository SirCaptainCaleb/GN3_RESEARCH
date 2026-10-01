# The G-only odd-central four-single state is an exact loss-one normal form

## Statement

In the odd-central state p=phi(v)=2q-3, suppose four assigned charged edges of ranks {q,q+1} are all single-contact on a fixed maximum v-path P, and suppose the right joint
  G=g_q∩g_{q+1}
is occupied while the right private slot F=private(g_q) is not.

Then the four occupied slots are exactly
  A=g_{q-3}∩g_{q-2},
  B=private(g_{q-2}),
  C=g_{q-2}∩g_{q-1},
  G=g_q∩g_{q+1}.
Moreover:
(1) G is the visible entrance of a rank-(q+1) edge h_G and phi(G)=q;
(2) C is terminal-only;
(3) the A- and B-edges have rank q+1;
(4) writing e_C for the C-edge, the sequence
    g_1,...,g_{q-2},e_C,h_G
    is a q-edge path ending in h_G through the wrong terminal v, hence an exact loss-one wrong-entrance state for h_G.

If either A or B is also terminal-only, its two-sided terminal-only spacing with C is attained at equality.

## Body

Since G is occupied, it is entrance-only by a01ddfa76dc8, and eac2e3da3eea applied to the clean joint entrance G forbids the first-contact cell q-1. Hence D=private(g_{q-1}) and E=g_{q-1}∩g_q are unoccupied.

We are assuming F is unoccupied. Four distinct contacts must therefore occupy all of A,B,C,G.

If C were a visible entrance, then C=g_{q-2}∩g_{q-1} and eac2e3da3eea would forbid the first-contact cell q-3, namely A. Thus C is terminal-only.

A and B cannot support rank-q edges: at p=2q-3 the rank-q witness window is exactly {C,D,E}. Hence the A- and B-edges have rank q+1. G likewise has rank q+1 and, being a visible entrance, satisfies phi(G)=q.

Let e_C={x_C,v,C}, with x_C absent from P, and h_G={G,v,z_G}. Since both incidences are single-contact, e_C has no other P-contact and h_G has no other P-contact besides G. Thus
  g_1,...,g_{q-2},e_C,h_G
is linear. Its length is q, it ends in h_G through terminal v, and G is a last vertex. Since h_G has rank q+1 and unique entrance G, this is exactly one edge short of a contradictory wrong-entrance witness.

Finally suppose A is terminal-only. Its rank is q+1. Its first occurrence is q-3 and C's first occurrence is q-2, so df8ad4c65be0 gives q-3<=q_C-3; when q_C=q this is equality, and when q_C=q+1 the inequality has one unit slack. In last coordinates A has last q-2 and C last q-1; f0c177137b7f gives q-1>=p-(q+1)+3=q-1, equality. If B is terminal-only, its last occurrence q-2 and C's last q-1 similarly give equality in f0c177137b7f. Thus every additional terminal-only contact is pinned at the extremal loss-one spacing permitted by the two-sided inequalities.