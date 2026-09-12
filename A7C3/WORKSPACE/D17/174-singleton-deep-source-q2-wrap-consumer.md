# The source-q2 failed-rho residue rotates back to the q2 gate or is P4-valued

**Workspace:** D17
**State:** established
**Key:** `singleton-deep-source-q2-wrap-consumer`

**Summary:** The sole bare ancestral-reversal residue had q2 as the source of its exact complement rail and rho=(q1,q2,z) bad. A dimer rail reverses freely and moves q2 terminal. For longer rails, R579 wrap success moves q2 off the source and immediately returns to the existing q2 insertion gate; double wrap failure gives a reverse P4 for order at least four. The only exceptional trimer double-fail cell is forced, if P4-free, to exact R516 signature 11. Its forced turns together with the inherited q0q1q2 source turn and q1q0d shield give a labelled P4 in all cases, including the possible overlaps z=q0 or w=q0. Thus no bare ancestral q1q2 reversal remains.


Retain the current q2 front after both eta tests pass. Let T be an exact complement two-cover and suppose q_2 is the SOURCE of its actual T-rail

  R=(q_2,z,r_2,...,r_m),                                  (SQ.1)

with successor z. Assume the sole right insertion seam

  rho=(q_1,q_2,z)                                         (SQ.2)

is bad, so R3 gives the retained reverse trimer

  (z,q_2,q_1) tight.                                      (SQ.3)

This is the sole bare ancestral-reversal cell left by `singleton-deep-ancestral-reversal-amplification`.

### 1. Dimer rail: free reversal moves q2 off the source
If R=(q_2,z) is a dimer, reverse it freely to (z,q_2). The same exact complement residue now has q_2 terminal. If z lies in S, its immediate predecessor is an S-contact occurring before the first ancestral coordinate q_2, so accepted R435/P448 is active. If z lies in C, this is exactly the C-predecessor q2 insertion cell with no right seam rho. Thus the dimer source-rho residue immediately returns to the already-consumed q2 gate.

### 2. Rails of order at least four: R579 gives a new q2 position or a P4
Assume |R|>=4. Apply accepted R579 to the actual Hamilton path R. Its two wrap seams are

  alpha=(r_m,q_2,z),
  beta=(r_{m-1},r_m,q_2).                                (SQ.4)

If alpha is tight, the head rotation

  (r_m,q_2,z,r_2,...,r_{m-1})                            (SQ.5)

is Hamiltonian on the same support and moves q_2 off the source. If beta is tight, the tail rotation

  (z,r_2,...,r_m,q_2)                                    (SQ.6)

is Hamiltonian and makes q_2 terminal. In either successful-wrap branch, immediately re-enter the q2 local insertion theorem on this actual new representative; the move itself is not called descent.

If both alpha and beta are bad, R579's double-fail branch for |R|>=4 gives the literal reverse-wrap P4

  (z,q_2,r_m,r_{m-1}).                                   (SQ.7)

Thus no long source-q2 failed-rho residue survives.

### 3. The only short wrap exception is a trimer, and its double-fail cell is rigid
Let

  R=(q_2,z,w).                                             (SQ.8)

If either wrap alpha=(w,q_2,z) or beta=(z,w,q_2) is tight, the corresponding R579 rotation moves q_2 off the source as above and returns to the q2 gate. Assume both wraps are bad. Then R3 gives

  (z,q_2,w), (q_2,w,z) tight,                              (SQ.9)

while the original T turn

  (q_2,z,w) tight                                         (SQ.10)

remains selected.

Consider the four-set F={z,q_2,q_1,w}. If F has a Hamilton P4, retain it. Assume F is P4-free. Apply accepted R516 to the base trimer

  (a,b,c)=(z,q_2,q_1)

from (SQ.3), with fourth vertex w. The known turn (z,q_2,w) gives alignment bit A=1. Among the A=1 no-P4 rows, the known turn (q_2,w,z) is present only in exact signature 11 (signature 10 contains its complete reverse (z,w,q_2)). Therefore F is exactly the R516-11 cell. In particular it forces

  (q_1,z,w), (z,q_1,q_2), (w,q_1,z) tight,                (SQ.11)

with the listed turns used below according to overlaps.

### 4. The signature-11 trimer cell always emits a P4, including q0 overlaps
Recall the inherited source turn and source shield

  (q_0,q_1,q_2), (q_1,q_0,d) tight.                       (SQ.12)

There are three possibilities.

**Generic: q_0 is distinct from z,w.** Test theta=(q_0,q_1,z). If theta is tight, combine it with (q_1,z,w) from (SQ.11):

  (q_0,q_1,z,w)                                           (SQ.13)

is a literal P4. If theta is bad, R3 gives (z,q_1,q_0), which combines with (q_1,q_0,d) to give

  (z,q_1,q_0,d).                                          (SQ.14)

**Overlap z=q_0.** Signature 11 gives (w,q_1,z)=(w,q_1,q_0). Together with (q_1,q_0,d),

  (w,q_1,q_0,d)                                           (SQ.15)

is a literal P4.

**Overlap w=q_0.** Signature 11 gives both

  (q_0,q_1,z), (z,q_1,q_2) tight.                         (SQ.16)

Test xi=(q_1,z,d). If xi is tight, (q_0,q_1,z,d) is a P4. If xi is bad, R3 gives (d,z,q_1), which combines with (z,q_1,q_2) to give

  (d,z,q_1,q_2).                                          (SQ.17)

Thus the trimer double-wrap-failure cell is always P4-valued.

### 5. Exact conclusion
The source-q2 failed-rho residue has no independent terminal state. A free dimer reversal or any successful R579 wrap moves q_2 off the source and returns to the already-consumed q2 insertion geometry; double wrap failure gives a labelled P4 directly for every rail order at least four, and the unique trimer exception is P4-valued by the exact R516-11 argument above.

Hence after this consumer there is no bare q1q2-reversal branch anywhere in the q2 insertion front. The remaining nonclosing outputs are R435 geometry, labelled P4s, or H-t rows whose source transport terminates in closure or a named wrap shield. This is established working exposition, not a certified exact unit.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R516"
    },
    {
        "relation": "dependency",
        "revision_id": "R579"
    }
]
```
