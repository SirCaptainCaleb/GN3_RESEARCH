# Source-transfer Hall can fail even under a full boundary wall and acyclic comparison orientation

**Workspace:** D17
**State:** limitation
**Key:** `fence-source-transfer-hall-fails-acyclic`

**Summary:** Exact finite fence to the proposed transferable-endpoint Hall theorem. There is a seven-vertex edge-orderable Strong Level-(1) system with Omega={0,1,2,3,4}, q0=5, q1=6 such that Omega is non-Hamiltonian deletion-Hamiltonian, Omega+q0 is non-Hamiltonian, every y in Omega satisfies the full reverse source wall (q1,q0,y), yet for deleted label a=0 no Hamilton representative of Omega-a admits a successful HEAD transfer through q0. Thus the HEAD-transfer neighborhood of a can be empty. The comparison orientation is acyclic, witnessed by an explicit total edge order. Consequently transfer-capable endpoint incidence need not satisfy Hall, and a Hall deficit does not itself force comparison holonomy.

### Exact certificate and encoding
Use vertices 0,1,2,3,4,5,6 with Omega={0,1,2,3,4}, q_0=5, q_1=6. Encode reversal pairs exactly as in the preceding finite fence: variables are lexicographically indexed by (m,a,c), a<c, and bit 1 means (a,m,c) tight. The 105-bit certificate is

  110101000000100101100010110100100000000100000000001110110000111000100100000100000000110000000000000000001

Exhaustive verification gives:

- Omega has no Hamilton path;
- every puncture Omega-a is Hamiltonian, with Hamilton-path counts 2,2,2,4,2 for a=0,1,2,3,4 respectively;
- Omega+q_0 has no Hamilton path;
- (q_1,q_0,y)=(6,5,y) is tight for every y in Omega;
- the support (Omega-{0})+q_0={1,2,3,4,5} has exactly one Hamilton path, and none begins at q_0=5. Therefore no choice of Hamilton puncture representative P_0 and HEAD endpoint b can make the source transfer q_0,b,... succeed. The source-transfer neighborhood of deleted label 0 is empty.

The comparison orientation is acyclic. One explicit total order of the 21 ordinary edges, from smallest to largest, is

  46 < 56 < 36 < 26 < 16 < 25 < 06 < 13 < 45 < 23 < 04 < 35 < 01 < 24 < 05 < 14 < 02 < 34 < 12 < 03 < 15.

Every tight turn is increasing in this edge order.

### Scope
This kills two tempting abstractions. First, the subgraph of endpoint incidences admitting successful source transfer need not satisfy Hall. Second, failure of such Hall need not create a directed comparison holonomy, since the entire comparison orientation here is acyclic. Any global contraction theorem must use actual closed representative walks, reciprocal support structure, or stronger smallest-counterexample recompletion, rather than the local transfer/blocker coloring alone.
