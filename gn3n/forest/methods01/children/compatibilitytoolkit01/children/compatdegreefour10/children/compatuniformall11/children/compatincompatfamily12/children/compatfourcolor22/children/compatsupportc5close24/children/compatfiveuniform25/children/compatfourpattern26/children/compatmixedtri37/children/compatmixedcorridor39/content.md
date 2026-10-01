# A blue-path mixed triangle is an opposite-component support-replacement corridor

## Statement

Assume the blue-path mixed-triangle normal form compatmixedtri37(A): F_a is support-compatible with F_b, F_b is support-compatible with F_c, F_a and F_c are support-incompatible, and their support disagreement is carried exactly by b. Write F_b=P|Q. Then a and c lie on opposite supports of F_b. After interchanging P,Q if necessary, take a in P and c in Q. At the support level one has F_a=(P-{a}+{b}) | Q and F_c=P | (Q-{c}+{b}), where each displayed support is Hamiltonian in the corresponding deletion cover. No common-order or insertion-slot conclusion is implied by support compatibility alone.

## Body

# Proof

Support compatibility of F_a and F_b means that after deleting a and b, the two covers induce the same two support classes.

Suppose a and b restored into different common support classes. Then the component of F_a containing b and the component of F_b containing a are disjoint Hamiltonian supports whose union is V(H). They would give a spanning two-cover of H, impossible. Hence a and b restore into the same common support class.

Therefore, if a lies on P in F_b=P|Q, then b lies on the corresponding P-{a} class in F_a, while the untouched support is Q. Thus the support partition of F_a is

(P-{a}+{b}) | Q.

Apply the same support-only argument to F_b and F_c. If c lies on one support of F_b, then b lies on that same support in F_c, and the other support is unchanged.

Now compatmixedtri37(A) says the support incompatibility of F_a and F_c is carried exactly by b. Thus b lies in opposite core classes in F_a and F_c. Consequently a and c lie on opposite supports of F_b.

After interchanging P,Q if necessary, let a lie on P and c on Q. Then

F_a=(P-{a}+{b}) | Q,
F_c=P | (Q-{c}+{b})

at the support level.

This is a persistent-label support-replacement corridor: the same label b substitutes for a vertex of P in one neighboring deletion state and for a vertex of Q in the other, while the opposite support remains fixed.

Importantly, support compatibility does not identify the Hamilton orders on the common support. Therefore no equal-or-adjacent insertion-slot conclusion is asserted.
