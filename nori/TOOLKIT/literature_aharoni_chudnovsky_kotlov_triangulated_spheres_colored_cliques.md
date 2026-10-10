# Aharoni–Chudnovsky–Kotlov: triangulated sphere fillings and colored cliques (2002)

**Summary:** The EH construction is part of a family of bounded-prior-neighbor triangulations of balls. Intermediate permissibility parameters let one trade the number of unavoidable constraints against local compatibility; the method yields multicolored cliques in graphs, not just hypergraph matchings.

## Statement

Every triangulation of S^{d-1} extends to a triangulation of B^d with at most d old-boundary neighbors per new vertex (Lemma 1.1), or by vertex insertion with at most 2d predecessors (Lemma 1.2); an interpolating (d+t,t)-filling lemma controls the exceptional neighbors. These fillings give a Sperner proof of Meshulam's colored-clique criterion (Theorem 3.3).

## Body

# Triangulated spheres and colored cliques: beyond the original Aharoni–Haxell EH lemma

**Reference.** R. Aharoni, M. Chudnovsky, A. Kotlov, *Triangulated spheres and colored cliques*, Discrete & Computational Geometry **28** (2002), 223–229, DOI https://doi.org/10.1007/s00454-002-2792-6 . Bibliographic/abstract page: https://collaborate.princeton.edu/en/publications/triangulated-spheres-and-colored-cliques/ . Full paper: https://scispace.com/pdf/triangulated-spheres-and-colored-cliques-e8wsl2ggm3.pdf . Exact theorem and lemma numbers are those in the paper.

## Geometric ingredients

Fix d>=1 and any finite triangulation T of S^(d-1).

**Lemma 1.1:** T extends to a triangulation T' of B^d with all added vertices interior and each added vertex adjacent to at most d vertices of the *original boundary triangulation T*. This controls boundary neighbors, NOT all previous vertices.

**Lemma 1.2:** There exists a ball extension constructed by successively adding interior vertices, with each new vertex adjacent to at most 2d predecessors. This controls ALL earlier neighbors and is a different, weaker numerical estimate.

The key interpolation is **Lemma 2.1**: for 0<=t<=d every T is (d+t,t)-fillable, with the precise definition below.

Let Q_t be the graph on 2(t+1) vertices obtained from a complete graph by deleting a perfect matching; Q_{-1} is empty. In an extension sequence T=T_0⊂⋯⊂T_s=T' by interior vertex insertions, an edge (v_i,u) incident to the newly inserted vertex v_i is *t-permissible* when u was not on the initial boundary T and the link of that edge (in the intermediate complex) contains a copy of Q_{t-1}. A (k,t)-filling means every inserted vertex v_i meets at most k of its predecessors via edges that are *not* t-permissible. The lemma asserts k=d+t. At t=0, all edges between two interior points are 0-permissible, recovering the original-boundary bound d. At t=d, no edge can be d-permissible in this setting, recovering total predecessor-degree bound 2d.

**Construction/proof mechanism** (paper §2). Induct on d+t. First triangulate a shell by repeatedly removing boundary-vertex caps: for a boundary vertex v, fill its (d−2)-sphere link with a (d−1)-ball using the lower-dimensional hypothesis and cone it to v, raising each relevant neighbor count by at most one; repeat until the original boundary has been replaced by a disjoint inner sphere. Second place an interior point z and repeat a cap-filling process using parameter t−1. Join newly created cells to the appropriate boundary vertex and z. Each such step introduces at most two additionally nonpermissible edges, while an embedded Q_{t-2} in a link acquires a suspension-like Q_{t-1} via v and z. The inductive bound becomes (d+t−2)+2=d+t. This proves interpolating geometric control; do not conflate the two stages or count arbitrary neighbors instead of nonpermissible ones.

## Graph-theoretic application (paper §3, Theorem 3.3)

Work in a **looped graph G** with a partition of its vertex set into nonempty colors V_1⊔⋯⊔V_m. For A⊆V(G), say G is k-narrow *with respect to A* if **every k vertices** of G have a common neighbor in A. A set A is t-free if G[A] contains **no induced copy of Q_t**. G is (k,t)-narrow if it is k-narrow with respect to some t-free A.

For nonempty I⊆[m], put G_I=G[⋃_{i∈I} V_i] and d_I=|I|−1. **Meshulam's criterion, as reproved by Aharoni–Chudnovsky–Kotlov:** if for every nonempty I either (a) G_I is 2d_I-narrow, or (b) for some 0≤t_I<d_I it is (d_I+t_I,t_I)-narrow, then G contains a clique meeting **every** color.

The paper's Lemma 3.2: a graph homomorphism from a triangulated (d−1)-sphere to a G satisfying the relevant narrowness condition extends over some triangulated d-ball. Build the index simplex face by face, extending each boundary labeling into a homomorphism on the face triangulation by this lemma. Each face remains labeled inside its allowed union of colors. Coloring each subdivision vertex by its graph vertex's color gives a Sperner labeling; a rainbow simplex maps to a colored clique. (Loops handle the possibility of equal images of adjacent triangulation vertices, but a rainbow selection necessarily has different colors.)

**Why this is a genuine extension.** The 2000 Aharoni–Haxell argument uses the d-boundary-neighbor case to select mutually compatible hyperedges. Here the *same geometric cap-filling strategy* yields a continuum of permissible-edge bounds and a colored-clique theorem for a general graph compatibility relation. The Q_t-free hypothesis is mathematically substantive: removing it invalidates the stated interpolation.

## NORI usefulness and exact open bridge

The bound is geometric/combinatorial: carefully selected triangulations bound the number **or topology** of obstructing earlier constraints. This might permit labels representing NORI physical path fragments, where a neighborhood with a particular link structure contributes less obstruction than an arbitrary conflicting neighbor.

Do not conclude that a colored clique of local path states is a real full geodesic. Pairwise compatibility of physical three-face windows need not imply simultaneous realization by one root, direction permutation, and exterior-bit assignment. An application must define the graph and prove a **clique-to-genuine-geodesic extraction lemma** before invoking the colored-clique result. The paper itself makes no statement about NORI. Related existing Toolkit entry: literature_aharoni_haxell_economically_hierarchic_sperner_construction.

## Metadata

- ID: literature_aharoni_chudnovsky_kotlov_triangulated_spheres_colored_cliques
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
