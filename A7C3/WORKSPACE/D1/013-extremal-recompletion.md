# Extremal recompletion: low fragmentation or four universally internal separated markers

**Workspace:** D1
**State:** established
**Key:** `extremal-recompletion`

**Summary:** Extremize one pair-deletion fiber. LOW gives r<=5 and a <=26-vertex D2 boundary instance. PERSISTENT gives universal X-internality/X-separation and reconstructible component-drop/shield/payment structure in general; in the crossed inward-anchor specialization, pending R921/P993 now consumes the fully internal MAX5 residue completely into labelled P4 or Reverse-Ear/reversal/cycle geometry, with no protected-contact or fixed-turn residue.

Fix a hypothetical smallest counterexample H to the two-path-cover conjecture. Let D={v,d} be two distinct vertices and X be a disjoint four-set; put W=V(H)-D and Y=W-X. For each ordered exact two-cover T of H-D define
  r(T)=c(T[Y]),
  s(T)=e_T(X)+delta_T(X),
  delta_T(X)=sum_{x in X}(2-deg_T(x)).
These are selected-forest quantities. Pair-deletion exactness follows directly from minimality: a Hamilton path on H-D plus the dimer D would two-cover H. Thus the finite collection of exact T is nonempty.

D13/selected-forest-counting gives, without gate or monotonicity hypotheses,
  r(T)=6-s(T).
Choose T_* maximizing s(T), equivalently minimizing r(T), over ALL exact two-covers of this one pair-deletion residue.

There is an exhaustive extremal dichotomy.
(LOW) s(T_*)>=1, hence r(T_*)<=5.
(PERSISTENT) s(T_*)=0, hence in EVERY exact two-cover T of H-D all four vertices of X have selected degree two and no selected edge joins two vertices of X.

Proof. Each summand in s(T) is nonnegative for a path forest. If the maximum is zero, both e_T(X) and delta_T(X) vanish for every T; this says precisely that every X vertex is internal and all its selected neighbors are in Y. The converse is immediate. In that case deleting X leaves exactly six nonempty Y-blocks. Contracting them gives the three N0/N1/N2 rail shapes according to the distribution 0+4, 1+3, or 2+2 of X markers between rails. These are T-ordered blocks; native-Q monotonicity is not asserted.

Fix x in X and orient J_x on {v,x,d} with middle x, using R3. The graded deletion theorem in D1/persistent-marker-deletion-lattice, applied with B=X and S={x}, gives an exact two-cover U sqcup V of H-J_x and proves that every such cover has both rails of order at least three. That section contains the general proof, directly from R3/R4 and universal internality; no R24-dependent rail floor is invoked.

For every such source cover, all four direct attachments of x to the ends of U,V are bad. Any tight attachment would again yield an exact H-D cover exposing x. For U=(u_0,...,u_t), this forces the tight reverse shields
  (u_1,u_0,x), (x,u_t,u_{t-1}),
and likewise at both ends of V. These conclusions hold for each x and every corresponding source cover. They require no R24, R5, R168, payment, or Reverse-Ear premise.

The quantifiers matter. A single selected MAX5 cover does not establish persistent internality. Persistence follows only when MAX5 survives minimization over the entire fixed pair-deletion fiber. Conversely finding one endpoint exposure of any x in X, or one selected X-X adjacency in any exact cover, eliminates the persistent branch.

In the crossed application D={q_2,q_{m-2}} and X={a,b,c,z}, this reorganizes the choice of recompletion before applying the existing five-cell classification. LOW here means r<=5 unconditionally; its refinement into the existing LOW2/MAX3/LOW4 branches still depends on the additional hypotheses used in those classifications.

This is a proved selection principle and shield consequence, not a closure theorem. It does not prove r(T_*)<=5, eliminate the persistent branch, synchronize the four different triple-deletion source covers, or guarantee D2 recognizer acceptance in the low-fragmentation branch. It is internal exposition pending independent mathematical review.

### Persistent internality is already a component-drop/payment branch

