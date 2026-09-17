# The cycle-dimer two-row cylinder has no selected-reversal branch and quiet rows share one break side

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-cycle-dimer-two-row-r435-reduction`

**Summary:** Retain the no-core cycle-dimer singleton output SV30097: H-y=P_x|V and H-x=P_y|V, where P_x is Hamilton on Q+x, P_y on Q+y, x,y are boundary endpoints, Q is one fixed oriented tight cycle support, each P_z retains all Q vertices in one cyclic-break order, V is the same literal complement, and Omega=Q+x+y is non-Hamiltonian. Comparing P_x and P_y by R435, the adjacent selected-state reversal branch is impossible because every common Q-Q edge selected by either path is a rim edge oriented in the same cyclic direction. Hence any nonquiet comparison is reverse-trimer or proper-cycle output, already routed to universal-core/fresh-forest or closed movable-break dynamics. If the comparison is R435-quiet, all common Q vertices occur in one linear order, forcing the two cyclic breaks to be identical. The endpoints x,y cannot lie on opposite sides of that common break, because then their two certified endpoint seams concatenate to a Hamilton path on Omega. Thus the only quiet residue has x and y attached on the same side of the same cyclic break. No closure of that same-side cell is claimed.


### 1. Cycle-derived two-row puncture cylinder
Retain the no-core output of `compatible-forest-cycle-dimer-singleton-to-fixed-complement` SV30097 in a hypothetical smallest Strong Level-(1) counterexample. Thus Q is the support of one fixed oriented tight cycle, V is a literal Hamilton path disjoint from Q,x,y, and

  H-y = P_x | V,
  H-x = P_y | V                                          (CDR.1)

are exact two-covers. Here P_x is Hamiltonian on V(Q) union {x}, P_y is Hamiltonian on V(Q) union {y}, x is a boundary endpoint of P_x, y is a boundary endpoint of P_y, and each P_z contains the Q vertices in the inherited cyclic order with exactly one break. Put

  Omega=V(Q) union {x,y}.

SV30097 retains that Omega is non-Hamiltonian. The literal complement V is identical in both rows.

### 2. Adjacent selected reversal is impossible
Compare the actual Hamilton words P_x and P_y by accepted R435. Their common vertices are exactly V(Q).

Suppose R435 took its adjacent selected-state reversal output. Then some common physical dimer {q_i,q_j} of Q would occur as a selected state in both paths, but in opposite directions.

Because x and y are endpoints, deleting x from P_x and y from P_y leaves cyclic breaks of the same fixed oriented tight cycle Q. Consequently every selected Q-Q state in either path is an actual rim edge of Q, oriented in the fixed cyclic direction. If a rim edge is selected by both breaks, its orientation is therefore identical in both words. It cannot be selected oppositely.

Hence the adjacent selected-state reversal branch of R435 cannot occur.       (CDR.2)

Therefore every R435-nonquiet comparison P_x versus P_y yields only

  reverse seam trimer,
  or proper tight cycle.                                  (CDR.3)

By the current consumers, a reverse trimer exports to a universally one-extendable four-set or a fresh maximum three-forest, while a proper cycle exports to a closed movable-break maximum-three-forest orbit.

### 3. Quietness forces one common cyclic break
Assume instead that P_x and P_y are R435-quiet. Then every common Q-contact of one path occurs in increasing order relative to the other.

Each Q-subword is a cyclic break of the same oriented cycle and contains every Q vertex exactly once. Two cyclic permutations of the same finite cyclic order can be monotone as complete linear orders only when the omitted rim edge is the same. Thus there is one literal break

  R=(r_0,r_1,...,r_{m-1})                                (CDR.4)

of Q such that the Q vertices occur in this exact order in both P_x and P_y.

Since x and y are boundary endpoints, each path has one of the forms

  (x,R) or (R,x),
  (y,R) or (R,y).                                         (CDR.5)

### 4. Opposite-side attachments Hamiltonize the active support
Suppose the attachments in (CDR.5) lie on opposite sides. After possibly swapping x,y, write

  P_x=(x,r_0,...,r_{m-1}),
  P_y=(r_0,...,r_{m-1},y).                               (CDR.6)

The first path certifies its sole new endpoint seam

  (x,r_0,r_1) tight,

and the second certifies

  (r_{m-2},r_{m-1},y) tight.

All internal turns of R are inherited from the tight cycle. Therefore

  (x,r_0,r_1,...,r_{m-1},y)                              (CDR.7)

is a Hamilton tight path on Omega, contradicting the retained non-Hamiltonicity of Omega.

The other opposite-side orientation is identical after exchanging x and y. Thus a quiet survivor must attach both x and y to the SAME side of the SAME cyclic break:

  (R,x) and (R,y),

or

  (x,R) and (y,R).                                        (CDR.8)

### 5. Cycle-dimer residual
The two-row cylinder exported by SV30097 therefore has the exact dichotomy:

1. R435 NONQUIET: selected reversal is impossible; reverse-trimer/proper-cycle output immediately enters the universal-core or actual/closed maximum-three-forest holonomy programs.
2. R435 QUIET: both singleton-producing rows use one common cyclic break and attach x,y on the same end of that break.

No claim is made here that the same-side quiet cell already closes H. The value is cycle-specific elimination of the only R435 species that could recycle into endpoint-endpoint fixed-complement reversal, together with exact synchronization of every quiet survivor to one break and one boundary side.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R435"
    }
]
```
