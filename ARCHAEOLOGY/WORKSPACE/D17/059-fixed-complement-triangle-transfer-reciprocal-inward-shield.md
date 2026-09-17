# A complementary-support transfer either closes at order three or forces the reciprocal first-inward shield

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-triangle-transfer-reciprocal-inward-shield`

**Summary:** In the HHH anchored triangle packet, whenever SV19956 transfers q0 into Omega-y_i and gives the Hamilton path P_i^*=q0,y_{i+2},y_{i+1},M with literal complement Q^-=(q1,...,qt), the reciprocal support Q^-+y_i cannot be Hamiltonian or it would pair with P_i^* to two-cover H. In particular (y_i,q1,q2) is bad, so R3 forces the first-inward reverse star (q2,q1,y_i). If |Q|=3, Q^-+y_i itself is a three-set and therefore has a Hamilton trimer by R3, so the transfer branch is impossible. Thus every surviving transferred label forces |Q|>=4 and a named first-inward Q shield. Two or three simultaneous transfers give the corresponding two- or three-witness first-inward packet on the same physical dimer (q2,q1). TTT is the exact terminal dual.


### 1. Retain one actual HHH support transfer
Use the HHH setup and notation of `fixed-complement-triangle-source-transfer-shield` SV19956. Thus

  Omega=Y disjoint_union V(M),
  Y={y_0,y_1,y_2},
  Q=(q_0,q_1,...,q_t),

with |Q|>=3. Suppose index i lies in the TRANSFER branch of SV19956. The proof of that branch constructs the literal Hamilton path

  P_i^*=(q_0,y_{i+2},y_{i+1},M)                         (RI.1)

on (Omega-{y_i}) union {q_0}, and retains the literal Hamilton suffix

  Q^-=(q_1,q_2,...,q_t).                                 (RI.2)

Hence P_i^* | Q^- is an exact two-cover of H-y_i.

### 2. The reciprocal replacement support is necessarily non-Hamiltonian
The support complementary to P_i^* inside H is

  R_i={y_i} union V(Q^-)=Q-{q_0}+{y_i}.                  (RI.3)

If R_i had any Hamilton tight path K_i, then P_i^* and K_i would be two vertex-disjoint Hamilton paths whose supports partition V(H). They would therefore form a spanning two-cover of H, contradiction. Consequently

  Q-{q_0}+{y_i} is non-Hamiltonian.                      (RI.4)

This is exactly the failure of the desired reciprocal one-for-one exchange q_0 <-> y_i. It is a support statement, not merely failure of one displayed insertion order.

### 3. The displayed source insertion therefore reverses one layer inward
The literal Q^- order begins (q_1,q_2). If

  (y_i,q_1,q_2)                                          (RI.5)

were tight, then

  (y_i,q_1,q_2,...,q_t)                                  (RI.6)

would be a Hamilton tight path on R_i, contradicting (RI.4). Therefore (RI.5) is bad. Boundary antisymmetry R3 gives the exact reverse turn

  (q_2,q_1,y_i) tight.                                   (RI.7)

Thus every actual source transfer from SV19956 forces the omitted physical triangle label to become a witness on the first-inward reverse Q dimer (q_2,q_1). No endpoint-Hamiltonicity theorem is being assumed: the argument uses the actual complementary transferred path P_i^* and the complete support partition.

### 4. The three-vertex complementary rail cannot host a transfer
If |Q|=3, then Q^-+y_i has exactly three vertices. By R3, every three-vertex boundary subtournament has at least one tight ordering, hence is Hamiltonian. This contradicts (RI.4). Therefore in a smallest counterexample

  TRANSFER => |Q|>=4.                                    (RI.8)

So every surviving transfer has q_3 available and carries the literal first-inward shield (RI.7).

### 5. Simultaneous transfers retain simultaneous inward witnesses
If two distinct indices i,j are in the TRANSFER branch of SV19956, their two exact singleton rows share the same literal complement Q^- and (RI.7) gives two distinct witnesses y_i,y_j on the same tested reverse dimer (q_2,q_1). If all three indices transfer, all three triangle labels witness that same first-inward reverse dimer.

This is stronger than exporting the transfers independently: the reciprocal failures are physically synchronized on one fixed Q boundary layer. It still does not supply the four exterior witnesses required by R974 and does not by itself close H.

### 6. TTT dual
For the TTT anchored packet, apply the exact terminal dual of the preceding argument to a transfer through q_t. The reciprocal support Q-{q_t}+{y_i} is non-Hamiltonian; the displayed terminal insertion is therefore bad and exact reversal forces the corresponding first-inward reverse terminal shield. The order-three complementary rail again makes any transfer impossible.

Status: direct working deduction from the actual SV19956 transfer path and accepted R3. It is not full Critical-Block Complement Absorption and does not consume the remaining reciprocal shield packet.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
