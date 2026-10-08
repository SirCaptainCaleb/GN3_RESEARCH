# Hard seam equality packets reduce to split-hole double matching blocks — preserved pre-item development

## Development

## The hard seam equality packet is a double matching-block residue

Retain the complete matching-block endpoint residue and the oriented seam band
\[
W=\{x,y,q_2,q_1,p_m,p_{m-1}\}
\]
from [[matching_block_endpoint_rectangles_force_local_both_hole_seam_seeds]].

Assume the hard equality branch:
- \(W\) is non-Hamiltonian;
- the two inner deletions
  \[
  W-\{q_2\},\qquad W-\{p_{m-1}\}
  \]
  are non-Hamiltonian;
- the other four one-vertex deletions, at
  \[
  x,\ y,\ q_1,\ p_m,
  \]
  are Hamiltonian.

Put
\[
D=\{x,y,q_1,p_m\}.
\]
Because we are in the original complete matching-block endpoint residue, the cross-tail four-set \(D\) is non-Hamiltonian.

Apply [[sixset_deletion_graph_oriented_recomp01]] to \(W\), whose good-deletion set is exactly \(D\).

Exactly one of the following occurs.

### 1. Adjacent good-deletion overlap

The good two-deletion graph on \(D\) has two adjacent edges. Then \(W\) already contains overlapping Hamiltonian four-supports, hence enters the established bounded order-disagreement / reversal-support machinery. No new static equality residue remains.

### 2. Second matching-block structure

The good two-deletion graph has no adjacent edges. Then the six-set deletion theorem forces it to be a perfect matching on \(D\), and \(H[D]\) is a non-Hamiltonian matching-block \(K_4\) relative to the exterior pair
\[
\{q_2,p_{m-1}\}.
\]

Thus the seam packet carries two simultaneous matching-block structures:

1. the original matching-block rectangle on
   \[
   \{x,y,p_m,q_1\}
   \]
   relative to the fixed hole pair \(\{x,y\}\), with \(p_m,q_1\) in opposite orientation classes;

2. a second matching-block rectangle on the same four labels \(D\), now relative to the inner seam pair
   \[
   \{q_2,p_{m-1}\}.
   \]

There are only three possible perfect matchings on \(D\).

If
\[
\{x,y\}
\]
is one matching edge of the second structure, then its complementary matching edge is
\[
\{q_1,p_m\}.
\]
By definition of the good two-deletion graph,
\[
W-\{x,y\}
=
\{q_2,q_1,p_m,p_{m-1}\}
\]
is Hamiltonian. Hence the explicit cross-seam rail quartet is recovered immediately.

Therefore the only genuinely new equality residue is the **split-hole double matching block**, in which \(x\) and \(y\) lie in opposite matching classes for the inner pair \(\{q_2,p_{m-1}\}\). Up to exchanging \(x,y\), its matching pairs are one of
\[
\{x,q_1\},\{y,p_m\}
\qquad\text{or}\qquad
\{x,p_m\},\{y,q_1\}.
\]

So the hard seam equality branch is reduced to:
- bounded overlapping-support disturbance;
- the explicit rail four-support; or
- one of two split-hole double-matching six-label normal forms.

This reduction uses only the exact four-good equality packet, the already-proved non-Hamiltonicity of the cross-tail core \(D\), and the six-set deletion-graph theorem.
