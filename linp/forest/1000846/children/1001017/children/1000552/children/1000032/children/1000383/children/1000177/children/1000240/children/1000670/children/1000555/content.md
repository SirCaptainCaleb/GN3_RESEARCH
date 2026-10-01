# Every one-rank-higher terminal competitor crosses the low entrance rail

## Statement

Let e={x,v,u} be ascending nonspecial of rank q with unique entrance x and terminal v. For every canonical (q-1)-edge entrance path R ending at x with R,e a longest q-edge path, every nonspecial rank-(q+1) edge h through v for which v is terminal must meet R. Otherwise R,e,h is a longest (q+1)-edge path entering h through terminal v, contradicting the unique entrance of h.

## Body

Let e={x,v,u} be ascending nonspecial of rank q with unique entrance x and terminal v. Let
  R=(r_1,...,r_{q-1})
be a canonical entrance path ending physically at x and avoiding v,u, so
  R,e
is a q-edge longest path ending in e through x.

Let h={a,v,w} be a distinct nonspecial edge of rank q+1 for which v is also terminal. Suppose for contradiction that h is disjoint from V(R).

By linearity e and h share exactly v. Since R avoids v,u and ends at x, and h is disjoint from R, the sequence
  R,e,h
is a linear path of length q+1 ending in h. Its entrance into h is the common vertex v=e∩h.

But phi(h)=q+1, so this is a longest path ending in h. Thus v is a longest-path entrance label of h. Since h is nonspecial and v is assumed terminal, its unique entrance is a different vertex a, contradiction.

Therefore every rank-(q+1) nonspecial edge h through terminal v must meet the canonical low-rank entrance rail R.

The same argument is path-universal: it applies to every canonical entrance path R for e.
