# Strict-rise high terminals have reciprocal central entrance structure

## Statement

Let h={y,v,z} be ascending nonspecial of rank q+1 with phi(y)=q, phi(v)=2q-2, and phi(z)>=2q-2. Then phi(z)<=2q. If phi(z)=2q, every maximum 2q-edge path ending at z contains y, necessarily at its unique central joint. If phi(z)=2q-1, then on every maximum z-path either y lies in one of the three central slots, or y is absent and v is forced to be the unique central joint r_{q-1}∩r_q. Thus every strict-rise charged terminal has a reciprocal central-gate normal form.

## Body

Let h={y,v,z} be ascending nonspecial of rank q+1, with unique entrance y and
  phi(y)=q,
  phi(v)=2q-2,
  phi(z)>=2q-2.
By the certified terminal-potential bound a7b7670e955a applied at rank q+1,
  phi(z)<=2q.
Thus phi(z) is one of 2q-2,2q-1,2q.

Assume t:=phi(z)>=2q-1, and let
  R=(r_1,...,r_t)
be any maximum t-edge path ending at z.

The edge h cannot belong to R. Since z is a last vertex, if h belonged to R it would have to be the last edge; then t<=phi(h)=q+1, contrary to t>=2q-1 for q>=3.

Suppose for contradiction that y is absent from R.
Then any h-contact before the last edge can only use v. Also z occurs only in r_t.

The vertex v must occur on R. Otherwise R,h is a (t+1)-edge path ending in h through terminal z, already exceeding phi(h)=q+1.

Let j be the first path-edge index containing v. Since a path vertex occurs only in one edge or two consecutive edges, choosing the first occurrence ensures
  r_1,...,r_j,h
is linear: y is absent, z has not yet appeared, and h meets the prefix only at v.
This path ends in h through the terminal v. Because h is nonspecial of rank q+1, a path of length q+1 entering h through v would give a second entrance label, while any longer one exceeds the rank. Hence
  j+1 <= q,
so
  j<=q-1.                                             (1)

Now let j' be the last occurrence index of v. The reversed path
  r_{t-1},r_{t-2},...,r_{j'},h
is linear: the final edge r_t containing z is omitted, y is absent, and by last-occurrence choice h meets the reversed suffix only at v.
Its length is
  (t-j')+1.
Again it ends in h through terminal v, so
  t-j'+1 <= q.
Thus
  j' >= t-q+1.                                        (2)

Since j'<=j+1 (a path vertex can occupy at most two consecutive path edges), (1) gives j'<=q. Combining with (2),
  t-q+1 <= q,
hence
  t<=2q-1.
If t=2q, contradiction immediately. If t=2q-1, equality throughout forces
  j=q-1, j'=q,
so v is exactly the central joint r_{q-1} cap r_q.

But then
  r_1,...,r_{q-1},h
is a q-edge path ending in h through v, while
  r_{2q-2},...,r_q,h
is also a q-edge path through v; these are allowed and do not yet contradict nonspeciality. Therefore the above argument alone does not exclude y-absence at t=2q-1; it localizes the sole exceptional state to v=r_{q-1} cap r_q.

Thus:
- if phi(z)=2q, every maximum z-path contains y;
- if phi(z)=2q-1, either every maximum z-path contains y, or the sole y-absent state has v as the unique central joint r_{q-1} cap r_q.

When y lies on R, the position-sensitive endpoint-potential bound 8b1790d79d74 and phi(y)=q localize it:
- for t=2q, y must be the unique central joint r_q cap r_{q+1};
- for t=2q-1, y is either private in r_q or one of the joints r_{q-1} cap r_q, r_q cap r_{q+1}.