# Rank-two cube coherence collapses the endpoint trident to one singleton-star four-cell

**Workspace:** D17
**State:** established
**Key:** `three-spoke-boolean-cube-ranktwo-port-coherence`

**Summary:** Retain the SV97234 common-base endpoint trident for a three-spoke source frame: one exact W-cover F=A|B and singleton fibers obtained by attaching p,q,r to endpoints of F. Compare every rank-two fiber W+{s,t}. If an exchanged root is internal, puncturing gives R159 on the opposite singleton fiber; otherwise trimming both roots gives exact singleton-fiber covers, and R410/R471 consumes any disagreement from the retained trident rows. In the synchronized branch, selected-edge accounting forces the rank-two cover to be exactly F plus the two root-to-port edges. Hence two roots cannot attach to the same endpoint of a nontrivial W rail, since that endpoint would have selected degree three. The only physical endpoint that two roots may share is an isolated singleton rail vertex v of F, where the rank-two fiber is the tight trimer through the two roots and v. Unless all three spokes attach to that same singleton v, the three singleton attachments can be installed simultaneously, using the relevant rank-two trimer if two share v; this gives an exact top-fiber cover H-{a,c} exposing source-internal spokes and R408 fires against the retained source frame. Thus a completely synchronized branch is forced into F=(v)|B with all p,q,r attached to v. In that residue every pair fiber is a trimer on {v,s,t} plus B, and X={v,p,q,r} must be non-Hamiltonian, else a Hamilton P4 on X together with B gives a top-fiber exact cover with a spoke endpoint and again R408. The order-independent quiet cube has therefore contracted to one singleton-star non-Hamiltonian four-cell with a common Hamilton W-minus-v rail. This is reduction, not yet frame absorption.

### 1. Input: the common-base endpoint trident
Retain the order-independent three-spoke source frame and Boolean cube of SV96081. Thus

  P={p,q,r},
  W=V(H)-({a,c}∪P),
  G_J=H[W∪J],

and every G_J has exact path-cover number two. The top fiber

  G_P=H-{a,c}

has the retained source representative U|V in which p,q,r are all internal.

Work outside the common-W component-drop and exact-cover disagreement outputs already isolated in SV97234. Hence choose one literal exact two-cover

  F=A|B                                                   (PC.1)

of W and, for every s∈P, one exact singleton-fiber cover T_s of W+s obtained from F by attaching s at one physical rail endpoint. Trimming s from T_s gives F literally up to rail exchange.

This section adds the rank-two cube constraints to that endpoint trident.

### 2. A quiet rank-two fiber must trim to the two retained singleton rows
Fix distinct s,t∈P and choose an arbitrary exact two-cover

  T_{st} of G_{s,t}=W∪{s,t}.                              (PC.2)

If s is internal on its T_{st}-rail, deleting s gives a literal three-cover of G_t: the s-rail splits into two nonempty tight pieces and the other rail remains nonempty. Since G_t has an exact two-cover, accepted R159 gives its component-drop balanced-pair output. The same holds with s,t interchanged.

Thus outside R159 both roots are rail endpoints of T_{st}. Neither root can be a singleton rail. If, say, (s) were a whole T_{st}-component, the other rail would be a Hamilton path on G_t, contradicting the Boolean-cube non-Hamiltonicity of G_t. Therefore deleting either root leaves a literal exact two-cover of the opposite singleton fiber.

Compare T_{st}-s with the retained T_t and T_{st}-t with T_s. Accepted R410 consumes any support-partition disagreement, while accepted R471/R435 consumes any literal Hamilton-order disagreement. Consequently, outside those outputs,

  T_{st}-s = T_t,
  T_{st}-t = T_s                                           (PC.3)

literally up to rail exchange.

### 3. Selected-edge conservation fixes the whole rank-two cover
Let e_s be the physical F-endpoint to which s is attached in T_s, and e_t the corresponding endpoint for t. In selected-edge language,

  E(T_s)=E(F)∪{s e_s},
  E(T_t)=E(F)∪{t e_t}.                                    (PC.4)

By (PC.3), every F-edge survives in T_{st}: it survives deletion of either root. Likewise s e_s must belong to T_{st}, because it survives deletion of t, and t e_t must belong to T_{st}.

