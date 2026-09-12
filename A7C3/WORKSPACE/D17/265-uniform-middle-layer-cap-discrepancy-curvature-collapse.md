# Any two distinct Arm-M cap representatives force explicit Reverse-Ear curvature

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-cap-discrepancy-curvature-collapse`

**Summary:** In R927 Arm M with k>=5, the literal cap layer has no nontrivial R435-quiet discrepancy. Let Q,Q' be any two literal Hamilton k-paths arising as cap rails, with supports X,X'. If X=X' and the literal words differ, accepted R435 applied directly to Q,Q' emits an adjacent reversal, reverse trimer, or proper cycle; if no such output occurs, equal-support monotonicity forces the words to be identical. If X!=X', choose any physical y in X-X'. Then y is exterior to Q'. Arm-M uniformity Hamiltonizes both endpoint-replacement k-supports of Q' by y, while X'+y has size k+1 and is non-Hamiltonian. Accepted R966 therefore forces explicit R435 geometry among Q' and those two endpoint-replacement paths, with y retained as a transition-linked historical label. Consequently every genuine cap-support change is portal-bearing, independently of any recompletion factorization, and after same-support fiber compression the portal-free cap quotient has at most one vertex. Hence no nontrivial portal-free closed walk of terminal cap supports exists. This fulfills the G16 R3 cap-transport extinction target at the portal-free level; the remaining obstruction is consumption of the resulting R435 curvature, not cap transport.

### 1. Cap discrepancy rather than cap transport
Assume accepted R927 alternative (M):

  |V(H)|=2k+1,
  every k-set is Hamiltonian,
  no (k+1)-set is Hamiltonian,

with k>=5 in the live Arm-M range.

Call a CAP REPRESENTATIVE any literal oriented Hamilton tight path

  Q=(q_0,...,q_{k-1})

on a k-support X which occurs as the k-rail of a literal maximum three-forest. The argument below is actually support-intrinsic and does not use the complementary two rails except to retain current provenance.

We prove that two distinct cap representatives can never be related in an R435-quiet world.

### 2. Same-support discrepancy is already Reverse-Ear curvature
Let Q and Q' be two literal cap representatives on the same physical k-support X. Compare Q and Q' by accepted Reverse Ear R435.

If an R435 output occurs, retain its exact adjacent reversal, reverse tight trimer, or proper tight cycle and stop.

Otherwise the Q-vertices must occur along Q' in increasing Q-order. Since Q' has exactly the same support and no exterior vertices, this forces

  Q'=Q

as literal oriented vertex words.

Hence there is no nontrivial same-support cap discrepancy outside explicit R435 curvature. This is precisely the fixed-support fiber collapse needed here; no separate transport theorem is required.

### 3. Different supports force universal cap curvature
Now let Q on X and Q' on X' be cap representatives with

  X != X'.

Choose any physical vertex

  y in X-X'.

Then y is exterior to the literal path Q'. The support X' union {y} has order k+1 and is non-Hamiltonian by Arm M. If q'_0,q'_{k-1} are the endpoints of Q', the two endpoint-replacement supports

  (X'-{q'_0}) union {y},
  (X'-{q'_{k-1}}) union {y}

both have order k and therefore are Hamiltonian by Arm M. Choose actual Hamilton paths L and R on those two supports.

These are exactly the hypotheses of accepted R966, with base path Q' and exterior vertex y. Therefore at least one comparison among

  (Q',L), (Q',R), (L,R)

emits explicit R435 Reverse-Ear geometry:

  adjacent reversed old state,
  reverse tight trimer,
  or vertex-simple proper tight cycle.

Crucially, y was not chosen anonymously. It is a physical vertex of the old cap support X and absent from the new cap support X'. Thus the R966 curvature is tied to the actual cap discrepancy by a retained expelled-label certificate.

No comparison with the old word Q itself is required. The support change already supplies the exterior historical label which activates the universal cap-curvature theorem.

### 4. Complete portal-free collapse of the cap quotient
Combine Sections 2 and 3. For any two literal cap representatives Q,Q':

- if their supports agree and their words differ, R435 fires directly;
- if their supports differ, R966 fires using any y in V(Q)-V(Q');
- if neither fires, the representatives are literally identical.

Therefore, after declaring R435 reversal/reverse-trimer/proper-cycle outputs to be portals, the portal-free cap-representative quotient has at most ONE vertex.

A fortiori the coarser quotient by cap support has at most one portal-free vertex. Consequently:

  THERE IS NO NONTRIVIAL PORTAL-FREE CLOSED WALK
  OF TERMINAL ARM-M CAP SUPPORTS.

This is stronger than acyclicity: outside named Reverse-Ear curvature there is no genuine cap-support edge to orient.

### 5. Relation to the phased Morse program
SV42128 originally reduced a rank-flat completed-anchor dimer exit to a cap-to-cap support transition through the bounded recompletion quotient. SV42888 sharpened that particular exit by applying R966 with the expelled completed anchor.

The present observation removes the dependence on the special exit mechanism. Any cap-to-cap discrepancy whatsoever already carries an expelled old-cap label y, and that label forces R966 curvature at the new cap rail. Thus the cap-support transport problem does not require one-edge factorization, cubical confluence, or a separate support potential in order to eliminate portal-free recurrence.

For the phased Morse program, the remaining rank-flat obstruction is therefore not transport among cap supports. It is CURVATURE CONSUMPTION: given the explicit R435 output forced by the cap discrepancy, show that it closes H or re-enters the Morse lineage below the previous checkpoint.

This section does not claim such curvature consumption. Its exact conclusion is the G16 R3 north star at portal-free level: nontrivial portal-free recurrence among terminal cap supports is impossible. 

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R927"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R966"
    }
]
```