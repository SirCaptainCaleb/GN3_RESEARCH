# A source-dimer wall collision upgrades to a P4 or a source-witness packet on the actual shortcut dimer

**Workspace:** D17
**State:** established
**Key:** `g36-source-collision-shortcut-carrier-upgrade`

**Summary:** Refine the collision branch of SV115482 without anonymizing it. In the OUT case retain the wall turn (d,b,t), collision turn (A,t,b), historical source turn (A,t,C), and let x,y be the other two source spokes. For every w in {C,x,y} distinct from b, test (b,t,w). A tight test concatenates with the wall to the literal P4 (d,b,t,w); a bad test reverses by R3 to (w,t,b), so w head-signs the actual attempted shortcut dimer (t,b). Since C is always distinct from b and at most one of x,y can equal b, if no P4 appears then carrier (A,t,b) contains (t,b) with at least two exterior same-polarity witnesses drawn entirely from the original source packet; if b is not a source spoke there are all three witnesses C,x,y. The IN case is the exact ordered dual: from (t,b,d) and carrier (b,t,C), test (w,t,b) for w in {A,x,y} distinct from b; success gives P4 (w,t,b,d), failure gives (b,t,w), so (b,t) has at least two exterior tail witnesses from the source packet. Thus the G36 collision does not need a fresh carrier or fresh witness reservoir: it transfers directly onto the physical shortcut dimer, retaining the wall and source identities.

### 1. Input from the source-gate wall collapse
Retain the G36 source packet with source anchors A,C and three distinct source spokes. Let t be the source spoke at which the persistent far wall is met, and denote the other two source spokes by x,y. Thus

  (A,t,C), (A,x,C), (A,y,C)

are historical tight source turns.

We refine only the collision alternative of SV115482. No generic collision compiler is applied.

### 2. OUT collision: move the collision from the source dimer to the actual shortcut dimer
In the OUT orientation, SV115482 retains the fixed-wall turn

  (d,b,t) tight,                                           (SC.1)

and in its collision branch the test at A failed, so R3 gave

  (A,t,b) tight.                                           (SC.2)

Together with (A,t,C), this was the same-oriented collision on the source dimer (A,t). The important additional fact is that (SC.2) is itself a literal tight carrier whose terminal dimer is the actual attempted closing dimer

  D=(t,b).                                                 (SC.3)

Let

  W_out={C,x,y} minus {b}.                                 (SC.4)

Every w in W_out is distinct from A,t,b. Since C is not a vertex of the top fiber G=H-{A,C}, the far vertex b is never C. Among x,y at most one can equal b. Therefore

  |W_out|>=2.                                              (SC.5)

For each w in W_out test the exact ordered turn

  (b,t,w).                                                 (SC.6)

If (SC.6) is tight for some w, then (SC.1) and (SC.6) concatenate to the literal vertex-simple tight P4

  (d,b,t,w).                                               (SC.7)

If instead (SC.6) is bad, boundary antisymmetry R3 gives its complete reversal

  (w,t,b) tight.                                           (SC.8)

Thus w head-signs the tested shortcut dimer D=(t,b). If no test (SC.6) succeeds, every w in W_out head-signs D while lying outside the carrier

  K=(A,t,b).                                               (SC.9)

Hence the non-P4 OUT residue is a literal short-carrier same-polarity witness packet on the ACTUAL shortcut dimer, with at least two witnesses drawn from the original source set. If b is not one of x,y, then all three vertices C,x,y are exterior head witnesses.

### 3. IN collision is the exact ordered dual
In the IN orientation, SV115482 retains

  (t,b,d) tight,                                           (SC.10)

and its collision branch gives

  (b,t,C) tight,                                           (SC.11)

while (A,t,C) remains tight. Now (SC.11) is a literal tight carrier whose initial dimer is the actual IN shortcut orientation

  D^in=(b,t).                                              (SC.12)

Put

  W_in={A,x,y} minus {b}.                                  (SC.13)

Again A is outside G and cannot equal b, while at most one of x,y can equal b, so |W_in|>=2. For w in W_in test

  (w,t,b).                                                 (SC.14)

If (SC.14) is tight, it concatenates with (SC.10) to the literal P4

  (w,t,b,d).                                               (SC.15)

If (SC.14) is bad, R3 gives

  (b,t,w) tight,                                           (SC.16)

so w tail-signs D^in=(b,t). If no test succeeds, carrier (b,t,C) therefore contains the physical shortcut dimer with at least two exterior same-polarity witnesses from the original source packet; if b is not x or y there are the three witnesses A,x,y.

### 4. Consequence
The source-dimer collision output of SV115482 is not terminal even before invoking any generic R523/R542 compiler. It has the sharper source-preserving refinement:

1. a literal P4 using the fixed wall, the source spoke t, and another source-packet vertex; or
2. a short-carrier two-witness packet on the actual attempted shortcut dimer, with every retained witness coming from the original source packet and the carrier retaining one source anchor.

When the fixed far vertex b is not another source spoke, the second alternative has three source-packet witnesses outright. Even in the collision b=x or b=y case, two exterior source witnesses remain, so the packet is already of the short-carrier type without manufacturing a fresh carrier.

This section deliberately stops before the generic short-carrier compiler: its gain is preservation of the source-gate, fixed-wall, and source-witness identities that G36 asks the final absorber to use. No R24, R5, payment, replay, or fresh witness reservoir is used.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
