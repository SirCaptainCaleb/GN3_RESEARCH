# Every critical-block vertex witnesses both reverse boundary dimers of the fixed Hamilton rail

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-critical-block-full-boundary-wall`

**Summary:** In any smallest-counterexample fixed-complement split V(H)=Omega disjoint-union Q with Omega non-Hamiltonian deletion-Hamiltonian and Q=(q0,...,qt) a literal Hamilton path of order at least two, every y in Omega tail-witnesses the reverse source dimer (q1,q0) and head-witnesses the reverse terminal dimer (qt,qt-1). Indeed choose any Hamilton puncture P_y on Omega-y. If (y,q0,q1) were tight then y,Q would Hamiltonize Q+y and pair with P_y to two-cover H; exact reversal therefore gives (q1,q0,y). The terminal statement is dual. Thus the full critical block, not merely an anchored R961 triangle, lies inside one common two-ended reverse boundary wall. No first-inward propagation or CBCA closure is claimed.

### 1. Fixed-complement critical-block setting
Let H be a hypothetical smallest Strong Level-(1) counterexample and suppose

  V(H)=Omega disjoint_union V(Q),
  Q=(q_0,q_1,...,q_t),

where Omega is non-Hamiltonian but deletion-Hamiltonian and Q is a literal Hamilton tight path. Assume |Q|>=2 so its two oriented boundary dimers are defined. For each y in Omega choose any actual Hamilton puncture path P_y on Omega-y. Then P_y|Q is an exact two-cover of H-y.

### 2. Every critical vertex reverses the source boundary
Fix y in Omega. If

  (y,q_0,q_1) tight,                                      (FW.1)

then the literal word

  (y,q_0,q_1,...,q_t)                                    (FW.2)

is Hamiltonian on {y} union V(Q): (FW.1) is its only new turn and every later turn is inherited from Q. Together with P_y on Omega-y this is a spanning two-cover of H, contradiction. Hence (FW.1) is bad. Boundary antisymmetry R3 gives

  (q_1,q_0,y) tight                                      (FW.3)

for every y in Omega.

### 3. Every critical vertex reverses the terminal boundary
Dually, if

  (q_{t-1},q_t,y) tight,                                 (FW.4)

then (q_0,...,q_t,y) Hamiltonizes Q+y and pairs with P_y to two-cover H. Thus (FW.4) is bad and R3 gives

  (y,q_t,q_{t-1}) tight                                  (FW.5)

for every y in Omega.

Therefore the same full witness set Omega occurs on both reverse outer boundary dimers of Q:

  (q_1,q_0,y) tight,
  (y,q_t,q_{t-1}) tight                                  (FW.6)

for all y in Omega.

### 4. Moonshot interface
This wall is independent of the R961 quiet/explicit-R435 dichotomy. In particular every explicit R435 reversal, reverse trimer, or proper tight cycle occurring among puncture paths of Omega lies inside the same two-ended Q-boundary witness wall. The quiet anchored triangle of SV20408 is only a three-vertex specialization of (FW.6).

No first-inward propagation is asserted here, and no Critical-Block Complement Absorption conclusion is claimed. The intended consumer is the explicit-R435 half of CBCA: combine its one-vertex exchange geometry with the all-Omega two-ended wall rather than treating the R435 output as anonymous local currency.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
