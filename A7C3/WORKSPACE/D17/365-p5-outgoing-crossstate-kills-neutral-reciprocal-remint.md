# One outgoing component-drop state kills the completely neutral reciprocal P5 remint

**Workspace:** D17
**State:** established
**Key:** `p5-outgoing-crossstate-kills-neutral-reciprocal-remint`

**Summary:** Retain the exact reciprocal-remint residue of SV87107, in particular the source P5 K=(u,a,m,c,v) and one reciprocal deletion cover H-{u,a}=(c,v)|Q with m internal in Q. Let r be the literal Q-successor of m. Split Q at m and absorb m into the source trimer (m,c,v), obtaining the three-cover (m,c,v)|Q_<m|Q_>m of H-{u,a}. The selected Q-state m->r crosses two components, so R176 may be applied to this specific outgoing state. Its R3 test on {r,m,c} has two branches. If (r,m,c) is tight, the tested source dimer (m,c) has a second head witness r in addition to source witness a, an R523 collision and hence new PAYABLE-FOUR ancestry through the current collision/absorber compiler. Otherwise (c,m,r) is tight. If r has a Q-successor s, then (c,m,r,s) is a literal P4, whose disjoint boundary dimers give a new mass-four birth using residual support. Thus a neutral branch forces r to be the terminal Q-vertex. Write Q=(Q^-,m,r), with Q^- nonempty. If |Q^-|=1, the source P5 K together with the automatic dimer formed by the sole Q^- vertex and r is already a spanning two-cover. If |Q^-|>=2, let k,l be the final two vertices of Q^-. If (k,l,r) were tight, P=Q^- followed by r would be a tight path disjoint from K and K|P would span H as two paths. Hence (k,l,r) is bad, so R3 gives the proper reverse trimer (r,l,k) tight. Its three vertices lie in W-{m}, hence outside K; SV83487 absorbs this new residual trimer into PAYABLE-FOUR with its trimer ancestry retained. Therefore the completely history-neutral reciprocal remint residue is empty: one outgoing m-neighbour test yields TWO-COVER or genuinely new PAYABLE-FOUR/collision ancestry. No Q=Qprime synchronization, R844 shield, or incoming/incoming case split is required. This is ancestry-level remint extinction, not a claim that paying the new birth strictly descends.


### 1. Input: one reciprocal exact-remint cover is enough
Retain the maximally history-neutral residue of SV87107. Thus the source P5 is the literal tight path

  K=(u,a,m,c,v),                                           (OX.1)

and one of the reciprocal exact deletion covers is

  H-{u,a}=(c,v) | Q,                                       (OX.2)

where Q is a Hamilton tight path on

  W=V(H)-{u,a,c,v}

and the physical source middle m is internal in Q. Write the local Q order as

  Q=(...,ell,m,r,...).                                     (OX.3)

Only (OX.2) will be used below. In particular the second reciprocal cover and the later synchronization Q=Q' from SV87835 are not needed.

The retained source P5 also belongs to the source fossil governed by SV83487, so every genuinely later proper trimer can be absorbed into PAYABLE-FOUR while retaining its physical trimer ancestry.

### 2. The outgoing state m->r is a literal component-drop cross-state
Inside the residue H-{u,a}, split Q at m and absorb m into the source end trimer (m,c,v). Since (m,c,v) is a source turn of K, this gives the literal three-cover

  R=(m,c,v) | Q_<m | Q_>m,                                (OX.4)

of the same residue for which

  T=(c,v) | Q                                               (OX.5)

is the exact two-cover (OX.2).

The selected Q-state

  m -> r                                                    (OX.6)

has m in the R-component (m,c,v) and r in Q_>m. Hence (OX.6) is itself a valid selected cross-state for accepted R176; no existential R159 choice is required.

The old R-neighbour of m in (m,c,v) is c. Applying R176 to the specific state (OX.6) therefore tests the literal triple {r,m,c}. Boundary antisymmetry gives exactly one of

  (r,m,c) tight,                                            (OX.7H)
  (c,m,r) tight.                                            (OX.7T)

If (OX.7H) holds, the oriented source dimer (m,c) is HEAD-signed by the new witness r. The source turn (a,m,c) already makes the same oriented dimer HEAD-signed by a. Since r lies in W and r!=a, accepted R523 gives a same-oriented two-head collision on (m,c). This is already new witness ancestry; through the current SV76748/SV83487-SV78086 collision route it re-enters PAYABLE-FOUR. Thus a completely history-neutral branch must satisfy (OX.7T).

