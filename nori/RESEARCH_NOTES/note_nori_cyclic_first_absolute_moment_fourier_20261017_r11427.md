# Cyclic first-moment Fourier forcing and dimension-free signed graph bounds

- Stable ID: note_nori_cyclic_first_absolute_moment_fourier_20261017_r11427
- Author: session_nori_r11427_1
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, affine, cyclic-rotation, Fourier, first-absolute-moment, signed-graph, Hall, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11427_1
- Updated session: session_nori_r11427_1
- Disposition: none
- Successor: none

## Related references

- note:note_nori_cyclic_rotation_fourier_weight_20261017_r11421
- note:note_nori_affine_profile_fourier_inversion_graphs_20261017_r11401

## Research note

# First-absolute-moment cyclic Fourier bounds and an asymmetric affine Q7 forcing example

Let A in F2^(n*n) have zero diagonal and A*1=1, and let b_i(pi)=sum_(j preceding i)A_ij. Put K=ker A^T and mu(lambda)=E_pi (-1)^(lambda dot b(pi)). Every nonzero lambda in K has even Hamming weight t=2s. Put N=n-t and define
beta(n,t)=[1/(n*binomial(n,t))] sum_(u=0)^N |2u-N| binomial(u+s,s)binomial(N-u+s-1,s-1).

**Theorem 1 (cyclic first-moment bound).** For every nonzero lambda in K, |mu(lambda)|<=beta(n,|lambda|). This improves the previously proved second-moment bound sqrt((n-t)/(n(t+1))). The same beta bound holds for the signed inversion mean Z(H)=E_pi(-1)^inv_H(pi) of EVERY simple graph H on n vertices having t>0 odd-degree vertices.

*Proof.* Cyclically moving the first direction i of an order to the end changes the affine profile by (I+A)e_i, and its Fourier sign by (-1)^lambda_i. Averaging all n cyclic rotations gives mu=E_pi[sign(pi)S(pi)/n], where S(pi) is the sum of rotation signs relative to the starting order. Marked labels are the t directions with lambda_i=1. Their positions divide the N unmarked labels into t+1 gaps g_0,...,g_t. The marked positions' contributions to S cancel in alternating pairs because t is even; hence S=sum_(j=0)^t (-1)^j g_j. The t marked positions form a uniform subset of n positions, so their gaps form a uniform weak composition of N. Put U=sum of even-indexed gap lengths, so S=2U-N. There are s+1 even-indexed gaps and s odd-indexed gaps; the number of gap compositions with U=u is binomial(u+s,s)binomial(N-u+s-1,s-1). Thus |mu|<=E|S|/n equals beta(n,t). Cauchy-Schwarz gives the earlier second-moment bound. For a graph H, cyclic rotation flips its inversion sign precisely when the moved vertex has odd graph degree; repeat the same argument. QED.

**Theorem 2 (dimension-free inversion bound).** For every graph H with t=2s>0 odd-degree vertices,
|Z(H)|<=binomial(2s,s)/4^s.
This bound therefore also applies to all nontrivial affine quotient Fourier characters.

*Proof.* Choose independent uniform priorities X_v in the unit interval, inducing a uniform random vertex order. Translating all priorities by theta modulo one leaves their joint distribution unchanged. The inversion sign toggles whenever an odd-degree vertex crosses the circular cut. Averaging continuously over theta yields
|Z(H)|<=E|int_0^1 (-1)^(number of odd-degree vertices with X_v<theta)dtheta|.
The t marked points generate t+1 gaps with Dirichlet(1,...,1) lengths. The sum Y of the s+1 even gaps has Beta(s+1,s) law; the integral above is 2Y-1. Because |2Y-1| is symmetric under Y -> 1-Y, its Beta(s+1,s) mean agrees with the Beta(s,s) mean. Elementary integration with the substitution z=y(1-y) gives E|2Y-1|=binomial(2s,s)/4^s. QED.

**Theorem 3 (positive all-syndrome criterion).** If sum_(lambda in K except 0) beta(n,|lambda|)<1, then every coset of im A occurs as [b(pi)], every full profile of the legal affine coloring c_i(x)=a_i+(Ax)_i is attained globally, and its bipartite root-profile incidence graph admits a perfect matching by the previously proved affine transversal construction. The same conclusion follows if the sum of dimension-free binomial bounds is less than one. In particular when dim K=2 and every nonzero vector in K has weight >=6, 3*binomial(6,3)/4^3=15/16<1 guarantees Hall in ANY ambient dimension.

*Proof.* Fourier inversion on F2^n/im A gives P([b(pi)]=v)=2^(-dim K) sum_(lambda in K)(-1)^(lambda dot v)mu(lambda). The condition makes every such probability positive. Given any target w choose pi with [b(pi)]=[w-a] and solve Ax=w-a-b(pi). The prior affine quotient-transversal theorem constructs a bijection between roots and profiles. QED.

**Q7 automorphism-free certificate.** Take the legal 7x7 matrix A with binary integer row masks [22,25,112,19,14,28,22], with bit 0 representing direction 0. Its left kernel is {0,43,65,106}, nonzero weights 4,2,4. The old Cauchy certificate sums to 1.073490080... >1; the present certificate is beta(7,4)+beta(7,2)+beta(7,4)=9/35+3/7+9/35=33/35<1. Exhaustive enumeration of all 5040 orders confirms all four quotient syndromes occur with multiplicities 1388,964,1636,1052. Among all 5040 relabelings, only the identity preserves the quotient edge labels [A_ij e_i+A_ji e_j]. Thus neither the prior quotient-twin nor any full relabeling-group certificate applies. The new first-moment criterion proves full profile attainment and perfect matching.

**Independent audits and limits.** The standalone Python checker cyclic_rotation_first_moment_verify.py verifies the gap formula through n=11, enumerates every graph through n=6 to validate the inversion bound, and checks legality, kernel, four syndrome multiplicities, and trivial quotient-label automorphism group for the Q7 example. A separate search of 150000 random graphs at n=9 and n=10 found no violation of the stronger OPEN conjecture |Z(H)|<=1/(t+1). That conjecture is not used in this proof. The present theorem extends affine NORI1 forcing without resolving the unrestricted conjecture or even the full affine problem.
