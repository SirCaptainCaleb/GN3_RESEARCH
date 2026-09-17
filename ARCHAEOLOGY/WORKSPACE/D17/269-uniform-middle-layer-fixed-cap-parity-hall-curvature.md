# Cross-cap parity makes every quiet endpoint-return cycle impossible: each cap descends or carries fixed-complement R435 curvature

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-fixed-cap-parity-hall-curvature`

**Summary:** In R927 Arm M with k>=6, fix any literal Hamilton k-path C and let Omega=V(H)-V(C). Then Omega is a non-Hamiltonian deletion-Hamiltonian (k+1)-block. Every exterior label u has the two reverse boundary turns against C because C+u is a forbidden (k+1)-support. Define chi_C(u) by whether the cross-cap turn (c0,u,c_{k-1}) is tight. Apply accepted R945 to Omega. For every matched endpoint-return edge u->v, deleting the exposed endpoint v from the certified Hamilton puncture path on Omega-u gives a Hamilton path on Omega-{u,v}; hence H-{u,v}=C|(Omega-{u,v}) is a literal pair-deletion frame. If chi_C(u)=chi_C(v), the R584 equal-parity splice gives a P5 or P4 whose complement is exactly C-interior plus that Hamilton core, producing a spanning maximum three-forest with largest rail k-1. Thus in any no-descent state every matched edge flips chi_C. The functional cycle of R945 must then be even; R945 says an R435-quiet extremal shortest cycle is a triangle, impossible. Therefore every fixed cap C either admits strict largest-rail descent or its complementary critical block contains explicit R435 geometry between actual puncture paths, all paired with the same literal complement C. This upgrades the two-probe mixed twist to a global parity/odd-cycle obstruction.


### 1. Fixed-cap critical block and its full two-ended wall
Assume accepted R927(M):

  |V(H)|=2k+1,
  every k-set is Hamiltonian,
  no (k+1)-set is Hamiltonian,                            (CP.1)

and work in the live range k>=6.

Fix ANY literal Hamilton k-path

  C=(c_0,c_1,...,c_{k-1})                                (CP.2)

on support X, and put

  Omega=V(H)-X.                                           (CP.3)

Then |Omega|=k+1. By (CP.1), Omega is non-Hamiltonian, while Omega-u is a Hamiltonian k-set for every u in Omega. Hence Omega is a non-Hamiltonian deletion-Hamiltonian block to which accepted R945 applies.

There is also a graph-intrinsic full reverse wall at both ends of C. For every u in Omega, if

  (u,c_0,c_1)

were tight then (u,c_0,c_1,...,c_{k-1}) would Hamiltonize the forbidden (k+1)-support X+u. Therefore R3 gives

  (c_1,c_0,u) tight.                                      (CP.4)

Dually, if (c_{k-2},c_{k-1},u) were tight then C followed by u would Hamiltonize X+u, so R3 gives

  (u,c_{k-1},c_{k-2}) tight.                              (CP.5)

Thus every exterior label simultaneously tail-signs the reverse source dimer and head-signs the reverse terminal dimer of the SAME literal cap C.

Define the CROSS-CAP PARITY bit

  chi_C(u)=1  iff  (c_0,u,c_{k-1}) is tight,              (CP.6)

and chi_C(u)=0 otherwise.

### 2. Equal parity on an endpoint-return edge is strict largest-rail descent
Apply accepted R945 to Omega. Retain its left-saturating endpoint-core matching, functional map f, an extremal shortest directed cycle, and for every matched edge

  u -> v=f(u)                                             (CP.7)

an ACTUAL Hamilton puncture path P_u on Omega-u that exposes v as a physical endpoint.

Delete that endpoint v from P_u. The remaining literal contiguous path

  D_{uv}=P_u-v                                            (CP.8)

is Hamiltonian on Omega-{u,v}, of order k-1. Hence

  H-{u,v}=C | D_{uv}                                      (CP.9)

is a literal exact pair-deletion two-cover with cap C.

Suppose first chi_C(u)=chi_C(v)=1. Then

  (c_0,u,c_{k-1}), (c_0,v,c_{k-1})

are tight. Accepted R584 gives one of

  (c_0,u,c_{k-1},v),
  (c_0,v,c_{k-1},u)                                      (CP.10)

as a literal tight P4. In the first case prepend c_1 using (CP.4) for u; in the second use (CP.4) for v. Thus one obtains a literal tight P5 S with vertex set

  {c_1,c_0,c_{k-1},u,v}.                                 (CP.11)

Its complement is exactly the union of the two literal paths

  C[2,k-2] | D_{uv}.                                      (CP.12)

Therefore S|C[2,k-2]|D_{uv} is a spanning three-path cover and hence a maximum three-forest by R4. Its rail orders are

  5, k-3, k-1,                                            (CP.13)

so for k>=6 its largest rail has order k-1, strictly below the cap height k.

Now suppose chi_C(u)=chi_C(v)=0. R3 gives

  (c_{k-1},u,c_0), (c_{k-1},v,c_0) tight.                (CP.14)

R584 gives one of the two literal P4s

  (c_{k-1},u,c_0,v),
  (c_{k-1},v,c_0,u).                                     (CP.15)

The complement is exactly

  C[1,k-2] | D_{uv},                                      (CP.16)

so restoring the P4 gives a maximum three-forest of rail orders

  4, k-2, k-1.                                            (CP.17)

Again the largest rail is k-1.

Consequently:

> Every matched endpoint-return edge u->v with chi_C(u)=chi_C(v) gives an explicit strict largest-rail Morse descent.                    (CP.18)

### 3. No-descent forces binary alternation around the endpoint-return cycle
Assume now that no strict descent of the form above occurs for the fixed cap C. Then every matched endpoint-return edge must satisfy

  chi_C(f(u)) = 1-chi_C(u).                               (CP.19)

Let

  y_0 -> y_1 -> ... -> y_{t-1} -> y_0                    (CP.20)

be the extremal shortest functional cycle retained by R945. Matched 2-cycles are impossible by R945, so t>=3. Equation (CP.19) says the binary bit flips at every step around C. Returning to y_0 therefore requires t even. Thus

  t>=4 and t is even.                                     (CP.21)

But accepted R945 says that if every adjacent puncture-path comparison around this extremal shortest cycle is R435-quiet, then t=3. This contradicts (CP.21).

Hence some adjacent pair of ACTUAL puncture paths P_i,P_{i+1} emits an explicit accepted R435 output: an adjacent selected reversal, a reverse trimer, or a proper tight cycle. Both puncture paths are source-visible with the same literal complement C, because

  P_i | C  covers H-y_i,
  P_{i+1} | C covers H-y_{i+1}.                           (CP.22)

Thus the R435 output lies in one fixed-complement critical-block puncture cylinder, not between unrelated historical representatives.

### 4. Fixed-cap parity theorem
We have proved:

> FIXED-CAP PARITY/HALL DICHOTOMY. In R927 Arm M with k>=6, for every literal Hamilton k-path C, either there exists a spanning maximum three-forest whose largest rail has order at most k-1, or the deletion-Hamiltonian complement Omega=V(H)-V(C) contains explicit R435 geometry between two actual Hamilton puncture paths, both paired with the same literal complement C in exact singleton-deletion covers.            (CP.23)

The theorem is stronger than the original two-probe mixed-twist statement in one decisive sense. A mixed cross-cap bit on one pair can survive locally, but it cannot remain globally flat on all endpoint-return incidences of the complementary critical block. If equal parity ever occurs on one certified incidence, Morse height drops. If every certified incidence is mixed, binary alternation forces every functional cycle even, while R945 says a quiet extremal cycle must be triangular. Hence curvature is forced.

No alternative R526/R527 descendants are compared, no payment lineage is used, and no Hamilton order is transported across different supports. The only synchronized word is the one fixed cap C; all puncture paths are retained exactly as supplied by R945.


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
        "revision_id": "R584"
    },
    {
        "relation": "dependency",
        "revision_id": "R927"
    },
    {
        "relation": "dependency",
        "revision_id": "R945"
    }
]
```