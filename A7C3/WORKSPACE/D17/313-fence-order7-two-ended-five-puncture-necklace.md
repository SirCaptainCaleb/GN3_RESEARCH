# Five common-endpoint Hamilton punctures do not force the two exterior punctures at order seven

**Workspace:** D17
**State:** limitation
**Key:** `fence-order7-two-ended-five-puncture-necklace`

**Summary:** Exact finite fence for the order-seven residue of SV64567. There is a seven-vertex Strong Level-(1) exact-reversal system Omega=K+{y,z}, with K a Hamilton P5, such that Omega is non-Hamiltonian; for every d in K, Omega-d has a Hamilton P6 whose physical endpoints are exactly y,z and whose four interior vertices are K-d; yet both Omega-y and Omega-z are non-Hamiltonian. Thus the rigid two-ended five-puncture necklace isolated by SV64567 is locally realizable and cannot be promoted to a full deletion-Hamiltonian critical block from puncture support data alone. The exact 105-bit certificate and five puncture paths are recorded below and were exhaustively rechecked. Any G23 extinction of this residue must spend additional common-complement/current-pair/ancestry geometry.

### 1. Encoding
Use vertices 0,1,2,3,4,5,6, with

  K={0,1,2,3,4},  y=5,  z=6.

For each middle vertex m and each unordered endpoint pair a<c in V-{m}, one bit specifies the reversal pair: bit 1 means (a,m,c) is tight and bit 0 means its complete reversal (c,m,a) is tight. For each fixed m the fifteen endpoint pairs are listed in lexicographic order. The seven 15-bit middle strings are

  m=0: 111111001010100
  m=1: 111010101101011
  m=2: 100001000000100
  m=3: 000101110110110
  m=4: 101010000110001
  m=5: 001001110100000
  m=6: 100000000110100.                                (F7.1)

Equivalently, for m=0 the pair order is
(1,2),(1,3),(1,4),(1,5),(1,6),(2,3),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6),(4,5),(4,6),(5,6),
and for every other m use the same lexicographic rule after deleting m from the endpoint set. This determines all 105 reversal pairs exactly.

### 2. Retained Hamilton P5 and five common-endpoint puncture paths
The five-set K has the literal Hamilton path

  (0,1,2,3,4).                                           (F7.2)

For each d in K, the following is a Hamilton path on Omega-d, with endpoints exactly 5 and 6 and interior support K-d:

  d=0: (5,2,3,4,1,6),
  d=1: (6,2,4,3,0,5),
  d=2: (5,1,0,4,3,6),
  d=3: (5,4,0,2,1,6),
  d=4: (5,1,3,2,0,6).                                  (F7.3)

Direct evaluation of the four internal turns of each word against (F7.1) verifies tightness. Thus all five K-root punctures are Hamiltonian in precisely the two-ended shape isolated by OC.8 of SV64567.

### 3. The full seven-set and both exterior punctures remain non-Hamiltonian
Exhaustive enumeration of all 7!=5040 vertex orders finds no Hamilton P7 on Omega. Exhaustive enumeration of all 6!=720 orders on Omega-5 finds no Hamilton P6, and the same holds for Omega-6. Therefore

  Omega non-Hamiltonian,
  Omega-5 non-Hamiltonian,
  Omega-6 non-Hamiltonian.                               (F7.4)

For reference, exhaustive enumeration finds Hamilton paths after deletion of each d=0,1,2,3,4, agreeing with the explicit witnesses (F7.3). Hence the good-deletion set can be exactly K while the two common physical endpoints y,z are both bad.

### 4. Consequence for G23
The bounded residue of SV64567 is not contradictory as a seven-vertex induced exact-reversal system. In particular the tempting implication

  five Hamilton punctures with one common endpoint pair
    => one of the two endpoint labels is Hamilton-deletable

is false. Nor can one infer full deletion-Hamiltonicity of Omega from the five-root wheel shell alone.

Therefore a valid extinction theorem for the order-seven coherent wheel must use geometry not present in this induced necklace certificate: for example the literal common Hamilton complement Q, the current pair-deletion edge cover of SV63649, the shared hub/spoke ancestry, the global completed-anchor ledger, or a genuine global Phi/epsilon_* descent. This fence is computational/exact finite evidence and is not a positive closure theorem.