# Aharoni–Haxell economically hierarchic simplex triangulation and Sperner selection

**Summary:** An EH triangulation exposes at most |I|-1 compatible boundary constraints at a face of index set I. Inductive non-pinned hyperedge labels become a global rainbow matching through Sperner; local extension plus global compatibility.

## Statement

Every simplex has an economically hierarchic triangulation: adjacent triangulation vertices have nested supporting faces, and the neighbors of each x with smaller support span a boundary simplex. Use pinning-resistant matchings M_I to label x by a hyperedge avoiding its <|I| boundary-neighbor labels; apply Sperner for one rainbow disjoint transversal.

## Body

# Economically hierarchic triangulation and the Aharoni–Haxell Sperner mechanism

## Geometric construction lemma

Let \(\Delta^{m-1}\) have distinguished vertices \(1,\ldots,m\). For a triangulation \(T\) of \(\Delta^{m-1}\) and a triangulation vertex \(x\), define \(S(x)\subseteq[m]\) to be the vertex set of the unique smallest face of \(\Delta^{m-1}\) whose relative interior contains \(x\). Let \(N_T(x)\) be the adjacent vertices in the one-skeleton.

A triangulation is **hierarchic** if, whenever \(xy\) is a one-simplex of \(T\), the index supports are nested: either \(S(x)\subseteq S(y)\) or \(S(y)\subseteq S(x)\).

It is **economically hierarchic** (EH) if, further, for every \(x\), the vertices
\[
B(x)=\{y\in N_T(x): S(y)\subsetneq S(x)\}
\]
span a simplex of \(T\), possibly empty. (Equivalently, they are its neighbors on the boundary of the minimal supporting face.) An EH triangulation exists for every finite-dimensional simplex; this nontrivial geometric existence lemma is due to Aharoni and Haxell.

The exact numerical significance is that \(B(x)\), being a simplex in the boundary of the face supported by \(I=S(x)\), has **at most \(|I|-1\) vertices**, and all its vertices are mutually adjacent. Hierarchy prevents edges of \(T\) between incomparable supports. Existence is obtained by a recursive face-to-interior, collar/prism triangulation; see the cited construction proof/illustrations. We invoke that triangulation-existence lemma, rather than asserting an independently checked explicit coordinate formula for its vertices.

## The inductive hyperedge-labeling construction

Assume hypergraphs \(H_1,\ldots,H_m\) satisfy Aharoni–Haxell's theorem. Fix, for each nonempty \(I\), a matching \(M_I\subseteq H_I\) that **cannot be pinned by fewer than \(|I|\) pairwise disjoint hyperedges** of \(H_I\).

Optionally replace each edge occurrence \((i,e)\), \(e\in H_i\), by \(e\cup\{d_{i,e}\}\), using a *distinct private auxiliary vertex per occurrence*. Then an edge-label unambiguously determines its family color, and two new edges intersect exactly when their original edges intersect. Do **not** use one common dummy vertex per family: that would create spurious intersections and change the matching conditions.

Process vertices \(x\in T\) in increasing \(|S(x)|\). At a vertex with \(I=S(x)\), the labels already assigned to its proper-support neighbors \(y\in B(x)\) are pairwise identical or disjoint (by induction and because \(B(x)\) spans a simplex). After removing repetitions they form a matching \(K\subseteq H_I\) of size \(|K|\le |I|-1\). The non-pinning hypothesis therefore gives a member \(e(x)\in M_I\) disjoint from **every** edge in \(K\). Label \(x\) by \(e(x)\).

This is consistent with neighbors already labeled on **the same support** \(I\): they too were chosen from the *matching* \(M_I\), so any two such labels are identical or disjoint. Neighbors of strictly larger support are treated later. Thus the finished labels satisfy simultaneously:
\[
e(x)\in M_{S(x)},\qquad
xy\in T^{(1)}\Longrightarrow[e(x)=e(y)\ \text{or}\ e(x)\cap e(y)=\varnothing].
\]
The heart of the proof is the EH count \(|K|\le |I|-1\). A merely hierarchic triangulation without the economic condition might expose too many incomparable boundary constraints; pinning arguments could then fail.

## Sperner selection

Use the unique family occurrence of \(e(x)\) to give \(x\) a color \(c(x)\in S(x)\). At each original vertex \(i\), its color is \(i\). On a boundary face indexed by \(I\), all colors lie in \(I\). This is precisely Sperner's boundary condition on the triangulated \((m-1)\)-simplex.

Sperner's lemma supplies an \((m-1)\)-simplex \(\sigma\) of \(T\) whose \(m\) vertices have colors \(1,\ldots,m\). Every two vertices of \(\sigma\) are adjacent in \(T\), so their edge labels are equal or disjoint. Equality is impossible for distinct colors after the private-vertex occurrence normalization. Thus their labels are **pairwise disjoint**. The \(i\)-colored vertex supplies an edge from \(H_i\), proving the hypergraph Hall theorem.

This proves the selection result conditional only on the standard Sperner lemma and the cited EH triangulation-existence lemma; it is not a new proof of EH triangulation existence. The proof is constructive at the labeling stage once \(T\) and \(M_I\) are supplied, but neither an efficient algorithm to find \(M_I\) nor a polynomial-size EH triangulation is claimed.

## Reusable mathematical design principle

The architecture is a two-stage compatibility amplifier:

- **Local extension**: a new label is selected from \(M_I\) against at most \(|I|-1\) pairwise compatible boundary labels.
- **Global assembly**: the simplex index geometry plus Sperner forces one full rainbow simplex, whose every pair of vertices is adjacent, hence compatible.

The important ingredient is not a generic application of Sperner. It is a triangulation whose local adjacency structure turns the Hall *pinning* bound into an inductive extension rule and makes disjointness of labels certified on a single simplex.

## NORI bridge: explicit outstanding implication

For a NORI application, index faces must encode meaningful subproblems; a vertex label must represent a mathematically **realizable physical path witness**; and disjoint selected hyperedges must imply one common root, direction order, actual ordered-three-face windows and a single change. Pairwise consistency alone may still lack a joint path realization, as the existing Article II topology and Article III rooted-support obstructions warn. This precise witness-to-geodesic implication is the substantive hurdle. The EH method should not be described as a proof of NORI without supplying it and the pinning witnesses.

## Original and explanatory sources

R. Aharoni and P. Haxell, "Hall's theorem for hypergraphs," *Journal of Graph Theory* **35** (2000), 83–88, https://doi.org/10.1002/1097-0118(200010)35:2%3C83::AID-JGT2%3E3.0.CO;2-V .
Gil Kalai, "Happy Birthday Ron Aharoni!" (2012), especially sections *Special types of triangulations* and *The miracle*: https://gilkalai.wordpress.com/2012/11/25/happy-birthday-ron-aharoni/ .
"Topological Combinatorics" course notes, 4 August 2022, https://www.ibs.re.kr/ecopro/wp-content/uploads/2022/08/Topological-Combinatorics-4.pdf , especially pp. 5–9, with diagrams of the EH construction and inductive matching labels.

## Metadata

- ID: literature_aharoni_haxell_economically_hierarchic_sperner_construction
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