Keep the chosen x, J_x, and exact source cover U sqcup V. The source-rail floor and terminal shields are as above.

Now choose any exact two-cover P sqcup Q of H-D. In the persistent branch x is internal in every such cover, so after relabelling P=(...,ell,x,r,...) with both sides nonempty. Deleting x from P gives a literal three-cover P_L sqcup P_R sqcup Q of the proper residue H-J_x, while U sqcup V is a literal two-cover of exactly the same residue. The fully reconstructible component-drop theorem R159 therefore gives a graph-intrinsic balanced opposite-sign pair. This recovers the useful pair-birth part of the historical universal-return theorem R359 without invoking R168 or any R24/R5 lineage.

The four direct attachments of x to the two ends of U and V are bad by persistent internality, so R3 gives the four reverse terminal shields already displayed above. The two left reverse terminal dimers of U and V have the same polarity with common witness x, while the two right reverse terminal dimers have the opposite polarity. Consequently each cross-rail diagonal, left(U) with right(V) and left(V) with right(U), is a disjoint mass-four balanced opposite-sign pair. This is the signed rectangle historically isolated in R373, but here it is rederived directly inside the persistent branch.

Apply the fully reconstructible terminal-reversal payment theorem R532 to either diagonal. Its conclusion is an alternative certificate-retaining continuation: either a spanning two-cover occurs, or the chosen diagonal has a strict balanced-pair descendant of mass less than four, with the named terminal dimer and chosen endpoint-survival certificate retained as ancestry. In the hypothetical counterexample the spanning-two-cover alternative is unavailable. The two diagonal descendants are alternative lineages and are not asserted to coexist.

Thus PERSISTENT is not a quiet descriptive residue. For every x in X and every chosen source exact two-cover of H-J_x it supplies (i) a noncircular R159 component-drop pair, (ii) four graph-intrinsic terminal shields, and (iii) two explicit R532 payment channels. What remains open is to consume one of these ancestry-bearing descendants into the desired spanning two-cover or to couple it back to the selected pair-deletion fiber. No claim is made that payment alone closes the branch.

### Consequence for the selected-cover compression side

In the LOW alternative, r(T_*)<=5. Therefore the fixed-cover boundary accounting used in D2 improves immediately for this extremal representative: with K=X and |D|=2 there are at most r+6<=11 movable pieces, and the original-vertex boundary budget 6+4r is at most 26 rather than the generic 30. This is only a sharpening of the pending D2 selected-cover compression interface; it does not imply that its exact recognizer accepts.

The extremal dichotomy therefore exposes a cleaner parent interface: either one has a selected exact pair-deletion cover with a <=26-vertex block-preserving boundary instance, or one has universal X-internality together with the reconstructible component-drop/shield/payment outputs above. Neither branch is yet a closure theorem.

### A noncircular partner-splice collision and a genuine paid-floor lineage

Keep the same source state; the already established order-three rail floor makes both terminal trimer carriers available.

Write U=(u_0,...,u_r) and V=(v_0,...,v_s), now with r,s>=2. Consider the literal spanning proposal obtained by concatenating U to V and keeping J_x as the other rail. Its only new turns are
  h_1=(u_{r-1},u_r,v_0),
  h_2=(u_r,v_0,v_1).
They cannot both be tight, since then (U,V) sqcup J_x would be a spanning two-cover of H.

If h_1 is bad, R3 gives A=(v_0,u_r,u_{r-1}) tight. The persistent right shield (x,u_r,u_{r-1}) is also tight. Hence the tested reverse terminal dimer S_U=(u_r,u_{r-1}) has two distinct same-polarity witnesses x and v_0. Since r>=2, S_U is the reverse terminal dimer of the tight carrier trimer K_U=(u_{r-2},u_{r-1},u_r), and both witnesses lie outside K_U. Therefore accepted fully reconstructible R542 applies.

