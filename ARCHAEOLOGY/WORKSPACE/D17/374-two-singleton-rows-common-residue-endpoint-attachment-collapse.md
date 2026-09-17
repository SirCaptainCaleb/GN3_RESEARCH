# Two singleton-deletion rows currentize on their common pair deletion, close, or force R407

**Workspace:** D17
**State:** established
**Key:** `two-singleton-rows-common-residue-endpoint-attachment-collapse`

**Summary:** Let r,s be distinct vertices and choose arbitrary exact two-covers T_r of H-r and T_s of H-s. Internal exchanged roots give R159 after puncturing to H-{r,s}. Otherwise both roots are endpoints and trim to exact covers F_r,F_s of the common pair residue. R410/R471 consumes support/order disagreement. If the trims are literally identical, the original rows are endpoint attachments of s and r to one common base cover. Different rails or opposite ends commute to TWO-COVER. If both attach at the same end, test the two possible root orders separately. A successful order closes; if both desired orders fail, R3 gives (v0,s,r) and (v0,r,s), so both orientations of the root dimer {r,s} are head-signed by the same boundary witness v0, exactly the R407 bidirectional same-witness packet. Thus the synchronized branch is TWO-COVER or R407, not unconditional closure.

### 1. Two arbitrary singleton-deletion rows
Let H be a hypothetical smallest Strong Level-(1) counterexample and let r,s be distinct physical vertices. Choose arbitrary literal exact two-covers

  T_r of H-r,
  T_s of H-s.

No compatibility between the representatives is assumed.

### 2. Internal exchanged roots give component drop
If s is internal on a rail of T_r, deleting s splits that rail into two nonempty tight paths while the other rail remains nonempty. Hence H-{r,s} has a literal three-cover. Smallest-counterexample minimality R4 supplies a cover with at most two components, so R159 gives a graph-intrinsic balanced opposite-sign pair. The same holds if r is internal in T_s.

Thus outside R159 geometry, s is an endpoint of T_r and r is an endpoint of T_s.

### 3. Endpoint trimming gives one common pair residue
If the component of T_r containing s is the singleton (s), the other component is Hamiltonian on V(H)-{r,s}; together with the dimer (r,s) it two-covers H. Hence outside closure the s-component has at least two vertices, and trimming endpoint s gives an exact two-cover F_r of H-{r,s}. Dually trimming endpoint r from T_s gives an exact two-cover F_s of the same residue.

Compare F_r,F_s by R410/R471. Different support partitions give an R410 balanced pair. Equal support partitions but different literal Hamilton orders give R435 adjacent-reversal/reverse-trimer/proper-cycle geometry. Hence the only quiet comparison branch is, after rail exchange if needed,

  F_r=F_s=:F=P|Q

literally.

### 4. Easy endpoint attachments commute
In the literal-sync branch, T_r is obtained from F by attaching s to one endpoint of P or Q, and T_s by attaching r to one endpoint of P or Q.

If the two roots attach to different rails, attach each to its own rail and obtain a spanning two-cover. If they attach to opposite ends of the same rail, both source seam turns are already certified in T_r,T_s, so both roots may be attached simultaneously and again H is two-covered.

### 5. Same-end attachment: closure or R407
It remains that both roots attach to the same end of the same nontrivial rail. Write that base rail as

  R=(v_0,v_1,...,v_k),  k>=1,

and suppose the source rows certify

  (s,v_0,v_1) tight,
  (r,v_0,v_1) tight.                                      (SR.5)

There are two possible two-root extensions at this end. If

  (r,s,v_0)

is tight, then (r,s,v_0,v_1,...,v_k) is a tight path using the first seam in (SR.5), and the untouched rail of F gives a spanning two-cover. If

  (s,r,v_0)

is tight, then (s,r,v_0,v_1,...,v_k) is a tight path using the second seam in (SR.5), again closing H.

Assume both desired turns are bad. Boundary antisymmetry R3 then gives their exact complete reversals

  (v_0,s,r) tight,
  (v_0,r,s) tight.                                       (SR.6)

On the physical root dimer {r,s}, (v_0,r,s) is a head certificate on tested orientation (r,s) with witness v_0, while (v_0,s,r) is a head certificate on the reverse tested orientation (s,r) with the same witness v_0. This is exactly the hypothesis of accepted R407: both tested orientations of one physical dimer carry the same polarity under one common witness. Hence the only nonclosing same-end synchronized branch is an ancestry-pinned R407 root-dimer interaction.

If the common base rail is the singleton (v_0), each original singleton-deletion row consists of the root-attached dimer plus the untouched other rail. The two roots together with v_0 form some tight trimer by choosing any tight ordering on that three-set; that trimer plus the untouched rail spans H, so this degenerate base-rail case closes directly.

### 6. Parent theorem
For any distinct deletion roots r,s and arbitrary exact singleton-deletion rows T_r,T_s, at least one of the following holds:

1. TWO-COVER of H;
2. an R159/R410 balanced opposite-sign pair on the common pair-deletion comparison;
3. R435 adjacent-reversal/reverse-trimer/proper-cycle geometry;
4. an R407 bidirectional same-witness interaction on the root dimer {r,s}.

No synchronization hypothesis on the original rows is required. The synchronized common-residue branch is created only after puncturing the exchanged roots. The original rows remain alternative representatives; no simultaneous currentness is asserted. R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R410"
    },
    {
        "relation": "dependency",
        "revision_id": "R471"
    },
    {
        "relation": "dependency",
        "revision_id": "R407"
    }
]
```