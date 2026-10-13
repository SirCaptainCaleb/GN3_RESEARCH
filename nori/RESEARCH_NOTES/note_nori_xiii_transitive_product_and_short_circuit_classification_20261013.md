# Color-transitive product obstruction and primitive short-circuit classification

- Stable ID: note_nori_xiii_transitive_product_and_short_circuit_classification_20261013
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_xiii_binary_involutive_rainbow_paths
- Labels: counterexample, color-transitivity, short-cycle-completion, matroid-classification, minimal-strengthening
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7442_1
- Updated session: session_nori_r7442_1
- Disposition: none
- Successor: none

## Related references

- article:nori_article_xiii_binary_involutive_rainbow_paths
- article:nori_article_xi_matroidal_turn_geometry

## Research note

THEOREM A (a color-transitive logarithmic obstruction with short forward-cycle completion). Let m>=4. Write B_m for the ordered-pair overlap graph on vertices (a,b), a!=b in [m], with forward edges (a,b)->(b,c) colored c for pairwise distinct a,b,c. Let rho(a,b)=(b,a), reversing forward arcs. Form G=B_m Cartesian product B_m, coloring the first-factor edges (1,c) and second-factor edges (2,c), and put tau(u,v)=(rho v,rho u). Then G is connected, its palette contains 2m ordinary colors, and every vertex has ordinary color degree k=2m-2. Tau is an involutive automorphism with no setwise-fixed edge, since it exchanges the two Cartesian factors. The diagonal S_m alphabet action and factor interchange commute with tau and together act transitively on the ordinary colors; thus all color classes are isomorphic.

Let t=ceil(log_2 m), represent [m] by distinct binary t-words, take j(a,b) to be the highest differing bit position, and define h(a,b)=2j(a,b)+bit_j(a). The height h ranges from 0 to 2t-1 and is proper on B_m: across (a,b)->(b,c), if the two j indices coincide, the two selected bits of a,b are opposite, while unequal j indices give distinct heights. Define b1(e)=1 if h increases along the forward orientation of B_m edge e, and 0 otherwise. Define b2(e)=1-b1(rho e). Give first-factor edges binary label b1 and second-factor edges label b2. Then chi(tau e)=1-chi(e) for every edge. Along a forward edge e:u->v, the second-factor bit b2(e)=1 iff h(rho v)>h(rho u).

Every forward directed two-arc path in G can be completed into a directed cycle of length three or four. Within one factor the two-step sequence (a,b)->(b,c)->(c,d) closes in three steps total when d=a, using (c,a)->(a,b), or in four steps total when d is a fourth distinct letter, using (d,a)->(a,b). Two arcs in different Cartesian factors complete a commuting square.

Every ordinary-color-rainbow simple path P with at most one chi-switch obeys |P|<=12 ceil(log_2 m)-6. Proof: project P onto each B_m factor, omitting edges moving the other factor. This produces a walk with pairwise distinct ordinary edge colors. A forward traversal immediately followed (in the projected walk) by a backward traversal is impossible, because both edges then enter the same ordered-pair state and have its second letter as ordinary color. Therefore the projected traversal-orientation word is of the form backward^r forward^s and has at most one change. Its inherited bit word also has at most one change, since deletion cannot increase switches. On every run with constant orientation and constant bit, the proper height h, or h composed with rho, changes strictly monotonically; the run has at most 2t-1 edges. The two switch positions yield at most three such runs per factor, so the sum of lengths in both factors is at most 6(2t-1)=12t-6. Thus L1/k tends to zero. This disproves linear one-switch guarantees under ordinary-color transitivity, isomorphic color classes, and closure of all forward directed two-arcs by directed triangles or quadrilaterals. Its ordinary-color deficit is two: palette size k+2.

THEOREM B (primitivity and circuits of size at most three force the two canonical matroid families). Let M be loopless with at least three parallel classes, with every circuit of size at most three, and suppose Aut(M) acts primitively on its parallel classes. Then M is either a direct sum of equal-size rank-one uniform matroids U_{1,q}, or an equal-size parallel extension of one rank-two uniform matroid U_{2,d}.

Proof: simplify M to a simple matroid N; its circuits are triangles. Two triangles in different rank-two flats cannot share one point: deleting their common point from the union gives a dependent four-set (rank at most three) whose every triple is independent, hence a four-circuit. Thus different rank-two circuit flats are disjoint and the connected components of N are rank-two uniform blocks and singleton coloops. Their partition is automorphism invariant. A primitive action has no nontrivial invariant partition, so either all components are singletons (N free) or N consists of one rank-two block (N=U_{2,d}). Transitivity forces equal parallel-class sizes. This classifies the candidate hypotheses instead of proving their path assertion.

Together these theorems show why transitivity alone leaves obstructing independent blocks, while adding the short-circuit restriction and 2-transitivity collapses the class to the canonical examples. Neither theorem gives a minimal sufficient strengthening for the common one-switch problem.

SHARPENING. Theorem B holds with the 2-transitivity assumption replaced by primitivity (transitivity with no nontrivial invariant partition); this is the version proved above. In particular, the symmetry hypothesis can be weakened from 2-transitivity to primitivity without admitting an intermediate matroid while all circuits have size at most three.
