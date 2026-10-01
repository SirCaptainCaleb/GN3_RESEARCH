# Every odd support cycle forces two-walk disturbance or a repeated-label double crossing

## Statement

Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1, and let G be its Hamiltonian-support odd graph. Let C=S_0S_1...S_{m-1}S_0 be a simple odd cycle of G, with edge S_iS_{i+1} labelled x_i (indices modulo m). Choose one Hamilton order on each support S_i and use these orders in the canonical exact deletion covers on the cycle edges. Then at least one of the following holds. (I) Some length-two subwalk S_i-S_{i+1}-S_{i+2} exposes one of the non-clean alternatives of astra004twowalk: an inherited three-part crossing or relative-order disagreement. (II) There is an index i with x_{i+3}=x_i. The two distinct cycle edges S_iS_{i+1} and S_{i+3}S_{i+4} are then two distinct exact covers of the same deletion H-x_i; their unordered support partitions differ, so by d9ef8e3fe739 each cover has at least two ordinary crossings across the other support partition. Hence no odd component of maximum degree two can be globally clean: every odd cycle carries explicit crossing/order disturbance.

## Body

# Proof

Assume (I) never occurs. Apply astra004twowalk to every length-two subwalk using the globally chosen Hamilton orders on the supports. Every subwalk is therefore in its clean branch.

For the subwalk S_i-S_{i+1}-S_{i+2}, odd-graph complementation gives
S_{i+2}=(S_i-{x_{i+1}}) union {x_i}.
The clean branch says x_{i+1} is an endpoint of the chosen Hamilton order on S_i, x_i is an endpoint of the chosen Hamilton order on S_{i+2}, and replacing x_{i+1} by x_i preserves the entire common order and uses the same end. Call that end the replacement side of step i.

Now compare consecutive jump-two steps i and i+2. The next clean step removes x_{i+3} from S_{i+2}. In the chosen Hamilton order on S_{i+2}, the endpoint at the previous replacement side is x_i. Therefore, if step i+2 uses the same replacement side as step i, necessarily x_{i+3}=x_i. Otherwise the replacement side flips.

Suppose for contradiction that x_{i+3}!=x_i for every i. Then the replacement side flips at every jump-two step. Because m is odd, addition by 2 modulo m is a single cycle through all m indices. After m successive jump-two steps one returns to the initial support and initial step, but an odd number of side flips changes the side, impossible. Hence x_{i+3}=x_i for some i.

The two cycle edges e_i=S_iS_{i+1} and e_{i+3}=S_{i+3}S_{i+4} therefore have the same omitted label x_i. They are distinct edges of the simple cycle, so their unordered support partitions are distinct. Each is an exact two-cover of H-x_i. Apply d9ef8e3fe739 with one as the reference cover and the other as T. Since the support partitions differ, the crossing number is at least two. This is (II). ∎
