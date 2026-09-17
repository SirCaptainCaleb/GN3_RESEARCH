# Deleting the middle core vertex extinguishes the selected-reversal-only fourth-puncture residue

**Workspace:** D17
**State:** established
**Key:** `universal-one-extension-pair-core-triangle-middle-puncture-reversal-extinction`

**Summary:** In the quiet cyclic pair-core triangle normal form SV31722, write the common trimer order T=(u,v,w) and exterior pair cycle a<b, b<c, c<a in one common insertion slot. Suppose the R195-forced fourth Hamilton puncture is U-v, deleting the middle core vertex. Let R be any Hamilton path on U-v. If every comparison of R with the three perimeter paths is either R435-quiet or has an adjacent selected-state reversal, then a four-slot order check forces exactly one quiet comparison; after cyclic relabeling R has one of a,c,b,u,w; u,a,c,b,w; u,a,c,b,w; u,w,a,c,b according to the common slot. In each slot the inherited perimeter turns plus R either directly give a Hamilton P6 on U or leave exactly one turn paired with its complete reversal in a second candidate P6, so R3 makes one candidate Hamiltonian. This contradicts non-Hamiltonicity of U. Hence when the mandatory fourth puncture deletes the middle core vertex, at least one comparison must emit reverse-trimer or proper-cycle R435 geometry rather than only selected reversal. Those outputs are already currentized by SV32145 into fresh/closed maximum-three-forest dynamics. The endpoint-core deletions are not claimed impossible.


### 1. Setup
Retain the quiet cyclic pair-core triangle of SV31722. Thus

  U=T union {a,b,c},   T=(u,v,w),

U is non-Hamiltonian, and the three Hamilton punctures

  P_ab on T+{a,b},
  P_bc on T+{b,c},
  P_ca on T+{c,a}

share the literal core order u,v,w. The three exterior labels occupy one common insertion slot, and their retained pair orders form the cycle

  a < b in P_ab,   b < c in P_bc,   c < a in P_ca.       (MP.1)

Assume the additional Hamilton puncture supplied in the fourth-puncture argument deletes the middle core vertex v. Thus

  R is a Hamilton path on U-v={u,w,a,b,c}.                (MP.2)

We prove that R cannot interact with all three perimeter paths using only R435-quiet comparisons and adjacent selected-state reversals.

### 2. Order lemma for the selected-reversal-only hypothesis
Assume every comparison R versus P_ab,P_bc,P_ca is either R435-quiet or has a common selected dimer occurring in the opposite order in the two paths.

Comparing the four common contacts in each pair gives the following elementary order table. In each row, up to the cyclic relabeling a->b->c->a, the only possible R-word is shown; in particular exactly one of the three comparisons is quiet.

| common insertion slot | quiet pair | forced order of R |
|---|---|---|
| before u | P_ab | (a,c,b,u,w) |
| u|v | P_ab | (u,a,c,b,w) |
| v|w | P_ab | (u,a,c,b,w) |
| after w | P_ab | (u,w,a,c,b) |

The two cyclic relabelings give the cases quiet against P_bc or P_ca. To verify the table, restrict R successively to the four common labels of P_ab,P_bc,P_ca. Quietness preserves that four-label order. A nonquiet comparison which is allowed only the selected-reversal branch must reverse one literal adjacent common dimer of the corresponding perimeter word. Chasing the cyclic pair relations (MP.1) leaves exactly the displayed word. In particular zero quiet comparisons and two quiet comparisons are both impossible under the selected-reversal-only hypothesis.                                              (MP.3)

It therefore suffices by cyclic symmetry to treat the four displayed P_ab-quiet words.

### 3. Boundary slots give an immediate Hamilton P6
If the common slot is before u, the perimeter paths have the forms

  P_ab=(a,b,u,v,w),
  P_bc=(b,c,u,v,w),
  P_ca=(c,a,u,v,w),

and (MP.3) gives R=(a,c,b,u,w). The six-word

  (a,c,b,u,v,w)                                           (MP.4)

is tight: its first two turns (a,c,b),(c,b,u) are consecutive turns of R, while (b,u,v),(u,v,w) are inherited perimeter turns. Hence U is Hamiltonian, contradiction.

If the common slot is after w, the exact terminal dual applies. The perimeter words are

  (u,v,w,a,b), (u,v,w,b,c), (u,v,w,c,a),

R=(u,w,a,c,b), and

  (u,v,w,a,c,b)                                           (MP.5)

is a Hamilton P6, using the first two turns from the perimeter family and the last two from R.

### 4. The two internal slots reduce to one R3 dichotomy
Suppose the common slot is u|v. Then

  P_ab=(u,a,b,v,w),
  P_bc=(u,b,c,v,w),
  P_ca=(u,c,a,v,w),

and R=(u,a,c,b,w). Consider

  A=(u,a,c,b,w,v),
  B=(u,c,a,v,w,b).                                        (MP.6)

Every turn of A is certified by R or the perimeter paths except possibly (b,w,v). Every turn of B is certified except possibly (v,w,b). These two missing turns are complete reversals. By R3 exactly one is tight, so A or B is a Hamilton P6 on U, contradiction.

Suppose instead the common slot is v|w. Then

  P_ab=(u,v,a,b,w),
  P_bc=(u,v,b,c,w),
  P_ca=(u,v,c,a,w),

and again R=(u,a,c,b,w). Consider

  A=(v,u,a,c,b,w),
  B=(a,u,v,b,c,w).                                        (MP.7)

Every turn of A is certified except possibly (v,u,a); every turn of B is certified except possibly (a,u,v). These are complete reversals, so R3 again makes one of A,B Hamiltonian on U, contradiction.

### 5. Consequence
Thus, when the mandatory fourth Hamilton puncture deletes the middle vertex v of the common trimer order, the selected-reversal-only hypothesis is impossible. At least one comparison of R with P_ab,P_bc,P_ca must therefore take a reverse-trimer or proper-cycle R435 branch. By the currentization already retained in SV32145, that output enters actual fresh maximum-three-forest dynamics or a closed movable-break orbit.

The middle position is load-bearing. This argument does not assert the same conclusion when the fourth puncture deletes u or w; endpoint-core deletion selected-reversal residues remain open.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R195"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    }
]
```
