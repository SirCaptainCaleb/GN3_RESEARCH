# A whole chord is endpoint-slack-shallow or its clean source rail reintersects the opposite side

## Statement

Let e={x,v,u} be an ascending nonspecial edge of rank r, with unique entrance x, and let
  S=(s_1,...,s_{r-1})
be a maximum source path ending at x such that S,e is a longest r-edge path ending in e through x and S avoids u,v.

Let R be any linear path avoiding v and containing both x and u. Let a be the endpoint of R lying on the side of u opposite x in the path order, and let T be the R-segment from u to a. Write t=|T| for its number of edges.

Then either

(A) t <= phi(a)-r,

or

(B) S meets V(T).

Every intersection in (B) is a common vertex of S and R distinct from x (and from u), so S and R have at least two distinct common vertices.

In particular, if R=(g_1,...,g_L) is a maximum endpoint path ending at y with phi(y)=L, and x occurs before u toward y, then a=y and
  t <= L-r
unless the clean source rail reintersects the u-to-y suffix.

For the precursor of a rank-q ascending anchor path this specializes to
  t <= q-r-1
in the unobstructed forward orientation.

## Body

The R-side T contains u but, by definition of the side opposite x, contains neither x nor v. By source cleanness, S avoids u and v.

Suppose branch (B) fails. Then S is vertex-disjoint from T. Concatenate S, then e through x to u, then T from u to a. This is a linear path: S meets e only at x; e meets T only at u because x,v are absent from T; and S has no vertex on T by assumption. Its length is
  (r-1)+1+t=r+t
and it ends at a. Therefore
  r+t <= phi(a),
which is exactly
  t <= phi(a)-r.

If branch (B) holds, a common vertex z of S with T is distinct from x because x is on the other R-side, and distinct from u because S avoids u. Hence x and z are two distinct common vertices of S and R.

No terminal-single, paid-cell, minimum-terminal, terminal-rank, or maximality hypothesis on R is needed for the general dichotomy. The displayed anchor specialization uses only that the relevant endpoint y of the anchor precursor has phi(y)=q-1.
