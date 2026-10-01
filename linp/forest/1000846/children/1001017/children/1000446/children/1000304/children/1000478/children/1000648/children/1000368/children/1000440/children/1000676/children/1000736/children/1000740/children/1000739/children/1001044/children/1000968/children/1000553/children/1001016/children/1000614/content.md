# A unique far-edge contact on a canonical entrance-a rail in 4455 is forced to the last rail edge

## Statement

In branch (E) of e277460104ac, let
  R_a=(h1,h2,h3)
be a canonical three-edge entrance path ending at a for
  f_a={a,v,u_a},
and let e5={d,v,w} be the fixed rank-five charged edge.

If e5 meets R_a in exactly one vertex, then that contact lies in h3.

## Body

By 2b9e6edca5bd, a unique e5-contact cannot lie in h2.

Suppose instead that the unique e5-contact lies in h1. Then e5 is disjoint from h2,h3. Since R_a,f_a is canonical, f_a meets R_a only at a∈h3, so f_a is disjoint from h1,h2. Also e5∩f_a={v}.

Therefore
  (h2,h1,e5,f_a)
is a four-edge linear path. It ends in the nonspecial rank-four edge f_a, and its predecessor e5 meets f_a at v. Thus the path enters f_a through v, a terminal rather than its unique rank-four entrance a. Contradiction.

Hence the unique contact is neither h1 nor h2, and therefore lies in h3.