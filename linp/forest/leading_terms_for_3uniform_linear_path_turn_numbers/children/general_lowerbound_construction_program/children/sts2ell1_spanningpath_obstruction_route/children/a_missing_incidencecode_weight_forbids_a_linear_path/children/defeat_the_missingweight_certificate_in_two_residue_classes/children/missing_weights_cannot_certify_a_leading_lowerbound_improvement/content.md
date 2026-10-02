# Ternary incidence-code missing weights cannot certify a leading lower-bound improvement

## Statement

Let H be a linear 3-graph and let C_3 be the F_3-linear span of its edge-incidence vectors. If H contains P_ell then C_3 contains a codeword of Hamming weight ell+2. Conversely, if Delta(H)>=floor((ell+2)/2) and ell>=2, then C_3 already contains a codeword of weight ell+2. Hence any H with |E(H)|/|V(H)|>ell/3 necessarily has such a codeword, so absence of weight ell+2 in a ternary incidence code cannot certify a P_ell-free construction beating the 1/3 coefficient.

## Body


For the path implication, let e_1,...,e_ell be a linear path and form the alternating sum
  1_{e_1}-1_{e_2}+1_{e_3}-... .
Every joint lies in two consecutive path edges with opposite coefficients and cancels. Every other path vertex lies in exactly one path edge and has coefficient plus or minus one. There are ell+2 such non-joint vertices, so the resulting ternary codeword has Hamming weight ell+2.

For the star implication, fix a vertex v of degree at least t and choose t incident edges. Linearity makes their other 2t vertices pairwise distinct. Give these t edge-incidence vectors arbitrary nonzero coefficients a_1,...,a_t in F_3. Every noncentral vertex survives, while the central coordinate is sum_i a_i. Thus the support has size 2t when the coefficient sum is zero and 2t+1 when it is nonzero.

For every t>=2 there are nonzero coefficients in F_3 with sum zero and also choices with nonzero sum: pair 1,2 to obtain zero sums, use 1,1,1 for an odd zero-sum block, and alter one coefficient when a nonzero total is desired. Let w=ell+2 and t=floor(w/2). If w is even choose sum zero; if w is odd choose nonzero sum. This gives a codeword of weight w.

Finally, |E(H)|/|V(H)|>ell/3 implies average vertex degree 3|E(H)|/|V(H)|>ell, hence Delta(H)>ell>=floor((ell+2)/2) for ell>=2. Therefore the ternary missing-weight criterion is incompatible with any leading-coefficient improvement above 1/3.
