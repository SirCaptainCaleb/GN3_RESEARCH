# Every large articulation side carries a fixed-complement R961/R435 fan

**Workspace:** D17
**State:** established
**Key:** `singleton-articulation-fixed-complement-r961-fan`

**Summary:** Let U be the selected-edge union of a singleton-cover family in a hypothetical counterexample and let w be an articulation with U-w=A+B. The accepted cut-vertex normal form makes Omega=A+w and B+w non-Hamiltonian deletion-Hamiltonian blocks and C_w supplies literal Hamilton rails A|B. For every y in Omega and every Hamilton puncture path P_y on Omega-y, P_y|B is an exact singleton-deletion cover of H-y, so the entire endpoint-Hall/R961 analysis on Omega is automatically current over the same literal complement B. If |Omega|>=5, accepted source-anchored SV304 applied to Omega=A+w says either explicit R435 geometry already occurs, or the quiet R961 HHH/TTT triangle contains w and anchors at the first or last two vertices of the literal A order; every remaining puncture Hamilton path is then R435-nonquiet against that same three-path packet. Hence a large articulation side is a support-wide common-complement R435 reservoir, not merely an abstract critical block. In the quiet anchored triangle, trimming consecutive matched labels gives three exact common-complement pair-deletion component drops with explicit boundary cross-states at the first or last core vertex.

### Fixed-complement currentization from an articulation

Retain a hypothetical smallest counterexample H, one chosen exact singleton-deletion cover family, and its ordinary selected-edge union U. Suppose w is an articulation and write

`U-w=A disjoint_union B`.

Use the accepted exact cut-vertex normal form `singleton-cover-union-block-normal-form` SV3086 proof-aware. The literal w-deletion cover is

`C_w = X | Q`,

where X is a Hamilton path on A and Q is a Hamilton path on B. Put

`Omega=A+{w}`.

SV3086 proves that Omega is non-Hamiltonian and deletion-Hamiltonian. More precisely, for every y in Omega there exists an actual Hamilton tight path P_y on Omega-y: for y=w take X itself, while for y in A take the contiguous Omega-y subpath extracted in the proof of SV3086.

The fixed opposite path Q upgrades this intrinsic critical-block family to current singleton-cover data. For **any** Hamilton path P on Omega-y, not merely the originally extracted one,

`P | Q`

is a literal two-cover of H-y. It is exact. If H-y were Hamiltonian, that Hamilton path together with the singleton path {y} would two-cover H, contradicting the hypothetical counterexample. Hence every Hamilton puncture path of Omega may be used as the active rail of an exact H-y cover while retaining the SAME literal complement Q. No seam or representative transport is needed.

Thus the complete endpoint-incidence system of Omega is automatically a fixed-complement singleton-cover system inside H.

### Accepted R961/SV304 becomes a common-complement fan

Assume |Omega|>=5, equivalently |A|>=4, and write the retained w-deletion rail as

`X=(x_1,...,x_k)`,  `k>=4`.

Apply accepted R961/P1033 to the non-Hamiltonian deletion-Hamiltonian block Omega, then the accepted exact source-anchored consequence `source-anchored-r961-fan` SV304 with p=w and source order X. The proof mechanism is retained rather than used as a statement-only arrow.

Either an explicit R435 reversal, reverse trimer, or proper tight cycle already occurs in the R961 puncture-path comparisons, or the unique fully X-quiet residue is source-anchored:

HHH:
`P_w=(x_1,x_2,x_3,...,x_k)=X`,
`P_{x_1}=(x_2,w,x_3,...,x_k)`,
`P_{x_2}=(w,x_1,x_3,...,x_k)`;

or TTT, the exact terminal dual anchored at x_{k-1},x_k.

Moreover SV304 proves that every Hamilton path on any remaining puncture Omega-x_j is R435-nonquiet against at least one member of this SAME three-path packet. By the preceding fixed-complement observation, every one of those paths can be paired with Q. Therefore every forced R435 comparison is current inside explicit singleton-deletion covers whose other rail is the identical literal Hamilton path Q.

So an articulation side of order at least five is not merely deletion-Hamiltonian. It carries a support-wide source-visible common-complement R435 reservoir. The dual side B+w has the identical conclusion with fixed complement X whenever |B+w|>=5.

### The quiet anchored triangle already contains three pair-deletion component drops

Retain the HHH packet; TTT is its exact head/tail dual. Put

`M=(x_3,...,x_k)`.

Consider the consecutive matched pair of deletion labels w,x_1. From the exact cover

`C_w^* = (x_1,x_2,M) | Q`

delete the endpoint x_1. This leaves the literal exact two-cover of H-{w,x_1}

`(x_2,M) | Q`.

From

`C_{x_1}^* = (x_2,w,M) | Q`

delete the internal vertex w. This leaves the literal three-cover

`(x_2) | M | Q`

of the SAME residue. The proof mechanism of R159 therefore has a completely visible first crossing: the smaller cover joins the singleton component (x_2) to M by its selected boundary state

`x_2 -> x_3`.

Retain that state and the common complement Q rather than immediately paying it.

Cyclically, the pair x_1,x_2 gives the exact common-residue comparison

`(w,M)|Q` versus `(w)|M|Q`,

whose visible selected crossing is

`w -> x_3`;

and the pair x_2,w gives

`(x_1,M)|Q` versus `(x_1)|M|Q`,

with visible selected crossing

`x_1 -> x_3`.

Thus the HHH anchor carries the three current boundary states

`x_2 x_3,   w x_3,   x_1 x_3`

on three named pair-deletion residues, all with literal common complement Q. In the TTT anchor the exact dual gives three current states incident with the last core vertex x_{k-2} and oriented toward the three anchor labels in the retained terminal orders.

This is stronger than anonymous R159 currency. The physical hub w, source order X, common complement Q, three pair-deletion residues, and all three crossing states remain available simultaneously as graph-intrinsic/current data.

### Boundary K4 selected-edge core

In the HHH packet, the three puncture paths together select all six ordinary adjacencies on

`{w,x_1,x_2,x_3}`:

from X: `x_1x_2, x_2x_3`;
from P_{x_1}: `x_2w, wx_3`;
from P_{x_2}: `wx_1, x_1x_3`.

Hence the local deletion-path union contains an ordinary K4 on the first anchored four-set. The TTT packet contains the exact terminal K4 on `{w,x_{k-2},x_{k-1},x_k}`.

This observation is purely about the selected-edge reservoir. It does not say the four-set is Hamiltonian or that the K4 edges coexist in one path.

### Scope

The theorem currentizes the full R961/SV304 fan across a cut vertex and exposes three exact pair-deletion component-drop crossings in its only quiet triangle. It does not consume a generic R435 reverse trimer/proper cycle, does not promote local reversal to R561, and does not prove the articulation impossible. The next consumer should spend the common complement Q together with either the fixed three-state boundary star above or a forced non-anchor R435 event. No anonymous payment is taken here.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R961"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R159"
    }
]
```
