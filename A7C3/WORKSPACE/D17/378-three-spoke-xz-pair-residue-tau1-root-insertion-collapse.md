# The tau=1 x/z pair-residue cell closes or emits source-pinned R523/R435 geometry

**Workspace:** D17
**State:** established
**Key:** `three-spoke-xz-pair-residue-tau1-root-insertion-collapse`

**Summary:** In the DR17.520 x/z pair residue with (p,tau)=(2,1), R560 makes S={a,y,c} one contiguous Hamilton trimer block and the other W-block a pure rail. Comparing the S-block with source (a,y,c), any different literal order gives R435; otherwise F is (a,y,c)B|C or B(a,y,c)|C. In the first form x prepends automatically using (x,a,y), giving an exact H-z row. Inserting z immediately after c requires only the boundary seam (c,z,b0); if it fails, R3 gives (b0,z,c), a second head witness on (z,c) beside source (a,z,c), hence R523. If it passes, an exact H-x row results. The B(a,y,c) form is dual: z appends automatically using (y,c,z), while insertion of x before a requires one seam whose failure collides on (a,x). In either successful restoration branch one of the roots is inserted internally between the source trimer and the nonempty W-block, so SV93413 gives R159. Hence tau=1 has no quiet survivor.

### 1. Unique-transition normal form
Retain K=(x,a,y,c,z), S={a,y,c}, W=H-K and an exact H-{x,z} cover F in the DR17.520 cell

  p=2,  tau=1.

By R560, all three S-vertices form one contiguous Hamilton S-block on the unique mixed rail and the other F-rail is a pure W-block. Compare the S-block with the retained source trimer (a,y,c) by R435. Outside adjacent reversal/reverse-trimer/cycle geometry, the literal order is exactly (a,y,c). Therefore, after naming the two nonempty W-blocks B,C, the only quiet forms are

  F=(a,y,c) B | C,
  or
  F=B (a,y,c) | C.                                      (T1.1)

### 2. Source-trimer followed by W
Suppose F=(a,y,c)B|C, with B=(b_0,...). Prepend x to the mixed rail. The source turn (x,a,y) is tight and every later turn was already certified in F, so

  T_z=(x,a,y,c)B | C

is an exact two-cover of H-z whose x-trim is F.

To restore z, insert it immediately after c. The source turn (y,c,z) is tight. The only new boundary turn is (c,z,b_0). If it is tight,

  T_x=(a,y,c,z)B | C

is an exact H-x row whose z-trim is F. If (c,z,b_0) is bad, R3 gives (b_0,z,c). Source (a,z,c) is also tight, so the tested dimer (z,c) has two distinct head witnesses b_0 and a; R523 gives a same-oriented two-head collision.

Thus outside R523 geometry both exact singleton rows exist. In T_x the restored z lies strictly between c and the nonempty W-block B, so z is internal. SV93413 therefore takes its internal-puncture branch and gives R159 component-drop geometry on H-{x,z}.

### 3. W followed by the source trimer
Suppose F=B(a,y,c)|C and let b_r be the terminal vertex of B. Appending z after c is automatic from source (y,c,z), giving an exact H-x row trimming to F.

To restore x immediately before a, test (b_r,x,a). If tight,

  T_z=B(x,a,y,c)|C

is an exact H-z row trimming to F, since (x,a,y) is a retained source turn. If (b_r,x,a) is bad, R3 gives (a,x,b_r). Source (a,x,c) is tight, so the tested dimer (a,x) has two distinct tail witnesses b_r and c; R523 gives a two-tail collision.

Again the successful branch gives two singleton rows, but now the restored x lies strictly between the nonempty W-block B and a, so x is internal. SV93413 therefore gives R159 component-drop geometry.

### 4. Conclusion
The (p,tau)=(2,1) pair-residue cell has no quiet survivor. It yields TWO-COVER, R407, R435 geometry, or a source-pinned R523 collision. No payment, generation ledger or return map is used. R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R560"
    },
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    }
]
```