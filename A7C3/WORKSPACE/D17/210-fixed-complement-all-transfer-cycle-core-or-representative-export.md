# An all-transfer endpoint-return cycle exits in one step to a small core or current maximum-forest dynamics

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-all-transfer-cycle-core-or-representative-export`

**Summary:** In a fixed-complement critical block, take a constant-HEAD endpoint-return cycle all of whose matched incidences transfer. After the common q0,q1 prefix push, the cycle labels form a live puncture cylinder with complement Q[2,t]. If the pushed cycle has an R435-active adjacent pair, all three R435 output species now have parent-scale current destinations. A proper cycle gives the closed movable-break maximum-three-forest family; a reverse trimer gives a universally one-extendable four-set or a fresh maximum three-forest; an adjacent selected-state reversal necessarily lies in the INTERNAL branch of the pair-deletion currentization because the exchanged head label y_{i+1} sits strictly internally at position three of the pushed path, and therefore also produces an exact pair-deletion two-cover whose dimer lift is a current maximum three-forest. If every pushed adjacent comparison is quiet, SV24412 forces the endpoint cycle to have length three and yields a directed comparison triangle; adjoining q0 gives a universally one-extendable four-set by R902. Thus the all-transfer endpoint-cycle branch does not require iterating deletion-Hamiltonicity after complement shortening: it already exits in one step to the small-core absorber or to actual maximum-three-forest representative dynamics. TAIL is dual.

### 1. Setup: all-transfer endpoint-return cycle
Retain the fixed-complement critical-block setting

  V(H)=Omega disjoint_union V(Q),
  Q=(q_0,q_1,...,q_t),

and a constant-HEAD directed endpoint-return cycle

  y_0 -> y_1 -> ... -> y_{ell-1} -> y_0

as in the accepted R945/R961 system. Choose actual Hamilton puncture paths

  P_i=(y_{i+1},r_i,...)

on Omega-y_i realizing the matched heads. Assume every matched incidence takes the successful HEAD-transfer branch.

By SV24412, after the common double-prefix push there are exact rows

  P_i^+=(q_1,q_0,y_{i+1},r_i,...) | Q^{(2)},
  Q^{(2)}=Q[2,t],                                          (AE.1)

for every cycle label y_i.

The family in (AE.1) is also a live puncture cylinder in the sense of SV25834, with active support

  A^+=Omega union {q_0,q_1}

and live set containing all y_i. No deletion-Hamiltonicity of A^+ at q_0 or q_1 is needed below.

### 2. Any pushed R435 activity has a current parent-scale destination
Compare two adjacent pushed rows P_i^+,P_{i+1}^+. Their supports differ by exactly the exchanged labels y_i,y_{i+1}, and both share the same literal complement Q^{(2)}.

Suppose the comparison is R435-active.

PROPER CYCLE. By SV25652, any proper tight cycle output already supplies all cyclic breaks as actual maximum spanning three-forests with one fixed exact two-covered complement. Thus this branch exits immediately to a closed movable-break representative family.

REVERSE TRIMER. By SV26759, a one-foreign reverse trimer in a live puncture cylinder gives either a universally one-extendable four-set or a literal fresh maximum spanning three-forest obtained by one physical cut and reattachment.

ADJACENT SELECTED REVERSAL. Apply SV27136. In the present pushed comparison, the label y_{i+1}, which is present in P_i^+ and omitted from P_{i+1}^+, occurs in the displayed word (AE.1) strictly between q_0 and r_i. Since the original puncture path has at least one vertex after its matched head, y_{i+1} is internal in P_i^+.

Therefore the endpoint-endpoint case of SV27136 is impossible for this pair. Deleting {y_i,y_{i+1}} gives a three-cover from the trimmed P_i^+ row; smallest-counterexample minimality supplies an exact two-cover T of the same pair-deletion residue, and T carries a current selected crossing between two components of that trim. Lifting T with the deleted dimer gives an actual maximum spanning three-forest on H. Hence the selected-reversal output also exits to current maximum-forest dynamics.

Thus every pushed R435-active adjacent pair yields one of

  UNIVERSAL ONE-EXTENSION FOUR-SET,
  FRESH MAXIMUM THREE-FOREST,
  CLOSED MOVABLE-BREAK MAXIMUM-FOREST FAMILY.              (AE.2)

No generic R435 abundance is being counted as progress; the actual representative produced by its output is the retained object.

### 3. The all-quiet pushed cycle is already the small-core branch
Suppose every adjacent pushed comparison is R435-quiet. SV24412 proves that ell cannot be at least four. Since endpoint-return 2-cycles are impossible, ell=3, and its three physical labels Y={y_0,y_1,y_2} form a directed comparison triangle.

Put

  S=Y union {q_0}.                                         (AE.3)

For every d outside S, the five-set S+d still contains the directed comparison triangle on Y, so it is nonintegrable. Accepted R902 therefore gives a Hamilton path on S+d. Thus

  S+d is Hamiltonian for every d outside S.                (AE.4)

No Hamiltonicity of S itself is required. Therefore S is exactly a universally one-extendable four-set in the strengthened G9 sense.

### 4. Consequence: no CBCA induction is needed for this branch
The original interpretation of SV24412 as an iterable contraction was too strong: after pushing q_0,q_1, the enlarged active support need not remain deletion-Hamiltonian and need not admit a new endpoint-return matching.

The present argument avoids that obligation. The one push is enough. Either an adjacent pushed comparison is active and (AE.2) exports the obstruction into actual maximum-three-forest representative dynamics, or all comparisons are quiet and (AE.4) exports to the small extension-core absorber.

Hence the all-transfer endpoint-return cycle is a one-step

  CBCA -> {SMALL CORE OR CURRENT REPRESENTATIVE DYNAMICS}

compiler, not an induction on critical blocks.

The constant-TAIL case is the exact terminal dual. This section does not prove the universal one-extension four-set absorber or Global Three-Forest Escape; it supplies their inputs with full physical ancestry.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R902"
    },
    {
        "relation": "dependency",
        "revision_id": "R945"
    },
    {
        "relation": "dependency",
        "revision_id": "R961"
    }
]
```
