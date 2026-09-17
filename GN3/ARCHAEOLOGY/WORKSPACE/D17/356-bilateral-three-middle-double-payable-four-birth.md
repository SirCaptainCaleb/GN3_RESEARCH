# Three same-orientation middles force two ancestry-distinct PAYABLE-FOUR births

**Workspace:** D17
**State:** established
**Key:** `bilateral-three-middle-double-payable-four-birth`

**Summary:** Fix one bilateral endpoint-ancestor packet L=(p,a) tail-signed and R=(c,q) head-signed and three distinct same-orientation middles b0,b1,b2 with (a,bi,c) tight. Call a middle easy if one nonexceptional ancestor seam passes, hence gives its own labelled P4 and PAYABLE-FOUR birth. Two easy middles immediately give two ancestry-distinct births. If exactly one is easy, the other two are seam-hard and SV83844 gives a second PAYABLE-FOUR whose source ancestry uses those two hard rows, distinct from the easy P4 birth. If none is easy and p!=q, every z!=p head-signs (a,p) and every z!=q tail-signs (q,c); the two ancestor dimers are disjoint, and the at-least-two choices on each side give two PAYABLE-FOUR certificates with distinct witness ledgers directly in the common parent. If p=q=r and r is one of the three middles, the other two rows give two literal P4s (x,a,r,c). If r is not a middle, the three rows create simultaneous same-polarity collisions on the distinct ancestor dimers (a,r) and (r,c); SV76748 parent-compiles each collision before payment, and SV78086/SV79137 make each output PAYABLE-FOUR, with distinct source-dimer ancestry. Hence three same-oriented middles always supply two source-visible PAYABLE-FOUR births before either is paid. Combining the five-internal-vertex pigeonhole with SV83462, every aligned floor above order ten either closes or reaches the same E with a bilateral packet and two such births; paying one through SV78086 leaves the other as a graph-intrinsic historical fossil.

### 1. Fixed packet and three like-oriented middles
Fix one ancestry-bearing phase-zero floor aligned to

  E={a,c}.

Retain a bilateral physical ancestor packet

  L=(p,a)  tail-signed,
  R=(c,q)  head-signed,                              (DB.1)

with p,q outside E. Let b0,b1,b2 be three distinct physical vertices outside E with

  J_i=(a,b_i,c) tight,  i=0,1,2.                    (DB.2)

No exact representative containing two of the J_i is assumed. All three turns and the signed ancestors in (DB.1) are graph-intrinsic data in one common parent.

For a middle z call z EASY if at least one of the two nonexceptional ancestor seams from the SV57993 replay calculation passes: either z!=p and (p,a,z) is tight, or z!=q and (z,c,q) is tight. An EASY z therefore gives respectively the literal P4

  (p,a,z,c)  or  (a,z,c,q),                          (DB.3)

and hence a source-visible PAYABLE-FOUR birth by SV78086. Record z and the actual passing seam in that birth ancestry.

### 2. Two easy rows already give two births
If two distinct middles z,z' are EASY, use their two P4s from (DB.3). Their source rows have different physical middle labels, so their retained birth ledgers are distinct even if the two four-vertex supports overlap. Thus the common parent already contains two ancestry-distinct PAYABLE-FOUR births before either payment continuation is chosen.

### 3. Exactly one easy row
Suppose exactly one middle z is EASY and write the other two as x,y. Then x and y are seam-hard against both ancestors. Apply SV83844 to the pair J_x,J_y. Its proof cannot exit through an easy seam for x or y, so its PAYABLE-FOUR conclusion is born from the two hard rows, via an ancestor-dimer collision or the explicit exceptional-label P4. In either case the source ancestry contains the hard pair {x,y}.

This birth is ancestry-distinct from the EASY birth, whose source ledger contains the separate middle z and its passing seam. Hence again two source-visible PAYABLE-FOUR births exist before either is paid.

### 4. No easy rows, p and q distinct
Assume now that none of b0,b1,b2 is EASY and first suppose p!=q. For every middle z among the three with z!=p, the left replay calculation gives

  (z,a,p) tight,                                       (DB.4)

so the tested dimer (a,p) is HEAD-signed by every vertex of B\{p}, where B={b0,b1,b2}. Since B has order three, |B\{p}|>=2. Dually, every z!=q gives

  (q,c,z) tight,                                       (DB.5)

