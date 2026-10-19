# Analytic Fano quartet forcing and dimension-uniform projective row-distance rigidity

- Stable ID: note_nori_analytic_fano_quartet_row_distance_r11715
- Author: unspecified; session provenance retained
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, parity-peeling, rank-four, Fano-plane, simplex-code, analytic-proof, zero-sum-quartet, compatibility, projective-row-distance, rank-five-prospect
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11510_3
- Updated session: session_nori_r11510_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_rank4_fano_column_quartet_forcing_r11704
- note:note_43efdcdab134f6eee75a199b

## Research note

# Analytic Fano quartet forcing by projective row-distance rigidity

**RESULT.** The seven-label rank-four Fano part of the earlier parity-peeling theorem is proved without enumeration. For its seven columns there are at least three full-column-zero-sum quartets, and no more than two can be exceptional under the four-vertex parity deletion lemma. Thus some quartet can be removed legally, reducing to a three-label odd matrix, which always has a nonsingular accessible core. The former 1048576-instance Fano check is now an independent audit only; the earlier at-most-six-label base remains computer-assisted. Full hand proof: nori_analytic_fano_quartet_forcing.md.

**NORMAL FORM AND CODE DISTANCE.** In the rank-four Fano normal form use labels t in F2^3\{0}, row factors u_t=(1,z_t), column factors v_t=(eps_t,t), with sum eps_t=1 and A_ij=u_i dot v_j. Two row words differ as
  A_(a,*)+A_(b,*) = ((z_a+z_b) dot t)_(t!=0).
If unequal their Hamming distance is FOUR, never two. More generally in a full projective quotient of dimension d=r-1, differences of distinct rows have Hamming weight 2^(d-1)=2^(r-2). This is a dimension-uniform simplex-code restriction on counterexample normal forms.

**AT LEAST THREE ZERO-SUM QUARTETS.** The seven quotient-zero quartets are complements of Fano lines L. Such a quartet has full column sum zero iff line epsilon parity lambda(L)=1, since sum_t eps_t=1. The number of odd lines is odd, because every point lies on three lines. It cannot be one: if a lone line L were odd, pick a point p not on L. Summing lambda over the three lines through p counts each epsilon point once modulo two and must give one, while every contributing line would be even. Hence at least three zero-sum quartets exist.

**PAIR COMPATIBILITY LEMMA.** Two distinct zero-sum Fano quartets C,D intersect in two labels x,y. If both are exceptional, their selected omitted vertices must both lie in C intersection D. To prove this, write C\D={a,b} and D\C={c,d}. If one omitted vertex is unique to its quartet and the other is shared, the two triangle constraints prescribe opposite values on a shared edge. If both omissions are unique, at a and c, each exceptional triangle includes x,y, so A_(x,a)=A_(x,c)=A_(y,a)=A_(y,c)=0 while A_(x,y)=A_(y,x)=1. The four quotient points a,b,c,d form one affine plane with difference space span(x,y), so t_a+t_c is t_z for z equal x or y. Thus v_a+v_c+v_z=delta s with s=(1,0,0,0). Evaluating at row z gives delta=0; evaluating at the other shared row gives delta=1. Contradiction. Therefore both omissions are shared.

**NO THREE EXCEPTIONS.** If three distinct quartets C,D,E were exceptional, the pair lemma forces each omitted vertex into their triple intersection. Three Fano-complement quartets have at most one common point: only two Fano lines avoid a prescribed pair of points. Thus either contradiction immediately or all omissions equal a common z. In the latter case, let p be the second common point of C,D and q the second common point of C,E; p and q are distinct. Row p is one on four points in (C union D)\{p,z}, zero at p,z; since C union D has six points and all row sums are odd, its seventh entry is also one. Hence row p = 1+e_p+e_z. Likewise row q =1+e_q+e_z. Their difference e_p+e_q has Hamming weight two, impossible by the simplex row-distance theorem. So there are at most two exceptional quartets. With at least three zero-sum quartets, a nonexceptional one must exist.

**COROLLARY.** Legally delete its four labels. The full column sum of that quartet is zero, hence every surviving row remains odd. Every odd zero-diagonal three-label matrix has a directed three-cycle (nonsingular) or a reciprocal two-cycle reachable by first deleting the remaining label. Thus every rank-four Fano normal form admits a successful peel without exhaustive computation. Combined with column compression and the earlier finite base for <=6 vertices, this preserves the dimension-uniform rank-at-most-four geodesic result.

**HIGHER-RANK SCOPE.** In rank-five full-projective 15-label normal forms, the analogous row difference has Hamming weight eight. Among the 105 quotient-zero quartets, each odd lift has 45 or more full-column-zero-sum quartets (checked for all 16384 odd lift patterns). This is a promising incidence-vs-exception problem, but the seven-point compatibility proof does not immediately extend.

**CAVEAT ABOUT EIGHT-POINT SPLITS.** A legal eight-point affine block of zero total column sum can fail to split into two independently peelable zero-sum quartets: t=8,...,15, epsilon mask 215 and row slopes z=(11,1,12,10,5,5,4,1) provide such a witness. Its whole eight-point induced graph nevertheless peels in order (0,2,1,4,5,3,6,7). The parallel research note note_43efdcdab134f6eee75a199b has since proved full eight-point peeling by a separate exhaustive certificate, so this example limits only the two-quartet shortcut and is NOT an obstruction to that theorem or to parity peeling.

**REPRODUCTION.** nori_analytic_fano_quartet_forcing.md; nori_fano_parity_audit.cpp; nori_fano_triple_linear.py; nori_rank5_zero_quads.cpp; nori_affine8_partition_counterexample.py; archive nori_analytic_fano_research_bundle.zip. Finite Fano audit reproduces zero-sum-quartet counts three/seven and exceptional count at most two; the proof above needs none of those enumerations. NORI1 and the all-rank matrix-peeling conjecture remain open.
