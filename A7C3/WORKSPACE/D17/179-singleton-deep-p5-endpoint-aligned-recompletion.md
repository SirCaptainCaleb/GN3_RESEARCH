# Endpoint alignment localizes every grown boundary P5 to one physical residual-M boundary packet

**Workspace:** D17
**State:** established
**Key:** `singleton-deep-p5-endpoint-aligned-recompletion`

**Summary:** For each of the four boundary-P4 growth rows of SV15718, cyclic endpoint alignment plus the exact R509 one-hole recompletion reduces the residual middle merge to a physical endpoint-dimer event. For G1/G2, residual |M|>=3 gives spanning closure, a labelled P4, or an R542 two-witness packet on the reverse boundary dimer; if both endpoint alignments fail R579 gives a P4. For G3/G4 the same conclusion holds for every |M|>1, modulo explicit same-support R435 geometry when the opposite cyclic wrap passes. The only unresolved overlap is |M|=2 in G1/G2; there the two successful alignments form a literal tight 5-cycle and the lone residual vertex reverse-signs both sides of every cycle boundary dimer. No claim is made that this short cyclic cell closes H.


### 1. Setup and scope
Retain the pending boundary-growth parent `singleton-deep-boundary-p4-growth-consumer` exact section version SV15718 only as working ancestry. Thus

  R=(s,M,p,q)|B

is an exact H-t two-cover, M=(m_1,...,u) is nonempty, and the Hamilton boundary-four-set branch has been reduced to one of the four literal tight P5s

  G_1=(s,q,t,p,u),
  G_2=(m_1,s,t,q,p),
  G_3=(m_1,s,t,p,q),
  G_4=(q,s,t,p,u).

If |M|=1 the parent already closes H. Assume |M|>1. This section does not regard P5 growth by itself as consumption. Instead it aligns the absorbed endpoint with the old M-rail and applies accepted R509/P524 to the resulting literal endpoint crossing. Every seam below is an actual physical seam; no generic payment is taken.

### 2. G1: terminal absorption localizes to the reverse initial dimer
Write M=(m_1,...,v,u), so v is the actual predecessor of u.

For the absorbed endpoint u, head-rotate G_1. The sole R548 seam is A=(u,s,q). If A is tight, Q_u=(u,s,q,t,p) is tight. Delete D_u={s,q,t,p}. The literal cover (m_1,...,v,u)|B of H-D_u is exact and selects the aligned C-to-S state v->u for S={u}. Accepted R509 therefore gives a one-hole spanning proposal whose sole hole is (v,u,s). It cannot be tight, so R3 gives

  (s,u,v) tight.                                      (EA.1)

For the boundary endpoint s, tail-rotate G_1. Its sole seam is B_1=(p,u,s). If B_1 is tight, Q_s=(q,t,p,u,s) is tight. Deleting D_s={q,t,p,u}, the literal cover (s,m_1,...,v)|B selects the aligned S-to-C state s->m_1 for S={s}. R509 gives the one hole (u,s,m_1), hence

  (m_1,s,u) tight.                                    (EA.2)

If both A and B_1 are bad, accepted R579 on G_1 gives the literal reverse P4 (q,s,u,p).

Assume A is tight. Then the full proposal (q,t,p,u,s,m_1,...,v)|B has only the two remaining boundary turns B_1=(p,u,s) and C=(u,s,m_1). If both pass, it is a spanning two-cover of H. If B_1 is bad, R3 gives (s,u,p); together with (EA.1), the tested dimer (s,u), which is the reverse initial dimer of the tight trimer (u,s,q), has the two distinct tail witnesses p and v. This is exactly accepted R542/P618 short-carrier geometry.

If C is bad, R3 gives (m_1,s,u). Together with (EA.1) these are opposite-polarity certificates on the same tested dimer (s,u). When m_1 != v, equivalently |M|>=3, accepted R523 gives the literal P4 (m_1,s,u,v). The argument starting from B_1 instead of A is the exact endpoint dual. Consequently for |M|>=3, G_1 gives a spanning two-cover, a labelled P4, or an R542 packet on a physical reverse boundary dimer.

### 3. G2: source absorption is the exact dual
Write M=(m_1,m_2,...,u). Tail-rotating G_2 tests A_2=(q,p,m_1). If A_2 passes, Q=(s,t,q,p,m_1) is tight. With S={m_1} and the literal exact cover M|B, R509 at the aligned S-to-C state m_1->m_2 gives the sole hole (p,m_1,m_2), hence

  (m_2,m_1,p) tight.                                  (EA.3)

Head-rotating G_2 tests B_2=(p,m_1,s). If B_2 passes, use S={p} and the literal exact cover (m_2,...,u,p)|B; its aligned C-to-S state u->p gives the sole hole (u,p,m_1), hence

  (m_1,p,u) tight.                                    (EA.4)

If both A_2 and B_2 fail, R579 gives the literal P4 (s,m_1,p,q).

