# Near-minimal source mass forces three-sevenths terminal retention

## Statement

Let v be an active misaligned p-center and let a low-defect switching family F_v split as
  F_v=X_v disjoint_union U_v,
with a=|X_v|, k=|U_v|, s=a+k.
Then, up to an additive O(p) boundary term,
  sum_{f in F_v} phi(x_f)
  >= (p/2)s + s^2/8
      + max{0, a(7a-4s)/16}.                         (*)

Consequently, if eta_v=o(p), so s=(5/8-o(1))p, then either the forced source-potential mass is larger than the generic 185/512 p^2 floor by a fixed positive multiple of p^2, or
  k >= (3/7-o(1))s
    = (15/56-o(1))p.

More quantitatively, if k <= (3/7-epsilon)s for fixed epsilon>0, then
  sum_{f in F_v} phi(x_f)
  >= (185/512 + c_epsilon-o(1))p^2
for some explicit c_epsilon>0 (for example one may take c_epsilon asymptotic to 25 epsilon/512 for small epsilon).

## Body

Write a=|X_v|, k=|U_v|, s=a+k.

The generic all-switcher theorem a5066873364f gives
  M:=sum_{f in F_v}phi(x_f)
  >= (p/2)s + s^2/8 - O(p).                           (1)

For the clean-retained part, 7e047fd40dd7 gives
  sum_{f in X_v}phi(x_f)
  >= (p/2)a + 5a^2/16 - O(a).                         (2)

For the terminal-retained part, c48823eea604 gives
  sum_{f in U_v}phi(x_f)
  >= (p/2)k + k^2/8 - O(k).                           (3)
(The exact theorem has a slightly better positive linear term.)

Adding (2) and (3),
  M >= (p/2)s + 5a^2/16 + k^2/8 - O(p).               (4)

Subtract the quadratic term in (1). Since k=s-a,
  5a^2/16 + k^2/8 - s^2/8
   = 5a^2/16 + (s-a)^2/8 - s^2/8
   = a(7a-4s)/16.                                     (5)

Taking the better of (1) and (4) proves (*).

Now assume eta_v=o(p). By b032348c1a8a,
  s=(5/8-o(1))p.
If k<(3/7)s, then a=s-k>(4/7)s, so the correction term in (*) is positive. If for some fixed epsilon>0,
  k <= (3/7-epsilon)s,
then
  a >= (4/7+epsilon)s
and
  7a-4s >= 7epsilon s.
Hence
  a(7a-4s)/16
  >= ((4/7+epsilon)7epsilon/16)s^2
  = (epsilon/4+7epsilon^2/16)s^2.
Since s^2=(25/64-o(1))p^2, this is a fixed positive multiple of p^2. The generic part of (1) equals
  (p/2)(5p/8)+(1/8)(25p^2/64)-o(p^2)
  =(185/512-o(1))p^2.
This proves the quantitative improvement.

Therefore any sequence of low-defect centers whose source mass remains within o(p^2) of the generic 185/512 floor must satisfy
  k >= (3/7-o(1))s
and hence
  k >= (3/7-o(1))(5/8-o(1))p
    = (15/56-o(1))p.
