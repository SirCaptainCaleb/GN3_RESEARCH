# Three residual labels supply one universally ordinary two-cap pair

**Workspace:** D17
**State:** conditional
**Key:** `middle-layer-common-two-cap-label`

**Summary:** Conditional on the near-maximal star signs and terminal theorem, at most one residual label admits an exceptional left cap and at most one an exceptional right cap. Of three labels, one has every left-cap path ending there and every right-cap path beginning there. Their union has an explicit Hamilton k-complement, but amalgamation remains open.

### Conditional two-cap selection
Assume the uniform residue and the complete star signs of middle-layer-nearmax-outer-terminal: |O|=k-2, k>=6, R={r,s,q} is the residual exterior triple, h,t are distinct outside O union R, and (h,x,y),(y,x,t) are tight for every x in O and every other exterior y. Every k-set is Hamiltonian and no (k+1)-set is Hamiltonian.

Put X_v=O union {h,v} and Y_v=O union {t,v}. There is a v in R such that EVERY Hamilton order on X_v has h first or second and ends at v, and EVERY Hamilton order on Y_v starts at v and has t last or penultimate.

### Proof
The left terminal theorem in middle-layer-nearmax-outer-terminal gives two possible X_v forms: h first/second with terminal v, or terminal dimer (v,h). At most one v admits the latter: two paths ending (v,h) and (w,h) would allow one to append the other's residual label, since exactly one of (v,h,w),(w,h,v) is tight.

For completeness the right form follows directly, without reversing any actual path. Let Q be a Hamilton order on Y_v. If t has at least two successors, its immediate successor must be v: a successor x in O followed by y would give (t,x,y), contrary to the tight reverse (y,x,t). If t is last or penultimate, the initial vertex must be v; otherwise its first two vertices x,y have x in O and y exterior, and h prepends by (h,x,y). If t has at least two successors and occurs after the first two positions, Q again starts with two exterior vertices, its initial vertex in O, and h prepends. The remaining noninitial possibility is Q=(x,t,v,...) with x in O. Choose w in R different from v. Then (w,x,t) is tight, so w prepends, again forbidden. Consequently the only other form begins (t,v).

At most one v admits a Y_v order beginning (t,v): if both v,w do, exactly one of (w,t,v),(v,t,w) is tight and prepends to the corresponding path. Thus at most one residual label is left-exceptional and at most one is right-exceptional. Three residual labels leave at least one outside their union. For this v both universal assertions follow.

### Explicit prospective consumer and limitation
The union X_v union Y_v=O union {h,t,v} has k+1 vertices. A Hamilton order on that union would have Hamilton k-set complement (P minus {h,t}) union (R minus {v}) in the original near-maximal application. The selection lemma does not construct this union order: the two chosen paths share O union {v}, whose vertices cannot be repeated or silently synchronized. All six support families and all physical labels remain available for reselection.

Status: new complete conditional internal deduction, unreviewed. Its application uses the unreviewed near-maximal star/terminal argument; it is not canonical acceptance or near-maximal branch closure.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
