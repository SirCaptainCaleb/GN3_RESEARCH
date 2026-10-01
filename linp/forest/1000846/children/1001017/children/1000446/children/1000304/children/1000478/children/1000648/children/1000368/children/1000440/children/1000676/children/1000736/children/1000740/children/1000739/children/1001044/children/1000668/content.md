# In the 4455 low-low witness geometry the second rank-five edge either enters privately through g4 or has two precursor contacts

## Statement

Assume the p=5 charged pattern (4,4,5,5) and the {b,c} witness geometry of e6eec0f670ed. Thus
  P=(g1,g2,g3,g4,e5)
ends at v,
  g3={a,b,c},
where b,c are the unique entrances of the two rank-four charged edges and phi(b)=phi(c)=3.

Let
  h={x,v,u}
be the other rank-five charged edge, with unique entrance x and phi(x)=4.

Then h is disjoint from g3. Moreover h meets g2∪g4. If h has exactly one contact with g2∪g3∪g4, then that contact lies in g4, is x, and x is the private vertex of g4.

Equivalently, every other case forces h to have contacts with both g2 and g4.

## Body

Because h and each rank-four charged edge share v, linearity forbids h from containing b or c. If h contained a, then the endpoint-chord lemma a570c0ad0001 applied to P at i=2 would give phi(c)>=4, contradicting phi(c)=3. Hence h∩g_3 is empty.

Apply the terminal-tail blocker lemma to h, which has rank five, against the five-edge path P ending at the common terminal v. Since h≠e_5, one of its non-v vertices x,u occurs in the final three precursor edges g_2,g_3,g_4. As h is disjoint from g_3, h meets g_2 or g_4.

Assume now that h has exactly one contact with g_2∪g_3∪g_4.

It cannot lie in g_2. In that case h is disjoint from g_4, and
  (g_2,h,e_5,g_4)
is a four-edge linear path: consecutive intersections are the unique g_2-contact, then v=h∩e_5, then d=e_5∩g_4; the nonconsecutive pairs g_2,e_5 and g_2,g_4 are disjoint in P, and h,g_4 are disjoint by the assumed unique central contact. The last edge is g_4, entered through d. The distinct vertex c=g_3∩g_4 is absent from the preceding edges, so it can be the last vertex. Hence phi(c)>=4, contradicting phi(c)=3.

Thus the unique contact lies in g_4. Suppose it is the terminal u rather than the entrance x. Then x is absent from g_2∪g_3∪g_4 and cannot lie in e_5 because h and e_5 already share v. If x lay in g_1, the position-sensitive potential bound on the five-edge path P, together with phi(x)=4, would force x=g_1∩g_2 (a private vertex of g_1 has potential at least five). But then h would also meet g_2, contradicting uniqueness of the central contact. Hence x is absent from P. Therefore h is disjoint from g_1,g_2,g_3 and meets g_4 only at u, so
  (g_1,g_2,g_3,g_4,h)
is a five-edge linear path ending in h through the terminal u. This contradicts that the nonspecial rank-five edge h has unique rank-five entrance x.

Consequently the unique g_4-contact is x. Finally x cannot be either joint of g_4: x≠c because h is disjoint from g_3, and x≠d=g_4∩e_5 because h and e_5 already share v. Thus x is the private vertex of g_4.