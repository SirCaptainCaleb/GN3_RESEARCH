# Andrade–Rodríguez Rey–Ruiz Sandoval: loopless matroid Sperner theorem and ordered-flat symmetry (2015)

**Summary:** Loopless face-flat matroid labeling guarantees a basis simplex by a nested-flat Sperner argument; loops are a genuine obstruction. Permuting ordered bases permutes induced labelings, not necessarily the triangulation or a NORI path.

## Statement

For a loopless rank-(d+1) matroid labeling of a triangulated d-simplex, if the outer labels form a basis and every triangulation vertex on an outer face is labeled inside the flat it spans, some d-simplex has labels forming a matroid basis. Allowing matroid loops invalidates the blanket statement. Ordering an outer basis gives nested flat chains and induced Sperner labelings, which change equivariantly under permutations of that ordered basis.

## Body

# Matroid generalization of Sperner: corrected hypotheses and ordered flat-chain mechanism

**Primary manuscript:** Gabriel Passamani Andrade, Andrés Rodríguez Rey and Alberto J. Ruiz Sandoval, *A Matroid Generalization of Sperner's Lemma*, November 7, 2015 (MSRI-UP).
**Full source:** https://gpandrade.github.io/MSRIREUPaperZ.pdf
**Locations:** Theorem 1.1 and loop counterexample, pp. 1, 7–9; corrected Theorem 3.1, Corollary 3.2 and Lemma 3.3, pp. 8–9; Theorem 3.4, pp. 10–11; Theorem 4.4 and Lemma 4.5, pp. 17–19.

## Corrected matroid-Sperner theorem (Corollary 3.2)

Let K triangulate a d-simplex Δ, and let each vertex of K carry an element of a **loopless** matroid M of rank d+1. Suppose the labels b_1,...,b_{d+1} of the outer vertices form a basis B, and each vertex of K lying on the outer face spanned by a subset A⊆B has its label in cl_M(A). Then some top simplex of K is labeled by a basis of M.

The paper exhibits a loop-containing matroid labeling for which the unqualified Lovász claim fails. Looplessness is a hypothesis ensuring the general result; it does not say that every particular instance with a loop lacks a basis simplex.

## Ordered-flat-chain reduction to Sperner (Lemma 3.3)

Order B=(b_1,...,b_{d+1}), and define F_i=cl_M({b_1,...,b_i}), with F_0=cl_M(∅)=∅ by looplessness. Label a triangulation vertex with matroid element e by the least i for which e∈F_i. The face-flat condition makes this an ordinary Sperner labeling: the fundamental circuit of e relative to B is supported among the outer basis labels spanning any face whose flat contains e, so its final basis index belongs to that face.

A fully labeled elementary d-simplex has one matroid element e_i in each F_i\F_{i-1}. Such e_i are independent: inductively e_1,...,e_{i-1} lie in F_{i-1}, while e_i does not. Their d+1 elements form a matroid basis.

This construction is a general *independence certificate from a nested chain of flats*, not a dimension-simple path theorem.

## Basis-order action (Theorem 4.4)

The flats cl_M(S) for S⊆B form a Boolean sublattice. An ordering of B selects a maximal flag through this lattice and an induced Sperner labeling. The permutation group S_{d+1} acts by permuting the basis ordering and the associated flags, hence on the **family of induced labelings**. This is not an asserted free action on K and does not by itself provide antipodal equivariance.

## Additional scope notes

Theorem 3.1 states a two-basis-simplex claim on a d-dimensional manifold given one basis simplex and looplessness. Its manifold hypothesis requires care: it must not be misapplied to a simplex or other manifold with boundary, where a single top simplex may be the only basis simplex. Theorem 3.4 discusses a rank-two, one-dimensional lower bound in the presence of a three-element circuit; its use presumes the labeling regime of the paper, including occurrence of the relevant matroid labels. The work discusses higher-dimensional multiplicity as a further direction, not as a universal established bound.

## Possible use in NORI and other research

- Build a genuine simplicial complex of admissible partial-path states, and identify a loopless matroid whose independence captures distinct dimensions or other needed conditions.
- Prove the **face-flat boundary condition**, not merely abstract independence of labels, before invoking the theorem.
- Use changes in the ordering of B as a tool for organizing Freudenthal or Coxeter flags and potentially chain-level transitions.
- Supply a separate **decoding theorem** showing that a basis simplex produces ONE compatible ordered geodesic or tournament tight path with all prescribed distinctness, endpoints and switch constraints.
- Do not infer an antipodal-odd map, a path, or a low-switch word directly from the matroid basis condition.
- Monitor loops and other rank-zero elements in proposed encodings: they can invalidate the Sperner reduction.

**Status:** Literature reference summarizing a 2015 manuscript; not a new NORI proof. Keep the corrected hypothesis and the limitations when applying this toolkit entry.

## Metadata

- ID: literature_andrade_rodriguez_rey_ruiz_sandoval_matroid_sperner_2015
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