Now F is a two-path forest on |W| vertices and therefore has |W|-2 selected edges. T_{st} is a two-path forest on |W|+2 vertices and therefore has exactly |W| selected edges. The edges in (PC.4) already account for all |W| of them. Hence

  E(T_{st})=E(F)∪{s e_s,t e_t}.                            (PC.5)

This is stronger than endpoint-role bookkeeping: no hidden root-root or cross-rail edge is available in the synchronized rank-two fiber.

### 4. Shared physical ports are possible only on a singleton W rail
Suppose e_s=e_t=v. If v is an endpoint of a nontrivial F-rail, then deg_F(v)=1. Equation (PC.5) gives

  deg_{T_{st}}(v)=3,

impossible because the selected-state graph of a two-path cover is a union of paths.

Therefore two distinct roots may share one physical attachment vertex only when v is an isolated singleton component of F. In that case deg_F(v)=0 and (PC.5) makes the root-containing T_{st} component the path on exactly {s,v,t}; its literal order is whichever of (s,v,t),(t,v,s) is tight. The other T_{st} component is the untouched second F-rail.

Thus every pair of spoke attachments satisfies the sharp physical rule:

- distinct endpoints of F; or
- one common endpoint v which is itself a singleton F-rail, with the pair fiber equal to a tight trimer through v.             (PC.6)

### 5. Unless all three roots share one singleton, the attachments commute to the top
First suppose no F-rail is singleton. By (PC.6) the three physical attachment endpoints e_p,e_q,e_r are pairwise distinct. Attach all three roots simultaneously to F. Since each is added at a distinct endpoint, the three endpoint extensions commute and give a literal two-path cover of the top fiber G_P. Every spoke is a rail endpoint in that cover. The retained source representative U|V has all three spokes internal, so accepted R408 applied to these two exact covers of the same proper residue G_P gives endpoint/internal component-drop geometry.

Now suppose F has one singleton rail (v) and one nontrivial rail B. There cannot be two singleton rails because |W|=|V(H)|-5>=6. If at most one spoke attaches to v, all three attachments again occupy path-forest-compatible distinct endpoints and commute to an exact top cover, so R408 applies.

If exactly two spokes, say s,t, attach to v, use their actual rank-two fiber from Section 4: its root component is one tight trimer on {s,v,t}. Attach the third root u at its certified endpoint of B. The trimer together with the u-extended B rail is an exact two-cover of G_P exposing all three spokes as endpoints, again giving R408 against U|V.

Consequently a branch avoiding R159/R410/R435/R408 must have

  F=(v)|B,
  p,q,r all attached to the singleton v.                   (PC.7)

In particular every singleton fiber is a dimer-plus-B cover and every rank-two fiber is a trimer-plus-B cover.

### 6. The residual four-set must be non-Hamiltonian
Put

  X={v,p,q,r}.                                             (PC.8)

If X had a Hamilton tight P4 Q, then

  Q | B

would be a literal exact two-cover of the top fiber G_P. A four-vertex path has two endpoints and at most one of them can be v, so at least one spoke in P is a rail endpoint of this cover. In the retained source cover U|V every spoke is internal. Accepted R408 would again give endpoint/internal component-drop geometry.

Hence the fully synchronized branch forces

  X={v,p,q,r} non-Hamiltonian.                             (PC.9)

The complete quiet cube has therefore contracted to one finite static nucleus:

- one Hamilton path B on W-{v};
- one isolated W vertex v in the common core cover;
- singleton fibers (v,s)|B for s=p,q,r;
- rank-two fibers J_{st}|B where J_{st} is the actual tight trimer on {s,v,t};
- a non-Hamiltonian four-cell X={v,p,q,r}; and
- the original top source cover U|V in which p,q,r are all internal.

### 7. Scope fence
This is a reduction, not yet three-spoke frame absorption. R159, R410, R435 and R408 are retained as constructive outputs, not declared terminal progress. The new content is that no large endpoint-port weave remains after the whole Boolean cube is synchronized: the only branch with none of those outputs is one singleton-star non-Hamiltonian four-cell X attached to a common Hamilton spectator rail B.

The next consumer may therefore focus on X together with the source spoke turns (a,p,c),(a,q,c),(a,r,c) and the source internality of p,q,r, rather than on arbitrary W-block boundaries.

No special Hamilton order on {a,c,p,q,r}, PAYABLE-FOUR payment, R24, or R5 is used.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R159"
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
