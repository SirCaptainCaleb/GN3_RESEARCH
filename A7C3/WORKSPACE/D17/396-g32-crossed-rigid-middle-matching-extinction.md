# Endpoint P5-freeness extinguishes the crossed rigid middle-matching residue

**Workspace:** D17
**State:** established
**Key:** `g32-crossed-rigid-middle-matching-extinction`

**Summary:** Retain the G32 transitive spectator gate frame and the rigid no-B-active-omission residue of SV100744. In the crossed R582 gate, the two possible choices of active M_S edge are both impossible once the already-retained P5-freeness of X+L and X+R is spent. In normalized cell notation M_R={ab,cz}>M_S={ac,bz}>M_L={bc,az}, L-outgoing M_S edge {b,z}, and crossed R-incoming edge {a,c}. If {a,c} is the active source-spoke pair, P5-freeness of X+L and X+R forces zLc and zRc; forbidding favorable omission of active a forces Rcb,Lcb,RzL, after which R-z-L-c-b is a tight endpoint-favorable P5 omitting a, contradiction. If {b,z} is active, endpoint P5-freeness forces zLa,zRa; forbidding favorable omission of active b forces czL,czR,RaL, after which c-z-R-a-L is a tight endpoint-favorable P5 omitting b, contradiction. Therefore every crossed live packet has an endpoint-favorable K_s omitting a B-active source spoke. The rigid exceptional branch of SV100744 can survive only in the aligned gate. R24 and R5 are unused.

### 1. Setup
Retain the G32 singleton-star spectator gate frame and the source-active reduction of SV100744. Normalize the transitive matching-height cell exactly as in R582/P660:

  X={a,b,c,z},
  M_R={ab,cz} > M_S={ac,bz} > M_L={bc,az}.

Let the left spectator endpoint be L and the right endpoint be R. Normalize the L-outgoing middle gate to {b,z}, so

  Lbz, Lzb, acL, caL

are tight. Work in the CROSSED gate, so the R-incoming middle gate is {a,c}, hence

  acR, caR, Rbz, Rzb

are tight. The matching-height cell supplies in particular

  zbc, zca

and the other standard cell turns. By SV99565, both X+L and X+R are Hamilton-P5-free.

SV100744 says that if no endpoint-favorable R582 path omits a B-active source spoke, then exactly two source spokes are B-active and they form one whole M_S edge; the complementary M_S edge consists of the center v and the unique B-inactive source spoke. In the crossed gate either M_S edge could a priori be the active one. We eliminate both possibilities.

### 2. Active edge {a,c}
Assume the B-active source spokes are a and c. By hypothesis there is no endpoint-favorable Hamilton P5 omitting a or c.

First spend endpoint P5-freeness. The five-word

  a,c,L,z,b

has acL and Lzb tight. Since X+L is P5-free, cLz is bad; R3 gives

  zLc tight.                                           (CG.1)

Likewise a,c,R,z,b has acR and Rzb tight. P5-freeness of X+R forces cRz bad, hence

  zRc tight.                                           (CG.2)

Now use the no-active-omission hypothesis. The endpoint-favorable candidate

  L,z,b,c,R

omits active a and has Lzb,zbc tight. Therefore bcR is bad and

  Rcb tight.                                           (CG.3)

Similarly R,z,b,c,L omits a and forces

  Lcb tight.                                           (CG.4)

Next L,z,R,c,b omits active a and has zRc,Rcb tight, so LzR is bad and

  RzL tight.                                           (CG.5)

But now

  R,z,L,c,b

is a tight Hamilton P5: its turns are RzL, zLc, Lcb. It is endpoint-favorable and omits active a. Contradiction.

Thus {a,c} cannot be the active edge in a crossed rigid residue.

### 3. Active edge {b,z}
Assume instead that b,z are the B-active source spokes, so no endpoint-favorable Hamilton P5 may omit b or z.

P5-freeness of X+L applied to

  a,L,z,b,c

uses Lzb,zbc and forces aLz bad, hence

  zLa tight.                                           (CG.6)

Likewise a,R,z,b,c in X+R forces

  zRa tight.                                           (CG.7)

Now the endpoint-favorable candidate

  L,z,c,a,R

omits active b and has zca,caR tight. Thus Lzc is bad and

  czL tight.                                           (CG.8)

The dual candidate R,z,c,a,L forces

  czR tight.                                           (CG.9)

Next c,z,L,a,R omits active b and has czL,zLa tight, so LaR is bad and

  RaL tight.                                           (CG.10)

But then

  c,z,R,a,L

is a tight Hamilton P5 with turns czR,zRa,RaL. It is endpoint-favorable and omits active b, contradiction.

Thus {b,z} also cannot be the active edge.

### 4. Consequence
Both possible exceptional active M_S edges are impossible in the crossed gate. Therefore every crossed G32 packet admits an endpoint-favorable R582 path K_s omitting a B-active source spoke s, together with an actual selected old source incidence from s into B.

Equivalently, the rigid no-active-omission residue of SV100744 survives only in the ALIGNED gate. This is a true contraction of the second G32 moonshot: crossed gate analysis no longer belongs to the hard full-H splice.

### 5. Scope
This section does not yet complete the full-H splice in the easy B-active branch. It only removes the crossed exceptional residue. Every forcing step is a literal forbidden-P5 test followed by R3; no finite-search assertion is used as proof. R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
