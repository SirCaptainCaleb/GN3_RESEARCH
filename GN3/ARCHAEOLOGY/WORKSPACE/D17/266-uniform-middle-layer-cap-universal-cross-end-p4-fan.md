# Every Arm-M cap has a universal cross-end P4 fan or an internal cross-end P4

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-cap-universal-cross-end-p4-fan`

**Summary:** A pure R3 seam lemma says that disjoint opposite-polarity signed dimers with one common witness always force a literal tight P4. Applied to the two reverse boundary dimers of a fixed Hamilton complement Q in a deletion-Hamiltonian critical block, the two seam tests are independent of the deleted critical vertex. Hence for |Q|>=4 one of three structural outcomes holds: every critical vertex prepends one fixed cross-end trimer to a P4; or every critical vertex appends to another fixed cross-end trimer; or Q itself contains a fixed cross-end P4 joining its first and last boundary dimers. In accepted R927 Arm M every k-path Q has a deletion-Hamiltonian (k+1)-vertex complement, so every literal cap representative satisfies this universal cross-end P4 trichotomy. No curvature payment or closure is claimed.


### 1. Pure common-witness opposite-dimer P4 lemma
Let

  H=(h_0,h_1)

be a head-signed dimer with sign witness y, so

  (y,h_0,h_1)                                             (CF.1)

is tight. Let

  T=(t_0,t_1)

be a physically disjoint tail-signed dimer with the SAME witness y, so

  (t_0,t_1,y)                                             (CF.2)

is tight. Assume the five displayed vertices are distinct.

Test the bridge turn

  L=(h_0,h_1,t_0).                                        (CF.3)

If L is tight, then (CF.1) and (CF.3) give the literal tight P4

  (y,h_0,h_1,t_0).                                        (CF.4)

Suppose L is bad. Boundary antisymmetry R3 gives

  (t_0,h_1,h_0)                                           (CF.5)

as a tight turn. Now test

  R=(h_1,t_0,t_1).                                        (CF.6)

If R is tight, then (CF.6) and (CF.2) give the literal tight P4

  (h_1,t_0,t_1,y).                                        (CF.7)

If R is bad, R3 gives

  (t_1,t_0,h_1)                                           (CF.8)

and (CF.8),(CF.5) concatenate to the literal tight P4

  (t_1,t_0,h_1,h_0).                                      (CF.9)

Thus two disjoint opposite-polarity signed dimers sharing one sign witness cannot remain a bare balanced-pair packet: before any payment or recompletion they already contain a literal tight P4.

### 2. Fixed-complement critical blocks have a two-ended universal wall
Now let H be a hypothetical smallest counterexample with a fixed-complement critical-block split

  V(H)=Omega disjoint_union V(Q),
  Q=(q_0,q_1,...,q_m),                                    (CF.10)

where Omega is non-Hamiltonian but deletion-Hamiltonian and Q is a literal Hamilton tight path. Assume |Q|=m+1>=4.

Fix y in Omega and choose any Hamilton puncture path P_y on Omega-y. If

  (y,q_0,q_1)                                             (CF.11)

were tight, then (y,q_0,...,q_m) together with P_y would be a spanning two-cover of H. Hence (CF.11) is bad, and R3 gives

  (q_1,q_0,y)                                             (CF.12)

for every y in Omega. Dually, if (q_{m-1},q_m,y) were tight, Q followed by y would pair with P_y to two-cover H. Hence

  (y,q_m,q_{m-1})                                         (CF.13)

is tight for every y in Omega.

Therefore the reverse source dimer

  T_Q=(q_1,q_0)

is tail-signed by EVERY y in Omega, while the reverse terminal dimer

  H_Q=(q_m,q_{m-1})

is head-signed by EVERY y in Omega. The two dimer supports are disjoint because |Q|>=4.

### 3. The two seam tests are y-independent
Apply the pure lemma above to H_Q and T_Q, but retain its two tests before choosing y. They are

  alpha=(q_m,q_{m-1},q_1),                                (CF.14)
  beta =(q_{m-1},q_1,q_0).                                (CF.15)

Both depend only on the literal cap order Q, not on y. Consequently one of the following three alternatives holds.

**FAN-HEAD.** If alpha is tight, then for EVERY y in Omega, (CF.13) and alpha give

  (y,q_m,q_{m-1},q_1)                                    (CF.16)

as a literal tight P4. Thus the fixed trimer (q_m,q_{m-1},q_1) is Hamilton-prepended by every critical-block vertex.

**FAN-TAIL.** Suppose alpha is bad but beta is tight. R3 reverses alpha to

  (q_1,q_{m-1},q_m).                                      (CF.17)

Independently, beta together with the universal tail sign (CF.12) gives, for EVERY y in Omega,

  (q_{m-1},q_1,q_0,y)                                    (CF.18)

as a literal tight P4. Thus the fixed trimer (q_{m-1},q_1,q_0) is Hamilton-appended by every critical-block vertex.

**INTERNAL-BRIDGE.** If both alpha and beta are bad, R3 gives both (CF.17) and

  (q_0,q_1,q_{m-1}).                                      (CF.19)

These concatenate to the cap-internal cross-end P4

  (q_0,q_1,q_{m-1},q_m).                                  (CF.20)

Hence the full family of vertexwise common-witness P4s synchronizes to one of two universal exterior P4 fans, unless Q itself already contains a fixed P4 joining its first and last boundary dimers.

### 4. Arm-M specialization
Assume accepted R927 alternative (M):

  |V(H)|=2k+1,
  every k-set is Hamiltonian,
  no (k+1)-set is Hamiltonian.                            (CF.21)

Take ANY literal Hamilton k-path

  Q=(q_0,...,q_{k-1})

on ANY k-support X. Put Omega=V(H)-X, so |Omega|=k+1. By (CF.21), Omega is non-Hamiltonian. For every y in Omega, Omega-y is a k-set and therefore Hamiltonian. Thus Omega is deletion-Hamiltonian and (CF.10) is a fixed-complement critical-block split. In the live Arm-M range k>=5, certainly |Q|>=4, so Sections 2-3 apply verbatim.

Therefore EVERY literal Arm-M cap representative Q satisfies the uniform trichotomy:

1. every exterior y gives (y,q_{k-1},q_{k-2},q_1); or
2. every exterior y gives (q_{k-2},q_1,q_0,y); or
3. Q contains (q_0,q_1,q_{k-2},q_{k-1}).                 (CF.22)

All words in (CF.22) are literal tight P4s.

### 5. Research consequence and scope
The cap layer is therefore more rigid than the R966 curvature picture alone suggests. Once a literal cap order is fixed, its entire exterior does not generate unrelated local P4 outputs: two cap-internal seam bits synchronize all exterior labels into one universal cross-end P4 fan, unless those same seam failures create a fixed internal cross-end P4.

This is a graph-intrinsic current portal theorem, not a closure theorem. It does not assert that the P4 fan itself Hamilton-extends to a universal four-core, that the P4s share an exact deletion representative, or that currentizing one of them by smallest-counterexample minimality strictly decreases a global Morse height. Those are the next consumers.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R927"
    }
]
```