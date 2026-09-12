# The quiet singleton-star nucleus renormalizes to a transitive two-ended spectator gate frame

**Workspace:** D17
**State:** established
**Key:** `three-spoke-singleton-star-transitive-spectator-gate-frame`

**Summary:** In the fully synchronized singleton-star residue, write the top pair-deletion fiber as G=X union B with X={v,p,q,r}, common W-cover (v)|B, and source cover U|V in which p,q,r are internal. Outside an R408 endpoint/internal discrepancy, the P4-free cell X cannot be the cyclic R517/00 type: R593 Hamilton-extends X by the first spectator endpoint b0 with b0 one step from an end, so that P5 together with B-b0 is an exact top-fiber cover exposing a spoke. Hence X is a transitive matching-height four-cell. Moreover X+b0 and X+bm are P5-free, since any such P5 cannot have the spectator endpoint as a path endpoint without Hamiltonizing X, so it again exposes a spoke when paired with the remaining B suffix/prefix. For every x in X, failure of an immediate top-fiber cover forces the universal reverse endpoint stars (b1,b0,x) and (x,bm,b_{m-1}). Accepted R549/R534 therefore give the full matching-gate packets at both spectator ends, and pure local R582 yields an endpoint-favorable Hamilton P5 on {b0,bm} union (X-{x}) for some x in X. This is a quarantine-clean static renormalization, not absorption; R540 bad-hole conclusions are not imported because the top fiber itself has pc=2.

### 1. Input: the fully synchronized singleton-star residue
Retain a hypothetical smallest counterexample H and the current singleton-star residue. Thus

  H-{a,c}=U|V

is the retained exact source frame, p,q,r are distinct source-internal same-orientation spokes,

  (a,p,c), (a,q,c), (a,r,c)

are tight, and with

  X={v,p,q,r}

the synchronized lower cube has the exact W-cover

  F=(v)|B,

where B=(b_0,...,b_m) is a nontrivial Hamilton path. The top fiber

  G=H-{a,c}=X union V(B)

has the retained exact cover U|V in which p,q,r are all internal. The preceding rank-two coherence theorem also forces X to be non-Hamiltonian, i.e. X has no tight Hamilton P4.

Throughout this section, an R408 endpoint/internal discrepancy on the same top fiber G is retained as an explicit output rather than declared closure.

### 2. The cyclic P4-free four-cell cannot remain quiet
Choose any tight trimer on three vertices of X by R8 and apply the universal four-cell compiler R518 to the fourth vertex. Since X has no Hamilton P4, X lies in one of the four exact R516/R517 no-P4 signatures: three transitive matching-height cells or the cyclic 00 cell.

Suppose X is the cyclic 00 cell. Apply accepted R593 to the fifth vertex b_0. It gives a Hamilton P5 Q on X union {b_0} in which b_0 occurs one step from an end. Hence both endpoints of Q lie in X. At most one of those two endpoints is v, so at least one is a source spoke in {p,q,r}. The untouched suffix B[1,m] is a tight path and is vertex-disjoint from Q. Therefore

  Q | B[1,m]

is an exact two-cover of the top fiber G exposing a source spoke as a rail endpoint. In U|V every source spoke is internal. Accepted R408 applied to these two exact covers of the same proper residue gives its endpoint/internal component-drop output.

Consequently, outside R408 geometry,

  X is a transitive matching-height P4-free four-cell.          (SG.1)

### 3. Both spectator endpoint five-sets are P5-free
Assume the R408 output has not occurred. Suppose X union {b_0} had a Hamilton P5 Q. The vertex b_0 cannot be an endpoint of Q, because deleting an endpoint from a tight path leaves a tight path, which would give a Hamilton P4 on X, contrary to (SG.1). Thus both endpoints of Q lie in X, and again at least one endpoint is a source spoke. Then

  Q | B[1,m]

is an exact top-fiber two-cover exposing that spoke, so R408 occurs. Contradiction to the quiet branch. Therefore X+b_0 is P5-free. The terminal argument is identical, using B[0,m-1], and gives

  X+b_0 and X+b_m are both P5-free.                       (SG.2)

### 4. Quietness forces universal reverse stars at both spectator ends
Fix any x in X. By R8 choose a tight Hamilton trimer C_x on X-{x}.

If (x,b_0,b_1) were tight, then

  (x,b_0,b_1,...,b_m) | C_x

would be an exact two-cover of G. If x is one of p,q,r, that spoke is itself a rail endpoint. If x=v, both endpoints of the trimer C_x lie in {p,q,r}. Thus in every case this exact cover exposes a source spoke and R408 applies against U|V. Hence in the quiet branch (x,b_0,b_1) is bad for every x in X, and R3 gives

  (b_1,b_0,x) tight for every x in X.                     (SG.3)

Dually, if (b_{m-1},b_m,x) were tight then B followed by x together with C_x would give the same R408 discrepancy. Therefore

  (x,b_m,b_{m-1}) tight for every x in X.                 (SG.4)

These are simultaneous graph-intrinsic two-ended reverse stars on the whole transitive cell X.

### 5. The spectator endpoints carry the full matching-gate packets
Apply accepted R549 to the P5-free five-set X+b_0. It supplies a fully outgoing M_L edge and a fully incoming M_R edge at b_0. Accepted R534 then supplies the alternating middle matching: exactly one M_S edge is fully outgoing from b_0 and its complementary M_S edge is fully incoming.

Apply the same two pure local theorems at b_m. Again the two M_S edges have opposite full-gate polarities there. Thus, after naming one endpoint as L=b_0 and the other R=b_m, the hypotheses of accepted R582 hold: at L one M_S edge is fully outgoing and its complement fully incoming, while at R one M_S edge is fully incoming and its complement fully outgoing.

R582 therefore yields some x in X and a literal endpoint-favorable Hamilton P5

  K_x on {b_0,b_m} union (X-{x}).                         (SG.5)

Retain x, the literal order K_x, its endpoint positions, the two endpoint gate packets, and the universal reverse stars (SG.3)-(SG.4).

### 6. Scope and the next missing splice
This is a static renormalization, not three-spoke frame absorption. In particular, do NOT import R540's conclusion that the unique seam in an endpoint-favorable cut must be bad: R540 obtains that conclusion from pc(ambient)>2, while the present ambient top fiber G=H-{a,c} already has pc(G)=2. Its path construction may later be reused only with a fresh complete seam ledger.

The unresolved global data are now sharply localized: a transitive matching-height four-cell X={v,p,q,r}, one Hamilton spectator rail B, the two universal reverse endpoint stars, the two full matching-gate packets, an endpoint-favorable cross-end P5 K_x, and the external source trimers (a,s,c) on the three source spokes. The next consumer must couple that packet back to the anchors a,c or to the retained source cover U|V and obtain a spanning two-cover or a separately justified global improvement.

R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R8"
    },
    {
        "relation": "dependency",
        "revision_id": "R518"
    },
    {
        "relation": "dependency",
        "revision_id": "R593"
    },
    {
        "relation": "dependency",
        "revision_id": "R408"
    },
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R549"
    },
    {
        "relation": "dependency",
        "revision_id": "R534"
    },
    {
        "relation": "dependency",
        "revision_id": "R582"
    }
]
```
