# Aharoni–Haxell hypergraph Hall theorem: pinning-resistant rainbow matchings

**Summary:** A matching-resistant local Hall condition for every subfamily forces one disjoint edge from each color class. The proof uses economically hierarchic triangulations and Sperner’s lemma; NORI still needs a faithful physical-path encoding.

## Statement

For finite hypergraph families H_i, if every nonempty union H_I contains a matching M_I that cannot be pinned by fewer than |I| pairwise disjoint edges of H_I, then there are pairwise disjoint representatives e_i in H_i. In rank at most r, nu(H_I)>r(|I|-1) suffices.

## Body

# Aharoni–Haxell hypergraph Hall theorem (rainbow disjoint representatives)

## Objects and exact hypothesis

Let \(H_1,\ldots,H_m\) be finite hypergraphs (set-systems) on a common ambient vertex set \(V\). Hyperedges need not have a common cardinality. For nonempty \(I\subseteq[m]\) write \(H_I=\bigcup_{i\in I}H_i\). A matching is a collection of pairwise disjoint hyperedges. For a matching \(M\subseteq H\), a **pinning family** \(K\subseteq H\) meets \(M\) if every \(e\in M\) intersects at least one member of \(K\). Here the version used in the construction requires pinning families \(K\) themselves to be matchings (their members pairwise disjoint).

**Theorem (Aharoni–Haxell, 2000; hypergraph Hall).** Suppose that, for every nonempty \(I\subseteq[m]\), there is a matching \(M_I\subseteq H_I\) which cannot be pinned by fewer than \(|I|\) *pairwise disjoint* hyperedges belonging to \(H_I\). Then there exist \(e_i\in H_i\) for all \(i\in[m]\) such that the \(e_i\) are pairwise disjoint.

For an equivalent numerical sufficient condition, define
\[
\pi_H^{\rm match}(M)=\min\{|K|:K\subseteq H\text{ is a matching and }(\forall e\in M)(\exists f\in K)\ e\cap f\ne\varnothing\},
\qquad
\operatorname{mw}_{\rm match}(H)=\max_{M\text{ matching in }H}\pi_H^{\rm match}(M).
\]
Then the hypothesis is \(\operatorname{mw}_{\rm match}(H_I)\geq |I|\) for every nonempty \(I\). A stronger (also sufficient) condition permits arbitrary, not-necessarily-disjoint pinning sets in the displayed minimum. **Terminology warning:** the literature sometimes abbreviates either pinning convention as matching width; always state which competing edge families may be used for pinning. The pairwise-disjoint convention suffices for the Sperner construction.

## Uniform bounded-rank corollary

If every edge in every \(H_i\) has size at most \(r\) and
\[
\nu(H_I)>r(|I|-1)\qquad(\varnothing\ne I\subseteq[m]),
\]
where \(\nu\) is maximum matching size, then disjoint representatives exist. Indeed, choose \(M_I\) with more than \(r(|I|-1)\) disjoint edges. Any \(|I|-1\) hyperedges, disjoint or not, meet at most \(r(|I|-1)\) members of \(M_I\), since a single vertex lies in at most one member of the matching. They cannot pin \(M_I\), and the theorem applies. For \(r=1\), this becomes the usual Hall inequality \(|\bigcup_{i\in I}H_i|\ge |I|\) when the \(H_i\) consist of singleton edges.

**Status and limitation.** This is a sufficient Hall-type criterion, not the assertion that every family admitting disjoint representatives meets the simple union matching-number bound, or even the stated matching-width condition. The original paper also develops a more delicate necessary-and-sufficient criterion involving simultaneously chosen matchings for nested index sets. Do not conflate that characterization with the sufficient condition above.

## Why the theorem is valid

Apply the economically hierarchic triangulation construction recorded separately as \`literature_aharoni_haxell_economically_hierarchic_sperner_construction\`. Its inductive edge labels are drawn from \(M_I\) on the face of the index simplex supported by \(I\). The pinning bound provides an edge disjoint from previously assigned labels along all adjacent proper faces. Sperner's lemma produces a full-dimensional simplex with all \(m\) family labels, and adjacency forces the corresponding \(m\) selected hyperedges to be disjoint. The construction entry gives the precise support, adjacency and labeling argument.

## Application test for NORI (not a theorem about NORI)

A promising application must *first* define families \(H_i\) of **realizable physical one-switch cube-path certificates**, and a conflict relation encoded by honest hyperedge intersections. It must then establish:

1. Why pairwise disjointness of one selected edge per family yields **one actual full antipodal geodesic with at most one color change**, rather than unrelated local paths; in particular, agree on the cube root, ordered seam windows, and exterior-face bits.
2. Why for every nonempty \(I\) the union \(H_I\) contains a matching resistant to fewer than \(|I|\) pairwise-disjoint pinning edges (or prove the stronger quantitative corollary).

Without the first implication the theorem cannot close the grand conjecture. The known legal \(Q_7\) proper-support rooted obstruction expressly forbids inferring a full rooted path from support coverage alone. Neither the exact Hall hypothesis nor a geometrically faithful path-certificate encoding has been established for arbitrary NORI colorings. This is a reusable mathematical *selection theorem*; the NORI bridge is an open research question.

## Sources and provenance

R. Aharoni and P. E. Haxell, "Hall's theorem for hypergraphs," *Journal of Graph Theory* **35** (2000), 83–88, DOI https://doi.org/10.1002/1097-0118(200010)35:2%3C83::AID-JGT2%3E3.0.CO;2-V . The authors explicitly identify their proof as topological. See also Gil Kalai, "Happy Birthday Ron Aharoni!" (2012), https://gilkalai.wordpress.com/2012/11/25/happy-birthday-ron-aharoni/ , and "Topological Combinatorics," lecture notes 2022, https://www.ibs.re.kr/ecopro/wp-content/uploads/2022/08/Topological-Combinatorics-4.pdf (pp. 3–9), for the matching-width and triangulation proof outline.

## Metadata

- ID: literature_aharoni_haxell_hypergraph_hall_matching_width_theorem
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
