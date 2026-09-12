# Nonuniform rigid reverse-bridge seam patterns force a genuine R561 five-support

**Workspace:** D17
**State:** established
**Key:** `directed-triangle-rigid-bridge-r561-consumer`

**Summary:** In the P4-free anti-aligned endpoint branch, nonconstant ancestral restoration seams force genuine R561 on explicit five-supports. The one-sided uniform residues currentize through second-bridge exact pair-deletion covers, giving structured same-residue R408 or a deeper ancestry-bearing R523 collision. In the remaining symmetric all-six-fail residue, every triangle index yields a literal double-reverse P6 P_i=(a1,a0,y_i,y_{i-1},bq,bq-1). Its complement is the three-cover A^o|B^o|{y_{i+1}}. Accepted R4/P601 makes that complement exactly two-coverable while retaining P_i, and the component-count core of R159 forces every exact complement two-cover to select a physical state crossing two of those three components. Hence the symmetric residue is a three-fiber retained-path crossing-portal system with current exact cross-states, not anonymous R159/R542 currency.

### 1. Rigid branch and exact 00 forward bridges
Retain Section 5 of `directed-triangle-two-rail-absorption`. Thus Y+a_0 and Y+b_q are P4-free. Section 2 identifies each four-set as the exact cyclic 00 cell of accepted R516. Index Y cyclically modulo 3. The 00 row gives, for every exterior vertex x in {a_0,b_q} and every i, the two mixed turns

  (x,y_i,y_{i-1}) tight,
  (y_i,y_{i-1},x) tight.                              (RC.1)

Consequently for every i the literal forward bridge

  F_i=(a_0,y_i,y_{i-1},b_q)                            (RC.2)

is a tight P4. The same rigid branch already has all three reverse bridges

  K_i=(b_q,y_{i+1},y_i,a_0).                           (RC.3)

For each i retain the two ancestral restoration seams from TA.7:

  A_i=(y_i,a_0,a_1),
  B_i=(b_{q-1},b_q,y_{i+1}).                            (RC.4)

At least one of A_i,B_i is bad for every i, since otherwise the corresponding reverse-bridge spanning proposal closes H.

### 2. A nonconstant A-side seam pattern gives R561
Suppose A_i is bad but A_{i-1} is tight for some i. By R3, badness of A_i gives the exact shield

  (a_1,a_0,y_i) tight.                                  (RC.5)

Concatenate (RC.5) with the forward bridge F_i from (RC.2). This gives a Hamilton tight path

  P_start=(a_1,a_0,y_i,y_{i-1},b_q)                    (RC.6)

on the five-vertex support

  X_i={a_1,a_0,y_i,y_{i-1},b_q},

which begins with the ordered boundary state (a_1,a_0).

Now K_{i-1}=(b_q,y_i,y_{i-1},a_0) is tight by (RC.3), and the assumed good seam A_{i-1}=(y_{i-1},a_0,a_1) appends a_1. Hence

  P_end=(b_q,y_i,y_{i-1},a_0,a_1)                      (RC.7)

is another Hamilton tight path on the SAME support X_i, ending with the reverse ordered state (a_0,a_1). Accepted R561 applies literally to X_i with u=a_1,v=a_0. Therefore X_i is universally one-vertex Hamilton-extendable. This is genuine full-support R561 geometry, not a local trimer reversal.

If the cyclic three-bit sequence [A_i tight] is nonconstant, some cyclic adjacent pair has A_i bad and A_{i-1} tight. Hence outside R561 the A-side seam bits are all equal.

### 3. The B-side dual
Suppose B_i is bad but B_{i+1} is tight. R3 gives

  (y_{i+1},b_q,b_{q-1}) tight.                           (RC.8)

Using (RC.1) with j=i+2 gives the forward bridge

  (a_0,y_{i+2},y_{i+1},b_q).

Appending (RC.8) yields the Hamilton path

  Q_end=(a_0,y_{i+2},y_{i+1},b_q,b_{q-1})               (RC.9)

on

  Z_i={a_0,y_{i+2},y_{i+1},b_q,b_{q-1}},

ending with (b_q,b_{q-1}). On the other hand the good seam B_{i+1}=(b_{q-1},b_q,y_{i+2}) prepends to the reverse bridge

  K_{i+1}=(b_q,y_{i+2},y_{i+1},a_0),

giving

  Q_start=(b_{q-1},b_q,y_{i+2},y_{i+1},a_0)             (RC.10)

