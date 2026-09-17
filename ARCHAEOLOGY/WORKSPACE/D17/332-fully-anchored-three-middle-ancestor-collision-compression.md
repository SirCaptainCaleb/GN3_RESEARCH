# Three-middle ancestor compression: compatible-orientation calculation with cycle-closing and normalization gaps

**Workspace:** D17
**State:** working
**Key:** `fully-anchored-three-middle-ancestor-collision-compression`

**Summary:** Strategic-use correction to SV71686: with three internal middles in the displayed orientation compatible with the retained signed completion dimers, the seam calculation gives a labelled adjacent reversal, a literal P5 for p!=q, two overlapping tight P4s for p=q, or the stated R542 collision packet. The p=q cycle additionally requires (c,p,a), which the original proof did not establish. The orientation pigeonhole also does not by itself align the majority orientation with the already retained signed ancestors; that normalization requires a separate argument. Therefore the original unconditional every-frame / proper-C4 compression is not justified by the displayed proof. These specific gaps are fenced; this is not a disproof of the full global statement. G26 retains ancestor-family extinction as the strategic target.

### Strategic-use fence added by Astra after the G25 review
This section is provisional at two specific points. First, in the p=q branch, the three displayed turns do NOT alone certify a tight 4-cycle: the additional closing turn (c,p,a) is required. What is directly retained is the pair of overlapping tight P4s (p,a,b,c) and (a,b,c,p). A cyclic-break consumer must not be applied without the fourth turn.

Second, the orientation pigeonhole supplies three middles in ONE of the two outer orientations, not necessarily the orientation of the fixed signed ancestors in (TM.2). Swapping a,c and the labels L,R does not by itself prove that the resulting physical dimers still have the displayed orientations, polarities and witnesses. The calculations in Sections 3-5 apply when the three chosen middles and the retained ancestor packet have the displayed compatible orientation; a universal normalization argument for the other orientation is not supplied here.

These are identified proof gaps, not a counterexample to the full global statement. Use the compatible-orientation branch calculations and the overlapping-P4 conclusion only. The unconditional every-frame conclusion and the untested cycle conclusion are not presently justified by this proof. G26 records the strategic implications. Historical SV71686 remains the exact original unit.

### 1. Fully anchored endpoint ancestry
Let H be a hypothetical smallest Strong Level-(1) counterexample and fix a fully anchored physical endpoint pair

  E={a,c}.                                                 (TM.1)

Retain the stronger pre-singleton ancestry from the two completed R434 endpoint episodes as in SV57993. After the standard orientation normalization write

  L=(p,a),   tail-signed by an exact witness w_L,
  R=(c,q),   head-signed by an exact witness w_R.          (TM.2)

Thus the graph-intrinsic tight carrier trimers

  K_L=(p,a,w_L),
  K_R=(w_R,c,q)                                            (TM.3)

are retained. The reverse boundary dimers

  S_L=(a,p),
  S_R=(q,c)                                                (TM.4)

are therefore legitimate R542 short-carrier boundary supports whenever they acquire two same-polarity witnesses on the displayed tested orientations.

Choose any literal exact pair-deletion frame

  H-E=U|V.                                                 (TM.5)

### 2. Three same-oriented internal middles
Accepted R533 gives n=|V(H)|>10. Since U,V are nontrivial by R429, they have exactly four displayed rail endpoints and therefore at least

  n-6 >= 5                                                (TM.6)

internal vertices in total. For every internal vertex b, R3 makes exactly one of

  (a,b,c),   (c,b,a)                                      (TM.7)

tight. Hence three distinct internal vertices b_1,b_2,b_3 share one outer orientation. Exchange a,c and the labels L,R if necessary and retain

  (a,b_i,c) tight,  i=1,2,3.                              (TM.8)

This is the same orientation pigeonhole underlying SV58280, but here we retain the three actual middles themselves rather than immediately replacing them by an abstract P5.

### 3. Immediate adjacent-reversal exceptions
If some b_i=p, then J_i=(a,p,c) selects the physical state a->p while the retained ancestor L=(p,a) selects p->a. Thus the packet already contains a labelled adjacent selected-state reversal on {a,p}.

If some b_i=q, then J_i=(a,q,c) selects q->c while the retained ancestor R=(c,q) selects c->q, giving the analogous adjacent reversal on {c,q}.

Stop in either case. Hence assume from now on

  b_i notin {p,q} for i=1,2,3.                            (TM.9)

### 4. Two ancestor seam bits per middle
For each i test the two ordered seams

  lambda_i=(p,a,b_i),
  rho_i=(b_i,c,q).                                        (TM.10)

If for some i both seams are tight, combine them with (TM.8).

