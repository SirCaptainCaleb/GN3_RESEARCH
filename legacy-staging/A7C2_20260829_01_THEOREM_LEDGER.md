> **Generation seal: A7C2-20260829.** This is a canonical Generation-2 package file. During normal initialization, do not substitute older `A5R_...`, `HANDOFF_...`, or `INCREMENTAL_HANDOFF_...` files with similar subject matter. Historical filenames inside archive prose are provenance handles only.

> **Ledger-status note.** This file is the baseline theorem ledger. Any sections here labeled “current proof spine,” “open interfaces,” or “awaiting audit” describe the ledger checkpoint and are superseded by the later canonical status in `A7C2_20260829_10_CONTINUITY.md`.

# Current proof state and theorem bank

> **2026-08-29 fresh-package note.** Current status is controlled by this file together with `A7C2_20260829_10_CONTINUITY.md`, `A7C2_20260829_10_CONTINUITY.md`, and any later append-only `HANDOFF_######.md` files. Handoffs through `HANDOFF_000008.md` are compressed into file `11`; they are intentionally omitted from this package.


> **2026-08-28 clean-packet note.** This is the baseline theorem bank recovered from the current project sources. Its internal “newest” checkpoint predates the later accepted work summarized in `A7C2_20260829_10_CONTINUITY.md`. For current work, read this file together with that supplement and any later independently audited `HANDOFF_######.md` delta. Do not infer current status from chronology inside this file alone.


## Status at this checkpoint

The target is the following conjecture.

> Every finite Strong Level-(1) boundary tournament has a spanning cover by at most two tight paths.

The conjecture remains open. The order-ten case also remains open.

The newest independently accepted layer is Explorer 27's quiet-return seam-alignment package, audited by Puzzler 27. Puzzler 27 then proved four broader or downstream statements; those four statements have not yet received an independent audit and are kept in a separate audit-pending section.

This file is the compact live state. It is organized by mathematical function, not by worker or date. Historical theorem names appear only where they are useful lookup aliases.

## Status words

- **Accepted** means independently audited in the scope stated here.
- **Corrected** means the original statement was too broad and only the repaired form is accepted.
- **Proved, audit pending** means a proof exists in its named handoff but has not received the next independent audit.
- **Historical** means valid in its recorded scope but absent from the shortest live proof spine, or dependent on an older hypothesis such as closed-walk-freeness.
- **Excluded** means false, insufficient, or deliberately not accepted.
- **Open** means neither proved nor disproved.

## Minimal working language

### Basic objects

A **tight turn** is an ordered triple of distinct vertices satisfying the Level-(1) local relation. Reversing all three vertices changes tight to bad and bad to tight. This is **boundary antisymmetry**.

A **state** is an oriented adjacency used by a tight path. A **physical pair** forgets that orientation. A **tight path** is a vertex sequence in which every consecutive triple is tight. A **path cover** is a vertex partition into tight paths. An **exact cover** has the minimum number of components allowed by the relevant minimality theorem.

A selected path in a cover is called a **rail** when its two ends or its interaction with another rail matters.

### Representatives and truth levels

A **representative** is one displayed current path cover. A state or path is **current** only when selected in that representative. It is **graph-intrinsic** when its tightness has been proved independently of whether it is currently selected. It is **historical** when it was selected or created earlier and is retained only as ancestry.

Facts from different representatives may not be conjoined unless an exact common deletion frame, common pair shadow, reversible exchange, or another named theorem transports them.

A set of graph-intrinsic alternatives can coexist while their current realizations occur only in separate **descendants**. This distinction is essential throughout the order-ten work.

### Exchange language

A **candidate** is a proposed set of inserted states. Its **blockers** are the selected states that must be removed to keep a path forest. Raw gain is inserted states minus blockers. A physical tight cycle costs one additional deletion to reopen it, called **cycle debt**. Actual gain equals raw gain minus cycle debt.

A neutral one-for-one or two-for-two exchange has zero net component gain. It may still be valuable because it preserves a marker, seam, witness, role, or ancestry.

### Boundaries, markers, and signs

A **historical seam** is an old carrier state at which a retained path was cut. A **splice** is a proposed or selected turn reconnecting pieces. A historical seam is not automatically the splice coordinate of a final two-path candidate.

A **marker** is a named physical pair, singleton, or small packet whose identity must survive. A marker orientation used during actualization need not equal an orientation selected in an earlier cover.

A **signed support** is a named tight support together with its polarity and a named outside witness certifying that polarity. A **collision** is a prescribed interaction between two signed certificates; its witness order matters. A certified turn may not be cyclically permuted without a fresh test.

