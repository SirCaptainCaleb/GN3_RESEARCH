# Six-path parity certificate in Q3 and linear parity obstructions in Q4 and Q5

- Stable ID: note_nori_six_path_parity_certificate_q3_and_failure_q4_q5_20261016
- Author: unspecified; session provenance retained
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, parity-certificate, finite-enumeration, linear-algebra, obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11022_1
- Updated session: session_nori_r11022_1
- Disposition: none
- Successor: none

## Related references

- subsection:full_geodesic_color_profiles_span_the_entire_binary_space

## Research note

For a rooted full antipodal geodesic P=(x,pi) of Q_n, M_P(c) is the indicator, over F_2, that all edges of P have the same color in an antipodally odd binary edge coloring c. The n2^{n-2} antipodal unoriented-edge orbits supply independent Boolean coloring variables z_j. If the path uses n distinct orbit variables z_{j_1},...,z_{j_n} with antipodal signs a_1,...,a_n, then M_P=prod_{k=2}^n (1+z_{j_1}+z_{j_k}+a_1+a_k), with z_j^2=z_j.

THEOREM (six-path certificate in Q3). Let L={(0,012),(0,102),(1,021),(1,102),(2,012),(2,021)}, where vertices are low-bit-first integers and orders are direction lists. For every legal Q3 coloring, sum_{P in L} M_P(c)=1 in F_2. Independent exhaustive checking of all 64 legal Q3 colorings yields 48 with one monochromatic member of L and 16 with three. Polynomial expansion and bitwise reduction likewise produces the constant one.

THEOREM (no constant-one linear parity certificate from complete-path monochromaticity indicators in Q4 or Q5). For n=4 and n=5, the constant-one Boolean function of all legal coloring variables is not in the F_2-linear span of the indicators M_P, as P ranges over all rooted full antipodal geodesics. Expanding each M_P into the square-free monomial basis and applying binary Gaussian elimination gives the following fully determined integer data:
n=3: 6 orbit variables, 12 distinct indicator polynomials, rank 10, constant one in span.
n=4: 16 orbit variables, 96 distinct indicator polynomials, rank 95, constant one outside span.
n=5: 40 orbit variables, 960 distinct indicator polynomials, rank 960, constant one outside span.
There are 209 distinct monomials used in n=4 and 3081 in n=5. Reversal and antipodal path translation preserve indicator polynomials, reducing the set to n!2^{n-2} distinct polynomials. Reproducible source files were created at /mnt/data/nori_parity_cert.py and /mnt/data/nori_parity_span5.py. All polynomial arithmetic and elimination are over F_2, with no numerical tolerance. This proves the stated failure of fixed GF(2)-linear parity certificates for n=4 and n=5, not a failure of nonlinear or weighted existence arguments.

Research disposition: the positive Q3 six-path witness is a compact constructive certificate, whereas the Q4 and Q5 algebraic obstructions justify retiring a dimension-uniform proof attempt based solely on a fixed linear combination of complete-path monochromaticity indicators.
