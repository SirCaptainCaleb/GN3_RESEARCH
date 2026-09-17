# The alternating adjacent double-hinge atom is a literal P4 or an R542 two-witness packet

**Workspace:** D17
**State:** established
**Key:** `fixed-endpoint-double-hinge-r542-collapse`

**Summary:** Sharpen SV57707 in its only non-growth adjacent-middle branch. In the opposite-outer-orientation DOUBLE-REVERSE cell r->b->d->s with J_b=(a,b,c), J_d=(c,d,a), test the single turn (d,a,b). If it is tight, J_d concatenates to the literal P4 (c,d,a,b). If it is bad, R3 gives (b,a,d) tight. The old DOUBLE-REVERSE certificate already gives (b,a,r) tight, so the identical tested oriented dimer S=(b,a) is tail-signed by two distinct witnesses r,d. Since S is the reverse boundary dimer of the retained carrier J_b=(a,b,c), both witnesses lie outside J_b, and accepted R542 applies. Hence the double-hinged floor-remint packet is not an independent terminal species: every adjacent hard pair gives literal turn growth or a certificate-bearing R542 capture/payment packet. R542 recycling may return rank-flat to the bottom family and is explicitly not counted as progress; this result only reduces the family alphabet.


### 1. Input: the alternating DOUBLE-REVERSE cell
Retain the exact common-parent packet of `fixed-endpoint-adjacent-middle-growth-or-double-hinge` (SV57707). Thus

  H-E=U|V,   E={a,c},

is one literal exact pair-deletion frame in a hypothetical smallest Strong Level-(1) counterexample, and one displayed rail contains four consecutive vertices

  r -> b -> d -> s.                                      (DH.1)

Assume both adjacent middle cells are in the only non-growth local state, DOUBLE-REVERSE, and that their outer orientations are opposite. Normalize exactly as in SV57707:

  J_b=(a,b,c),
  J_d=(c,d,a)                                             (DH.2)

are tight. The retained DOUBLE-REVERSE certificates include

  (b,a,r) tight,
  (d,c,b) tight,
  (s,a,d) tight.                                         (DH.3)

In particular the tested oriented dimer

  S=(b,a)                                                 (DH.4)

is tail-signed by witness r.

SV57707 used the four resulting dimers to produce two R547 floor births on {b,d}. We now consume that apparent terminal atom before paying either floor.

### 2. One additional turn test
Test the single ordered turn

  (d,a,b).                                                (DH.5)

If (DH.5) is tight, concatenate it with the retained turn J_d=(c,d,a). The two consecutive tight turns

  (c,d,a), (d,a,b)

make the literal vertex-simple tight P4

  (c,d,a,b).                                              (DH.6)

So this branch is explicit strict path geometry.

Assume instead that (d,a,b) is bad. Boundary antisymmetry R3 gives its complete reversal

  (b,a,d) tight.                                         (DH.7)

Together with (b,a,r) from (DH.3), the identical tested oriented dimer S=(b,a) is now tail-signed by the two distinct witnesses

  r, d.                                                   (DH.8)

They are distinct because r,b,d,s are consecutive distinct vertices of one path.

### 3. Exact R542 fit
The retained source turn

  J_b=(a,b,c)                                             (DH.9)

is a tight trimer. Its reverse initial boundary dimer is exactly

  (b,a)=S.                                                (DH.10)

Thus (DH.7) and the first certificate in (DH.3) are two same-polarity certificates on the same tested reverse boundary dimer required by accepted R542.

Both witnesses lie outside the carrier J_b. The witness d is distinct from a,b,c because d is another physical rail vertex and J_d=(c,d,a) is vertex-simple. The witness r is distinct from a,b,c: r is distinct from a,b by (DH.1), and if r=c then the selected frame H-{a,c} would contain c, impossible. Hence

  r,d notin V(J_b).                                       (DH.11)

Accepted R542 therefore applies to carrier J_b, reverse boundary dimer S=(b,a), and witnesses r,d. It yields the exact same-frame capture/refund alternative and, because S has order two, a finite certificate-retaining continuation to

  TWO-COVER,
  or a descendant balanced opposite-sign pair with a singleton support. (DH.12)

The continuation retains J_b, the tested orientation (b,a), witnesses r,d, the original exact H-E frame, and the R542/R527/R526 capture ancestry.

### 4. Adjacent-middle consequence
Combining with SV57707 gives the sharpened adjacent-middle compiler:

> Every pair of consecutive internal middles in one exact H-E rail yields either literal P4/P5 turn growth, or an R542 two-witness capture/payment packet. The former DOUBLE-HINGE floor-remint output is not an independent terminal species.

Indeed SV57707 already proves literal growth unless both cells are DOUBLE-REVERSE. Same outer orientation of two DOUBLE-REVERSE cells gives a literal P4 by R584. Opposite outer orientation is the packet above and gives either the literal P4 (DH.6) or R542.

### 5. Bottom-family fence
This is a structural compression, not bottom-family extinction. In the R542 branch, accepted payment may return to the same fully anchored phase-zero stratum with no decrease of the exhausted fixed-E clock. G26 therefore requires this R542 ancestry to remain in the typed bottom-family state. No claim is made that collision/payment is contradictory, that its paid descendant is simultaneously current with the source frame, or that a P4/P5 born at phase zero is numerical progress.

The gain is narrower and exact: an alternating DOUBLE-HINGE is no longer a third family species. A reconstruction-closed survivor that absorbs every adjacent hard middle pair must absorb only two kinds of output from this compiler: literal path geometry and ancestry-bearing R542 recycling.


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