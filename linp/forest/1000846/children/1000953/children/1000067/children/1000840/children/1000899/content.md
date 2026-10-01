# High-degree stars defeat the missing-weight certificate in two residue classes

## Statement

Let H be a linear 3-graph and C its binary incidence code. If ell is congruent to 2 mod 4 and Delta(H)>=(ell+2)/2, or if ell is congruent to 1 mod 4 and Delta(H)>=(ell+1)/2, then C contains a codeword of weight ell+2. Consequently no family with |E(H)|/|V(H)|>ell/3 can be certified P_ell-free solely by absence of weight ell+2 in its incidence code for ell congruent to 1 or 2 mod 4.

## Body


Fix a vertex v and choose t distinct incident edges. Since H is linear, these edges intersect pairwise exactly in v and their remaining 2t vertices are all distinct. Summing their incidence vectors over F_2, the vertex v survives exactly when t is odd. Thus the resulting codeword has weight 2t when t is even and 2t+1 when t is odd.

If ell=4a+2, choose t=(ell+2)/2=2a+2, which is even. The resulting codeword has weight 2t=ell+2.

If ell=4a+1, choose t=(ell+1)/2=2a+1, which is odd. The resulting codeword has weight 2t+1=ell+2.

Finally, if |E(H)|/|V(H)|>ell/3 then the average vertex degree is 3|E(H)|/|V(H)|>ell, so Delta(H)>ell. In either residue class this is more than enough to choose the required t incident edges. Hence the sufficient criterion “the incidence code has no word of weight ell+2” cannot establish any leading-coefficient improvement above 1/3 in these residue classes.
