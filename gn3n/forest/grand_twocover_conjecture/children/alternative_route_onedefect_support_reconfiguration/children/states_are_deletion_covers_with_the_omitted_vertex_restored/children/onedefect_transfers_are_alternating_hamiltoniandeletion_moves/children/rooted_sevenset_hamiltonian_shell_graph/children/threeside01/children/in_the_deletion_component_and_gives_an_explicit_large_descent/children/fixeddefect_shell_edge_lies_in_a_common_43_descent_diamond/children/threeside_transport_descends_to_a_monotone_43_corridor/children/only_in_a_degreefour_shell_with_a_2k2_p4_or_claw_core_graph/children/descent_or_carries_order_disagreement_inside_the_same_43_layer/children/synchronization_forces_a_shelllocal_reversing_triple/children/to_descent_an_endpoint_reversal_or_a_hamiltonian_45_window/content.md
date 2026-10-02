# The fixed-defect second-layer fork reduces to descent, an endpoint reversal, or a Hamiltonian 4/5 window

## Statement

In the fixed-defect lower-shell setup with tail order at least six, either two lower 4|3 states admit synchronized strict second-layer descent, or there is a reachable state K|T|R such that one of the following holds: (i) a tight triple reverses an end edge of the displayed Hamiltonian four-path K; (ii) H contains a proper Hamiltonian four-set with non-Hamiltonian path-cover-two complement; or (iii) H contains a proper Hamiltonian four- or five-set meeting a displayed endpoint of T, with non-Hamiltonian path-cover-two complement. Thus after the new shell synchronization machinery, the only reversal not already absorbed into the standard small-window engine is a four-side endpoint-edge reversal.

## Body

Start from synchronization_forces_a_shelllocal_reversing_triple. If its synchronized strict second-layer descent branch holds, we are done. Otherwise there is a reachable lower-layer cover
K | T | R,
where K=(k_0,k_1,k_2,k_3) is a Hamiltonian four-path, T is the inherited long tail, and a tight triple S contained in the shell five-set F reverses an ordered edge of K.

If the reversed edge is k_0k_1 or k_2k_3, conclusion (i) holds. Assume therefore that the reversed edge is the internal edge k_1k_2.

Apply hamiltonian_cyclic_or_uniquely_ordered_matchingblock_fourkernel to K and S. It produces a four-vertex kernel X contained in V(K) union V(S), hence contained in F, with one of three possibilities: X is Hamiltonian; X is the exceptional cyclic non-Hamiltonian K4; or X is the uniquely oriented edge-orderable matching-block K4.

The cyclic possibility is impossible here. The five-set F is non-Hamiltonian by the construction in descent_or_carries_order_disagreement_inside_the_same_43_layer, hence smallset01 gives an edge-order representation of F. Every induced four-set of an edge-orderable boundary tournament is edge-orderable, whereas the exceptional cyclic K4 is not. Thus X cannot be cyclic.

If X is Hamiltonian, it is a proper Hamiltonian four-set in the minimum counterexample. Its complement cannot be Hamiltonian, since otherwise the Hamilton path on X and a Hamilton path on the complement would two-cover H. Minimum-counterexample calculus therefore gives path-cover number exactly two on H-X. This is conclusion (ii).

It remains that X is the matching-block kernel. Let t be either displayed endpoint of the inherited tail T. Since t lies outside the shell five-set F, it lies outside X. Apply fourset_always_extends_to_a_hamiltonian_four_or_fiveset with y=t. That theorem gives either a Hamiltonian four-set formed from its reverse-fan triple together with t, or a Hamiltonian five-set X union {t}. In either case the support W has order four or five and contains the displayed tail endpoint t. It is proper, and minimum-counterexample calculus again implies that H-W is non-Hamiltonian with path-cover number exactly two. This is conclusion (iii).

Therefore an internal reversed edge from the lower-shell obstruction is fully absorbed into the standard Hamiltonian 4/5-window frontier, and in the matching-block case the resulting window can be chosen endpoint-aligned with the long tail. Only a reversal of an end edge of K remains outside that frontier.