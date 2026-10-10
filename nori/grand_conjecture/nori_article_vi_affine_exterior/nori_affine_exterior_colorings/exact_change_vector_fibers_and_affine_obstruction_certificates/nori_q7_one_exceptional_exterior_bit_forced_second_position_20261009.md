# Q7 single-exceptional-exterior-coordinate family: full closure with g second

# Exact Q7 closure with one exceptional exterior coordinate: g can be SECOND

Fix a distinguished coordinate g of Q_7 and put R=[7]\\{g}. Consider any legal antipodally reversal-odd coloring of physical ORDERED three-faces satisfying the following one-bit dependence restriction:
(i) for an ordered free triple t containing g, its color h(t) depends only on the ORDER of its three free directions (and h(reverse t)=1−h(t));
(ii) for an ordered free triple t⊂R, its color depends only on t and the fixed exterior g-bit. Writing f(t) for g-bit 0, the NORI symmetry forces the g-bit 1 color to be 1−f(reverse t). All fixed residual R-coordinate bits are irrelevant.
No restriction on f(t) versus f(reverse t) is imposed. The exterior derivative in direction g may vary arbitrarily across ordered triples. This class is generally NEITHER coordinate-only NOR universal-flipper.

**Computer-verified theorem (exact finite encoding).** Every such coloring admits a good FULL Q_7 antipodal geodesic with g as the SECOND direction. By antipodal reversal of the full geodesic, g may equivalently be sixth. This resolves the complete 165-parameter class, independently of the previously proved one-universal-flipper theorem.

**Encoding and reproducibility.** There are 6·5·4=120 free f(t) values for no-g ordered triples. The g-containing ordered triples number 3·6·5=90, paired by direction reversal into 45 free h values. Thus 165 Boolean variables. For every 6! order p with g second and each of the two initial g bits, compute the five consecutive actual ordered-three-face colors along the full direction-distinct cube path. All other initial bits are irrelevant by hypothesis. Forbid each of the ten binary five-window words with 0 or 1 color switch. There are 6!·2·10=14400 distinct 5-literal clauses. The 165-variable conjunction is UNSAT in Z3; a standalone direct encoding appears as script nori_q7_onebit_position_sat.py (select subset (1,)), which prints '(1,) 14400 unsat'. Consequently every legal choice h,f has a good full path with g second.

**Correctness of face-to-word realization.** For a window containing g its color is the actual h(t) and is independent of root. For a window omitting g, the physical fixed g-bit at that window equals x_g plus the indicator that g has already been traversed. If that bit is zero use f(t); if it is one use 1−f(reverse t). Since g occurs second, every no-g window follows its flip, and the two root-g choices exhaust the two legal suffix tables. Every full order with g second is included.

**Proof status.** A finite UNSAT computation proves the result relative to the exact SAT generator and solver. Independent DRAT/LRAT or conceptual proof of the (1)-position forcing would elevate its certification. The unrestricted NORI grand conjecture allows dependence on the remaining exterior bits and is open.

**Sharp positional warning.** The complementary explicit Item nori_q7_exceptional_onebit_fixed_middle_position_no_go_20261009 constructs a legal member of THIS SAME class in which NO good full geodesic has g third or fifth. Thus a flexible position choice is essential even in this highly structured 165-variable family.
