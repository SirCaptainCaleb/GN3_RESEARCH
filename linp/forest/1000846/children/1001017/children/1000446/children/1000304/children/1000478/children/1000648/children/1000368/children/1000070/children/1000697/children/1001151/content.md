# At potential four, a rank-three charged edge is pinned by its entrance

## Statement

Let v satisfy phi(v)=4 and let P=(g_1,g_2,g_3,g_4) be a maximum four-edge path ending at v. If e={x,v,u} is a potential-charged ascending nonspecial edge of rank 3 with phi(u)>=4, then x=g_2∩g_3. In particular the unique central witness is the entrance, not the opposite terminal, and phi(g_2∩g_3)=2.

## Body

By a02e06077f82, the path-relative witness for a rank-3 charged edge at v has only one possible slot, namely the middle joint w=g_2∩g_3.

Suppose first that x lies on P. By the witness convention the chosen witness is x, hence x=w, and ascendingness gives phi(x)=phi(e)-1=2.

It remains to exclude the alternative that x is absent from P and the chosen witness is u=w. Since w=g_2∩g_3, the sequence (g_1,g_2,e) is a linear three-edge path: g_2 meets e at u=w; g_1 is disjoint from e because x is absent, v lies only in the last path edge g_4, and the third vertex of e cannot lie on g_1 without becoming another P-contact and violating the witness localization/prefix argument. More directly, this is exactly the prefix used in the proof of 220a14637b5f when a terminal witness is the joint after g_2.

This path has length 3=phi(e) and enters e through the terminal u, whereas e is nonspecial with unique longest-path entrance x. That is impossible. Therefore x cannot be absent, so x=w=g_2∩g_3 and phi(w)=2.

Thus the rank pattern (3,4,4,4) at p=4 has a completely pinned low-rank edge: its unique entrance is the middle joint of every chosen maximum v-ending path to which the central-window argument is applied.
