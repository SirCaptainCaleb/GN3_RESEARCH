# Three-witness same-parent collisions refine to a direct pair, a literal P4, or bidirectional saturation

**Workspace:** D17
**State:** established
**Key:** `three-witness-collision-refinement`

**Summary:** Refines the collision alternative of SV44176. A same-parent R523 collision on the crossing marker remembers whether it came from the tight or bad R526 test class. If it came from a tight class, the collision marker has polarity opposite to the original signed dimer, so the two disjoint dimers already form a direct balanced pair of total support mass four. If it came from a bad class, the collision marker has the same polarity as the original dimer. Test the opposite marker orientation against all three witnesses. Any opposite-polarity certificate on the collision orientation combines with one of the two existing same-polarity witnesses via R523 to give a literal tight P4. If all opposite-orientation tests fail, R3 makes the reverse marker orientation carry the same polarity for all three witnesses, so one physical marker is signed in both tested orientations with a common witness, exactly the accepted R407 bidirectional same-witness packet. Tail polarity is checked explicitly. Hence the anonymous collision output disappears: three-witness common-crossing interaction yields P4/P5 geometry, a direct mass-four pair, or an R407 interaction packet, all upstream of alternative payment descendants.

### 1. Input from the common-crossing compiler
Retain the setup and output of SV44176. Thus S=(a,b) is one tested oriented signed dimer inside a carrier K, with three distinct same-polarity witnesses W={w1,w2,w3} outside K, and one exact H-S two-cover supplies a physical carrier/exterior crossing marker D on two vertices disjoint from S. SV44176 works entirely in the common parent and yields either a literal tight P4/P5 already, or an R523 same-oriented-dimer collision on D or its reverse.

Only the collision output remains to be refined. The key extra datum is that the collision class remembers whether it arose from a TIGHT R526 terminal test or from a BAD test reversed by R3.

### 2. Tight-class collision is already a direct balanced pair
Assume first S is head-signed by all three witnesses. In the SV44176 calculation, a tight actualization test on an oriented marker M=(u,v) is

  (u,v,w) tight.

Therefore M is tail-signed by w. Since S is head-signed and V(M) is disjoint from V(S), S and M are physically disjoint opposite-polarity signed dimers. They are therefore a direct balanced pair of total support mass four. This conclusion exists already in the common parent frame; no paid descendant is asserted current.

If S is tail-signed, a tight R526 test has the form

  (w,u,v) tight,

so M is head-signed and is again opposite in polarity to S. Thus every collision coming from the tight outcome class is already a direct mass-four balanced pair.

### 3. Bad-class collision: test the opposite marker orientation
Assume now S is head-signed and the collision comes from BAD R526 tests. After naming the collision orientation D=(v,u), there are two distinct witnesses p,q in W with

  (p,v,u), (q,v,u) tight.                                  (CR.1)

Thus D is head-signed by p and q, the same polarity as S. Consider the opposite marker orientation D^op=(u,v). Because all witnesses lie outside the physical marker in the collision case, the R526 head-signed test for D is equivalently the ordered turn

  (v,u,w),

while testing D^op uses

  (u,v,w).                                                (CR.2)

Apply (CR.2) to all three witnesses.

If (v,u,r) is tight for some r in W, then D is tail-signed by r. Since D is already head-signed by two distinct witnesses p,q, choose one of {p,q} different from r. Accepted R523 on the SAME tested orientation D=(v,u) gives the literal tight P4

  (p,v,u,r)   or   (q,v,u,r).                             (CR.3)

If instead (v,u,r) is bad for every r in W, R3 gives

  (r,u,v) tight for every r in W.                         (CR.4)

Hence D^op=(u,v) is head-signed by all three witnesses, while D=(v,u) is already head-signed by at least p,q. In particular one common witness, say p, head-signs BOTH tested orientations of the same physical marker. This is exactly the bidirectional same-witness dimer saturation hypothesis of accepted R407.

Thus a bad-class head collision refines to literal P4 or an R407 bidirectional packet.

### 4. Explicit tail dual
Suppose S is tail-signed and a bad-class collision gives one orientation D=(v,u) tail-signed by two distinct witnesses p,q:

  (v,u,p), (v,u,q) tight.                                 (CR.5)

Test D=(v,u) in the opposite actualization direction against all r in W, i.e. inspect

  (r,v,u).                                                (CR.6)

If (r,v,u) is tight for some r, D is head-signed by r; choosing one of p,q distinct from r, R523 gives a literal P4 with middle dimer D. If every (r,v,u) is bad, R3 gives

  (u,v,r) tight for every r in W,                         (CR.7)

so the reverse orientation D^op=(u,v) is tail-signed by all three witnesses. Again D and D^op share a common same-polarity witness and accepted R407 applies.

No informal reversal of a certified turn is used.

### 5. Refined same-parent output
Combining with SV44176, one common selected carrier/exterior crossing under three same-polarity witnesses yields, before unrelated payment lineages can erase the parent frame, at least one of:

1. a literal graph-intrinsic tight P4;
2. a literal graph-intrinsic tight P5;
3. a direct graph-intrinsic balanced pair of two disjoint signed dimers, total support mass four;
4. a bidirectional same-witness dimer saturation packet on the crossing marker, hence the accepted R407 fixed-anchor historical interaction.

The refinement is useful because the anonymous R523 collision label disappears. The first two outputs are explicit path geometry, the third enters the accepted mass-four payment machinery, and the fourth has an existing interaction compiler. No two R526 or R527 descendants are claimed to coexist: every premise used above is an ordered turn in the common parent frame.

### 6. Arm-M consequence
Apply this at either boundary dimer of every Arm-M pair-deletion cap frame from SV42382. Therefore each end of every such cap rail has, in any exact deletion frame chosen for the boundary dimer, an upstream output of one of the four forms above. In particular the G16 three-witness packet cannot dissolve into unrelated witness-indexed payment descendants without first leaving either explicit P4/P5 geometry, a direct mass-four pair birth, or the bidirectional R407 interaction certificate.

This still does not close Arm M: direct pair payment may return only an ancestry-bearing floor, and R407 records interaction rather than a two-cover. But the alternative-descendant loophole is now removed even from the collision branch.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R407"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    },
    {
        "relation": "dependency",
        "revision_id": "R526"
    }
]
```