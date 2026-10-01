# Six odd edges force local disturbance or a repeated-label double crossing

## Statement

Let H be a minimum counterexample in the sharp half-order shell, and let S_0-S_1-...-S_6 be a simple path of six edges in the Hamiltonian-support odd graph, with edge S_iS_{i+1} labelled x_i for 0<=i<=5. Choose one Hamilton order on each support S_i. Then at least one of the following holds. (I) One of the jump-two subwalks S_0-S_1-S_2, S_2-S_3-S_4, S_4-S_5-S_6 exposes a non-clean astra004twowalk alternative: inherited three-part crossing or relative-order disagreement. (II) Two of the six edge labels x_0,...,x_5 are equal. The corresponding distinct odd edges are then two exact covers of the same one-vertex deletion with different support partitions, so d9ef8e3fe739 forces at least two ordinary crossings across the other partition. In particular every six-edge degree-two corridor exposes explicit crossing/order complexity; a featureless clean label-simple corridor has length at most five.

## Body

# Proof

Assume (I) fails, so the three displayed jump-two walks are clean. If two edge labels are already equal, (II) holds and d9ef8e3fe739 gives the crossing conclusion because the path is simple and the two edges are distinct. Hence suppose for contradiction that x_0,...,x_5 are pairwise distinct.

Cleanliness of S_0-S_1-S_2 says that x_1 is an endpoint of the chosen Hamilton order on S_0, x_0 is the corresponding endpoint of the chosen order on S_2, and the opposite endpoint is unchanged.

Cleanliness of S_2-S_3-S_4 says x_3 is an endpoint of S_2. Since x_3!=x_0, it must be the opposite endpoint from x_0. Therefore the endpoints of S_2 are exactly x_0,x_3. Replacing x_3 by x_2 at that same end gives the chosen Hamilton order on S_4 with endpoints exactly x_0,x_2.

Now cleanliness of S_4-S_5-S_6 says x_5 is an endpoint of the chosen Hamilton order on S_4. Hence x_5 is x_0 or x_2, contradicting pairwise distinctness. Thus some two edge labels are equal, proving (II). The final crossing conclusion is d9ef8e3fe739. ∎
