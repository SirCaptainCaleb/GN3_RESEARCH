# The full maximum-three-forest exchange groupoid has a portal-relative presentation

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-full-recompletion-portal-presentation`

**Summary:** Fixed-support ambiguity also disappears outside R435: two different Hamilton words on one common support force an R435 reversal/reverse-trimer/proper-cycle output, since otherwise Reverse Ear makes the second word encounter all vertices in the first word order and hence the words are identical. Therefore every portal-free fixed-support FIBER-REORDER is literally the identity representative. For support-changing motion, every recompletion outside the explicit SV40898 nuclei/portals factors through at most two reversible one-edge transfers. Adjoin comparison 2-cells between safe recompletion edges and those factor paths. SV39912 then contracts every resulting closed one-edge walk through verified squares and serial triangles unless augmentation, a current trimer, or a current proper cycle appears. For arbitrary history transport, any failure of coherence is atomic curvature on one square, triangle, or safe-recompletion comparison cell. Thus any nontrivial global holonomy has an atomic witness among regular-cell curvature or the finite portal alphabet: R435 reversal, current trimer/cycle, C4/C6 support-incidence nucleus, or repeated-crossing nucleus. Generic recompletion and same-support reorder contribute no hidden large-scale portal-free topology.


### 1. The right object is a transport groupoid, not a matroid
Let H be a hypothetical smallest counterexample and let \\mathcal F be the set of LITERAL maximum spanning three-forest representatives. A representative remembers its three actual oriented tight path words and selected directed states.

There are three qualitatively different kinds of base motion already isolated in the current development.

1. **Literal-retention fiber reorder.** If F,G have the same unordered three supports, SV35882 allows the exact FIBER-REORDER jump F<->G whenever a retained mark is literally present with the same certified meaning at both ends. Such a jump has no hidden mark transport: it is exactly literal retention.
2. **Support-changing one-edge transfer.** These are the reversible edges of the triangle-square complex of SV39912.
3. **Arbitrary support-changing recompletion.** Compare any two literal maximum forests F,G with distinct support partitions by SV40898.

The earlier failure of ordinary matroid, delta-matroid, median, and CAT(0)-cube models in SV39424 shows that an abstract feasible-set system forgets the essential datum. The missing datum is not another exchange axiom. It is **transport curvature attached to relations, plus explicit physical portals where a relation is unavailable**.

We formalize that statement without assuming the transported datum is abelian or state-determined.


### 1A. Outside R435, every fixed-support fiber is literally a point
The literal-retention language above can be sharpened. Suppose

  F=P_1|P_2|P_3,
  G=Q_1|Q_2|Q_3

have the same unordered support partition, and match the components so that

  V(P_i)=V(Q_i)=X_i

for i=1,2,3. Fix one i and compare the two actual Hamilton tight paths P_i and Q_i by accepted Reverse Ear R435.

Write

  P_i=(v_0,...,v_t).

R435 proves, by taking consecutive reverse-order contacts and testing the two ear seams, that any decrease in P_i-index along Q_i gives one of exactly three graph-intrinsic outputs: the adjacent reversal of an old P_i-state, a reverse tight trimer, or a proper tight cycle. If none occurs, all P_i-contacts along Q_i occur in increasing P_i-order.

But Q_i is Hamilton on the SAME support X_i. Every vertex v_0,...,v_t occurs exactly once on Q_i. The only increasing permutation of the complete index set {0,...,t} is

  0,1,...,t.

Hence

  Q_i=P_i                                                   (PR.0)

as a literal oriented word. Apply this independently to all three supports. We obtain the fixed-support rigidity dichotomy

  F=G as the same literal representative,
  OR an explicit R435 reversal / reverse-trimer / proper-cycle portal.  (PR.0a)

Therefore a portal-free FIBER-REORDER jump is not merely identity transport of a retained mark: its two endpoint representatives are literally equal. It may be deleted from a literal portal-free walk without breaking composability. This is the missing base-space justification needed below.

Long same-support Hamilton-word motion is thus not a separate source of global topology. Any nontrivial fixed-support change is already R435 curvature.

### 2. Safe recompletions have relation length at most two

Call a support-changing recompletion edge

  e : F -> G

**safe** if the comparison in SV40898 lands in its ONE-EDGE FACTORIZATION outcome, rather than a C4/C6 support-incidence nucleus, repeated-crossing nucleus, R435 cell portal, or mixed-seam trimer.

The proof of SV40898 is literal. After synchronizing every contiguous incidence-cell word, the old/new seam union is a forest. If there are four nonempty cells, F and G differ by one old seam o and one new seam n, so e has a one-edge factor path

  p_e : F -> G.

If there are five cells, write old seams o_1,o_2 and new seams n_1,n_2. Unless copy competition or the unique genuinely mixed turn gives the advertised current trimer, the mixed selected set consisting of the common cell interiors together with {o_2,n_1} is itself a literal maximum three-forest F_*. Hence

  p_e : F -> F_* -> G                                      (PR.1)

is a two-edge path of reversible support-changing one-edge transfers.

Thus every safe arbitrary recompletion comes with a base relation

  e  ~  p_e,       |p_e| <= 2.                              (PR.2)

No ancestry transport has yet been asserted across (PR.2).

### 3. Recompletion curvature is the exact missing transport datum
Let \\mu be any history-bearing datum whose legal transitions act by invertible transport maps. This may be nonabelian: think of each path as carrying an isomorphism between fibers of possible marks.

For a safe recompletion e:F->G and one chosen literal factorization p_e from (PR.1)-(PR.2), define its **recompletion comparison curvature** to be the discrepancy between the certified transport along e and the composite certified transport along p_e, whenever both transports are licensed:

  K(e,p_e) = T(e) T(p_e)^{-1}.                              (PR.3)

Equation (PR.3) is notation for an automorphism at the appropriate endpoint; no commutativity is assumed. If the source theorem does not license transporting \\mu along one side, no flatness claim is made and that transition remains outside the safe lifted subcategory.

This is precisely the point that a base factorization alone cannot erase history. The factorization reduces every possible failure of history-coherence to one bounded relation cell. A long arbitrary recompletion carries no further primitive datum beyond K(e,p_e).

The one-edge sector has the analogous atomic curvatures: discrepancies around an actual SV38940 square and around an actual serial triangle of SV39912.

### 4. Normalize any portal-free recompletion loop to a one-edge loop
Consider a closed lifted walk W based at a literal forest F_0, using only:

- literal-retention FIBER-REORDER jumps of SV35882;
- support-changing one-edge transfers;
- safe support-changing recompletion edges e for which both sides of (PR.2) carry the datum under consideration.

Assume first that every recompletion comparison cell is flat for \\mu:

  K(e,p_e)=1.                                               (PR.4)

Replace each safe recompletion edge e in W by its chosen path p_e. Because (PR.4) identifies the two transports, this changes neither endpoints nor total transported mark. Every fixed-support jump may be collapsed at the mark level because its defining hypothesis is literal retention of the same certified mark at both ends.

After finitely many replacements, W becomes a closed walk W_1 consisting entirely of reversible support-changing one-edge transfers, with exactly the same total holonomy as W.

Now apply the literal contraction algorithm of SV39912 to W_1. Bubble its first transfer through every independent successor using verified SV38940 squares. At the first genuine interaction, either the pair cancels, contracts across a serial triangle, or the reduction exposes augmentation, a current trimer, or a current proper cycle. Repeating strictly shortens the one-edge word.

Therefore, if no one-edge portal is exposed and square/triangle transport is flat, W_1 contracts to the empty walk without changing transported data. Hence W has trivial holonomy.

We have proved the nonabelian implication

  SAFE RECOMPLETION FLATNESS
  + ONE-EDGE SQUARE/TRIANGLE FLATNESS
  + NO PORTAL
  => TRIVIAL GLOBAL RECOMPLETION HOLONOMY.                  (PR.5)

### 5. Exact portal presentation theorem
Take the contrapositive of Section 4, but retain the physical failure modes rather than calling them generic nonflatness.

Any nontrivial marked holonomy in the full maximum-three-forest recompletion calculus has an atomic witness of at least one of the following kinds.

**CELL CURVATURE**

- nontrivial transport around one verified one-edge exchange square;
- nontrivial transport around one serial-composition triangle;
- nontrivial comparison curvature K(e,p_e) for one safe arbitrary recompletion and its literal factor path of length at most two.

**PHYSICAL PORTAL**

- a spanning two-cover augmentation, which closes the counterexample branch;
- a current proper tight trimer;
- a current proper tight cycle;
- a C4 or C6 support-incidence nucleus from SV40898;
- a repeated-crossing seam nucleus from SV40898;
- an R435 same-cell reversal/reverse-contact cell (its trimer/cycle alternatives are already in the preceding two portal classes).

The mixed-seam failure of SV40898 is already a current-trimer portal, so it adds no new class. Likewise higher missing cube faces from SV39424 are current proper-cycle portals, not a new large-scale species.

Thus arbitrary component recompletion does not create an unbounded family of topological generators. Modulo literal-retention support fibers, the full representative calculus has a **portal-relative presentation** whose regular relations have size at most three edges: square, serial triangle, or recompletion-versus-at-most-two-one-edge factorization. The only unreduced generators are the explicit physical portals above.

### 6. Universal factorization of history transport
The theorem is stronger than an H_1 statement because no abelianization was used. Let T be any transport functor into any groupoid of marks. On the subcalculus where all regular relation cells are T-flat, every closed transport word is trivial unless its normalization crosses a physical portal.

Equivalently, every history representation of the full recompletion calculus factors through the quotient obtained by collapsing:

- literal-retention fixed-support fibers;
- verified one-edge squares;
- serial triangles;
- safe recompletion comparison cells.

The quotient has no regular global loops left. Its surviving letters are exactly physical portal events. In this sense the maximum-three-forest state space is a

  PORTAL-COMPLETED CUBICAL-TRIANGULAR EXCHANGE GROUPOID,   (PR.6)

not a defective matroid waiting for one more basis-exchange axiom.

### 7. Why this changes the global moonshot
SV39912 had already removed long topology from the one-edge sector. SV40898 had already removed unbounded combinatorial type from a single arbitrary recompletion. The present synthesis removes the remaining possibility that *alternating many generic recompletions* could rebuild a new global holonomy invisible in either theorem separately.

It cannot. Any such loop normalizes relation-by-relation to the one-edge core. If its mark changes, the first irreducible cause is already visible on one bounded comparison cell or at one explicit physical portal.

Hence the global monodromy problem can be attacked locally without reverting to local shape taxonomy: one must prove transport-flatness for the actual Arm-M/R435 ancestry on the three regular cell types, and consume the finite portal alphabet. There is no additional large-scale recompletion topology waiting beyond those tasks.

This also interfaces directly with the phased Morse program. A productive-exit reentry which changes representatives arbitrarily can only defeat global rank through (i) one atomic recompletion-curvature cell, or (ii) one of the named physical portals. Generic reentry itself is not a new source of recurrence.

No claim is made that the actual project ancestry is already flat on every comparison cell, or that the C4/C6 and repeated-crossing nuclei are already consumed. Those are now the exact missing data rather than symptoms of an unknown global exchange structure.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R435"
    }
]
```