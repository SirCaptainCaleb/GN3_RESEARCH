# Connected unique-intersection crossing components have constant rank-position difference

## Statement

Let P be a maximum p-edge path ending at v. For each vertex c in a finite set C, choose:
(1) an occurrence of c on P, with kappa_P(c) equal to the number of P-edges in the prefix ending at that occurrence;
(2) a maximum endpoint path P_c ending at c;
(3) a common vertex a_c of P and P_c such that the P-segment P[a_c,c] and the corresponding P_c-segment have the same number of edges and have no common internal vertex.

Define a graph G on C as follows. Join distinct c,d when their chosen P-intervals cross and the pair satisfies the hypotheses of 20606dbd4cd9 with P_c and P_d having exactly one common vertex.

Then on every connected component K of G there is a constant sigma_K such that
  phi(c)-kappa_P(c)=sigma_K
for every c in K.

Consequently, if all vertex ranks phi(c), c in K, lie in an integer interval [A,B], then
  |K| <= B-A+1.
In particular, no connected component contains two distinct vertices of the same vertex rank.

## Body

For every edge cd of G, 20606dbd4cd9 gives
  phi(c)-kappa_P(c)=phi(d)-kappa_P(d).
Equality propagates along paths in G, proving that phi(c)-kappa_P(c) is constant on each connected component K.

Now fix a component K and write the common value as sigma_K. Then
  phi(c)=kappa_P(c)+sigma_K
for every c in K.
The chosen occurrences of distinct vertices on the linear path P are distinct, so the integers kappa_P(c) are distinct. Hence the vertex ranks phi(c) are also distinct. If all of them belong to [A,B], there are at most B-A+1 possible integer values, giving
  |K|<=B-A+1.
The equal-rank assertion is the special case B=A.
