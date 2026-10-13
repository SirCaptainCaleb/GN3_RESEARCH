# Frick–Wellner colorful Borsuk–Ulam: simultaneous signed covers and response maxima

**Summary:** A single point satisfies independently imposed signed-cover or face-preserving response constraints, with a permutation matching the conditions; application requires proving those cover or map hypotheses.

## Statement

For d+1 antipodal covers of S^d with cross-family signed separation, a permutation selects d+1 sets with prescribed signs and one common point. For d+1 continuous face-respecting maps of a d-simplex, one point and a permutation simultaneously maximize designated distinct components.

## Body

# Colorful Borsuk–Ulam: one point satisfying constraints across independent sphere covers

## Two simultaneous-choice theorems

**Source:** Florian Frick and Zoe Wellner, "Colorful Borsuk–Ulam Theorems and Applications" (2023 preprint, published 2025), https://arxiv.org/html/2309.14539v1 , Theorems 3.3 and 4.4.

**Theorem A (colorful antipodal sphere covering, Theorem 3.3).** Fix d≥1. For each j∈[d+1] let A_1^(j),...,A_(d+1)^(j) be closed subsets of S^d satisfying:
  S^d = ⋃_i(A_i^(j)∪(−A_i^(j))) for each j.
Assume cross-family antipodal separation:
  A_i^(j) ∩ (−A_i^(ℓ)) = ∅
for every i and every pair j≠ℓ. Given arbitrary prescribed signs s_1,...,s_(d+1)∈{−1,+1}, there is a permutation π of [d+1] such that
  ⋂_{i=1}^{d+1} s_i A_i^(π(i)) ≠ ∅.
This is a single shared point lying simultaneously in d+1 signed sets, with one set from each row and each column. Distinguish the cross-family separation hypothesis from the weaker within-family condition A_i^(j)∩(−A_i^(j))=∅ used by Meunier–Su's multilabeled Fan covering theorem. Without the stated separation hypothesis this permutation conclusion is not asserted.

**Theorem B (continuous maximum-response selection, Theorem 4.4).** Let α^(1),...,α^(d+1):Δ_d→Δ_d be continuous maps respecting faces:
  α^(i)(Δ_d^J)⊆Δ_d^J
for all i and all nonempty J⊆[d+1], where Δ_d^J is the face spanned by the vertices indexed by J. Then there exists ONE x∈Δ_d and a permutation π of [d+1] such that, for all i and all j,
  α_i^(π(i))(x) ≥ α_j^(π(i))(x).
Equivalently, the response vector of each selected map π(i) has its assigned component i among its maximal components, all at one x. This strengthens Gale's colorful KKM lemma by working with continuous simplex self-maps rather than merely set covers.

## Derivation and limitations

The sphere-cover theorem is proved by labeling barycentric subdivisions of increasingly fine centrally symmetric triangulations according to different cover families, then applying a signed-label Fan alternative. The face-preserving map theorem is obtained by applying a colorful Borsuk–Ulam statement to the two-fold deleted join of the simplex, then selecting a full row-column transversal of response maxima.

NORI exploration: construct a shared continuous parameter x encoding consistent choices among partial paths, with one family recording eligibility of an ordinary edge color and another recording compatibility with a chosen binary-phase ordering. This theorem is an especially direct form of simultaneous feasibility: independent response maps agree on a shared x, with distinct assignments. However, its assumptions are highly structured (face-preserving maps or signed antipodal covers with cross-family exclusion). Arbitrary ordinary and binary graph edge colorings do not supply such maps or covers automatically. Moreover, response maxima alone do not certify a vertex-simple path, a rainbow word, or at most one bit switch. Those implications would require separate proofs.

Theorem 3.4 in the same article restates Meunier–Su's multilabeled Fan covering theorem with a within-family exclusion, giving for each family an alternating signed list of d_j+1 memberships, with ∑d_j=d, on one shared intersection point. This statement may be closer to independent binary-label constraints than Theorem A, since it does not require cross-family antipodal separation, but it produces alternating faces rather than a low-switch path. See separate Toolkit entry literature_meunier_su_multilabeled_sperner_fan_simultaneous_simplex.

Primary source: https://arxiv.org/html/2309.14539v1 , Theorems 3.3, 3.4 and 4.4.

## Metadata

- ID: literature_frick_wellner_colorful_borsuk_ulam_simultaneous_cover_selectors
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
