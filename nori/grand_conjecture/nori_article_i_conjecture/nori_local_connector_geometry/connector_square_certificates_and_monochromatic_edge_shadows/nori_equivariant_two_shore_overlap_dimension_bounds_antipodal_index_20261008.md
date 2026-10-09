# General two-color carrier theorem: overlap dimension k forces equivariant map to sphere S^(k+1)

# General equivariant two-color overlap-dimension theorem: topological index is bounded by dimension of genuine opposite-color overlap

**Theorem.** Let X be a finite simplicial or regular cubical complex with a FREE cellular involution tau on its geometric realization, and suppose
  X=A union tau(A)
for a subcomplex A. Put C=A intersect tau(A), which is tau-invariant. Suppose C has geometric dimension at most k>=0 and tau acts freely on |C|. Then there exists a continuous tau-equivariant map
  F:|X| -> S^(k+1)
where the target carries the standard antipodal involution.

Consequently the (k+2)-nd power of the first Stiefel–Whitney double-cover class vanishes:
  w_1(X/tau)^(k+2)=0.
In particular the cohomological Z2 index of X is at most k+1. If C is empty, X is the disjoint union of A and tau A and equivariantly maps to S^0, giving index0.

**Proof.** Use an equivariant barycentric subdivision so C is a genuine finite simplicial free-Z2 complex of dimension<=k. Select one vertex representative from each tau pair, choose for each such representative a generic vector v_i∈R^(k+1), and assign its tau partner -v_i. Choose these finitely many vectors in general linear position so every set of at most k+1 vectors coming from DISTINCT tau-orbits is linearly independent. (This is possible because finitely many determinant constraints define a proper algebraic subset of parameter space.) Since tau acts FREELY on |C|, NO simplex contains both vertices of a tau-pair. Each simplex has at most k+1 vertices, so its assigned vectors are linearly independent. The affine piecewise-linear interpolation g0:|C|→R^(k+1) of their vectors never vanishes on any simplex: a nonempty positive barycentric combination of independent vectors cannot be zero. Normalize to obtain a continuous equivariant g:|C|→S^k.

Identify the upper closed hemisphere H_+⊂S^(k+1) with the (k+1)-ball D^(k+1), whose equator is S^k. The map g on the subcomplex C⊂A extends continuously to a map G:|A|→H_+, because D^(k+1) is a convex ball and continuous maps from closed subcomplexes into a convex ball extend (e.g. extend each Euclidean coordinate by Tietze and radially project to the closed unit ball). The restriction of G to C has values in the equator. On tau A define F(x)=-G(tau x), taking values in lower hemisphere -H_+. On C the two prescriptions agree because g(tau x)=-g(x); on the rest of X the two domains have no overlap. The gluing lemma makes F continuous, and its construction is tau-equivariant.

The cover X→X/tau is the pullback under the quotient of the standard antipodal cover S^(k+1)→RP^(k+1). Its first Stiefel–Whitney class is the pullback of the generator a∈H¹(RP^(k+1);F2), and a^(k+2)=0 by dimension. Hence w_1^(k+2)=0 as claimed. QED.

**NORI application 1 (certified square edge shadow).** Let A=X_0 be the subcomplex of every actual color-0 monochromatically certified middle-pair square, its edges, plus ALL cube vertices; tau A=X_1 is the color-1 certified-square subcomplex. If NO physical edge supports monochromatic certified squares of both colors, then A intersect tau A consists exactly of the physical vertices (k=0), forcing an equivariant X_c→S¹ and w1²=0. The active NORI connected-square theorem gives nonzero w1, hence index EXACTLY1. Conversely index≥2 implies a GENUINE bichromatic common-edge certificate. This is the earlier explicit semicircle proof generalized.

**NORI application 2 (prospective higher-memory carrier).** Suppose X is enlarged to include genuine compatible mono-geodesic witness cells, with q-colored subcomplexes X_q swapped by antipodal reversal. To force index d>=2, their honest mixed-color overlap MUST have dimension >=d−1, otherwise the above theorem supplies a forbidden low-dimensional equivariant sphere map. This is a concrete topological reason why unstructured short-path square connectivity does not close the grand conjecture: higher-order Tucker arguments need correspondingly high-dimensional opposite-color witness overlap, or a different support-complement carrier.

**Guardrail.** The theorem only bounds index from ABOVE under low-dimensional overlap; it does not assert the converse that sufficiently large overlap forces high index. Nor does a bichromatic shared edge in the current square complex imply grand closure. The high-dimensional witness-overlap forcing remains unproved.
