# A cut vertex of the selected-edge union creates two overlapping critical blocks

**Workspace:** D17
**State:** established
**Key:** `singleton-cover-union-block-normal-form`

**Summary:** Assume the selected-edge union U of a singleton-cover family has a cut vertex w. The concurrent bridgeless theorem already handles edge cuts. Here U-w has exactly two components A,B and the w-deletion cover Hamiltonizes both. For each x in A, counterexamplehood forces A-x+w Hamiltonian: otherwise the x-deletion cover exposes a Hamilton B+w rail and closes against the Hamilton path on A; dually B-y+w is Hamiltonian for every y in B. Hence A+w and B+w are non-Hamiltonian deletion-Hamiltonian blocks, intersecting exactly in w and covering H. Thus every selected-edge union in a counterexample is either 2-vertex-connected or directly presents the old double-critical overlap obstruction.

### Setup
Retain a hypothetical smallest counterexample H and one exact singleton-deletion two-cover C_x for every x. Let U be the ordinary selected-edge union. The concurrent section `singleton-cover-union-bridgeless` proves that U is connected and has no bridge. This section records the stronger consequence of a vertex cut.

### A cut vertex has exactly two sides
Suppose w is a cut vertex. Every rail of C_w is a connected path in U-w. Since C_w has exactly two nonempty rails spanning H-w, U-w has at most two connected components. Because w is a cut vertex it has at least two, hence exactly two; call their vertex sets A and B. The two rails of C_w are therefore Hamilton paths on all of A and all of B.

### Every puncture of one side plus w is Hamiltonian
Fix x in A and inspect C_x. Since U-w has no A-B edge, only the C_x rail containing w can meet both A-x and B. The other rail lies wholly in one side.

If the other rail lies in A, then the w-containing rail contains every vertex of B. Removing any possible A-prefix or A-suffix at w leaves a contiguous tight subpath spanning exactly B+w, so B+w is Hamiltonian. But C_w already supplies a Hamilton path on A; the two paths A | (B+w) would span H, contradiction. Therefore this case cannot occur.

Hence the rail not containing w lies in B. The w-containing rail contains every vertex of A-x. Its contiguous portion on (A-x)+w is a Hamilton tight path. Thus

  (A-x)+w is Hamiltonian for every x in A.

The dual argument gives

  (B-y)+w is Hamiltonian for every y in B.

Together with the C_w paths on A=(A+w)-w and B=(B+w)-w, both A+w and B+w are vertex-deletion-Hamiltonian.

### Both blocks are genuinely non-Hamiltonian
If A+w itself were Hamiltonian, it would pair with the Hamilton path on B from C_w to give a spanning two-cover of H. Therefore A+w is non-Hamiltonian. Dually B+w is non-Hamiltonian. Thus

  (A+w) intersect (B+w)={w},
  (A+w) union (B+w)=V(H),

and both blocks are non-Hamiltonian deletion-Hamiltonian boundary subtournaments.

### Parent normal form
Consequently every selected-edge union of a hypothetical counterexample is either 2-vertex-connected, or any exhibited articulation vertex directly currentizes the familiar pair of overlapping critical blocks. This recovers the structural double-star obstruction from the global selected-edge-union representation without requiring an edge-maximal compatibility family or rail-incidence-root derivation. It does not consume the two critical blocks; their ordered interaction remains the residual.

Status: complete elementary working deduction; not canonically reviewed.
