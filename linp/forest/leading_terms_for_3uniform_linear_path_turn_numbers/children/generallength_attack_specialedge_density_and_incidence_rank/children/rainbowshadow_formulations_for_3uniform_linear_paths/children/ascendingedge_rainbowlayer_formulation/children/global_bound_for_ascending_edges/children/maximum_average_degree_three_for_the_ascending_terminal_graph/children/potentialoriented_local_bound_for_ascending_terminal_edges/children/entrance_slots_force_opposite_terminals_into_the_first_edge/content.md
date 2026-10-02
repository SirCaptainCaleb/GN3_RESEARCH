# Middle entrance slots force opposite terminals into the first edge

## Statement

In the pure p=4 obstruction, fix P=(g_1,g_2,g_3,f_4) as in f9e64ea63be0. If another charged rank-four edge f={a,v,b} has visible entrance a equal either the private vertex of g_2 or the middle joint g_2∩g_3, then b is a private vertex of g_1.

## Body

Write f={a,v,b}, with phi(a)=3 and phi(b)>=4.

First suppose a is the private vertex of g_2. The opposite terminal b cannot lie in g_2, since f and g_2 already meet at a. It cannot lie in f_4, since f and f_4 already meet at v.

If b were absent from P, then f would meet P exactly in g_2 and f_4. This is forbidden by the certified two-contact competitor lemma 0a5cb0d55cbd: for p=q=4 a sole precursor contact cannot be g_2.

If b were the middle joint g_2∩g_3, then f and g_2 would share both a and b, violating linearity. If b were private to g_3, then
g_1,g_2,f,f_4
would be a four-edge linear path ending in f_4 through v, contradicting the unique entrance of f_4. If b were the first joint g_1∩g_2, then f and g_2 would again share two vertices. The last joint g_3∩f_4 is impossible because f and f_4 already share v.

Therefore b lies in g_1 but not in g_2, i.e. b is private to g_1.

Now suppose a=g_2∩g_3. Then f meets both g_2 and g_3 at the single vertex a. By linearity b lies in neither g_2 nor g_3, and again b cannot lie in f_4.

If b were absent from P, then
g_1,g_2,f,f_4
would be a four-edge linear path ending in f_4 through v: g_1 is disjoint from f, g_2 meets f at a, and f meets f_4 at v. This contradicts nonspecialness of f_4. Hence b lies on P.

The only remaining path edge is g_1. It cannot be the joint g_1∩g_2, because then f and g_2 would share that joint together with a. Thus b is private to g_1.

So in either entrance position the opposite charged terminal is forced to a private vertex of the first edge.