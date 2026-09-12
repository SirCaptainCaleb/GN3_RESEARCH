# Every successful endpoint-return transfer is a same-residue boundary reversal square

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-general-transfer-reversal-square`

**Summary:** In the general fixed-complement endpoint-return compiler SV23560, a successful HEAD transfer on a puncture path P_a=(b,r1,...) does more than shorten the complement. The original exact H-a row P_a|Q selects q0->q1, while the double-pushed exact row (q1,q0,P_a)|Q[2,t] selects the same physical dimer in the reverse direction q1->q0. Since a surviving transfer forces |Q|>=5, q0 is endpoint/internal and q1 internal/endpoint across the two exact covers, so accepted R408 applies at both vertices. Deleting q0 gives the explicit 2-versus-3 component pair P_a|(q1,...,qt) versus P_a|{q1}|Q[2,t], with named crossing q1->q2 in the smaller cover. Deleting q1 gives P_a|{q0}|Q[2,t] versus (q0,P_a)|Q[2,t], with named crossing q0->b. The TAIL case is the exact terminal dual on q_{t-1}q_t. Thus every successful endpoint-return transfer is automatically a source-current support-switch reversal square, without anchored-triangle hypotheses.

### 1. General successful HEAD transfer
Retain the fixed-complement critical-block setting and one successful HEAD endpoint-return transfer from `fixed-complement-endpoint-return-transfer-compiler` SV23560. Thus

  V(H)=Omega disjoint_union V(Q),
  Q=(q_0,q_1,...,q_t),
  P_a=(b,r_1,...,r_k)

with P_a Hamiltonian on Omega-a, and the successful transfer gives the two exact H-a covers

  F = P_a | (q_0,q_1,...,q_t),                           (RS.1)
  F'=(q_1,q_0,b,r_1,...,r_k) | (q_2,...,q_t).             (RS.2)

SV23560 already proves that any surviving successful transfer has |Q|>=5.

### 2. The pushed row reverses the literal boundary state
The original row F selects the physical state

  q_0 -> q_1,

while F' selects the same physical dimer in the opposite direction

  q_1 -> q_0.                                             (RS.3)

This is not merely an abstract order discrepancy. It occurs in two literal exact two-covers of the SAME singleton residue H-a. Moreover q_0 is a rail endpoint in F and internal in F', whereas q_1 is internal in F and a rail endpoint in F'. Hence accepted R408 applies at both physical vertices.

### 3. The two component drops are explicit
Delete q_0 from (RS.1)-(RS.2). The two resulting literal covers of H-{a,q_0} are

  P_a | (q_1,q_2,...,q_t),
  P_a | {q_1} | (q_2,...,q_t).                           (RS.4)

Thus the component counts are two and three. In the smaller cover the selected edge

  q_1 -> q_2                                                (RS.5)

crosses the singleton block {q_1} to the Q[2,t] block of the larger cover.

Delete q_1 instead. The two resulting covers of H-{a,q_1} are

  P_a | {q_0} | (q_2,...,q_t),
  (q_0,b,r_1,...,r_k) | (q_2,...,q_t).                    (RS.6)

Again the component counts are three and two, and the smaller cover contains the explicit crossing

  q_0 -> b.                                                (RS.7)

So a successful transfer carries two ancestry-current component drops automatically; no generic payment step is needed to locate their crossing states.

### 4. TAIL dual
If b is the certified TAIL of P_a and the terminal transfer succeeds, the original row selects

  q_{t-1} -> q_t,

whereas the double-pushed row ending (...,b,q_t,q_{t-1}) selects

  q_t -> q_{t-1}.                                         (RS.8)

Deleting q_t gives the explicit two-versus-three pair with named smaller-cover crossing q_{t-2}->q_{t-1}; deleting q_{t-1} gives the reciprocal pair with named crossing b->q_t. This is the exact terminal dual of (RS.4)-(RS.7).

### 5. Scope
Therefore EVERY successful endpoint-return transfer in a fixed-complement critical block is automatically a same-residue support-switch reversal square on the appropriate boundary dimer of Q. The earlier anchored-triangle reversal-square phenomenon is a specialization, not the source of the mechanism.

This section does not by itself turn the support-switch reversal into R561, because the two reversed occurrences lie on different support partitions. Its value for common-complement holonomy contraction is that every successful transfer already carries a literal selected-state reversal plus two lower-residue component drops, with all physical labels current.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R408"
    }
]
```
