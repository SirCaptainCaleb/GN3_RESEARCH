# Every non-Hamiltonian deletion singleton lift has immediate strict quadratic descent

## Statement

Let H be a minimum counterexample. Let X,Q partition V(H), with H[X] non-Hamiltonian and Q Hamiltonian. Fix d in X, let P=(p_0,...,p_{N-1}) be a Hamilton path on X-{d}, and suppose P|Q is a deletion two-cover of H-d.

Then N>=3 and the singleton lift P|Q|{d} has a legal pairwise repartition
(d,p_0) | (p_1,...,p_{N-1}) | Q
whose quadratic potential is smaller by 2N-4>0.

Consequently no such deletion singleton lift is locally Phi-minimal. In particular, any order-disagreement or restored-label cycle analysis carried out inside this singleton lift automatically lands in strict descent; there is no separate cycle residue to classify at a quadratic minimum.

## Body

Since H[X] is non-Hamiltonian and every boundary tournament of order at most three is Hamiltonian, |X|>=4. Hence N=|X|-1>=3.

The two-vertex sequence (d,p_0) is a tight path vacuously, and (p_1,...,p_{N-1}) is an inherited contiguous subpath of P. Thus replacing the pair P|{d} by these two paths, while leaving Q unchanged, is a legal pairwise repartition.

The changed component orders are N,1 -> 2,N-1. Therefore
Phi_old-Phi_new
=N^2+1-[4+(N-1)^2]
=2N-4>0.
So every such singleton lift strictly descends.

This conclusion is independent of any order disagreement between Hamilton paths on different one-vertex deletions of X, and independent of whether path-intersection calculus produces a reversed edge, reversing triple, old-path cycle, or restored-label cycle. Those refinements may provide additional structure, but none can survive as an obstruction to descent at the singleton-lift level.
