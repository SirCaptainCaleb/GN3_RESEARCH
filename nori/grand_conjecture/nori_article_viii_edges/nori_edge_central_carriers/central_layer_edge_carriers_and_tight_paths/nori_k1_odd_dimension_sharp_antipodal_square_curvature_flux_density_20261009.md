# Sharp odd-dimensional antipodal edge-color curvature: at least 2^(n−2) odd physical squares, attained by functional matchings

# Sharp global cubical curvature forced by antipodally odd physical EDGE coloring

Fix n>=3 ODD. Color every ACTUAL undirected physical edge of Q_n with a bit c(e), obeying the antipodal law c(bar e)=1+c(e) in F2. Regard c as a cubical 1-cochain. For every physical 2-dimensional square face F, define its F2 CURVATURE (coboundary)
  K(F)= Σ_(four physical boundary edges e of F) c(e) mod 2.
Antipodal oddness implies K(bar F)=K(F), since four edge complements sum to0 modulo2. A square has K(F)=1 iff its four edge colors have ODD parity (one color appears three times, the other once). Let N_odd be the number of DISTINCT physical square faces of Q_n with K=1.

**THEOREM (sharp odd curvature density).** For EVERY odd n>=3 and EVERY legal antipodally odd physical cube edge coloring:
   N_odd >= 2^(n-2).
Equivalently among the binom(n,2)*2^(n-2) ACTUAL square faces, at least the fraction 1/binom(n,2) has odd edge-color parity. The inequality is SHARP for every odd n>=3. No affine, root-symmetry, or probabilistic assumption is imposed on c.

**Proof 1 (antipodal loop + finite square filling).** Fix ANY root x and ANY permutation p=(p_1,...,p_n) of the n coordinate directions. Let P be the genuine n-edge geodesic from x to bar x in direction order p. Let bar P be its physically ANTIPODAL copy, beginning at bar x and ending at x, using the SAME order p. Concatenate to form an actual closed 2n-edge walk C=P*(bar P). Each second-half physical edge is the antipodal mate of the corresponding first-half edge, and their colors are opposite. Hence its mod2 edge-color circulation is
   <c,C> = Σ_(e in P) ( c(e)+c(bar e) ) = n =1 mod2.

The cubical Q_n is contractible and every reordering of a coordinate-distinct cube geodesic is achieved by adjacent swaps of direction steps, each swap bounding one ACTUAL physical 2-dimensional square. Starting with bar P (order p from bar x to x), change the order of its n distinct steps to REVERSE(p), by exactly binom(n,2) adjacent swaps (a fixed bubble-sort inversion sequence). After this reordering the second-half path exactly traverses P in reverse, so the resulting 2n-walk cancels edge by edge. The binom(n,2) physical squares swept out in the adjacent swaps give an ACTUAL finite cubical 2-chain D_(x,p) with boundary C over F2. The cubical Stokes identity therefore gives
  Σ_(F in D_(x,p)) K(F) = <c,C> =1 mod2.
In particular EVERY such canonical square filling contains at least one odd-curvature square. The filling comprises exactly one physical square in each unordered coordinate pair {i,j}, because bubble sorting the reverse order exchanges each pair once, and so contains binom(n,2) DISTINCT physical squares.

Now fix p and translate x UNIFORMLY through all 2^n cube vertices. Every canonical square of a fixed direction pair {i,j} translates uniformly over its 2^(n-2) distinct parallel physical squares; each physical face has 4 hub representatives. Therefore
  E_x[ # odd-curvature squares in D_(x,p)]
   = Σ_(i<j) (# odd physical {i,j} squares)/2^(n-2)
   = N_odd/2^(n-2).
The count on the left is an ODD nonnegative integer and hence at least1 for EVERY x. Averaging yields N_odd/2^(n-2)>=1. QED.

**Proof 2 (cohomological restatement).** The edge 1-cochain c obeys c(bar e)=c(e)+1. The canonical antipodal 2n-loop C has nonzero F2 circulation n mod2=1. Its cubical disk filling is a 2-chain D with <delta c,D>=<c,boundary D>=1, forcing nonzero curvature, and averaging antipodal translates supplies the sharp quantitative bound above. This is a curvature/holonomy obstruction, not a proof of a monochromatic full geodesic.

**SHARPNESS CONSTRUCTION.** For odd n=2m+1>=3, pair 2m of the coordinate indices into disjoint unordered pairs (1,2),(3,4),...,(2m-1,2m), leaving one index r=2m+1. Define a loopless coordinate-dependency FUNCTION f by f(2s−1)=2s and f(2s)=2s−1 for all s=1,...,m, and f(r)=1. Color every actual undirected direction-i physical edge through vertex x by
   c_i(x)=x_(f(i)).
This is a valid physical edge coloring because f(i)!=i, and it is antipodally odd because complementing all cube bits toggles its one input bit. On a square with free directions i,j, the curvature equals
  K_(i,j)=1{f(i)=j}+1{f(j)=i} mod2,
independent of its other fixed bits. The paired indices give reciprocal arcs and curvature0 on their mutual square families; every other pair has no arc except the UNIQUE unreciprocated edge r->1. Thus K=1 EXACTLY on all the 2^(n-2) physical squares with directions {r,1}; all other physical square faces have K=0. Consequently N_odd=2^(n-2), equality. QED.

**Local physical connector corollary.** Every odd-curvature physical square has exactly one minority-colored edge and three majority-colored edges. It therefore contains exactly TWO distinct MONOCHROMATIC length-two CUBE geodesics, each between one pair of its opposite cube vertices, both of the majority edge color: one avoids the minority edge through one corner, the other avoids it through the other. These 2-edge paths are distinct across different physical square faces because their actual two-coordinate support and unique containing square are determined by the path. Hence every antipodally odd edge coloring in ODD dimension has at least 2^(n-1) distinctly situated monochromatic length-two cube geodesic certificates arising just from its forced nonzero-curvature squares. This is a quantitative LOCAL theorem, not full antipodal closure.

**Exact parity divide.** For EVEN n, the same canonical antipodal loop has <c,C>=n mod2=0, and the curvature argument imposes no nonzero bound. In fact choose a fixed-point-free involution f pairing ALL n coordinate indices and c_i(x)=x_(f(i)); then all A_ij=A_ji and every physical square has curvature0, while the antipodal odd edge law still holds. Thus the odd-dimensional curvature lower bound cannot be extended unchanged to EVEN n. Combined with the proved dimension-lifting theorem nori_k1_counterexamples_lift_across_dimensions_by_doubled_facets_20261009 (the unrestricted edge conjecture would follow from proving all even dimensions), this exposes a precise reason a purely first-curvature-flux proof is insufficient: a global even-dimensional proof must use a different or higher-order invariant.

**Frontier.** Seek a coupling of multiple odd-curvature square connectors that forces a full monochromatic geodesic, or a SECONDARY topological obstruction usable in even dimension when the first curvature class vanishes. The result rigorously realizes cubical holonomy and topological compression using ACTUAL physical edge squares; it should not be transferred to active ORDERED THREE-FACE NORI without a separate compatible-window analysis.
