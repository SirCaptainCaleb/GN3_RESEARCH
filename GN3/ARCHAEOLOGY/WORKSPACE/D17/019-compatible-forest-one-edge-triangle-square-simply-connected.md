# The portal-free support-changing one-edge exchange complex is triangle-square simply connected

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-one-edge-triangle-square-simply-connected`

**Summary:** Build a 2-complex whose vertices are literal maximum three-forest representatives, whose edges are reversible support-changing one-edge transfers, whose square 2-cells are the verified SQUARE outcomes of SV38940, and whose triangle 2-cells record serial composition a->b followed by b->c whenever the endpoint is the direct support-changing one-edge transfer a->c. Then every closed one-edge walk has the following reduction: commute its first transfer across all later independent transfers using verified squares until it meets the first transition deleting its new edge or re-adding its deleted edge. A square failure is already augmentation/current trimer/shared current cycle. If the new edge is deleted first, the two transfers either cancel, contract across one serial triangle to the direct transfer, or the direct move is same-support cycle-rebreak geometry and hence a cycle portal. If the deleted edge is re-added first, the fixed-added-edge uniqueness mechanism inside SV38940 forbids the resulting second transfer into the same added edge, except the literal inverse which cancels. Induction therefore contracts every portal-free closed one-edge walk to the empty walk. Thus the one-edge sector is simply connected relative to its explicit portal set. Consequently any history-bearing mark whose transport is coherent around every verified square and serial triangle has globally trivial monodromy on the portal-free one-edge sector; nontrivial long holonomy must localize to one atomic square/triangle curvature defect or pass through a trimer/cycle/non-one-edge portal. Combined with SV39424, the base geometry is a higher-dimensional cubical exchange system with serial triangle relations and explicit cycle-circuit defects, rather than an ordinary matroid or CAT(0) cube graph.

### 1. The triangle-square exchange complex
Work in a hypothetical smallest counterexample H. Consider the graph X whose vertices are LITERAL maximum spanning three-forest representatives and whose edges are reversible SUPPORT-CHANGING one-edge transfers. Thus an oriented edge has the selected-matching form

  M -> M-a+b.                                             (TS.1)

The complete pairwise theorem SV38940 supplies exact SQUARE relations whenever two coinitial support-changing generators commute through a fourth literal maximum forest. Attach one square 2-cell along every such verified four-cycle.

There is a second elementary relation which is already implicit in the reduction of SV39182. Suppose two consecutive transfers are

  M -> M-a+b -> M-a+c.                                   (TS.2)

The endpoint forest differs from the initial forest by exactly the one-edge replacement a->c. If that direct replacement is support-changing, it is itself an edge of X. Attach a SERIAL TRIANGLE 2-cell along

  (a->b),(b->c),(a->c)^{-1}.                             (TS.3)

If instead the direct replacement is same-support, the proof mechanism of SV39182 identifies it as same-rail CYCLE-ROTATE/rebreak geometry; that is a cycle portal rather than a triangle relation in X.

Call the resulting square-and-triangle 2-complex X^{triangle-square}. The claim is not that every local pair supplies a 2-cell: SV38940's AUGMENTATION, CURRENT TRIMER, and SHARED CURRENT CYCLE branches remain explicit exits/portals.

### 2. Global contraction theorem
Let

  F_0,F_1,...,F_m=F_0                                  (TS.4)

be any closed walk in X. Then exactly one of the following occurs during the reduction below:

1. a pairwise comparison produces a spanning TWO-COVER AUGMENTATION;
2. a pairwise comparison produces a CURRENT TRIMER portal;
3. a pairwise comparison or serial compression produces a CURRENT PROPER CYCLE portal;
4. the closed walk is null-homotopic in X^{triangle-square}.

In a hypothetical counterexample the augmentation branch is contradictory, so the substantive dichotomy is PORTAL or CONTRACTION.

### 3. Bubble the first transfer through every independent successor
Write the first transfer as

  tau: a -> b.                                           (TS.5)

Because the final selected matching equals the initial one, the new edge b must eventually disappear and the deleted old edge a must eventually reappear. Choose the first later transition which either deletes b or adds a. Every transition strictly before it does neither.

Consider one such earlier next transfer, say d->c, immediately after tau. From the post-tau forest, compare the inverse generator b->a with d->c. Both are support-changing. Apply SV38940.

If the comparison is AUGMENTATION, TRIMER, or SHARED CYCLE, we have an advertised exit. Otherwise it is a verified SQUARE. Crossing that square replaces the consecutive order

  (a->b) then (d->c)

by

  (d->c) then (a->b),                                   (TS.6)

with the same endpoint literal representative. Thus tau moves one position to the right by an actual square homotopy.

Repeat. Unless a portal appears, tau can be bubbled all the way to its first genuine interaction with {a,b}. No mark, potential, or abstract commutativity is assumed; every swap is one literal SV38940 square.

### 4. First interaction type I: the new edge b is deleted
The first interacting pair now has the form

  a -> b,
  b -> c.                                                (TS.7)

After the two transfers the selected matching is simply M-a+c. The endpoint is already a literal maximum forest, so it certifies the direct one-edge replacement a->c from the state before tau.

If c=a, the two transfers are literal inverses and cancel.

If c!=a and the direct transfer a->c is support-changing, (TS.7) is exactly one SERIAL TRIANGLE and contracts from two edges to one.

If the direct transfer preserves the support partition, the exact proof mechanism in SV39182 applies: one edge has been added between the terminal and source of one old rail and one rim edge has been deleted to rebreak that same directed cycle. This is same-support CYCLE-ROTATE/rebreak geometry, hence an explicit current cycle portal.

Therefore, outside the cycle portal, the first interacting pair strictly shortens the closed walk by cancellation or one serial triangle.

### 5. First interaction type II: the old edge a is re-added
The only other possibility is

  a -> b,
  d -> a.                                                (TS.8)

If d=b, this is the literal inverse and cancels. Suppose d!=b. The two-step endpoint matching is

  M-d+b.                                                 (TS.9)

Hence the endpoint forest itself would certify a second literal one-edge transfer d->b from the state before tau, with the SAME added edge b but a different deleted edge.

Now use the fixed-added-edge uniqueness mechanism proved inside SV38940 Section 2 and reused explicitly in SV39182. For a support-changing transfer with added edge b=u->v, any occupied endpoint copy forces its incident selected edge to be the unique deletion. If both endpoint copies are free, b is a terminal-to-source merge seed; on distinct rails the root-gate analysis again permits at most one support-changing deletion, while same-rail multiplicity is exactly the same-support cycle-rebreak fiber. Since tau is support-changing, the competing transfer d->b with d!=a cannot occur.

Thus (TS.8) is impossible except for immediate inverse cancellation.

### 6. Induction: portal-relative simple connectedness
Start with any nonempty closed walk. Bubble its first edge to its first genuine interaction by Section 3. If a portal/augmentation appears, stop. Otherwise Sections 4-5 replace the walk by a strictly shorter closed walk through square/triangle homotopy and inverse cancellation. Iterate on length.

The process terminates only at the empty walk. Therefore

  EVERY CLOSED SUPPORT-CHANGING ONE-EDGE WALK
  IS TRIANGLE-SQUARE NULL-HOMOTOPIC
  UNLESS THE REDUCTION EXPOSES AUGMENTATION, A CURRENT TRIMER,
  OR A CURRENT PROPER CYCLE.                              (TS.10)

This strengthens the canonical edge-token conclusion of SV39182 from one chosen ancestry coordinate to a theorem about the BASE one-edge exchange complex itself.

### 7. Local curvature controls every one-edge history mark
Let mu be any history-bearing datum transported along reversible support-changing one-edge transfers, with inverse transport on reversed edges. Assume only the following LOCAL flatness conditions:

- transport around every verified SV38940 square is identity;
- transport around every serial triangle (TS.3) is identity.

No assumption is made that mu is state-determined.

Apply the homotopy of Section 6 to any closed portal-free walk. Square moves, triangle moves, and inverse cancellations preserve the total transport of mu by local flatness. The walk contracts to the empty walk, whose transport is identity. Hence

  LOCAL SQUARE/TRIANGLE FLATNESS => GLOBAL ONE-EDGE MONODROMY TRIVIALITY.  (TS.11)

Contrapositively, any nontrivial history-bearing monodromy carried entirely by support-changing one-edge moves has an ATOMIC witness: either some verified square/serial triangle already has nontrivial mark curvature, or the reduction necessarily passes through a trimer/cycle portal. Long one-edge holonomy contains no additional global topological mystery.

### 8. Synthesis with the higher cubical theorem
SV39424 shows that a pairwise-clean star of one-edge generators fills every higher Boolean cube until the first missing face, which is one unique all-generator physical cycle portal. The present theorem handles arbitrary SERIAL compositions and closed walks by adding the triangle relation.

Together they give the following bespoke exchange structure for the one-edge sector:

- independent generators span genuine higher cubes;
- serial replacements satisfy exact composition triangles;
- every portal-free closed base walk contracts through these cells;
- every minimal absent higher cube is labelled by one physical cycle-circuit;
- any history-bearing monodromy is therefore either elementary 2-cell curvature or portal transport.

This is stronger and more accurate than an ordinary matroid/median/CAT(0)-cube analogy. It is a portal-relative simply connected CUBICAL-TRIANGULAR EXCHANGE COMPLEX with explicit physical cycle circuits.

The remaining G15 problem is correspondingly concentrated: understand mark curvature on the elementary cells for the ACTUAL ancestry carried by Arm-M/R435 transports, and understand what trimer/cycle and non-one-edge component-recompletion portals do to that ancestry. No claim is made that those portal transports are already trivial.
