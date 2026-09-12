# The common-rail reciprocal cell has a chosen double-outgoing R176 collapse

**Workspace:** D17
**State:** established
**Key:** `common-rail-double-outgoing-r176-star-triangle-collapse`

**Summary:** In the synchronized G28 reciprocal cell, the same Q-state m->r is a selected cross-state between distinct components on BOTH deletion residues: H-{u,a} compares (c,v)|Q with (m,c,v)|Q_<m|Q_>m, while H-{c,v} compares (u,a)|Q with (u,a,m)|Q_<m|Q_>m. Hence R176 may be applied to the outgoing state on both sides; the apparent incoming/incoming nucleus is a choice, not a forced branch. On the right residue R176 tests (r,m,c)/(c,m,r): the first gives a second HEAD witness r on source dimer (m,c), colliding by R523 with source witness a. On the left it tests (r,m,a)/(a,m,r): the second gives a TAIL certificate on (a,m), opposite the source HEAD certificate from (u,a,m), hence the literal P4 (u,a,m,r). If both immediate outputs are avoided, (c,m,r), (r,m,a), and source (a,m,c) are tight, giving the directed star-triangle mc->mr->ma->mc in Gamma(H). Adding source vertex u produces a nonintegrable five-set, so R902 forces a Hamilton P5. Thus a lawful double-outgoing continuation always gives raw R523 collision, P4, or P5, hence PAYABLE-FOUR through the existing compilers. This removes incoming/incoming as an irreducible G28 local nucleus, but does not yet prove that the resulting distinct birth cannot flat-remint the same (K,m,Q) cell.

### 1. Input: the synchronized common-rail reciprocal cell
Retain the G28 common-rail residue from SV87107 and SV87835. Thus

  K=(u,a,m,c,v)

is the retained source P5, and there is one literal Hamilton residual rail

  Q=(...,ell,m,r,...)

on

  W=V(H)-{u,a,c,v},

with m internal, together with the reciprocal exact covers

  H-{u,a}=(c,v) | Q,
  H-{c,v}=(u,a) | Q.                                    (DO.1)

The two covers are graph-intrinsic facts on different deletion residues; they are not asserted simultaneously current representatives. The source P5 retains in particular

  (u,a,m), (a,m,c), (m,c,v) tight.                       (DO.2)

Split Q at m, excluding m from the two residual pieces, and write them Q_<m and Q_>m. Since m is internal, both are nonempty and r is the first vertex of Q_>m.

### 2. The outgoing state is available on BOTH reciprocal residues
On H-{u,a}, compare the literal two-cover

  T_R=(c,v) | Q

with the literal three-cover

  R_R=(m,c,v) | Q_<m | Q_>m.                             (DO.3)

The selected Q-state

  m -> r

has its endpoints in distinct R_R-components, namely (m,c,v) and Q_>m. Therefore accepted R176 applies directly to this chosen cross-state. No appeal to an arbitrary R159-selected crossing is needed.

On H-{c,v}, compare

  T_L=(u,a) | Q

with

  R_L=(u,a,m) | Q_<m | Q_>m.                             (DO.4)

The SAME selected physical state m->r again crosses distinct R_L-components, now (u,a,m) and Q_>m. Hence R176 applies to this outgoing state on the left reciprocal residue as well.

Thus the purported incoming/incoming nucleus is not a forced choice: a lawful chosen continuation may use the outgoing state on both reciprocal residues before any payment descendant is selected.

### 3. Right outgoing branch: source-dimer collision or the reverse turn (c,m,r)
Apply the explicit R176/P540 construction to (DO.3) with x=m, y=r. The R_R-component containing m is the trimer (m,c,v), so the unique old neighbour of m in that component is c. R176 therefore tests the exact reversal pair

  (r,m,c), (c,m,r).                                      (DO.5)

If (r,m,c) is tight, then the tested oriented dimer (m,c) is HEAD-signed by witness r. The retained source turn (a,m,c) makes the same tested dimer (m,c) HEAD-signed by the distinct witness a. Since r lies in W and a does not, r!=a. Accepted R523 gives a raw same-oriented two-head collision on (m,c).

Hence outside that collision retain

  (c,m,r) tight.                                          (DO.6)

### 4. Left outgoing branch: literal P4 or the reverse turn (r,m,a)
Apply R176 to (DO.4), again with x=m, y=r. The R_L-component containing m is the trimer (u,a,m), whose unique old neighbour of m is a. Thus R176 tests

  (r,m,a), (a,m,r).                                      (DO.7)

If (a,m,r) is tight, then (a,m) is TAIL-signed by witness r. But the retained source turn (u,a,m) makes the same tested oriented dimer (a,m) HEAD-signed by witness u. These are opposite-polarity certificates on one tested orientation, so accepted R523 gives the literal vertex-simple P4

  (u,a,m,r).                                              (DO.8)

Hence outside that P4 retain

  (r,m,a) tight.                                          (DO.9)

### 5. The joint survivor is a star-triangle, hence a Hamilton P5
Assume neither Section 3 nor Section 4 has already produced its displayed output. Then (DO.6), (DO.9), and the retained source turn (a,m,c) are all tight. In the comparison orientation Gamma(H) of accepted R887 these three turns are exactly

  mc -> mr,
  mr -> ma,
  ma -> mc.                                               (DO.10)

Thus the three ordinary edges mc,mr,ma form a directed star-triangle at the common middle m.

Choose the source vertex u as a fifth vertex. The five vertices

  {a,c,m,r,u}

are distinct because K is vertex-simple and r lies in W. The induced five-vertex boundary tournament already contains the directed comparison cycle (DO.10), so it is nonintegrable. Accepted R902 therefore forces a Hamilton tight P5 on this five-set.

Consequently the chosen double-outgoing continuation has the exhaustive parent output alphabet

  RAW R523 COLLISION on (m,c),
  LITERAL P4 (u,a,m,r),
  or LITERAL HAMILTON P5 on {a,c,m,r,u}.                  (DO.11)

### 6. G28 consequence
The P4/P5 alternatives are PAYABLE-FOUR by SV78086. The raw R523 collision parent-compiles through SV76748 to P4/P5, a direct mass-four pair, or R407; SV78086 and SV79137 make every resulting branch PAYABLE-FOUR.

Therefore the common-rail reciprocal P5 cell has a chosen certificate-retaining route back to PAYABLE-FOUR which does not inspect the incoming R176 branch at all. In particular the G28 `incoming/incoming' configuration is not an irreducible local nucleus: both reciprocal residues expose the same outgoing state m->r, and their two R176 calculations jointly collapse as above.

This is a local-kernel compression, not yet FLAT-REMINT NONREPETITION. The PAYABLE-FOUR packet produced by (DO.11) may itself be paid and may return rank-flat to the identical physical (K,m,Q) cell. No strict old-E descent is claimed from the output alone. The remaining G28 obligation is to use the distinct paid-birth ancestry to forbid that exact remint, not merely to manufacture another payable packet.

R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R176"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    },
    {
        "relation": "dependency",
        "revision_id": "R887"
    },
    {
        "relation": "dependency",
        "revision_id": "R902"
    }
]
```