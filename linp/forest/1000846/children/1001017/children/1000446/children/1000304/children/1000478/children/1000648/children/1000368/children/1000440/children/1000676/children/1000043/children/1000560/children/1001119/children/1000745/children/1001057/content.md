# A single far-edge contact cannot occur in the middle of a canonical 4445 entrance rail

## Statement

In the 4445 setting, let
  R_b=(h_1,h_2,h_3)
be a canonical three-edge entrance path for
  f_b={b,v,u_b},
so R_b ends at b and avoids v,u_b, and R_b,f_b is a four-edge path ending in f_b through its unique entrance b.

Suppose the rank-five edge e5 meets R_b in exactly one vertex. Then that contact does not lie in h_2.

## Body

Assume the unique contact of e5 with R_b lies in h_2.

The four-edge path
  Q=(h_1,h_2,h_3,f_b)
ends in f_b. Since R_b avoids v and e5 meets f_b at v, the edge e5 meets Q in exactly two path edges: h_2 and the final edge f_b.

Apply the certified two-contact rotation lemma a51a7f9cff95 with p=4 and j=2=p-2. It yields the four-edge linear path
  (h_1,h_2,e5,f_b).

This path ends in f_b and enters f_b through
  e5∩f_b={v}.
But f_b is nonspecial of rank four with unique rank-four entrance b, while v is a terminal distinct from b. Hence no four-edge path ending in f_b can enter through v. Contradiction.

Therefore the unique e5-contact on R_b cannot lie in h_2.