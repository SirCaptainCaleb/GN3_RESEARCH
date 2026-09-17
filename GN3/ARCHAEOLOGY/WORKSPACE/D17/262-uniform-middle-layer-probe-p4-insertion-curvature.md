# Every Arm-M probe-P4 is a two-seam insertion barrier or immediate Reverse-Ear curvature

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-probe-p4-insertion-curvature`

**Summary:** Let A=(a0,...,a_{k-1}) be a Hamilton k-rail and z exterior with A+z non-Hamiltonian. If one consecutive trimer K_i=(a_i,a_{i+1},a_{i+2}) together with z supports a Hamilton P4, compare that P4 with A by accepted R435. Any reverse order of the three A contacts is already an adjacent reversal, reverse trimer, or proper cycle. Otherwise the P4 is one of the four literal insertion orders obtained by placing z in the ordered triple K_i. Each such local insertion extends along the inherited A order to a candidate Hamilton path on A+z with at most two uncertified boundary turns: two when z lies outside K_i, one when z lies in either internal gap, with the obvious endpoint degeneracies. If all required turns were tight, A+z would be Hamiltonian. Therefore one boundary turn is bad, and R3 makes its complete reversal a proper tight trimer involving z and an adjacent A-pair within distance at most two of the active cell. In R927 Arm M, A+z is a forbidden (k+1)-support, so EVERY probe-P4 from SV42636 immediately compiles to bounded graph-intrinsic curvature: an R435 output or one of these local reverse insertion-barrier trimers. R4 currentizes every such trimer. Consequently the positive-density P4 alternative of SV42636 is actually positive-density cell-indexed curvature, not a separate quiet portal species. Exact distinctness of the resulting trimer supports is not claimed.

### 1. Local setup and Reverse-Ear straightening
Let A=(a_0,a_1,...,a_{k-1}) be a vertex-simple tight path, let z be a vertex outside A, and assume A+z is non-Hamiltonian. Fix i with 0<=i<=k-3 and put K_i=(a_i,a_{i+1},a_{i+2}). Suppose the four-set V(K_i) union {z} supports an actual Hamilton tight P4 P.

Compare P with the ancestral path A using accepted Reverse Ear R435. If the A-vertices encountered along P are not in increasing A-order, retain the exact R435 output: an adjacent selected reversal, a reverse tight trimer, or a proper tight cycle. Henceforth assume no such output. Since P contains exactly the three consecutive A-vertices a_i,a_{i+1},a_{i+2}, their order in P must be exactly

  a_i < a_{i+1} < a_{i+2}.

Thus P is literally one of the four insertion words

  P_0=(z,a_i,a_{i+1},a_{i+2}),
  P_1=(a_i,z,a_{i+1},a_{i+2}),
  P_2=(a_i,a_{i+1},z,a_{i+2}),
  P_3=(a_i,a_{i+1},a_{i+2},z).              (IP.1)

No other quiet P4 order is possible.

### 2. Exterior-left insertion has only two missing turns
Assume P=P_0. Extending to the right along A is automatic, so

  (z,a_i,a_{i+1},...,a_{k-1})

is tight. The global insertion candidate

  G_0=(a_0,...,a_{i-1},z,a_i,...,a_{k-1})

uses only inherited A-turns and the P_0 turns, except for

  g_0=(a_{i-2},a_{i-1},z)  when i>=2,
  g_1=(a_{i-1},z,a_i)      when i>=1.       (IP.2)

If every defined turn in (IP.2) were tight, G_0 would Hamiltonize A+z. Therefore some defined turn is bad. Boundary antisymmetry R3 gives respectively

  (z,a_{i-1},a_{i-2}) tight,
  or (a_i,z,a_{i-1}) tight.                    (IP.3)

If i=0 there is no missing turn and P_0 itself extends to a Hamilton path on A+z, contrary to hypothesis.

### 3. First internal insertion has one missing turn
Assume P=P_1. The candidate

  G_1=(a_0,...,a_i,z,a_{i+1},...,a_{k-1})

has exactly one uncertified turn,

  g=(a_{i-1},a_i,z)  when i>=1.               (IP.4)

For i=0 there is no missing turn and A+z is Hamiltonian. Otherwise g must be bad, so R3 gives

  (z,a_i,a_{i-1}) tight.                       (IP.5)

### 4. Second internal insertion has one missing turn
Assume P=P_2. The candidate

  G_2=(a_0,...,a_{i+1},z,a_{i+2},...,a_{k-1})

has exactly one uncertified turn,

  h=(z,a_{i+2},a_{i+3})  when i<=k-4.          (IP.6)

For i=k-3 there is no missing turn and A+z is Hamiltonian. Otherwise h must be bad, so R3 gives

  (a_{i+3},a_{i+2},z) tight.                   (IP.7)

### 5. Exterior-right insertion has only two missing turns
Assume P=P_3. Extending to the left along A is automatic. The global candidate

  G_3=(a_0,...,a_{i+2},z,a_{i+3},...,a_{k-1})

has only

  h_0=(a_{i+2},z,a_{i+3})  when i<=k-4,
  h_1=(z,a_{i+3},a_{i+4})  when i<=k-5          (IP.8)

as uncertified turns. If every defined turn were tight, G_3 would Hamiltonize A+z. Hence one is bad and R3 gives respectively

  (a_{i+3},z,a_{i+2}) tight,
  or (a_{i+4},a_{i+3},z) tight.                (IP.9)

For i=k-3 there is no missing turn and P_3 itself extends to A+z, impossible.

### 6. P4-to-curvature compiler
Combining Sections 1-5 gives the order-free local theorem:

  Hamilton P4 on z plus one consecutive A-trimer
  + non-Hamiltonicity of A+z
  => R435 curvature, or one proper reverse insertion-barrier trimer.   (IP.10)

The barrier trimer always uses z and an adjacent physical A-pair lying within distance at most two from the P4 window. It is graph-intrinsic. No cover synchronization, payment, or representative transport is used.

### 7. Arm-M consequence: the dense P4 family is dense curvature
Return to accepted R927 Arm M and the pair-deletion propagation theorem SV42636. There A has order k and every active probe z lies outside A. The support A+z has order k+1 and is therefore non-Hamiltonian. Thus every ACTIVE cell of SV42636, after choosing its actual probe-P4, enters (IP.10).

Consequently the railwide dichotomy sharpens to

  adjacent DUAL cells -> explicit R435 reverse-trimer/proper-cycle curvature,

  otherwise every retained ACTIVE cell -> bounded local R435/reverse-trimer curvature.  (IP.11)

In particular the repeated common-probe P4 family requested by G16 is not a new quiet portal species. Each occurrence already carries a bounded curvature certificate tied to its exact rail position; if the same deleted probe z occurs in two separated active cells, both cell-indexed curvature certificates retain that same physical probe. The certificates may coincide when localization neighborhoods overlap, so no distinctness count is asserted here.

Every proper reverse trimer in (IP.3),(IP.5),(IP.7),(IP.9) currentizes by accepted R4 to a literal maximum spanning three-forest. The remaining global problem is therefore curvature consumption, not P4 absorption: turn these ancestry-bearing local reverse trimers / R435 outputs into forbidden (k+1)-path, strict phased-Morse descent, or closure.

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
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R927"
    }
]
```