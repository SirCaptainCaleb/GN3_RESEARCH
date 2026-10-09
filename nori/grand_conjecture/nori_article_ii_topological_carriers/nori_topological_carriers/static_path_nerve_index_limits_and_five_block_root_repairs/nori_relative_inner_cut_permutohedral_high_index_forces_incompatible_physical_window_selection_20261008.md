# Relative Tucker inner-cut high index forces actual geometrically incompatible selected three-face windows near the cube midpoint

# Relative Tucker localization: the INNER permutohedral support-cut complex retains high index and forces a real incompatible-window pair

Let n>=7, let c be ANY active NORI ordered-three-face coloring, and fix ANY cube root x. Let K_x be the genuine free-antipodal simplicial face nerve whose vertices are ACTUAL full antipodal x-rooted geodesic direction orders π with OPPOSITE initial and final ordered three-face colors, and whose simplices are collections of these actual orders lying together in a proper permutohedron face. The team's previously proved honest index theorem gives w1(K_x/τ)^(n-3) !=0, with τ(π)=reverse(π).

Fix an integer k with 2<=k<=floor(n/2). For each nonempty proper used-coordinate support T⊂[n], let D_T be the FULL simplex of genuinely endpoint-opposed orders whose FIRST |T| directions have coordinate support exactly T. Each D_T is a simplex in K_x. Reversal carries D_T to D_(T-complement).

Define TWO equivariant subcomplexes:
  O_k=union D_T over OUTER ranks |T|<k or |T|>n-k;
  I_k=union D_T over INNER ranks k<=|T|<=n-k.
Every simplex of K_x lies in some proper permutohedron facet D_T, so K_x=O_k union I_k.

**THEOREM 1 (high index survives within the inner ranks).** For every k as above,
  **w1(I_k/τ)^(n-2k-1) !=0**, whenever the displayed exponent is nonnegative.
In particular ind_Z2(I_k)>=n-2k-1.

**Proof.** The finite equivariant cover of O_k by full simplices D_T has intersections exactly when the corresponding supports T are nested, since one coordinate order cannot have incomparable initial support sets. An inclusion chain drawn from the outer ranks has at most 2k-2 members, so the equivariant nerve has dimension at most 2k-3. It follows by the equivariant nerve map and antipodal-class naturality that w1^(2k-2) vanishes on O_k/τ. (The nerve action is free: a nonempty chain cannot contain both T and its complementary set, as they are disjoint and nonempty.) Let d=n-3 and s=d-(2k-2)=n-2k-1. If w1^s also vanished on I_k/τ, take invariant open regular neighborhoods of O_k and I_k retracting to those subcomplexes. The two local vanishings, via the relative-cohomology cup-product argument, would imply w1^(s+2k-2)=w1^d=0 on all K_x/τ, contradicting the known nonzero w1^d. Hence w1^s restricts nontrivially to I_k/τ. QED.

**THEOREM 2 (unconditional physical incompatibility of equivariantly selected three-edge windows).** Let n>=11 and put k=floor((n-5)/2), so n-2k-1>=4. For EVERY τ-equivariant choice assigning to EACH actual endpoint-opposed full x-geodesic π ONE of its ACTUAL consecutive three-edge window subpaths P_π, with P_(reverse π)=ΘP_π (where Θ is the physical antipodal complement+reversal), there exist TWO different endpoint-opposed full geodesic direction orders π,σ having the following properties:
(a) both orders lie in some common permutohedron facet H_T with k<=|T|<=n-k, so their full paths share a genuine near-central cube vertex y=x XOR T;
(b) their SELECTED actual three-edge subpaths have starting roots x(P_π),x(P_σ) with
  supp(x(P_π) XOR x(P_σ)) NOT SUBSET W(P_π) UNION W(P_σ),
where W(P) is the set of the three directions used by that subpath.
Consequently the TWO ACTUAL ordered-three-face physical windows cannot be shifted within their own free coordinate faces to a common physical starting root while retaining their real ordered physical face data.

**Proof.** The TRUE short physical-root-sheet carrier E3 of ALL length-three directed NORI paths has cohomological antipodal index EXACTLY3: by exact two-sided box nerve equivalence, it is equivariantly homotopy equivalent to the antipodal 3-skeleton of the signed n-cube boundary (Item nori_two_sided_root_sheet_helly_equivariant_exact_grand_fixedpoint_index_four_ceiling_20261008). Thus any equivariant continuous map I_k→E3 would force w1(I_k/τ)^4=0, contradicting Theorem1 as n-2k-1>=4.

Every chosen subpath P_π is automatically admitted (one three-face window), and the assignment is equivariant under the actual involutions because the chosen path at reverse π is physically ΘP_π. Suppose every edge of I_k between actual order vertices π,σ had selected two-sided root boxes intersecting. The genuine root-sheet nerve E3 is FLAG by literal coordinate-box Helly2, so this vertex assignment would extend to an equivariant simplicial map I_k→E3, impossible by the high-index obstruction. Hence some actual I_k edge πσ has disjoint physical two-sided boxes. Since both selected paths have length3, their sheet free sets equal their entire three-direction used supports M(P)=W(P). The exact NORI box pair test reduces precisely to
  B(P_π)∩B(P_σ) nonempty iff
  supp(x(P_π) XOR x(P_σ)) ⊆ W(P_π) UNION W(P_σ).
Therefore the required bad edge gives the stated genuine root-geometry incompatibility. Because πσ belongs to I_k it lies in some common inner-rank facet H_T, giving the shared physical near-midpoint vertex. QED.

**THEOREM 3 (conditional good-partial witness selection obstruction, more directly tied to GRAND closure).** In n>=12, put k=floor((n-6)/2), so the proven inner-index exponent s=n-2k-1>=5. Under hypothetical grand failure, for ANY equivariant assignment to each actual endpoint-opposed full rooted order π of SOME arbitrary ACTUAL <=1-switch partial NORI path P_π of length>=3 (the assigned good subpath need not belong to π), there must be an I_k edge πσ for which the exact TWO-SIDED box compatibility inequality FAILS:
  supp(x(P_π) XOR x(P_σ)) UNION (W(P_π)△W(P_σ))
      NOT SUBSET M(P_π) UNION M(P_σ).
Proof: otherwise the flag property extends the assignment to I_k→E_c, where under grand failure w1^5=0 by the universal index4 ceiling. This contradicts Theorem1's w1^5!=0 on I_k. The bad pair shares a near-central used-coordinate support T because its edge belongs to I_k. Thus even an arbitrary equivariant choice of certified partial good paths cannot be continuously glued inside the genuine near-middle full-path packet complex under grand failure.

**INTERPRETATION AND LIMIT.** This is a TOPOLOGICALLY FORCED, CONCRETELY GEOMETRIC DISCONTINUITY: honest near-middle endpoint-opposed full geodesics cannot all be assigned a single equivariant family of short face windows whose actual physical root sheets glue on every inner permutohedron face. It reveals where new ORDER-EXCHANGE/REPAIR cells must live. However an incompatible certificate pair is NOT by itself a full one-switch geodesic or a contradiction to the NORI coloring: it is precisely a failure of the naive path-selection lift. The missing grand-forcing theorem must exploit these forced incompatibilities to generate additional reachable paths or genuine seam repairs, rather than merely observing their existence.
