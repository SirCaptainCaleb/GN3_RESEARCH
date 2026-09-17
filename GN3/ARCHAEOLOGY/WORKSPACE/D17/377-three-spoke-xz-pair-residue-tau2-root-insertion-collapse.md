# The tau=2 x/z pair-residue cell closes or emits source-pinned P4/R523/R435 geometry

**Workspace:** D17
**State:** established
**Key:** `three-spoke-xz-pair-residue-tau2-root-insertion-collapse`

**Summary:** In the DR17.520 x/z pair residue with exactly two W-blocks and (p,tau)=(1,2), there is exactly one selected S-S state on S={a,y,c}. If that state is the reverse-order c->a contact, R435 is already active. If it is a->c, replacing that state by a->x->c and by a->z->c gives exact H-z and H-x rows with the same trim F, so the inserted roots are internal and SV93413 gives R159. If the selected state is a->y, x can be inserted immediately before a using source (x,a,y); any missing predecessor seam reverses to a second tail witness on (a,x). Independently z can be inserted immediately after c; failures of its one/two local seams give either a P4 against source (a,z,c) or a second head witness on (z,c). The y->c case is the exact dual. Thus outside P4/R523/R435 geometry both roots restore to singleton rows whose trims are the identical F, forcing R159 if either root is internal and TWO-COVER otherwise; the endpoint attachments are at distinct a,c so R407 is impossible.

### 1. Setup
Retain the G30 pair-residue coordinates K=(x,a,y,c,z), S={a,y,c}, W=H-K and an exact cover F of H-{x,z} in the DR17.520 branch

  b_W(F)=2,  p=1,  tau=2.

Thus F selects exactly one S-S state.

### 2. The skip state a-c
If the unique S-S state is selected in reverse source order c->a, comparison with the retained source trimer (a,y,c) is R435-active, so retain that output. Outside R435, the selected skip orientation is a->c.

Replace the selected state a->c by the two-state path a->x->c. The source spoke turn (a,x,c) is tight, so this produces an exact two-cover T_z of H-z. Deleting x from T_z restores the selected state a->c and recovers F literally. Likewise the source spoke (a,z,c) replaces a->c by a->z->c, producing an exact H-x row T_x whose z-trim is F. Here both inserted roots are internal on their singleton-deletion rows, so SV93413 takes its internal-puncture branch and gives R159 component-drop geometry on H-{x,z}.

### 3. The selected source edge a->y
Assume the unique S-S state is a->y. Restore x immediately before a. If a is the source endpoint of its F-rail, the source turn (x,a,y) makes the restoration automatic. Otherwise let u in W be the predecessor of a and test (u,x,a). If tight, the local word u,x,a,y is tight and insertion of x gives an exact H-z row trimming to F. If bad, R3 gives (a,x,u). Together with source (a,x,c), the tested dimer (a,x) has two distinct tail witnesses u,c, so R523 gives a same-oriented collision.

Now restore z immediately after c. Because p=1 and the only S-S state is a-y, every selected neighbor of c lies in W. If c is terminal with predecessor v, test (v,c,z); failure reverses to (z,c,v), which is opposite polarity on tested dimer (z,c) to source (a,z,c), giving a literal P4 by R523. If c is source with successor w, test (c,z,w); failure reverses to (w,z,c), a second head witness on (z,c) beside source witness a. If c is internal, test both required seams (v,c,z) and (c,z,w); either failure gives the corresponding P4/collision, while success inserts z and produces an exact H-x row trimming to F.

Thus outside source-pinned P4/R523 geometry both root restorations succeed. If either inserted root is internal, SV93413 gives R159. If both are endpoints, x is attached at physical endpoint a and z at distinct physical endpoint c; they are therefore on different rails or opposite ends of one rail, and SV93413 gives TWO-COVER. The same-end R407 residue cannot occur.

### 4. The selected source edge y->c
This is the exact ordered dual. Restore z immediately after c using the retained turn (y,c,z), with at most one W-side seam test; a failed test gives a second certificate on the source z-c boundary dimer. Restore x immediately before a; since a has no selected S-neighbor in this case, one or two W-side seam tests suffice, and their reversals interact with source turns (x,a,y) and (a,x,c) to give a literal P4 or R523 collision. If all tests pass, apply the same endpoint/internal dichotomy: an internal inserted root gives R159, while if both are endpoints they attach at distinct physical endpoints a,c and commute to TWO-COVER. No same-end R407 branch is possible.

### 5. Conclusion
The (p,tau)=(1,2) cell has no quiet survivor: it yields TWO-COVER, R407, R435 geometry, a literal source-pinned P4, or an R523 same-dimer collision. No payment or return map is used. R24 and R5 are unused.

## References

```json
[
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