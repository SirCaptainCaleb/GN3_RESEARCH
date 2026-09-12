# A failed H-t tail wrap is source-transfer progress or a two-ended fixed-hub defect

**Workspace:** D17
**State:** established
**Key:** `singleton-deep-wrap-terminal-endpoint-transfer`

**Summary:** For a q2-produced exact H-t row R|B at a failed tail wrap, moving the current source s=r0 to B is an explicit legal lambda decrease whenever B+s is Hamiltonian: (R-s)|(B+s) retains the same d/y dimer and lowers source distance by one. If this transfer fails, then B+s, B+t and B+{s,t} are all non-Hamiltonian and s,t give synchronized reverse endpoint shields on B. Applying the certified fixed-hub deletion dichotomy separately at source s and terminal q=rm, any no-direct support replacement is either R435-active or, in its quiet near-end form, is forced by the wrap/append data to emit an explicit labelled P4. Hence outside P4/R435 geometry both endpoint deletion fibers must contain actual source-support/B crossings. The hard failed-wrap state is therefore a two-ended fixed-hub B-transfer object, not an anonymous wrap shield.


### 1. Setup and the current failed wrap
Retain the current universal-q2 output `singleton-deep-universal-q2-gate` SV13364 and its source transport `singleton-deep-single-row-source-transport` SV12703. Thus we have a literal exact singleton-deletion cover

  R | B  of H-t,

where B is Hamiltonian,

  R=(r_0,r_1,...,r_m),

selects one physical dimer e_0->e_1 with (e_0,e_1)=(d,y) or (y,d), and

  (t,e_0,e_1)

is tight. The selected dimer has positive source distance lambda. Put

  s=r_0,   q=r_m,   p=r_{m-1}.

Suppose the directed tail-rotation transport stops at the current row because

  omega=(p,q,s)                                            (WT.1)

is bad. Hence R3 gives the exact current wrap shield

  (s,q,p) tight.                                          (WT.2)

Every q2-produced H-t row has order at least five: before any source rotations its active order contains the five distinct consecutive vertices

  h,e_0,e_1,q_1,q_2,

and cyclic rotations preserve order. Hence m>=4 throughout this section.

Appending t to the current R would leave B literally untouched and would close H if the sole new turn (p,q,t) were tight. Therefore

  (p,q,t) bad,   (t,q,p) tight.                           (WT.3)

Apply accepted R579 to the current R. Its head-wrap seam is

  alpha=(q,s,r_1).                                        (WT.4)

Since the tail seam omega is bad, if alpha were also bad then the R579 double-fail branch, valid because m>=4, would already give the labelled P4

  (r_1,s,q,p).                                             (WT.5)

Thus outside labelled-P4 geometry we may and do retain

  (q,s,r_1) tight.                                        (WT.6)

### 2. Moving the current source to B is an honest lambda decrease
Delete the current source s from R. The suffix

  A=(r_1,...,r_m)                                         (WT.7)

is a literal tight path, still selects the same physical oriented dimer e_0->e_1, and its source distance is exactly lambda-1.

If B+s is Hamiltonian in any actual order B_s, then

  A | B_s                                                  (WT.8)

is an exact H-t two-cover. It preserves the physical dimer and the omitted label t, and the new source distance is literally lambda-1. Therefore (WT.8) is a legal restart of the same source-transport process with strict progress; no support-invariance fiction is used.

Hence the nonprogress branch may assume B+s non-Hamiltonian. Also B+t is non-Hamiltonian, because R together with a Hamilton path on B+t would two-cover H. Finally B+{s,t} is non-Hamiltonian: if it had a Hamilton path, that path together with A would two-cover H. Thus

  B+s,  B+t,  B+{s,t} are all non-Hamiltonian.             (WT.9)

For any retained Hamilton order B=(b_0,...,b_k), the two one-vertex failures in (WT.9) give the synchronized endpoint shields

  (b_1,b_0,s), (b_1,b_0,t),
  (s,b_k,b_{k-1}), (t,b_k,b_{k-1}) tight.                 (WT.10)

Indeed the complete reverse prepend/append turns would otherwise Hamilton-extend B by s or t. By the accepted singleton-deletion rail floor, k>=2.

### 3. A quiet source-endpoint replacement is always P4-valued
Apply the accepted fixed-hub dichotomy `singleton-fixed-hub-critical-dichotomy` SV4445 to the source endpoint s of the fixed hub row H-t=R|B. Either some exact H-s cover contains an actual selected adjacency crossing

  (R-s) | B,                                              (WT.11)

or there is an exact support-copy cover

  L | B  of H-s,   V(L)=(R-s)+t.                          (WT.12)

