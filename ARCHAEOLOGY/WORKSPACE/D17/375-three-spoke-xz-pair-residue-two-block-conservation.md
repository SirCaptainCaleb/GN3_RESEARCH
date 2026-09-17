# The x/z common pair residue has exactly two W-blocks and p+tau=3 outside component drop

**Workspace:** D17
**State:** established
**Key:** `three-spoke-xz-pair-residue-two-block-conservation`

**Summary:** In the G30 three-spoke packet K=(x,a,y,c,z), put S={a,y,c}, D={x,z}, W=H-K and let F be any exact two-cover of H-D. The Hamilton P5 K is a one-path absorber on D union S, so R560 with k=2 and pc(H)>2 forces at least two maximal W-blocks in F. If there are at least three, those W-blocks form a literal >=3-path cover of H[W], while smallest-counterexample minimality supplies an at-most-two cover; R159 gives a balanced pair. Hence outside component-drop geometry F has exactly two W-blocks. If p is the number of selected S-S states and tau the number of selected S-W transitions, two-path forest arithmetic gives p+tau=3. Thus the quiet pair-residue has only three combinatorial cells: (p,tau)=(2,1),(1,2),(0,3). The tau=1 cell has S as one contiguous Hamilton trimer block; tau=2 has exactly one selected S-S state; tau=3 has the three source-trimer vertices pairwise separated by W blocks/rail breaks. This is a finite static reduction, not a consumer of the three cells.

### 1. Common pair-deletion residue
Retain the G30 source P5 K=(x,a,y,c,z). Put

  D={x,z},
  S={a,y,c},
  W=V(H)-V(K).

Thus D,S,W are pairwise disjoint and cover V(H), and K is a literal one-path cover of H[D union S]. Let F be any literal exact two-cover of H-D=H[S union W].

### 2. R560 forces at least two W-blocks
Apply accepted R560 with absorber cover A=K, so a=1, and deletion cover F with k=2. Since H is a counterexample, pc(H)>2. Therefore

  b_W(F) >= pc(H)-1 >= 2,                                (PB.1)

where b_W(F) is the number of nonempty maximal contiguous W-blocks obtained by cutting the two F-rails at every selected S|W transition.

This recovers the R508 crossing law and strengthens it to a block floor.

### 3. Three W-blocks already give component drop
If b_W(F)>=3, the W-blocks themselves are vertex-disjoint tight paths whose supports partition W, hence form a literal cover of H[W] with at least three components. Because W is a proper induced subsystem of the smallest counterexample H, accepted minimality R4 supplies a path cover of H[W] with at most two components. Accepted R159 therefore gives a graph-intrinsic balanced opposite-sign pair.

Hence outside R159 component-drop geometry every exact H-{x,z} cover satisfies

  b_W(F)=2.                                                (PB.2)

### 4. Exact conservation p+tau=3
Work in the two-W-block branch (PB.2). Let

  p = number of selected adjacent states of F with both endpoints in S,
  tau = number of selected adjacent states of F with one endpoint in S and one in W.

The two F-rails span |W|+3 vertices, so together they contain exactly |W|+1 selected adjacent states. The two maximal W-blocks contain exactly |W|-2 selected W-W states. Every remaining selected state is counted by p or tau. Therefore

  (|W|-2)+p+tau = |W|+1,

so

  p+tau=3.                                                (PB.3)

R508 ensures tau>=1. Since p>=0, the only possibilities are

  (p,tau)=(2,1), (1,2), (0,3).                           (PB.4)

### 5. Physical meaning of the three cells
If tau=1, then p=2. On the three vertices S, two selected S-S states form one Hamilton trimer block; equivalently this is precisely the R560 unique-transition normal form with all of S contiguous on the mixed rail.

If tau=2, exactly one S-S state survives. The third S-vertex is separated from that selected dimer by W or by the rail break.

If tau=3, no two S-vertices are selected adjacent in F. All three source-trimer vertices are separated at the selected-state level.

Thus the static G30 pair-residue has a three-cell finite alphabet before any R509 seam refinement.

### 6. Scope fence
This theorem does not claim any of the three cells is realizable, nor does it pay the R159 output. It records a source-frame-intrinsic finite reduction on the actual pair residue H-{x,z}. The source trimer (a,y,c), both deleted roots x,z, the two W-blocks, and every selected S|W crossing remain physically named for subsequent consumers. R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R560"
    },
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R159"
    }
]
```