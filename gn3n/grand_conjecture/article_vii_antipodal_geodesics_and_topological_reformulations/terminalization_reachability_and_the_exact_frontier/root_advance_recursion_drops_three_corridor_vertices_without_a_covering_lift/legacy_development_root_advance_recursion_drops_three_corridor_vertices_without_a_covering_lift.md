# Root-advance recursion drops three corridor vertices without a covering lift — preserved pre-item development

## Development

## Root-advance recursion must preserve the vertices already cut off

The local alternatives in [[three_common_reversers_force_a_three_cover_by_finite_root_advance]] are valid up to its recursive call. But that call proves a statement on a strictly smaller vertex set and does not supply the asserted three-cover of the original set.

In the displayed p_2-rooted case, the original set is
\[
W=V(P)\cup V(Q)\cup U,
\]
whereas the recursive set is
\[
W'=V(p_3,p_4,\ldots)\cup V(q_2,q_3,\ldots)\cup U
   =W-\{p_1,p_2,q_1\}.
\]
A three-cover of W' does not cover the three removed corridor vertices. No reinsertion or path-count-preserving extension lemma is given.

The earlier Hamiltonian sets K_z=S-{z} cannot simply be kept alongside the recursive cover: each contains two labels of U, while the recursive configuration still uses all three labels of U. The resulting paths overlap. Covering the removed three-set separately would add a fourth path; repeated recursion could add one path at every step.

Thus “the total tail length decreases” proves termination of the sequence of common-reverser configurations, but does not prove termination with a three-cover of W. Termination and preservation of the covering conclusion are distinct obligations.

**Verified corrected reduction.** Under the common-initial-reverser hypotheses, the displayed local step yields either:
1. one of the explicitly constructed three-covers of W; or
2. shorter tails with the same three reverser labels, together with a removed three-vertex set A={p_1,p_2,q_1} and Hamiltonian five-sets K_z covering A plus U-{z}.

This reduction becomes a three-cover theorem only after proving a lifting statement: a suitably specified three-cover of the shorter configuration extends over A without increasing the number of paths. A generic three-cover is not presently shown to have that property. An alternative valid induction must retain a state recording disjoint packet ownership and the required endpoint orientations.

This audit concerns the proof's covering invariant. It is not a counterexample to the three-cover statement or the grand theorem, and it leaves the direct nonrecursive outcomes and the common-reverser five-path lemma intact.
