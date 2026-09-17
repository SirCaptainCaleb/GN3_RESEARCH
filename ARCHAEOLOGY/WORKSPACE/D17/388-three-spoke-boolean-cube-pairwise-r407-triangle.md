# The three-spoke Boolean cube reduces to a triangle of pairwise R407 packets outside recompletion disagreement

**Workspace:** D17
**State:** established
**Key:** `three-spoke-boolean-cube-pairwise-r407-triangle`

**Summary:** Let a three-spoke source frame have internal same-orientation spokes P={p,q,r} and Boolean exact-two-cover cube G_J=W∪J from SV96081. Fix a spoke pair {s,t} and let u be the third spoke. Compare arbitrary exact covers of G_{s,u} and G_{t,u} over the common fiber G_u. If s or t is internal, puncturing gives a literal three-cover of G_u against its exact two-cover and R159 fires. Otherwise trim the endpoint roots to exact covers of G_u; R410/R471 consumes support/order disagreement. In the synchronized branch the two upper covers are endpoint attachments of s,t to one common base cover F of G_u. Attachments on different rails or opposite ends, or any successful root-order splice at one common end, produce an exact top-fiber cover G_P in which s or t is an endpoint; the retained source frame has all three spokes internal, so R408 gives endpoint/internal component-drop geometry. If the common base rail is singleton, a tight trimer on {s,t,v} gives the same R408 discrepancy. Therefore the only branch avoiding R159/R410/R435/R408 is a nontrivial same-end double attachment in which both two-root splice turns are bad; R3 then gives both tested orientations of {s,t} the same polarity with the common boundary witness, exactly R407. Applying this to all three spoke pairs, the completely disagreement-free Boolean cube carries R407 packets on {p,q},{q,r},{r,p}. This is a static finite reduction, not absorption; the three R407 packets still need a common-parent consumer.

### 1. Setup: one Boolean cube with an internal top representative
Retain a hypothetical smallest counterexample H and one exact source frame

  H-{a,c}=U|V

with three distinct internal same-orientation spokes

  P={p,q,r}.

Put W=V(H)-({a,c}∪P) and G_J=H[W∪J] for J⊆P. By SV96081 every G_J is non-Hamiltonian and has exact path-cover number two. The top fiber

  G_P=H-{a,c}

has the retained literal representative U|V in which p,q,r are all internal.

We compare neighboring rank-two fibers through their common rank-one fiber. The point is to retain physical endpoint roles rather than collapse the cube edges to anonymous balanced-pair births.

### 2. One spoke pair over the third-spoke fiber
Fix distinct s,t∈P and let u be the third spoke. Choose arbitrary literal exact two-covers

  T_s of G_{s,u}=W∪{s,u},
  T_t of G_{t,u}=W∪{t,u}.

If s is internal on its rail of T_s, deleting s splits that rail into two nonempty tight subpaths and leaves the other T_s rail nonempty. Hence G_u has a literal three-cover. Since G_u also has an exact two-cover, accepted R159 gives a graph-intrinsic balanced opposite-sign pair. The same conclusion holds if t is internal in T_t.

Thus outside this component-drop output both exchanged roots are endpoints. Their root-containing rails cannot be singleton: if, say, T_s had singleton rail (s), its other rail would be a Hamilton path on all of G_u, contradicting the Boolean-cube non-Hamiltonicity of G_u. Therefore trimming s and t gives literal exact two-covers

  F_s, F_t of G_u.                                      (BT.1)

### 3. Common-fiber disagreement is already explicit geometry
Compare F_s and F_t. Accepted R410 gives a balanced-pair output if their unordered support partitions differ. If their support partitions agree but a Hamilton rail order differs, accepted R471/R435 gives an adjacent selected-state reversal, a reverse trimer, or a proper tight cycle.

Outside those outputs the trims are literally identical up to rail exchange. Write the common exact base cover as

  F=A|B.                                                  (BT.2)

Then T_s and T_t are literal endpoint attachments of s and t to the four oriented ends of the same physical base cover F. No simultaneous currentness beyond these two source covers is asserted; the attachment certificates themselves are graph-intrinsic path facts.

