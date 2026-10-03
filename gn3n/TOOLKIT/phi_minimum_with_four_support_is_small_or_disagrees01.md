# A quadratic minimum containing a four-support is small or has an order disagreement

**Summary:** If a Phi-minimal three-cover contains a 4-component, then either it also contains a 3-component and lies in the previously classified order-at-most-thirteen regime, or a four-side comparison yields an order disagreement, or all component orders lie between four and six and the total order is at most eighteen.

## Statement

Let H be a minimum counterexample and let C=P_1|P_2|P_3 be Phi-minimal in its pairwise-repartition component. Suppose some component has order four. Then at least one of the following holds: (1) C has a component of order three, hence |V(H)|<=13 and its size multiset is one of {3,3,5},{3,4,4},{3,4,5},{3,5,5}; (2) for the four-component X and some other displayed path P, the endpoint six-set of four_path_long_pair_escape01 has Hamiltonian five-vertex deletions with an order disagreement; (3) every component order belongs to {4,5,6}, so |V(H)|<=18 and the size multiset is one of {4,4,4},{4,4,5},{4,4,6},{4,5,5},{4,5,6},{4,6,6}.

## Body

Let X be a displayed component of order four. If another component has order three, [[toolkit_a_phi_minimum_containing_a_three_path_has_order_at_most_thirteen]] gives outcome (1). Assume therefore that the other two component orders are at least four. Let P be either of them, of order m. If m>=7, apply [[four_path_long_pair_escape01]] to X|P. Its strict-descent alternative contradicts Phi-minimality, and its neutral migration occurs only when m=6. Therefore the only possible outcome for m>=7 is the order-disagreement alternative. Hence, if no such disagreement occurs, both components other than X have order at most six. Since they have order at least four, every component order lies in {4,5,6}. The six displayed multisets and the bound |V(H)|<=18 follow immediately.

## Metadata

- ID: phi_minimum_with_four_support_is_small_or_disagrees01
- Kind: toolkit
- Version: 2
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
