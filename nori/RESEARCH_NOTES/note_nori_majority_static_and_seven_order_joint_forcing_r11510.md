# Four-majority fixed-word root theorem and seven-order joint forcing certificate

- Stable ID: note_nori_majority_static_and_seven_order_joint_forcing_r11510
- Author: unspecified; session provenance retained
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, Q8, paired-flat, majority-network, fixed-word, root-uniqueness, seven-orders, shared-assignment, joint-obstruction, finite-SAT, analytic-static
- Lifecycle: active
- Epistemic status: tested
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11510_3
- Updated session: session_nori_r11510_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_rank_four_pointwise_sensitivity_cycle_r11510
- note:note_nori_cyclic_pair_gate_sensitivity_product_r11510

## Research note

# Four-majority transport: common fixed word and seven-word simultaneous forcing

**SCOPE.** Work continuing Article XVI's unrestricted compatibility programme. One proved constructive theorem concerns static four-majority gates, while the general parity-dependent seven-word forcing assertion is a finite UNSAT finding awaiting a hand derivation or independently checked UNSAT proof log. NORI1 remains open.

**THEOREM A: a common static majority word.** Let h_i:F2^4->F2 ignore q_i and obey h_i(q+1111)=1+h_i(q). Suppose all h_i have three essential inputs, and no state has reciprocal nonzero derivatives D_jh_i D_ih_j. For the red paired-matching system with gates h_i independent of paired parity bits, the fixed pair-label word W=(3,2,1,2,0,3,0,1) is a red full antipodal geodesic from ONE and only one starting q in F2^4. Consequently it succeeds from sixteen full Q8 roots, one per initial pair-parity vector.

**Proof.** Each h_i is a signed majority, h_i(q)=Maj(q_j+a_ij:j!=i). For unordered i,j and complementary k,l the absence of reciprocal derivatives is equivalent to a_ik+a_il+a_jk+a_jl=1. These six F2-linear equations on twelve signs have rank five. Fix a reference solution h*_0=Maj(q1,q2,q3), h*_1=Maj(q0,1+q2,q3), h*_2=Maj(1+q0,1+q1,q3), h*_3=Maj(q0,1+q1,q2). All solutions are h_i(q)=h*_i(q+t)+s_i for some t,s in F2^4, with only the common global redundancy (t,s)~(t+1111,s+1111). For each of sixteen s, direct substitution in W gives the sole successful q=(s1,s3,1+s3,s1)+t. An independent 128-network by 16-root exhaustive checker verifies this short substitution and uniqueness. QED. A general paired-flat coloring depends on pair parity, so the static theorem does not apply without a transport argument.

**GENERAL Q8 SAT PORTFOLIO.** Let c be an arbitrary legal paired-flat Q8 coloring. Suppose that at one parity fiber, after translation and pair-member relabeling, f_0 restricted to diagonal pair inputs is Maj(q1,q2,q3), and that no four-face retaining P0 and one other complete pair contains a red full geodesic. Then at least one of the opposite six-faces P0=00 and P0=11 contains a red full three-pair geodesic with pair-label word among
  121323, 213123, 213132, 213231, 231231, 312123, 312321.
Such a red face geodesic extends to a red full Q8 antipodal geodesic by the established paired-endpoint insertion theorem.

**Computational verification of portfolio.** Use 256 Boolean gate variables v_(i,s) (64 per pair), 128 antipodal-oddness equations, and eight fixed f0 majority values. For every P0,Pj four-face, forbid a red full face geodesic by demanding that at least one of its two gates is constant on that face (rank-two identity R=2E(a)E(b)). For each chosen pair word, each rooted geodesic on faces P0=00 and11 and each first-member choice in the three retained pairs, forbid the all-red path by a six-edge Boolean blocking clause. After removing repeated clauses there are 7168 path constraints. Z3 returns UNSAT. Removing any one of the seven entire pair-word families yields SAT; this was separately checked seven times. This is a finite reproducible SAT implication, with a much smaller order family than all possible three-pair words. No proof-log checker or short paper proof has yet been obtained, and minimality among all possible portfolios is not claimed.

**LESSON FOR UNRESTRICTED NORI1.** The static majority theorem has a one-word constructive witness. Pair-parity dependence invalidates the single-word guarantee; a direct SAT attempt with the one static word is satisfiable. Restoring the simultaneous no-two-pair-face compatibility restrictions makes seven words sufficient in the full parity-dependent system. Pairwise cross-face equalities alone, even combined with oddness, are insufficient; a separate SAT model satisfies those weaker constraints while avoiding red full paths on both candidate six-faces. These results localize the required transport to specific joint cross-parity constraints rather than separate scalar influence counts.

**FILES.** Full mathematical and computational audit: /mnt/data/nori_majority_joint_transport.md. Reproducer: /mnt/data/nori_majority_transport_certificate.py. Generated standalone SMT-LIB2 instance: /mnt/data/nori_majority_seven_word.smt2. The checker verifies the 128-network theorem without external packages and obtains the seven-word UNSAT result with installed libz3.so.4.
