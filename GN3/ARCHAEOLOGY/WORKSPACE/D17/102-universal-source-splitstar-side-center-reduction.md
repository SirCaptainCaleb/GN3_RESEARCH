# Side-centered split-star weave reduces to local substitution curvature plus one opposite-rail connector

**Workspace:** D17
**State:** established
**Key:** `universal-source-splitstar-side-center-reduction`

**Summary:** If the split-star center is L or R, the center lies on the original source rail A=L-z-R. The source-order crossing between the two center portions together with one leaf-center transition on the opposite rail yields a bounded connector packet. Restoring z on its literal source side handles one half; the remaining mismatch is exactly an in-place p-for-z substitution window on A. Therefore the side-centered branch closes if all bounded seams pass and otherwise emits a source-labelled reverse trimer by R3, currentized by R4. Combined with the B-centered unit, all split-star label assignments now export to spanning two-cover or current curvature.

### 1. Center L; center R is dual
Retain the split-star exact cover F=P|Q of W=H-{p,z}. Suppose the center class is L. Then one rail alternates between B and L, the other between L and R. The class L is split nontrivially across both rails; B and R are leaves.

Choose a source L-edge e_L=u-v crossing the two L portions. Choose one selected B-L transition on the B/L rail and one selected L-R transition on the L/R rail, extremal relative to u,v. This is the same three-connector packet as before, but now the split center belongs to the source bridge rail A rather than the fixed complement B.

### 2. Restore z on the R side
The original source order is L-z-R. Cut the selected L-R transition nearest the L endpoint participating in e_L and use the literal source edge from z into the R-side source segment to attach z to the retained R piece. This introduces only the local turn at z and one neighboring connector turn. If the needed L boundary orientation disagrees with the retained source L order, compare the corresponding L block with the source L path by R435; nonquiet gives immediate current curvature, quiet aligns the block boundary.

After this restoration, the remaining discrepancy is that the two split L portions must be rejoined and p must replace the historical z-position on the A side if the B/L rail is to be incorporated without creating a third component.

### 3. The residual is exactly a local p-substitution window
Insert p into the original source position of z in A=L-z-R, but now retain the already restored R-side piece and the L-source edge e_L used to connect the split L portions. Every turn away from the radius-two neighborhood of the old z position is inherited from A or from the exact split-star rails. Hence the only uncertified p-turns are the same at-most-three windows of `universal-source-local-substitution-curvature`.

If all these p-windows and the two connector seams are tight, the reconstructed rails form a spanning two-cover of H. If any fails, R3 reverses that failed turn to a proper tight trimer carrying p or one connector endpoint. R4 currentizes it.

Thus center L yields spanning two-cover or current source-labelled curvature. Center R is the exact reversal/rail dual.

### 4. Complete split-star export
Together with `universal-source-splitstar-central-b-curvature`, every assignment of the split-star center among L,R,B has the same parent-scale outcome:

  spanning two-cover,
  explicit R435 order curvature on a source block,
  or a proper source-labelled reverse trimer currentized into maximum-three-forest space.

No transition-count induction survives. The remaining problem is wholly downstream in current curvature consumption.

Status: complete working reduction at theorem-interface level; the local seam bookkeeping is bounded and source-labelled, but not independently reviewed as a canonical exact section unit.

