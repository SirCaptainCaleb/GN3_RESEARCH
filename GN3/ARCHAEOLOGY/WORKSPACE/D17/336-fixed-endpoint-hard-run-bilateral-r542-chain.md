# A growth-free internal-middle run alternates and bilaterally R542-saturates every interior trimer

**Workspace:** D17
**State:** established
**Key:** `fixed-endpoint-hard-run-bilateral-r542-chain`

**Summary:** Iterate SV57707 together with SV72347 along one exact H-E rail. If three consecutive internal middles b,d,e occur in a run with no literal P4/P5 growth, their outer orientations must alternate; normalize J_b=(a,b,c), J_d=(c,d,a), J_e=(a,e,c). The local DOUBLE-REVERSE rows give (d,c,b) and (e,a,d). The no-growth branch of SV72347 on b,d additionally gives (b,a,d); its exact endpoint-dual on d,e gives (d,c,e). Hence the two reverse boundary dimers of the central trimer J_d are simultaneously saturated by the SAME witness pair {b,e}: (d,c) is tail-signed by b,e and (a,d) is head-signed by b,e. Accepted R542 is therefore available at both ends before any payment is chosen. More generally every growth-free consecutive hard run has alternating outer orientations and every interior middle carries this bilateral neighbor-witness R542 packet. The two R542 descendants are alternatives; no rank decrease or closure is claimed. The gain is a deterministic physical skeleton for the G26 recycling branch.


### 1. Three consecutive internal middles
Fix one ancestry-bearing aligned endpoint pair

  E={a,c}

and one literal exact pair-deletion frame

  H-E=U|V.

Suppose one displayed rail contains five consecutive vertices

  r -> b -> d -> e -> s,                                 (BR.1)

so b,d,e are three consecutive internal middles. Assume that applying the adjacent-middle compiler SV57707 and its sharpening SV72347 produces no literal P4/P5 growth on either adjacent pair {b,d} or {d,e}.

SV57707 then forces every local middle cell to be DOUBLE-REVERSE. Moreover adjacent DOUBLE-REVERSE cells with the same outer orientation already force a literal P4 by R584. Hence the outer orientations must alternate. After one fixed naming of E, normalize

  J_b=(a,b,c),
  J_d=(c,d,a),
  J_e=(a,e,c)                                             (BR.2)

all tight.

### 2. The central trimer gets both reverse boundary packets
The DOUBLE-REVERSE row at b, whose predecessor is r and successor is d, gives

  (b,a,r) tight,
  (d,c,b) tight.                                         (BR.3)

The DOUBLE-REVERSE row at d, in the opposite outer orientation and with predecessor b and successor e, gives

  (d,c,b) tight,
  (e,a,d) tight.                                         (BR.4)

Now use the sharpened adjacent-pair theorem SV72347 on the pair b,d. Its only non-P4 branch tests (d,a,b) as bad and therefore, by R3, retains

  (b,a,d) tight.                                         (BR.5)

Apply the exact endpoint-dual of the same calculation to the pair d,e, exchanging a and c. The P4 branch would have (e,c,d) tight and hence (a,e,c,d) tight. By the no-growth hypothesis that branch is absent, so (e,c,d) is bad and R3 gives

  (d,c,e) tight.                                         (BR.6)

Consider the CENTRAL carrier

  J_d=(c,d,a).                                            (BR.7)

Its reverse initial boundary dimer is

  S_L=(d,c).

Equations (BR.3) and (BR.6) say on the identical tested orientation

  (d,c,b), (d,c,e) tight,                                (BR.8)

so S_L is tail-signed by the two distinct exterior witnesses b,e.

Its reverse terminal boundary dimer is

  S_R=(a,d).

Equations (BR.4) and (BR.5) say

  (e,a,d), (b,a,d) tight,                                (BR.9)

so S_R is head-signed by the SAME witness pair b,e.

The vertices b,e lie outside J_d because the displayed rail and the proper turn are vertex-simple. Therefore accepted R542 applies independently to both S_L and S_R, with identical exterior witness set {b,e}.

### 3. Bilateral saturation is simultaneous parent data
The two R542 packets in (BR.8)--(BR.9) are graph-intrinsic consequences of the one source frame (BR.1). They coexist as historical source certificates BEFORE any R542 payment continuation is chosen. No assertion is made that their paid descendants coexist.

Thus a growth-free triple of consecutive internal middles forces one BILATERALLY SATURATED central trimer:

  J_d=(c,d,a),
  reverse initial (d,c) tail-witnessed by b,e,
  reverse terminal (a,d) head-witnessed by b,e.           (BR.10)

This is stronger than two unrelated R542 opportunities: the carrier, both tested boundary orientations, and the complete two-vertex witness set are shared physical parent data.

### 4. Arbitrary hard runs
Let

  v_0 -> v_1 -> ... -> v_{m+1}

be a segment of one exact H-E rail with v_1,...,v_m internal and m>=3. Suppose every local middle cell v_i avoids the literal P4/P5 outputs of SV57707 and every adjacent pair avoids the literal-growth branch of SV72347.

Then:

1. every v_i is DOUBLE-REVERSE;
2. the outer orientations of J_{v_i} alternate along the rail, since equal orientations on adjacent cells force a P4 by SV57707;
3. for every interior index 2<=i<=m-1, the two reverse boundary dimers of J_{v_i} are each signed by BOTH rail neighbors v_{i-1},v_{i+1}, with the polarity prescribed by the orientation of J_{v_i}.

Point 3 is exactly the translated calculation of Sections 1--2 on the triple v_{i-1},v_i,v_{i+1}.

Hence every growth-free hard run is an ALTERNATING BILATERAL R542 CHAIN. The unresolved recycling branch has a deterministic physical embedding in one actual source rail rather than an arbitrary sequence of payment portals.

### 5. Scope fence
This theorem does not consume R542. Each R542 continuation may close or may return through payment/steering to a rank-flat phase-zero state, exactly the G26 scope gap. No numerical bottom-rank decrease is claimed, and the two boundary payments at one central trimer are alternatives.

Nor does bilateral saturation by two witnesses alone imply a Hamilton P5: the local five-vertex packet is consistent. The gain is family-level compression. Any reconstruction-closed bottom survivor containing a sufficiently long hard rail must retain an alternating sequence of source-visible trimers whose two reverse boundary dimers are simultaneously saturated by their neighboring rail vertices. A future extinction theorem therefore needs to absorb this one explicit chain architecture, not an unrestricted R542 history.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R542"
    }
]
```