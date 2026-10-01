# Absent entrances in the pure p=4 obstruction are pinned to the first joint

## Statement

Let phi(v)=4 and let f_1,f_2,f_3,f_4 be four rank-four potential-charged ascending nonspecial edges through v. Fix a longest path P=(g_1,g_2,g_3,f_4) ending in f_4 with last vertex v. For i∈{1,2,3}, if the unique entrance a_i of f_i is absent from P, then the opposite terminal b_i equals the first joint g_1∩g_2. Consequently at most one of f_1,f_2,f_3 can have its entrance absent from P.

## Body

Write f_i={a_i,v,b_i}, where a_i is the unique entrance, so phi(a_i)=3, and b_i is the opposite terminal with phi(b_i)>=4.

Assume a_i is absent from P. Since f_i and f_4 share the terminal v and both have rank four, f_i must have another contact with P; otherwise P,f_i would extend beyond length four. Because a_i is absent, every precursor contact is through b_i.

The central-window localization places b_i among the five possible central positions
g_1∩g_2, private(g_2), g_2∩g_3, private(g_3), g_3∩f_4.
The last joint g_3∩f_4 is impossible: f_i already meets f_4 at v, so sharing that joint would violate linearity.

If b_i is private to g_2, then f_i meets P exactly in g_2 and f_4. The certified two-contact competitor lemma 0a5cb0d55cbd with p=q=4 forbids this: a sole precursor contact must lie in g_1 or g_3, not g_2.

If b_i is private to g_3, then
g_1,g_2,g_3,f_i
is a four-edge linear path ending in f_i through entrance label b_i. Since b_i is a terminal rather than the unique entrance a_i, this contradicts nonspecialness of f_i.

If b_i=g_2∩g_3, then
g_1,g_2,f_i,f_4
is a four-edge linear path ending in f_4 through the label v. Indeed f_i meets g_2 at b_i and f_4 at v, while g_1 is disjoint from f_i and f_4 and g_2 is disjoint from f_4. This contradicts nonspecialness of f_4, whose unique entrance is g_3∩f_4.

Thus the only remaining possibility is
b_i=g_1∩g_2.

Finally distinct f_i through v have disjoint non-v pairs by linearity. Hence two different edges cannot both use the same vertex g_1∩g_2 as opposite terminal. Therefore at most one of f_1,f_2,f_3 has entrance absent from P.