**Capture** records that a named endpoint was obtained through a named selected crossing and actualization event. Capture is historical. **Protection** is a stronger theorem-specific continuation in which the captured anchor remains controlled until a target role or first contact. Capture alone does not imply protection.

### Deletion and transfer language

An **exact deletion frame** is a displayed exact cover of the graph after deleting a named set. **Componentwise re-rooting** means that deleting any one component of a displayed minimum three-cover leaves the other two as an exact two-cover of the deletion.

For a fixed deleted vertex, the **transfer graph** has exact two-covers as vertices. An edge moves one physical endpoint from one rail to the other while preserving tightness. Deleting both the fixed root and the moved endpoint leaves the same two residual rails at both ends of the edge; this is the **common pair shadow**. The hierarchy is:

1. all exact covers for the fixed root;
2. one connected transfer component;
3. one transfer edge;
4. one fixed attachment fiber over a named root, moved endpoint, and common pair shadow.

Selected facts do not move upward or sideways in this hierarchy without a theorem.

## Universal foundation

### Boundary antisymmetry — Accepted

For three distinct vertices, an ordered triple is tight exactly when its complete reversal is bad. All local blocker-to-reverse-turn arguments use this law.

### Smallest-counterexample minimality — Accepted

In a smallest counterexample, the full graph has path-cover number three, while every nonempty proper induced subgraph has path-cover number at most two.

For every proper tight path, its complement has an exact two-cover. Restoring that path gives a minimum spanning three-cover containing it literally.

### Gain minus cycle debt — Accepted

For any compatible inserted family, actual path-cover improvement is raw exchange gain minus the number of physical tight-cycle components created. A physical tight cycle is constructive, not contradictory; open one selected state on each cycle.

### Prescribed-path completion — Accepted

Every proper graph-intrinsic tight path can be made one current component of a minimum three-cover by taking an exact two-cover of its complement. This subsumes bare currentization of one state, pair, trimer, or larger proper packet. It does not preserve unrelated current states, roles, or ancestry.

### Universal internal-vertex graft — Accepted

If a retained tight path contains a vertex internally and a current cover contains that vertex while covering everything outside the rest of the path, insert the two missing path states at the vertex. The complete blocker set is exactly the currently selected states incident with the vertex. If its selected incidence degree is zero, one, or two, the gain is respectively two, one, or zero, with no cycle debt. The resulting representative contains the whole retained path and every component of the old cover after removing that vertex.

This is the parent of older fixed-vertex graft and local four-vertex surgery theorems. Specializations remain useful only when they retain a boundary role, chosen side, or ancestry not present in the parent.

## Exact deletion and completion calculus

### Cover-puncture fragmentation identity — Accepted

Delete any proper set from a historical spanning cover and split what remains into maximal historical runs. In an exact cover of the deletion, the number of selected states joining different runs equals the number of run-color blocks in the current rails minus the number of current rails. It is at least the number of historical runs minus the number of current rails. Equality means each historical run occurs in one contiguous block.

This controls how many crossings exist, but not which crossings, their orientations, endpoint roles, or ancestry.

### Intrinsic partition-cover deficit identity — Accepted

For a fixed partition into physical classes, the number of selected transitions between classes equals the sum of the intrinsic path-cover numbers of the classes, minus the number of current cover components, plus a nonnegative representative excess. Equality means each class restriction realizes its own minimum path-cover number.

The excess belongs to one representative and one partition. It is not a global monotone and is not literal exchange credit.

### Puncture crossing parents — Accepted

If a retained path is punctured and its surviving part is nonempty, every exact two-cover of the punctured graph selects a state crossing from the surviving retained side to the rest of the graph unless that surviving side is already one whole component. Repeated use under nested deletions produces crossing ancestry but does not by itself preserve one current crossing through later recompletions.

### Small-deletion exactness — Corrected and accepted

Every nonempty proper induced subgraph obtained by deleting at most four vertices from a smallest counterexample has an exact two-cover unless its complement is itself a tight path used as the third component of a minimum three-cover. The proof uses repaired one-vertex-floor arguments; the earlier cyclic-four-vertex shortcut is not accepted.

### Componentwise re-rooting — Accepted

Deleting any current component from a displayed minimum three-cover leaves the other two components as an exact two-cover of that deletion. This is the standard bridge from one displayed three-cover to several exact deletion frames.

## Sign, pair, and payment bank

### Signed-support actualization — Accepted

A graph-intrinsic signed support may be currentized in a representative suited to its own witness. Its sign certificate persists as graph-intrinsic ancestry after later recompletion, but current selection and endpoint role do not persist unless separately preserved.

### Same-frame capture — Accepted

