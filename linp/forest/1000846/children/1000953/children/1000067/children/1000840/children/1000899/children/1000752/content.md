# Density above ell/3 forces the path weight in the binary incidence code

## Statement

Let ell>=3 and let H be a finite linear 3-graph with m edges and n vertices. If m/n>ell/3, then the binary linear code spanned by the edge-incidence vectors of H contains a codeword of Hamming weight exactly ell+2. Consequently, the sufficient certificate 'the binary incidence code has no word of weight ell+2' can never certify a P_ell-free construction whose edge density exceeds ell/3.

## Body

Proof. Pass to the >ell/3-core H0. It is nonempty, satisfies |E(H0)|/|V(H0)|>=m/n>ell/3, and has minimum degree greater than ell/3. Hence its average degree is greater than ell, so some vertex v has degree d>=ell+1. The d edges through v form a linear star: outside v their 2d vertices are pairwise distinct. The binary sum of k star edges therefore has weight 2k when k is even and 2k+1 when k is odd.

Put w=ell+2.

If ell≡2 (mod 4), take k=w/2. Then k is even and the sum of any k star edges has weight w.

If ell≡1 (mod 4), take k=(w-1)/2=(ell+1)/2. Then k is odd and the sum of any k star edges has weight w.

Suppose ell≡0 (mod 4). Since m/n>ell/3>=4/3, H0 is not a star through v, so choose an edge f not containing v. By linearity, f meets at most three edges of the v-star. Put k=(ell-2)/2, which is odd. Since d>=ell+1, we have d-3>=k, so choose k star edges disjoint from f. Their sum has weight 2k+1=ell-1, and adding f, which is disjoint from its support, gives weight ell+2.

Finally suppose ell≡3 (mod 4). Put k=(ell+1)/2, which is even. Choose a star edge e={v,a,b}. Because the >ell/3-core has minimum degree at least 2, there is an edge f≠e through a. By linearity f does not contain v or b, and besides e it meets at most two further v-star edges. Since d-3>=k-1, choose k-1 additional v-star edges disjoint from f. Together with e these k star edges have binary sum of weight 2k; the edge f meets that support exactly in a, so adding f changes the weight by +1. The resulting codeword has weight 2k+1=ell+2.

In every residue class the binary incidence code of H0, hence also that of H, contains a word of weight ell+2.
