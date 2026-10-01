# Paired transfer normalizes to a Hamiltonicity blockade plus one local insertion gadget

## Statement

In the corrected paired-transfer lemma compatmixedpaired40, each of its two support patterns has both a complementary Hamiltonicity blockade and a legitimate normalized-order dichotomy.

Case I: F_a=(R+{b,c})|S, F_b=(R+{a,c})|S, F_c=R|(S+{a,b}). Then S+{a}, S+{b}, R+{c}, R+{a,b,c}, and S+{a,b,c} are non-Hamiltonian. After normalizing the common S-component of F_a,F_b to one Hamilton order, either the varying paths disagree on the common support R+{c}, or the normalized covers are fully compatible and a,b use equal or adjacent insertion slots in that common order, with the adjacent case forcing the certified reversing triple.

Case II: F_a=(R+{b})|(S+{c}), F_b=(R+{a})|(S+{c}), F_c=R|(S+{a,b}). Then S+{a,c}, S+{b,c}, R+{a,b}, R+{c}, and S+{a,b,c} are non-Hamiltonian. After normalizing the common S+{c} component, either the varying paths disagree on R, or the normalized covers are fully compatible and a,b use equal or adjacent insertion slots in R, again with the adjacent case forcing the reversing triple.

## Body

# Proof

Use the two support patterns from compatmixedpaired40.

## Case I

The three deletion covers have Hamiltonian support pairs

(R+{b,c}) | S,
(R+{a,c}) | S,
R | (S+{a,b}).

Hence each displayed support is Hamiltonian.

Because H has no spanning two-cover, the complement in H of any one of these Hamiltonian supports must be non-Hamiltonian whenever the complement is nonempty.

The complements are:

V(H)-(R+{b,c}) = S+{a},
V(H)-(R+{a,c}) = S+{b},
V(H)-S = R+{a,b,c},
V(H)-R = S+{a,b,c},
V(H)-(S+{a,b}) = R+{c}.

Thus all five listed induced subtournaments are non-Hamiltonian.

Now compare F_a and F_b. Their S-support is literally the same Hamiltonian vertex set. Choose one Hamilton path on S and use that same component in both covers.

The varying Hamilton paths have supports R+{b,c} and R+{a,c}, with common vertex set R+{c}. If their common vertices occur in different relative orders, the ordered-path intersection calculus yields its standard disagreement witness.

Otherwise the varying paths induce the same order on R+{c}. Together with the common normalized S-order, the two covers are fully compatible on H-{a,b}. Therefore d43a7c9e2f61 applies: a and b insert into the common R+{c} order at equal or adjacent slots, and adjacent slots force the certified reversing triple.

## Case II

Now the Hamiltonian support pairs are

(R+{b}) | (S+{c}),
(R+{a}) | (S+{c}),
R | (S+{a,b}).

Taking complements in H gives the forced non-Hamiltonian sets

S+{a,c},
S+{b,c},
R+{a,b},
S+{a,b,c},
R+{c}.

For the order comparison, normalize the common support S+{c} to one Hamilton path in both F_a,F_b. The varying components have supports R+{b} and R+{a}, with common vertex set R.

If the induced R-orders disagree, path intersection gives the explicit disagreement witness. If they agree, the normalized covers are fully compatible and d43a7c9e2f61 gives equal or adjacent insertion slots for a,b in R, with its adjacent-slot reversing triple.

Thus both paired-transfer patterns reduce to a complementary Hamiltonicity blockade plus one legitimate local order-disagreement/insertion gadget.
