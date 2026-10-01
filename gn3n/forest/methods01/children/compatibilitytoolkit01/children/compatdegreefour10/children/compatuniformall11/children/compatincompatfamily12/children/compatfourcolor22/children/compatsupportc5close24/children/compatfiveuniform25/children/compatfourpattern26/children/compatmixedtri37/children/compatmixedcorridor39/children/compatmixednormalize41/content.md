# Normalizing the fixed supports turns a mixed corridor into two legitimate local insertion gadgets

## Statement

In the corrected blue-path mixed corridor compatmixedcorridor39, write F_b=P|Q, F_a=(P-{a}+{b})|Q, and F_c=P|(Q-{c}+{b}) at the support level. For the pair F_a,F_b, replace the Q-components by one common Hamilton order of H[Q]. Then either the two varying component orders disagree on P-{a}, yielding the standard ordered-path disagreement witness, or the normalized covers are fully compatible and a,b occupy equal or adjacent insertion slots in the common P-{a} order; in the adjacent case the certified reversing triple is forced. Symmetrically, after normalizing the common P-component of F_b,F_c, either there is order disagreement on Q-{c}, or b,c occupy equal or adjacent insertion slots there, with the adjacent case forcing a reversing triple. Thus the mixed corridor reduces soundly to two local order-disagreement/insertion gadgets sharing the same replacement label b.

## Body

# Proof

Use the support identities from compatmixedcorridor39:

F_b=P|Q,
F_a=(P-{a}+{b})|Q,
F_c=P|(Q-{c}+{b}).

We first compare F_a and F_b.

The support Q is literally the same vertex set in both covers and is Hamiltonian. Choose one Hamilton path order on H[Q] and use that same Q-component in both deletion covers. This replacement does not affect the Hamiltonian varying components.

Now inspect the two varying Hamilton paths, one on P and one on P-{a}+{b}. Their common vertex set is P-{a}.

If two common vertices occur in different relative orders, the ordered-path intersection calculus applies and gives its standard explicit witness: a reversed common ordered edge, a tight triple reversing an ordered edge at an intersection, or a vertex-simple tight cycle.

Assume instead that all vertices of P-{a} occur in the same relative order in the two varying paths. Because the Q-components were normalized to the same order, the two complete deletion covers are now fully compatible on H-{a,b}.

The compatible-pair theorem d43a7c9e2f61 therefore applies legitimately. It says that a in F_b and b in F_a insert into the common ordered P-{a} support at equal or adjacent slots. If the slots are adjacent, its local conclusion forces the reversing triple through the unique intervening common vertex.

Thus the F_a,F_b comparison has exactly the claimed dichotomy.

For F_b,F_c, normalize the common P-component to one Hamilton order in both covers and repeat the argument on the varying supports Q and Q-{c}+{b}. Either their common Q-{c} order disagrees, giving the ordered-path witness, or the normalized covers are fully compatible and b,c use equal or adjacent slots, with the adjacent case forcing the certified reversing triple.

The two local gadgets share the same replacement label b and occur on opposite components of the middle deletion cover F_b.