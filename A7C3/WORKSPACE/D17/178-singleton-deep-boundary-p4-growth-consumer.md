# The failed-wrap boundary P4 either grows across M or currentizes as Reverse-Ear geometry

**Workspace:** D17
**State:** established
**Key:** `singleton-deep-boundary-p4-growth-consumer`

**Summary:** In the true T+ failed-wrap row R=(s,M,p,q)|B, every Hamilton boundary P4 F used by this consumer lives on X={s,q,p,t} inside H itself. Hence H-X is literally M union B, and M|B is an exact two-cover of that complement: if H-X were Hamiltonian, its Hamilton path together with F would two-cover H. All endpoint/internal P4s obtained from F by the Section 2-3 R579 reductions stay on this same support X, so they retain the same exact H-complement M|B and omit no labels. This is distinct from the earlier R579 double-fail reverse P4 (m1,s,q,p), which lies in H-t and leaves t omitted; that preliminary output is not assigned the H-complement claim. For an X-P4, endpoint-t orders either currentize as exact R435 geometry against ancestral R or reduce to a t-internal order. The ten possible t-internal Hamilton orders are exhaustive after the three known bad turns; four literal rows extend to a P5 using exactly (m1,s,t) or (t,p,u), and the remaining rows reduce by R579 to those growth rows or endpoint-t P4s. If |M|>1, the P5 has literal exact two-path complement (M with one endpoint deleted)|B; if |M|=1, the P5 together with B spans H. Thus the clean boundary-P4 output is a genuine three-to-two consumer: spanning closure, strict one-vertex P5 growth with exact complement, or explicit R435 geometry.


### 1. Setup and the four exterior restoration shields
Retain the true T+ failed-wrap row from `singleton-deep-tplus-anti-extension-cell`:

  R=(s,m_1,...,u,p,q) | B = (s,M,p,q) | B

as an exact two-cover of H-t, with M nonempty. The failed current tail wrap gives

  (p,q,s) bad,  hence (s,q,p) tight.

Outside the already-separated R579 double-wrap P4, the opposite head wrap is tight, so

  R^h=(q,s,m_1,...,u,p) | B

is a second exact H-t two-cover on the same support and literal complement B.

Because either exterior restoration by t would two-cover H with B, all four endpoint tests are forced bad:

  (t,s,m_1) bad,   (p,q,t) bad,
  (t,q,s) bad,     (u,p,t) bad.

By R3 retain the exact reverse shields

  (m_1,s,t),  (t,q,p),  (s,q,t),  (t,p,u) tight.        (BP.1)

These coexist with the two inherited H-t orders. In particular the boundary four-set

  X={s,q,p,t}

already has the tight trimers (s,q,p), (s,q,t), and (t,q,p), while their complete reverses (p,q,s), (t,q,s), and (p,q,t) are bad.

Assume now that X is Hamiltonian and fix any actual tight Hamilton order F on X. The aim is to consume F together with the literal residual paths M and B.

### 2. Endpoint t normalizes to t-internal or exact R435 geometry
Suppose first that t is an endpoint of F. Apply accepted R579/P657 to the actual four-vertex path F. One of the two cyclic rotations moves t into an internal position. If that wrap succeeds, retain the resulting t-internal P4. If both wraps fail, the R579 DF reverse P4 has t internal. Hence the only way to remain in an endpoint-t state is the single-wrap branch in the other direction, which supplies another actual endpoint-t Hamilton order on X.

Compare any surviving endpoint-t order with the ancestral path R, using only their common old vertices {s,p,q}. If these contacts are not increasing in the ancestral order

  s <_R p <_R q,

accepted R435/P448 gives its explicit reverse-state / reverse-trimer / tight-cycle geometry, and this section stops.

It remains to check the R435-quiet contact order. Then the old contacts occur as s,p,q. If t is terminal, the path would be

  (s,p,q,t),

which is impossible because (p,q,t) is bad by (BP.1). If t is the source, the only quiet order is

  (t,s,p,q).

