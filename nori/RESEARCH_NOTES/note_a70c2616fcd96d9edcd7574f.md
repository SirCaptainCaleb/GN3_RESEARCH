# Global turn-star census and sharp all-dimensional imbalance theorem

- Stable ID: note_a70c2616fcd96d9edcd7574f
- Author: unspecified; session provenance retained
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, dimension-uniform, turn-census, vertex-star, sharp-moment, forcing-certificate
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11300_1
- Updated session: session_nori_r11300_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

For n>=3, let O_n be the 2^(n-2)(n-1)! coherent antipodal edge-orbit supports of full geodesics, and T_c(O) the cyclic number of color transitions along the 2n-edge antipodally complementary cycle of O. Write r(x) for the number of color-one incident edges at cube vertex x, so r(bar x)=n-r(x). Define signed vertex-star imbalance S(x)=sum_i (-1)^(c_i(x))=n-2r(x).

THEOREM 1 (global turn/star census, unrestricted): sum_(O in O_n) T_c(O) = 2(n-2)! sum_[x] r(x)(n-r(x)), where [x] denotes an antipodal vertex pair. Equivalently E_O T_c(O) = [n^2-E_x S(x)^2]/(n-1). PROOF: Each support contributes n wedge incidences in the folded cube Q_n/(x~bar x). There are 2^(n-1) binom(n,2) projective wedges; the automorphism group is transitive on them. Thus every wedge is contained in n*2^(n-2)(n-1)!/[2^(n-1)binom(n,2)]=(n-2)! supports. At x, precisely r(x)(n-r(x)) pairs of unlike-colored incident edges give projective wedge color changes. Each projective change appears twice on its 2n-edge antiperiodic cycle. Double count. Expand (n-2r)^2=n^2-4r(n-r).

THEOREM 2 (sharp range and signed-star inequality): For every legal coloring, 2<=E_O T_c(O)<=n+1 for odd n, and <=n^2/(n-1) for even n>=4. Both bounds are attained for every dimension. The lower inequality is equivalent to E_x S(x)^2 <= (n-1)^2+1. Equality on the low-energy end holds iff EVERY coherent support contains a monochromatic full geodesic. Equality on the upper-energy end holds iff every vertex has as balanced a red/blue incident star as possible: r in {(n-1)/2,(n+1)/2} for odd n or r=n/2 for even n.

PROOF: Each antiperiodic cyclic word has 2 modulo 4 transitions, at least 2. Hence E T>=2. The upper bounds use the parity-pointwise inequalities S(x)^2>=1 for odd n, S(x)^2>=0 for even n. Sharp low-energy construction: c_0(x)=x_1, c_i(x)=x_0 for i>=1. At antipodal representatives x_0=0, the red degree is x_1, producing sum_[x]r(n-r)=2^(n-2)(n-1), so E T=2. Sharp high-energy construction, even n>=4: pair (0,1) with c_0=x_2,c_1=1+x_2 and pair each (2k,2k+1), k>=1, with c_(2k)=x_0,c_(2k+1)=1+x_0. Every pair contributes one color-one incident edge, so r=n/2. For odd n>=3 use c_0=x_1,c_1=1+x_0,c_2=x_0, then each remaining pair (3,4),(5,6),... reads x_0 with opposite offsets. This yields r=(n-1)/2+x_1. All rules ignore their own direction and are odd under antipodal complementation.

THEOREM 3 (quantitative certificate for NORI1): Put Delta=(n-1)^2+1-E_x S(x)^2>=0. The fraction of coherent supports containing a monochromatic full geodesic is >=max(0,1-Delta/[4(n-1)]). In particular E_x S(x)^2>n^2-6(n-1) guarantees a monochromatic full antipodal geodesic. PROOF: T_c(O)=2+4h(O) with nonnegative integer h. The turn/star identity gives E_O h=Delta/[4(n-1)]. Every nonmonochromatic support has h>=1, so Markov bounds its fraction. For n=3,4, the universal upper bounds n+1=4 and n^2/(n-1)=16/3 are below six, giving a short direct proof of the NORI1 geodesic statement in these dimensions. For n>=5 the moment condition does not cover all legal colorings.

Independent incidence and direct-energy enumeration verifies Theorem 1 for n=3,4,5,6: projective wedge multiplicities 1,2,6,24 and support counts 4,24,192,1920. The explicit extremizers have been independently checked for every dimension n=3,...,12. Full proof and verifiers in nori_turn_star_moment_theorem.md, nori_global_turn_energy_verify.py, nori_turn_star_extremizers_verify.py. A mathematical theorem for arbitrary nonlinear legal colorings; no assumption of monochromatic connectivity or local descent. The unrestricted dimension-uniform NORI1 conjecture remains open.
