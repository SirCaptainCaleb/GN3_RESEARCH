# A complete reverse fan forces a sharp linear star of overlapping Hamiltonian five-sets

## Statement

Let H be a minimum counterexample and let T=(x,v,u) be the tight three-vertex path from a complete reverse fan. Put L=V(H)-V(T) and join a,b in a graph J when T union {a,b} is Hamiltonian. Then alpha(J)<=2. If r=|L|, Mantel's theorem gives e(J)>=binom(r,2)-floor(r^2/4), so some a has at least floor((r-1)/2) neighbors. Hence at least floor((r-1)/2) Hamiltonian five-sets share the same four-core T union {a}; every one has non-Hamiltonian path-cover-two complement. Since |H|>10, r>=8 and the star has at least three leaves.

## Body

For any three distinct a,b,c in L, the fixed-three-path extension theorem applied to T gives a Hamiltonian five-set among T+{a,b}, T+{a,c}, T+{b,c}. Thus every three vertices of J span an edge, so alpha(J)<=2 and the complement of J is triangle-free. Mantel gives e(J)>=binom(r,2)-floor(r^2/4). The ceiling of the resulting average-degree lower bound is floor((r-1)/2), so choose a with at least that many neighbors B. For every b in B, T+{a,b} is a proper Hamiltonian five-set. Its complement cannot be Hamiltonian, else H has a two-cover; by minimality the complement has path-cover number exactly two. The degree guarantee is sharp under alpha(J)<=2, via complements of balanced complete bipartite graphs.