If h_2 is bad, R3 gives B=(v_1,v_0,u_r) tight. The persistent left shield (v_1,v_0,x) is tight, so S_V=(v_1,v_0) has the two distinct same-polarity witnesses u_r and x. Since s>=2, S_V is the reverse boundary dimer of K_V=(v_0,v_1,v_2), again exactly in the scope of R542. Thus the U-to-V splice forces at least one R542-ready terminal collision. Reversing the roles of U and V gives a second directional collision certificate. This reconstructs the partner-only core of historical R455 directly from persistence, without R359, R389, or R168.

R542 converts whichever winning collision is chosen into a certificate-retaining continuation to either a spanning two-cover or a balanced opposite-sign descendant with one singleton support. In the hypothetical counterexample only the latter remains. If the opposite support is already singleton, this is a genuine ancestry-bearing mass-two floor; otherwise fully reconstructible R428 pays the opposite support down to singleton width while preserving the installed singleton. Consequently every persistent source state has a completely reconstructible route to a genuine paid floor carrying the R542 carrier/dimer/two-witness/crossing/capture ancestry.

This is stronger than mere existence of a floor, which is globally ubiquitous by later coordinate theorems. Its potential value is the retained source provenance: the floor descends from a specific terminal dimer of U or V and from the literal U-to-V (or V-to-U) splice. The present argument does not show that a prescribed source coordinate is the singleton produced by R542, does not keep the old source cover current through R428, and does not yet convert that ancestry into closure. Those are the remaining consumer questions.

### Crossed PERSISTENT face: the fully internal MAX5 residue is entirely geometric

Specialize to the crossed inward-anchor frame D={q_2,q_{m-2}}, X={a,b,c,z}, with Y=G_0 union G_1 union G_2, G_0={L,u}, G_1=Q[3,m-3], G_2={s,R}. In PERSISTENT every exact H-D cover has e_T(X)=0 and delta_T(X)=0. Thus all four X vertices have selected degree two, all eight selected X-incidences go to Y, and both middle-gate cells are fragmented.

Fix such an exact cover T. Apply accepted R885/R894/R898. Any R885 P4/Reverse-Ear output or R898 P4-END output is already retained geometry. Otherwise T is MAX5 and R898 gives four simultaneous tested middle-gate witness packets. Each physical middle gate has an inward witness outside {L,R}: if both vertices of one gate had neighbour set {L,R}, the selected forest would contain a 4-cycle. Moreover some X-Y incidence lands in the genuine middle cell G_1. Otherwise all eight incidences land in B={L,u,s,R}, forcing every vertex of X union B to have degree two in the induced selected subgraph and hence forcing a cycle. Therefore choose a tested middle-gate orientation S with a deep witness y=q_i, 3<=i<=m-3.

Pending R921/P993 now consumes this witness completely. Apply accepted R682 to S,y in a fresh exact H-V(S) cover. No selected state of T is transported.

In XET, one obtains (R,y,L) or (L,y,R). The first is immediately R435-active because Q is encountered in reverse order. For (L,y,R), probe by q_{i-1} using R518. A Hamilton P4 is already geometry; otherwise R518 forces (y,L,q_{i-1}), whose consecutive Q contacts y then L run backward, so R435 fires.

In CAP, retain the actual selected endpoint crossing {e,t} avoiding y and orient R527 to capture e. The underlying R526 actualization certificate itself contains exactly one tight turn from the reversal pair (t,e,y),(y,e,t), centered at the physical endpoint e. If that turn encounters Q in reverse order, R435 fires immediately. In the only monotone orientation, choose one of q_{i-1},q_{i+1} different from t and probe the capture turn by R518. Its no-P4 signature forces a trimer with consecutive Q contacts e/y in reverse order, so R435 fires; otherwise a labelled P4 occurs. The right endpoint is the exact dual.

Thus, pending review of R921/P993, the crossed PERSISTENT/MAX5 face has **no payment, protected-contact, or fixed-turn residue**. It terminates entirely in a labelled P4 or explicit Reverse-Ear/reversal/cycle certificate with source Q-coordinates retained. This is stronger than the earlier paid-floor and protected-contact continuations and makes them unnecessary for this face. R921/P993 remain pending independent review and are not canonical inputs until accepted.
