# Selected-edge unions satisfy the Hamilton-path separator bound, with a rigid equality row

**Workspace:** D17
**State:** established
**Key:** `singleton-cover-union-separator-row`

**Summary:** For any chosen singleton-cover family and any nonempty S, the selected-edge union U satisfies c(U-S)<=|S|+1. Equality rigidifies every x-deletion cover: after trimming S-{x}, each component of U-S is one contiguous Hamilton block and the remaining separator labels alternate internally between these blocks along exactly two rails. For a 2-cut {p,q} with three components, q in C_p and p in C_q each join two Hamilton atoms. If they join different atom-pairs, a spanning two-cover follows immediately; hence every counterexample equality cell has both connectors joining the same two atoms with the third atom as a fixed Hamilton complement.

### Separator bound
Let H be a hypothetical smallest counterexample. Choose one exact two-nonempty-path cover C_x of H-x for every vertex x, and let U be the ordinary graph formed by the union of all selected rail adjacencies in this family.

For every nonempty vertex set S,

  c(U-S) <= |S|+1.

Fix x in S. Start from the two literal rails of C_x and delete the |S|-1 vertices of S-{x}. Deleting one vertex from a path can increase the number of nonempty path pieces by at most one, so the two rails leave at most

  2+(|S|-1)=|S|+1

nonempty path pieces. Every remaining selected edge lies in U-S, and these pieces cover all vertices of U-S. Consequently each connected component of U-S contains at least one of the pieces, proving the bound.

This is exactly the ordinary separator inequality necessary for a Hamilton path, but here it comes with actual tight-path representatives inherited from every singleton fiber.

### Equality rigidifies every singleton row
Assume now

  c(U-S)=|S|+1.

Then the preceding argument is sharp for every choice x in S. Therefore trimming S-{x} from C_x produces exactly |S|+1 nonempty pieces, and since U-S itself has exactly that many components, each component of U-S contains exactly one trimmed piece. Hence every component of U-S is itself spanned by one contiguous tight subpath of C_x. In particular every component of U-S is Hamiltonian.

Sharpness of path fragmentation also forces every y in S-{x} to be internal on its C_x rail, and no two vertices of S-{x} can be consecutive selected vertices on that rail. After contracting every component of U-S to one atom, C_x becomes exactly two disjoint alternating paths whose atom-vertices are the components of U-S and whose separator vertices are S-{x}. Every separator vertex has quotient degree two.

Thus equality gives a simultaneous row of actual alternating connector covers, one for every omitted x in S, on a common family of Hamilton atoms.

### The three-component 2-cut
Specialize to S={p,q} and suppose U-{p,q} has three components A,B,C. Equality holds. The p-deletion cover C_p has q internal. Trimming q gives exactly the three Hamilton atoms A,B,C, so, up to exchanging rails, permuting the atoms, and retaining the actual orientations,

  C_p = (A - q - B) | C,

where the notation means one literal tight rail consists of a Hamilton A-block, then q, then a Hamilton B-block, while the other rail is a Hamilton path on C. Likewise

  C_q = (A' - p - B') | C'

for some assignment of the same three atoms to the two joined positions and the isolated rail.

Call the unordered atom-pair joined by q in C_p the q-connector pair, and define the p-connector pair dually.

### Different connector pairs close H
Suppose the two connector pairs differ. Write C_p=(A-q-B)|C. Since the p-connector pair is a different edge of the three-atom triangle, it contains C and exactly one of A,B. For example, after relabelling,

  C_q=(A-p-C)|B.

The contiguous suffix p-C (or prefix C-p, according to the retained orientation) is a tight Hamilton path on {p} union C. It is vertex-disjoint from the full tight rail A-q-B of C_p, and the two paths together span all of H. This is a spanning two-cover, contradiction. The case C_q=(B-p-C)|A is identical.

Therefore in a hypothetical counterexample the p- and q-connector pairs must be equal.

### Fixed-complement equality normal form
Every surviving three-component 2-cut consequently has, after relabelling,

  C_p=(A-q-B)|C,
  C_q=(A'-p-B')|C'',

where A,A' are Hamilton orders on the same atom A, B,B' on the same atom B, and C,C'' are Hamilton orders on the same atom C. Thus both separator vertices are alternative internal bridges between the same two Hamilton atoms, while the third atom is a fixed Hamilton complement.

This is a global selected-edge-union parent of the fixed-complement rows that arise much later in the R953 recurrence analysis. No R927, R942, R953, stationarity, or minimum-offending-side hypothesis is used here.

The remaining hard equality cell is therefore precise: consume two alternative internal bridge vertices on one fixed pair of Hamilton atoms, with an explicit Hamilton complementary atom. A successful consumer would either rule out three-component 2-cuts entirely or currentize directly to a support transfer / boundary-reversed Hamilton dimer / spanning two-cover.

Status: complete elementary deduction from the selected-edge-union representation; not independently reviewed or canonically certified.
