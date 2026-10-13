# McGinnis matroid-colored KKM: independent choices with one common intersection

**Summary:** KKM-style topology selects a matroid-independent full family, a shared intersection, and convex balance simultaneously; path coherence and one-switch extraction remain additional tasks.

## Statement

For a rank-k matroid M and an M-Komiya cover of a (k−1)-polytope P, there is a matroid basis w_1,...,w_k and faces σ_i whose indexed cover sets have a common point, while prescribed points on the faces have convex hull containing any chosen p∈P.

## Body

# McGinnis's matroid-colored Komiya–KKM theorem

## The theorem

**Reference:** Daniel McGinnis, "Matroid colorings of KKM covers" (2024), Theorem 1.6, https://arxiv.org/html/2409.03026v2 .

Let P be a polytope of dimension k−1, let p∈P, and let M be a finite matroid of rank k on ground set W. Let F(P) denote the nonempty faces of P. For each w∈W and σ∈F(P), choose a closed set A^w_σ⊆P and a point y^w_σ∈σ.

A Komiya cover of P is a family (A_σ) indexed by its nonempty faces satisfying, for every nonempty face τ:
  τ ⊆ ⋃_{σ∈F(P), σ⊆τ} A_σ.

The doubly indexed family (A^w_σ) is an **M-Komiya cover** if, for every G⊆W with matroid rank r_M(W\G)≤k−1, the sets indexed by G combine to give a Komiya cover:
  for every τ∈F(P),
  τ ⊆ ⋃_{σ⊆τ} ⋃_{w∈G} A^w_σ.

**Theorem (McGinnis, Theorem 1.6).** Under these assumptions there exist a matroid basis {w_1,...,w_k} of M and nonempty faces σ_1,...,σ_k of P such that simultaneously
  ⋂_{i=1}^k A^{w_i}_{σ_i} ≠ ∅,
  p ∈ conv{y^{w_i}_{σ_i} : 1≤i≤k}.
The theorem also allows all sets in the cover to be open in place of closed.

This is a simultaneous *matroid independence + common intersection + convex balance* selection theorem. Its KKM-like covering hypothesis is imposed not independently on each w but on every G whose complement fails to span M. The ordinary colorful KKM theorem of Gale is a specialization involving a partition matroid. Soberón's sparse-colorful KKM theorem is a specialization involving a uniform matroid.

## Why this bears on two separately handled NORI colorings

A potential bridge would place the ordinary edge-color distinctness condition into an auxiliary independence matroid on candidate transition slots. The binary parity labeling remains an independent input determining allowed sets A^w_σ. Then McGinnis's theorem can select a matroid basis whose admissibility sets have a common point. This is closer to a direct conjunction of conditions than encoding an entire graph using an oriented matroid.

However, the matroid must describe a legitimate independence condition on selections. Even if matroid independence enforces pairwise distinct colors, it does not by itself ensure selected transitions can be arranged in a graph path. Nor does a common intersection guarantee a one-switch binary word. The essential unproved tasks are:
  (i) choose a parameter polytope P whose points represent legal path states or coherent families of such states;
  (ii) verify the M-Komiya covering property from the two motivating instances;
  (iii) show that basis-plus-intersection-plus-convex-balance yields one vertex-simple path with distinct ordinary colors and no more than one binary switch.
A candidate failing any one of these tests does not constitute a NORI proof. No additional condition is imposed on the binary colors beyond the given vertex-involution reversal law.

## Nearby literature

Soberón's sparse colorful KKM theorem, reproduced as Theorem 1.3 in McGinnis: n≥k and n families (A_i^j) on Δ^(k−1), with the union over any n−k+1 families satisfying KKM, force an injection π:[k]→[n] and ⋂_{i=1}^k A_i^{π(i)} nonempty. The full face-covering assumption is necessary; merely having many sets or large color degree is insufficient.

For comparison: the Toolkit already contains Gale's colorful KKM in literature_fixed_point_theorems, Kalai–Meshulam's topological Hall principle in literature_holmsen_martinez_montejano_general_position_complex_q_star_2016, and Aharoni–Haxell's Sperner hypergraph Hall theorem. This entry adds a separate matroid-constrained intersection principle absent from those records.

Primary source: https://arxiv.org/html/2409.03026v2 , Definitions 1.2, 1.5 and Theorem 1.6.

## Metadata

- ID: literature_mcginnis_matroid_colored_kkomiya_kkm_simultaneous_selection
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
