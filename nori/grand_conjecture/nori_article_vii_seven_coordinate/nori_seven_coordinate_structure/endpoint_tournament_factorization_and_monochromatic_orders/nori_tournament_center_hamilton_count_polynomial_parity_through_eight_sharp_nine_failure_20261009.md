# Center-marked tournament Hamiltonian-path polynomial is constant through eight and varies at nine

# A mod-two spanning-path invariant for center-marked tournaments, sharp through eight vertices

Let t(a,c)+t(c,a)=1 be any tournament orientation and s(b) an arbitrary vertex marking. Put h(a,b,c)=t(a,c)+s(b) in F_2, and let N_n(t,s) be the number of permutations p with h(p_i,p_(i+1),p_(i+2))=0 for every 1<=i<=n-2.

**Finite polynomial identity (exact symbolic verification).** For each n=3,4,5,6,7,8, the polynomial over F_2 in independent orientation variables T_ab (a<b) and marking variables S_b,
  P_n = sum_(p in S_n) product_(i=1)^(n-2) (1 + t(p_i,p_(i+2)) + S_(p_(i+1))),
with t(a,c)=T_ac if a<c and t(a,c)=1+T_ca if a>c, is IDENTICALLY equal to binom(n,ceil(n/2)) mod 2. This is a formal polynomial identity, stronger than equality on Boolean inputs. In particular P_7=1; thus for EVERY tournament and EVERY marking, N_7(t,s) is odd. This supplies a parity existence certificate for seven-direction center-marked tournament triples without SAT.

**Exact reproducible symbolic calculation.** Index the C(n,2)+n independent variables by bits in a machine integer. Represent a squarefree F_2 monomial by its variable-bitmask and a polynomial by the set of monomials with odd coefficient. For each permutation p, expand the n-2 linear factors: factor at (a,b,c) offers the monomials {T_(min(a,c),max(a,c)), S_b}, plus the constant monomial 1 iff a<c. Toggle the resulting product monomial in the global set. Since the factors of any one path involve distinct tournament edges and distinct center vertices, multiplying their monomials is simply bitwise union. After all n! permutations, the surviving polynomial monomial sets have sizes 1,0,0,0,1,0 for n=3..8; the surviving monomial is the constant for n=3 and 7. The expansion sizes in total are respectively 15,150,1850,27380,472675,9325750. This uses only elementary finite arithmetic over F_2 and can be independently reproduced from the stated expansion rule.

**Sharp limit of the universal parity claim.** At n=9 the parity depends on s. Take the transitive tournament t(a,c)=1 iff a>c, with vertices 0,...,8. For s=0, the odd and even position chains are increasing, yielding exactly C(9,5)=126 color-0 Hamilton orders, parity0. When s(1)=1 and all other s=0, an exact subset/last-two DP gives 469 such orders, parity1. Thus the formal polynomial P_9 is NOT constant. The parity method through n=8 does not imply a universal all-n parity forcing theorem.

**DP for independent count.** Initialize D[{a,b},a,b]=1 for all ordered pairs a≠b. For each state (A,a,b), each c outside A contributes D[A,a,b] to D[A+c,b,c] iff t(a,c)=s(b). Summing D[[n],a,b] over distinct a,b gives N_n(t,s), proving the displayed integer counts with elementary finite arithmetic. The same DP checks the n<=8 parity identities numerically for arbitrary t,s; the polynomial expansion proves them formally.

**Consequence and frontier.** The seven-vertex identity strengthens the finite tournament-center SAT closure: it certifies an odd number of monochromatic color-0 orders. Seek a path-exchange or algebraic identity that preserves nonvanishing of N_n without requiring its parity to be fixed. Its failure at nine explains why a direct extension of the parity invariant cannot close the all-dimensional tournament-center problem, let alone general NORI.
