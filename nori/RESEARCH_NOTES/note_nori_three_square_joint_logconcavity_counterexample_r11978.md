# Three switches in Q6 refute joint log-concavity of red antipodal geodesic counts

- Stable ID: note_nori_three_square_joint_logconcavity_counterexample_r11978
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, paired-flat, nonlinear, square-switch, method-obstruction, log-concavity
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11978_1
- Updated session: session_nori_r11978_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Let Q6 have direction pairs (0,1),(2,3),(4,5). For i=0,1,2 pack the four outside-pair vertex bits in increasing direction order into z in {0,...,15}. Let f_i(z)=bit_(min(z,15-z))(M_i)+[z>=8] modulo 2, with eight-bit masks (M0,M1,M2)=(0x20,0xE6,0x6F). The red direction in pair i is 2i+f_i(z). These gates ignore their own pairs and satisfy f_i(15-z)=1+f_i(z), hence give a legal paired-flat antipodally odd coloring.

Interpolate three antipodally paired alternating-square switches in pair 0 with canonical outside assignments z=0,1,2, using weights t0,t1,t2 between 0 and 1. On a switched edge, weight 1-tj when originally red and tj when originally blue. Unchanged red edges have weight one, unchanged blue edges zero. Define Z(t) as the total weight of rooted full antipodal geodesics, summed over all 64 roots and all 720 permutations of the original six directions.

THEOREM (multiswitch log-concavity counterexample). Full-path enumeration gives the integer polynomial
Z(t0,t1,t2)=276+56t0+28t1+124t2-24t0^2-24t1^2-40t2^2-40t0t1-40t0t2.
The polynomial has degree at most two because all switches lie in pair 0, whose two original directions each occur once in a full geodesic. On the interior line (t0,t1,t2)=(1/2+2s,1/2-2s,1/2-s), one obtains Z(s)=338-48s+8s^2. Hence (log Z)''(0)=(338*16-48^2)/(338^2)=776/28561>0. Thus log Z is NOT jointly concave on the three-parameter cube, despite the single-switch concavity theorem and earlier successful pairwise numerical probes.

VERIFICATION. The dependency-free nori_logconcavity_polynomial_certificate.py enumerates all rooted original-direction permutations, constructing and summing each path's multivariate polynomial with integer coefficients. An independent nori_logconcavity_counterexample_exact.py uses rational arithmetic on the one-parameter line and reproduces Z(s)=338-48s+8s^2. A separate C++ dual-number switch DP independently finds a positive log-Hessian eigenvalue at the same coloring. All eight Boolean endpoint choices t in {0,1}^3 have strictly positive Z, so this result refutes a proposed inequality, not NORI1 or one-switch preservation.

IMPLICATION. The attempt to infer unrestricted NORI1 from universal multivariate log-concavity across legal square switches is closed: its mathematical premise is false. Even a valid log-concavity statement would not by itself prohibit an endpoint with zero witnesses. Return to collective red-path/repair-path compatibility under one hypothetical critical switch.
