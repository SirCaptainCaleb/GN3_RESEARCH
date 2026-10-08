# Antipodal degree and minimality force every closed deletion core to be the complete odd middle layer

## Composition

Assume H is a minimum-order boundary 3-tournament without a spanning two-path cover. Let C be ANY nonempty antipodally invariant pure source-sink cubical 1-cocycle made of actual one-hole deletion-cover edges. No minimum-imbalance restriction is imposed.

Use the full-star descent and minimum-degree polarity results (265-267). Choose a source of minimum positive outdegree d and descend to a full-star source D of size d. Let U be its saturated Johnson block. Every d-subset F of U is a full-star source, hence non-Hamiltonian. Every (d-1)-subset R of U is Hamiltonian. For each y outside U, Type I polarity holds relative to every such F: the edge F+y -> F is absent, and every R+y is a sink. In particular the edge R+y -> R is absent.

Claim 1: every R in binom(U,d-1) has incoming degree exactly |U|-d+1 in C.
Indeed each u in U-R gives the full-star edge R+u -> R. Each y outside U gives no such edge, by Type I polarity. These are all possible incoming edges. Since R is a sink, these are all its C-edges.

Antipodal complementation sends a sink of incoming degree t to a source of outgoing degree t. Minimality of d therefore gives
|U|-d+1 >= d, or |U| >= 2d-1.

Claim 2: U=V(H).
Every Hamiltonian path in H[U] has order at most d-1: otherwise a contiguous d-vertex subpath would make a d-subset of U Hamiltonian. If U were proper, minimum-order minimality would supply a two-path cover of H[U], forcing |U| <= 2d-2. This contradicts Claim 1. Thus the saturated Johnson block contains every vertex.

Claim 3: n=2d-1 and C is the complete middle incidence layer.
All d-subsets of V are non-Hamiltonian, so every Hamiltonian support has size at most d-1. For a full-star source F of size d, its actual deletion edge F -> F-x certifies that V-F is Hamiltonian. Therefore n-d <= d-1. Combining this with n=|U| >= 2d-1 gives n=2d-1.
Writing r=d-1, all r-subsets are Hamiltonian and all (r+1)-subsets are non-Hamiltonian. Every (r+1)-set is a full-star source, so all edges from rank r+1 to rank r belong to C. Conversely an actual deletion cover consists of two Hamiltonian supports whose sizes sum to 2r; since neither can exceed r, both have size r. Thus no other deletion edge exists.

Consequences.
1. A minimum counterexample of even order has no nonempty antipodally invariant closed top residue, for ANY family of actual deletion covers.
2. At odd order, any such residue forces the original full deletion-cover interface itself to be precisely the complete middle layer. There are then no unique-incidence top faces, so a top leaf collapse begun with the full interface cannot make even its first move.
3. Starting from the full deletion interface, the terminalization dichotomy is consequently exact: either every top facet is removed, or no top facet can be removed and the interface is already the odd uniform middle layer.
4. This strengthens 262: minimum imbalance is unnecessary, and its conditional even half-set residue is excluded by full-star descent, antipodal degree, and proper-induced two-coverability.

Limits. This is not closure. The all-collapsed case still requires an actual spanning cover or a contradiction, and the odd uniform family still needs a genuine augmentation argument. It is invalid to infer either conclusion merely from the existence or absence of top homology. The proof supplies a global restriction on any surviving core, not a terminal path surgery.

## Development

Assume H is a minimum-order boundary 3-tournament without a spanning two-path cover. Let C be ANY nonempty antipodally invariant pure source-sink cubical 1-cocycle made of actual one-hole deletion-cover edges. No minimum-imbalance restriction is imposed.

Use the full-star descent and minimum-degree polarity results (265-267). Choose a source of minimum positive outdegree d and descend to a full-star source D of size d. Let U be its saturated Johnson block. Every d-subset F of U is a full-star source, hence non-Hamiltonian. Every (d-1)-subset R of U is Hamiltonian. For each y outside U, Type I polarity holds relative to every such F: the edge F+y -> F is absent, and every R+y is a sink. In particular the edge R+y -> R is absent.

Claim 1: every R in binom(U,d-1) has incoming degree exactly |U|-d+1 in C.
Indeed each u in U-R gives the full-star edge R+u -> R. Each y outside U gives no such edge, by Type I polarity. These are all possible incoming edges. Since R is a sink, these are all its C-edges.

Antipodal complementation sends a sink of incoming degree t to a source of outgoing degree t. Minimality of d therefore gives
|U|-d+1 >= d, or |U| >= 2d-1.

Claim 2: U=V(H).
Every Hamiltonian path in H[U] has order at most d-1: otherwise a contiguous d-vertex subpath would make a d-subset of U Hamiltonian. If U were proper, minimum-order minimality would supply a two-path cover of H[U], forcing |U| <= 2d-2. This contradicts Claim 1. Thus the saturated Johnson block contains every vertex.

Claim 3: n=2d-1 and C is the complete middle incidence layer.
All d-subsets of V are non-Hamiltonian, so every Hamiltonian support has size at most d-1. For a full-star source F of size d, its actual deletion edge F -> F-x certifies that V-F is Hamiltonian. Therefore n-d <= d-1. Combining this with n=|U| >= 2d-1 gives n=2d-1.
Writing r=d-1, all r-subsets are Hamiltonian and all (r+1)-subsets are non-Hamiltonian. Every (r+1)-set is a full-star source, so all edges from rank r+1 to rank r belong to C. Conversely an actual deletion cover consists of two Hamiltonian supports whose sizes sum to 2r; since neither can exceed r, both have size r. Thus no other deletion edge exists.

Consequences.
1. A minimum counterexample of even order has no nonempty antipodally invariant closed top residue, for ANY family of actual deletion covers.
2. At odd order, any such residue forces the original full deletion-cover interface itself to be precisely the complete middle layer. There are then no unique-incidence top faces, so a top leaf collapse begun with the full interface cannot make even its first move.
3. Starting from the full deletion interface, the terminalization dichotomy is consequently exact: either every top facet is removed, or no top facet can be removed and the interface is already the odd uniform middle layer.
4. This strengthens 262: minimum imbalance is unnecessary, and its conditional even half-set residue is excluded by full-star descent, antipodal degree, and proper-induced two-coverability.

Limits. This is not closure. The all-collapsed case still requires an actual spanning cover or a contradiction, and the odd uniform family still needs a genuine augmentation argument. It is invalid to infer either conclusion merely from the existence or absence of top homology. The proof supplies a global restriction on any surviving core, not a terminal path surgery.
