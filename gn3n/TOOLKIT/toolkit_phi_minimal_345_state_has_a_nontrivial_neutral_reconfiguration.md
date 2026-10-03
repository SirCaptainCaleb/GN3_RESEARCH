# Every Phi-minimal 3|4|5 state has a nontrivial neutral reconfiguration

**Summary:** A Phi-minimal 3|4|5 cover always has an explicit equal-Phi move within its repartition component: either a one-step 3|4 endpoint swap to 4|3, or a two-step route 3|4|5 -> 5|2|5 -> 5|3|4. Hence this bounded profile is recurrent rather than rigid.

## Statement

Let H be a minimum counterexample and let T|C|D be a Phi-minimal spanning three-cover with |T|=3, |C|=4, |D|=5. Then there is a nontrivial sequence of at most two pairwise repartitions ending at another three-cover of the same size multiset {3,4,5} and the same quadratic potential.

## Body

Apply toolkit_34_pair_gives_a_neutral_endpoint_swap_or_a_controlled_52_detour to T|C.

In the first outcome, one endpoint of C Hamiltonian-extends T. Replacing T|C by the corresponding 4|3 cover is a one-step nontrivial pairwise repartition with no change in Phi. The third component D is unchanged, so the full size multiset remains {3,4,5}.

In the second outcome, both endpoint extensions are non-Hamiltonian and T|C repartitions as K|E with |K|=5 and |E|=2, where E is the displayed interior edge of C. The first move changes the affected square sum from 3^2+4^2=25 to 5^2+2^2=29, an increase of 4.

Now pair E with the untouched 5-path D=(d_1,...,d_5). The general two-vertex balancing lemma gives a repartition of E|D with component orders 3 and 4: explicitly, E union {d_1} has a tight Hamiltonian 3-path and (d_2,...,d_5) is tight. This changes the affected square sum from 2^2+5^2=29 to 3^2+4^2=25, a decrease of 4.

Thus the two-step route

3|4|5 -> 5|2|5 -> 5|3|4

returns exactly to the original value of Phi and to the same size multiset {3,4,5}. Since the intermediate and final covers are obtained by legal pairwise repartitions, they lie in the same component of the repartition graph.

Therefore every Phi-minimal 3|4|5 state has an explicit neutral recurrence: a one-step endpoint swap or a controlled two-step detour through a temporary two-vertex component.

## Metadata

- ID: toolkit_phi_minimal_345_state_has_a_nontrivial_neutral_reconfiguration
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
