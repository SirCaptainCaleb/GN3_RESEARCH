# Induced reachability complexes in one fixed triangulation

- Stable ID: note_induced_reachability_complexes_fixed_triangulation
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_ix_unification
- Labels: reachability, topology, nori1
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6202_5
- Updated session: session_nori_r6202_2
- Disposition: none
- Successor: none

## Related references

- note:note_common_freudenthal_reachability_intersection_extraction

## Research note

# Induced reachability complexes in one fixed triangulation

Let c be a binary coloring of the undirected edges of Q_n, n≥2. Write bar a for the bitwise complement of a, and R(a) for endpoints of monochromatic geodesics from a, in either color, including a.

Fix a geometric triangulation T of [0,1]^n whose vertex set is Q_n. For example, the staircase triangulation has simplices given by chains of subsets of [n], embedded as incidence vectors. Define the induced subcomplex
K(a)=T[R(a)]={σ∈T: V(σ)⊆R(a)}.
The same T is used for every root.

**Proposition.** For every a,
|K(a)|∩|K(bar a)|≠∅
⇔ R(a)∩R(bar a)≠∅
⇔ there is an antipodal geodesic from a to bar a comprising at most two monochromatic subpaths.

**Proof.** If p belongs to both realizations, choose simplices σ∈K(a) and η∈K(bar a) containing p. In a geometric simplicial complex σ∩η is a common face. It is nonempty and therefore contains a vertex x belonging to both R(a) and R(bar a). Conversely such a vertex belongs to both realizations.

Choose monochromatic geodesics P from a to x and Q from bar a to x. Their coordinate supports are
A={i:a_i≠x_i}, B={i:bar a_i≠x_i}=[n]\A.
Thus P followed by the reverse of Q uses every coordinate once and ends at bar a. Reversing Q preserves its edge colors. The resulting geodesic comprises at most two monochromatic subpaths, with no condition on equality of their colors. Conversely splitting such an antipodal geodesic at its monochromatic partition gives a common reachable vertex. Empty subpaths are permitted. □

**NORI1 rotation.** Assume c(bar e)=1−c(e). If the two subpaths have the same color, their concatenation is monochromatic. Otherwise its edge word is i^p(1−i)^(n−p), with 0<p<n. Append its antipodal image to form a closed 2n-edge walk with word
i^p(1−i)^(n−p)(1−i)^p i^(n−p).
The n consecutive edges starting after the initial p edges all have color 1−i. Their directions are a cyclic rotation of the original permutation, so they form a monochromatic antipodal geodesic rooted at the partition vertex. Therefore existence of |K(a)|∩|K(bar a)|≠∅ for some a is equivalent to the NORI1 full-geodesic conclusion. □

**Equivariance and scope.** For the staircase triangulation the complement map τ(x)=bar x is simplicial: it takes each subset chain to a chain in reverse order. Under NORI1, R(bar a)=τR(a), and hence K(bar a)=τK(a). Equivariance by itself does not force intersection: the induced complexes L(a)=T[{a}] satisfy L(bar a)=τL(a) and have disjoint realizations for every antipodal pair. These L(a) serve only as a counterexample to an implication from equivariance alone; they are not asserted to be reachability complexes of a NORI1 coloring.

The induced-complex construction requires individual vertex reachability certificates. Vertices of a simplex may be witnessed by different monochromatic paths. Intersection decoding uses a single common vertex and the complementary coordinate supports proved above. Thus one fixed triangulation suffices for endpoint extraction without a common path witness for each simplex.

The unresolved statement is that every NORI1 coloring has some a with |K(a)|∩|K(bar a)|≠∅. No topological forcing theorem or reduction for ordinary boundary tournaments is established here.
