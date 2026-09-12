# At the unique stationary equality middle, every current selected incidence is immediately nonquiet or PAYABLE-FOUR

**Workspace:** D17
**State:** established
**Key:** `fully-anchored-stationary-middle-selected-incidence-compiler`

**Summary:** Fix the fully anchored stationary predecessor-equality atom E={a,c}, common old secondary x, unique middle b, with (b,a,x), (x,c,b), (a,b,c) tight. Now add the current-frame data required by SV79258: an exact H-E cover in which b is internal, with selected predecessor r and successor s. Apply the literal R434/R3 split at b. On the a-side, either (r,a,b) is tight, giving the P4 (r,a,b,c), or its reverse (b,a,r) is tight. In the reverse branch compare r with the historical x. If r=x, the current dimer is exact replay of the historical a-dimer (x,a), so the endpoint is spent and R436 gives explicit nonquiet geometry. If r!=x, test (r,a,x): tight gives the P4 (r,a,x,c) after one additional seam test against (x,c,b), while failure gives a reverse trimer that pairs with the current/historical opposite-side packet. The c-side is dual. Combining the two sides, unless an explicit R436/R435/contact portal appears, one obtains a source-visible proper P4 and therefore PAYABLE-FOUR cancellation. Hence the unique physical middle is not a silent bottom recurrence once a current exact frame is present.

### 1. Add the missing current-frame bridge
Retain the stationary historical atom

  E={a,c},
  x outside E,
  J=(a,b,c) tight,
  (b,a,x) tight,
  (x,c,b) tight.                                         (SI.1)

Now suppose a current exact pair-deletion cover

  H-E=U|V                                                 (SI.2)

has b internal on one rail, with selected predecessor and successor

  r -> b -> s.                                            (SI.3)

This is exactly the current-frame datum whose absence was fenced in SV79258.

### 2. Current a-side incidence
Apply the R434 predecessor split. Exactly one of

  (r,a,b), (b,a,r)                                       (SI.4)

is tight.

If (r,a,b) is tight, concatenate with J to obtain the literal P4

  (r,a,b,c).                                             (SI.5)

This is immediately PAYABLE-FOUR by SV78086.

Assume instead

  (b,a,r) tight.                                         (SI.6)

If r=x, then (SI.6) is exact graph-intrinsic replay of the historical reverse trimer/dimer packet at a. Since a is fully anchored and the old nontrivial a-ancestor is retained, accepted R436 gives explicit nonquiet at-anchor geometry. Thus r=x is not silent.

Assume r!=x.

### 3. Distinct current predecessor versus historical predecessor
Test

  (r,a,x).                                               (SI.7)

If it is tight, combine with the historical turn (x,c,b) only after testing

  (a,x,c).                                               (SI.8)

If (SI.8) is tight, then

  (r,a,x,c)                                              (SI.9)

is a literal P4, PAYABLE-FOUR.

If (SI.8) is bad, R3 gives

  (c,x,a) tight.                                         (SI.10)

Together with (SI.7) and (SI.6), this is explicit bounded reverse/contact geometry on {b,a,r,x,c}; retain it as an explicit nonquiet portal. No P4 is claimed in this subbranch.

If (SI.7) is bad, R3 gives

  (x,a,r) tight.                                         (SI.11)

Comparing (SI.11) with (SI.6) yields a same-middle two-witness packet on the tested dimer through a; accepted R523/R435 gives explicit reversal/trimer/P4 geometry. In every nonportal outcome a proper P4 is exposed.

Thus the a-side current incidence yields either PAYABLE-FOUR or explicit nonquiet geometry.

### 4. c-side is dual
The selected successor split gives exactly one of

  (b,c,s), (s,c,b)                                       (SI.12)

as tight. The forward branch gives the literal P4

  (a,b,c,s).                                             (SI.13)

In the reverse branch compare s with historical x. Equality s=x is spent-endpoint replay and hence explicit R436 nonquiet geometry. If s!=x, the exact dual of Section 3 gives either a proper P4 or explicit bounded reverse/contact geometry.

No informal path reversal is used; the ordered turns are dual with a<->c and predecessor<->successor.

### 5. Stationary-middle collapse with current data
Therefore, once a current exact H-E frame internalizing b is supplied, the stationary equality atom has no silent selected-incidence continuation. The first current predecessor/successor episode gives

  PAYABLE-FOUR,
  or EXPLICIT NONQUIET PORTAL.                            (SI.14)

PAYABLE-FOUR is consumed by SV78086 into two-cover, strict old-E descent, or explicit nonquiet portal. Hence the unique stationary physical middle cannot support a portal-free rank-flat recurrence.

This section does not consume the explicit nonquiet portal itself and does not claim old and current covers coincide. It uses exactly the current-frame bridge required by SV79258.