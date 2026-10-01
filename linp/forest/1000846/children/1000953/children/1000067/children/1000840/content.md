# A missing incidence-code weight forbids a linear path

## Statement

Let H be a 3-uniform hypergraph and let C be the binary linear code spanned by the incidence vectors of E(H). If H contains a linear path P_ell^(3), then C contains a codeword of Hamming weight exactly ell+2. Consequently, if C has no codeword of weight ell+2, then H is P_ell^(3)-free.

## Body

Let e_1,...,e_ell be the edges of a linear path, and let J be its ell-1 joint vertices e_i intersect e_{i+1}. Sum the ell edge-incidence vectors over F_2. Every joint belongs to exactly two path edges and cancels. Every other path vertex belongs to exactly one path edge and survives. Since a 3-uniform linear path has 2ell+1 vertices, the surviving set has
 (2ell+1)-(ell-1)=ell+2
vertices. Hence the sum is a codeword of C of weight ell+2.

This strengthens the spanning-path incidence-code constraint: no ambient-order hypothesis is needed. It suggests a lower-bound construction program based on dense linear triple systems whose binary incidence codes have a prescribed missing weight. In particular, to beat the leading 1/3 benchmark one could seek systems on substantially more than 2ell vertices with edge density above ell/3 while keeping weight ell+2 out of the incidence code.
