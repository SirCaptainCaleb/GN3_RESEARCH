# Split-star weave reduces to two physical connectors and one source-order crossing

**Workspace:** D17
**State:** working
**Key:** `universal-source-splitstar-two-connector`

**Summary:** In the split-star weave branch, the hard arbitrary-fragmentation cover has exactly two rails alternating X-K and K-Y, with K split between both rails. The original Hamilton source order on K supplies a physical selected adjacency crossing the K1|K2 split. Together with one leaf-center transition on each rail, this gives a three-edge connector packet on one common residue. Cutting at the two leaf-center connectors isolates one terminal piece from each rail; the source K-crossing then either reconnects those pieces into a two-path spanning cover after restoring p or z, or one of the two required seam turns fails and R3 emits a named reverse trimer anchored on the source K edge. This reduces the split-star branch to a bounded two-connector curvature packet rather than arbitrary alternating words, but the final orientation-by-orientation restoration theorem remains open.

### 1. Split-star normal form
Retain an exact two-cover F=P|Q of the common residue

  W=H-{p,z}=L disjoint_union R disjoint_union B

in the hard connected-interaction branch, and assume the no-rainbow alternative of `universal-source-connected-rainbow-splitstar`. Then there are distinct source classes X,Y,K such that

  P alternates only between X and K,
  Q alternates only between K and Y,

both rails are nontrivial, X occurs only on P, Y only on Q, and K is split nontrivially between the two rails. Put

  K_1=V(P) intersect K,
  K_2=V(Q) intersect K.

The retained source order on K is a literal Hamilton path. Since K_1,K_2 are nonempty, there exists at least one consecutive source edge

  e_K = u-v

with u in K_1 and v in K_2 or vice versa. Retain its orientation in the source Hamilton word.

Because J(F) contains both edge types X-K and K-Y, choose one actual selected transition

  e_P between X and K on P,
  e_Q between K and Y on Q.

These are physical selected states of the same exact W-cover. Thus every split-star weave contains the bounded connector packet

  (e_P, e_K, e_Q)

linking the three source classes through the split center K.

### 2. Choosing boundary connectors
For useful reconstruction, choose e_P and e_Q extremally along their rails relative to the K-source edge e_K. More precisely, orient P and Q arbitrarily in their retained literal directions. On P choose an X-K transition closest along P to the K_1 endpoint of e_K; on Q choose a K-Y transition closest along Q to the K_2 endpoint. Cutting P at e_P and Q at e_Q produces four literal path pieces. Two pieces contain the selected K endpoints u,v of e_K; call them P_K,Q_K. The other two pieces contain the leaf-only tails toward X and Y; call them P_X,Q_Y. Empty leaf tails cannot occur because X,Y are nonempty and each chosen transition has one leaf endpoint.

The source edge e_K is not selected in F because its endpoints lie on different F rails. Adding it would join P_K and Q_K at the K source boundary positions, but one must audit the new turns at u and v. These are the only local compatibility holes introduced by the K reconnection. All other turns are inherited from P,Q, or the K source path inside their pieces.

Thus the combinatorial core of split-star absorption is two seam tests, one at each endpoint of e_K.

### 3. Two-seam reconstruction principle
Delete the selected transitions e_P,e_Q from F and add the source edge e_K. At the ordinary graph level this keeps the number of selected edges unchanged and transforms two rails into three path pieces unless one also reconnects one leaf tail through a restored omitted label p or z. The original source data provides exactly one bridge L-z-R and the source-pivot label p.

For each concrete identification of {X,Y,K} with {L,R,B}, one of the omitted labels has a natural role:

* if K=B, then z bridges L and R, the two leaf classes. The target is to use z to connect P_X and Q_Y while e_K reconnects the center pieces;
* if K=L or K=R, then z lies in the center/leaf source rail A and p is the alternative source-pivot label for the opposite side. The target uses the corresponding literal source segment through z or a p-substitution seam.

In every case, after fixing the retained orientations, the proposed spanning two-path reconstruction has only a bounded number of new turns: the two e_K endpoint turns and at most two turns involving the restored label. If all are tight, the construction yields a spanning two-cover of H. If not, R3 reverses a failed turn to a named tight trimer supported on the physical connector packet and one adjacent rail vertex.

This is a finite local-curvature reduction. The current section does not enumerate all six label assignments and both rail orientations, because that case check has not yet been independently verified. What is established is that no arbitrary number of alternating blocks remains relevant once extremal connectors are chosen: every attempted repair is controlled by e_P,e_Q,e_K plus p,z and the immediate neighboring vertices.

### 4. Relation to current trimer curvature
Any failed connector seam produces a proper tight reverse trimer. Properness follows because W contains three nonempty source classes and at least one omitted/restored label remains outside the local three-set. Accepted R4 can therefore currentize the trimer into a maximum spanning three-forest, and the source ancestry identifies exactly which split-star connector failed.

Hence a future complete split-star theorem has only two legitimate terminal outputs:

  spanning two-cover,
  or source-labelled current-trimer curvature.

This matches the parent compression `r927-curvature-single-parent-compression`. The branch should not terminate in a generic balanced pair or an unlabelled P4.

### 5. Open exact consumer
The unresolved theorem is SPLIT-STAR TWO-CONNECTOR ABSORPTION: for each identification of X,Y,K with L,R,B and the actual orientations of e_P,e_Q,e_K, prove that the bounded reconstruction either closes H or emits a current trimer whose source ancestry strictly improves the global curvature/holonomy state.

The first half, bounded localization, is proved here. The second half, a well-founded improvement after trimer currentization, is part of the common maximum-three-forest curvature program and is not claimed.

Status: working. The split-star normal form and bounded connector localization are complete consequences of the established connected-interaction theorem; the final orientation case analysis and curvature descent are open.

