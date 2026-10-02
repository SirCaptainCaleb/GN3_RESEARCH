# Every canonical left-entrance rail in 4455 crosses both the middle edge and the far rank-five edge

## Statement

Continue in the surviving 4455 geometry {a,b}, and suppose a is the entrance of its rank-four charged edge
  f_a={a,v,u_a}.
Let
  e5={d,v,w}
be the fixed rank-five charged last edge, with d its unique entrance.

For every canonical three-edge entrance path
  R_a=(h1,h2,h3)
ending at a and avoiding v,u_a:
1. R_a meets g3={a,b,c} at a second vertex, hence contains b or c in h1∪h2;
2. R_a meets e5, hence contains d or w.

Thus every canonical a-ending entrance rail simultaneously crosses the middle edge away from a and the far rank-five edge away from v.

## Body

Part (1) is 3925baec6cf9.

For part (2), suppose R_a is disjoint from e5. By definition of a canonical entrance path,
  (h1,h2,h3,f_a)
is a four-edge linear path ending in f_a through its unique entrance a, and R_a avoids both terminals v,u_a. Hence f_a meets R_a only at a.

The edge e5 meets f_a at the common terminal v. Since R_a avoids v and is assumed disjoint from e5, the concatenation
  (h1,h2,h3,f_a,e5)
is a five-edge linear path ending in e5 and entering e5 through v.

But e5 is nonspecial of rank five and v is a terminal, whereas its unique rank-five entrance is d. Contradiction.

Therefore R_a meets e5. Since it avoids v, the contact is d or w.