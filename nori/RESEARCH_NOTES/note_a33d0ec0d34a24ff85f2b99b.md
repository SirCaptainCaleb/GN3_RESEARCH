# Universal cross-profile gate influence and critical-square curvature

- Stable ID: note_a33d0ec0d34a24ff85f2b99b
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: 
- Lifecycle: active
- Epistemic status: proved
- Current version: 6
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11887_1
- Updated session: session_nori_r11887_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Complete-halfword midpoint collisions require odd finite differences of the shared pair gates. A midpoint profile without singly used pairs requires two vertex-disjoint directed dependency cycles.

THEOREM A. Let w contain each pair label twice and v_k be its red matching trajectory. With visits r_i<s_i, reaching the antipode is equivalent to f_i(v_(r_i-1))+f_i(v_(s_i-1))=1 for all i. This equals the sum of finite differences f_i(v_(k-1))+f_i(v_k) over r_i<k<s_i. Every nonzero term involving a step in pair j supplies a dependency arc i->j. Proof: each pair parity returns to its start; its first-member fiber bit must flip once, meaning the two selected red directions in the pair differ. Gate i ignores its own pair, and its values telescope between the visits.

THEOREM B. Split the word after m steps. Define D as pairs occurring twice in first half, Z as pairs occurring zero times, and S as pairs occurring once. Then |D|=|Z|. Any successful full geodesic forces an outgoing dependency arc from every i in D into D union S, and from every i in Z into Z union S. If G[D] is acyclic, every vertex of D has a directed path to S; likewise for Z. Proof: the odd temporal derivative for each repeated pair contains a nonzero increment caused by a pair in its own half. A finite walk following these arcs either enters S or creates a directed cycle.

COROLLARY C. When S is empty and D is nonempty, the directed dependency graph contains a cycle inside D and another inside Z. These cycles are vertex disjoint. Thus if the graph has no pair of vertex-disjoint directed cycles, every complementary-halfword midpoint incidence with multiplicities only 0 or 2 vanishes: tr(P_alpha^T P_beta J)=0 for every alpha,beta with complementary all-even pair counts and every starting parity fiber. This is a shared-gate zero-incidence theorem, not a proof of unrestricted NORI1.
CRITICAL-SQUARE CURVATURE: If a legal paired-square switch turns a successful coloring into a bad one, every red full geodesic on the good side hits the switch once internally. The switched pair step cannot commute with either neighboring red step from another pair. Otherwise swapping that adjacent pair of red moves keeps the two-step endpoint and all original directions, but moves the unique switched edge outside the switched square orbit, producing a red full geodesic surviving the switch. For adjacent pair labels i,j, local red commutation holds precisely when both finite derivatives f_i(v)+f_i(T_j v) and f_j(v)+f_j(T_i v) vanish. This adds two necessary nonzero-curvature conditions to every strict one-hit witness, but does not force such a witness to be repairable.
INDEPENDENT AUDIT. Exhaustive Q8 checker nori_crossprofile_derivative_verifier.py tested all 2520 pair words from all 256 starting vertices in three legal gate systems. Directed four-cycle gates: 4736 red full geodesics, zero with all-even midpoint profile. Two disjoint two-pair directed cycles: 4480 red full geodesics, 128 with all-even midpoint profile. Arbitrary nonlinear parity-dependent self-dual gates: 15794 red full geodesics, 384 with all-even midpoint profile. Each test verifies endpoint antipodality equivalent to the pairwise gate-derivative conditions and the temporal-dependency witness statement. Full self-contained report nori_unrestricted_crossprofile_influence.md. These are unrestricted structural identities, not NORI1 closure.