### 3. If r is not terminal, (c,m,r) immediately grows to a new P4
Assume (OX.7T). If r has a successor s in Q, then Q tightness gives

  (m,r,s) tight.                                            (OX.8)

Together with (c,m,r) this makes

  P_4=(c,m,r,s)                                             (OX.9)

a literal proper P4. Its boundary dimers are

  (c,m), tail-signed by r,
  (r,s), head-signed by m.                                 (OX.10)

Their supports are disjoint, so (OX.10) is a direct opposite-sign mass-four birth. Its ancestry is genuinely new relative to the source P5 births because the second support (r,s) uses residual Q vertices outside the source five-set. Hence (OX.9) is a new PAYABLE-FOUR certificate.

Therefore a completely history-neutral branch can survive only if

  r is the terminal vertex of Q.                            (OX.11)

### 4. A terminal r forces either a spanning two-cover or a new residual reverse trimer
Under (OX.11), write

  Q=(Q^-,m,r),                                              (OX.12)

where Q^- is nonempty because m is internal. Every vertex of Q^- and the vertex r lie in W-{m}, hence are disjoint from the source P5 K.

If Q^- has order one, say Q^-=(ell), then (ell,r) is automatically a tight dimer. Consequently

  K | (ell,r)                                               (OX.13)

is a spanning two-cover of H, contradiction.

Thus Q^- has order at least two. Let k,ell be its final two vertices, so

  Q^-=(...,k,ell).                                         (OX.14)

Consider the vertex-simple path candidate obtained by bypassing m at the final Q seam:

  P=Q^- followed by r.                                     (OX.15)

Every turn of P inherited from Q^- is tight. Its only new consecutive turn is

  (k,ell,r).                                                (OX.16)

If (OX.16) were tight, P would be a tight path on W-{m}. Since K is a tight path on {u,a,m,c,v}, the two disjoint paths

  K | P                                                     (OX.17)

would span H, again contradicting pc(H)>2. Therefore (k,ell,r) is bad. By R3 its complete reversal is tight:

  (r,ell,k) tight.                                          (OX.18)

This is a proper tight trimer whose three physical vertices lie in W-{m}, so it is disjoint from the source P5 five-set. By SV83487, (OX.18) is absorbed into PAYABLE-FOUR with the residual reverse-trimer certificate retained in the birth ancestry. In particular it cannot be identified with any of the old source-only P5 births.

### 5. Extinction of the completely neutral reciprocal-remint cell
Sections 2--4 exhaust the outgoing state m->r in the single reciprocal cover (OX.2):

1. (r,m,c) tight gives an R523 collision on the old source dimer (m,c) with new witness r;
2. (c,m,r) tight with a successor s gives the new literal P4 (c,m,r,s) and a direct residual-support mass-four birth;
3. (c,m,r) tight with r terminal gives either the spanning two-cover (OX.13) or the new residual reverse trimer (r,ell,k), which SV83487 sends to PAYABLE-FOUR.

Hence the maximally history-neutral reciprocal P5 remint residue of SV87107 is empty. Every such putative remint already yields

  TWO-COVER

or

  GENUINELY NEW PAYABLE-FOUR / COLLISION ANCESTRY.           (OX.19)

This is stronger than residual-rail synchronization: the proof does not need Q'=Q, the second reciprocal deletion cover, either R844 insertion shield, or an incoming/incoming case split. The obstruction disappears before those coordinates matter.

### 6. Scope fence
The conclusion is ancestry-level exact-remint extinction, not a new numerical descent theorem. If (OX.19) produces a new PAYABLE-FOUR birth and that birth is subsequently paid, the normalized payment macro may still have a rank-flat branch. What is ruled out here is the claim that the reciprocal cell itself is completely history-neutral: its own outgoing Q-state necessarily exposes a new physical certificate before another payment is chosen.

Alternative payment descendants are never treated as simultaneously current. Only the source P5, the one exact reciprocal deletion cover, its graph-intrinsic component-drop comparison, and the newly exposed collision/P4/reverse-trimer certificate are combined. R24 and R5 are unused.


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
        "revision_id": "R176"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    },
    {
        "relation": "dependency",
        "revision_id": "R514"
    }
]
```