# History-neutral full-P5 replay forces the same middle and a reciprocal dimer-rail Hamilton residue

**Workspace:** D17
**State:** established
**Key:** `p5-exact-replay-reciprocal-dimer-rail-residue`

**Summary:** Building on current firewall SV84932, exact source-oriented replay of (u,a) tail by m through R434 forces the returned middle b' into {u,m}, while replay of (c,v) head by m forces b' into {m,v}; hence b'=m and the returned frame literally selects u->m->v. If the two R434 actualizations are also ancestry-neutral, their outputs must remint the old opposite outer dimers. R526's short branch contains the old witness m, so exact remint of (c,v) or (u,a) can only occur through the whole-marker branch. Thus one gets reciprocal exact covers H-{u,a}=(c,v)|Q and H-{c,v}=(u,a)|Q' on the common residual support W. The source middle m is internal in both Hamilton residual rails, else the source P5 plus the punctured residual rail two-covers H. Splitting at m and absorbing it into the appropriate source end trimer gives a localized 3-to-2 R159/R176 packet on each reciprocal residue; an outgoing-m crossing on the right residue has one R3 branch giving an R523 collision on (m,c), while the left reciprocal side analogously has one branch giving an opposite-polarity P4 on (a,m); incoming-m crossings give only the generic localized R176 birth. R844 additionally forces a reversed bad-turn certificate in each complete insertion window immediately before and after m, not necessarily on a turn containing m. Therefore the final history-neutral G27 recurrence is reduced to one finite same-middle reciprocal-dimer-rail Hamilton cell. This is reduction, not yet extinction.


### 1. Input: the strengthened bilateral fossil firewall
Retain the source P5

  K=(u,a,m,c,v)

and the exact-history-neutral exceptional branch of the current firewall SV84932. The opposite outer orientation has already been excluded there. Hence any completely history-neutral nonclosing rank-flat same-E return, E={a,c}, must use the source orientation and reproduce both outer source boundary certificates

  (u,a) tail-signed by m,
  (c,v) head-signed by m.                                  (ER.1)

The source middle turn (a,m,c) remains graph-intrinsic historical data. No old payment descendant is treated as simultaneously current with the returned frame.

### 2. Exact full-P5 replay fixes the returned middle
Let b' be the internal middle of the returned exact H-E frame, with selected predecessor r and successor s.

For the predecessor channel, accepted R434 says exactly one of

  (r,a,b'),   (b',a,r)

is tight. The resulting a-anchored tail dimer is respectively (r,a), witnessed by b', or (b',a), witnessed by r. To replay the exact old certificate (u,a) tail-signed by m, either

  r=u and b'=m,

or

  b'=u and r=m.

Hence

  b' in {u,m}.                                               (ER.2)

Dually, the successor channel tests exactly one of

  (b',c,s),   (s,c,b')

and its c-anchored head dimer is respectively (c,s), witnessed by b', or (c,b'), witnessed by s. Exact replay of (c,v) head-signed by m therefore forces

  b' in {m,v}.                                               (ER.3)

Because u,m,v are distinct in the vertex-simple source P5, (ER.2)-(ER.3) give

  b'=m.                                                       (ER.4)

The exact witness identities then force r=u and s=v. Thus the returned frame literally selects

  u -> m -> v.                                                (ER.5)

So a completely history-neutral full-P5 replay cannot migrate to another physical middle.

### 3. Maximal neutrality forces reciprocal dimer-rail actualization
Now inspect the balanced-pair actualization attached to each replayed R434 endpoint dimer.

On the a-side the replayed tail dimer (u,a), whose old sign witness is m, is actualized by R526 using a nontrivial marker path disjoint from {u,a,m}. If the resulting opposite-polarity support is not literally the old outer head dimer (c,v), then the return has already created new support/orientation ancestry and is outside the maximally neutral cell. Suppose instead that the actualized support is exactly (c,v).

In the tail-signed dual of R526, the bad terminal-test branch creates a short head support containing the old sign witness m. Since m is distinct from c,v, that branch cannot equal (c,v). Therefore exact remint of (c,v) can occur only in the whole-marker branch, and the actualizing marker rail itself is the dimer (c,v). The exact deletion frame used by R434 is consequently

  H-{u,a}=(c,v) | Q.                                        (ER.6)

