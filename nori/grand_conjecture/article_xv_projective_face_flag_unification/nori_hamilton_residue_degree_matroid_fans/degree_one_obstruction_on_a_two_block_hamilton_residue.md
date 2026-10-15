# Degree-one obstruction on a two-block Hamilton residue

### Degree-one obstruction on a Hamilton two-block cell

**Theorem.** A reversal-odd coloring of triples on six vertices admits a four-dimensional dual Coxeter cell D all of whose 36 Hamilton orders have two or more switches, while the extreme-switch bivector labels have a piecewise-linear boundary realization of nonzero degree in S^3.

*Proof.* Partition the six symbols into triples A and B. Each flag in the two-block cell D has order (a,b,c,d,e,f) with abc permuting A and def permuting B. Choose any reversal-odd bit functions t(abc), s(def) on permutations of these respective triples. Prescribe consecutive colors t,1-t,1-s,s. This defines legal triple colors: the second bit uses b(b,c,d) with a determined by b,c, and the third uses b(c,d,e) with f determined by d,e. Their reverses do not conflict with the prescribed types. Every word switches at positions 1 and 3.

Put T=sum_{a in A} e_a - 1/2 1, xi_c=e_c-(sum_A e)/3, eta_d=e_d-(sum_B e)/3. Centered prefix vectors satisfy Z_2=(2/3)T-xi_c and Z_4=(2/3)T+eta_d. Since ||T||^2=3/2, contracting the bivector Z_2 wedge Z_4 by T gives xi_c+eta_d in the four-dimensional orthogonal sum W_A+W_B. The cell D is the product of two hexagons. On their boundary vertices, the last A symbol and first B symbol each run around the three corresponding centered triangle vertices once, with repetitions. Cone both hexagon boundary maps to zero at their centers. Their product agrees with all 36 contracted flag labels, is nowhere zero on the boundary of D, and has an isolated interior zero of Brouwer degree plus or minus one. Normalizing the boundary map gives degree plus or minus one in S^3. QED.

The individual-cell degree depends on lower-cell filling choices. This refutes a proposed local automatic degree-zero mechanism; global compatibility between two-block residues remains open.
