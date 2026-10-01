# Rigid zero-slack cross-half edges match the entrance half-deficit

## Statement

In the rigid zero-slack half-neighborhood setting with S=N_G(y)=N_G(z), let e={x,y,z}, |S|=k, X=S disjoint-union B_X disjoint-union e, and put t=|N_G(x)∩S|. Then x has exactly k-t neighbors in B_X, and the number of DXX graph edges joining S to B_X is at least k-t.

## Body

The first assertion is immediate from k-regularity of G. The vertex x has no neighbors y,z inside its own forest triple e, so all k neighbors of x lie in S union B_X. Hence
d_{B_X}(x)=k-t.

Now count degree from S. Every s∈S has degree k, so the total degree sum over S is k^2.

There are no G-edges inside any forest triple. The set S is the disjoint union of |S|/3=k/3 forest triples, so compared with a complete graph on S, at least 3(k/3)=k internal pairs are forbidden. Thus
2e_G(S) <= k(k-1)-2k = k(k-3).

The edges from S to e consist of all sy and sz edges, because N(y)=N(z)=S, together with the t edges from S to x. Hence there are exactly 2k+t such S-e edges.

Let E(S,B_X) denote the number of S-B_X edges. Degree summation on S gives
k^2 = 2e_G(S)+(2k+t)+E(S,B_X).
Using the upper bound on 2e_G(S),
E(S,B_X)
 >= k^2-k(k-3)-2k-t
 = k-t.

Therefore the number of genuine cross-half connectors is at least the deficit of x from being complete to S.
