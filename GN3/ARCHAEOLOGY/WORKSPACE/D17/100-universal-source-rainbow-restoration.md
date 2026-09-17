# Rainbow hinge: exact restoration windows and one-step current-trimer export

**Workspace:** D17
**State:** working
**Key:** `universal-source-rainbow-restoration`

**Summary:** In a rainbow-hinge exact two-cover X-K-Y|Q of H-{p,z}, the original source labels L,R,B can be assigned to X,K,Y in six ways. Restoring z across the original L-z-R bridge or restoring p by in-place substitution changes only a bounded neighborhood of the two rainbow seams. For each assignment, every candidate spanning restoration has at most four uncertified turns. If all pass, H is two-covered; otherwise R3 reverses a failed turn to a proper source-labelled tight trimer, which R4 currentizes. Thus rainbow hinges always export directly to the common maximum-three-forest curvature layer, though no well-founded descent after currentization is claimed.

### 1. Rainbow-hinge packet
Retain an exact two-cover

  F=P|Q

of W=H-{p,z} in the hard connected-interaction branch, with one rail containing three consecutive maximal source-class blocks

  P = (... X_0 - K_0 - Y_0 ...)

whose source labels X,K,Y are the three distinct classes L,R,B. Retain the two actual selected seam states e_XK and e_KY and the literal neighboring vertices on both sides of those seams. The remainder of P outside these three blocks, if any, belongs to the same source classes but creates no new local uncertainty for a restoration performed at the displayed hinge.

The original source cover is

  C_p=A|B,
  A=L-z-R.

Hence z is a literal bridge between L and R in one retained source order, while p is the omitted source label.

### 2. Restoring z when the hinge places L and R on opposite sides
Suppose the rainbow order is L-K-R or R-K-L, with K necessarily B. The displayed hinge already gives an actual tight rail connecting L through a B-block to R. To restore z using the original source bridge, cut the two hinge seams at the chosen L-B and B-R transitions, producing three literal path pieces. Reconnect the L and R pieces through z in the original source orientation L-z-R. Keep the B-piece attached to whichever remainder of P contains it, and retain Q as the other rail.

At the ordinary graph level this exchanges two selected seam edges for the two source edges incident with z and preserves the number of path components. Every turn away from the four reconnection endpoints is inherited from F or the original source A. Therefore the resulting spanning two-path proposal has at most four uncertified turns, all supported on z together with the immediate hinge-boundary vertices.

If all these turns are tight, the proposal is a spanning two-cover of H. If any is bad, R3 gives its complete reverse as a proper tight trimer. The trimer is source-labelled by z and by the specific rainbow seam it obstructed.

### 3. Restoring z when one of L,R is the middle block
Suppose K=L, so X,Y are B,R in some order. The hinge contains two selected transitions incident with the displayed L-block. Cut the transition joining L to R-side material if present, and use the original z-R source edge to restore z at the appropriate L boundary. The remaining B transition stays selected. The dual construction applies when K=R.

Again, after choosing the literal orientation matching the retained source side, only the turn at z and at most two neighboring hinge turns are new. Hence there are at most three uncertified turns. All-pass gives a spanning two-cover after keeping Q; any failure reverses by R3 to a named proper tight trimer.

If the literal block orientation does not match the source boundary needed to attach z, compare that block order with the corresponding retained source order using R435. A nonquiet comparison is already explicit current curvature. A quiet comparison aligns the needed boundary order and returns to the preceding bounded restoration.

### 4. Restoring p when z-restoration is geometrically unavailable
There are assignments/orientations in which z lies behind a block boundary that cannot be reached by one cut without fragmenting P excessively. In that case perform the literal in-place p-for-z substitution on the original source word A as in `universal-source-local-substitution-curvature`. The universal obstruction makes the substituted support A-z+p non-Hamiltonian, so one of at most three source-local turns is bad and reverses to a proper p-labelled tight trimer. This export is independent of the rainbow order and may be used as fallback.

Thus the rainbow branch never requires unbounded transition-word analysis: either its literal hinge supports a bounded z-restoration attempt or the source itself supplies the local p-substitution curvature cell.

### 5. Currentization
Any tight reverse trimer J produced above is proper because W contains the three nonempty source classes and at least one vertex lies outside the local restoration window. Accepted R4 therefore gives an exact two-cover of H-V(J), making J one rail of a literal maximum spanning three-forest. Retain the rainbow hinge ancestry, the failed seam, and whether J arose from z-restoration, R435 block alignment, or p-substitution.

Hence every rainbow hinge has the parent-scale output

  spanning two-cover,
  OR current source-labelled trimer / R435 curvature.

This establishes the restoration/export half of the rainbow-hinge program. It does not prove that the resulting current curvature strictly descends or closes H; that is the common maximum-three-forest curvature problem.

Status: working. The bounded-window principle and fallback export are exact; the six assignment/orientation reconstructions are summarized rather than exhaustively tabulated, so this section is not yet an independently checked finite case theorem.