Retain the DIRECT alternative (WT.11) with its actual selected orientation and cover ancestry. Suppose instead (WT.12) holds. Compare the actual Hamilton path L with the reference R by accepted R435. If R435 emits a reversed old state, reverse trimer/contact, or proper tight cycle, retain that exact fixed-complement geometry.

Outside R435 output, the common R-vertices occur in increasing R-order along L. Since the full support R+t is non-Hamiltonian, t cannot be inserted after the first two common vertices: if L began (r_1,r_2,...) then prepending s using the inherited turn (s,r_1,r_2) would Hamiltonize R+t. Therefore exactly one of the two quiet source-replacement orders occurs:

  L_0=(t,r_1,r_2,...,q),
  L_1=(r_1,t,r_2,...,q).                                  (WT.13)

For L_0 test theta=(q,t,r_1). If theta is tight,

  (q,t,r_1,r_2)                                           (WT.14)

is a literal P4. If theta is bad, R3 gives (r_1,t,q), and (WT.3) gives

  (r_1,t,q,p)                                             (WT.15)

as a literal P4.

For L_1, restoring the omitted source s by prepending it would close H if (s,r_1,t) were tight. Hence (s,r_1,t) is bad and

  (t,r_1,s) tight.                                        (WT.16)

Test theta=(q,t,r_1) again. If theta is tight then

  (q,t,r_1,s)                                             (WT.17)

is a P4. If theta is bad, (WT.15) is again a P4.

Thus a no-direct source replacement cannot remain R435-quiet: it is always labelled-P4-valued. Outside P4/R435, the source deletion fiber must therefore realize the actual direct crossing (WT.11).

### 4. A quiet terminal-endpoint replacement is always P4-valued
Apply the same accepted fixed-hub dichotomy to the terminal endpoint q. Either some exact H-q cover contains an actual selected adjacency crossing

  (R-q) | B,                                              (WT.18)

or there is an exact support-copy cover

  E | B  of H-q,   V(E)=(R-q)+t.                          (WT.19)

Again retain any R435 output from comparing E with R. Outside R435, the common R-prefix occurs in increasing order. Since R+t is non-Hamiltonian, t must lie in one of the last two slots; otherwise E would end with the inherited pair r_{m-2},p and appending q would Hamiltonize R+t. Hence exactly

  E_0=(s,r_1,...,p,t),
  E_1=(s,r_1,...,r_{m-2},t,p).                            (WT.20)

For E_1, appending the omitted q would close H if (t,p,q) were tight. Thus R3 gives

  (q,p,t) tight,                                          (WT.21)

and the wrap shield (WT.2) immediately yields the P4

  (s,q,p,t).                                              (WT.22)

For E_0, appending q would close if (p,t,q) were tight, so

  (q,t,p) tight.                                          (WT.23)

Test phi=(s,q,t). If phi is tight,

  (s,q,t,p)                                               (WT.24)

is a P4. If phi is bad, R3 gives (t,q,s), which together with the good head-wrap seam (WT.6) gives

  (t,q,s,r_1)                                             (WT.25)

as a P4.

Thus a no-direct terminal replacement likewise cannot remain R435-quiet. Outside P4/R435, the terminal deletion fiber must therefore realize the actual direct crossing (WT.18).

### 5. Exact failed-wrap interface
A current failed H-t source-transport wrap therefore has the following exact refinement before generic payment.

1. If B+s Hamiltonizes, transfer the physical source s to B and restart the SAME d/y source transport on A with source distance lambda-1. This is a proved strict move despite the changed support partition because the new exact cover is displayed explicitly.
2. Otherwise the untouched complement satisfies the two-vertex nonextension fence (WT.9)-(WT.10).
3. At each of the two physical endpoints s,q of R, the fixed-hub deletion theorem gives either an actual source-support/B crossing in the corresponding endpoint-deletion fiber, explicit fixed-complement R435 geometry, or one of the labelled P4s (WT.14),(WT.15),(WT.17),(WT.22),(WT.24),(WT.25), together with the R579 P4 (WT.5).
4. Consequently, outside labelled P4 and explicit R435 geometry, BOTH endpoint-deletion fibers are END-DIRECT simultaneously: one exact H-s cover selects a physical (R-s)|B crossing and one exact H-q cover selects a physical (R-q)|B crossing. These crossings live in different named singleton fibers and are not silently transported into one cover.

Thus the failed wrap is no longer merely a reverse trimer. Its hard nongeometric state is a two-ended, fixed-hub B-transfer object attached to the same H-t source row, the same wrap shield, the same untouched complement B, and the failed source-transfer support B+s. This section does not claim that the two direct crossings already close H. It is established working exposition, not a certified exact unit.


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
        "revision_id": "R579"
    }
]
```
