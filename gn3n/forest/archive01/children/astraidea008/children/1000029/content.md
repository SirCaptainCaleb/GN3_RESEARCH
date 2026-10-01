# Astra 008 eliminates all half-order slack but is vacuous on the sharp odd shell

## Statement

Assume Astra idea 008 holds. Let H be a minimum counterexample of order n and let lambda be its maximum tight-path order. Then H must lie in the sharp odd half-order shell n=2lambda+1. Conversely, on that shell Astra 008 is identically vacuous: with k=floor(n/2)=lambda, the complement of every k-set has order lambda+1 and is therefore non-Hamiltonian, so the second marginal and the joint probability are both zero.

## Body

Minimum-counterexample calculus gives lambda>=ceil((n-1)/2).

First suppose n=2k is even. Then lambda>=k, so H has a Hamiltonian k-set. For uniformly random k-set S, the two marginals in Astra 008 are equal by complementation and are therefore both positive. The conjectured inequality then gives positive probability that both S and its complement are Hamiltonian. Those two Hamilton paths form a spanning two-cover of H, contradiction.

Now suppose n=2k+1 is odd and lambda>=k+1. Then some (k+1)-set R is Hamiltonian, so the complement marginal Pr(H[V(H)-S] Hamiltonian) is positive. A Hamilton path on R contains a tight k-vertex subpath, so the k-set Hamiltonicity marginal is also positive. Astra 008 again makes the joint probability positive, producing complementary Hamiltonian supports of orders k and k+1 and hence a spanning two-cover, contradiction.

Thus any minimum counterexample surviving Astra 008 must have n=2k+1 and lambda=k, i.e. n=2lambda+1.

Finally, in this sharp shell no (lambda+1)-vertex set is Hamiltonian by definition of lambda. Since k=lambda, for every sampled k-set S the complement V(H)-S has lambda+1 vertices and is non-Hamiltonian. Hence
Pr(H[V(H)-S] Hamiltonian)=0
and
Pr(H[S] and H[V(H)-S] both Hamiltonian)=0.
The Astra-008 inequality reduces to 0>=0 and yields no further information. ∎
