# Meunier–Su multilabeled Sperner and Fan: simultaneous constraints in one simplex

**Summary:** One simplex simultaneously fulfills quotas for independent labelings. Sperner quotas measure distinct values; Fan quotas measure alternating faces, not low-switch paths.

## Statement

For m independent Sperner labelings of a triangulated (n−1)-simplex, prescribed positive quotas k_i summing to m+n−1 occur simultaneously as distinct-label counts on one simplex. For m Fan labelings of a free Z_2-complex, quotas d_i summing to its equivariant index yield alternating faces in a single simplex.

## Body

# Multilabeled Sperner and Fan theorems: simultaneous patterns on one simplex

## Theorems (Meunier–Su, 2019)

**Theorem A (multilabeled Sperner, Theorem 2.1).** Let T be a triangulation of the (n−1)-simplex Δ^(n−1). Let ℓ_1,...,ℓ_m : V(T)→[n] be **independent Sperner labelings**: at a triangulation vertex lying in the face spanned by J⊆[n], every ℓ_i takes a value in J. Given positive integers k_1,...,k_m with
  k_1+...+k_m = m+n−1,
there exists ONE simplex σ∈T such that, for each i, the set ℓ_i(V(σ)) contains at least k_i distinct labels. Moreover σ can be chosen so that every label j∈[n] is used by at least one of the m labelings on σ.

For m=2 and k_1+k_2=n+1, one simplex has at least k_1 distinct first-label values and at least k_2 distinct second-label values simultaneously. In particular the symmetric choice k_1=⌊(n+1)/2⌋, k_2=⌈(n+1)/2⌉ is guaranteed.

**Theorem B (dual label-multiplicity statement, Theorem 2.1).** Given positive integers q_1,...,q_n with sum q_1+...+q_n = m+n−1, there is ONE simplex τ∈T such that for every j∈[n], at least q_j of the m labelings use j on some vertex of τ. The distributions in the two statements are independently prescribed and need not hold on the same simplex unless established by another argument.

**Theorem C (multilabeled Fan, Theorem 3.1).** Let K be a free simplicial Z_2-complex with involution x↦−x, and set d=ind(K), the least r for which an equivariant continuous map |K|→S^r exists. Let f_1,...,f_m be Fan labelings of its vertices by nonzero signed integers, each satisfying f_i(−v)=−f_i(v) and forbidding adjacent vertices labeled +a and −a. For any nonnegative d_1,...,d_m with ∑d_i=d, there is ONE simplex σ of K such that, for every i, σ has a face of dimension d_i whose f_i-labels alternate in sign when ordered by increasing absolute value. The alternating faces for different labelings may differ: the statement is simultaneous within a simplex, not necessarily within one face.

In the two-label case, d_1+d_2=ind(K). This is a shared topological budget across two independent antisymmetric labelings.

## Proof mechanisms

Theorem A is proved using a triangulation of the product Δ^(m−1)×Δ^(n−1) that refines Δ^(m−1)×T, a polytopal Sperner argument, and a Hall-type incidence calculation. Theorem C applies an ordinary Fan/Tucker labeling to the barycentric subdivision, recording the first labeling failing its assigned alternating-face quota.

## Earlier permutation-based related theorem

Bapat (1989) showed that n independent Sperner labelings of a triangulation of Δ^(n−1) have a top simplex together with a bijection between its vertices and its labelings such that the n chosen labels are pairwise distinct. This is a discrete counterpart of Gale's colorful KKM theorem already included in Toolkit literature_fixed_point_theorems. Bapat's result assigns different labelings to different vertices; Meunier–Su gives per-labeling diversity quotas on one shared simplex. Do not conflate the two conclusions.

## NORI relevance and barriers

Ordinary edge colors λ and binary edge bits χ are logically separate. A possible application would construct one simplicial complex of admissible partial-path data, with two independently defined face-respecting labelings: one recording extension/distinct-color conditions, another recording binary switch or parity conditions. Theorem A supplies simultaneous diversity on one simplex. Theorem C is more suited to a free vertex involution and independent antipodal-odd labelings.

However, the theorems do not automatically imply that a simplex represents an ordered path, that its labels yield distinct edge colors in the order of traversal, or that alternating faces force at most one bit switch. Indeed the alternating-face conclusion demands alternation of signed labels and is not itself a low-switch bound. These decoding implications must be proved separately. Never treat pairwise compatible partial paths as one path without a valid assembly lemma.

## Primary sources

Frédéric Meunier and Francis Edward Su, "Multilabeled Versions of Sperner's and Fan's Lemmas and Applications," SIAM Journal on Applied Algebra and Geometry 3 (2019); https://arxiv.org/html/1801.02044v3 , Theorems 2.1 and 3.1, sections 2.3 and 3.2.
R. B. Bapat, "A constructive proof of a permutation-based generalization of Sperner's lemma," Mathematical Programming 44 (1989), 113–120, DOI https://doi.org/10.1007/BF01587081.

## Metadata

- ID: literature_meunier_su_multilabeled_sperner_fan_simultaneous_simplex
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
