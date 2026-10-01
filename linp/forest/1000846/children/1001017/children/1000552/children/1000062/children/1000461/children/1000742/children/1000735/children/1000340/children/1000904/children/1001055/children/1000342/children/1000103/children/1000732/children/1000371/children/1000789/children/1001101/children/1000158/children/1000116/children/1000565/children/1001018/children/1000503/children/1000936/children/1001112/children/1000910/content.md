# A unique selected-common-path intersection with the same-terminal cycle neighbor is exactly the reciprocal terminal

## Statement

Retain the hard unique-intersection residual of d0a41dede20a for
  e={x,v,u},
and let f be the fundamental-cycle neighbor of e that shares terminal v. Let R_e and R_f be canonical maximum source paths for e and f. Let A be the selected common-path precursor at terminal v, so both x and u lie on A.

Assume
  V(R_e) intersect V(R_f)={s}.
Then u belongs to V(R_f) intersect V(A).

Consequently, if
  |V(R_f) intersect V(A)|=1,
then
  V(R_f) intersect V(A)={u}.
Moreover u is an internal joint on both maximum endpoint paths R_f and A at the same path index.

Thus, in the unique-intersection branch, the second gate of R_f against the selected common path is canonically labeled by the reciprocal terminal u; it is not an unspecified return vertex.

## Body

Because R_e and R_f have exactly one common vertex and f is the fundamental-cycle neighbor sharing terminal v, f4f2089110b2 applies and gives
  u in V(R_f)
and
  x notin V(R_f).

By the selected whole-contact certificate for e at v, both non-v vertices x and u lie on the common precursor A. Hence
  u in V(R_f) intersect V(A).

If this intersection contains only one vertex, it must therefore be exactly u.

The paths R_f and A are maximum endpoint paths with distinct last vertices. Applying the certified unique-intersection theorem 5854d853a44b to their unique common vertex u shows that u is an internal joint on both paths and occurs at the same joint index.
