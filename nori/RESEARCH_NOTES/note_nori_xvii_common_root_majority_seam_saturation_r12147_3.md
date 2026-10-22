# Common-root odd-majority and simultaneous seam-route saturation

- Stable ID: note_nori_xvii_common_root_majority_seam_saturation_r12147_3
- Author: unspecified; session provenance retained
- Primary home: subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- Labels: NORI1, topology, integral-profile, minimum-defect
- Lifecycle: active
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12147_3
- Updated session: session_nori_r12147_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_xvii_median_three_route_telescoping_r12024_2

## Research note

# Common-root odd-majority and simultaneous phase saturation

Session session_nori_r12147_3. Work in an arbitrary antipodally odd edge coloring. Let P have twisted defect d=2r+1>=3, with red run blocks E_j, red-to-blue seam vertices z_j, majority m, and A_j=D(m,z_j)=E_(j+1) union ... union E_(j+r). The three disjoint direction sets A_j,E_j,A_(j+r) partition [n]. For arbitrary direction-simple arms H_j:m->z_j, with switch count s_j and initial/final colors alpha_j,beta_j, let K_j:z_j->bar(z_(j+r)) be the reverse of the red E_j-run. Set Gamma_j=H_j*K_j*rev(tau H_(j+r)). These are full geodesics rooted at m, with words h_j, red E_j-run, 1-rev(h_(j+r)). Consequently

D(Gamma_j)=1+s_j+s_(j+r)+beta_j-beta_(j+r)+[alpha_j!=alpha_(j+r)].

THEOREM (directionwise integral majority). Write v_j(i) for the color used in original direction i along Gamma_j. Then sum_j v_j(i)=r for every i, so the pointwise majority of the d direction-indexed profiles is all red. Indeed each i lies in r arms H_j, each of whose chosen edge occurs again with complementary color in the terminal segment of Gamma_(j-r). These r complementary pairs occupy 2r different routes; the remaining occurrence is on the red E_i-block connector. This gives compatible ORIGINAL complete path witnesses, although their majority profile need not be realizable by a path rooted at m.

SHARPNESS OF THE d INDIVIDUAL DEFECT BOUNDS. Put j_k=kr mod d, 0<=k<=2r. Choose s_(j_k)=r for even k and r-1 for odd k, with alpha_(j_k)=k mod2. Then every beta_j=r mod2. For consecutive star positions except the closing pair, the s-sum is 2r-1 and the initial phases disagree; for the closing pair the s-sum is 2r and phases agree. Thus D(Gamma_j)=d for all j. These choices can be realized in one legal edge coloring with E_j of size two, without conflicting with the prescribed doubled P-cycle: choose the first direction of H_j in E_(j+1), after which different H_j are internally vertex-disjoint, since mutual inclusion of their first directions in the other's A-set would require opposite cyclic differences both <=r-1. Positive and antipodal negative arm faces are disjoint, and a median arm face meets the doubled P-cycle only at its seam vertex. Assign the arm words, red runs and antipodal complements independently, and complete unused edge orbits arbitrarily.

The marked graph formed by those paths contains no monochromatic antipodal connected pair. For r>=2 every spoke switches; red components through either hub use portions of at most two arm supports when comparing any two vertices and omit an E-block. Each red connector attaches red spokes on at most one end, since all beta_j are equal, and its component lies in a face supported on E_j union A_j or E_j union A_(j+r). For r=1 the single zero-switch blue spoke has a red antipodal mate joining one connector inside a proper two-block face. Other red components remain in spoke interiors. Blue follows by antipodality.

SCOPE. The specified P need not be globally minimal in the completed coloring. This proves that odd-cycle arm phases, shared-edge consistency on this marked network, and integral majority alone permit equality without an internal monochromatic repair. A closure argument must exploit further original square edges and the global-minimizer constraints on additional recombined paths.

## Unbounded bounded-radius plateau under square exchanges (session session_nori_r12147_3)

**Theorem (arbitrarily deep square-exchange stability of the saturated odd-star ensemble).** For every odd integer d=2r+1>=3 and every integer k>=0, there exist n, a legal antipodally odd binary coloring of Q_n, a defect-d full geodesic P, and the d common-root seam recombinants Gamma_j from the preceding construction, such that (i) D(Gamma_j)=D(P)=d for all j; (ii) their directionwise color profiles have the all-red strict majority; and (iii) every full geodesic obtained from any member of this ensemble by at most k original two-direction square exchanges, allowing cyclic re-rooting along the SAME antiperiodic doubled geodesic between exchanges, has twisted defect at least d.

