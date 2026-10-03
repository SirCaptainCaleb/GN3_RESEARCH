# A Phi-minimal 3|4|4 state has a neutral swap, an order disagreement, or a common terminal pair

**Summary:** For a Phi-minimal 3|4|4 cover T|A|B, either T has a neutral endpoint swap with A or B, or both 3|4 pairs force Hamiltonian five-paths T plus the two displayed endpoints of the 4-side. If those two five-paths use different endpoint pairs in T, they disagree on the order of T; otherwise both use the same two vertices of T as endpoints.

## Statement

Let H be a minimum counterexample and let T|A|B be a Phi-minimal spanning three-cover with |T|=3 and |A|=|B|=4, where A=(a_1,a_2,a_3,a_4) and B=(b_1,b_2,b_3,b_4). Then at least one of the following holds: (i) T|A or T|B admits a Phi-neutral 3|4 to 4|3 endpoint swap; (ii) there are Hamiltonian five-paths K_A on V(T) union {a_1,a_4} and K_B on V(T) union {b_1,b_4} whose restrictions to V(T) have different relative orders; (iii) there is a fixed two-set E subset V(T) such that both K_A and K_B can be chosen with endpoint set exactly E.

## Body

Apply toolkit_34_pair_gives_a_neutral_endpoint_swap_or_a_controlled_52_detour to T|A and T|B.

If either pair is in the neutral endpoint-swap outcome, we have (i). Assume neither is. Then both endpoint extensions are non-Hamiltonian on each side. The controlled two-bad-four-extensions lemma yields a Hamiltonian five-path K_A on V(T) union {a_1,a_4} with both endpoints in V(T), and similarly a Hamiltonian five-path K_B on V(T) union {b_1,b_4} with both endpoints in V(T). Let E_A,E_B be their two-element endpoint sets inside V(T).

If E_A is not equal to E_B, then the restrictions of K_A and K_B to the common three-set V(T) have different relative orders. Indeed, because both global endpoints of each K lie in T, those two endpoints are exactly the first and last vertices of T in the restricted order. Distinct endpoint pairs therefore give distinct extremal pairs, so the restricted total orders cannot agree. This is outcome (ii). The standard order-disagreement machinery then turns such a pair into a tight reversal.

If E_A=E_B, put E=E_A. Then both forced Hamiltonian five-paths use the same two vertices of T as their global endpoints, giving outcome (iii).

Thus the only 3|4|4 state that avoids both a neutral endpoint swap and an order disagreement is a common-terminal-pair configuration: the two locked 4-sides synchronize on the same pair of endpoints in the 3-side.

## Metadata

- ID: toolkit_a_neutral_swap_an_order_disagreement_or_a_common_terminal_pair
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
