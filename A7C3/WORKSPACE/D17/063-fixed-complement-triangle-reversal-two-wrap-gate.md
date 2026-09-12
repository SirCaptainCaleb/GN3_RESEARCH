# The anchored same-support reversal has only two genuine wrap gates before R561 closure

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-triangle-reversal-two-wrap-gate`

**Summary:** In the same-support branch of SV21962, write the reverse-order active path as P^-=(q1,q0,a,b,m0,...,mr), where (a,b,M)=R_i and |M|>=3. Moving q1q0 from the source to the terminal boundary by repeated head rotations has only two genuinely new seam tests: (mr,q1,q0), then (m_{r-1},mr,q1). Once both pass, every further rotation through M tests an inherited consecutive M-turn; moving b across the front tests (b,m0,m1), universally tight from the anchored M-wall; moving a next tests (a,b,m0), inherited from R_i. Thus q1q0 reaches the terminal boundary, while the forward representative starts q0q1, and accepted R561 restores the omitted y_i and closes H with the common Q[2,t] complement. Consequently any nonclosing same-support branch is trapped by exactly one of two common terminal blockers: (mr,q1,q0) bad, giving (q0,q1,mr), or after that succeeds, (m_{r-1},mr,q1) bad, giving (q1,mr,m_{r-1}). These blockers are independent of the transfer index and collapse the generic wrap-shield family to a two-bit physical gate.

### 1. Anchored same-support reversal coordinates
Retain the same-support branch of `fixed-complement-triangle-double-transfer-reversal-absorber` SV21962. For one transfer index i write

  R_i=(a,b,m_0,m_1,...,m_r)

where {a,b}=Y-{y_i} in the exact anchored order. The fixed-complement triangle packet gives |M|>=3, so r>=2. We have two Hamilton paths on the same active support X_i:

  P^+=(q_0,q_1,a,b,m_0,...,m_r),                       (WG.1)
  P^-=(q_1,q_0,a,b,m_0,...,m_r),                       (WG.2)

and both pair with the identical literal Hamilton complement

  Q^{(2)}=(q_2,...,q_t)

in exact two-covers of H-y_i. The path P^+ begins with q_0q_1. It remains only to move the selected reverse dimer q_1q_0 in P^- to the terminal boundary.

### 2. Only the first two head rotations are genuinely new
Perform successive head rotations, each time moving the current final vertex to the front.

The first rotation of P^- moves m_r to the front. Its unique new seam is

  g_0=(m_r,q_1,q_0).                                    (WG.3)

If g_0 is bad, stop. R3 gives the exact blocker

  (q_0,q_1,m_r) tight.                                  (WG.4)

Assume g_0 is tight. The first rotation is Hamiltonian. The second head rotation moves m_{r-1} to the front and has unique new seam

  g_1=(m_{r-1},m_r,q_1).                                (WG.5)

If g_1 is bad, stop. R3 gives

  (q_1,m_r,m_{r-1}) tight.                              (WG.6)

Assume g_1 is tight as well.

Now every further rotation that moves m_j to the front, for j=r-2,r-3,...,0, tests exactly the inherited consecutive M-turn

  (m_j,m_{j+1},m_{j+2}),                                (WG.7)

which is tight because M is the retained literal Hamilton path. Hence all remaining M-rotations succeed automatically. After them the current Hamilton order is

  (m_0,m_1,...,m_r,q_1,q_0,a,b).                       (WG.8)

### 3. The two Y-rotations are already certified
Move b from the terminal position to the front. The only new seam is

  (b,m_0,m_1),                                          (WG.9)

which is tight by the anchored quiet-R961 M-boundary wall: every y in Y satisfies (y,m_0,m_1).

The resulting path is

  (b,m_0,...,m_r,q_1,q_0,a).

Move a next. Its only new seam is

  (a,b,m_0),                                            (WG.10)

which is inherited from the original puncture path R_i=(a,b,M). Therefore this rotation also succeeds. The final Hamilton order is

  P^{end}=(a,b,m_0,...,m_r,q_1,q_0).                   (WG.11)

Thus P^{end} ends with q_1q_0, while P^+ in (WG.1) begins with q_0q_1.

### 4. Passing both gates closes H
Accepted R561 now applies on the common active support X_i with u=q_0 and v=q_1. Its exact-reversal proof makes every exterior vertex Hamilton-extend X_i. In particular the omitted singleton y_i extends X_i to a Hamilton path on

  X_i+{y_i}=Omega union {q_0,q_1}.

The untouched Q^{(2)} is Hamiltonian and disjoint, so this extension together with Q^{(2)} is a spanning two-cover of H, contradiction.

Therefore a surviving same-support reversal branch cannot have both g_0 and g_1 tight. It has the exact two-gate alternative

  (m_r,q_1,q_0) bad, giving (q_0,q_1,m_r) tight;        (WG.A)

or

  (m_r,q_1,q_0) tight and (m_{r-1},m_r,q_1) bad,
  giving (q_1,m_r,m_{r-1}) tight.                       (WG.B)

These are the ONLY wrap blockers needed for this anchored geometry.

### 5. Synchronization across transfer labels
The gates (WG.3) and (WG.5) depend only on the common literal M-tail and q_0,q_1. They are independent of the transfer index i and of the two Y labels occupying a,b. Hence if several transfer pairs produce same-support reversal candidates, all of them encounter the same two-bit terminal gate. There is no separate long wrap-obstruction family for each label.

The TTT packet has the exact order-dual statement at the opposite end of M and Q. This section does not eliminate the two blockers. It compresses the selected-reversal residue to two named physical turns while preserving the exact singleton fiber, common complement, reversed q_0q_1 state, and the omitted triangle label.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R561"
    }
]
```
