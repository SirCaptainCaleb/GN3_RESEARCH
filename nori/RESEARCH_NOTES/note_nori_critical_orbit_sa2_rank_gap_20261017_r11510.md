# Critical-orbit second-moment relaxation: Q4 infeasible, Q5 feasible

- Stable ID: note_nori_critical_orbit_sa2_rank_gap_20261017_r11510
- Author: Independent NORI1 mathematician
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, critical-orbit, Sherali-Adams, quadratic-moments, Q4, Q5, computational-method-boundary
- Lifecycle: active
- Epistemic status: tested
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11510_1
- Updated session: session_nori_r11510_1
- Disposition: none
- Successor: none

## Related references

- note:note_nori_q4_ten_path_critical_surgery_r11435
- note:note_nori_q6_profile_critical_sat_extension_r11435

## Research note

# Level-two moment relaxation of a critical antipodal-orbit recoloring

Fix a rooted full geodesic P and an internal edge orbit O. Write one Boolean variable y_J for every antipodal edge orbit J, fixing the n variables met by P so that P is red. After flipping O, a successful recoloring would have a red full geodesic. For each rooted full geodesic Q, encode its edge-blue indicators after the flip as affine literals b_e(y)=y_J or 1-y_J and impose the blocker inequality sum_(e in Q)b_e(y)>=1. The conjunction of these inequalities over all Q is unsatisfiable if orbit-flip preservation holds.

The level-two Sherali-Adams relaxation uses u_i=E[y_i], u_ij=E[y_i y_j] for each remaining orbit bit and pair. It imposes 0<=u_i<=1 and max(0,u_i+u_j-1)<=u_ij<=min(u_i,u_j). For every blocker inequality H_Q(y)=sum_e b_e(y)-1>=0, it also imposes E[H_Q]>=0, E[y_i H_Q]>=0 and E[(1-y_i)H_Q]>=0 for every free orbit variable i. These form a linear program.

COMPUTATIONAL FINDING. On Q4 normalize P to root 2 and order (1,0,2,3), with the pivot in position 2. After deduplication there are 110 blocker inequalities on 12 free variables, with widths 2,3,4 occurring 6,48,56 times. The resulting relaxation has 78 variables and 2948 inequalities. SciPy HiGHS reports infeasibility.

On Q5 normalize P to root 0 and order (0,1,2,3,4), with the pivot in position 3. There are 1397 blockers on 35 free variables, with widths 2,3,4,5 occurring 4,33,350,1010 times. The level-two system has 630 variables and 100972 inequalities. SciPy HiGHS finds a feasible point EVEN WITH all 35 first marginals fixed at 1/2. An independent evaluator recomputed the original and conditional blocker inequalities from the solver's moments; the smallest conditional slack was -3.06e-13 and no bound was violated beyond solver tolerance. Thus quadratic moment constraints from these pathwise first-order blockers do not yet detect the Q5 critical-orbit impossibility.

SCOPE. The Q4 and Q5 calculations are numerical linear-programming findings, not independently certified rational primal or dual proofs. The underlying Boolean Q5 critical-orbit exclusion is separately established in the archive by finite SAT computations. Feasibility of this level-two relaxation on Q5 blocks a dimension-uniform proof based solely on these particular rank-two Sherali-Adams constraints; it does not rule out higher-degree algebraic relations or a distinct constructive repair argument. Source code: /mnt/data/nori_critical_flip_sa2_probe.py. Related archive: note_nori_q4_ten_path_critical_surgery_r11435 and note_nori_q6_profile_critical_sat_extension_r11435.
