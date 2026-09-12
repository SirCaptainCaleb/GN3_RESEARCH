# Astra fence: Hamilton existence is not the special P5 order; endpoint-pair insertions omit W-side turns

**Workspace:** D17
**State:** limitation
**Key:** `astra-static-three-spoke-source-order-and-full-window-fence`

**Summary:** At DR17.527 the special K order is an extra hypothesis, not supplied by SV58280; an opposite-cycle five-vertex example refutes its automatic selection. SV94553/SV94554 omit changed W-side turns, so SV94555 is not a proved five-output extinction. The two-block arithmetic and conditional tau=3 endpoint argument survive. The global target remains source-frame absorption, not generic portal existence.

### Astra strategic audit at DR17.527
This is a limitation/fence, not a proof of the two-cover conjecture and not canonical rejection of the historical exact units. R24/R5 are not used.

### 1. Existential Hamilton P5 versus the required physical order
SV58280 proves that the set {a,c,p,q,r} with tight turns (a,p,c),(a,q,c),(a,r,c) has SOME Hamilton P5. Its edge-order contradiction constructs a special order only under the temporary assumption that the five-set is non-Hamiltonian. That contradiction does not construct such an order in the unrestricted Hamiltonian case.

The stronger special-order implication is false under R3. On the neighbors p,q,r at middle a prescribe the cycle p->q->r->p; at middle c prescribe the opposite cycle q->p, r->q, p->r. At each middle s in {p,q,r} prescribe (a,s,c) tight. These constraints are compatible: they concern distinct R3 reversal bits. Complete all unspecified comparisons arbitrarily, yielding a boundary tournament through R887. For any permutation (x,y,z) of (p,q,r), tightness of (x,a,y) makes y the cyclic successor of x in the a-cycle, so z is the successor of y; then (y,c,z) is bad by the opposite c-cycle. Consequently NO order (x,a,y,c,z) is tight. Swapping a,c also supplies no such order. This does not refute SV58280's existential Hamiltonicity: one completion (all unspecified comparisons increasing in the alphabetical order a<c<p<q<r) has nine Hamilton orders, including (a,c,p,q,r).

Thus G30 and all endpoint-petal applications requiring the displayed K must retain it as an ADDITIONAL literal hypothesis until a source-selection theorem or a separate non-special-order branch is provided. Three spoke turns alone do not supply its two seam turns. SV89302's pairwise four-set Hamiltonicity is unaffected.

### 2. Complete insertion windows are missing in SV94554
In the tau=1 cell F=(a,y,c)B|C with B=(b0,b1,...), the proposed T_x=(a,y,c,z)B|C needs BOTH (c,z,b0) and (z,b0,b1), the latter whenever |B|>=2. The old turn (c,b0,b1) does not certify (z,b0,b1). The source supplies (y,c,z) only. A bad omitted seam gives the exact turn (b1,b0,z), on the reversed W-boundary dimer (b1,b0), not the asserted source dimer (z,c). Dually B(x,a,y,c)|C also requires (b_{r-1},b_r,x) when |B|>=2, as well as the tested (b_r,x,a). No inference identifies these different middle-vertex R3 bits. Thus SV94554's asserted insertion and restricted output alphabet are not proved for non-singleton B.

### 3. Complete insertion windows are missing in SV94553
For a selected skip a->c with predecessor u of a and successor v of c, replacement by a->x->c requires (u,a,x) and (x,c,v) whenever those neighbors exist, besides source (a,x,c). The corresponding z insertion needs its own two seams. Source tightness alone does not justify either row.
Inserting x into (...,t,u,a,y,...) changes three turns: (t,u,x), (u,x,a), (x,a,y). The proof checks the middle one and inherits the last, but omits the first. Inserting z into (...,v,c,w,t,...) requires (v,c,z), (c,z,w), (z,w,t); the last is omitted. Boundary omissions must be determined from the actual rail lengths. The y->c case has the same dual defect.
Also distinguish physical deletion (which cuts a path at an internal vertex and produces components) from deleting the vertex and rejoining its old neighbors. Only the latter can recover the old selected edge of F; it is justified here only by that retained old edge, not by a generic trimming rule.
The conclusion paragraphs of SV94553/SV94554 still list R407 and omit R159 despite the repaired summaries. SV94555's body still cites historical SV92282/SV92659/SV92660 instead of current tau units. These are secondary editorial issues; the missing turns are substantive.

### 4. Surviving content
Conditional on an actual displayed K=(x,a,y,c,z), SV91906's block count and p+tau=3 arithmetic survive. SV94552's tau=3 proof uses genuine endpoint extensions, so each extension has only the one tested seam; its distinct-a,c commuting argument survives this audit. The corrected generic SV93413 endpoint theorem also retains its same-end R407 exception. The tau=1/tau=2 proofs and SV94555's five-output conclusion must not be used as a completed contraction without repair. This finding disproves the local inference/normal-form implication; it does not exhibit a smallest counterexample or disprove the global theorem.

### 5. Strategic meaning
Even a repaired five-output theorem is not yet extinction. SV58280 section 4 already supplies a component drop on the SAME W from deleting the three internal spokes from the original H-{a,c} frame. R159/R176 only produces a graph-intrinsic pair, possibly with singleton support; R523's same-polarity case only names two extensions; R435 explicitly permits a nonclosing proper cycle. Their existence is compatible with the already-known source packet. A useful consumer must retain the actual F, old source frame, exact W-block orders/boundary vertices, and complete bad-seam clauses, and yield a spanning two-cover or a separately justified strict global improvement.
The strategic target is three-spoke frame absorption for an actual realizable common parent, uniformly over its Hamilton orders. The special endpoint-pair subproblem remains a promising conditional front end, not a proved replacement of the entire phase-zero bottleneck.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R887"
    },
    {
        "relation": "dependency",
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R176"
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
