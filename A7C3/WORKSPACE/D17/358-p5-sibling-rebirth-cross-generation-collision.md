# The unused P5 sibling and its flat-return rebirth force a P4 or R523 collision

**Workspace:** D17
**State:** established
**Key:** `p5-sibling-rebirth-cross-generation-collision`

**Summary:** In the flat branch of SV81686 retain the unused source sibling B_R with tail dimer (a,y) and head dimer (c,z) witnessed by y, and the first post-return rebirth B_new with the same tail dimer and head dimer (c,t) witnessed by w, where t,w are distinct and neither equals y. If t=z, the source and returned head certificates give an immediate two-head R523 collision on (c,z) with witnesses y,w. If t!=z, test (y,c,t). Tightness already gives the P4 (a,y,c,t) and also a collision on (c,t) with witnesses y,w. If bad, R3 gives (t,c,y); then test (t,c,z). Tightness gives a collision on (c,z) with witnesses y,t. If bad, R3 gives (z,c,t); unless w=z this collides with the returned head certificate on (c,t), while if w=z the retained source turn (a,z,c) concatenates to the P4 (a,z,c,t). Thus the unused sibling and the first flat-return rebirth can never be independent quiet copies: before any second payment they force a literal P4 or a raw same-oriented dimer collision, hence a PAYABLE-FOUR packet through SV76748/SV78086/SV79137 with explicit post-return ancestry. This is a nonreplay theorem for one sibling/rebirth stack, though it still permits another flat payment return.


### 1. The exact sibling/rebirth packet
Retain the rank-flat branch of SV81686 at one physical endpoint pair

  E={a,c}.

The source three-spoke P5 is

  K=(x,a,y,c,z),                                          (CG.1)

so in particular

  (a,y,c), (y,c,z), (a,z,c)                              (CG.2)

are tight. The unused source sibling is the PAYABLE-FOUR birth

  B_R : T=(a,y) tail-signed by c,
        H_0=(c,z) head-signed by y.                       (CG.3)

After paying the other sibling, returning rank-flat to the same E, reusing the source H-E frame, and taking the controlled c-successor incidence of SV81686, the first post-return episode gives a second PAYABLE-FOUR birth

  B_new : T=(a,y) tail-signed by c,
          H_1=(c,t) head-signed by w,                     (CG.4)

where the R434 extraction gives

  t != y,  w != y,  t != w.                              (CG.5)

The two births are historical certificates; no paid descendants are asserted simultaneously current. Their common tail dimer is literal, and the source and returned head certificates are the exact ordered turns

  (y,c,z), (w,c,t) tight.                                 (CG.6)

We show that B_R and B_new cannot form two quiet independent birth epochs.

### 2. Exact head-support replay is already a collision
Suppose first

  t=z.                                                    (CG.7)

Then (CG.6) gives two HEAD certificates on the same tested oriented dimer

  (c,z)

with distinct witnesses y and w, because w!=y. Accepted R523 therefore gives a same-oriented two-head collision on (c,z).

Thus exact physical support replay is not quiet. The witness change proved in SV81686 is already the missing collision certificate.

### 3. Distinct returned head support: first seam test
Assume now

  t!=z.                                                   (CG.8)

Test the ordered turn

  (y,c,t).                                                (CG.9)

If (CG.9) is tight, then the source turn (a,y,c) concatenates with it to the literal vertex-simple P4

  (a,y,c,t).                                              (CG.10)

Moreover, because (w,c,t) is also tight and w!=y, the same branch simultaneously gives an R523 two-head collision on the tested dimer (c,t). Either certificate is already enough for the later PAYABLE-FOUR conclusion.

Hence retain only the bad-seam branch. By R3,

  (t,c,y) tight.                                          (CG.11)

This is the exact adjacent reversal of the source selected state y->c inside K, but we do not stop at that short portal.

### 4. Second seam test kills the reversal-only residue
Test

  (t,c,z).                                                (CG.12)

If (CG.12) is tight, then the source certificate (y,c,z) and (CG.12) are two HEAD certificates on the same tested dimer (c,z), with distinct witnesses y,t by (CG.5). Accepted R523 gives a same-oriented collision.

Suppose instead that (CG.12) is bad. By R3,

  (z,c,t) tight.                                          (CG.13)

Compare this with the returned head certificate (w,c,t).

If w!=z, then (CG.13) and (w,c,t) are two HEAD certificates on the same tested dimer (c,t), with distinct witnesses z,w. Again R523 gives a collision.

If w=z, then (CG.13) is the returned head certificate itself. But z is one of the retained source three-spoke middles, so (a,z,c) is tight by (CG.2). Therefore

  (a,z,c,t)                                               (CG.14)

is a literal vertex-simple P4. This exhausts the last exceptional equality.

### 5. Cross-generation nonreplay theorem
Combining Sections 2--4 gives:

> In the flat-return stack produced by SV81686, the unused source sibling B_R and the first post-return PAYABLE-FOUR rebirth B_new force, before any second payment is chosen, either a literal proper P4 or a raw R523 same-oriented dimer collision carrying both source and post-return ancestry.

The collision alternative parent-compiles through SV76748 to P4/P5, a direct opposite-sign mass-four pair, or R407. The first three are PAYABLE-FOUR by SV78086 and R407 is PAYABLE-FOUR by SV79137. Hence every branch re-enters the PAYABLE-FOUR interface with a certificate whose source ledger explicitly contains the cross-generation interaction between the fossil and the returned incidence.

This is stronger than merely saying that B_new itself is payable. The new birth cannot be an ancestry-neutral replay of B_R: exact support replay gives an immediate witness collision, while distinct support forces a P4 or a collision after at most two R3 tests.

### 6. Relation to R441 and the G27 stack
Accepted R441 says two historical balanced-pair births with nontrivial supports cannot remain quiet: overlap is consumed by R436 and disjoint generations by R440. The present calculation is a sharper specialization to the G27 sibling stack. Because B_R and B_new intentionally share the fossil tail dimer, the generic R436 overlap route could otherwise replay a known source trimer. Sections 2--4 spend the extra P5/source-middle provenance and remove exactly that replay ambiguity, upgrading the overlap to P4 or R523 collision.

Thus after one flat return the stack is not merely longer: it has acquired a concrete nonreplaying cross-generation interaction certificate.

### 7. Scope fence
This does not yet prove global portal-stack extinction. The resulting PAYABLE-FOUR packet may itself be paid and may again return flat. No numerical rank below Psi_E=(0,0,0) is claimed. The theorem supplies the G27 success ingredient that was previously missing: one unused sibling plus one flat-return rebirth cannot replay quietly; it necessarily produces P4/collision geometry with retained source-versus-return ancestry.

R24 and R5 are unused.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    }
]
```