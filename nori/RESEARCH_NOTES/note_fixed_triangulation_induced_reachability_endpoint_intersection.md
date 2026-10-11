# Induced reachability subcomplexes in one fixed cube triangulation

- Stable ID: note_fixed_triangulation_induced_reachability_endpoint_intersection
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_ix_unification
- Labels: reachability, topology, nori1
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6202_6
- Updated session: session_nori_r6202_2
- Disposition: none
- Successor: none

## Related references

- note:note_common_freudenthal_reachability_intersection_extraction
- article:nori_article_viii_edges

## Research note

Let \(Q_n\) have a binary coloring of its undirected edges, and let \(\bar a\) denote the bitwise complement of a vertex \(a\). Write \(R(a)\) for all endpoints of monochromatic geodesics starting at \(a\), allowing either color and including the length-zero path.

Fix the staircase triangulation \(T\) of \([0,1]^n\): its simplices are the convex hulls of chains of subsets of \([n]\), represented by their incidence vectors. Complementation reverses chains, so \(T\) is antipodally invariant. For every root \(a\), define the induced subcomplex
\[
K(a)=T[R(a)]=\{\sigma\in T:V(\sigma)\subseteq R(a)\}.
\]
The same triangulation is used for every root.

**Proposition.** For every vertex \(a\),
\[
|K(a)|\cap |K(\bar a)|\ne\varnothing
\quad\Longleftrightarrow\quad
R(a)\cap R(\bar a)\ne\varnothing.
\]
Either condition is equivalent to the existence of an antipodal geodesic from \(a\) to \(\bar a\) comprising at most two monochromatic consecutive subpaths.

**Proof.** In a geometric simplicial complex, two simplices intersect in their common face. Consequently
\[
|T[A]|\cap|T[B]|=|T[A\cap B]|
\]
for any two subsets \(A,B\) of its vertex set. This intersection is nonempty precisely when \(A\cap B\) contains a vertex.

Let \(v\in R(a)\cap R(\bar a)\). Choose monochromatic geodesics \(P:a\to v\) and \(Q:\bar a\to v\). Put
\[
S=\{j:a_j\ne v_j\}.
\]
The coordinates changed by \(P\) are precisely \(S\); those changed by \(Q\) are precisely \([n]\setminus S\). Hence \(P\) followed by the reverse of \(Q\) changes every coordinate once, giving the required antipodal geodesic. Reversing \(Q\) preserves its color because the edges are undirected. Conversely, the meeting vertex of two monochromatic consecutive subpaths lies in both reachability sets. A wholly monochromatic path is covered by allowing one subpath to have length zero. \(\square\)

**NORI1 rotation.** Assume additionally \(c(\bar e)=1-c(e)\). Write the resulting antipodal path as \(x_0,\ldots,x_n\), with monochromatic portions of lengths \(t\) and \(n-t\). If its colors agree, it is already monochromatic. Otherwise let the first color be \(p\), so the second is \(1-p\). The path
\[
x_t,x_{t+1},\ldots,x_n=\bar x_0,\bar x_1,\ldots,\bar x_t
\]
has color \(1-p\) throughout. Its coordinate sequence is the cyclic rotation of the original sequence, and its endpoints are antipodal. Thus an intersection for some root is equivalent to the NORI1 monochromatic antipodal-geodesic conclusion.

The induced complex uses separate endpoint witnesses: its definition imposes no requirement that all vertices of a simplex occur on one monochromatic path. The proposition only extracts a shared vertex, for which the two witnesses suffice.

**Remaining question.** Prove that some root satisfies \(|K(a)|\cap|K(\bar a)|\ne\varnothing\) for every NORI1 coloring. Antipodal covariance follows from the coloring rule:
\[
R(\bar a)=\overline{R(a)},\qquad K(\bar a)=\overline{K(a)}.
\]
These identities alone do not force intersection: the abstract assignment \(A(a)=\{a\}\) has the same covariance and disjoint antipodal pairs. This assignment is only a counterexample to the symmetry-only implication; it is not asserted to arise as monochromatic reachability.

No intersection-forcing theorem or extension yielding vertex-simple tight paths in every boundary tournament is established here.