If p,q,b_i are pairwise distinct, the three consecutive turns

  (p,a,b_i), (a,b_i,c), (b_i,c,q)                         (TM.11)

make the literal vertex-simple tight P5

  (p,a,b_i,c,q).                                          (TM.12)

If p=q, the same three turns certify the two overlapping vertex-simple tight P4s

  (p,a,b_i,c),   (a,b_i,c,p).                              (TM.13)

The additional turn (c,p,a) would certify the proper tight 4-cycle, but is not supplied by (TM.11).

Thus the only branch left is that NO b_i passes both ancestor seams.

### 5. Pigeonhole forces a two-witness collision on one completion dimer
Assume no i has both lambda_i and rho_i tight. For every i at least one of lambda_i,rho_i is bad. Assign each i to one bad side, choosing arbitrarily if both are bad. Among three indices, two are assigned to the same side.

#### Left collision
Suppose lambda_i and lambda_j are bad for distinct i,j. Boundary antisymmetry gives

  (b_i,a,p),   (b_j,a,p) tight.                            (TM.14)

These are two HEAD certificates on the identical tested oriented dimer

  S_L=(a,p)                                                (TM.15)

with distinct witnesses b_i,b_j.

The old completion sign in (TM.2) says

  (p,a,w_L) tight.                                        (TM.16)

Hence K_L=(p,a,w_L) is a tight trimer and S_L=(a,p) is one of its reverse boundary dimers. Both collision witnesses lie outside K_L. Indeed b_i,b_j are distinct from a,p by (TM.9). If, say, b_i=w_L, then (TM.14) would give (w_L,a,p) tight while (TM.16) gives its complete reversal (p,a,w_L) tight, contradicting R3. Thus b_i,b_j != w_L.

Accepted R542 now applies exactly to K_L,S_L and witnesses b_i,b_j. It forces a same-frame capture/refund continuation and, because S_L has order two, a finite certificate-retaining continuation to

  TWO-COVER,
  or a descendant balanced opposite-sign pair with a singleton support.   (TM.17)

Accepted R428/R415 may then pay the remaining opposite support to a both-singleton floor or closure while retaining the R542 ancestry.

#### Right collision
If instead rho_i,rho_j are bad, R3 gives

  (q,c,b_i),   (q,c,b_j) tight.                            (TM.18)

These are two TAIL certificates on the identical tested dimer

  S_R=(q,c).                                               (TM.19)

Since R=(c,q) is head-signed by w_R,

  (w_R,c,q) tight,                                        (TM.20)

so K_R=(w_R,c,q) is a tight trimer and S_R=(q,c) its reverse boundary dimer. Again neither collision witness can equal w_R: if b_i=w_R, (TM.18) and (TM.20) would be complete reversals both tight. R542 therefore gives the exact dual of (TM.17).

### 6. Fully anchored three-middle compression
Combining Sections 3-5 gives the graph-intrinsic finite packet:

> THREE-MIDDLE ANCESTOR COMPRESSION. At a fully anchored endpoint pair with retained completion dimers L=(p,a) and R=(c,q), every exact pair-deletion frame contains three like-oriented internal middles. Those three middles force at least one of:
> 1. a labelled adjacent reversal against L or R;
> 2. a literal P5 through both completed endpoints and both ancestor secondaries;
> 3. two overlapping tight P4s when the two ancestor secondaries coincide (a proper cycle requires its additional closing turn);
> 4. an R542 two-witness capture/payment packet on the reverse boundary dimer of one retained completion trimer.

The R542 branch is not anonymous payment: it retains which completion dimer was hit, the two actual internal-middle witnesses, the old completion carrier trimer, the chosen exact H-E frame, and the R527/R526 capture ancestry.

### 7. Phase-zero consequence and fence
In the fixed-E phase-zero calculus, output 4 is a legitimate certificate-bearing paid excursion and can be fed through SV57138/SV57422. At a bottom fully anchored rank, a rank-flat paid return must immediately re-expose explicit nonquiet geometry; it is not a quiet sink.

The theorem does NOT yet consume outputs 1-3. In particular a P5, proper cycle, or adjacent reversal born at a phase-zero checkpoint cannot simply be sent to phase one and counted as progress. The remaining hard object has therefore been narrowed from arbitrary bilateral R445 geometry to large literal ancestor geometry versus a known payable collision packet.

R24, R5, and unusable R446/R358 are not used.

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
        "revision_id": "R533"
    },
    {
        "relation": "dependency",
        "revision_id": "R542"
    },
    {
        "relation": "dependency",
        "revision_id": "R415"
    },
    {
        "relation": "dependency",
        "revision_id": "R428"
    }
]
```