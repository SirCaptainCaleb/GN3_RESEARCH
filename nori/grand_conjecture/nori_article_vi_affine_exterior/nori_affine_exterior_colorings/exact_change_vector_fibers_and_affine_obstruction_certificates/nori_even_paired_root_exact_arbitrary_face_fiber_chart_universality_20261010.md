# Any paired-root window maps with one omitted parameter are simultaneously realized by a legal NORI coloring

# Exact universality of the physical paired-root chart on one prescribed direction order

Let n=2m>=6 and p=(p_1,...,p_{2m}) be a fixed permutation of cube directions. For each b=(b_1,...,b_m) in F_2^m choose the genuine initial cube vertex x(b) by
x_(p_(2j−1))=1−b_j,   x_(p_(2j))=b_j (1<=j<=m).
Write W_i(b) for the color of the actual ordered three-face traversed by consecutive directions (p_i,p_(i+1),p_(i+2)) on this full antipodal geodesic, 1<=i<=2m−2.

Define omitted-parameter indices psi(2j−1)=j and psi(2j)=j+1.

**THEOREM (exact paired-root universality).** A family of arbitrary Boolean functions w_i:F_2^m→F_2, i=1,...,2m−2, can occur as the full physical window-color maps W_i(b)=w_i(b) simultaneously for SOME legal antipodally reversal-odd coloring of physical ordered three-faces of Q_(2m) if and only if each w_i is independent of the parameter b_(psi(i)). There are exactly
    2^((2m−2)2^(m−1))
distinct such order-chart word maps, all realizable. Every resulting path is a genuine length-2m antipodal cube geodesic.

**Proof (necessity).** For an odd starting position i=2j−1, the ordered free triple consists of the ENTIRE coordinate pair (p_(2j−1),p_(2j)) and the first coordinate p_(2j+1) of the next pair. Both coordinates encoding b_j are free, so changing b_j does not alter any fixed exterior bit of this physical three-face. Every other b_k can be recovered from at least one fixed exterior bit: the second coordinate p_(2j+2) in pair j+1 recovers b_(j+1), and in any other pair an exterior coordinate remains. Consequently the exterior-face address map b↦F_i(b) is exactly two-to-one, identifying precisely b and b+e_j.

For an even starting position i=2j, the three free coordinates are p_(2j) and the ENTIRE next pair (p_(2j+1),p_(2j+2)), so the same argument gives fibers exactly {b,b+e_(j+1)}. Prefix flips of directions already traversed merely complement the relevant fixed exterior bits, preserving their recoverability. Thus W_i cannot depend on the omitted parameter b_(psi(i)).

**Proof (sufficiency).** For each i prescribe on the 2^(m−1) distinct physical faces F_i(b) with the ordered free triple t_i=(p_i,p_(i+1),p_(i+2)) the required values w_i(b). These assignments are consistent because w_i is constant on the fibers just identified. The forward ordered triples t_i are pairwise distinct, and no t_i is the reverse of another t_j: the entries of p are all distinct and appear only once. Therefore the prescribed face colors are mutually independent across i and do not meet any reversal-orbit conflict. Extend the assignment to their antipodal-reversed ordered faces by c(bar F,rev t)=1−c(F,t), and assign one arbitrary representative value on every still-unassigned reversal orbit. This defines a legal global NORI coloring with the desired chart. Each w_i has exactly 2^(m−1) free truth-table bits, proving the exact count. QED.

**Corollary (sharp boundary of the central two-layer path-square DP).** All these paired-root window faces lie on the two central exterior Hamming layers, yet each W_i may depend NONLINEARLY on ALL m−1 observable paired bits. For example, setting w_i(b)=product_(k≠psi(i)) b_k realizes genuine degree-(m−1) interactions on the central layers. Accordingly the path-square four-state dynamic program for central two-layer triple-ORDER tables (Item nori_general_central_two_layer_arbitrary_triple_table_signed_path_square_dp_20261009) relies essentially on the hypothesis that face color within a layer depends only on the ordered triple, rather than the exterior face's identity.

**Exact fixed-order obstruction.** Taking w_i(b)=i mod 2 yields a legal NORI coloring under which EVERY paired root in this fixed direction order has 2m−3 switches. The stronger same-order all-root obstruction is equally realizable by assigning those constants to all physical faces with ordered free triples t_i. Thus any dimension-independent universal extraction proof must couple genuinely different direction orders or exploit additional structure of the coloring. This local universality is compatible with full NORI closure after changing orders.

**Positive frontier.** Study the transition maps between neighboring paired direction orders. Their face-orbit overlaps are the only constraints coupling these otherwise free Boolean window maps; a global consistency or exchange theorem, rather than fixed-order low-width dynamic programming, is needed for unrestricted exterior dependence.
