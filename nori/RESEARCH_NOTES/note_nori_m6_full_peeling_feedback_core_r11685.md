# Complete six-pair parity peeling and unbounded feedback-core forcing

- Stable ID: note_nori_m6_full_peeling_feedback_core_r11685
- Author: unspecified; session provenance retained
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, Q12, affine-holonomy, parity-peeling, complete-enumeration, nonlinear-phases, directed-cycle, feedback-core, odd-principal-minors, constructive-forcing
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11510_3
- Updated session: session_nori_r11510_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_nested_core_phase_peeling_r11660
- note:note_nori_phase_interlacement_corank_r11640

## Research note

# Six-pair complete parity-peeling certificate and cycle-feedback forcing

**Finite theorem (computer-assisted).** Every zero-diagonal 6x6 binary matrix A satisfying A1=1 has an ordered deletion i_1,...,i_k (0<=k<=4) with sum_(s<t) a_(i_t,i_s)=0 at each step and nonsingular remaining principal matrix A[R,R]. A portable C++17 verifier explicitly enumerates all 16^6=16,777,216 such matrices and performs subset-reachability plus binary Gaussian elimination. There are no failures.

**MINIMUM DELETION COUNTS.** k=0:5,000,192; k=1:7,958,848; k=2:2,933,900; k=3:658,510; k=4:225,766. Total 16,777,216. This table counts the smallest feasible k for each matrix, not merely the first successful subset in numerical order. An independently written Python audit verified positive results on 15,000 sampled six-pair matrices, and a separate red-path simulator validated predicted 2^k roots for 2,000 random six-pair nonlinear-phase instances.

**NORI1 CONSEQUENCE.** By the established nested-core forcing theorem, every legal paired-flat Q12 coloring with fixed odd affine q-slope matrix A and arbitrary nonlinear parity-phase gates has a red full antipodal geodesic rooted in EVERY prescribed pair-parity fiber. There are 2^24 eligible coefficient matrices and 2^192 possible phase tables, covering 2^216 such colorings. The pair order is selected from A alone and guarantees 2^k starting q-states in each fiber.

**ALL-DIMENSIONAL FEEDBACK-CORE THEOREM.** Put a directed influence arc j->i when a_ij=1. Suppose some label set R satisfies det A[R,R]=1 and the induced subgraph on D=[m]\R is acyclic. Deleting D in reverse topological order is a valid parity peel, because no newly deleted vertex receives an arc from a previously deleted vertex. The nested-core word produces 2^|D| full red geodesic roots in each prescribed parity fiber for arbitrary nonlinear phase assignments. This gives a simple constructive graph certificate for any dimension.

**SCC CYCLE-INTERSECTION COROLLARY.** In particular, suppose NO strongly connected component contains two vertex-disjoint directed cycles. For each cyclic SCC H choose a shortest directed cycle C_H. It is an induced cycle (a chord would create a shorter directed cycle), so the corresponding adjacency submatrix is a cyclic permutation matrix with determinant one. Their union R has block-triangular principal adjacency, hence det A[R,R]=1. Every cycle lies within an SCC and meets C_H by hypothesis; thus the complement D is acyclic. The feedback-core theorem applies. This is an unbounded-dimensional forcing theorem for potentially singular influence matrices and arbitrary nonlinear phase gates. A separate full graph enumeration verified the criterion for 8/8 matrices on three labels, 231/256 on four labels, and 17,664/32,768 on five labels.

**PRINCIPAL-MINOR PARITY LEMMA.** Every zero-diagonal A with A1=1 has an odd number of nonsingular principal minors of order at least two. Over F2, det(I+A)=sum_(R subset [m]) det A[R,R], with det(empty)=1. But (I+A)1=0 so det(I+A)=0, and singleton principal minors vanish. Therefore sum_(|R|>=2) det A[R,R]=1. This proves that an invertible principal core ALWAYS EXISTS; the general conjecture asks additionally for one accessible through legal parity peeling.

**STATUS AND LIMITS.** The six-pair conclusion is a complete finite computation with reproducible source, not a dimension-uniform proof of the odd-matrix peeling conjecture. The SCC-feedback criterion is proved in all dimensions, but does not cover every odd matrix (on five labels it covers 17,664 of 32,768). Full NORI1 allows parity-varying affine slopes or non-affine dependence on q; neither is resolved by the finite static-slope result.

**AUDIT FILES.** /mnt/data/nori_six_pair_peeling_feedback_report.md, /mnt/data/nori_matrix_m6_minpeel.cpp, /mnt/data/nori_matrix_m6_exhaust.cpp, /mnt/data/nori_m6_independent_audit.py, /mnt/data/nori_feedback_cycle_test.py, /mnt/data/nori_nested_direct_paths.py. Research archive /mnt/data/nori_six_pair_peeling_feedback_bundle.zip.