The c-side is exact dual. If its actualized support is literally the old tail dimer (u,a), the short R526 branch would contain the old witness m and hence cannot equal (u,a). Therefore the whole marker rail is (u,a), giving

  H-{c,v}=(u,a) | Q'.                                       (ER.7)

The two residual Hamilton rails Q,Q' have the common support

  W=V(H)-{u,a,c,v}.                                         (ER.8)

Thus the absolute history-neutral remint residue is a pair of reciprocal dimer-rail deletion covers on one common Hamilton residual support.

### 4. The source middle is internal in both residual Hamilton rails
The source middle m lies in W. It cannot be an endpoint of Q. If it were, deleting m from the endpoint of the Hamilton path Q would leave one tight path Q-m. The retained source P5

  K=(u,a,m,c,v)

is disjoint from Q-m, and together K | (Q-m) would be a spanning two-cover of H, contradicting pc(H)>2.

Hence m is internal in Q. The same argument applies to Q'. Therefore

  m is internal in both Q and Q'.                           (ER.9)

Write, in one reciprocal cover,

  Q=(...,ell,m,r,...),                                      (ER.10)

with both residual pieces Q_<m and Q_>m nonempty.

### 5. Each reciprocal dimer rail carries a localized 3-to-2 component-drop certificate
On the residue H-{u,a}, (ER.6) is a literal exact two-cover

  T=(c,v) | Q.                                               (ER.11)

The retained source turn (m,c,v) is tight. Splitting Q at its internal vertex m therefore gives a literal three-cover of the SAME residue H-{u,a}:

  R=(m,c,v) | Q_<m | Q_>m.                                  (ER.12)

Thus R159 applies to the component drop R -> T. More precisely, the only selected T-states capable of crossing distinct R-components are the two Q-states incident with m, namely ell->m and m->r in the displayed Q orientation. Hence the R159/R176 birth is localized at an m-neighbour.

For example, if the selected cross state m->r is used, its R-component in (ER.12) is the source trimer (m,c,v), whose old neighbour of m is c. R176 tests the literal triple {r,m,c}. If (r,m,c) is tight, then the tested oriented source dimer (m,c) is head-signed by the new witness r. But the source P5 already makes (m,c) head-signed by witness a through (a,m,c). Since r lies in W and hence r!=a, accepted R523 gives a same-oriented two-head collision on (m,c). If instead the reverse turn (c,m,r) is tight, R176 gives its alternate singleton-plus-dimer balanced-pair birth with the same cross-state provenance. If R159 instead selects the incoming boundary ell->m, R176 still gives a valid m-local component-drop birth, but its signed support is determined by the R-component containing ell; no source-dimer collision follows automatically.

