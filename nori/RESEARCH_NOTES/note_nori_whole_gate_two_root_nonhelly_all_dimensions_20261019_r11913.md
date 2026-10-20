# Whole-gate two-root forcing fails in every even dimension

- Stable ID: note_nori_whole_gate_two_root_nonhelly_all_dimensions_20261019_r11913
- Author: NORI1 independent researcher session_nori_r11913_3
- Primary home: subsection:creative_routes_to_unrestricted_forcing_and_a_carry_forward_map
- Labels: nori1, paired-flat, whole-gate, 2-cnf, two-root, dimension-uniform, method-obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11913_3
- Updated session: session_nori_r11913_3
- Disposition: none
- Successor: none

## Related references

- subsection:obstruction_compatibility_and_a_programme_for_nori1_closure

## Research note

## Dimension-uniform two-root obstruction for whole-pair-gate clauses

**Theorem.** For each m≥3, some legal fixed paired-flat gates f_1,...,f_(m−1) on Q_(2m) satisfy: for every two starting vertices r,s, there is a legal choice of f_0 for which neither vertex starts a red full antipodal geodesic. In particular the root-r and root-s clauses of the geometric whole-gate 2-CNF are jointly satisfiable for every r,s. This is the whole-*pair*-gate formula, rather than the distinct two-free-direction formula.

**Q6 base, including a finite exhaustive certificate.** Number directions 0,...,5, pair i=(2i,2i+1). At a pair-i edge compress the four outside bits in ascending dimension order into y∈{0,...,15}. Define k(y)=y when y<8, and k(y)=15−y otherwise; e(y)=[y≥8]. For table M_i∈{0,...,255}, set f_i(x)=((M_i >> k(y)) & 1) xor e(y). Direction 2i+d is red iff f_i(x)=d. All tables are antipodally odd and independent of their own pair. Fix M_1=0x4E and M_2=0xAA; M_0 remains arbitrary.

For a root r let A_r be the subset of the 256 possible M_0 tables that admit no full red path starting at r. Two independent implementations (C++ and Python) enumerate every r∈Q6 and π∈S_6, inspect the four fixed-gate edges, and impose the two remaining requirements on M_0. They verify min_r |A_r|=16, max_r |A_r|=48, and min_(r≠s) |A_r∩A_s|=1 over all 2016 distinct root pairs. Thus all one-root and two-root geometric clause systems have a satisfying gate0 table.

**Three-root failure and five witnessed clauses.** A_0∩A_1∩A_2=∅. Write X_j for free gate0 orbit bit j. Each row below provides a rooted full direction order, whose four fixed-gate edges are red, and the two gate0 values needed to make its complete path red:
- r=1, π=(1,5,0,3,4,2): (X_0,X_7)=(1,1).
- r=0, π=(2,1,3,4,0,5): (X_1,X_7)=(1,0).
- r=1, π=(5,0,3,4,2,1): (X_0,X_7)=(0,1).
- r=2, π=(3,4,1,2,0,5): (X_6,X_7)=(1,0).
- r=2, π=(3,4,0,5,1,2): (X_1,X_6)=(0,0).
Avoiding the first and third paths forces X_7=0; avoiding the fourth forces X_6=0; avoiding the fifth forces X_1=1; avoiding the second forces X_7=1. Therefore at least one of these five direction-simple full geodesics is red, independently of M_0. The five clauses form an inclusion-minimal unsatisfiable subfamily.

**Uniform lift.** For m>3, let the first three gates depend only on the first six vertex bits, with M_1,M_2 fixed as above. Put f_j(x)=x_0 for every j≥3. Every gate remains independent of its own pair and changes value under antipodality. For arbitrary r,s in Q_(2m), project them to r',s'∈Q6. Choose M_0∈A_(r')∩A_(s') and extend f_0 independently of the new dimensions. If there were a red full geodesic upstairs from r or s, deleting its steps in directions ≥6 leaves a red full geodesic in Q6 from r' or s': all six remaining directions occur once and their colors depend only on the first six vertex bits. Contradiction. This proves the quantified theorem for every m≥3. The lift was separately verified using a red-path subset recursion for sample root pairs in Q8, Q10, Q12 and by testing gate legality at every vertex of those instances.

**Reproduction of the Q6 finite base.** For each of 64 roots r and each of 720 direction permutations, trace the vertex before every step. Discard a word if any edge from pair1 or pair2 is blue under the two fixed tables. For each surviving word, record the gate0 orbit indices and required values at its two pair0 edges. Delete M_0 from A_r iff its two bits equal those requirements. The 64 resulting 256-bit masks have nonzero intersection for every pair; the smallest pairwise intersection has size one. This computation uses neither a theorem prover nor a NORI1 assumption.

**Research consequence and limitation.** No proof can force unrestricted NORI1 by claiming that, for arbitrary other fixed gates, some pair of starting roots already gives an unsatisfiable whole-gate clause collection. The obstruction holds in arbitrarily high even dimension and permits implications between different free-gate sites. Three-root forcing in the Q6 base does not imply three-root forcing after lifting when the complete free gate may depend on the added dimensions. Growing root networks, mixed-site implication transport, and the unrestricted strict critical-square problem remain open. This is a method obstruction, not a counterexample to NORI1.
