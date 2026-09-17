# A bad fixed-complement singleton row lifts to phase one before any pair payment

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-bad-singleton-prepayment-phase-lift`

**Summary:** Let V(H)=Omega disjoint_union Q with Q a literal Hamilton path and let y be a bad singleton label. If some good label d has an actual fixed-complement row H-d=P_d|Q and an exact bad row C_y of H-y selects any Omega|Q state, then before any R176/R428 payment the two restored singleton rows already expose a proper tight trimer whose two physical edges are exactly the bad-row crossing and one adjacent selected Q-edge. Boundary antisymmetry gives the direct seam trimer or its complete reverse. Both source rows are literal phase-1 maximum three-covers. Relative to the lower-rank of those two birth checkpoints, SV52939 therefore gives a finite certificate-retaining continuation to a spanning two-cover or phased rank strictly below both source checkpoints. Thus a fixed-complement bad singleton with even one good puncture is phase-rank unstable; the SV66139 four-root common-center star is unnecessary for phase lifting, though it remains useful for the global anchor budget. No R24/R5 is used.


### 1. Fixed-complement bad/good source packet
Let H be a hypothetical smallest Strong Level-(1) counterexample. Retain

  V(H)=Omega disjoint_union V(Q),
  Q=(q_0,q_1,...,q_m),

with Q a literal Hamilton tight path and Omega non-Hamiltonian. Let y in Omega be BAD, so Omega-y is non-Hamiltonian, and let d in Omega-{y} be GOOD, so Omega-d is Hamiltonian.

Choose an actual Hamilton puncture path P_d on Omega-d. Since Q is Hamiltonian, the literal row

  C_d=P_d|Q                                               (PL.1)

covers H-d. It is exact: if H-d were Hamiltonian, adjoining singleton d would two-cover H. Likewise choose any literal exact two-cover

  C_y=A|B                                                 (PL.2)

of H-y. Restoring the deleted labels gives two literal spanning minimum three-covers

  F_d={d}|P_d|Q,
  F_y={y}|A|B.                                            (PL.3)

Both are legitimate phase-1 checkpoints for the SV41376 phased rank.

The fixed Q-rail has order at least three. Indeed, if |Q|=1 then Q+d is a dimer and (Q+d)|P_d two-covers H. If |Q|=2, boundary antisymmetry R3 gives a tight trimer on V(Q) union {d}, again pairing with P_d to two-cover H. Hence

  |Q|>=3.                                                 (PL.4)

### 2. A bad row must physically cross the fixed cut
The bad row C_y cannot have support partition

  (Omega-y)|Q.                                            (PL.5)

Otherwise its Omega-side rail would Hamiltonize Omega-y, contradicting badness. If no selected C_y state crossed Omega|Q, each C_y rail would be cut-pure. With exactly two nonempty rails covering both sides, their supports would necessarily be exactly Omega-y and Q, again contradicting (PL.5).

Therefore retain one actual selected directed state of C_y with physical endpoints

  {o,q},   o in Omega-y,   q in V(Q).                     (PL.6)

Its direction is whichever orientation is selected in the displayed bad-row path. This is a CURRENT physical state of F_y.

### 3. The crossing and one Q-edge force a prepayment trimer
Choose either literal Q-neighbor p of q; such a neighbor exists by (PL.4). Retain the actual selected Q-edge {p,q} from F_d. The two physical selected states from the two phase-1 source rows meet at q:

  bad-row edge {o,q} from F_y,
  fixed-complement edge {p,q} from F_d.                   (PL.7)

Apply boundary antisymmetry R3 to the three distinct vertices o,q,p. Exactly one of the complete-reversal turns

  (o,q,p),   (p,q,o)                                      (PL.8)

is tight. Let J be that literal tight trimer.

This is not an arbitrary trimer chosen elsewhere in H. Its two ordinary edges are exactly the two retained physical source states in (PL.7). If their displayed directions concatenate through q, J is either that direct two-state seam or its exact complete-reversal contact. If their displayed directions point to the same side of q, J is the corresponding same-end reverse-contact trimer. In every case its birth certificate consists of the current bad-row crossing, the literal Q-edge from the good row, their common physical endpoint q, and the one R3 comparison. No R176 pair birth, R428 payment, floor steering, or completed-anchor return has occurred.

Thus the fixed-complement bad/good packet has already produced a graph-intrinsic proper tight path

  J on {o,q,p}                                             (PL.9)

at phase one.

### 4. Rank comparison: choose the better source checkpoint
For a literal maximum three-cover F, write M(F) for the order of its largest rail and

  Phi(F)=(1,n-M(F))                                       (PL.10)

for its phase-1 rank prefix. Put

  M_* = max(M(F_y),M(F_d)),

and choose F_* from {F_y,F_d} with M(F_*)=M_*. Then

  Phi(F_*) <= Phi(F_y), Phi(F_d).                         (PL.11)

The trimer J was born from the retained two-checkpoint packet before either source left phase one; in particular its exact birth ancestry includes F_* and the other source representative. The proof of SV52939 uses only the retained phase-1 birth height M_* after the proper path has been exposed. Apply that proof verbatim to J with birth threshold M_*: currentize J by accepted minimality R4, mark a largest rail of the resulting maximum forest, and run the SV40879 largest-rail continuation. One obtains either

  TWO-COVER,                                               (PL.12)

or a forest/pair state F' with

  phased-rank(F') < Phi(F_*).                              (PL.13)

Combining with (PL.11), every nonclosing continuation satisfies

  phased-rank(F') < Phi(F_y)
  and
  phased-rank(F') < Phi(F_d).                             (PL.14)

Thus the phase lift is strict relative to BOTH literal singleton source covers, not merely relative to an auxiliary currentization.

### 5. G25 consequence: bad-singleton fixed-complement shells are phase-rank unstable
Suppose a reconstruction-closed family of minimum three-covers is chosen minimal for the legitimate SV41376 phased rank and contains the fixed-complement source packet above. Then (PL.12)-(PL.14) contradict nonclosing rank minimality.

Hence a nonclosing phase-rank-minimal family cannot contain a bad singleton row crossing a fixed Hamilton complement together with even one good puncture row on that same complement.

In particular every G24/G25 shell with at least five good roots is already extinguished before the SV66139 common-center star is paid. The common-center theorem remains valuable for epsilon_* and historical anchor control in settings where one deliberately follows the pair-payment branch, but it is not needed to obtain the requested PHASE-LIFT in the fixed-complement bad-singleton setting.

This is the exact architectural distinction emphasized by G25: the current good-bad pair kernel is not consumed after payment. Its source crossing is lifted backward to a proper path born at an actual phase-1 minimum-cover checkpoint, where SV52939 supplies strict descent.

### 6. Scope fence
The theorem requires one literal fixed Hamilton complement Q that appears as a rail of the good singleton row and one actual selected Omega|Q state in the bad singleton row. It does not claim that an arbitrary current pair-deletion portal lacking such source ancestry phase-lifts. It does not identify unrelated threshold boxes, and it does not use R24 or R5.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R4"
    }
]
```