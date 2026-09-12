# At complement order five, two forced reciprocal punctures cannot both be Reverse-Ear quiet

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-order5-reciprocal-r435-forcing`

**Summary:** In the anchored HHH same-support transfer branch with Q=(q0,q1,q2,q3,q4), fix p=y_i and A=Omega-p. The transfer makes Q-q0+p non-Hamiltonian; the same-support path q0,q1,A makes A+q1 Hamiltonian, so Q-q1+p is also non-Hamiltonian. R195 on Lambda=Q+p then forces Q-q2+p and Q-q3+p (indeed also Q-q4+p) Hamiltonian. For arbitrary Hamilton paths K2,K3 on the first two supports, at least one is R435-nonquiet relative to the ancestral Q. If both were quiet, their Q-contacts occur in increasing Q-order. The full critical-block boundary wall, the first/second inward transfer shields, and non-Hamiltonicity of E0=Q-q0+p reduce K2 to two insertion words and K3 to two insertion words. Since E0 is a non-Hamiltonian five-set, accepted R902 gives an edge order on E0. In each of the four insertion-type pairs, one comparison of two edge labels yields an explicit increasing Hamilton path of E0, contradiction. Thus order-five reciprocal density necessarily produces a current R435 reversal/reverse-trimer/proper-cycle output on one of the two R195-forced reciprocal singleton fibers; the conclusion is symbolic and uses no finite SAT certificate.

### 1. Order-five same-support reciprocal setup
Retain the HHH same-support branch of `fixed-complement-triangle-double-transfer-reversal-absorber` SV21962 and specialize to

  Q=(q_0,q_1,q_2,q_3,q_4).

Fix the transfer index i used by that branch and put

  p=y_i,
  A=R_i=Omega-{p}.

The original q_0-transfer makes

  A+q_0 Hamiltonian,
  Q-q_0+p non-Hamiltonian.                                (O5.1)

The same-support forward path is

  (q_0,q_1,A).

Deleting its source q_0 leaves a literal Hamilton path on A+q_1. Therefore A+q_1 is Hamiltonian. If Q-q_1+p were Hamiltonian, these two complementary supports would give a spanning two-cover of H. Hence

  Q-q_1+p is non-Hamiltonian.                              (O5.2)

Put

  Lambda=Q+p.

Lambda itself is non-Hamiltonian, since a Hamilton path on Lambda together with A would span H by two paths. Its p-puncture is Q, hence Hamiltonian, while its q_0- and q_1-punctures are the two bad supports in (O5.1)-(O5.2).

Accepted R195 now applies to the six-set Lambda. At least four of its six punctures are Hamiltonian. Since p is already good and q_0,q_1 are bad, all three remaining punctures are good:

  Q-q_j+p is Hamiltonian for j=2,3,4.                     (O5.3)

Retain arbitrary Hamilton paths K_2 on Q-q_2+p and K_3 on Q-q_3+p.

### 2. If both reciprocal paths are R435-quiet, each has only two possible insertion words
Apply accepted R435 to K_2 against the ancestral path Q. If R435 outputs a reversed old Q-state, a reverse trimer, or a proper tight cycle, retain that output and stop. Otherwise the Q-vertices met by K_2 occur in increasing Q-order. Since K_2 contains q_0,q_1,q_3,q_4 and the one exterior vertex p, it is Q-q_2 with p inserted into one of five slots.

The full fixed-complement boundary wall SV23225 gives

  (q_1,q_0,p) tight,   (p,q_4,q_3) tight.                (O5.4)

Hence p cannot occupy the source slot, because (p,q_0,q_1) is bad, and cannot occupy the terminal slot, because (q_3,q_4,p) is bad.

The middle slot

  (q_0,q_1,p,q_3,q_4)

is also impossible. Together with the transfer shield

  (q_2,q_1,p) tight                                    (O5.5)

it would make

  (q_2,q_1,p,q_3,q_4)

a Hamilton path on the forbidden support Q-q_0+p.

Thus a quiet K_2 has exactly one of the two forms

  A_2=(q_0,p,q_1,q_3,q_4),
  B_2=(q_0,q_1,q_3,p,q_4).                              (O5.6)

Now apply R435 to K_3. Outside an immediate R435 output, K_3 is Q-q_3 with p inserted into the increasing contact order q_0,q_1,q_2,q_4.

Again the source slot is forbidden by (O5.4). The slot

  (q_0,p,q_1,q_2,q_4)

would make (p,q_1,q_2,q_3,q_4) Hamiltonian on Q-q_0+p, using the two inherited Q turns after q_1, so it is impossible. The slot

  (q_0,q_1,q_2,p,q_4)

would make

  (q_1,q_2,p,q_4,q_3)

Hamiltonian on Q-q_0+p, using its two displayed middle turns and the terminal wall (p,q_4,q_3). Hence it is impossible as well.

Therefore a quiet K_3 has exactly one of

  C_3=(q_0,q_1,p,q_2,q_4),
  D_3=(q_0,q_1,q_2,q_4,p).                              (O5.7)

### 3. The bad five-set is edge-orderable
Let

  E_0=Q-q_0+p={q_1,q_2,q_3,q_4,p}.

By (O5.1), E_0 is non-Hamiltonian. Accepted R902 therefore makes E_0 edge-orderable. Fix a total edge order < realizing its tight turns. Write uv for the ordinary edge {u,v}. Every tight turn (u,v,w) gives uv<vw.

The ancestral Q order, the first/second inward transfer shields SV20713/SV21176, and the terminal wall give

  q_1q_2 < q_2q_3 < q_3q_4,
  q_1q_2 < q_1p,
  q_2q_3 < q_2p,
  q_4p < q_3q_4.                                        (O5.8)

The four quiet insertion types add:

  A_2: q_1p < q_1q_3 < q_3q_4,
  B_2: q_1q_3 < q_3p < q_4p,
  C_3: q_1p < q_2p < q_2q_4,
  D_3: q_1q_2 < q_2q_4 < q_4p.                         (O5.9)

### 4. Every pair of quiet insertion types Hamiltonizes E_0
There are four cases.

**A_2+C_3.** Compare q_3q_4 and q_2q_4. If q_3q_4<q_2q_4, then

  p,q_1,q_3,q_4,q_2

is increasing. If q_2q_4<q_3q_4, then

  q_1,p,q_2,q_4,q_3

is increasing. Either order Hamiltonizes E_0.

**A_2+D_3.** Compare q_1p and q_4p. If q_1p<q_4p, then

  q_2,q_1,p,q_4,q_3

is increasing. If q_4p<q_1p, then

  q_2,q_4,p,q_1,q_3

is increasing.

**B_2+C_3.** Compare q_3p and q_2p. If q_3p<q_2p, then

  q_1,q_3,p,q_2,q_4

is increasing. If q_2p<q_3p, then (O5.8) gives q_2q_3<q_2p<q_3p, and

  q_1,q_2,q_3,p,q_4

is increasing.

**B_2+D_3.** Compare q_1q_2 and q_1q_3. If q_1q_2<q_1q_3, then

  q_2,q_1,q_3,p,q_4

is increasing. If q_1q_3<q_1q_2, then

  q_3,q_1,q_2,q_4,p

is increasing.

Every case produces an increasing Hamilton path of E_0, contradicting its non-Hamiltonicity.

Therefore K_2 and K_3 cannot both be R435-quiet relative to Q. Since both supports are Hamiltonian by (O5.3), at least one of the two supports has an actual Hamilton representative whose comparison with Q yields an R435 output: a reversed old Q-state, a reverse trimer at a Q/ear seam, or a proper tight cycle. In fact the argument shows that it is impossible for both supports even to possess one quiet representative each, so at least one support is entirely R435-active.

### 5. Scope and significance
This is an order-five reciprocal-exchange theorem. It consumes the R195 density forced by the two adjacent bad reciprocal punctures and converts it into unavoidable order activity. No SAT certificate is used in the proof.

The output remains current in an exact singleton fiber: K_j pairs with the fixed literal complement A to give an exact cover of H-q_j. Thus the R435 geometry carries the original fixed-complement ancestry and should be consumed before projection to generic balanced-pair or payment currency.

The theorem does not yet prove CBCA. Its gain is that the order-five same-support transfer residue cannot remain simultaneously support-quiet on the reciprocal side. The TTT statement is the exact order dual.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R195"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R902"
    }
]
```