The reciprocal cover H-{c,v}=(u,a)|Q' gives the same localization at an edge incident with m. If its selected crossing is an outgoing state m->r', R176 tests {r',m,a}. The branch (a,m,r') tight gives a tail certificate on the tested dimer (a,m); together with the retained source head certificate (u,a,m), accepted R523 gives the literal P4 (u,a,m,r'). The other R3 branch is a head certificate on the reverse tested orientation (m,a). If the selected crossing is incoming to m, retain only the generic localized R176 birth. Thus neither reciprocal residue automatically produces a source-dimer collision.

These are alternative representative-local component-drop certificates. No simultaneous currentness of Q and Q' is asserted.

### 6. The reciprocal cell also carries compulsory insertion shields around m
Use the four-set {u,a,c,v} with its literal exact two-cover

  (u,a) | (c,v)                                             (ER.13)

as the exact core and use Q as the Hamilton complement. Accepted R844 applies because pc(H)>2.

Insert the block (u,a) immediately before the internal position m of Q while leaving the other core rail (c,v) untouched. The complete R844 seam window cannot be all tight, else the inserted path together with (c,v) would form a spanning two-cover of H. Hence at least one left insertion seam is bad, and R3 certifies its complete reversal.

Dually, insert the block (c,v) immediately after m while leaving (u,a) untouched. Again at least one right insertion seam is bad, and its complete reversal is tight.

Therefore the maximally neutral reciprocal-remint residue carries a reversed bad-turn certificate in each of the two complete insertion windows immediately before and immediately after the SAME internal physical middle m. The certified reversed turn need not itself contain m; the full R844 window and insertion slot remain part of the certificate.

### 7. G27 reduction and scope fence
Combining SV84932 with Sections 2--6, a rank-flat same-E recurrence can remain completely history-neutral only inside the following finite cell:

1. the source P5 K=(u,a,m,c,v) is replayed literally in the source outer orientation;
2. the returned middle is the same physical vertex m and the frame selects u->m->v;
3. both endpoint actualizations remint the old opposite outer dimers through their whole-marker branches, forcing the reciprocal exact covers (ER.6)-(ER.7);
4. m is internal in both Hamilton residual rails Q,Q';
5. each reciprocal deletion cover carries an m-local R159/R176 component-drop birth; when the selected crossing is outgoing from m, one R3 branch on the right residue yields an R523 collision on (m,c), while the corresponding branch on the left residue yields an opposite-polarity same-dimer P4 on (a,m); incoming crossings carry no automatic source-dimer interaction; and
6. R844 supplies one reversed bad-turn certificate in each complete insertion window adjacent to m, without asserting that the reversed turn itself contains m.

Every earlier deviation has already left the exact history-neutral cell by producing new PAYABLE-FOUR ancestry, a raw R523 collision, explicit nonquiet portal geometry, TWO-COVER, or strict old-clock descent through the established G27 machinery.

This is a reduction, not yet stack extinction. The remaining G27 target is now finite and exact: combine the two reciprocal m-local component-drop/seam certificates and show that this Hamilton-residual cell forces cross-generation interaction, a new PAYABLE-FOUR birth, TWO-COVER, or strict descent.

R24 and R5 are unused.


## References

```json
[
    {
        "status": {
            "label": "accepted · usable · revision-valid · active · current",
            "headline": "Usable: intrinsic/foundational (R3)",
            "blocker_ids": [
            ],
            "object_type": "axiom",
            "revision_id": "R3",
            "current_usable": true,
            "revision_valid": true,
            "lifecycle_status": "active",
            "current_revision_id": "R3",
            "is_current_revision": true,
            "canonical_review_status": "accepted"
        },
        "relation": "dependency",
        "revision_id": "R3",
        "resolved_label": "accepted · usable · revision-valid · active · current",
        "proof_routes_call": "get_revision_proof_routes(array['R3'],'A7C3',false)",
        "claim_contract_call": "get_claim_contracts(array['R3'],false)",
        "full_proof_routes_call": "get_revision_proof_routes(array['R3'],'A7C3',true)"
    },
    {
        "status": {
            "label": "accepted · usable · revision-valid · active · current · proof P555:accepted/valid",
            "headline": "Usable via P555 (fully reconstructible)",
            "blocker_ids": [
            ],
            "object_type": "theorem",
            "revision_id": "R159",
            "current_usable": true,
            "revision_valid": true,
            "lifecycle_status": "active",
            "supporting_proof": {
                "is_valid": true,
                "proof_id": "P555",
                "proof_kind": "full",
                "review_status": "accepted",
                "dependency_complete": true
            },
            "current_revision_id": "R159",
            "is_current_revision": true,
            "canonical_review_status": "accepted"
        },
        "relation": "dependency",
        "revision_id": "R159",
        "resolved_label": "accepted · usable · revision-valid · active · current · proof P555:accepted/valid",
        "proof_routes_call": "get_revision_proof_routes(array['R159'],'A7C3',false)",
        "claim_contract_call": "get_claim_contracts(array['R159'],false)",
        "full_proof_routes_call": "get_revision_proof_routes(array['R159'],'A7C3',true)"
    },
    {
        "status": {
            "label": "accepted · usable · revision-valid · active · current · proof P540:accepted/valid",
            "headline": "Usable via P540 (fully reconstructible)",
            "blocker_ids": [
            ],
            "object_type": "theorem",
            "revision_id": "R176",
            "current_usable": true,
            "revision_valid": true,
            "lifecycle_status": "active",
            "supporting_proof": {
                "is_valid": true,
                "proof_id": "P540",
                "proof_kind": "full",
                "review_status": "accepted",
                "dependency_complete": true
            },
            "current_revision_id": "R176",
            "is_current_revision": true,
            "canonical_review_status": "accepted"
        },
        "relation": "dependency",
        "revision_id": "R176",
        "resolved_label": "accepted · usable · revision-valid · active · current · proof P540:accepted/valid",
        "proof_routes_call": "get_revision_proof_routes(array['R176'],'A7C3',false)",
        "claim_contract_call": "get_claim_contracts(array['R176'],false)",
        "full_proof_routes_call": "get_revision_proof_routes(array['R176'],'A7C3',true)"
    },
    {
        "status": {
            "label": "accepted · usable · revision-valid · active · current · proof P446:accepted/valid",
            "headline": "Usable via P446 (fully reconstructible)",
            "blocker_ids": [
            ],
            "object_type": "theorem",
            "revision_id": "R434",
            "current_usable": true,
            "revision_valid": true,
            "lifecycle_status": "active",
            "supporting_proof": {
                "is_valid": true,
                "proof_id": "P446",
                "proof_kind": "full",
                "review_status": "accepted",
                "dependency_complete": true
            },
            "current_revision_id": "R434",
            "is_current_revision": true,
            "canonical_review_status": "accepted"
        },
        "relation": "dependency",
        "revision_id": "R434",
        "resolved_label": "accepted · usable · revision-valid · active · current · proof P446:accepted/valid",
        "proof_routes_call": "get_revision_proof_routes(array['R434'],'A7C3',false)",
        "claim_contract_call": "get_claim_contracts(array['R434'],false)",
        "full_proof_routes_call": "get_revision_proof_routes(array['R434'],'A7C3',true)"
    },
    {
        "status": {
            "label": "accepted · usable · revision-valid · active · current · proof P546:accepted/valid",
            "headline": "Usable via P546 (fully reconstructible)",
            "blocker_ids": [
            ],
            "object_type": "theorem",
            "revision_id": "R526",
            "current_usable": true,
            "revision_valid": true,
            "lifecycle_status": "active",
            "supporting_proof": {
                "is_valid": true,
                "proof_id": "P546",
                "proof_kind": "full",
                "review_status": "accepted",
                "dependency_complete": true
            },
            "current_revision_id": "R526",
            "is_current_revision": true,
            "canonical_review_status": "accepted"
        },
        "relation": "dependency",
        "revision_id": "R526",
        "resolved_label": "accepted · usable · revision-valid · active · current · proof P546:accepted/valid",
        "proof_routes_call": "get_revision_proof_routes(array['R526'],'A7C3',false)",
        "claim_contract_call": "get_claim_contracts(array['R526'],false)",
        "full_proof_routes_call": "get_revision_proof_routes(array['R526'],'A7C3',true)"
    },
    {
        "status": {
            "label": "accepted · usable · revision-valid · active · current · proof P538:accepted/valid",
            "headline": "Usable via P538 (fully reconstructible)",
            "blocker_ids": [
            ],
            "object_type": "theorem",
            "revision_id": "R523",
            "current_usable": true,
            "revision_valid": true,
            "lifecycle_status": "active",
            "supporting_proof": {
                "is_valid": true,
                "proof_id": "P538",
                "proof_kind": "full",
                "review_status": "accepted",
                "dependency_complete": true
            },
            "current_revision_id": "R523",
            "is_current_revision": true,
            "canonical_review_status": "accepted"
        },
        "relation": "dependency",
        "revision_id": "R523",
        "resolved_label": "accepted · usable · revision-valid · active · current · proof P538:accepted/valid",
        "proof_routes_call": "get_revision_proof_routes(array['R523'],'A7C3',false)",
        "claim_contract_call": "get_claim_contracts(array['R523'],false)",
        "full_proof_routes_call": "get_revision_proof_routes(array['R523'],'A7C3',true)"
    },
    {
        "status": {
            "label": "accepted · usable · revision-valid · active · current · proof P918:accepted/valid",
            "headline": "Usable via P918 (fully reconstructible)",
            "blocker_ids": [
            ],
            "object_type": "theorem",
            "revision_id": "R844",
            "current_usable": true,
            "revision_valid": true,
            "lifecycle_status": "active",
            "supporting_proof": {
                "is_valid": true,
                "proof_id": "P918",
                "proof_kind": "full",
                "review_status": "accepted",
                "dependency_complete": true
            },
            "current_revision_id": "R844",
            "is_current_revision": true,
            "canonical_review_status": "accepted"
        },
        "relation": "dependency",
        "revision_id": "R844",
        "resolved_label": "accepted · usable · revision-valid · active · current · proof P918:accepted/valid",
        "proof_routes_call": "get_revision_proof_routes(array['R844'],'A7C3',false)",
        "claim_contract_call": "get_claim_contracts(array['R844'],false)",
        "full_proof_routes_call": "get_revision_proof_routes(array['R844'],'A7C3',true)"
    }
]
```