Apply R579 once more. Its tail-wrap seam is (p,q,t), already bad. If the other wrap passes, the rotation (q,t,s,p) is a t-internal P4; if it also fails, the R579 DF reverse P4 (s,t,q,p) is t-internal. Therefore an endpoint-t P4 never remains quiet: it yields a t-internal P4 or exact R435 geometry.

### 3. The t-internal orders reduce to four literal P5 growth rows or an endpoint P4
Now let t be internal in F. The three bad turns

  (p,q,s), (p,q,t), (t,q,s)

exclude every t-internal permutation using one of them as a consecutive triple. The ten remaining possible Hamilton orders are exactly the rows below. Each row is consumed using only its two certified F-turns, (BP.1), and R579.

1. F=(s,q,t,p). Then

     (s,q,t,p,u)

   is a tight P5, using the F turns followed by (t,p,u).

2. F=(s,p,t,q). Here the R579 tail-wrap seam (t,q,s) is already bad. If the other wrap passes, R579 gives the endpoint-t P4 (q,s,p,t); if it fails too, DF gives the endpoint-t P4 (p,s,q,t).

3. F=(s,t,q,p). Then

     (m_1,s,t,q,p)

   is a tight P5, using (m_1,s,t) followed by the two F turns.

4. F=(s,t,p,q). Then

     (m_1,s,t,p,q)

   is a tight P5.

5. F=(q,s,t,p). Then

     (q,s,t,p,u)

   is a tight P5.

6. F=(q,p,t,s). Its first turn (q,p,t), together with the retained (s,q,p), gives the endpoint-t P4

     (s,q,p,t).

7. F=(q,t,s,p). The R579 head-wrap seam (p,q,t) is already bad. Hence R579 gives either the endpoint-t rotation (t,s,p,q) or, in DF, the endpoint-t reverse P4 (t,q,p,s).

8. F=(q,t,p,s). Here the R579 head-wrap seam (s,q,t) is tight. If the other wrap fails, R579 gives the growth row (s,q,t,p), which is Row 1; if it passes, the other rotation is the endpoint-t P4 (t,p,s,q).

9. F=(p,s,t,q). Here the R579 tail-wrap seam (t,q,p) is tight. If the other wrap fails, R579 gives the growth row (s,t,q,p), Row 3; if it passes, the other rotation is the endpoint-t P4 (q,p,s,t).

10. F=(p,t,s,q). Here the R579 tail-wrap seam (s,q,p) is tight. If the other wrap fails, R579 gives the endpoint-t P4 (t,s,q,p); if it passes, the other rotation is (q,p,t,s), Row 6, which immediately gives the endpoint-t P4 (s,q,p,t).

Thus every t-internal P4 reaches either an endpoint-t P4, already consumed in Section 2, or one of the four displayed P5 growth rows.

### 4. The growth is literal and strict
In Rows 1 and 5 the P5 absorbs the terminal M-vertex u. Its literal complement is

  (m_1,...,M-u) | B.

In Rows 3 and 4 the P5 absorbs the source M-vertex m_1. Its literal complement is

  (M-m_1) | B.

When |M|>1 these are literal two-path complements with the M-rail shortened by one. They are exact: if either complement were Hamiltonian, that Hamilton path together with the displayed P5 would two-cover H. Hence the clean boundary-P4 branch gives strict graph-intrinsic path growth while preserving B literally.

When |M|=1, the displayed P5 uses all vertices outside B, so the P5 together with B is already a spanning two-cover of H. Therefore the boundary-P4 branch cannot survive with |M|=1.

### 5. Consequence
The Hamilton boundary-four-set output of SV14742 is not a terminal P4 packet. Before any generic R159/R176/R523/R542 payment it yields exactly one of:

1. a spanning two-cover when |M|=1;
2. a tight P5 whose literal exact complement is (M with one endpoint deleted)|B, a strict one-vertex absorber growth; or
3. explicit accepted R435 geometry witnessed by the actual endpoint-t P4 against the ancestral order s<M<p<q.

The P5 output is intentionally retained with its physical absorbed endpoint and literal B complement. This section does not claim that the residual R435 output is closure, nor that the grown P5 automatically iterates by the same failed-wrap theorem without a fresh reconstruction.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R579"
    }
]
```
