# B-centered split-star weave has a three-connector spanning proposal with bounded curvature

**Workspace:** D17
**State:** established
**Key:** `universal-source-splitstar-central-b-curvature`

**Summary:** In the split-star branch with center K=B, the exact W-cover has rails alternating L-B and B-R. Choose extremal leaf-center transitions and a source B-edge crossing the two B portions. Cutting the two selected leaf-center transitions and inserting the B source edge reconnects the center pieces; restoring z through the literal L-z-R bridge reconnects the leaf pieces. The resulting spanning two-path proposal has only finitely many new seam turns, all within the three connector edges and their immediate neighbors. All tight closes H; any failure reverses by R3 to a proper trimer, hence current maximum-three-forest curvature by R4. This gives one completely checked split-star label assignment.

### 1. B-centered split star
Retain the exact common-residue cover F=P|Q of

  W=H-{p,z}=L disjoint_union R disjoint_union B

in the split-star branch, with center class B. Thus, after rail exchange,

  P alternates only between L and B,
  Q alternates only between B and R,

L occurs only on P, R only on Q, and B is split nontrivially between both rails.

Choose one selected L-B transition e_P on P and one selected B-R transition e_Q on Q. Choose them extremally relative to a fixed literal source edge e_B=u-v of the original Hamilton B-order with u on the P-side B-support and v on the Q-side B-support, as in the split-star connector section.

### 2. Cut-and-reconnect graph surgery
Delete the two selected transitions e_P,e_Q from F. This splits P and Q into four literal path pieces. By extremal choice, one piece on each rail contains the corresponding B endpoint u or v; call these P_B,Q_B. The other pieces contain the leaf supports L and R; call them P_L,Q_R.

Add the source edge e_B=u-v, joining P_B and Q_B into one ordinary path component. Restore z and add the two source edges of the literal bridge L-z-R at the appropriate boundary positions of P_L and Q_R. At the ordinary graph level these two added z-edges join the two leaf pieces into one path component. Thus the selected-edge set is a spanning two-component path forest on all vertices of H except p. To span H itself, retain p as part of whichever B-side piece contains the source-pivot position from C_p; if p is not already selected, use the literal source-pivot insertion as in the local-substitution packet, adding at most one further bounded seam. Equivalently one may view the construction first as an H-p two-cover and then test p insertion.

The essential point is boundedness: all unchanged turns are inherited from F, A=L-z-R, or B. The only uncertified turns lie at endpoints of e_P,e_Q,e_B, the two z-attachments, and possibly the single p insertion.

### 3. Curvature dichotomy
If every uncertified turn in the spanning proposal is tight, the two components give a spanning two-cover of H. Otherwise choose a failed turn. R3 gives its complete reverse as a tight trimer J. The failed turn contains at least one connector endpoint, z, or p, so J retains explicit source/split-star ancestry.

J is proper. The split-star source has three nonempty classes and the connector window uses only a bounded subset of them, so at least one physical vertex remains outside J. Accepted R4 currentizes J with an exact two-cover of its complement, yielding a literal maximum spanning three-forest.

Thus the B-centered split-star weave has the exact parent output

  spanning two-cover OR source-labelled current trimer curvature.

### 4. Scope
This section checks only the central class B assignment. The cases center L or center R require mixing the z-bridge and p-substitution roles differently and remain under the broader working split-star section. No descent theorem for the current trimer is claimed.

