# Two distinct same-orientation middles against one bilateral ancestor packet force PAYABLE-FOUR

**Workspace:** D17
**State:** established
**Key:** `bilateral-ancestor-two-middle-payable-four-collapse`

**Summary:** Fix one ancestry-bearing E={a,c} floor carrying graph-intrinsic bilateral endpoint ancestors L=(p,a) tail-signed and R=(c,q) head-signed. Let b!=d be two later physical middles with (a,b,c) and (a,d,c) tight. Apply the SV57993 bilateral replay-breaker to each turn. If any ancestor seam passes, a literal P4 is already present and hence PAYABLE-FOUR by SV78086. Otherwise every middle z!=p gives the reverse trimer (z,a,p), so if neither b nor d equals p the ancestor dimer (a,p) has a same-oriented two-witness collision. Dually, if neither equals q, (q,c) has a two-witness collision. Each collision parent-compiles through SV76748/SV79137 to PAYABLE-FOUR. Avoiding both collisions forces the exceptional labels: if p!=q then {b,d}={p,q}, and (q,a,p)+(a,p,c) is a literal P4; if p=q=r then the two middles are {r,x} and (x,a,r)+(a,r,c) is a literal P4. Hence every two distinct same-orientation reentry middles force a source-visible PAYABLE-FOUR packet. Corollary: in any exact H-E frame above order ten, at least five internal vertices exist and three share one outer orientation; use one to manufacture the SV83462 bilateral packet and the other two force PAYABLE-FOUR. Thus a bottom family cannot keep multiple same-oriented middles in a genuinely short-portal-only state before payment.

### 1. Bilateral ancestor packet and two later middles
Fix an ancestry-bearing phase-zero floor aligned to the physical pair

  E={a,c}.

Retain one graph-intrinsic bilateral endpoint-ancestor packet

  L=(p,a)  tail-signed,
  R=(c,q)  head-signed,                              (TM.1)

with p,q outside E. The packet may come from completed endpoint episodes as in SV57993 or from the direct manufacture theorem SV83462; only the literal signed dimers in (TM.1) are used below.

Let b,d be two distinct physical vertices outside E such that both same-orientation turns

  J_b=(a,b,c),
  J_d=(a,d,c)                                           (TM.2)

are tight. No exact cover containing both turns is assumed. They are graph-intrinsic turns available from the same boundary tournament.

### 2. Any passing ancestor seam is already PAYABLE-FOUR
Apply the local bilateral replay-breaker SV57993 separately to J_b and J_d against the fixed packet (TM.1).

At the left endpoint, for z in {b,d}: if z!=p and (p,a,z) is tight, then

  (p,a,z,c)                                             (TM.3)

is a literal P4. At the right endpoint, if z!=q and (z,c,q) is tight, then

  (a,z,c,q)                                             (TM.4)

is a literal P4.

By SV78086 every proper P4 is PAYABLE-FOUR through its two disjoint opposite-polarity boundary dimers. Therefore assume from now on that none of the four available ancestor seams produces (TM.3) or (TM.4).

### 3. The generic no-P4 branch gives a collision on an ancestor dimer
Under the no-P4 assumption, SV57993 gives the exact reverse turns

  (z,a,p) tight whenever z!=p,                         (TM.5)
  (q,c,z) tight whenever z!=q.                         (TM.6)

If neither b nor d equals p, then (TM.5) says that the same tested oriented dimer (a,p) is head-signed by the two distinct witnesses b,d. This is an R523 same-oriented two-witness collision on the fixed physical ancestor dimer.

Similarly, if neither b nor d equals q, then (TM.6) says that the tested dimer (q,c) is tail-signed by the two distinct witnesses b,d, again an R523 collision.

Current collision compiler SV76748 sends either collision, before unrelated payment, to a literal P4/P5, a direct mass-four opposite-sign pair, or an R407 packet. The first three outputs are PAYABLE-FOUR by SV78086 and the last is PAYABLE-FOUR by SV79137. Hence avoiding PAYABLE-FOUR forces simultaneously

  one of {b,d} equals p,
  one of {b,d} equals q.                               (TM.7)

### 4. The exceptional labels also give a literal P4
First suppose p!=q. Since b,d are distinct, (TM.7) forces

  {b,d}={p,q}.                                          (TM.8)

Without loss let b=p and d=q. Because d=q!=p, the no-P4 left branch gives

  (q,a,p) tight.                                        (TM.9)

But J_b=(a,p,c) is tight by (TM.2), so

  (q,a,p,c)                                             (TM.10)

is a literal P4 on four distinct physical vertices. Hence it is PAYABLE-FOUR.

Now suppose p=q=r. Condition (TM.7) says one of the two distinct middles equals r; write the pair as {r,x}. The no-P4 left branch for x gives

  (x,a,r) tight,                                        (TM.11)

while J_r=(a,r,c) is tight. Therefore

  (x,a,r,c)                                             (TM.12)

is again a literal P4 and hence PAYABLE-FOUR.

Thus no exceptional label pattern survives.

### 5. Two-middle parent theorem
Combining Sections 2--4:

> For one fixed bilateral endpoint-ancestor packet L=(p,a), R=(c,q), any two distinct later proper turns (a,b,c),(a,d,c) with the same outer orientation force a source-visible PAYABLE-FOUR packet in the common graph-intrinsic parent.

No payment descendant from one turn is identified with a descendant from the other. The theorem acts before that split.

At a fixed-E phase-zero checkpoint, SV78086 therefore gives TWO-COVER, strict descent of the old fixed-E clock, or explicit nonquiet portal geometry. The conclusion is not that PAYABLE-FOUR itself is strict progress at the exhausted bottom tuple; the gain is that a genuinely short-portal-only family has physical-middle capacity one for a fixed ancestor packet and outer orientation.

### 6. Frame-abundance corollary above order ten
Fix any ancestry-bearing E-aligned floor and one exact frame

  H-E=U|V.                                               (TM.13)

Accepted R429 makes both rails nontrivial. Since the current smallest counterexample has n>10, the number of internal rail vertices is

  (|U|-2)+(|V|-2)=n-6 >= 5.                             (TM.14)

Color each internal vertex z by which of the two outer turns

  (a,z,c), (c,z,a)                                      (TM.15)

is tight. Three internal vertices share one color. Display the unordered endpoint pair in that common orientation and call the three middles b0,b1,b2.

Apply SV83462 to b0. Outside TWO-COVER it returns lawfully to the same E with a manufactured bilateral packet of the form (TM.1), preserving the source frame and witnesses as historical data. The two remaining graph-intrinsic turns J_{b1},J_{b2} have the same displayed outer orientation, so Section 5 forces PAYABLE-FOUR.

Hence every ancestry-bearing aligned floor above order ten admits a finite source-visible route to PAYABLE-FOUR using one exact H-E frame and three like-oriented internal middles. This is a family-level branching statement: it does not require prior quiet completion of either endpoint and does not treat alternative descendants as simultaneous current representatives.

### 7. Scope fence
This theorem does not by itself consume the explicit nonquiet portal allowed by SV78086 at the bottom tuple. It proves a capacity/branching fact before payment: once the bilateral ancestor packet is fixed, two distinct same-orientation middles cannot both remain in the short reverse-trimer/adjacent-reversal residue.

R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    },
    {
        "relation": "dependency",
        "revision_id": "R533"
    }
]
```