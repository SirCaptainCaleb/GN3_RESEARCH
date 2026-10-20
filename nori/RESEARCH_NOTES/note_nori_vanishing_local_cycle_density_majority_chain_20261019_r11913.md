# Vanishing local feedback density in strongly connected nonlinear paired-flat cubes

- Stable ID: note_nori_vanishing_local_cycle_density_majority_chain_20261019_r11913
- Author: unspecified; session provenance retained
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, paired-flat, dimension-uniform, Boolean-derivatives, local-cycles, method-obstruction, nonlinear, majority
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11913_2
- Updated session: session_nori_r11913_2
- Disposition: none
- Successor: none

## Related references

- note:note_nori_rank_four_pointwise_sensitivity_cycle_r11510

## Research note

# Vanishing local-cycle density with no reciprocal sensitivities

For m>=5 let k be the largest odd integer <=m-2 and t=(k+1)/2. Label the 2m cube dimensions in pairs (a_i,b_i), put q_i=x_(a_i), and color the a_i-edge by f_i(q), the b_i-edge by 1+f_i(q), where

f_0(q)=Maj_k(q_1,...,q_k), f_i(q)=q_(i+1) for 1<=i<=m-2, and f_(m-1)(q)=q_0.

**Theorem.** The coloring is legal, antipodally odd, perfectly vertex-balanced, and has a strongly connected global dependency digraph without reciprocal dependencies. No two-pair four-face admits a monochromatic full geodesic. Nevertheless, in each pair-parity fiber the fraction of vertices with a directed cycle in the local Boolean-derivative digraph equals 2*C(k,(k-1)/2)/2^k ~ sqrt(8/(pi*k)) = O(m^(-1/2)). The coloring has a red full antipodal geodesic in every dimension 2m.

**Proof.** Each f_i ignores both bits of its own pair and reverses under q->q+1^m; the two incident colors within a pair are complementary. Using arrows j->i when D_j f_i(q)=1, all unary gates supply the chain 0->m-1->m-2->...->1. The majority gate contributes only arrows j->0 for 1<=j<=k<=m-2. Thus no reciprocal pair occurs; the union of these arrows contains the additional arc 1->0 and is strongly connected. A monochromatic full four-step path using only two paired groups must interleave their group labels, requiring mutual gate dependence, which is absent.

The local graph has a directed cycle iff some majority derivative is active. If w is the weight of (q_1,...,q_k), this occurs iff w=(k-1)/2 or w=(k+1)/2. Counting both weight layers yields the stated fraction and asymptotic.

For a red full geodesic, start with x_(a_0)=1 and all other starting vertex bits zero. Use the direction order

b_(m-1), a_0, a_1,...,a_t, b_0,b_1,...,b_(t-1),
(a_(t+1),b_t),...,(a_(m-2),b_(m-3)), a_(m-1),b_(m-2).

The initially red b_(m-1) leaves q_(m-1)=0; red a_0 sets q_0=0. Each a_j for 1<=j<=t is red and raises q_j to one, taking the majority to one, so b_0 is red. Every subsequent a_j is red before q_(j+1) changes, and every b_j is red after a_(j+1) changes q_(j+1) to one. Finally a_(m-1) is red since q_0=0, followed by red b_(m-2). Thus all 2m distinct directions are used once and all edges are red.

**Scope.** The pointwise active-cycle result for four self-dual gates cannot extend to arbitrary m from self-duality, balance, strong global connectivity, and absence of reciprocal derivatives. Even the fraction of cycle-active states may tend to zero. A dimension-uniform cycle-based closure argument therefore needs additional path-witness transport or hypotheses deduced from a hypothetical bad coloring. No NORI1 counterexample is asserted.

**Independent computational checks.** Full derivative enumeration gives 24 of 32 cyclic states for m=5, 80 of 128 for m=7, and 280 of 512 for m=9, with no reciprocal derivatives. The displayed red full direction order was verified for m=5,6,7,8,9,10,15,25,55,105.
