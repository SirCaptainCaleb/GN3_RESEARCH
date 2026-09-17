# A stationary R696 witness sandwich either closes H or shifts to a final-gap boundary packet

**Workspace:** D17
**State:** working
**Key:** `stationary-r696-sandwich-shift`

**Summary:** Corrected SANDWICH shift: non-Hamiltonicity of X+p or Y+p directly forces the two turns giving an R542 packet on (u_X,p) or (u_Y,p). The former punctured-complement spanning-cover claims are withdrawn; the final-gap packet conclusion survives without them.

### Exact stationary SANDWICH packet and correction
Retain the stationary R542 packet on reverse boundary dimer (c,d) of the tight trimer (d,c,p), with witnesses u_X,u_Y. Accepted R696 SANDWICH supplies an actual selected tight trimer (u_X,p,u_Y) or (u_Y,p,u_X) in an exact H-{c,d} cover.

Write X=(a_1,...,a_{k-1},u_X), Y=(b_1,...,b_{k-1},u_Y), with k>=4. R953 gives non-Hamiltonicity of X+p and Y+p. Retain the quiet Hamilton punctures K_A=(a_1,...,a_{k-2},p,a_{k-1}) and K_B=(b_1,...,b_{k-2},p,b_{k-1}).

Correction to DR17.94: its claimed Hamilton complement B+Z, with B=Y-u_Y, is not supplied by R953; R953 supplies full petal pair unions. In the dual displayed proposed cover, X+Z overlaps the proposed path at u_X. Those spanning-cover justifications are withdrawn. The shift conclusion survives by the shorter non-Hamiltonicity argument below, which needs neither punctured complement.

### First sandwich orientation
Suppose (u_X,p,u_Y) is tight. The turn (a_{k-1},u_X,p) must be bad: if tight, the literal historical path X followed by p would already Hamiltonize X+p, contrary to R953. Thus (p,u_X,a_{k-1}) is tight.

Next (a_{k-2},p,u_X) must be bad. If tight, the literal word
  (a_1,...,a_{k-2},p,u_X,a_{k-1})
would Hamiltonize X+p. Its earlier turns are inherited from K_A, and its two new turns are exactly the tested turn and (p,u_X,a_{k-1}). Therefore (u_X,p,a_{k-2}) is tight.

Together with (u_X,p,u_Y), this gives two tail witnesses a_{k-2},u_Y on the tested dimer (u_X,p). The tight carrier (p,u_X,a_{k-1}) has this as its reverse initial boundary dimer. Both witnesses are distinct and outside the carrier. R542 applies with complementary singleton a_{k-1}. Thus the packet shifts to the exact final-gap dimer (u_X,p), preserving the selected sandwich as one witness turn.

### Other sandwich orientation
If (u_Y,p,u_X) is tight, non-Hamiltonicity of Y+p forces (b_{k-1},u_Y,p) bad, hence (p,u_Y,b_{k-1}) tight. The exact K_B prefix then forces (b_{k-2},p,u_Y) bad, hence (u_Y,p,b_{k-2}) tight. R542 applies on (u_Y,p), the reverse initial boundary of (p,u_Y,b_{k-1}), with witnesses u_X,b_{k-2} and complementary singleton b_{k-1}. No actual path is reversed.

### Scope
SANDWICH always supplies the stated final-gap packet under these hypotheses. This is a packet shift, not a proved strict descent or spanning-cover construction. END and FREE remain separate R696 outputs. Repeated application requires currentizing the new carrier, complementary singleton and witness roles in the newly required deletion fiber.

Status: corrected complete internal deduction, unreviewed. Uses accepted R3/R542/R696/R953 and the working quiet terminal-puncture input. No Hamilton deletion of a full pair-union is inferred.

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
    },
    {
        "relation": "dependency",
        "revision_id": "R696"
    },
    {
        "relation": "dependency",
        "revision_id": "R953"
    }
]
```
