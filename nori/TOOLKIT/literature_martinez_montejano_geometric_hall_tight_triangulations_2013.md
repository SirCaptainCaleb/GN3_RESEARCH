# Martínez–Montejano: geometric Hall variants via tight Sperner triangulations (2013)

**Summary:** Aharoni–Haxell's geometric proof works outside hypergraphs: tight simplex triangulations can force rainbow geometric selections under suitable Hall-type abundance hypotheses. Exact numerical thresholds must be checked in the full original paper.

## Statement

The 2013 work extends the Aharoni–Haxell topological triangulation technique to geometric rainbow selection: linear Hall-type conditions for pairwise disjoint unit balls in Euclidean space, and quadratic Hall-type conditions for planar points in general position.

## Body

# Geometric Hall-type results using tight triangulations

**Reference:** L. Martínez-Sandoval and L. Montejano, *Geometric variants of Hall's Theorem through Sperner's Lemma*, Electronic Notes in Discrete Mathematics **44** (2013), 127–132, DOI https://doi.org/10.1016/j.endm.2013.10.020 . Primary publisher abstract: https://www.sciencedirect.com/science/article/pii/S1571065313002369 . Related 2014 preprint *Geometric Hall's Theorems* is indexed at https://www.researchgate.net/publication/263658084_Geometric_Hall%27s_Theorems .

## Verified results (abstract-level)

The authors present and extend the Aharoni–Haxell technique based on Sperner's lemma and **tight triangulations of the index simplex**. Their reported conclusions include:

1. **Euclidean equal-radius balls:** A *linear* Hall-type lower bound is sufficient for a rainbow choice of pairwise disjoint unit balls in R^d.
2. **Planar points:** A *quadratic* Hall-type lower bound is sufficient for a rainbow choice of points in general position (no three selected points collinear).

The later preprint abstract says the treatment starts with a linear Hall-type condition for a rainbow independent set in a graph and derives the unit-ball result, before treating planar general-position points. These results show the triangulation method can handle geometric intersection and geometric dependence rather than only hyperedge disjointness.

**Precision limitation:** I verified publication metadata and the two qualitative theorem descriptions from publisher/preprint abstracts, **not** a complete accessible theorem-and-proof text for the 2013 article. Accordingly NO numerical coefficient, universal general-rank claim, or unconditional extension assertion is recorded here. For exact Hall functions, prescribed forbidden configurations and dimensions, consult the paper. A general-position condition on d-dimensional points (all ≤d+1 affinely independent) is not identical to pairwise compatibility when d≥2.

## Follow-on with fully checkable statements

Holmsen, Martínez-Sandoval and Montejano, *A geometric Hall-type theorem*, Proceedings AMS **144** (2016), 503–511, https://arxiv.org/abs/1412.6639 , gives fully written theorem/proof with O(k^d) Hall functions, topological connectivity, a q-star completion lemma and extension to matroid uniformity complexes. See separate NORI Toolkit entry literature_holmsen_martinez_montejano_general_position_complex_q_star_2016.

## NORI takeaway, not a consequence

This is an example of geometric compatibility conditions being fed into a Sperner/EH-style mechanism. The possibility worth testing is whether rich NORI path labels can be given a geometric/simplicial compatibility system. No general bound on the number of NORI-compatible labels and no extraction of a single full physical antipodal geodesic follows from the cited statements.

## Metadata

- ID: literature_martinez_montejano_geometric_hall_tight_triangulations_2013
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
