# Above order seventeen every Hamiltonian five-side descends or forces order disagreement

## Statement

Let H be a minimum counterexample of order n>=18. Let W be a proper Hamiltonian five-vertex set such that H-W is non-Hamiltonian with path-cover number two. Choose any displayed two-cover H-W=P|Q. Then either the spanning three-cover W|P|Q lies in a pairwise-repartition component containing a three-cover of strictly smaller quadratic potential Phi, or H contains explicit order disagreement between Hamiltonian paths on overlapping bounded supports.

## Body

# Proof

Write p=|P| and q=|Q|. Since p+q=n-5>=13, at least one of p,q is at least seven; after interchanging P,Q assume p>=7.

Consider the connected component of the pairwise-repartition graph containing the spanning three-cover C=W|P|Q. If C does not minimize Phi in that connected component, then by definition there is a reachable spanning three-cover C_prime in the same component with Phi(C_prime)<Phi(C), giving the first alternative.

Assume instead that C minimizes Phi in its connected component. The five-side W is Hamiltonian, and P has order at least seven. Therefore the certified five-side local-minimum theorem 83353015664a applies to C with X=W and the displayed long path P. It states that for each displayed endpoint e of P the six-set W union {e} is non-Hamiltonian with at least four Hamiltonian one-vertex deletions, and consequently Hamilton paths on those deletions exhibit explicit order disagreement. This is the second alternative.

Thus every Hamiltonian five-side with pc-two complement at order at least eighteen either already has strict quadratic descent inside its move component or forces order disagreement. ∎