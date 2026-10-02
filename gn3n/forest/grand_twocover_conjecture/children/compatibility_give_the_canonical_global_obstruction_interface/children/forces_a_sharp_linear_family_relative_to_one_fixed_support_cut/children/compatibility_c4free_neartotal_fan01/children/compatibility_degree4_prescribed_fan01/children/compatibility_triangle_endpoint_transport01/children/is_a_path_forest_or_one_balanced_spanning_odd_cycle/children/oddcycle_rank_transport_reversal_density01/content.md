# Odd-cycle rank transport forces linearly many adjacent-slot reversal gadgets

## Statement

In the exceptional spanning odd-cycle compatibility configuration on n=2k+1 labels, traverse the balanced Hamiltonian supports in the step-two order S_0,S_2,S_4,... . For each transition S_i to S_{i+2}, compatible-pair localization says that the outgoing label d_{i+1} and incoming label d_i occupy either the same insertion slot or adjacent insertion slots of the common (k-1)-vertex Hamilton order. Transporting rank tokens through these replacements, a same-slot move induces the identity permutation and an adjacent-slot move induces one adjacent transposition. After one full circuit the total rank permutation is a k-cycle. Consequently at least k-1=(n-3)/2 transitions are adjacent-slot replacements, hence force reversing tight triples. Moreover every adjacent rank boundary 1|2,...,(k-1)|k occurs in at least one such reversal.

## Body

Assume the exceptional spanning odd-cycle compatibility configuration on n=2k+1 labels, with balanced Hamiltonian supports S_i of order k and
F_{d_i}=S_{i-1}|S_i
cyclically. The support identity may equivalently be indexed so that
S_{i+2}=S_i-{d_{i+1}}+{d_i}.

Consider a transition from S_i to S_{i+2}. The corresponding neighboring deletion covers are fully compatible, and the two Hamilton paths have common ordered vertex set
R_i=S_i-{d_{i+1}}=S_{i+2}-{d_i}
of order k-1. By the compatible-pair insertion localization from compatibility_give_the_canonical_global_obstruction_interface, the omitted/restored vertices d_{i+1} and d_i occur in either the same insertion slot of R_i or in adjacent insertion slots. In the adjacent-slot case, if the intervening common vertex is z, the triple with the two replacement vertices reverses: one orientation is non-tight and its boundary flip is tight. Thus every adjacent-slot transition supplies a reversing tight triple.

Attach k abstract rank tokens to the k positions of the Hamilton order on S_i. Transport them through a transition S_i to S_{i+2} by letting the incoming vertex d_i inherit the token carried by the outgoing vertex d_{i+1}, while every common vertex keeps its token. If the replacement uses the same insertion slot, the induced permutation of rank positions is the identity. If it uses adjacent slots, precisely the token of the replacement vertex crosses the intervening common vertex, so the induced rank permutation is one adjacent transposition s_j for some j in {1,...,k-1}.

Now traverse all supports in the step-two order
S_0,S_2,S_4,...,
with indices modulo 2k+1. Since gcd(2,2k+1)=1, this visits every S_i exactly once before returning to S_0.

Track the labels carried by the initial position tokens. Starting from
S_0={d_1,d_3,...,d_{2k-1}},
the replacement rule d_{i+1}->d_i along this full circuit transports the token initially on d_1 to the final position occupied by d_{2k-1}, the token initially on d_3 to the final position occupied by d_1, and successively around the alternating support. Thus the total permutation of the k rank tokens after the circuit is one k-cycle.

Therefore the product of the adjacent transpositions contributed by the adjacent-slot transitions is a k-cycle. A k-cycle has Coxeter length at least k-1 with respect to adjacent transpositions; equivalently any expression of a k-cycle as a product of adjacent transpositions contains at least k-1 factors. Hence at least k-1=(n-3)/2 transitions are adjacent-slot replacements, and therefore at least that many compatibility transitions supply reversing tight triples.

There is also a support statement across rank boundaries. If some generator s_j never occurred, then every transition permutation would preserve the initial segment {1,...,j} of rank positions setwise, so their product would preserve this proper nonempty subset. A k-cycle preserves no proper nonempty subset. Hence every generator s_j, j=1,...,k-1, occurs at least once.

Thus the exceptional odd-cycle configuration contains reversal gadgets spanning every adjacent rank boundary of its balanced Hamilton orders; same-slot replacement alone cannot carry the cyclic monodromy.