# A two-move exchange forbids whole-path extensions at a four-side quadratic minimum

## Statement

Let F=X|P|Q be a spanning three-cover of a boundary tournament, with X=(x_0,x_1,x_2,x_3), P=(p_1,...,p_m), m>=6, and |Q|=q. Suppose F minimizes Phi throughout its connected component under pairwise repartition. If 2m-q>7, then neither Q union {x_0} nor Q union {x_3} is Hamiltonian. More generally, if X union {p_1} and X union {p_m} are non-Hamiltonian but Q union {z} is Hamiltonian for an endpoint z of X, two legal pairwise repartitions yield orders 5,m-2,q+1 and decrease Phi by 4m-2q-14.

## Body

First prove the more general assertion. Fix z in {x_0,x_3}, and write X-z for the inherited three-vertex path. By the repeated-bad-deletion lemma in localextend01, the five-set S=(V(X)-{z}) union {p_1,p_m} is Hamiltonian. Choose a Hamilton path on Q union {z}.

The first move repartitions X|Q as (X-z)|(Q union {z}), leaving P unchanged. It is legal because X-z is a contiguous path and the other support is Hamiltonian by hypothesis. The second move repartitions (X-z)|P as S|(p_2,...,p_{m-1}), leaving Q union {z} unchanged. The five-set is Hamiltonian by the cited lemma, and the middle path is inherited from P. All supports are disjoint and each move preserves its pair-union.

The original potential is 16+m^2+q^2; the final potential is 25+(m-2)^2+(q+1)^2. Their difference is 4m-2q-14. The intermediate potential may increase; both states nevertheless belong to the same connected component.

Now assume F minimizes Phi in that connected component. Each of X union {p_1} and X union {p_m} must be non-Hamiltonian: otherwise transferring that endpoint from P to X gives orders 5,m-1,q and decreases Phi by 2m-10>0. The general construction therefore applies to either endpoint z of X if Q union {z} is Hamiltonian. When 2m-q>7 the final potential is smaller than Phi(F), a contradiction. This proves the assertion for both endpoints.
