# Every endpoint-pair grid cell has a strictly more imbalanced two-cover complement

## Statement

Let H be a minimum counterexample and let X|P|Q minimize Phi=sum |C_i|^2 among all spanning three-covers of H, with |X|=4, |P|=m>=6, and |Q|=r>=6. Let E be the four displayed endpoints of P and Q, and put d=|m-r|. For every x in V(X) and every pair {e,f} subset E, let F=(V(X)-{x}) union {e,f}. Then F is Hamiltonian, H-F is non-Hamiltonian with path-cover number two, and every two-cover U|V of H-F satisfies
||U|-|V||^2 >= d^2+2(m+r)-19 > d^2.
Hence every such complement cover is strictly more imbalanced than P|Q. In particular, after relabeling so m>=r, every two-cover of every one of these 24 complements has smaller component order at most r-1.

## Body

The Hamiltonicity of every five-set
F=(V(X)-{x}) union {e,f}
is exactly the complete endpoint-pair grid theorem e8189e57c528.

Fix one such F. Since H is a minimum counterexample, the proper induced subtournament H-F has path-cover number at most two. It cannot be Hamiltonian: otherwise a Hamilton path on H-F together with a Hamilton path on F would give a spanning two-cover of H. Therefore H-F is non-Hamiltonian and has path-cover number two.

Let U|V be any two-cover of H-F, and write
u=|U|, v=|V|.
Then
F|U|V
is a spanning three-cover of H. Global Phi-minimality of X|P|Q gives
16+m^2+r^2 <= 25+u^2+v^2,
so
u^2+v^2 >= m^2+r^2-9.

Also
u+v=|V(H)|-5=m+r-1.

Let
d=|m-r|,
delta=|u-v|.
Using
2(m^2+r^2)=(m+r)^2+d^2
and
2(u^2+v^2)=(m+r-1)^2+delta^2,
the preceding inequality becomes
(m+r-1)^2+delta^2 >= (m+r)^2+d^2-18.
Hence
delta^2 >= d^2+2(m+r)-19.

Because m,r>=6, we have m+r>=12, so
2(m+r)-19>=5.
Thus delta^2>d^2 and therefore delta>d: every complement cover is strictly more imbalanced than the original pair P|Q.

Finally assume m>=r. If the smaller component of U|V had order at least r, then, since u+v=m+r-1, the larger component would have order at most m-1. Its imbalance would therefore be at most
(m-1)-r=d-1,
contradicting delta>d. Hence the smaller component has order at most r-1.

The conclusion holds simultaneously for all four choices of x and all six endpoint pairs {e,f}, giving 24 Hamiltonian five-sets whose complements uniformly drop the smaller-side scale.