When a selected crossing is actualized in the same frame as a named signed support, one may record which endpoint was obtained through that crossing. Capture is a historical relation among support, crossing, endpoint, and witness order.

### Opposite-sign payment — Accepted

A compatible opposite-sign pair can pay one unit of a prescribed local deficit when both signs are realized in a common licensed frame. Same-sign data instead forces a collision test. Cross-frame sign data cannot be combined without a transport theorem.

### Fixed-trimer interaction — Accepted

Two pair births through a common fixed trimer anchor cannot both remain quiet. Either their selected representatives interact through a named crossing/floor/return structure or an immediate local finish occurs. Interaction itself is not a contradiction and must be consumed by later machinery.

### Static-core-transparent floor descent — Accepted

A split-free root may descend to a mass-two floor while retaining a specified static graph-intrinsic core and its ancestry. The floor does not automatically retain current endpoint roles, current crossings, or final candidate seams.

## Transfer, root, and return bank

### Boundary-transfer lattice — Accepted

For a fixed deleted root, exact two-covers organize into transfer components under one-endpoint moves. Transfer is local: current data is preserved only along the named edge or within a theorem's stated fiber.

### Common pair shadow — Accepted

Across one transfer edge, deleting the fixed root and moved endpoint leaves the same two residual rails. This exact common deletion frame licenses comparison of the two endpoint attachments.

### Endpoint absorption and exchange squares — Accepted

A suitable endpoint pair can be absorbed into one rail or exchanged across a common shadow to create canonical splice alternatives. The theorem controls the named endpoint/resource data inside its square; it is not a global matching principle.

### Global-longest gap exchanges — Accepted

For a globally longest path, certain internal gaps cannot be crossed or refilled without producing another path of equal length or a direct contradiction to maximality. These exchanges are the source of the order-ten root geometry.

### Order-ten root geometry — Accepted

In an order-ten smallest counterexample, every globally longest tight path has order five. The complement of any such five-path has an exact two-cover on four vertices, so every root is five plus four.

Every exterior-pair deletion from such a root enters an exact five-plus-three or four-plus-four frame. Every five-plus-three root has three exact three-plus-three pair shadows and a canonical family of three-anchor interactions and return routes.

### Pivot folds and marker ancestry — Accepted

Named root pivots can be folded through exact shadows while retaining marker ancestry. The fold controls which historical pair or seam is descended from which root packet, but not necessarily current orientation after later recompletion.

### Root rotation and R15/R16 return — Accepted

In the order-ten five-plus-three geometry, internal returns can be organized through the R15/R16 family. The accepted package forces capture and reduces quiet anchor locations to the two historical global endpoints, with first-closure credit retained for the historical longest-path order-six branch.

### Quiet-return seam alignment — Accepted

The newest accepted return package gives, in the appropriate internal-return frame, a current selected captured crossing together with restoration of one or two historical seams while preserving exact cover structure. The crossing stays selected through the stated restoration sequence.

The theorem does **not** promote historical capture to active protection and does not identify a restored historical seam with the current seam of the final candidate unless separately proved.

## Static finish and assembly boundary

### Static same-candidate finish — Accepted in its corrected scope

A static assembly theorem finishes when the required endpoint-exposed inherited seam, mate/candidate identity, orientation, and component budget are all present in one licensed representative. It cannot consume merely historical seam identity or data assembled from separate representatives.

### One-hole currentization correction — Accepted

The old order-six one-hole theorem was too broad. The surviving transitive matching-block residue is not eliminated by currentization alone; only the cyclic four-vertex quotient is excluded by the fifth-vertex extension theorem.

### Pair-shadow attachment correction — Accepted

The old attachment-side dichotomy was too broad. The accepted result is restricted to one fixed attachment fiber over a named root, moved endpoint, and common pair shadow.

### Packet currentization limitation — Controlling

Currentizing an intrinsic packet does not transport endpoint role, seam identity, capture ancestry, selected mate, or witness orientation unless the currentization theorem explicitly names those roles.

### State-graph cycles versus physical cycles — Controlling

A cycle in a transfer/state/matching/compatibility graph is not a physical tight cycle. Conversely a physical tight cycle is not a contradiction; it incurs cycle debt and can be opened.

## Historical but still useful

The following families are valid in their recorded scopes but are not on the shortest current spine.

- older closed-walk-free reductions predating the Strong formulation;
- local four-vertex graft/surgery statements subsumed by universal internal-vertex graft;
- special same-support collision lemmas now subsumed by signed-support actualization plus exact witness-order testing;
- early endpoint-reminting and packet-currentization lemmas useful mainly as archive lookup handles;
- early transfer-side dichotomies superseded by the fixed-fiber correction;
- early cyclic-four-vertex small-deletion proofs superseded by repaired one-vertex-floor arguments.

