# Clean single contacts avoid the first and penultimate rail edges

## Statement

Let e={x,v,u} be ascending nonspecial of rank q with canonical entrance rail R=(r_1,...,r_{q-1}). If a distinct edge through the same terminal meets R in exactly one private contact on r_j, then j≠1 and j≠q-2; moreover no two such occupied positions differ by two. The previously claimed exclusion of j=q-1 is not justified by the available splice, so that last-edge case remains open.

## Body

Let e={x,v,u} be ascending nonspecial of rank q with unique entrance x and terminal v, and let
  R=(r_1,...,r_{q-1})
be a canonical entrance path ending at x and avoiding v,u.

Let h be a distinct edge through v which meets R in exactly one path edge r_j and exactly one vertex w. Then w is private in r_j. Because h and e already share v, h cannot contain x.

First, j≠1. If j=1, then
  h,r_1,r_2,...,r_{q-1}
is a q-edge linear path ending at x: h meets R only in its private r_1-contact and x is absent from h. This contradicts phi(x)=q-1.

Second, j≠q-2. If j=q-2, then
  r_1,...,r_{q-2},h,e
is a q-edge linear path. The edge h meets the prefix only at its private r_{q-2}-contact, h∩e={v}, and e meets R only at x in the omitted final rail edge r_{q-1}. Thus this is a longest rank-q path ending in e through the terminal v, contradicting nonspeciality of e.

The same splice does not exclude j=q-1. In that case the tempting sequence r_1,...,r_{q-1},h,e is not linear, because the nonconsecutive edges r_{q-1} and e still meet at x. Hence the last-edge contact remains an unresolved case.

Therefore the unconditional positional conclusion is
  j in {2,...,q-3} union {q-1}.

Distinct edges through v have disjoint non-v pairs, and each rail edge has a unique private vertex, so at most one clean single-contact competitor occupies any given private position. Together with 990186a1aaa6, no two occupied clean positions differ by two.
