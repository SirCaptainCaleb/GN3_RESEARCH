# Three-side endpoint six-sets have no prescribed-pair matching residue

## Statement

Assume the setting and notation of threeside_consecutive_fivewindows01, with persistent pair Z={z,zprime}. For each of the positioned six-sets U_L=Z union {q_0,q_1,q_2,q_3} and U_R=Z union {q_{s-3},q_{s-2},q_{s-1},q_s}, the prescribed-pair menu sixset_prescribed_pair_menu01 reduces to only three possibilities: (1) U is Hamiltonian; (2) U-z or U-zprime is Hamiltonian; or (3) U is non-Hamiltonian and contains two Hamiltonian four-sets sharing three vertices and each containing Z. The perfect-matching/no-overlap alternative of sixset_prescribed_pair_menu01 is impossible at either end. In a minimum counterexample, every Hamiltonian support so produced has non-Hamiltonian path-cover-two complement.

## Body

Apply sixset_prescribed_pair_menu01 to U_L with prescribed pair p=z,q=zprime and A={q_0,q_1,q_2,q_3}. The set A is Hamiltonian because it is four consecutive vertices of the displayed tight path Q. Alternative (4) of sixset_prescribed_pair_menu01 requires A to be a non-Hamiltonian matching-block four-set, so that alternative is impossible. Hence one of alternatives (1),(2),(3) holds. In alternative (3), the deleted labels d,e,f all lie in A, so each Hamiltonian four-set U_L-{d,e} and U_L-{d,f} retains the entire prescribed pair Z. The complement assertion follows from minimum-counterexample calculus exactly as in sixset_prescribed_pair_menu01. The argument for U_R is identical because its four vertices outside Z are the consecutive Q-segment {q_{s-3},q_{s-2},q_{s-1},q_s}.
