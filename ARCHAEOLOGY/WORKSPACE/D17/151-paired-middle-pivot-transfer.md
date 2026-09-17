# A doubled same-residue head discrepancy forces an actual pivot-transfer cover

**Workspace:** D17
**State:** established
**Key:** `paired-middle-pivot-transfer`

**Summary:** For the paired HHH pair-deletion covers T_U=(i,P_U)|P_V and T_V=P_U|(i,P_V), one R3 test on {u_1,i,v_1} always gives a third exact cover of the same residue, transferring u_1 onto the i+V rail or v_1 onto the i+U rail. Across the three circuit labels, two transfers share a direction; they Hamiltonize the target core together with the transferred pivot and those two labels, forcing the punctured source core plus the third label to be non-Hamiltonian and hence the source core to have order at least four. Comparing T_U and T_V directly in both directions also gives two R176 pair births whose nontrivial dimers {i,u_1} and {i,v_1} have opposite polarity under the same pivot test. This supplies a genuinely coupled paid-floor front door via either R176 birth followed by R428, while the other middle and both exact covers remain retained witnesses. R547 applies to the signed dimer hinge at the graph-intrinsic level; no cross-lineage steering claim is made from that hinge alone.

### 1. Double-prepend pivot transfer on one exact residue
Work in the HHH branch of the paired constant-role hexagon. Write

  P_U=(u_1,u_2,\\ldots,u_r), \\qquad P_V=(v_1,v_2,\\ldots,v_s),

with r,s\\ge 2, and fix a circuit label i with the other two labels j,k deleted. The preceding section supplies two literal exact covers of the same residue G=H-\\{j,k\\}:

  T_U=(i,P_U)\\mid P_V, \\qquad T_V=P_U\\mid(i,P_V).                         (PT.1)

Apply boundary antisymmetry R3 only to the reversal pair with middle i on the physical triple \\{u_1,i,v_1\\}. Exactly one of

  (u_1,i,v_1), \\qquad (v_1,i,u_1)

is tight. If (u_1,i,v_1) is tight, then

  C_i^U=(u_1,i,v_1,v_2,\\ldots,v_s)\\mid(u_2,\\ldots,u_r)                  (PT.2U)

is a literal exact two-cover of G: after the new bridge turn, every remaining turn on the first rail is inherited from (i,P_V), and the second rail is a literal suffix of P_U. If instead (v_1,i,u_1) is tight, then

  C_i^V=(v_1,i,u_1,u_2,\\ldots,u_r)\\mid(v_2,\\ldots,v_s)                  (PT.2V)

is a literal exact two-cover. The rail floor r,s\\ge2 makes the displayed suffix rail nonempty even in the smallest case.

Thus the doubled endpoint/internal discrepancy has an immediate same-residue support consequence: relative to T_V, (PT.2U) transfers the single physical vertex u_1 from U onto i+V; relative to T_U, (PT.2V) transfers v_1 from V onto i+U. No payment, floor steering, or historical interaction theorem is used. Call the two alternatives U\\to V and V\\to U respectively. The TTT branch is the exact tail dual.

More generally, if disjoint tight paths A=(a,A') and B=(b,B') both have order at least two and a pivot x gives exact covers (x,A)\\mid B and A\\mid(x,B) of one residue, R3 on \\{a,x,b\\} forces either A'\\mid(a,x,B) or B'\\mid(b,x,A) as a third exact cover of that same residue.

### 2. Three circuit labels force a repeated transfer direction
Apply the preceding construction separately to i,j,k. Each circuit label receives one transfer bit in \\{U\\to V,V\\to U\\}. Two labels, say a,b, have the same bit. Suppose first both are U\\to V. Then

  (u_1,a,v_1), \\qquad (u_1,b,v_1)

are tight, and the original HHH source extensions give (a,v_1,v_2) and (b,v_1,v_2). R3 on \\{a,u_1,b\\} chooses exactly one of (a,u_1,b),(b,u_1,a). In the first case

  (a,u_1,b,v_1,v_2,\\ldots,v_s)

is a Hamilton path on V\\cup\\{u_1,a,b\\}; in the second case interchange a and b. Hence

  V+u_1+a+b \\quad\\text{is Hamiltonian}.                                  (PT.3U)

