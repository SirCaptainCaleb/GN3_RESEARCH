# Arm-M cap reentry has no flat support-transport sector: every expelled anchor forces R966 curvature

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-cap-reentry-universal-r966-curvature`

**Summary:** In R927 Arm M, every literal Hamilton k-path Q=(q0,...,q_{k-1}) and every exterior vertex y are automatically R966-active: Q+y is a forbidden (k+1)-support, while the two endpoint-replacement supports Q-q0+y and Q-q_{k-1}+y are k-sets and hence admit actual Hamilton paths. Accepted R966 therefore forces an explicit R435 output among Q and those two replacement paths. Apply this to the only rank-flat R434/R436 dimer reentry isolated in SV42128. If the old terminal rail had order below k, SV42128 already gives strict largest-rail improvement. If it had order k, currentizing the exit gives a new literal k-rail U and the completed old anchor e lies in the exit dimer, hence e is exterior to U. Taking Q=U and y=e, the universal cap-curvature observation forces an explicit adjacent reversal, reverse trimer, or proper tight cycle. Thus the apparent cap-to-cap flat support transport is never a genuinely flat Morse sector: every completed-anchor dimer exit is either strict primary height improvement or immediately accompanied by named R435 curvature. This does not yet consume the R435 portal, but it removes anonymous cap-support recurrence from PRODUCTIVE-EXIT REENTRY.

### 1. Universal cap curvature from one exterior label
Assume accepted R927 alternative (M):

  |V(H)|=2k+1,
  every k-set is Hamiltonian,
  no (k+1)-set is Hamiltonian.                            (UC.1)

Let

  Q=(q_0,q_1,...,q_{k-1})                               (UC.2)

be ANY literal Hamilton tight path on a k-set X, and let y be ANY vertex outside X. In the live Arm-M range k>=5, so Q has order at least three.

The support X union {y} has order k+1 and therefore is non-Hamiltonian by (UC.1). On the other hand the two endpoint-replacement supports

  X_L=(X-{q_0}) union {y},
  X_R=(X-{q_{k-1}}) union {y}                            (UC.3)

are k-sets. Again by (UC.1), choose actual Hamilton tight paths

  L on X_L,
  R on X_R.                                               (UC.4)

These are exactly the physical hypotheses of accepted R966 with base path Q and exterior vertex y. Its proof compares Q with L and R using R435. If Q-L were quiet, the inherited Q-vertices of L would have to occur in increasing Q-order and non-Hamiltonicity of X+y would force y into one of the first two slots of L. Dually Q-R quietness forces y into one of the last two slots of R. The four resulting near-end insertion forms cannot also be L-R quiet: except for the three tiny overlap patterns, a common Q-vertex and y occur in reverse order and R435 fires; in each tiny overlap pattern the certified turns of L and R literally concatenate to a Hamilton path of X+y, forbidden by (UC.1).

Therefore, for EVERY pair (Q,y) as above, at least one of

  (Q,L), (Q,R), (L,R)                                    (UC.5)

has an explicit R435 Reverse-Ear output:

  an adjacent reversed old state,
  a reverse tight trimer at a seam,
  or a vertex-simple proper tight cycle.                  (UC.6)

Call this the UNIVERSAL CAP-CURVATURE property. Notice that this is stronger than saying some cap support somewhere is portal-bearing: every oriented Hamilton realization Q of every k-support and every exterior physical label y force a named Reverse-Ear event after choosing the two guaranteed endpoint-replacement Hamilton paths. No representative synchronization across different y is asserted.

### 2. Apply curvature to the completed-anchor flat dimer exit
Now retain the phased Morse lineage of SV41376 and the flat completed-anchor exit analyzed in SV42128. Thus a completed fixed-turn outer anchor e lies on the old terminal marked rail A*, and the productive R434/R436 event is only a new tight dimer D through e. Accepted R4 currentizes D as

  F_D=D|U|V,                                              (UC.7)

where SV42128 proves {|U|,|V|}={k,k-1}.

If |A*|<k, SV42128 already gives strict primary Morse improvement by marking U, so there is no rank-flat reentry. Assume therefore

  |A*|=k.                                                 (UC.8)

Then SV42128 shows U is the new cap rail and, crucially,

  e notin V(U),                                          (UC.9)

because e lies in the disjoint exit dimer D. Retain the literal current order

  U=(u_0,...,u_{k-1})                                    (UC.10)

from F_D and apply Section 1 with Q=U and y=e. Arm M supplies Hamilton paths on

  (V(U)-{u_0}) union {e},
  (V(U)-{u_{k-1}}) union {e},                            (UC.11)

while V(U) union {e} is a forbidden (k+1)-support. Hence accepted R966 emits explicit R435 geometry with the expelled completed anchor e retained as the exterior label.

Thus the cap-support change in SV42128 is not merely known to lie in a bounded/factorized recompletion quotient. It is intrinsically curved at the new cap rail before any further support transport is attempted.

### 3. Currentness and provenance
The rail U is literal in the current forest F_D. The two endpoint-replacement Hamilton paths in (UC.11) are graph-intrinsic actual paths supplied by Arm-M support Hamiltonicity. If the R966 output uses one of those alternative paths, accepted R4 may restore that proper Hamilton path into its own literal maximum three-forest; no simultaneous currentness with F_D is claimed or needed. A reverse trimer is itself a proper graph-intrinsic tight path, and a proper tight cycle contains named consecutive proper trimers if a path representative is required. The adjacent-reversal alternative retains the two actual Hamilton words witnessing the reversed state.

The historical data from the Morse lineage are not discarded: retain the old terminal forest F*, the completed fixed-turn anchor e, the exit dimer D, the currentized cap forest F_D, the new literal cap order U, and the two R966 endpoint-replacement paths. The R435 output is therefore cross-epoch geometry tied to the very anchor whose dimer contact caused the formerly flat exit.

### 4. Productive-exit reentry sharpens to curvature
Combining SV42128 with Sections 1-3 gives the sharper dichotomy

  COMPLETED-ANCHOR DIMER EXIT
    => strict largest-rail improvement
       OR explicit R435 cap curvature.                    (UC.12)

There is no third outcome consisting of anonymous rank-flat wandering among cap supports. In particular the ONE-EDGE FACTORIZATION branch of SV40898 is no longer needed merely to explain where a flat cap transition lives: Arm-M endpoint-replacement saturation already puts a named Reverse-Ear portal directly on the new cap rail using the expelled historical anchor.

This does NOT consume the resulting reversal/trimer/cycle portal and therefore does not by itself close Arm M. Its global effect is narrower but structural: the PRODUCTIVE-EXIT REENTRY obligation of SV41376 has no genuinely flat completed-anchor support-transport sector. Any failure of strict primary descent is forced immediately into explicit R435 curvature carrying the old completed anchor as a physical witness label. The next Morse consumer should therefore be formulated on R435 curvature itself, not on cap-support drift.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R927"
    },
    {
        "relation": "dependency",
        "revision_id": "R966"
    },
    {
        "relation": "dependency",
        "revision_id": "R4"
    }
]
```