### 4. Commuting attachments contradict source internality
Suppose the two roots attach to different rails of F. Attach both roots simultaneously at their certified ends. The two attachments are vertex-disjoint and commute, giving a literal exact two-cover of the top fiber G_P. In that top cover s and t are rail endpoints. But in the retained source representative U|V both are internal. Accepted R408 applied to the two exact covers of the same proper residue G_P therefore gives its endpoint/internal component-drop balanced-pair output.

The same argument applies when s and t attach to opposite ends of one nontrivial base rail: both certified end extensions may be made simultaneously, again exposing s and t as endpoints of a top-fiber exact cover and triggering R408 against U|V.

It remains that both roots attach at the same end of one base rail. First suppose that rail is a singleton (v). Then some ordering of {s,t,v} is a tight trimer by boundary antisymmetry. That trimer together with the untouched second rail of F is an exact two-cover of G_P. At least one of s,t is a trimer endpoint, whereas both are internal in U|V, so R408 again applies. Thus the quiet same-end residue requires a nontrivial base rail.

### 5. Same-end double failure is exactly R407
Orient the nontrivial common base rail from the common attachment end as

  R=(v_0,v_1,...).

In the source-end case T_s certifies (s,v_0,v_1) tight and T_t certifies (t,v_0,v_1) tight. Test the two possible two-root splices.

- If (s,t,v_0) is tight, then (s,t,v_0,v_1,...) is a tight extension of R, using the certified t-attachment for its second seam. Together with the untouched base rail it is an exact two-cover of G_P exposing s as an endpoint, so R408 applies against U|V.
- If (t,s,v_0) is tight, the symmetric splice exposes t and again R408 applies.

Therefore a branch avoiding R408 must have both displayed turns bad. R3 gives their complete reversals

  (v_0,t,s) tight,
  (v_0,s,t) tight.                                      (BT.3)

These are head certificates with the same witness v_0 on the two tested orientations (t,s) and (s,t) of the physical root dimer {s,t}. This is exactly the hypothesis of accepted R407.

The terminal-end case is the exact order dual. If both two-root tail splices fail, R3 makes the two tested orientations of {s,t} tail-signed by the same terminal boundary witness, again giving R407.

Consequently for the fixed pair {s,t}, at least one of the following holds:

  R159 component drop on G_u;
  R410 common-fiber partition disagreement;
  R435/R471 common-fiber order disagreement;
  R408 endpoint/internal discrepancy on the top fiber G_P;
  R407 bidirectional same-witness interaction on {s,t}.   (BT.4)

### 6. Triangle consequence
Apply (BT.4) to the three unordered spoke pairs

  {p,q} over G_r,
  {q,r} over G_p,
  {r,p} over G_q.

If any of the first four output types occurs, retain that physical source/cube comparison as constructive G31 data. If none occurs for any pair, the source frame carries three graph-intrinsic R407 packets, one on each physical spoke-pair dimer

  {p,q}, {q,r}, {r,p}.                                  (BT.5)

Their common witnesses and head/tail polarities may differ from pair to pair and come from the corresponding common rank-one fibers. No equality of those witnesses and no simultaneous current representative is claimed. What coexists is the three exact R407 path/sign certificates themselves.

Thus the completely disagreement-free Boolean cube is finite: it collapses to an R407 triangle on the three source spokes.

### 7. Scope fence
This is a structural reduction, not three-spoke frame absorption. Under active G31 guidance, R159, R408, R410, R435 and R407 outputs are not counted as theorem closure merely because they exist. The gain is that eight exact-cover fibers cannot remain independently quiet: after all ordinary component/support/order/endpoint discrepancies are suppressed, only three pairwise bidirectional same-witness packets remain. A subsequent consumer must use their common three-spoke source ancestry to obtain a spanning two-cover or a separately justified global improvement.

No special P5 order, PAYABLE-FOUR payment, R24, or R5 is used.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R407"
    },
    {
        "relation": "dependency",
        "revision_id": "R408"
    },
    {
        "relation": "dependency",
        "revision_id": "R410"
    },
    {
        "relation": "dependency",
        "revision_id": "R471"
    }
]
```
