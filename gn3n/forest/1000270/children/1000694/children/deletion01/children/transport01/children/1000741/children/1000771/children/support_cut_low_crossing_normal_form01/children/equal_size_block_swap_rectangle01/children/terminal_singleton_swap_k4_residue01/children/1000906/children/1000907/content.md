# Above order seventeen the hard terminal singleton-swap residue enters the five-side escape trichotomy

## Statement

Let H be a minimum counterexample of order n>=18 in the hard paired matching-block branch of terminal_singleton_swap_k4_residue01. Then H has a spanning three-cover X|P|Q with |X|=5 and max{|P|,|Q|}>=7 such that at least one of the following holds for X together with a longest of P,Q: (1) one legal pairwise repartition strictly decreases quadratic potential; (2) one legal pairwise repartition preserves the component-order multiset and exchanges one vertex of X with one displayed endpoint of that long complementary path; (3) a tight triple containing a vertex of X reverses a displayed edge of that long complementary path.

More precisely, 1000906 supplies a Hamiltonian five-set X through the swapped pair whose complement is non-Hamiltonian with path-cover number exactly two. Any exact two-cover P|Q of H-X has |P|+|Q|=n-5>=13, hence one component has order at least seven. Applying five_side_arbitrary_escape01 to X and that component gives the trichotomy.

This is an escape statement for the produced five-side state; it does not assert that the new three-cover lies in the same pairwise-repartition component as the original terminal singleton-swap state.

## Body

By 1000906, the hard paired endpoint residue contains a Hamiltonian five-set X retaining the two swapped labels, and H-X is non-Hamiltonian with path-cover number exactly two. Choose any exact two-cover P|Q of H-X and relabel so |P|>=|Q|. Since n>=18,
|P|+|Q|=n-5>=13,
so |P|>=ceil((n-5)/2)>=7.

Thus X|P|Q is a spanning three-cover satisfying the hypotheses of five_side_arbitrary_escape01. That theorem gives exactly one of three outcomes for the pair X|P: a legal strict quadratic-potential descent; a legal equal-potential support exchange preserving component orders {5,|P|} and swapping one X-label with a displayed endpoint of P; or a tight triple using a vertex of X that reverses a displayed edge of P.

No trappedness or Phi-minimality hypothesis is needed for five_side_arbitrary_escape01, so no further assumptions are required. The only bookkeeping caution is reachability: the exact two-cover P|Q of H-X comes from minimum-counterexample calculus, not from an asserted reconfiguration path out of the original singleton-swap cover. Accordingly the conclusion is attached to the produced five-side state rather than claimed as a descent inside the original pairwise-repartition component.
