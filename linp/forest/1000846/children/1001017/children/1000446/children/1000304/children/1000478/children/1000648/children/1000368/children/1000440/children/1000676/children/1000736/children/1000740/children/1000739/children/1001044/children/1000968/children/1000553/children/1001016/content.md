# The final 4455 witness geometry splits into a high-c branch or a forced two-contact entrance rail

## Statement

Assume the p=5 charged pattern (4,4,5,5) in its sole surviving witness geometry {a,b}, with
  P=(g_1,g_2,g_3,g_4,e_5),
  a=g_2∩g_3,
  b private in g_3,
  c=g_3∩g_4.
Let f_a be the rank-four charged edge whose selected path-relative witness is a, and let f_b be the rank-four charged edge with entrance b.

Then exactly one of the following holds.

(T) a is the opposite terminal of f_a. In this case the unique entrance x_a of f_a is off V(P), and
  phi(c)>=5.

(E) a is the unique entrance of f_a. Then phi(a)=3, and every canonical three-edge entrance path
  R_a=(h_1,h_2,h_3)
ending at a and avoiding the two terminals of f_a must meet g_3 in a second vertex besides a. Equivalently, every such R_a contains b or c.

## Body

The witness a is either the unique entrance of f_a or its opposite terminal.

Suppose first that a is the opposite terminal. Since the path-relative selected witness is a rather than the entrance, the unique entrance x_a is absent from the fixed path P. Write
  f_a={x_a,v,a}.
Then f_a meets g_2 exactly at a, meets e_5 exactly at v, and is disjoint from g_1 and g_4: x_a is off P, a lies only in g_2,g_3 on P, and v lies only in e_5. Therefore
  (g_1,g_2,f_a,e_5,g_4)
is a five-edge linear path. Its last edge g_4 is entered through d=e_5∩g_4. The distinct vertex c=g_3∩g_4 can be chosen as physical last vertex. Hence phi(c)>=5. This proves (T).

Now suppose a is the unique entrance. Since f_a has rank four and is ascending,
  phi(a)=3.
Let R_a=(h_1,h_2,h_3) be any canonical three-edge entrance precursor ending physically at a and avoiding the two terminals of f_a.

If R_a met g_3 only at a, then
  (h_1,h_2,h_3,g_3)
would be a four-edge linear path: the final consecutive intersection is a, and g_3 has no other R_a-contact by assumption. The last edge g_3 is entered through a, while b is a distinct vertex of g_3, so b can be chosen as physical last vertex. This would give phi(b)>=4, contradicting the known phi(b)=3. Therefore R_a has an additional contact with g_3, necessarily at b or c. This proves (E).