on the same support Z_i, starting with (b_{q-1},b_q). Accepted R561 applies with u=b_{q-1},v=b_q. Thus any nonconstant B-side seam pattern also gives genuine R561 geometry.

### 4. Uniform residual classification
Outside R561, all three A_i have one common truth value A and all three B_i one common truth value B. Every row forbids A=B=true. Hence the complete rigid reverse-bridge residue has only three possibilities:

  (A,B)=(false,true): all three A-side restorations fail;
  (A,B)=(true,false): all three B-side restorations fail;
  (A,B)=(false,false): all six ancestral restorations fail.

In the first and third cases the reverse initial ancestral dimer (a_1,a_0) has ALL THREE Y vertices as same-tail witnesses. In the second and third cases the reverse terminal ancestral dimer (b_q,b_{q-1}) has ALL THREE Y vertices as same-head witnesses. Thus the former pigeonhole conclusion of merely two witnesses on one boundary is strengthened, outside genuine R561, to a uniform three-witness boundary obstruction on one or both ancestral sides.

### Scope
This section consumes every nonuniform three-row seam ledger into accepted R561 on an explicitly displayed five-vertex support. It does not claim that the remaining uniform three-witness boundary packet closes H. In particular generic R542 payment should still be postponed until the three simultaneous failed bridge reconstructions and the untouched ancestral complement have been tested together.

### 5. Proof-aware three-witness sharpening of the R542 fallback
Consider the uniform A-failure residues of Section 4. Put

  S_A=(a_1,a_0),    K_A=(a_0,a_1,a_2).

Then S_A is the reverse initial boundary dimer of the literal trimer K_A and is tail-signed by all three physical witnesses y_0,y_1,y_2:

  (a_1,a_0,y_i) tight for every i.                       (RC.11)

Do not execute generic R542 payment yet. Reconstruct its proof P618. Deleting V(S_A), pair-deletion exactness gives an exact two-cover T of H-{a_0,a_1}. R508 applied to the complementary carrier singleton {a_2} and the recompletion path K_A forces T to select at least one physical carrier/exterior state

  {a_2,z},     z outside {a_0,a_1,a_2}.                   (RC.12)

Fix one such selected physical state and retain its actual selected direction in T. For the following marker test choose the auxiliary marker orientation

  M=(a_2,z).

R526/P546 is proof-local here: because S_A is tail-signed by a witness w disjoint from M, it tests exactly

  (w,a_2,z).                                               (RC.13)

If (RC.13) is tight, M is head-signed by w. If it is bad, R3 gives

  (z,a_2,w) tight,                                        (RC.14)

so the reverse tested dimer M^rev=(z,a_2) is tail-signed by w. Marker orientation is an actualization choice; it is not silently identified with the selected direction of (RC.12).

#### 5.1 Exterior marker: immediate current-support collision
Suppose z is not in Y. Then all three witnesses y_0,y_1,y_2 are disjoint from M, so perform the same test (RC.13) for all three while retaining the one physical selected support {a_2,z}. Among the three truth values, two agree.

- If two tests are tight, those two witnesses head-sign the same tested dimer M, so accepted R523 gives the same-oriented two-head collision packet on M.
- If two tests are bad, their reversals (RC.14) tail-sign the same reverse tested dimer M^rev, so R523 gives the same-oriented two-tail collision packet there.

Thus any R508 carrier crossing whose exterior endpoint lies outside Y forces an R523 collision on one orientation of the ACTUAL current crossing support {a_2,z}, before payment. The collision orientation may be the selected direction or its reverse; only the physical support is asserted current in T.

#### 5.2 A marker landing in Y: collision, Hamilton P4, or the exact cyclic-00 split
Now suppose z=y_k. The marker meets exactly one of the three witnesses, so R526 may be run with the two remaining witnesses y_{k-1},y_{k+1}. If their two tests (RC.13) have the same truth value, the identical argument gives an R523 collision on M or M^rev.

Assume instead that the two tests are mixed. If Y+a_2 has a Hamilton P4, retain that literal four-vertex path as a new local reconstruction object. Otherwise Section 2 and accepted R516 force Y+a_2 to be the exact cyclic 00 cell. Reading the complete 00 row with external vertex a_2 gives the middle-a_2 cycle

  (y_{k-1},a_2,y_k) tight,
  (y_k,a_2,y_{k+1}) tight,
  (y_{k+1},a_2,y_{k-1}) tight.                            (RC.15)