## Current proof spine

The live architecture is best read as five layers.

### Layer 1: universal exactness and local calculus

Smallest-counterexample minimality, prescribed-path completion, small-deletion exactness, partition and fragmentation identities, blocker formulas, and gain minus cycle debt make local path production and exact recompletion cheap.

### Layer 2: representative-producing parents

Singleton re-rooting, maximin splice signs, the boundary-transfer lattice, endpoint absorption, transfer edges, common pair shadows, global-longest gap exchanges, and marker folds produce exact representatives with named resources. Each parent has a strict representative fence.

### Layer 3: ancestry and payment

Signed-support actualization, same-frame capture, fixed-trimer interaction, static-core-transparent floor descent, R15/R16 return, and the R28 through R34 lineages retain witness, marker, anchor, carrier, or seam information that generic currentization forgets.

### Layer 4: order-ten convergence

Every root is five plus four; every exterior-pair deletion enters a five-plus-three or four-plus-four frame; every five-plus-three root has three exact three-plus-three shadows, a three-anchor interaction family, and four return routes. Internal returns now force capture, reduce quiet anchors to the two historical global endpoints, and align either one historical seam or both while retaining the selected captured crossing.

### Layer 5: unresolved assembly bridge

The static finish wants a current endpoint-exposed inherited seam in the exact same candidate or an equivalent licensed one-hole frame. The strongest current return representative has current crossing and restored historical seam information. A protected capture continuation has active first-contact control. No accepted theorem preserves both packages into one representative with the final candidate roles.

The bottleneck is therefore not object production. It is minimum-budget synchronization of:

- the right representative;
- the final candidate's seam identity;
- current endpoint role;
- selected crossing or mate identity;
- capture/protection ancestry;
- witness and orientation; and
- component and cycle-debt budget.

## Proved but awaiting independent audit

The following four statements are proved in the Puzzler 27 handoff. They may be studied or audited, but must not be used as accepted infrastructure yet.

### Global-longest endpoint-crossing seam exchange

For a current crossing incident with a historical endpoint of a globally longest path, either current internality creates the accepted same-support sign outputs, or the endpoint is current terminal and the crossing is the unique blocker of the adjacent historical seam. Replacing it by that seam is a one-for-one zero-debt exchange.

This is the parent-level form of Explorer 27's near-return theorem. Its scope fences still distinguish current crossing, graph-intrinsic longest path, historical seam, and later exchange descendant.

### Concentrated three-vertex two-seam restoration

Suppose a current rail contains a named middle dimer of a graph-intrinsic four-path on vertices `u,a,b,v`, and all exterior incidence of the three-vertex class `{u,v,w}` is concentrated at `w`. Then the chord joining `u` and `v` is forced, exactly one chord endpoint is current terminal, and a forced chain through `w` identifies two one-for-one seam restorations. Both old seams can be restored with zero debt while a named exit state survives.

This abstracts Explorer 27's far-return construction.

### Far-restoration marker-cut survival or captured-boundary promotion

After the far two-seam restoration, the old marker-cut state remains graph-intrinsic. Either the whole old marker-cut turn survives current, or the retained selected crossing becomes a current boundary marker-cut at the far endpoint. This is boundary-marker information, not endpoint exposure or active protection.

### Far-restoration profile split and captured-singleton re-root

For a four-plus-four source return, the restored representative has the old four-path, the crossing dimer, and the other four-path. An optional final seam exchange spends the crossing and leaves its exterior endpoint as a singleton; the complement is an exact five-plus-four root and re-enters the eight-splice/root package.

For a five-plus-three source return, the restored representative has the old four-path and an exact three-plus-three two-trimer complement, entering the double-central-anchor interaction family.

These are separate descendants. Capture remains historical; protection and final same-candidate seam identity are not transported.

## Open interfaces

### Global conjecture — Open

No accepted theorem converts the full live architecture into a spanning two-cover in every smallest counterexample.

### Order-ten case — Open

The order-ten root has strong universal geometry, but neither the edge basin nor complete-shielding basin is closed. The quiet-return alignment still stops before the corrected same-candidate static boundary.

### Protected first-contact versus current seam geometry — Open

The return representative can retain a selected captured crossing and one or two restored historical seams. The protected continuation controls the captured endpoint at first contact but does not preserve that current crossing or seam geometry. A bridge synchronizing these resources is missing.

### Consuming an ancestry-bearing mass-two floor — Open

