# R912 is R24-independent: fixed-complement critical-block walls follow from exactness and R3

**Workspace:** D17
**State:** established
**Key:** `r24-independent-r912-fixed-complement-critical-block-wall`

**Summary:** R912, `Fixed-Complement Critical-Block Wall`, does not require R24. Let Omega be non-Hamiltonian but deletion-Hamiltonian and let Q be a fixed Hamilton complement. For every y in Omega choose a Hamilton puncture path on Omega-y. If y could attach tightly to either end of Q, that puncture path plus the extended Q would two-cover H. Therefore both attachment turns are bad and R3 gives the reverse boundary-wall turns. The conclusion is exactly the two-ended universal wall used by R912. No singleton-order floor or short-complement rigidity enters.

### 1. Critical-block split
Retain

  V(H)=Omega disjoint_union V(Q),
  Q=(q_0,...,q_m),                                       (R912.1)

with Omega non-Hamiltonian and deletion-Hamiltonian. For each y in Omega choose a Hamilton path P_y on Omega-y.

### 2. Source-end wall
If

  (y,q_0,q_1)

were tight, then (y,Q)|P_y would be a spanning two-cover of H. Therefore this turn is bad, and R3 gives

  (q_1,q_0,y) tight.                                     (R912.2)

### 3. Terminal-end wall
Similarly, if

  (q_{m-1},q_m,y)

were tight, then Q followed by y together with P_y would two-cover H. Hence R3 gives

  (y,q_m,q_{m-1}) tight.                                 (R912.3)

These are exactly the fixed-complement boundary walls.

### 4. Dependency repair
The proof uses only deletion-Hamiltonicity, the literal complement Q, counterexamplehood, and R3. R24 is unnecessary.