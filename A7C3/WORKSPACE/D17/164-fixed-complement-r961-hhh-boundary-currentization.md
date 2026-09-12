# The HHH wall currentizes one layer inward or creates a common-complement support transfer

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-r961-hhh-boundary-currentization`

**Summary:** Starting from the two-ended three-witness wall on Q, test the next inward Q dimer against each anchor label. A failed inward test gives the desired first-inward reverse shield; a tight test transfers one Q endpoint into the active puncture support and yields an exact singleton-deletion cover with shortened common complement. Thus for each anchor label independently, source side and terminal side obey TRANSFER-or-INWARD-SHIELD. If two labels transfer on the same side, the shortened common complement is shared and the two transferred active supports differ by one anchor label, creating a same-residue comparison after deleting both anchors.

### Setup
Retain the fixed-complement packet and wall on

  Q=(q_0,q_1,...,q_t),

with |Q|>=3 and anchor labels Y={y_0,y_1,y_2}. For each i the active puncture path P_i Hamiltonizes Omega-y_i and is paired with Q in an exact cover of H-y_i.

The wall gives

  (q_1,q_0,y_i) tight,
  (y_i,q_t,q_{t-1}) tight

for every i.

### Source transfer-or-shield
Fix i and test the next inward turn

  a_i=(y_i,q_1,q_2).

If a_i is bad, R3 gives

  (q_2,q_1,y_i) tight,

a first-inward reverse shield on the Q dimer (q_2,q_1).

If a_i is tight, then

  (y_i,q_1,q_2,...,q_t)

is a Hamilton path on {y_i} union (Q-{q_0}). Pair it with the active path obtained from P_i after adjoining q_0 at the appropriate source-transfer position supplied by the anchored packet. In the HHH packet that active transfer path is literal and was constructed in the earlier source-transfer section; denote it A_i(q_0). Then

  A_i(q_0) | (y_i,q_1,...,q_t)

is a spanning two-cover unless the two supports overlap at y_i. To keep the fibers disjoint, instead regard the tight a_i as currentizing the reciprocal support Q-q_0+y_i: it gives an explicit Hamilton path on that support. By the reciprocal universal-crossing duality, the active replacement Omega-y_i+q_0 must then be non-Hamiltonian in a counterexample; hence the source-transfer branch of the anchored packet cannot simultaneously occur for that same i. Thus a_i tight is exactly the RECIPROCAL-HAMILTONIAN alternative opposite active transfer.

Accordingly each label i has a clean support dichotomy:

  active q_0-transfer, forcing inward shield (q_2,q_1,y_i),
  or reciprocal Hamiltonian Q-q_0+y_i.

The terminal side is dual.

### Corrected currentization interface
The useful conclusion is not that every tight inward turn itself performs the active transfer. Rather, the anchored packet supplies an independent active-transfer bit, and reciprocal Hamiltonicity is disjoint from it. Therefore:

- if i is an active transfer label, the first-inward reverse shield is forced;
- if the inward shield is absent, the reciprocal support is explicitly Hamiltonian and i is not an active transfer label.

This is the exact transfer-or-shield currentization already implicit in the reciprocal-universal-crossing theorem, now expressed directly at the Q boundary.

### Multi-label consequence
If two distinct anchor labels are active transfers through q_0, both force the same reverse dimer (q_2,q_1) with distinct witnesses. Their transferred singleton-deletion covers share the shortened literal complement Q-q_0. Deleting both anchor labels from the two covers gives two covers of one common proper residue; any endpoint/internal discrepancy or selected cross-state between them is therefore same-residue current.

### Scope
This corrected section withdraws any implication that a tight inward turn alone yields a spanning support transfer. The exact usable statement is active-transfer => inward shield, and absence of shield => reciprocal Hamiltonicity. The three-witness outer wall remains independently valid.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