In particular, for the marker M=(a_2,y_k), the two admissible witness tests are forced to be opposite:

  (y_{k-1},a_2,y_k) tight,
  (y_{k+1},a_2,y_k) bad,                                  (RC.16)

and the second bad test reverses exactly to the second turn in (RC.15). Hence the collision-free, P4-free marker-in-Y residue is not an unspecified R526 outcome: it is the exact opposite-tested cyclic-00 split on Y+a_2.

#### 5.3 Fiber-level consequence
The preceding argument applies to EVERY exact two-cover T of H-{a_0,a_1} and to EVERY selected carrier/exterior state {a_2,z} supplied in that cover. Consequently, outside the current-support R523 collision and Hamilton-P4 outputs, every such selected carrier crossing has z in Y, and Y+a_2 is the exact cyclic 00 cell. Since the carrier side is the singleton {a_2}, every selected adjacency incident with a_2 in T is a carrier/exterior crossing. R508 guarantees at least one. Therefore the hard residue has the representative-level confinement

  1 <= deg_T(a_2) <= 2,     N_T(a_2) subseteq Y            (RC.17)

for every exact T of H-{a_0,a_1}, with each selected attachment carrying the forced opposite-tested 00 split (RC.16) after cyclic relabelling.

This is strictly stronger than the generic R542 output. The three witnesses have converted payment into either a collision on a current physical crossing support, a Hamilton P4 on Y+a_2, or a complete Y-confined pair-deletion attachment normal form. The exact B-side dual holds in the uniform B-failure residue, with the complementary carrier b_{q-2} and deletion {b_{q-1},b_q}.


### 6. The Y-confined pair-deletion fiber is role-rigid outside current collision/R408
Remain in the hard A-side residue (RC.17). Thus every exact two-cover T of

  G_A=H-{a_0,a_1}

has a_2 non-singleton, every selected neighbor of a_2 lies in Y, and Y+a_2 is the exact cyclic 00 cell. Let z=y_k be a selected neighbor. The exact 00 marker split gives

  (y_{k-1},a_2,z) tight,
  (z,a_2,y_{k+1}) tight.                                  (RC.18)

#### 6.1 Source exposure forces a current-support collision
Suppose some exact T has a_2 as the source endpoint of its rail, so that the rail begins

  (a_2,z,...).

Replace this beginning by

  (a_0,a_1,a_2,z,...).

The other T-rail is untouched and every turn is inherited except (a_1,a_2,z). If that turn were tight, the two modified rails would span H, impossible. Hence it is bad and R3 gives

  (z,a_2,a_1) tight.                                      (RC.19)

Now (RC.18) gives (z,a_2,y_{k+1}) tight on the same tested orientation D=(z,a_2). Thus D has two distinct tail witnesses a_1 and y_{k+1}. Accepted R523 yields a same-tail collision on the reverse orientation of the actual selected support {a_2,z}. Therefore outside the current-support collision output, a_2 is never a source endpoint in any exact cover of G_A.

#### 6.2 Endpoint/internal variation is already same-residue R408
Because a_2 is non-singleton in every exact cover and source exposure has just been excluded, any endpoint occurrence of a_2 is a terminal occurrence. If one exact G_A cover has a_2 internal and another has it terminal, they are two exact covers of the SAME proper residue with endpoint/internal disagreement at the same physical vertex. Accepted R408 applies literally. Retain both covers, the confined Y-neighbor data, and the exact local 00 turns rather than discarding them after the discrepancy birth.

Consequently, outside current-support collision and R408, exactly one of the following fiber-wide statuses holds:

  INTERNAL-RIGID: a_2 is internal in every exact cover of G_A;
  TERMINAL-RIGID: a_2 is a terminal endpoint in every exact cover of G_A.    (RC.20)

#### 6.3 The two rigid statuses have finite local forms
In INTERNAL-RIGID, the two selected neighbors of a_2 are distinct vertices of Y. Since the selected consecutive triple through a_2 must be tight and the complete 00 row has exactly the three middle-a_2 turns in (RC.15), every exact cover selects exactly one cyclic local wedge

  (y_{k-1},a_2,y_k),     k in Z/3Z.                       (RC.21)

Thus the entire pair-deletion fiber has only three possible local states at a_2.

In TERMINAL-RIGID, every exact cover ends its a_2-rail as (...,y_k,a_2) for some k. Put

  tau_A=(a_2,a_0,a_1).

