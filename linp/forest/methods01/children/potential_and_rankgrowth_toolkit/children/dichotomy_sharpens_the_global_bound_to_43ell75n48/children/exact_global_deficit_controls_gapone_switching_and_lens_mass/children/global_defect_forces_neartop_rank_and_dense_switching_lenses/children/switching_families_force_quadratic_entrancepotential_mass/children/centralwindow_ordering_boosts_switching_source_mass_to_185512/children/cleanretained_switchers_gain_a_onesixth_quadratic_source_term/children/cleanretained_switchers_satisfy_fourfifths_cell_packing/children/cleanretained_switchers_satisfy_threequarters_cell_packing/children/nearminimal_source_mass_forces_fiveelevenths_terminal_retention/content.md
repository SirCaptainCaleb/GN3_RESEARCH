# Near-minimal source mass forces five-elevenths terminal retention

## Statement

Let v be an active misaligned p-center and split a switching family
  F_v=X_v disjoint_union U_v
with
  a=|X_v|, k=|U_v|, s=a+k.
Then, up to an additive O(p) term,
  sum_{f in F_v}phi(x_f)
  >= (p/2)s + s^2/8
      + max{0, a(11a-6s)/24}.                         (*)

Consequently, suppose eta_v=o(p) and the switching-source mass remains within o(p^2) of the generic 185/512 p^2 floor. Then necessarily
  s=(5/8+o(1))p
and
  k >= (5/11-o(1))s
    = (25/88-o(1))p.

If instead eta_v=o(p) and
  k <= (5/11-epsilon)s
for a fixed epsilon>0, then the source-potential mass exceeds the generic 185/512 p^2 floor by a fixed positive multiple of p^2.

## Body

The generic all-switcher ordering theorem a5066873364f gives
  M:=sum_{f in F_v}phi(x_f)
  >= (p/2)s+s^2/8-O(p).                               (1)

The strengthened clean-retained theorem a6f97c9fd9c3 gives
  sum_{f in X_v}phi(x_f)
  >= (p/2)a+a^2/3-O(a).                               (2)

The terminal-retained theorem c48823eea604 gives
  sum_{f in U_v}phi(x_f)
  >= (p/2)k+k^2/8-O(k).                               (3)

Adding (2) and (3),
  M >= (p/2)s+a^2/3+k^2/8-O(p).                       (4)
Since k=s-a,
  a^2/3+k^2/8-s^2/8
   =a^2/3+(s-a)^2/8-s^2/8
   =11a^2/24-as/4
   =a(11a-6s)/24.                                     (5)
Taking the better of (1) and (4) proves (*).

Now assume eta_v=o(p), and suppose the switching-source mass is within o(p^2) of the generic 185/512 p^2 floor. By b032348c1a8a,
  s >= (5/8-o(1))p.                                   (6)
On the other hand, (1) and the assumed upper bound
  M <= (185/512+o(1))p^2
force
  (p/2)s+s^2/8 <= (185/512+o(1))p^2.
The left side is increasing in s>=0, and at s=(5/8)p it equals (185/512)p^2. Combining with (6) therefore gives
  s=(5/8+o(1))p.                                      (7)

Because the extra term in (*) must now be o(p^2), we have
  max{0,a(11a-6s)/24}=o(p^2).                         (8)
We claim this forces
  a <= (6/11+o(1))s.
Indeed, if there were a fixed epsilon>0 and infinitely many centers with
  a >= (6/11+epsilon)s,
then by (7), a=Theta(p) and
  11a-6s >= 11epsilon s=Theta(p),
so the correction in (8) would be Omega(p^2), a contradiction. Hence
  a <= (6/11+o(1))s,
and therefore
  k=s-a >= (5/11-o(1))s
          =(25/88-o(1))p.

For a quantitative gap, assume
  k <= (5/11-epsilon)s
for a fixed epsilon>0. Then
  a >= (6/11+epsilon)s
and
  11a-6s >= 11epsilon s.
Hence the correction in (*) is at least
  [(6/11+epsilon)11epsilon/24]s^2.
Whenever eta_v=o(p), (6) makes s=Theta(p), so this is a fixed positive multiple of p^2.