# Clean entrance-only ascending terminal chords satisfy three-halves packing

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge linear path ending at v, with h=g_p. Let X(P,v) be the family of ascending nonspecial edges e={x,v,u}, e!=h, such that e meets V(P)\V(h) in exactly one vertex and that vertex is its unique entrance x.

Let alpha_p be the maximum weight of an independent set in the distance-two graph on indices {1,...,p-1}, with weight 2 at index 1 and weight 1 elsewhere; for p=1 this graph is empty and alpha_1=0. Then
  |X(P,v)| <= p-2 + alpha_p <= floor(3p/2)
for p>=2, while X(P,v)=emptyset for p=1.

For p>=2,
  alpha_p =
    p/2+1       if p≡0 mod4,
    (p+1)/2     if p≡1 mod4,
    p/2+1       if p≡2 mod4,
    (p+3)/2     if p≡3 mod4.
In particular |X(P,v)|<=floor(3p/2), with a one-unit stronger bound when p is even.

## Body

If p=1, every rank-one edge is special, so there is no ascending nonspecial edge terminal at v. Thus X(P,v)=emptyset. The claimed bound holds with alpha_1=0. Assume henceforth p>=2.

Every entrance x of an edge in X(P,v) lies in V(P)\V(h). Distinct edges in X(P,v) have distinct entrances, because two edges through v sharing x would violate linearity.

There are p-2 path-joint vertices in V(P)\V(h), namely g_i∩g_{i+1} for 1<=i<=p-2. Hence at most p-2 members of X(P,v) have a joint entrance.

For private entrances, index an edge by the path edge g_j containing its entrance privately. Among g_1,...,g_{p-1}, the first edge g_1 has two private vertices and every g_j with 2<=j<=p-1 has one. Thus index 1 has capacity two and all other indices capacity one.

By c265aa8ded39, if private clean entrance contacts occur at indices j and j+2, they are incompatible. Hence the occupied private indices form an independent set in the graph on {1,...,p-1} whose edges join indices differing by two, with weight/capacity two at index 1 and one elsewhere.

This graph is the disjoint union of the odd-index path and even-index path. On the even-index path all weights are one, so the maximum weight is the ceiling of half its number of vertices. On the odd-index path the first vertex has weight two and all later vertices weight one; an optimum contains the first vertex, and its maximum weight is one more than the ceiling of half the number of odd indices. Evaluating for p>=2 by p modulo four gives the displayed alpha_p.

Adding the at most p-2 joint entrances gives |X(P,v)|<=p-2+alpha_p. In each residue class this is at most floor(3p/2); when p is even it is at most 3p/2-1.