The split-free root and pivot packages can descend to floors retaining substantial historical truth. No accepted theorem turns that retained static core into the exact current endpoint/seam roles needed for assembly.

### Fixed-anchor interaction — Open

Multiple pair births through one or two fixed trimer anchors are provably nonquiet, but interaction itself is not a contradiction or two-cover. A productive consumer beyond existing return and floor machinery is missing.

### Representative-independent progress — Open

Several promising quantities—partition excess, rail gap, transfer distance, marker depth, and return rotation—are representative-relative. No accepted reset-safe global monotone prevents recurrence across arbitrary recompletions.

## Corrections and exclusions that remain controlling

- Test the exact witness order in every same-polarity collision. Do not infer cyclic permutations of certified turns.
- The original order-six one-hole currentization was corrected: the transitive matching-block residue survives; only the cyclic four-vertex quotient is eliminated by the fifth-vertex extension theorem.
- The original pair-shadow attachment-side dichotomy was corrected to one fixed attachment fiber.
- Universal small-deletion exactness through four vertices uses the repaired one-vertex-floor proof, not the discarded cyclic-four-vertex argument.
- R15/R16 retain first-closure credit for the historical longest-path order-six branch.
- Three-Cover Fan Reduction is Strong-safe but consumes nothing on a representative already saturated with the same fan information.
- A state-graph, Hall graph, matching graph, compatibility graph, or transfer graph cycle is not automatically a physical tight cycle.
- A physical tight cycle is not a contradiction.
- Raw gain is not actual gain until cycle debt is paid.
- Endpoint-only relocation and segment reversal are not a complete Hamilton descent system.
- Repeated pair reminting is not progress.
- Packet currentization is not role-bearing synchronization.
- Positive partition excess does not literally pay reverse trimers.
- No current cover may borrow a selected state from another cover merely because both lie in one transfer component.
- Every-extremal-edge continuation and order-ten-transfer-graph-edgelessness remain excluded.

## Certificate map for the newest live layer

| Logical family | Primary certificate |
|---|---|
| Hard-reset universal bank and static finish | `02_ACTIVE_THEOREM_LEMMA_BANK_STRONG_LEVEL1_HARD_RESET_2026-08-25.md` |
| Componentwise re-rooting and short-complement rigidity | `INCREMENTAL_HANDOFF_PUZZLER_13_COMPONENTWISE_REROOT_SHORT_PATH_RIGIDITY_ANCESTOR_EXTERIOR_RESET_2026-08-26.md` |
| Maximin splice faces and boundary-transfer lattice | `INCREMENTAL_HANDOFF_PUZZLER_15_BOTH_GOOD_EXACT_RESIDUE_CANONICAL_SPLICE_TRICHOTOMY_2026-08-26.md` and `INCREMENTAL_HANDOFF_PUZZLER_15_V15_AUDIT_SIGN_CONTROLLED_TRANSFER_LATTICE_CAP_GRID_2026-08-26.md` |
| Endpoint absorption and mate/splice compatibility | `INCREMENTAL_HANDOFF_PUZZLER_16_ENDPOINT_PAIR_ABSORPTION_EXCHANGE_SQUARES_2026-08-26.md` and `INCREMENTAL_HANDOFF_VISIONARY_17_P16_AUDIT_CANONICAL_RESOURCE_COMPATIBILITY_SPINE_RESET_2026-08-26.md` |
| Transfer graph and common-shadow fibers | Puzzler 18 through Puzzler 20 handoffs dated 2026-08-26 |
| Small deletion, longest-path gaps, and order-ten root | Puzzler 21 and Puzzler 22 handoffs dated 2026-08-27 |
| Pivot folds, anchors, shadows, and floors | Puzzler 23 and Puzzler 24 handoffs dated 2026-08-27 |
| Root rotation and same-frame capture | Puzzler 25 and Puzzler 26 handoffs dated 2026-08-27 |
| Accepted quiet-return seam alignment | `INCREMENTAL_HANDOFF_EXPLORER_27_QUIET_RETURN_SEAM_ALIGNMENT_CAPTURED_CROSSING_RETENTION_2026-08-27.md`, audited in Puzzler 27 |
| Audit-pending parent lifts | `INCREMENTAL_HANDOFF_PUZZLER_27_QUIET_RETURN_PARENT_LIFT_MARKER_ROLE_PROFILE_REROOT_2026-08-27.md` |

The historical package used a source manifest and JSONL claim catalog to resolve raw archive identities. That raw catalog is intentionally absent from this clean packet. Use `A7C2_20260829_09_PROVENANCE.md` for the present provenance boundary, and recover an exact historical source externally if a theorem's raw certificate must be rechecked.
