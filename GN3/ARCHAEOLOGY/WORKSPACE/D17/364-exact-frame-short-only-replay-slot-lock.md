# A PAYABLE-FOUR-free same-E short replay is locked to one literal frame slot

**Workspace:** D17
**State:** established
**Key:** `exact-frame-short-only-replay-slot-lock`

**Summary:** Fix E={a,c}, a retained bilateral ancestor packet L=(p,a) tail-signed and R=(c,q) head-signed with their actual sign witnesses, and an exact H-E frame. Let a later same-orientation middle b occur locally in one selected rail with predecessor r and successor s. In the short-only branch, if the combined ancestor/current-incidence packet creates no new PAYABLE-FOUR birth, then every nonexceptional side is forced to replay the old ancestor support exactly: generically r=p and s=q, so the frame literally contains p->b->q. If b coincides with p or q, the exceptional side is still rigid: avoiding PAYABLE-FOUR forces the corresponding selected neighbor to equal the old retained sign witness. Any deviation gives either an immediate literal P4 or a same-oriented two-witness collision on the tested ancestor dimer, which SV76748 parent-compiles to PAYABLE-FOUR. Thus a flat short return is not an abstract R435/R436 species; relative to the retained bilateral packet it occupies one named physical replay slot. With three like-oriented source middles, the sibling-birth theorem leaves at least one unused PAYABLE-FOUR fossil outside that slot. This is a supporting replay-lock lemma; newer P5 fossil results strengthen the subsequent G27 stack analysis.

### 1. Setup
Fix one physical endpoint pair

  E={a,c}.

Retain a genuine bilateral ancestor packet

  L=(p,a) tail-signed,
  R=(c,q) head-signed,

including the actual witnesses that certify those two signs. Let

  H-E=U|V

be an exact two-cover frame. Suppose a later physical middle b has the same outer orientation

  J=(a,b,c) tight,

and that in the selected frame b is internal with local rail neighborhood

  r -> b -> s.

We analyze only the branch in which this replay remains short and produces no fresh source-visible PAYABLE-FOUR certificate before the next payment choice.

### 2. Left replay lock
Apply the bilateral replay calculation on the left ancestor dimer (p,a) and combine it with the selected predecessor incidence at b. If the relevant seam passes, one obtains a literal P4 using the retained ancestor and the current middle/rail incidence, hence PAYABLE-FOUR by the P4 payment compiler.

If the ancestor seam fails, R3 gives (b,a,p) tight. Now use the literal R434 predecessor extraction from the selected frame: exactly one of (r,a,b) and (b,a,r) is tight. If (r,a,b) is tight, it concatenates with J=(a,b,c) to the literal P4 (r,a,b,c), hence PAYABLE-FOUR. Thus in the short-only branch the surviving R434 case is (b,a,r) tight. The tested oriented dimer (b,a) is then tail-signed by both witnesses p and r through (b,a,p) and (b,a,r). Unless r=p, accepted R523 gives a raw same-oriented two-witness collision. SV76748 is a parent compiler, so before payment it converts that collision to P4/P5, direct mass-four, or R407 geometry; SV78086/SV79137 make every such output PAYABLE-FOUR.

Therefore PAYABLE-FOUR avoidance forces the generic left equality

  r=p.

When b=p, the label equality itself is unavailable. The same collision test instead compares the selected predecessor with the retained old sign witness. Avoiding a distinct-witness collision forces the selected predecessor to be exactly that old witness. Thus the exceptional row is not free: it is pinned to the historical witness.

### 3. Right replay lock
The dual argument is literal. If the right ancestor seam passes, there is a P4. If it fails, R3 gives (q,c,b) tight. R434 says exactly one of (b,c,s) and (s,c,b) is tight; the first already concatenates with J to a P4, so short-only survival forces (s,c,b). On the tested oriented dimer (c,b), the failed-seam reversal and the surviving R434 turn are two same-polarity witnesses unless s=q, yielding the same R523/SV76748 PAYABLE-FOUR exit. Hence outside the label-coincidence case b=q, PAYABLE-FOUR avoidance forces

  s=q.

If b=q, avoiding the corresponding distinct-witness collision forces the selected successor to equal the old retained sign witness on the right.

### 4. Literal replay slot
Hence for a generic later middle b not equal to p or q, every PAYABLE-FOUR-free short replay is literally realized in the exact frame as

  p -> b -> q.

A path-forest rail has only one vertex occupying the slot between a fixed ordered predecessor p and fixed ordered successor q. Therefore, relative to one retained bilateral packet and one exact frame, at most one generic physical middle can realize a PAYABLE-FOUR-free short-only replay. The exceptional b=p or b=q cases are even more rigid because one selected neighbor is forced to equal the old retained sign witness.

The important point is physical rather than typological: the surviving short branch is not merely an R435/R436 portal class. It has one named rail location determined by the old ancestors and, in the exceptional rows, by their retained witnesses.

### 5. Interaction with sibling PAYABLE-FOUR births
The three-middle double-birth theorem supplies at least two ancestry-distinct PAYABLE-FOUR births in the common parent before payment. Paying one flatly leaves the other as an unused historical birth fossil. The replay lock shows that any subsequent short-only same-E return can occupy at most one literal replay slot in the retained frame. Thus the normalized surviving stack may be recorded as

  one literal replay slot
  + one paid lineage returned flat to E
  + at least one unused sibling PAYABLE-FOUR fossil.

This is the local mechanism behind the later P5 sibling/fossil firewall results now present in D17. Those newer results strengthen the global G27 analysis; this section is retained because it isolates the exact frame-level reason short replay has only one physical place to hide.

### 6. Scope fence
This section does not by itself prove extinction of the flat stack, and it does not assert that two paid descendants coexist. The unused sibling remains historical ancestry in the R514/SV78086 sense. The conclusion is only the exact-frame replay lock and its one-slot capacity consequence.

R24 and R5 are unused.

## References

```json
[
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
            "label": "accepted · usable · revision-valid · active · current · proof P529:accepted/valid",
            "headline": "Usable via P529 (fully reconstructible)",
            "blocker_ids": [
            ],
            "object_type": "theorem",
            "revision_id": "R514",
            "current_usable": true,
            "revision_valid": true,
            "lifecycle_status": "active",
            "supporting_proof": {
                "is_valid": true,
                "proof_id": "P529",
                "proof_kind": "full",
                "review_status": "accepted",
                "dependency_complete": true
            },
            "current_revision_id": "R514",
            "is_current_revision": true,
            "canonical_review_status": "accepted"
        },
        "relation": "dependency",
        "revision_id": "R514",
        "resolved_label": "accepted · usable · revision-valid · active · current · proof P529:accepted/valid",
        "proof_routes_call": "get_revision_proof_routes(array['R514'],'A7C3',false)",
        "claim_contract_call": "get_claim_contracts(array['R514'],false)",
        "full_proof_routes_call": "get_revision_proof_routes(array['R514'],'A7C3',true)"
    },
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
    }
]
```