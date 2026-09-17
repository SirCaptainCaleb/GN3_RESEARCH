# Every Hamilton P5 carries a bounded root-capture circuit whose arcs currentize on the same deleted pair

**Workspace:** D17
**State:** established
**Key:** `closed-return-p5-root-capture-currentization-circuit`

**Summary:** Fix a Hamilton P5 K from the SV58280 family object. For each root d in K choose any exact H-d two-cover. R508 forces a selected crossing between K-d and H-K; write its K-endpoint k. Choose a third K-vertex w as a singleton-sign witness for d. Since the crossing avoids w, R527 may orient its dimer marker to capture k. The actualized opposite support has order two and signed anchor k, so R428 preserving d either closes H or pays exactly to the ancestry-bearing floor {d,k}. Thus every chosen root crossing gives a physical directed return edge d->k inside K. Puncturing k from the SAME H-d representative currentizes that edge: if k was a rail endpoint, the punctured representative is an exact two-cover of H-{d,k}; if k was internal, it is a literal three-cover of H-{d,k}, while R429 supplies an exact two-cover of the same residue and R159 yields a graph-intrinsic component-drop pair. Choosing one edge for each of the five roots gives, outside closure, a fixed-point-free map K->K and hence a directed cycle of length 2..5. Every cycle arc is liftable and carries both capture/payment ancestry and same-pair current geometry. This is a bounded return-circuit extractor for G22, not yet no-sink extinction.

### 1. One rooted singleton fiber gives a capture edge inside K
Retain a Hamilton tight P5 K on five physical vertices in a hypothetical smallest counterexample H, in particular the K supplied by SV58280. Put E=V(H)-V(K), which is nonempty in that application. Fix a root d in V(K), and choose one literal exact two-cover

  T_d = U_d | V_d

of H-d.

Apply accepted R508 with deletion set D={d}, absorbable block S=V(K)-{d}, and carrier path Q=K. Every such T_d selects a physical crossing between K-d and E. Fix one selected crossing and write its endpoints

  {k,e},   k in V(K)-{d},   e in E.                       (RC.1)

Because K has five vertices, choose

  w in V(K)-{d,k}.                                        (RC.2)

Treat singleton (d) as a signed support with exact witness w; this is legitimate by the accepted singleton signed-support convention, since the two-vertex path through d,w is automatic. The marker {k,e} is disjoint from {d,w}. Accepted R527 therefore applies in its capture branch. Orient the two-vertex marker so that the K-side endpoint k is the actualization endpoint appropriate to the chosen polarity of (d). R527/R526 then gives either a spanning two-cover already in actualization or a balanced opposite-sign pair consisting of singleton (d) and an order-two signed support Q_{d,k} whose signed physical endpoint is exactly k. The support Q_{d,k} is either the oriented crossing marker itself or the short witness-plus-k support from the failed terminal marker test; in both cases it has order two and signed anchor k.

Apply accepted R428 with singleton d fixed. In the nonclosing case the opposite support has order two. Proof-level R175, in the appropriate head/tail orientation, clips its unsigned end and preserves its signed end. Hence the nonclosing descendant is not an arbitrary both-singleton floor: it is exactly

  {d,k}.                                                   (RC.3)

Retain T_d, the selected crossing (RC.1), witness w, marker orientation, captured endpoint k, actualization test, pair birth, and payment/refund certificate. We call this a ROOT-CAPTURE EDGE d -> k.

### 2. The same capture edge currentizes on H-{d,k}
The return edge d->k is not merely historical. Delete the captured vertex k from the ORIGINAL exact singleton-deletion representative T_d. There are exactly two physical cases.

#### END case
Suppose k is an endpoint of its T_d rail. Then T_d-k is a path cover of H-{d,k} by at most two nonempty paths. Accepted R429 says pc(H-{d,k})=2, so T_d-k cannot collapse to one Hamilton path. Consequently it is itself a literal exact two-cover

  H-{d,k} = P | Q.                                        (RC.4)

Thus the root-capture edge d->k already carries a current exact pair-deletion representative on its own endpoint pair.

#### INTERNAL case
Suppose k is internal on its T_d rail. Deleting k splits that rail into two nonempty path intervals, while the other T_d rail remains nonempty. Hence T_d-k is a literal three-cover

  R_{d,k}

of the same pair-deletion residue W=H-{d,k}. Accepted R429 supplies an exact two-cover

  F_{d,k}

of W. Since W is proper and 2<3, accepted R159 applies to R_{d,k},F_{d,k} and yields a graph-intrinsic balanced opposite-sign pair with component-drop provenance on this exact physical deleted pair.

Therefore every capture edge has the SAME-PAIR CURRENTIZATION dichotomy

  d->k  =>  exact H-{d,k} two-cover from puncturing T_d,
             OR an R159 component-drop packet on H-{d,k}.  (RC.5)

The selected crossing in T_d need not remain current after puncturing; RC.5 retains the source representative and the endpoint/internal role of k as ancestry.

### 3. Five roots force a bounded liftable return circuit
Choose, for every d in V(K), one exact singleton-deletion cover T_d and one R508 crossing in it. If any corresponding capture/actualization/payment branch closes H, stop. Otherwise define

  f(d)=k

from the K-side endpoint of the chosen crossing. By construction f(d) != d. Thus f is a fixed-point-free function on the five-element set V(K). Its functional digraph contains a directed cycle

  d_0 -> d_1 -> ... -> d_{r-1} -> d_0,    2 <= r <= 5.    (RC.6)

Every arc of RC.6 is liftable by an actual exact H-d_i representative, one selected K-d_i|E crossing, a witness/marker capture, exact floor payment to {d_i,d_{i+1}}, and the same-pair currentization alternative RC.5. Hence RC.6 is not a graph of naked normalized tuples or an unbounded history quotient. It is a bounded physical return circuit with at most five arcs and bounded certificates per arc.

### 4. Relation to the G22 closed-family problem
In a reconstruction-closed nonclosing family, any chosen set of five root crossings must be absorbable. RC.6 shows that a rank-flat sink cannot hide behind indefinitely changing endpoint pairs without already containing a bounded ancestry-bearing circuit of physical pair returns. Moreover every arc either supplies a current exact pair-deletion frame on its own pair or a component-drop balanced pair on that same pair. This is a stronger interface than a paid floor alone and is compatible with the global-completed-anchor saturation of SV58856.

The surviving obligation is to consume a shortest circuit RC.6. In particular, one must show that the cyclic family of same-pair exact frames / component-drop packets cannot all normalize back into one closed rank-flat family. No such extinction is asserted here.

### 5. Scope fences
Alternative root branches and their paid descendants are not asserted simultaneously current. R159 pairs in INTERNAL arcs are graph-intrinsic historical certificates, not selected supports. A cycle of root labels is not itself rank descent. This section does not identify its arcs with the support-partition moves counted by SV53785's global Phi, because payment alone does not currentize a replacement partition. The new content is precisely the bounded liftable circuit plus RC.5.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R508"
    },
    {
        "relation": "dependency",
        "revision_id": "R527"
    },
    {
        "relation": "dependency",
        "revision_id": "R428"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    },
    {
        "relation": "dependency",
        "revision_id": "R159"
    }
]
```