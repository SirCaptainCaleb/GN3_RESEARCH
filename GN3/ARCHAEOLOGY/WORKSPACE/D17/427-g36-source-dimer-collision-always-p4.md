# Every G36 source-dimer wall collision already contains a source-visible P4

**Workspace:** D17
**State:** established
**Key:** `g36-source-dimer-collision-always-p4`

**Summary:** The collision arm of the G36 source-gate wall packet is never terminal. In the OUT case SV115482 gives the tight carrier K=(A,t,b). Choose one of the other two source spokes x distinct from b. Test the reverse terminal dimer (b,t) first with C and then with x. A bad test (C,b,t) reverses to (t,b,C), giving P4 (A,t,b,C); if it is tight, C head-signs the reverse terminal dimer. A bad test (x,b,t) reverses to (t,b,x), giving P4 (A,t,b,x); if it too is tight, C and x are two distinct exterior head witnesses on the reverse terminal dimer of K, so accepted exact unit SV78488 forces a literal P4. The IN collision is the exact ordered dual: carrier K=(b,t,C), choose another source spoke x distinct from b, and test the reverse initial dimer (t,b) with A and x; either a bad test gives P4 (A,b,t,C) or (x,b,t,C), or two tight tests invoke the reverse-initial case of SV78488. Therefore both the original P4 arm and the collision arm of SV115482 end in graph-intrinsic source-visible P4 geometry, without generic R523 payment, replay, or fresh witnesses.

### 1. Input and tested-order fence
Retain the G36 source-gate wall packet of SV115482. Thus A,C are the source anchors, t is the source spoke at the wall, and x,y are the other two distinct source spokes. The historical source turns

  (A,t,C), (A,x,C), (A,y,C)

are tight. We consume only the source-dimer COLLISION output of SV115482. The point is to repair the orientation mismatch left by the direct shortcut-carrier upgrade: the collision carrier exposes the natural shortcut dimer, whereas the accepted two-witness P4 unit SV78488 applies to a reverse boundary dimer. All tested orders below are therefore literal.

### 2. OUT collision: force the reverse terminal packet or a P4
In the OUT orientation, SV115482 retains

  (d,b,t) tight,
  (A,t,b) tight.                                         (CP.1)

The second turn is a literal tight trimer

  K=(A,t,b),                                              (CP.2)

whose reverse terminal dimer is

  D_R=(b,t).                                              (CP.3)

Because b lies in the top fiber G=H-{A,C}, b is distinct from A,C. Among the two source spokes x,y, at most one can equal b. Choose

  z in {x,y} with z != b.                                 (CP.4)

Then C and z are distinct vertices outside K.

Test first

  (C,b,t).                                                (CP.5)

If (CP.5) is bad, R3 gives its complete reversal

  (t,b,C) tight,                                          (CP.6)

and (A,t,b) followed by (t,b,C) certifies the literal P4

  (A,t,b,C).                                              (CP.7)

Assume therefore that (C,b,t) is tight. Then C head-signs the tested reverse terminal dimer D_R=(b,t).

Now test

  (z,b,t).                                                (CP.8)

If it is bad, R3 gives

  (t,b,z) tight,                                          (CP.9)

and the carrier turn (A,t,b) concatenates with (CP.9) to the literal P4

  (A,t,b,z).                                              (CP.10)

If instead (CP.8) is tight, the reverse terminal dimer D_R=(b,t) of K is head-signed by the two distinct exterior witnesses C,z. This is exactly the reverse-terminal hypothesis of accepted exact unit SV78488. Hence K union {C,z} contains a literal vertex-simple tight P4.

Thus every OUT source-dimer collision already contains a source-visible P4. Notice that the fixed-wall turn (d,b,t) remains retained as provenance, but no generic collision compiler is needed.

### 3. IN collision: exact ordered dual
In the IN orientation, SV115482 retains

  (t,b,d) tight,
  (b,t,C) tight.                                         (CP.11)

Now

  K^in=(b,t,C)                                            (CP.12)

is a literal tight trimer whose reverse initial dimer is

  D_L=(t,b).                                              (CP.13)

Again choose z in {x,y} with z != b. Then A,z are distinct vertices outside K^in.

Test

  (t,b,A).                                                (CP.14)

If it is bad, R3 gives

  (A,b,t) tight,                                          (CP.15)

and (A,b,t) followed by the carrier turn (b,t,C) gives the literal P4

  (A,b,t,C).                                              (CP.16)

Assume (CP.14) is tight, so A tail-signs the reverse initial dimer D_L=(t,b). Test next

  (t,b,z).                                                (CP.17)

If it is bad, R3 gives

  (z,b,t) tight,                                          (CP.18)

and hence the literal P4

  (z,b,t,C).                                              (CP.19)

If (CP.17) is tight, A,z are two distinct exterior tail witnesses on the reverse initial dimer D_L of K^in. The reverse-initial case of accepted exact unit SV78488 therefore gives a literal P4.

Thus every IN source-dimer collision also contains a source-visible P4.

### 4. G36 contraction
SV115482 already outputs a literal P4 in its noncollision arm. Sections 2-3 show that its collision arm also necessarily contains a literal P4, using only two source-packet tests, R3, and the accepted tested-order-safe unit SV78488. Therefore every persistent far wall reaching a source gate yields graph-intrinsic source-visible P4 geometry.

The P4 keeps the physical shortcut dimer and source identities visible; the old gate orientation, fixed-wall turn, and historical source packet remain retained certificate data. No R24, R5, generic R523 spend, payment, replay, or fresh witness reservoir is used. This section does not yet prove that the resulting P4 itself yields strict old-source transition descent or a spanning two-cover of H; source-gate P4 absorption is the remaining obligation.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
