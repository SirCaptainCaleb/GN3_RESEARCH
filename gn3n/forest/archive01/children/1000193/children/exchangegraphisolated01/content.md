# The success-only endpoint splice graph is isolated at every deletion singleton

## Statement

Let H be a minimum-order counterexample to the grand two-cover conjecture and let H-x=P|Q be any deletion cover. Consider the canonical spanning three-cover P|Q|{x}. In the natural success-only endpoint-to-cut splice graph proposed in the alternating-exchange brainstorm, the singleton endpoint x has no splice edge to any insertion position of the displayed path P and no splice edge to any insertion position of Q. Moreover neither support V(P) union {x} nor V(Q) union {x} is Hamiltonian. Thus a success-only Hall/augmenting-path formulation has an isolated left vertex in the canonical counterexample state and cannot by itself prove augmentation. Any viable exchange graph must encode failed-splice obstruction data, or use a different transition notion, rather than treating absence of successful splice edges as a Hall certificate to be ruled out directly.

## Body

# Proof

Let H be a minimum counterexample and choose a deletion cover

H-x=P|Q.

Regard this as the spanning three-cover

P | Q | {x}.

Suppose x were insertable into some position of the displayed tight path P. Then the resulting order would be a tight path on V(P) union {x}. Together with the unchanged tight path Q, this would be a spanning two-cover of H, contradiction.

Therefore x has no successful insertion splice into P. The same argument applies to Q.

In particular neither induced subtournament H[V(P) union {x}] nor H[V(Q) union {x}] can be Hamiltonian. If, say, V(P) union {x} had any Hamilton path, that Hamilton path together with Q would again be a spanning two-cover of H.

Hence in the natural auxiliary bipartite graph whose left vertices include path endpoints and whose right vertices are insertion/cut positions, with an edge recording a successful endpoint transfer preserving three paths, the singleton component contributes an endpoint x with no neighbor in either nontrivial component.

A Hall obstruction is therefore present already at the one-element set {x}: its neighborhood is empty.

Boundary antisymmetry does not make this failed-splice situation disappear. Rather, the certified failed-insertion calculus converts the absence of insertion into reversed triples and bounded obstruction windows. Those obstruction windows are precisely additional information not represented by the success-only splice graph.

Consequently a viable alternating-exchange formulation must enlarge its state/edge alphabet to carry failed-splice obstruction data, or otherwise replace ordinary success-edge Hall augmentation. The raw success-only graph cannot be the complete proof object for the canonical deletion-singleton state.