Let c be the third circuit label. Its physical complement in H is (U-u_1)+c. Since H is a counterexample, (U-u_1)+c cannot be Hamiltonian. In particular r\\ge4: if r=2 the complement is a dimer, and if r=3 it is a three-set, so it is Hamiltonian in either case. Testing the literal proposal

  (c,u_2,u_3,\\ldots,u_r)

then shows that its only new first turn (c,u_2,u_3) is bad, so R3 gives the exact reverse-head shield

  (u_3,u_2,c) \\quad\\text{tight}.                                         (PT.4U)

The V\\to U majority is the exact dual: U+v_1+a+b is Hamiltonian, (V-v_1)+c is non-Hamiltonian, s\\ge4, and (v_3,v_2,c) is tight.

Thus the three-label packet cannot consist merely of three independent endpoint/internal discrepancies. It contains a repeated-direction transfer pair, a strictly larger Hamilton support on the target side, and an exact nonextension/shield on the punctured source side. This new reverse-head shield sits opposite the reverse-terminal shields already retained from the paired hexagon.

### 3. The same pivot test couples the two direct R176 births
There is also a cleaner paid-floor entrance than puncturing one middle first. Stay on the common proper residue G=H-\\{j,k\\} and compare the two exact covers (PT.1) directly.

Use T_U as the source cover and T_V as the comparison cover. The selected directed state i v_1 of T_V crosses the two T_U components, while i lies on the nontrivial source rail (i,P_U) with literal neighbor u_1. Choose either spare outer vertex d in \\{j,k\\}. Accepted R176/P540 therefore gives a genuine pair birth whose nontrivial support is an oriented dimer on \\{i,u_1\\} and whose opposite support is the singleton (d). Dually, using T_V as source and T_U as comparison, the selected state i u_1 crosses the two T_V components; i lies on (i,P_V) with literal neighbor v_1, so R176 gives a second genuine pair birth with nontrivial dimer on \\{i,v_1\\}.

The two dimer polarities are not independent. If the pivot transfer is U\\to V, so (u_1,i,v_1) is tight, the first R176 proof takes

  D_U=(u_1,i) \\quad\\text{tail-signed by }v_1,

while the reverse comparison takes

  D_V=(i,v_1) \\quad\\text{head-signed by }u_1.

If the pivot transfer is V\\to U, so (v_1,i,u_1) is tight, then

  D_U=(i,u_1) \\quad\\text{head-signed by }v_1,
  D_V=(v_1,i) \\quad\\text{tail-signed by }u_1.

Hence in either branch D_U and D_V are opposite-polarity nontrivial dimers meeting exactly at i, and the same R3 bit both chooses the actual transfer cover (PT.2) and chooses the signs of the two R176 births. Accepted R547 may therefore cut their common hinge i and produce the graph-intrinsic opposite-sign singleton pair on u_1,v_1. Because the two dimers belong to distinct R176 births, no claim is made here that this R547 singleton pair by itself is one steerable ancestry-bearing floor; that would require an explicit lineage-composition statement.

If a paid checkpoint is actually needed, no such composition is necessary. Take either one of the two R176 births. Its opposite support is already the chosen singleton d and its dimer support is nontrivial, so accepted R428 applies with d fixed and yields either a spanning two-cover or an ancestry-bearing both-singleton floor. Choosing d=j leaves only the k coordinate to install by the one-coordinate case of R432/R433. Throughout this paid continuation, T_U,T_V, both physical middle coordinates u_1,v_1, the two selected cross states i v_1 and i u_1, and the pivot-transfer orientation remain retained historical witnesses even though they need not remain current representatives.

The point is that payment is downstream of the coupled same-residue geometry. The doubled discrepancy first yields an actual support-transfer cover and two opposite-signed R176 dimer births; only then, if necessary, one may spend one birth into the fixed-turn floor machinery.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R176"
    },
    {
        "relation": "dependency",
        "revision_id": "R547"
    },
    {
        "relation": "dependency",
        "revision_id": "R428"
    },
    {
        "relation": "dependency",
        "revision_id": "R432"
    }
]
```
