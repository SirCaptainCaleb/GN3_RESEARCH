# Largest-rail descent and fixed-turn payment splice to one global quiet-lineage Morse potential

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-phased-global-morse-potential`

**Summary:** Compose the repaired largest-rail Morse theorem SV40879 with accepted fixed-turn lex descent R172. Start from any literal maximum three-forest, mark a largest rail A, and greedily perform only inward endpoint SLIDEs that grow A; d=n-|A| strictly decreases. At the first nonclosing terminal forest F*=A*|B*|C*, choose and retain any proper turn J of A*. The terminal wall produces a genuine certificate-bearing balanced pair before any floor steering: in the |A*|=3 branch the rooted component-drop construction gives a singleton+dimer pair of mass 3, while for |A*|>=4 the opposite boundary dimers give a mass-4 pair. Enter the R172 fixed-J lineage immediately. Define the hybrid rank Phi=(1,d) during the forest phase and Phi=(0,epsilon_J,M-2,delta_J) during the pair-lineage phase, ordered lexicographically with 1>0. Every forest SLIDE lowers d; the transition into the paid pair lineage lowers the phase coordinate; every designated quiet nonclosing nonexit R172 macro strictly lowers (epsilon_J,M-2,delta_J). Therefore every maximum-three-forest state admits a chosen finite continuation to either a spanning two-cover or one of the explicit productive historical pair/contact exits recognized by R172. No quiet recurrence or anonymous remint can survive this continuation. This is a genuine global well-founded potential on the hybrid forest/ancestry state space. It does not yet orient arbitrary behavior after an explicit productive exit, so extinction reduces to consuming those named exit portals and showing they re-enter below the previous Phi level or close.

### 1. Input: the repaired forest gradient
Retain the established largest-rail theorem SV40879. From any literal maximum spanning three-forest

  F=A|B|C

choose A of maximum order and keep its growing physical descendant marked. Repeatedly take any inward endpoint SLIDE supplied by SV22098 which transfers one endpoint of B or C into A. With

  d(F,A)=|V(H)|-|A|,

every such literal maximum-forest move satisfies

  d -> d-1.                                               (PG.1)

Hence this forest phase is finite. If a move merges away a component, H has a spanning two-cover. Otherwise the process reaches a terminal literal maximum forest

  F*=A*|B*|C*                                             (PG.2)

with no inward endpoint SLIDE into A*.

SV40879 proves |A*|>=3 and, crucially, does not stop at a raw signed wall. It gives a genuine certificate-bearing balanced-pair birth:

- if |A*|=3, deleting the middle vertex of A* gives the rooted four-cover versus exact-two-cover component-drop construction and births a singleton+dimer opposite-sign pair of total mass 3;
- if |A*|>=4, the reverse initial and reverse terminal dimers of A* are disjoint opposite-polarity signed supports, giving a certified balanced pair of total mass 4.

Thus every nonclosing terminal forest enters actual signed-payment ancestry, not a free formal pair.

### 2. Freeze one graph-intrinsic turn before paying
Because |A*|>=3, choose once and for all any consecutive proper turn

  J=(a,b,c)                                               (PG.3)

of the literal tight path A*. The path A* and hence J are graph-intrinsic and remain valid historical data even when later representatives change.

Make this choice BEFORE starting the pair-payment continuation from the terminal balanced-pair birth. Retain J as the fixed lineage coordinate. The terminal pair from Section 1 has mass M equal to 3 or 4 and carries the exact physical birth ledger required by the accepted payment machinery. Therefore the hypotheses of accepted R172 apply to the chosen J-lineage.

Write

  A_J subseteq {a,c}

for the outer endpoints already completed by quiet selected-incidence return episodes, put

  epsilon_J = 2-|A_J|,                                   (PG.4)

let M be the current active balanced-pair mass, and at mass two let S be the current singleton floor pair and define

  delta_J = 2-|S intersect {a,c}|.                        (PG.5)

For M>2 use the R172 convention delta_J=0. The accepted fixed-turn rank is

  Psi_J=(epsilon_J, M-2, delta_J).                        (PG.6)

R172 proves that every designated quiet, nonclosing, nonexit macro retaining J strictly decreases Psi_J in ordinary lexicographic order.

### 3. One phased global potential
Define a hybrid marked-state rank Phi on the chosen continuation by

  Phi = (1, d(F,A))                                       (PG.7)

while the state is in the largest-rail forest phase, and

  Phi = (0, epsilon_J, M-2, delta_J)                      (PG.8)

once the terminal certified pair birth has occurred and the fixed-J payment lineage has begun.

Order these tuples lexicographically, taking the phase coordinate first and 1>0. Missing trailing coordinates are irrelevant once the phase differs.

There are exactly three kinds of quiet nonclosing transition on the chosen continuation.

1. FOREST SLIDE. Equation (PG.1) leaves phase 1 fixed and strictly lowers d.
2. TERMINAL PAIR ENTRY. The forest phase ends at F* and the certified mass-3 or mass-4 pair lineage begins. The first coordinate drops 1->0, so Phi strictly decreases regardless of the numerical pair coordinates.
3. FIXED-TURN PAYMENT MACRO. Phase 0 stays fixed and accepted R172 strictly lowers Psi_J.

Therefore every quiet, nonclosing, nonexit step strictly lowers Phi.             (PG.9)

The target order is well founded because it is a finite lexicographic product of well-founded nonnegative-integer orders preceded by one binary phase coordinate.

### 4. Consequence: quiet global recurrence is impossible
Starting from ANY literal maximum-three-forest state, choose the continuation of Sections 1-3. It cannot contain an infinite quiet recurrence, cannot return quietly to an earlier marked hybrid state, and cannot support anonymous pair remint as a source of unbounded history.

The continuation terminates in one of exactly two parent outcomes:

  TWO-COVER,

or an EXPLICIT PRODUCTIVE EXIT of the accepted R172 fixed-turn lineage.          (PG.10)

Such an exit is not anonymous failure of the potential. It is one of the named historical pair/contact outputs appearing in the R172/R434 machinery: anchor contact or strict tight-path growth, proper-cycle output, reverse-contact/reversal geometry, strict signed-side descent outside the designated quiet macro, or another accepted explicit pair/contact interaction.

Thus the global maximum-forest Morse problem has been compressed from arbitrary recurrence to portal consumption: quiet motion is well founded, and every obstruction to continued descent is a named productive historical exit.

### 5. Relation to the circular-sheet cube and recompletion contraction
SV40405 independently shows that a fixed ancestry-oriented circular-word SLIDE sheet is either portal-bearing or an explicit cube Q_3, hence horizontally contractible. SV40898 shows that arbitrary component recompletion factors through at most two one-edge transfers unless it exposes a bounded C4/C6 support-incidence nucleus, a repeated-crossing nucleus, R435 cell geometry, or a current mixed-seam trimer.

The phased rank is compatible with those structural reductions: it does not try to orient every reversible edge in an undirected SLIDE cube. Instead it chooses one monotone largest-rail direction until the first signed critical state, then switches to the history-bearing R172 coordinates. In this sense the phase change is the discrete-Morse critical transition that the square/cube topology alone cannot see.

### 6. Exact remaining obligation
This theorem is NOT yet full monodromy extinction. R172 itself is lineage-relative and deliberately stops at explicit productive exits. Therefore Phi is not claimed to decrease after an arbitrary exit, after abandonment of J, or under an unrelated representative reset.

The remaining parent obligation is now precise:

  PRODUCTIVE-EXIT REENTRY:
  every explicit R172 exit born from the terminal largest-rail lineage either closes H or can be currentized/re-entered into the forest/pair state space at a mark whose phased rank is strictly below the pre-exit checkpoint.       (PG.11)

Proving (PG.11), possibly using the bounded overlap nuclei of SV40898 and the portal-relative simple-connectedness work, would upgrade the present quiet-lineage potential to full global monodromy extinction. Until then, (PG.7)-(PG.10) give the requested genuine global well-founded quantity on the chosen forest/ancestry continuation and isolate all curvature in named exit portals rather than local seam taxonomies.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R172"
    }
]
```