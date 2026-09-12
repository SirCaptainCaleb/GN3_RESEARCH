# An anchored source transfer automatically pulls two complementary vertices and pushes the reciprocal shield one layer deeper

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-triangle-transfer-double-prefix-push`

**Summary:** In the HHH anchored critical-block packet, any actual SV19956 transfer index i not only moves q0 into Omega-y_i. The universal reverse outer Q-boundary wall from SV20408 lets q1 prepend to the transferred active path, giving an exact H-y_i two-cover with common complement Q[2,t]. Therefore the reciprocal support Q[2,t]+y_i is non-Hamiltonian. This rules out transfers when |Q|=4 and, for |Q|>=5, forces the second-inward reverse star (q3,q2,y_i). Combined with SV20408 and SV20713, every transferred label witnesses the three consecutive reverse source dimers (q1,q0),(q2,q1),(q3,q2). Multiple transfers retain the same shortened literal complement Q[2,t]. TTT is the exact terminal dual. This is a strict support advance, not full absorption.

### 1. Retain one actual HHH transfer
Retain the HHH notation and literal transfer of `fixed-complement-triangle-source-transfer-shield` SV19956 together with the two-ended Q-boundary wall of `fixed-complement-triangle-complement-double-boundary-wall` SV20408. Thus

  Omega=Y disjoint_union V(M),
  Y={y_0,y_1,y_2},
  Q=(q_0,q_1,...,q_t),

and for a TRANSFER index i the actual Hamilton path

  P_i^*=(q_0,y_{i+2},y_{i+1},M)                         (DP.1)

lies on (Omega-{y_i}) union {q_0}. Its literal complementary rail is

  Q^-=(q_1,q_2,...,q_t).

SV20408 is stronger than the transfer-or-shield source test: independently of the transfer bit it gives

  (q_1,q_0,y) tight for every y in Y.                    (DP.2)

### 2. The transfer automatically pulls q_1 across as well
Apply (DP.2) with y=y_{i+2}. Prepending q_1 to (DP.1) creates exactly one new consecutive turn,

  (q_1,q_0,y_{i+2}),

and that turn is tight. Therefore

  \widehat P_i=(q_1,q_0,y_{i+2},y_{i+1},M)              (DP.3)

is a literal Hamilton tight path on

  (Omega-{y_i}) union {q_0,q_1}.

Put

  Q^{(2)}=(q_2,q_3,...,q_t).

Then

  \widehat P_i | Q^{(2)}                                (DP.4)

is a literal two-cover of H-y_i. It is exact, because a Hamilton path on H-y_i together with singleton y_i would two-cover H.

Thus an SV19956 source transfer is intrinsically a TWO-VERTEX COMPLEMENTARY PREFIX PUSH. It shortens the retained common complement by two vertices, not merely by q_0.

### 3. The new reciprocal support is non-Hamiltonian
The support complementary to \widehat P_i inside H is

  R_i^{(2)}={y_i} union V(Q^{(2)}).                      (DP.5)

If R_i^{(2)} were Hamiltonian, a Hamilton path on it together with \widehat P_i would be a spanning two-cover of H. Hence

  Q^{(2)}+y_i is non-Hamiltonian.                        (DP.6)

This immediately improves the order floor for a surviving transfer. If |Q|=4, then Q^{(2)}+y_i has three vertices and is Hamiltonian by boundary antisymmetry R3, contradicting (DP.6). Together with the already-excluded shorter cases,

  TRANSFER => |Q|>=5.                                   (DP.7)

For |Q|>=5, if

  (y_i,q_2,q_3)                                         (DP.8)

were tight, then the literal word

  (y_i,q_2,q_3,...,q_t)

would Hamiltonize R_i^{(2)}, contradicting (DP.6). Therefore (DP.8) is bad and R3 forces

  (q_3,q_2,y_i) tight.                                  (DP.9)

This is a genuine SECOND-INWARD reciprocal shield.

### 4. Consecutive reverse-boundary ancestry
The existing units retain, for the same transferred label y_i,

  (q_1,q_0,y_i) tight                                   from SV20408,
  (q_2,q_1,y_i) tight                                   from SV20713,
  (q_3,q_2,y_i) tight                                   by (DP.9).

Hence every transferred triangle label tail-signs THREE consecutive reverse source-boundary dimers of the original Q. This is not an anonymous three-sign packet: the three witnesses arise in one exact support-transfer chain, and (DP.4) records the actual shortened-complement singleton fiber that creates the last one.

If two distinct indices transfer, the two exact rows (DP.4) share the SAME literal complement Q^{(2)} and retain two distinct second-inward witnesses on (q_3,q_2). If all three transfer, all three rows share that complement and all three triangle labels witness the same second-inward reverse dimer. Their support partitions are restrictions of the one global support bipartition

  (Omega union {q_0,q_1}) | Q^{(2)}

on the corresponding singleton-deletion residues. No claim is made that the enlarged active block is deletion-Hamiltonian.

### 5. TTT dual and scope
The terminal-anchored TTT packet is the exact order dual. A transfer through q_t automatically pulls q_{t-1} across using the full reverse terminal wall, shortens the common complement to Q[0,t-2], rules out |Q|=4, and for surviving |Q|>=5 forces

  (y_i,q_{t-2},q_{t-3}) tight

as the second-inward reverse terminal shield. Multiple terminal transfers share the same shortened literal complement.

This is working support geometry toward Critical-Block Complement Absorption. It is not a spanning two-cover, not an induction on complement length, and not full CBCA closure. The new active block after the push has not been proved deletion-Hamiltonian, so the move may not be iterated by reapplying the critical-block hypothesis without additional work.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
