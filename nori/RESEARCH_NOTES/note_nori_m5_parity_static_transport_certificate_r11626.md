# Ten-cube nonlinear-phase fiberwise forcing and transported-incidence cancellation

- Stable ID: note_nori_m5_parity_static_transport_certificate_r11626
- Author: unspecified; session provenance retained
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, Q10, paired-flat, affine-holonomy, parity-static-slope, nonlinear-phases, fiberwise-forcing, computational-certificate, transported-incidence, dimension-uniform-criterion
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11510_3
- Updated session: session_nori_r11510_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_affine_holonomy_joint_phase_forcing_r11510

## Research note

# Five-pair parity-static affine phase forcing and transported-incidence criterion

Let N=2m and let a legal paired-flat coloring have pair-parity bits p_i=x_(a_i)+x_(b_i) and first-member bits q_i=x_(a_i). Suppose its gate has form f_i(p,q)=a_i dot q + theta_i(p_except_i), with odd off-diagonal slope row a_i fixed independently of p, and arbitrary Boolean phase function theta_i. This permits nonlinear dependence on pair-parity bits.

**DIMENSION-UNIFORM TRANSPORTED-INCIDENCE LEMMA.** Let S_i=I+e_i a_i^T. For any double-occurrence pair-label word w=(i_1,...,i_(2m)) and starting parity p, set p_t=p+sum_(s<t)e_(i_s), L=S_(i_(2m))...S_(i_1), and v_t=S_(i_(2m))...S_(i_(t+1)) e_(i_t). The red return equation is
  (L+I)q=1+sum_t v_t+sum_t theta_(i_t)((p_t)_except_i_t) v_t.
The word admits a full red antipodal path from some q for EVERY assignment of the independent phase truth values iff, for all z in ker((L+I)^T), (1) z dot (1+sum_t v_t)=0 and (2) for each phase key (i,u), sum_(t: i_t=i and (p_t)_except_i=u) z dot v_t=0. Proof: the right side must be orthogonal to every left-null vector for all independent phase variables, forcing each affine coefficient to vanish. When these conditions hold and k=corank(L+I), every phase assignment has 2^k red starting q-roots in the prescribed parity fiber. This is a shared-coloring compatibility condition expressed through transported occurrence vectors.

**COMPUTER-ASSISTED FINITE THEOREM IN Q10.** For m=5, every one of the 32768=8^5 odd off-diagonal slope matrices admits a double-occurrence word whose transported-incidence conditions hold; hence EVERY one of the 2^95 corresponding legal paired-flat Q10 colorings has a red full antipodal geodesic starting in EVERY prescribed pair-parity fiber. The witness word depends only on the slope matrix, not on the 80 arbitrary nonlinear phase bits. The 32768 matrices form 324 relabeling classes under S5. Independent Python and C++ implementations test all 39480 admissible double-occurrence pair words, checking all 324 class representatives. Every class succeeds. With the first word chosen by the deterministic search, the corank distributions are: k=0: 83 classes/8848 labeled matrices; k=1:129/12800; k=2:43/4760; k=3:69/6360. Thus the selected order guarantees respectively 1,2,4,8 red starting roots q for every phase assignment. Direct red-step trajectory checks in 1296 independently sampled class/phase instances reproduced those root counts.

**FILES.** Full proof nori_affine_m5_static_transport.md; standard-library independent verifier nori_affine_m5_static_cover.py; C++ verifier nori_m5_phase_exhaust.cpp. The parent prior note note_nori_affine_holonomy_joint_phase_forcing_r11510 already proves the general affine return mechanism and the m=3,4 cases. This is a dimension-ten extension and a more geometric phase-cancellation criterion, not a complete proof of NORI1.

**RESEARCH BOUNDARY.** The existence of such a phase-immune word for every static odd slope matrix in arbitrary dimension remains unproved. For general legal colorings the slope rows may themselves depend on p and may be nonlinear in q, so the present sufficient criterion does not apply.

**GENERALIZED TRANSPORT LEMMA.** The preceding transported-incidence lemma remains valid when the affine slope vectors a_i(p) vary with pair parity p, as long as the gate is affine in q on each parity fiber. For a chosen pair-label word let S_t=I+e_(i_t) a_(i_t)(p_t)^T and replace every suffix product defining v_t by the corresponding time-dependent product S_(2m)...S_(t+1). The parity trajectory is determined by the word, hence all matrices S_t are fixed before choosing the starting q or any phase values. The return remains affine in q and the independent phase entries, and precisely the same left-kernel coefficient-cancellation argument proves the criterion. The positive five-pair classification still requires the slopes to be parity-independent; the criterion itself does not.
