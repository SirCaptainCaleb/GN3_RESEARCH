# Unique-colored certified squares admit explicit antipodal circle map; index two forces bichromatic common edge

# The exact topological meaning of the NORI certified-square edge-shadow dichotomy

Let n>=5 and c be a genuine active NORI ordered-three-face coloring. Write X=X_c for the finite cubical 2-complex of actual monochromatically certified middle-pair physical squares and all their vertices/edges. Physical cube-antipodality τ is a free involution on X. Every genuine centered monochromatic 4-geodesic of color q certifies its middle-pair physical square as color q.

Suppose the **bichromatic common-edge alternative fails**: NO physical cube edge is contained in certified physical squares of BOTH colors (equivalently the edge color sets K(e)⊆{0,1} of nori_center_square_bichromatic_edge_or_antipodally_odd_edge_shadow_20261008 all have size<=1).

For q∈{0,1}, define X_q as the cubical subcomplex formed by EVERY certified q-colored square and its boundary edges, together with **all cube vertices** (including isolated vertices). Because an actual certified edge has only one permitted color, X_0∩X_1 consists of ONLY the discrete cube vertices; no common edge, square, or higher cell occurs. Furthermore X=X_0∪X_1 and τX_0=X_1, since antipodal-reversing a genuine mono4 certificate switches its color.

**THEOREM (explicit equivariant circle factorization).** If the bichromatic common-edge alternative fails, there is an ACTUAL continuous τ-equivariant map
  f:|X| -> S^1
with f(τx)=−f(x) for every x, and the first Stiefel–Whitney antipodal cover class on the quotient satisfies
  w_1(X/τ)^2=0.
For all active NORI colorings n>=5, X is already connected by nori_certified_square_complex_connected_antipodal_one_class_20261008, so w_1≠0 and the index of X is EXACTLY ONE under the no-bichromatic-edge assumption.

**Proof (constructive, no external topology black box).** Pick one representative from each antipodal cube VERTEX pair {z,τz} and assign vertex values f(z)=+i and f(τz)=−i on the unit circle. These choices guarantee f(τz)=−f(z) on the 0-dimensional intersection X_0∩X_1.

Identify the closed RIGHT semicircle H_+={exp(iθ):−π/2<=θ<=π/2}. It contains both +i and −i, and is homeomorphic to a closed interval, hence contractible and an absolute retract for finite CW complexes. Extend the prescribed vertex function continuously over every 1- and 2-cell of X_0 with image in H_+. One explicit construction: define angular values θ(z)=+π/2 or −π/2 on vertices, extend θ affinely on each cube cell using the ordinary bilinear/PL interpolation, and set f_0=exp(iθ). Since θ lies in a convex real interval, the extension is well-defined and continuous even when different squares share edges.

Now DEFINE f on X_1=τX_0 by f(x)=−f_0(τx). On their intersection (the entire vertex set), the preassigned antipodality gives f_0(x)=−f_0(τx), so the two definitions agree. The cubical gluing lemma yields a continuous global f:X→S^1, and the definition makes it equivariant. Passing to quotient gives a map X/τ→S^1/(±1) ≅ S^1 classifying the pullback of the standard antipodal double cover. Thus w_1 is a pullback of the 1-dimensional base circle class, whose square is zero. As X connected under active NORI, w_1 itself is nonzero, proving exact index1. QED.

**COROLLARY (a conditional higher-index extraction theorem).** If an active NORI coloring has w_1(X/τ)^2≠0 on its true monochromatically certified center-square complex, then there MUST be an actual PHYSICAL cube edge contained in a monochromatic certified square of color0 AND another of color1. Thus a genuinely dimension-two equivariant obstruction cannot exist without the local bichromatic common-edge phenomenon.

**Further interpretation.** This does NOT assert that a bichromatic shared edge forces w_1²≠0: the converse is false or unproved, and the existing valid reversal-odd direction-only low-index examples have such bichromatic certificates while w_1²=0. The theorem instead isolates a precise implication: any topology strong enough to obstruct equivariant maps to S¹ automatically extracts an actual overlapping pair of opposite-color four-geodesic middle-pair certificates. This is a rigorously color-coherent refinement of the earlier abstract index-one square-complex no-go, and it makes the edge-shadow dichotomy into a concrete topological decomposition theorem. It does not close the NORI grand conjecture without a proof that either the common-edge witness can be lifted to a long connector or the no-closure hypothesis forces higher index.
