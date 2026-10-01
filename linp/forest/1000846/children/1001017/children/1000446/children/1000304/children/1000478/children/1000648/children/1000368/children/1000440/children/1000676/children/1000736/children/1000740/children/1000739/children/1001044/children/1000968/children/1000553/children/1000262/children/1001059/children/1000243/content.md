# Every canonical left-entrance rail in the surviving 4455 branch also crosses the opposite rank-four edge

## Statement

Continue in the surviving p=5 pattern 4455, entrance-a branch. Thus
  g_3={a,b,c},
  f_a={a,v,u_a},
  f_b={b,v,u_b},
where f_a,f_b are rank-four charged ascending nonspecial edges with unique entrances a,b and
  phi(a)=phi(b)=3.

Let
  R_a=(h_1,h_2,h_3)
be any canonical three-edge entrance path ending at a such that R_a,f_a is a four-edge path ending in f_a through a and R_a avoids v,u_a.

Then R_a meets f_b. Since R_a avoids v, it contains b or u_b.

Together with 3925baec6cf9 and ebd9e72015cd, every canonical R_a therefore simultaneously:
- contains b or c, as a second contact with g_3;
- contains d or w, as a contact with e_5;
- contains b or u_b, as a contact with f_b.

In particular, if R_a avoids b (so its extra g_3-contact is c), then R_a necessarily contains u_b.

## Body

The three edges f_a,g_3,f_b are pairwise distinct and satisfy
  f_a∩g_3={a},
  g_3∩f_b={b},
  f_a∩f_b={v},
by linearity. Hence they form a linear 3-cycle.

Suppose R_a were disjoint from f_b. By the canonical entrance-path definition,
  (h_1,h_2,h_3,f_a)
is a four-edge linear path and R_a avoids both terminals v,u_a of f_a. Thus f_a meets R_a only at a.

Since f_a∩f_b={v} and R_a is assumed disjoint from f_b, the concatenation
  (h_1,h_2,h_3,f_a,f_b)
is a five-edge linear path.

But f_b has edge rank four. This is impossible; equivalently it is a five-edge path ending in f_b through terminal v rather than its unique rank-four entrance b.

Therefore R_a meets f_b. As v∉V(R_a) and f_b={b,v,u_b}, the contact lies in {b,u_b}.

The remaining assertions are the already proved middle-edge and far-edge transversal statements. If R_a avoids b, its mandatory f_b-contact must be u_b.
