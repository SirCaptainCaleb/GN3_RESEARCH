# Astra pair-repartition graph branches at every small deletion side

## Statement

Let H be a minimum counterexample and let P|Q|{x} be the three-cover obtained from an exact deletion cover H-x=P|Q with 3<=|P|<=5. In the pairwise-repartition move graph of Astra idea 003, the connected component of P|Q|{x} contains at least four states of the form R_y|Q|{y}, with distinct y in V(P) union {x}; each such state is reached from P|Q|{x} by one legal repartition of the pair P,{x}. Moreover, among any four chosen Hamilton orders R_y on the varying supports, two have relative-order disagreement on their common vertices.

## Body

Put C=V(P) union {x}. By the certified synchronized-omission theorem 6f72075b0b54, the set G={y in C : H[C-{y}] is Hamiltonian} has size at least four and contains x. For every y in G choose a Hamilton path R_y on C-{y}. The cover R_y|Q|{y} is a spanning three-cover of H.

Starting from P|Q|{x}, consider the two components P and {x}. Their union is exactly C. Replacing these two components by R_y and {y} is legal in the move system of Astra idea 003: R_y and the singleton {y} are at most two tight paths whose supports partition the same union C. The third component Q is unchanged. Hence every y in G gives a state R_y|Q|{y} in the same connected component, in fact at distance one from the starting state. Since |G|>=4, this gives at least four distinct omission-label states and at least three nontrivial outgoing exchanges from the initial state.

The final assertion is again exactly the order-disagreement conclusion of 6f72075b0b54: for any four distinct labels in G and any chosen Hamilton paths on the corresponding C-{y}, the four paths cannot be pairwise compatible, so some pair has different relative order on common vertices.

Thus Astra idea 003 has no locally isolated singleton-deletion state whose smaller non-singleton component has order at most five. Any trapped class in a minimum counterexample must either have minimum deletion side at least six or remain trapped despite this forced branching and order-disagreement data. This matches the one-defect route's order-six threshold and identifies the precise next obstruction: convert one of these disagreement-bearing neighboring states into a move involving Q or into an actual component merge.