so (q,c) is TAIL-signed by every vertex of B\{q}, again at least two witnesses.

Because p,q lie outside E and p!=q, the physical dimers

  D_L=(a,p),  D_R=(q,c)                               (DB.6)

are disjoint. They have opposite polarity. Thus every choice of one retained head witness h in B\{p} and one retained tail witness t in B\{q} gives a PAYABLE-FOUR certificate on the same physical support pair (D_L,D_R). There are at least four such witness pairs. Choose two different pairs. The physical supports may agree, but the PAYABLE-FOUR definition retains the sign witnesses and source packet, so the two birth ancestries are distinct. Both certificates are already graph-intrinsic in the common parent.

### 5. No easy rows, p=q
Now let p=q=r.

If r is one of the three middles, write B={r,x,y}. Since x and y are seam-hard, the left replay calculation gives

  (x,a,r), (y,a,r) tight.                              (DB.7)

Together with J_r=(a,r,c), these give two literal P4s

  (x,a,r,c),  (y,a,r,c).                              (DB.8)

They are distinct source-visible PAYABLE-FOUR births.

It remains that r is not one of b0,b1,b2. Then all three middles head-sign the tested ancestor dimer (a,r) by (DB.4), and all three tail-sign the distinct tested ancestor dimer (r,c) by (DB.5). Hence the common parent contains a same-polarity R523 collision on (a,r) and another same-polarity R523 collision on (r,c). These collision packets have different physical tested dimers and therefore distinct source ancestry.

SV76748 is a parent compiler: before generic payment it converts each raw same-oriented collision, by graph-intrinsic R3 tests and an exact pair-deletion frame, into P4/P5, a direct mass-four opposite-sign pair, or R407. SV78086 makes the first three PAYABLE-FOUR and SV79137 makes R407 PAYABLE-FOUR. Apply that parent compiler separately to the two simultaneously retained collision packets. The resulting PAYABLE-FOUR births retain different source-dimer ancestry, namely (a,r) versus (r,c), so they are ancestry-distinct. No payment descendant has yet been chosen.

### 6. Double-birth theorem
Combining Sections 2--5:

> One bilateral ancestor packet together with any three distinct same-orientation middle turns forces at least two source-visible PAYABLE-FOUR births with distinct retained birth ancestry before either birth is paid.

The two certificates need not have disjoint physical supports from each other. Distinctness here is deliberately the G27 notion: the retained source ledger differs in a physical middle/seam, witness assignment, or source tested dimer. Each certificate separately satisfies the PAYABLE-FOUR support condition of SV78086.

### 7. Every aligned frame supplies the unused fossil
Now begin from any ancestry-bearing E-aligned floor and exact frame

  H-E=U|V.                                               (DB.9)

The frame-abundance calculation in SV83844 gives at least five internal rail vertices, so three physical middles b0,b1,b2 share one outer orientation. Use b0 in the SV83462 bilateral-ancestor manufacture. Outside TWO-COVER, this returns lawfully to the same E carrying a packet of the form (DB.1), while the source frame and the three turns J_0,J_1,J_2 remain graph-intrinsic historical facts. In particular the turn J_0 used during manufacture is not consumed as a graph fact.

Apply Section 6 to all three turns against the manufactured packet. Thus every such aligned frame yields TWO-COVER or reaches the same E with two ancestry-distinct PAYABLE-FOUR births visible before payment.

Choose one birth and run the SV78086 cancellation macro. If it closes or descends, stop. In the flat-return branch R514/SV78086 preserve separately certified graph-intrinsic static facts as historical ancestry, so the second PAYABLE-FOUR certificate survives as an UNUSED BIRTH FOSSIL while the first selected-incidence episode emits the explicit short R435/R436 portal.

Therefore the G27 portal-stack state requires no extra branching hypothesis: every surviving flat bottom state can be normalized to

  unused PAYABLE-FOUR fossil
  + one paid birth lineage returned flat to the same E
  + the resulting explicit short portal.                (DB.10)

The remaining theorem is to show that the short portal cannot replay indefinitely while the unused fossil and the three source middle rows remain graph-intrinsic.

### 8. Scope fence
This theorem does not claim that two paid descendants coexist, nor that the unused birth remains current after the other birth is paid. It remains a graph-intrinsic historical certificate exactly in the R514/SV78086 sense. It does not yet consume the explicit short portal in (DB.10), and it does not count a flat return as descent.

R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R514"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    }
]
```