If A_2 passes, the proposal (m_2,...,u,p,m_1,s,t,q)|B has only the two boundary turns (u,p,m_1) and (p,m_1,s). Full success closes H. Failure of the first gives (m_1,p,u), which concatenates with (EA.3) to P4 (m_2,m_1,p,u) when m_2 != u, equivalently |M|>=3. Failure of the second gives (s,m_1,p); together with (EA.3), s and m_2 are two distinct head witnesses on the tested reverse terminal dimer (m_1,p) of the tight trimer (q,p,m_1), hence accepted R542 applies. The B_2-first argument is dual. Thus |M|>=3 gives the same closure/P4/R542 trichotomy.

### 4. G3 has no short overlap
For G_3=(m_1,s,t,p,q), tail rotation tests A_3=(p,q,m_1). If A_3 is bad, test the opposite head-wrap seam (q,m_1,s). If it is also bad, R579 gives P4 (s,m_1,q,p). If it passes, compare the resulting same-support cyclic order with G_3; accepted R435 gives explicit reversal/reverse-trimer/cycle geometry.

Assume A_3 is tight. R509 with S={m_1} in M|B gives (q,m_1,m_2) bad, hence

  (m_2,m_1,q) tight.                                  (EA.5)

The old H-t active rail (M,p,q) tail-rotates through A_3 to (m_2,...,u,p,q,m_1). If (q,m_1,s) were tight, appending s,t using the retained turn (m_1,s,t) would give a spanning path outside B and close H. Hence (q,m_1,s) is bad and

  (s,m_1,q) tight.                                    (EA.6)

The two distinct witnesses s,m_2 head-sign the tested dimer (m_1,q), the reverse terminal dimer of (p,q,m_1). Accepted R542 applies. This remains valid when |M|=2.

### 5. G4 is the terminal dual
For G_4=(q,s,t,p,u), head rotation tests A_4=(u,q,s). If A_4 is bad, test the opposite tail-wrap seam (p,u,q). Double failure gives the R579 P4 (s,q,u,p); single success gives an actual same-support cyclic order and hence explicit R435 geometry on comparison.

Assume A_4 is tight. With S={u}, R509 on the literal exact cover (m_1,...,v,u)|B gives (v,u,q) bad, hence

  (q,u,v) tight.                                      (EA.7)

The old H-t active prefix (q,s,M) head-rotates through A_4 to (u,q,s,m_1,...,v). If (p,u,q) were tight, prepending t,p using the retained turn (t,p,u) would close H with B. Therefore (p,u,q) is bad and

  (q,u,p) tight.                                      (EA.8)

The distinct witnesses p,v tail-sign the tested dimer (q,u), the reverse initial dimer of (u,q,s). Accepted R542 applies, again including |M|=2.

### 6. The unique overlap left by endpoint alignment
For |M|>=3 all four P5 growth rows are therefore reduced before generic payment to

  spanning two-cover | labelled P4 | explicit R435 geometry | physical R542 short-carrier packet.

For |M|=2, G_3 and G_4 have the same reduction. Only G_1/G_2 retain a witness-coincidence overlap in the opposite-polarity branch of Sections 2-3.

For G_1 write M=(v,u). If both endpoint-alignment seams (u,s,q) and (p,u,s) pass, then the five cyclic turns (s,q,t), (q,t,p), (t,p,u), (p,u,s), (u,s,q) show that C=(s,q,t,p,u) is a literal tight 5-cycle. The two aligned R509 failures give (s,u,v) and (v,s,u), while the old H-t row supplies (s,v,u) and (v,u,p).

Moreover C+v is non-Hamiltonian, since any Hamilton path on these six vertices together with B would two-cover H. For every cyclic rotation of C, prepending or appending v must therefore fail. By R3, for every directed boundary state a_i->a_{i+1} of C the reverse tested dimer a_{i+1}->a_i is both head- and tail-signed by v:

  (v,a_{i+1},a_i), (a_{i+1},a_i,v) tight.

This is a genuine finite short-overlap cell, not an R966 instance: only the support C-{t}+v is currently known Hamiltonian, so the two-ended replacement hypothesis of R966 is not available. The G_2 overlap is its exact source/terminal dual. No closure is claimed for these two order-five active-rail cells.

### 7. Consequence
The residual middle length no longer appears in the seam complexity of the grown boundary P5 except in the explicit |M|=2 G_1/G_2 overlap. In every longer cell, and in G_3/G_4 even at the floor, endpoint alignment converts the residual-M merge into a one-hole R509 certificate and then into closure, labelled P4, exact R435 geometry, or an R542 packet on an actual reverse boundary dimer. The physical absorbed M endpoint, the literal complement B, and every predecessor/successor witness are retained.


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
        "revision_id": "R509"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    },
    {
        "relation": "dependency",
        "revision_id": "R542"
    },
    {
        "relation": "dependency",
        "revision_id": "R548"
    },
    {
        "relation": "dependency",
        "revision_id": "R579"
    }
]
```
