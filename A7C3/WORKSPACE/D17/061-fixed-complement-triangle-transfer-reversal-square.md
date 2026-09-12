# Every anchored two-prefix transfer creates a same-residue selected-edge reversal square with two reciprocal component drops

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-triangle-transfer-reversal-square`

**Summary:** For a transferred triangle label y_i, retain the original fixed-complement exact row R_i|Q on H-y_i and the pushed exact row (q1,q0,R_i)|Q[2,t] from SV21176. The physical edge q0q1 is selected in opposite directions in these two exact covers of the same residue. Since |Q|>=5, q0 is source/internal across the two rows and q1 is internal/source, so accepted R408 applies at both vertices. More strongly, deleting q0 gives an explicit two-cover R_i|(q1,q2,...,qt) versus three-cover R_i|{q1}|Q[2,t], with named smaller-cover crossing q1->q2. Deleting q1 gives the reciprocal three-cover R_i|{q0}|Q[2,t] versus two-cover (q0,R_i)|Q[2,t], with named crossing q0->first(R_i)=q0->y_{i+2}. Thus the transfer is a literal support-switch square carrying two ancestry-current component drops, not merely a chain of reverse shields. Multiple transfers synchronize the q1->q2 drop while rotating the q0->Y crossing.

### 1. Two exact covers of the same singleton residue
Retain one HHH TRANSFER index i and the notation of `fixed-complement-triangle-transfer-double-prefix-push` SV21176. Let

  R_i=(y_{i+2},y_{i+1},M)

be the original retained Hamilton puncture path on Omega-{y_i}; its existence with literal complement Q is part of the anchored fixed-complement packet. Thus

  C_i^0 = R_i | (q_0,q_1,q_2,...,q_t)                  (RS.1)

is an exact two-cover of H-y_i.

SV21176 gives the pushed exact row

  C_i^2 = (q_1,q_0,R_i) | (q_2,q_3,...,q_t).           (RS.2)

A surviving transfer has |Q|>=5, so all displayed q_0,q_1,q_2,q_3 positions are physically present.

### 2. The source transfer reverses one selected physical edge on the same residue
In C_i^0 the ordinary edge {q_0,q_1} is selected in orientation

  q_0 -> q_1,

while in C_i^2 the same physical edge is selected in orientation

  q_1 -> q_0.                                          (RS.3)

This is a literal selected-edge reversal between two exact covers of the SAME proper residue H-y_i. The support partitions differ, so no fixed-support R561 conclusion is inferred.

The endpoint roles swap simultaneously. In C_i^0, q_0 is a source endpoint and q_1 is internal on Q. In C_i^2, q_1 is the source endpoint and q_0 is internal on the pushed rail. Hence accepted R408 applies separately at q_0 and q_1. Its proof mechanism is useful here because the two resulting component drops can be written completely rather than compressed to the abstract balanced-pair conclusion.

### 3. Deleting q_0 exposes the first reciprocal component drop
Delete q_0 from both rows. From C_i^0 one obtains the literal two-cover

  T_0 = R_i | (q_1,q_2,...,q_t)                        (RS.4)

of W_0=H-{y_i,q_0}. It is exact: if W_0 were Hamiltonian, its Hamilton path together with the tight dimer {y_i,q_0} would two-cover H.

Deleting the internal q_0 from C_i^2 splits its active rail and gives the literal three-cover

  F_0 = R_i | {q_1} | (q_2,q_3,...,q_t).               (RS.5)

The selected state of the smaller cover T_0 that visibly joins two F_0-components is the ancestral Q-edge

  q_1 -> q_2.                                          (RS.6)

Thus the R408/R159 component-drop mechanism at q_0 is current with a named physical crossing and the full source ancestry retained.

### 4. Deleting q_1 gives the reciprocal drop
Delete q_1 instead. From the original row C_i^0, where q_1 is internal, one gets the literal three-cover

  F_1 = R_i | {q_0} | (q_2,q_3,...,q_t).               (RS.7)

From the pushed row C_i^2, deleting its source q_1 leaves the literal two-cover

  T_1 = (q_0,R_i) | (q_2,q_3,...,q_t)                  (RS.8)

of W_1=H-{y_i,q_1}. Again exactness follows because the omitted pair {y_i,q_1} is a tight dimer.

The selected T_1 state that joins two F_1-components is exactly the source-transfer edge

  q_0 -> y_{i+2},                                      (RS.9)

where y_{i+2} is the first physical vertex of R_i. This is the reciprocal current crossing to (RS.6).

### 5. The transfer is a support-switch square, not a shield packet
Equations (RS.1)-(RS.9) exhibit one exact square:

  original singleton row C_i^0
       | delete q_0              | delete q_1
       v                         v
  two-cover T_0              three-cover F_1

  pushed singleton row C_i^2
       | delete q_0              | delete q_1
       v                         v
  three-cover F_0            two-cover T_1.

The two vertical comparisons are reciprocal component drops, while the two top-level singleton rows select q_0q_1 in opposite directions. This is stronger source information than the graph-intrinsic balanced pair supplied by R408/R159 after abstraction.

If two distinct triangle labels transfer, the q_0-deletion drops share the identical crossing q_1->q_2 and identical tail rail Q[2,t], while their q_1-deletion drops carry the distinct rotating crossings q_0->y_{i+2}. If all three labels transfer, all three physical Y labels occur as these q_0-source crossings around the same fixed q_0/q_1 reversal square.

The TTT case is the exact terminal dual. No spanning two-cover, fixed-support R561 state, or automatic descent is claimed. The purpose of the square is to expose a stronger reciprocal consumer interface for CBCA before any generic balanced-pair/payment compilation.

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
    }
]
```