If tau_A were tight, appending a_0,a_1 to (...,y_k,a_2) would have only one further uncertain seam, (y_k,a_2,a_0). Tightness of that seam would close H, so it must be bad and R3 would give

  (a_0,a_2,y_k) tight.

Together with the first turn of (RC.18), (y_{k-1},a_2,y_k), this gives two distinct head witnesses a_0,y_{k-1} on the tested dimer (a_2,y_k), hence another R523 current-support collision. Therefore the collision-free TERMINAL-RIGID residue forces

  tau_A bad, equivalently (a_1,a_0,a_2) tight.             (RC.22)

So after exhausting genuine R561, marker-support collision, Hamilton P4, and same-residue R408, the uniform A-boundary obstruction has only two finite pair-deletion normal forms: a three-state cyclic internal wedge at a_2, or a terminal Y-attachment with the fixed global reverse turn (RC.22). The B-side dual is exact.


### 7. The untouched opposite rail builds literal second-bridge covers in the one-sided uniform residues
The one-sided uniform cases retain more than a three-witness boundary packet. The opposite ancestral restoration side is uniformly good, so each reverse bridge can be truncated into a literal pair-deletion reconstruction. This gives a second consumer before R542.

First assume

  (A,B)=(false,true).

Thus every A_i is bad and every B_i is tight. For k modulo 3 put i=k+1, so the omitted triangle vertex of K_i is y_k. From B_i and the first turn of K_i the path

  J_k=(b_0,...,b_q,y_{k-1},y_{k+1})                    (RC.23)

is tight and spans B together with Y-{y_k}.

There is an additional rail-length floor in this one-sided residue. If p=2, then A=(a_0,a_1,a_2) is a tight trimer. If A+{y_k} had a Hamilton P4 for some k, that P4 together with J_k would two-cover H. Hence all three four-sets A+{y_k} are P4-free. Apply accepted R522/P537 to the same tight trimer A and any two distinct Y vertices. Its proof compares their two exact R516 cells on the shared core and produces a literal Hamilton P5 on A plus those two vertices. The remaining y_m can be appended to B because B-good means (b_{q-1},b_q,y_m) is tight for every m. This again gives a spanning two-cover. Therefore

  p>=3.                                                   (RC.24)

The vertex a_3 is now physical. Define the second-bridge carrier seam

  t_k = [(y_k,a_2,a_3) tight].                            (RC.25)

Whenever t_k=1, the two paths

  T_k = (y_k,a_2,a_3,...,a_p)
        | (b_0,...,b_q,y_{k-1},y_{k+1})                  (RC.26)

form a literal exact two-cover of the SAME residue G_A=H-{a_0,a_1}. Tightness is inherited from t_k, A, B_i, and K_i. Exactness is literal: if G_A were Hamiltonian, that Hamilton path together with the vacuous dimer (a_0,a_1) would two-cover H.

If two distinct bits t_k,t_l are tight, then two actual covers (RC.26) coexist. After cyclic relabelling take l=k+1. The vertex y_k is a source endpoint in T_k, while in T_{k+1} it lies strictly internally in the second rail segment

  ... b_q,y_k,y_{k+2}.

Thus accepted R408/P417 applies on the same residue G_A. Proof-aware retention is stronger than the abstract R408 output: keep both exact covers T_k,T_{k+1}, the common deleted pair {a_0,a_1}, the shared ancestral A-suffix edge a_2a_3, and the two distinct reverse-bridge reconstructions that built them.

If at most one t_k is tight, at least two are bad. For each bad t_k, R3 gives

  (a_3,a_2,y_k) tight.                                   (RC.27)

Hence the reverse ancestral A-edge (a_3,a_2) has at least two same-tail Y witnesses and accepted R523 gives a two-tail collision there. If exactly one t_k is tight, the physical support {a_2,a_3} is simultaneously current in the corresponding exact cover T_k, where it is selected in the forward direction; if none is tight, retain instead its exact ancestry as the selected A-edge in the original H-Y cover. In neither case is the collision spent anonymously.

Therefore the one-sided residue (false,true) sharpens to

  structured same-residue R408 from two bridge-built covers,
  OR an ancestry-bearing R523 collision on the next physical A-edge. (RC.28)

The B-side dual is exact. Assume (A,B)=(true,false). Then every A_i is tight and every B_i is bad. For each k the truncated reverse bridge and A_i give the tight path

  J^B_k=(y_{k-1},y_{k+1},a_0,a_1,...,a_p),               (RC.29)

