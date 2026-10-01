# A global quadratic minimum with a five-vertex path has a complete endpoint-pair two-for-two replacement grid

## Statement

Let H be a minimum counterexample and let X|P|Q be a spanning three-cover minimizing the quadratic potential among all spanning three-covers, with |X|=5 and |P|,|Q|>=7. Let E be the four displayed endpoints of P and Q. Then for every two-element set {e,f} subset E there are distinct x,z in X such that F=(X-{x,z}) union {e,f} is Hamiltonian. Moreover H-F is non-Hamiltonian with path-cover number two, and every two-cover U|V of H-F has component-size imbalance at least ||P|-|Q||. Hence each endpoint pair supports an equal-size five-set replacement whose complementary two-cover cannot be more balanced than the original pair P|Q.

## Body

Write |P|=m and |Q|=r.

First, every endpoint e of P is a bad extension of X. Indeed, if X union {e} were Hamiltonian, then replacing X|P by a Hamilton path on X union {e} together with the inherited path P-e would change the two path orders from 5,m to 6,m-1. The quadratic-potential change would be
[6^2+(m-1)^2]-[5^2+m^2]
=12-2m<0
because m>=7. This contradicts global Phi-minimality. The same argument applies to both endpoints of Q. Thus
X union {e}
is non-Hamiltonian for every e in E.

Fix any distinct e,f in E. Apply the preceding two-bad-extension lemma to the Hamiltonian five-set X and the two bad exterior extensions e,f. It gives distinct x,z in X such that
F=(X-{x,z}) union {e,f}
is Hamiltonian.

Because H is a minimum counterexample, the proper induced subtournament H-F has path-cover number at most two. It cannot be Hamiltonian: a Hamilton path on H-F together with one on F would form a spanning two-cover of H. Hence
pc(H-F)=2.

Choose any two-cover U|V of H-F. Then
F|U|V
is a spanning three-cover of H. Since |F|=5, while |U|+|V|=m+r, global Phi-minimality gives
5^2+|U|^2+|V|^2 >= 5^2+m^2+r^2.
Therefore
|U|^2+|V|^2 >= m^2+r^2.

For fixed total m+r, the sum of squares of two path orders is monotone in the absolute size imbalance. Thus
||U|-|V|| >= |m-r|.

Therefore every pair among the four long-path endpoints admits a Hamiltonian two-for-two replacement of two vertices of X, and every complementary two-cover is at least as imbalanced as the original pair P|Q. ∎
