# A trimer with one retained internal-middle outer-pair cover has no mate-only branch

**Workspace:** D17
**State:** established
**Key:** `internal-source-trimer-payable-return`

**Summary:** Let J=(a,x,c) be a proper tight trimer in a hypothetical smallest counterexample and suppose one retained exact two-cover F_int of H-{a,c} has x internal. Then J always has a certificate-bearing balanced-pair exit, not merely the R919 mate alternative. Apply R920. If every exact H-{a,c} cover keeps x internal, R920's all-internal branch gives an R159 pair directly. If some exact H-{a,c} cover F_end exposes x, compare F_end with the retained internal F_int by accepted R408: deleting x gives an at-most-two-cover from F_end and a literal three-cover from F_int, so R159 yields a balanced pair. In either branch the R159 proof supplies a selected cross-state and R176 ancestry, hence accepted R415 lawfully pays it to an ancestry-bearing both-singleton floor or closure. Therefore every internal-source trimer admits a finite certificate-retaining pair-to-floor continuation. In a fixed-E phase-zero application this removes the isolated R919 mate-clause residue whenever the trimer middle is known internal in a retained H-E frame. It does not apply to an arbitrary trimer whose outer-pair deletion has no retained internal-middle representative.

### 1. Internal-source trimer setup
Let H be a hypothetical smallest Strong Level-(1) counterexample and let

  J=(a,x,c)                                                (IT.1)

be a proper graph-intrinsic tight trimer. Put

  E={a,c}.                                                 (IT.2)

Assume, in addition to the trimer itself, that we retain one literal exact two-cover

  F_int=P|Q  of H-E                                       (IT.3)

in which x is INTERNAL on its path component. Thus if x lies on P we may write

  P=(...,ell,x,r,...),                                    (IT.4)

with both selected neighbors ell,r present.

This extra representative is exactly what is available at an aligned fixed-turn phase-zero checkpoint when J was chosen from an internal vertex of the current exact pair-deletion frame.

### 2. Apply the universal trimer return machine
Apply accepted R920 to J. Its outer-pair dichotomy is exhaustive.

#### Case A. Every exact outer-pair cover keeps x internal
Then R920 is in its ALL-INTERNAL branch. Using any exact H-E return, in particular the retained F_int, deleting x produces a literal three-cover of H-J. R4 supplies the exact two-cover of H-J used in R920. Accepted R159 therefore yields a graph-intrinsic balanced opposite-sign pair.

Inspecting R159/P555, this pair is born by a selected cross-state between two components of the literal three-cover and accepted R176. Therefore it carries the physical cross-state/recompletion certificate required by accepted R415. Outside closure, R415 pays it by a finite certificate-retaining continuation to an ancestry-bearing both-singleton floor.

#### Case B. Some exact outer-pair cover exposes x
Choose one such exact cover

  F_end=P'|Q'  of H-E                                    (IT.5)

in which x is a physical rail endpoint. R920/R919 would ordinarily record an endpoint mate clause here. Instead compare F_end directly with the already-retained F_int.

Accepted R408 applies to these two exact covers of the SAME proper residue H-E because x is endpoint in F_end and internal in F_int. Its proof is literal: delete x. Trimming the endpoint occurrence from F_end leaves a cover of H-J with at most two components, while deleting the internal occurrence from F_int splits its rail into two nonempty intervals and leaves the other rail unchanged, giving a literal three-cover of H-J. Hence R159 applies to the common residue.

Again the fully reconstructed R159 proof chooses an actual selected state of the smaller cover crossing two components of the three-cover and invokes R176. Retain that state, both source covers F_end,F_int, their endpoint/internal roles at x, and the R176 birth certificate. This is a certificate-bearing balanced pair eligible for R415. Therefore outside a spanning two-cover it pays to an ancestry-bearing both-singleton floor.

The physical R919 mate clause from F_end remains a valid optional certificate, but it is no longer the only continuation and is not needed for the pair-to-floor route.

### 3. Internal-source trimer payment theorem
Combining the two R920 regimes gives:

> INTERNAL-SOURCE TRIMER PAYMENT. If a proper tight trimer J=(a,x,c) comes with one retained exact H-{a,c} two-cover in which its middle x is internal, then there is a finite certificate-retaining continuation to either a spanning two-cover or an ancestry-bearing both-singleton floor. The birth of the payable pair is always an R159/R176 cross-state birth.

The theorem is deliberately representative-aware. It uses the retained internal cover in Case B; without that cover, R919's mate-only endpoint branch remains a genuine possibility.

### 4. Fixed-endpoint phase-zero use
At an E-aligned phase-zero checkpoint, choose an internal middle x in the current exact H-E frame and orient E union {x} by R3 to obtain J. The hypotheses above are then automatic. Thus the SOURCE trimer of every internal-middle fixed-E episode has a lawful paid excursion. By SV57138/SV57422 that pair can be paid, steered back to the old E, and returned through R1022 without increasing the fixed-E clock; it is strict except at the known fully anchored aligned equality stratum.

This does NOT by itself consume an arbitrary R445 geometric output, because such an output may contain a trimer whose outer pair is different from E and for which no internal-middle exact cover is retained. Therefore the theorem removes mate clauses only for internal-source trimers, not for generic phase-zero curvature.

### 5. Dependencies and fences
Only accepted R408, R920, R159, R176, and R415 are used. R24, R5, and R446/R358 are not used. Current source representatives and historical paid descendants are kept distinct throughout.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R408"
    },
    {
        "relation": "dependency",
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R176"
    },
    {
        "relation": "dependency",
        "revision_id": "R415"
    },
    {
        "relation": "dependency",
        "revision_id": "R920"
    }
]
```