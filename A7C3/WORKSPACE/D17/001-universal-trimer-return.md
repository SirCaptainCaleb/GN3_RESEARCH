# Universal outer-pair return machine for any proper tight trimer

**Workspace:** D17
**State:** established
**Key:** `universal-trimer-return`

**Summary:** R358/R359 are the historical endpoint/all-internal interface. Pending revisions R919/R920 with full proof P992 reconstruct the same return machine without R168 and sharpen the all-internal source rails to order at least three, exposing the partner-splice/R542 terminal-collision consumer.

R358 and R359 are the main abstraction and should be the public interface for the return geometry.

**R358, endpoint-return compiler.** Let `J=(a,x,c)` be any proper tight trimer. If an exact two-cover of `H-{a,c}` exposes x at a rail endpoint, insert J at that endpoint. Exactly two new seam turns are uncertified. No spanning two-cover implies one is bad, so its reverse is tight. The result is a literal R173-admissible two-hole mate clause. No capture or contact hypothesis is used.

**R359, universal outer-pair return machine.** Currentize any proper J by prescribed-path completion: `H=J⊔U⊔V`. Then either some outer-pair return exposes x and R358 applies, or every return keeps x internal. In the all-internal branch, deleting x from a return gives a three-cover of `H-J` while U⊔V is a two-cover of the same residue, so R159 yields a balanced pair. Also every direct x-attachment at either end of U,V is bad, hence four reverse terminal shield turns are tight. This exactly abstracts R334/R337/R338 away from first-contact ancestry.

R360 adds an optional all-internal continuation beyond order ten. One source residual rail has order at least four; its shielded terminal dimers form an opposite-signed pair, the central interval refunds to the rail endpoint floor, and x becomes the middle of a new tight turn on that disjoint outer pair. This is the generic same-middle target rotation.

R361 and R370 formalize iteration. If neither a fixed-turn exit nor an endpoint mate clause occurs, repeated all-internal rotations traverse disjoint consecutive outer pairs around one fixed middle. Finiteness yields a decorated directed cycle in the Kneser graph on two-subsets. The cycle is constructive historical data, not a contradiction.

Later theorems R385,R389,R392,R419,R432,R434,R455 provide consumers that remove the need to leave that cycle as the generic terminal residue. Those theorems are cited at the exact steps where used rather than rederived here.



### Noncircular reconstruction repair: R919/R920 and P992

The historical R358/R359 statements are accepted and usable, but their selected proof routes inherit the non-reconstructible R168 rail-floor dependency. Pending exact revisions R919 and R920, with full proposed proof P992, remove that dependency completely. Until independent review accepts them, the old accepted revisions remain the canonical interfaces; this paragraph records the repaired proof for integration and future review.

For endpoint return, no order-three rail floor is needed. If the x-containing return rail is singleton, restoring J itself closes H, so that case is impossible. If the rail is the dimer (x,u), inserting J produces a spanning proposal with exactly one new turn (x,c,u); it must be bad and R3 forces the one-hole mate (u,c,x). For rail order at least three the usual two-hole seam ledger applies. The right-end case is dual. This is R919.

For all-internal return, currentize J by R4 rather than historical R18 and compare the three-cover obtained by deleting internal x from any H-{a,c} return with the source two-cover of H-J. Fully reconstructible R159 gives the component-drop balanced pair. The source rails need no R168 floor: a singleton source rail (y) would make the dimer (x,y) an H-{a,c} endpoint return; a dimer source rail (y,z) is also impossible because the direct attachment (x,y,z) is bad, so R3 makes (z,y,x) tight, again yielding an H-{a,c} endpoint return. Hence every source rail has order at least three. All four direct x-attachments are bad and their reversals give the four terminal shields. This is R920.

The order-three sharpening matters downstream. In either residual-rail concatenation direction, the two possible new seam turns cannot both be tight. Reversing a bad seam gives a second same-polarity witness on one of the already shield-signed reverse terminal dimers. Because both source rails now have order at least three, whichever terminal dimer wins is literally a reverse boundary dimer of a source terminal trimer, so the fully reconstructible R542 short-carrier consumer is available. This is the reconstructible core of the older R455 partner-splice collision. The extra R389/R467 historical interaction fan remains additional ancestry-rich geometry, not a prerequisite for this core collision.

P992 therefore gives a clean dependency path R3 + R4 + R159 -> pending R919/R920, followed if desired by R542 and R428 for a source-localized genuine paid-floor lineage. No R24, R5, R168, R169, R224, capture ancestry, or first-contact theorem is needed for the return normal form itself.

## References

- comparison: R358
- comparison: R359
- related: R919
- related: R920
- dependency: R3
- dependency: R4
- dependency: R159