spanning A together with Y-{y_k}. If q=2, a Hamilton P4 on B+{y_k} together with J^B_k closes H, so all three such four-sets would be P4-free. R522 applied to the tight trimer B and two Y vertices then gives a Hamilton P5 on B plus those two, while the remaining Y vertex prepends to A because every (y_m,a_0,a_1) is tight. Contradiction. Hence q>=3.

Put

  t^B_k=[(b_{q-3},b_{q-2},y_k) tight].                   (RC.30)

For every tight t^B_k there is an exact cover of H-{b_{q-1},b_q},

  T^B_k=(b_0,...,b_{q-2},y_k)
        |(y_{k-1},y_{k+1},a_0,...,a_p).                  (RC.31)

Two tight bits again give endpoint/internal disagreement at one of their Y labels and therefore a structured same-residue R408 with both covers retained. If at most one bit is tight, at least two are bad and R3 gives

  (y_k,b_{q-2},b_{q-3}) tight,                            (RC.32)

so the reverse ancestral B-edge (b_{q-2},b_{q-3}) carries a same-head two-witness R523 collision. This is the literal head/tail dual of (RC.28).

Thus after the genuine R561 nonuniform cases, the two one-sided uniform residues are no longer merely anonymous boundary packets: their untouched good side forces either two competing exact pair-deletion reconstructions with an actual R408 discrepancy, or a collision one edge deeper on the ancestral rail. The genuinely symmetric hard residue is now (A,B)=(false,false), where neither truncation (RC.26) nor (RC.31) is available because both opposite restoration seams fail.


### 8. The symmetric all-six-fail P6s are retained-path complement crossing portals
Remain in the symmetric uniform residue

  (A,B)=(false,false),

so every A_i and every B_i is bad. For every i modulo 3, R3 and the cyclic 00 forward-bridge turns give the literal tight path

  P_i=(a_1,a_0,y_i,y_{i-1},b_q,b_{q-1}).                  (RC.33)

Indeed the four required turns are

  (a_1,a_0,y_i),
  (a_0,y_i,y_{i-1}),
  (y_i,y_{i-1},b_q),
  (y_{i-1},b_q,b_{q-1}).

Put

  A^o=(a_2,...,a_p),
  B^o=(b_0,...,b_{q-2}),
  h_i=y_{i+1}.                                             (RC.34)

Both A^o and B^o are nonempty because the ancestral rail floor gives p,q>=2. The complement of the retained P6 is exactly

  W_i=H-V(P_i)=V(A^o) union V(B^o) union {h_i},

and it has the literal three-cover

  R_i=A^o | B^o | {h_i}.                                  (RC.35)

Now use the proof mechanism of accepted R4/P601 with the RETAINED proper tight path P_i. The complement W_i cannot be Hamiltonian, since a Hamilton path of W_i together with P_i would two-cover H. Smallest-counterexample minimality gives pc(W_i)<=2, hence pc(W_i)=2 exactly. Choose any exact two-cover

  T_i=T_i^1|T_i^2                                          (RC.36)

of W_i. The same retained-path argument gives P_i|T_i as a minimum spanning three-cover of H.

Before invoking the payment part of R159, use only its elementary component-count step. If no selected adjacency of T_i joined two distinct components of R_i, then each T_i rail would lie wholly inside one R_i component. Two rails could not cover the three nonempty components A^o,B^o,{h_i}. Therefore T_i selects an ACTUAL directed state

  x_i -> x'_i                                              (RC.37)

whose endpoints lie in two distinct members of {A^o,B^o,{h_i}}.

Retain the entire portal cell

  (P_i; A^o|B^o|{h_i}; T_i; x_i->x'_i).                   (RC.38)

Thus the symmetric all-six-fail residue is not merely three overlapping double-reverse P6s or two independent boundary packets. It is a THREE-FIBER triangle-indexed family of minimum-three-cover portals over the common two-rail base A^o|B^o, each with its own omitted Y-label and a CURRENT exact selected crossing in an exact complement representative. R176 may be applied downstream to (RC.37), but doing so is optional and is not the progress claim.


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
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R408"
    },
    {
        "relation": "dependency",
        "revision_id": "R508"
    },
    {
        "relation": "dependency",
        "revision_id": "R516"
    },
    {
        "relation": "dependency",
        "revision_id": "R522"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    },
    {
        "relation": "dependency",
        "revision_id": "R526"
    },
    {
        "relation": "dependency",
        "revision_id": "R542"
    },
    {
        "relation": "dependency",
        "revision_id": "R561"
    }
]
```
