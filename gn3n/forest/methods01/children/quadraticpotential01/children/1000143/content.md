# A restoration-containing interval cycle forces strict quadratic descent

## Statement


Let H be a minimum counterexample and let H-d=P|Q be a deletion cover, with P=(p_0,...,p_{N-1}). Consider the singleton lift P|Q|{d}. Suppose that for some 0<=j<i<=N-1 there is a vertex-simple tight cycle whose cyclic order is
d,p_j,p_{j+1},...,p_i,d
up to cyclic rotation.

Then the singleton lift has a legal pairwise repartition with strictly smaller quadratic potential.


## Body

Let N=|P|. If H[V(P) union {d}] were Hamiltonian, a Hamilton path on V(P) union {d} together with the displayed path Q would be a spanning two-cover of H, impossible. Hence H[V(P) union {d}] is non-Hamiltonian.

If N=2, then V(P) union {d} has three vertices. Every three-vertex boundary tournament is Hamiltonian, because exactly one member of either reversal pair on its three vertices is tight and itself gives a three-vertex tight path. This contradicts the preceding paragraph. Therefore N>=3.

Now replace the pair P|{d} by the two paths (d,p_0) and (p_1,...,p_{N-1}), leaving Q unchanged. The first path has order two and is tight vacuously; the second is an inherited contiguous subpath of P. The changed component orders are N,1 -> 2,N-1, so the quadratic contribution changes by

4+(N-1)^2-(N^2+1)=4-2N<0

for N>=3. This is one legal pairwise repartition in the same reconfiguration component, hence gives strict quadratic-potential descent.

Thus the stated conclusion holds. In fact the cycle hypothesis is stronger than necessary; the descent follows for every deletion singleton lift once the displayed component has order at least three.