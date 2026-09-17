# Every source-labelled current pair-deletion crossing lifts through a dimer forest and descends below its phase-one parent

**Workspace:** D17
**State:** established
**Key:** `forest-phase-current-pair-portal-dimer-lift`

**Summary:** Let F0 be a retained phase-1 maximum-three-forest checkpoint with largest-rail height M. Suppose a certificate-retaining descendant analysis, before any payment-phase transition, produces a CURRENT exact pair-deletion cover T=U|V of H-{p,t} selecting a designated physical crossing state x->y, with the portal ancestry explicitly rooted at F0. Restore the deleted pair as the literal dimer (p,t): G0=(p,t)|U|V is a maximum three-forest, regardless of its own largest-rail height. Boundary antisymmetry on {p,x,y} gives one of (p,x,y) or (y,x,p) as a proper tight trimer K, retaining the portal edge {x,y}, its selected orientation, the deleted pair, and the source ancestry. Currentize K by R4. Compare the new largest rail to the OLD source threshold M, not to G0. If it exceeds M, the new phase-1 rank is already below F0. Otherwise run SV40879 largest-rail growth until closure, first height M+1, or a terminal forest. Height M+1 is strict phase-1 descent below F0; a terminal forest enters SV41376 phase 0, also strictly below F0. Hence every source-labelled current pair-deletion crossing has a finite ancestry-retaining continuation to TWO-COVER or phased rank strictly below its actual phase-1 parent, even when the dimer-restored forest itself has worse phase-1 rank. This is the G26 currentness-to-rank exchange mechanism. It does not apply when the only parent checkpoint is already phase 0.

### 1. Source-labelled current pair-deletion portal
Let H be a hypothetical smallest Strong Level-(1) counterexample. Retain a literal maximum spanning three-forest checkpoint

  F_0=A|B|C                                                (PD.1)

in phase one of the SV41376 hybrid rank. Mark a largest rail and put

  M=max{|A|,|B|,|C|},
  Phi_0=(1,|V(H)|-M).                                      (PD.2)

Suppose a certificate-retaining analysis rooted at F_0, and occurring before any transition into a payment-phase checkpoint, produces distinct physical vertices p,t and a literal exact pair-deletion cover

  T=U|V  of H-{p,t}.                                      (PD.3)

Assume T selects a designated directed physical state

  x -> y,                                                  (PD.4)

with x,y in H-{p,t}. In applications (PD.4) is the CURRENT crossing/component-drop state that constitutes the pair-deletion portal. Retain its exact source meaning: which two comparison components it crosses, the source row or forest that produced the comparison, the deleted pair {p,t}, and its selected direction.

The theorem only needs that this portal packet is source-labelled by F_0. It does not require the pair-deletion cover itself to be a state of the phased process.

### 2. Literal dimer restoration gives a maximum forest
The directed two-vertex word

  D=(p,t)                                                   (PD.5)

is vacuously a tight path. Therefore

  G_0=D|U|V                                                 (PD.6)

is a literal spanning three-cover of H. Since H is a smallest counterexample, accepted R4 gives pc(H)=3, so G_0 is a genuine maximum spanning three-forest.

No favorable comparison between its largest rail and M is assumed. In particular G_0 may initially have a worse phase-1 rank than F_0. This is the point of the threshold argument below.

### 3. The current portal edge plus one deleted vertex forces a proper trimer
Apply boundary antisymmetry R3 to the three distinct physical vertices p,x,y. Exactly one of the complete reversals

  (p,x,y),   (y,x,p)                                      (PD.7)

is tight. Retain the tight one and call it K.

K is vertex-simple. It is proper because the second deleted vertex t is outside V(K). Its birth certificate retains the CURRENT state (PD.4): the physical edge {x,y} is exactly the selected portal edge of T, with its original selected orientation recorded separately. If the tight orientation in (PD.7) uses y->x, no claim is made that y->x was selected in T; it is the R3-forced reverse contact on the same physical portal edge.

Relative to G_0, K meets the dimer rail at p and the T-rail containing x,y. Thus the pair-deletion portal has been PHASE-LIFTED to an explicit proper tight path at a literal maximum-three-forest representative, without R176 payment, floor steering, or completed-anchor recurrence.

### 4. Use the OLD source threshold, not the restored-forest height
Accepted R4 currentizes the proper path K: choose an exact two-cover

  H-V(K)=R|S                                               (PD.8)

and form the literal maximum forest

  G=K|R|S.                                                 (PD.9)

Let L be the order of a largest rail of G and mark one such rail. We now compare L to the OLD source height M from (PD.2).

If

  L>M,                                                     (PD.10)

then the current state G has phase-1 rank

  (1,|V(H)|-L) < (1,|V(H)|-M)=Phi_0.                      (PD.11)

Stop.

Assume henceforth L<=M. Starting from G, run the same greedy marked-largest-rail A-growth continuation used in SV40879/SV52939. Every successful nonclosing SLIDE increases the marked physical descendant by one vertex. Stop at the first of:

1. TWO-COVER: H closes;
2. OLD-THRESHOLD OVERSHOOT: the marked rail first reaches order M+1;
3. TERMINAL: no marked-rail growth remains while its order is at most M.

The process is finite. In case 2 the phase-1 rank is

  (1,|V(H)|-(M+1)) < Phi_0.                               (PD.12)

In case 3, SV40879 births its certificate-bearing balanced pair and SV41376 enters phase 0. Therefore the first payment checkpoint has leading coordinate 0 and hence

  phased-rank < Phi_0                                     (PD.13)

regardless of all trailing payment coordinates.

Thus the possibly unfavorable initial height of the dimer-restored forest G_0 never matters. The old parent threshold M is a finite ceiling: either the lifted portal currentizes above it, grows through it, or terminates below it and drops phase.

### 5. Currentness-to-rank exchange theorem
Combining Sections 1-4 gives:

> SOURCE-LABELLED CURRENT PAIR PORTAL PHASE LIFT. Let a current exact pair-deletion crossing/component-drop portal retain ancestry to a phase-1 maximum-three-forest checkpoint F_0 of largest-rail height M. Then restoring the deleted pair as a dimer and applying one R3 test to the current portal state produces a proper tight trimer K. There is a finite certificate-retaining continuation from K to either a spanning two-cover or a checkpoint of SV41376 phased rank strictly below F_0.

The retained portal ancestry survives the whole construction: F_0, the exact pair-deletion cover T, deleted pair {p,t}, designated current state x->y, its crossing/component-drop meaning, the restored dimer forest, R3 orientation test, and the resulting trimer K.

This is stronger than saying that current pair-deletion geometry exports to maximum-forest dynamics. It gives an explicit exchange rate from currentness to the global phased rank.

### 6. G26 consequence and scope fence
Any ordinary current kernel whose portals are emitted from literal phase-1 source forests can now be consumed root-by-root: currentize the exact pair deletion, restore its deleted pair as a dimer, lift the designated current state through (PD.7), and threshold-normalize against the ACTUAL source height rather than against the restored forest.

The theorem does not solve curvature born only after the lineage has already entered phase 0. If the sole parent checkpoint of the current portal has leading phase coordinate 0, returning to a forest and then applying Sections 3-4 does not by itself prove descent below that phase-0 parent. That remains the genuine completed-anchor curvature problem.

R24 and R5 are not used.

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
    }
]
```