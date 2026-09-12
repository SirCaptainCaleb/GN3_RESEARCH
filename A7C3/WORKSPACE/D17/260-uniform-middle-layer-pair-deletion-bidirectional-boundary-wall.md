# Every Arm-M pair-deletion frame is already a two-ended bidirectional Morse wall

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-pair-deletion-bidirectional-boundary-wall`

**Summary:** Assume accepted R927 Arm M: |V(H)|=2k+1, every k-set Hamiltonian, no (k+1)-set Hamiltonian. Fix any distinct x,y and any exact two-cover H-{x,y}=A|B supplied by R429. Every rail has order at most k, since any longer tight path contains a contiguous Hamilton (k+1)-subpath; as |A|+|B|=2k-1, after relabelling |A|=k and |B|=k-1. Orient A=(a0,...,a_{k-1}) and restore the deleted pair as either oriented dimer (x,y) or (y,x), both vacuously tight. In the maximum forest A|B|(x,y), any inward endpoint SLIDE into A is impossible because it would create a tight path of order k+1, forbidden by Arm M. Applying the exact SLIDE/double dichotomy SV22098 to the four inward gates therefore forces the reverse boundary contacts rather than slides. From orientation (x,y), x head-signs the reverse terminal dimer (a_{k-1},a_{k-2}) and y tail-signs the reverse initial dimer (a1,a0); reversing the free deleted dimer swaps x,y and forces the complementary two contacts. Hence BOTH deleted vertices head-sign the reverse terminal dimer and BOTH tail-sign the reverse initial dimer. The source and terminal endpoints of B additionally give a third head and third tail witness respectively. Thus every exact pair-deletion frame in Arm M is already a terminal largest-rail Morse state carrying a common two-probe bidirectional reverse wall; no greedy SLIDE phase is needed in the uniform arm.

### 1. Arbitrary pair deletion in Arm M
Assume accepted R927 alternative (M):

  |V(H)|=2k+1,
  every k-set is Hamiltonian,
  no (k+1)-set is Hamiltonian.                            (PW.1)

Fix arbitrary distinct physical vertices x,y. Accepted Pair-Deletion Rigidity R429 gives an exact two-cover

  H-{x,y}=A|B.                                            (PW.2)

No rail of (PW.2) can have more than k vertices. Indeed, a tight path of order at least k+1 contains a contiguous tight subpath of order exactly k+1, Hamiltonizing its support and contradicting (PW.1).

Since

  |A|+|B|=2k-1,                                          (PW.3)

the two positive rail orders are therefore exactly k and k-1. Relabel so

  A=(a_0,a_1,...,a_{k-1}),
  |A|=k, |B|=k-1.                                        (PW.4)

Write B=(b_0,...,b_{k-2}).

### 2. Restore the deleted pair as a free oriented dimer
Every oriented two-vertex word is vacuously a tight path. Hence both

  C_xy=(x,y),
  C_yx=(y,x)                                              (PW.5)

are literal tight dimers. Consequently

  A|B|C_xy

and

  A|B|C_yx                                                (PW.6)

are literal spanning three-path covers. Since H is a smallest counterexample and pc(H)=3 by R4, they are maximum three-forest states.

The key point is that A already has the maximum Arm-M path order k. Any inward one-vertex SLIDE into A would create a tight path of order k+1 and is therefore impossible.

### 3. The B endpoints already sign the two reverse boundary dimers
Consider the ordered merge seed from the terminal a_{k-1} of A to the source b_0 of B. Its A-side seam is

  alpha_B=(a_{k-2},a_{k-1},b_0).                         (PW.7)

If alpha_B were tight, then because the complete merge cannot give a spanning two-cover, the other seam would be bad and the exact one-hole SLIDE of SV22098 would move b_0 into A, producing a literal tight path

  (A,b_0)

of order k+1. This contradicts (PW.1). Hence alpha_B is bad, and R3 gives

  (b_0,a_{k-1},a_{k-2}) tight.                            (PW.8)

Thus b_0 head-signs the tested reverse terminal dimer

  D_R=(a_{k-1},a_{k-2}).                                 (PW.9)

Dually use the merge seed from the terminal b_{k-2} of B into the source a_0 of A. If its A-side seam

  (b_{k-2},a_0,a_1)

were tight, the corresponding one-hole SLIDE would prepend b_{k-2} to A and again create an order-(k+1) tight path. Therefore it is bad and R3 gives

  (a_1,a_0,b_{k-2}) tight.                               (PW.10)

So b_{k-2} tail-signs the reverse initial dimer

  D_L=(a_1,a_0).                                         (PW.11)

### 4. One dimer orientation signs one deleted vertex at each end
Now use the restored dimer C_xy=(x,y).

For the merge seed A -> C_xy, the A-side seam is

  (a_{k-2},a_{k-1},x).                                   (PW.12)

If it were tight, the other native seam must be bad and SV22098 would slide x into A, creating the forbidden order-(k+1) path (A,x). Hence (PW.12) is bad, so R3 gives

  (x,a_{k-1},a_{k-2}) tight.                              (PW.13)

Thus x head-signs D_R.

For the opposite ordered seed C_xy -> A, the A-side seam is

  (y,a_0,a_1).                                           (PW.14)

If tight, the dual SLIDE would move y into the head of A, again producing an order-(k+1) tight path. Thus it is bad and

  (a_1,a_0,y) tight.                                     (PW.15)

Hence y tail-signs D_L.

### 5. Reverse the free dimer and obtain the complementary contacts
Repeat Section 4 with the equally literal dimer C_yx=(y,x). The same no-(k+1)-path argument gives

  (y,a_{k-1},a_{k-2}) tight,
  (a_1,a_0,x) tight.                                     (PW.16)

Combining (PW.13),(PW.15),(PW.16), BOTH deleted vertices satisfy

  (x,D_R), (y,D_R) tight in head position,
  (D_L,x), (D_L,y) tight in tail position.               (PW.17)

Equivalently:

  D_R is head-signed by both x and y,
  D_L is tail-signed by both x and y.                     (PW.18)

Together with (PW.8),(PW.10), D_R actually has the three distinct head witnesses

  {x,y,b_0},                                              (PW.19)

and D_L has the three distinct tail witnesses

  {x,y,b_{k-2}}.                                         (PW.20)

### 6. Uniform-arm Morse consequence
The pair x,y and the exact pair-deletion cover (PW.2) were arbitrary. Therefore EVERY exact pair-deletion frame in Arm M has a k-rail whose two reverse boundary dimers carry the same deleted pair as a common two-probe witness set, with a third witness supplied by the opposite rail at each end.

Thus the Arm-M uniform layer does not merely admit a greedy path to a largest-rail Morse critical point. Every pair-deletion frame is already critical for the largest-rail height: all four inward gates from the other k-1 rail and the restored deleted dimer into the k-rail are blocked, and exact reversal records those blocks as the bidirectional wall (PW.18).

This theorem does not yet close Arm M. Its gain is a universal physical starting object for the next consumer: one common pair of probes signs opposite-polarity reverse dimers at both ends of every k-rail arising from pair deletion. No payment descendant or representative synchronization across different pair deletions is asserted.

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
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    },
    {
        "relation": "dependency",
        "revision_id": "R927"
    }
]
```