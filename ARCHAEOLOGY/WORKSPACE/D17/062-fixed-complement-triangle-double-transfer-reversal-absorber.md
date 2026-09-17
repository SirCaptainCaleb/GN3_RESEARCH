# Two anchored transfers force a same-support reversal absorber or a named cyclic seam obstruction

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-triangle-double-transfer-reversal-absorber`

**Summary:** Assume two distinct HHH triangle labels transfer through q0. Cyclically choose i so that both y_i and y_{i+2} transfer. Any transferred label z forces (q0,q1,z) tight, since the opposite turn (z,q1,q0) would prepend z to its pushed exact H-z row and, with common complement Q[2,t], two-cover H. Hence q0,q1,y_{i+2} is tight. The candidate (q0,q1,y_{i+2},y_{i+1},M) on the same active support as the pushed path (q1,q0,y_{i+2},y_{i+1},M) has exactly one remaining seam h_i=(q1,y_{i+2},y_{i+1}). If h_i is bad, R3 gives the named cyclic obstruction (y_{i+1},y_{i+2},q1). If h_i is tight, the two exact H-y_i covers have identical support partition and common complement Q[2,t] while selecting q0q1 oppositely. Repeated one-seam head rotations of the reverse-order active path either hit a named reverse-wrap shield or move q1q0 to the terminal boundary; in the latter case accepted R561 makes the active support universally one-vertex extendable, so restoring y_i closes H while retaining Q[2,t]. Thus two transfers are reduced to closure, one explicit cyclic seam obstruction, or one ancestry-preserving wrap blocker. With three transfers, absence of a same-support reversal candidate forces all three cyclic turns (y_{i+1},y_{i+2},q1) tight.

### 1. A transferred label forces the forward q_0q_1 boundary turn
Retain the HHH anchored critical-block packet and the exact pushed rows of `fixed-complement-triangle-transfer-double-prefix-push` SV21176. If a triangle label z transfers, its pushed row has active Hamilton path

  (q_1,q_0,R_z)

on (Omega-{z}) union {q_0,q_1}, with literal Hamilton complement Q^{(2)}=Q[2,t].

If

  (z,q_1,q_0)                                           (DA.1)

were tight, prepend z to that active path. The only new turn is (DA.1), so the resulting path would Hamiltonize

  Omega union {q_0,q_1}.

Together with Q^{(2)} this would be a spanning two-cover of H. Therefore (DA.1) is bad and R3 forces

  (q_0,q_1,z) tight                                     (DA.2)

for every transferred label z.

### 2. Two transfers create a one-hole same-support reversal candidate
Assume two distinct triangle labels transfer. Because the indices are cyclic modulo three, choose i so that both y_i and y_{i+2} are transferred.

Let

  R_i=(y_{i+2},y_{i+1},M)

be the retained Hamilton puncture path on Omega-{y_i}. The pushed exact H-y_i row from SV21176 is

  P_i^-=(q_1,q_0,y_{i+2},y_{i+1},M) | Q^{(2)}.          (DA.3)

Since y_{i+2} also transfers, (DA.2) gives

  (q_0,q_1,y_{i+2}) tight.                              (DA.4)

Now test

  h_i=(q_1,y_{i+2},y_{i+1}).                            (DA.5)

If h_i is tight, then

  P_i^+=(q_0,q_1,y_{i+2},y_{i+1},M)                    (DA.6)

is Hamiltonian on exactly the same active support as P_i^-: (DA.4) certifies its first new turn, (DA.5) the second, and every later turn is inherited from R_i. Therefore

  P_i^+ | Q^{(2)},    P_i^- | Q^{(2)}                  (DA.7)

are two literal exact covers of the SAME singleton residue H-y_i, with the SAME support partition and SAME literal complement, selecting the physical dimer {q_0,q_1} in opposite directions.

If h_i is bad, R3 gives the exact cyclic obstruction

  (y_{i+1},y_{i+2},q_1) tight.                          (DA.8)

Thus two transfers already force either (DA.8) or a genuine fixed-support selected reversal.

### 3. The fixed-support reversal is an almost-absorber
Assume the same-support branch (DA.7). The forward representative P_i^+ begins with (q_0,q_1). The reverse representative P_i^- begins with (q_1,q_0).

Starting from P_i^-, repeatedly perform the head rotation that moves its final vertex to the front. At each step the current Hamilton path has the same physical support, still selects the adjacent state q_1->q_0, and the rotation changes exactly one wrap turn. If that one turn is tight, the rotated order is again Hamiltonian and the selected q_1q_0 dimer moves one position toward the terminal boundary. This is the one-sided transport mechanism of accepted R548, reconstructed directly from its single-wrap-seam proof.

If a required head-rotation seam is bad, stop at the first failure. R3 supplies its complete reverse turn, a named reverse-wrap shield attached to the current active representative. The common complement Q^{(2)}, the omitted label y_i, and the physical q_0q_1 reversal remain current.

If no such failure occurs, finitely many rotations put q_1q_0 at the terminal boundary of a Hamilton path P_i^{end} on the same active support. Then P_i^+ begins with q_0q_1 while P_i^{end} ends with q_1q_0. Accepted R561 applies with X=V(P_i^+), u=q_0, v=q_1. Its proof says that for the exterior vertex y_i exactly one of

  (y_i,q_0,q_1),    (q_1,q_0,y_i)

is tight, and the corresponding boundary attachment extends one of the two Hamilton representatives to a Hamilton path on X+{y_i}. Hence Omega+{q_0,q_1} is Hamiltonian. Retaining Q^{(2)} gives a spanning two-cover of H, contradiction.

Therefore the same-support branch has only two outcomes:

  closure of H through R561,
  or a first named reverse-wrap shield encountered while transporting q_1q_0 to the terminal boundary.          (DA.9)

### 4. Three-transfer compression
If all three triangle labels transfer, the construction of Section 2 is available for every cyclic i. Hence either one h_i is tight and the corresponding fixed-support reversal enters (DA.9), or all three h_i are bad and R3 gives the full cyclic q_1 obstruction fan

  (y_{i+1},y_{i+2},q_1) tight for every i mod 3.        (DA.10)

This full fan is a physical three-turn object attached to the actual Q-boundary vertex q_1, not generic signed-dimer currency.

The exact TTT dual holds at the terminal end of Q. No claim is made that the wrap-shield or full-fan residues are already contradictory. The theorem-scale gain is that two simultaneous complementary transfers cannot remain an amorphous collection of support moves: they either create a fixed-support R561 route or collapse to one explicitly located boundary obstruction.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R548"
    },
    {
        "relation": "dependency",
        "revision_id": "R561"
    }
]
```
