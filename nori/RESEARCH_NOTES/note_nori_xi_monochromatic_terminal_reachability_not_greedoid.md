# Monochromatic terminal reachability is accessible but not a greedoid

- Stable ID: note_nori_xi_monochromatic_terminal_reachability_not_greedoid
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: boundary-tournaments, greedoid-obstruction, endpoint-reachability, spanning-one-turn, matroid-exchange, density-obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6430_2
- Updated session: session_nori_r6430_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

For a reversal-odd ordinary boundary 3-tournament b on V, fixed ordered pair (u,v) and color epsilon, let F_uv^epsilon be the family of subsets S ⊂ V\{u,v} admitting an epsilon-monochromatic vertex-simple tight path on S∪{u,v} ending in (u,v); include S=∅ as the vacuous two-vertex path.

Each family is accessible: if S is nonempty and a witness is a word (x_1,...,x_k,u,v), delete its first vertex x_1; the remaining path ends in (u,v) and stays epsilon-monochromatic, so S\{x_1} remains feasible.

However these families are not in general greedoids. On V={0,1,2,3,4}, encode the 30 reversal-pairs of triples by increasing middle vertex followed by lexicographically increasing outer pair a<c. Let the representative bit mask be M=0x345cb98d and complement on reversing triples. Take epsilon=1, (u,v)=(1,2). The complete feasible family of subsets S⊂{0,3,4} is
  F_12^1={∅,{3},{0,3},{4},{0,3,4}}.
Witnesses: (0,3,1,2) is all color 1 and gives A={0,3}; (4,1,2) is color 1 and gives B={4}. The two candidate augmentations B∪{0}={0,4}, B∪{3}={3,4} are both infeasible, as the only possible paths ending (1,2) on {0,1,2,4} or {1,2,3,4} fail. Thus |A|>|B| but no element of A\B augments B, violating the greedoid exchange axiom.

Verification: enumerate all permutations of S∪{1,2} ending (1,2), check all ordered triple colors equal one using the mask convention. This gives the displayed complete feasible family.

The unification problem has a direct Boolean-lattice complement formulation: a spanning at-most-one-turn tight path exists iff for some pair u≠v and some epsilon there is S∈F_uv^epsilon with (V\{u,v})\S∈F_vu^epsilon. The recurrence for nonempty S is
 F_uv^epsilon(S) ↔ ∃x∈S: [b(x,u,v)=epsilon] ∧ F_xu^epsilon(S\{x}).
This gives a uniform subset-DP of size O(n^3 2^n) and a complementary reachability target parallel to the cube's antipodal endpoint problem.

Research consequence: one cannot invoke generic greedoid augmentation for monochromatic terminal reachability. An additional cross-terminal exchange or complementary-density theorem is required. Preserve as an obstruction note, not a publication Subsection.

An additional counting obstruction: for n=8, the reversal-odd representative-bit mask
M=0xd63f56b74021379c67fbd03d46effde5a4780fa7d0
(using increasing middle vertex, then increasing outer pair a<c) has only 768 color-0 reachable terminal states and 769 color-1 reachable terminal states out of N=n(n−1)2^(n−2)=3584 ordered-terminal subset states. Thus neither color's reachable set exceeds even 22% of all states, much less the 50% needed for the elementary global complement-pigeonhole shortcut. Nonetheless, a spanning one-turn witness is (4,2,0,1,3,7,5,6) with color word (1,1,0,0,0,0).

The state counts follow the recurrence stated above, with the vacuous 2-vertex paths counted in both colors. The example was obtained by local search and its terminal-state counts recomputed independently from the bit-mask representation. It is an obstruction to proving the spanning result via a universal global reachable-state density >1/2, not an obstruction to the conjecture itself. A stronger central-level or endpoint-sensitive inequality might still succeed.