The allowed re-rooting operation sends (x,(i_1,...,i_n)) to (x xor e_(i_1),(i_2,...,i_n,i_1)), rotating the doubled color word. It is distinct from the Freudenthal CHAMBER FACET r_0(x,pi)=(x xor e_(pi_1),pi), which translates almost all later edges and is not covered by this theorem.

*Run survival lemma.* Write W=(w,1-w) for a doubled path color word, viewed on a cycle of length 2n. If its 2d maximal alternating monochromatic runs each have length at least L>2k, then every path reached using k such square exchanges and cyclic re-rootings has twisted defect >=d.

*Proof.* Cyclic re-rooting rotates W. A square exchange between two successive original directions replaces just the two intervening original edges, preserving all remaining ordered edges, so it changes at most two positions of W modulo the antiperiodic half-period. After k exchanges, track the cyclic alignment induced by the re-rootings: at most 2k antipodal pairs of word positions can differ from the starting word. Each original monochromatic run has length smaller than n (since d>=3), so each intersects at most 2k modified position pairs and retains one position of its starting color. The 2d surviving positions occur in cyclic order and alternate in color. The final doubled word therefore has at least 2d switches, giving defect >=d. QED.

*Uniform construction.* Begin with the preceding saturation construction, enlarging the d red-run blocks E_j to a common size L, with L>=(r+1)(2k+1). The starting P then has all doubled monochromatic runs of length L. Each median-arm support A_j has rL directions. In the odd-star order j_t=tr mod d, prescribe alpha_(j_t)=t mod2 and s_(j_t)=r for even t, r-1 for odd t. As before each beta_j=r mod2 and formula (M2) gives D(Gamma_j)=d. Because rL>=(r+1)(2k+1), the r+1 or r successive monochromatic runs of each H_j can all be chosen with length >=2k+1. Choose its first direction in E_(j+1), order the other directions freely, and assign the selected word. The established disjointness proof still applies: any intersection of distinct positive arms after their first edges would require contradictory opposite cyclic differences; positive and negative arm faces are disjoint; each median arm face meets the doubled P only at its seam. Thus all prescribed edges admit one legal antipodally odd coloring, extended arbitrarily on unused edge orbits. Each recombined Gamma_j concatenates two arms (the second antipodally complemented) with a red run K_j of length L, so all maximal runs of its doubled word have length >=2k+1. Apply the run survival lemma separately to P and every Gamma_j. The directionwise odd-majority theorem holds independent of arm lengths. QED.

**Limit of this theorem.** The constructed P and Gamma_j need not minimize defect among ALL cube geodesics; this establishes stability only in their bounded square-exchange neighborhoods. A chamber facet changing the root from x to x xor e_(pi_1) while retaining direction order pi generally changes n-1 edge colors at once. Accordingly no exclusion of root-facet global forcing follows from the run survival lemma. Proving unrestricted NORI1 still requires a mechanism reaching geodesics beyond the above bounded neighborhood, possibly through full Freudenthal root-facet incidence or shared derivative constraints.

FULL FREUDENTHAL FACET STABILITY (session session_nori_r12147_3). For every k>=0, set L=2k+1 and n=3L. Take the legal one-parent cyclic affine coloring c_i(x)=x_(i+1 mod n) xor alpha_i. Select alpha so the root-0, increasing-order path has temporal word 0^L 1^L 0^L and twisted defect 3. Every original square-exchange chamber facet changes at most two word positions. Every root-changing chamber facet (x,pi)->(x xor e_(pi_1),pi) changes precisely one word position, since each root direction is the parent of one edge-color function. Hence any chamber at gallery distance <=k differs from the selected word in at most 2k positions. The doubled antiperiodic word has six alternating constant runs, each of length L>2k; each run retains one color position. Therefore every chamber in this gallery ball has twisted defect >=3. Nonetheless, for each fixed direction order pi, the direction-indexed profile map x->(c_i(x xor prefix_pi(i))) is affine BIJECTIVE: its linear part is the cyclic permutation matrix. So each fixed order even has a root giving an all-red path, and its conjugate x xor F_pi(x) is a complete even- or odd-self-dual root packet, since I+P maps two-to-one onto the even-parity subspace. This obstruction includes BOTH full Freudenthal generators and preserves one global legal coloring. It rules out any universal bounded-radius descent from an arbitrary bad path, even in the presence of a transportable all-root parity packet. It does NOT construct a globally minimum bad path, and so does not refute a global-minimizer forcing theorem.
