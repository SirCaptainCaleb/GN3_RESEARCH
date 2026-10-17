# Field-uniform obstruction to fixed geodesic calibrations and Pfaffian parity

- Stable ID: note_nori_pfaffian_mod8_does_not_determine_geodesic_parity_20261016
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: pfaffian, counterexample, finite-certificate, geodesic-parity, linear-incidence, characteristic-two, dimension-uniform, fixed-weight-calibration, all-fields, D8-symmetry, odd-characteristic, rooted-geodesics, dimension-three-sharpness
- Lifecycle: active
- Epistemic status: proved
- Current version: 4
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10917_4
- Updated session: session_nori_r11254_5
- Disposition: none
- Successor: none

## Related references

- subsection:paired_direction_involutions_and_geodesic_endpoint_matchings

## Research note

**Finite obstruction to a Pfaffian parity closure.** In the antipodally odd edge-coloring model on \(Q_5\), identify the 40 antipodal edge orbits by scanning undirected edges \((u,u\oplus2^i)\), \(u<u\oplus2^i\), in ascending \(u\) and then ascending direction \(i\); introduce an orbit on its first appearance. The bit at this orbit is one when its first encountered edge is red, with the antipodal partner blue, and zero otherwise. Consider the masks
\[
a=\texttt{0xba22266a0b},\qquad b=\texttt{0x8c690383a8}.
\]
Let \(N_R(c)\) count unoriented red antipodal full geodesics. Construct the \(16\times16\) skew matrix \(M_c\) indexed by even-parity vertices of \(Q_5\) in ascending integer order, setting \(M_c(u,v)=+1\) if \(u,\bar v\) form a red edge, \(-1\) if blue, and zero otherwise. Then direct finite enumeration gives
\[
\operatorname{Pf}(M_a)=3,\quad N_R(a)=60;\qquad
\operatorname{Pf}(M_b)=11,\quad N_R(b)=53.
\]
The Pfaffians may be verified by skew Gaussian elimination, and the geodesic counts by enumerating \(16\cdot5!=1920\) paths with initial root in \(\{0,\ldots,15\}\) and each direction used once. Hence the two Pfaffians are both congruent to \(3\bmod8\), while the red-geodesic counts have opposite parity. In particular \(\operatorname{Pf}(M)^2\bmod16\) does not determine red-geodesic parity, even within legal odd-dimensional colorings. This limits direct use of Pfaffian congruence as a geodesic counting invariant; it does not contradict the odd determinant and matching-cofactor theorems.

## Fixed-weight geodesic incidence has no nonzero constant calibration

Let \(\mathcal G_n\) be the set of rooted, ordered full antipodal geodesics in \(Q_n\). For a legal antipodally odd coloring \(c\) and \(P\in\mathcal G_n\), write \(I_c(P)=1\) when every edge of \(P\) has color zero, and \(I_c(P)=0\) otherwise. A fixed-weight linear calibration over a field \(K\) would be weights \(w_P\in K\), independent of \(c\), and a scalar \(\kappa\ne0\) such that \(\sum_P w_P I_c(P)=\kappa\) for every legal \(c\).

**Theorem (characteristic-zero obstruction).** No such calibration exists over a characteristic-zero field in any dimension \(n\ge3\).

**Proof.** The hyperoctahedral cube-automorphism group acts transitively on \(\mathcal G_n\) and preserves the legal coloring class. If a constant calibration existed, transform its coefficients by every cube automorphism and average them in \(K\). This yields another calibration with the same nonzero constant and a common coefficient \(\lambda\) on every path. Hence \(\kappa=\lambda N_R(c)\) for every legal \(c\), where \(N_R(c)=\sum_P I_c(P)\) is the rooted red full-geodesic count.

Two explicit legal colorings give different \(N_R\). First, with indices modulo \(n\), take \(c_i(x)=x_{i+1}\). Each direction order admits precisely one starting root for which its full path is red, because the root bits are forced by the precedence relations. Hence \(N_R(c)=n!\). Second, take \(d_0(x)=x_1\) and \(d_i(x)=x_0\) for \(1\le i<n\). An all-red full path must place direction zero first or last: all other direction colors read the same bit \(x_0\) before or after its flip. For either type of order, two root bits are forced and the remaining \(n-2\) root bits are free. Thus \(N_R(d)=2^{n-1}(n-1)!\). Since \(n\ne2^{n-1}\) for \(n\ge3\), the counts differ. This contradicts \(\kappa\ne0\). QED.

**Theorem (characteristic-two obstruction with finite base certificate).** For every \(n\ge4\), over every field of characteristic two there is no fixed-weight linear calibration with \(\kappa\ne0\). This remains true if terms corresponding to color-one geodesics are also allowed.

**Finite Q4 certificate.** Encode a legal coloring of \(Q_4\) by sixteen bits, one per antipodal orbit of undirected edges. List the undirected edges by increasing smaller endpoint \(u\in\{0,\ldots,15\}\) and then increasing direction \(i\in\{0,1,2,3\}\); first encounter of an orbit assigns its bit index. A mask bit gives the color on that first edge, and its antipodal partner has the opposite color. Let \(\mathcal M\) be the following seventeen masks (hexadecimal):
\[
0,\,3,\,4,\,11,\,14,\,20,\,22,\,82,\,84,\,90,\,a0,\,100,\,101,\,110,\,400,\,401,\,402.
\tag{P1}
\]
They satisfy
\[
\boxed{\ \sum_{m\in\mathcal M}I_{c^{(m)}}(P)=0\pmod2
\quad\text{for every }P\in\mathcal G_4.\ }
\tag{P2}
\]
A finite verifier enumerates the sixteen vertex roots and all twenty-four direction orders. For each of the resulting 384 paths, traverse each edge and test whether the mask bit at the corresponding antipodal edge orbit, toggled when the edge is the opposite representative, equals zero. The number of successful tests among (P1) is even for each path. The sixteen orbit representatives, in the indicated scanning order, have pairs \((u,i)\):
\[
(0,0),(0,1),(0,2),(0,3),
(1,1),(1,2),(1,3),
(2,0),(2,2),(2,3),
(3,2),(3,3),
(4,0),(4,1),(5,1),(6,0).
\tag{P3}
\]
Equations (P1)--(P3) permit independent verification using only finite Boolean operations. Each mask specifies a legal antipodally odd coloring.

**Lifting proof.** For \(n>4\), extend each \(c^{(m)}\) to a legal coloring \(C^{(m)}\) on \(Q_n\) by retaining its rules in the first four directions and setting \(C^{(m)}_j(x)=x_0\) for every \(j\ge4\). For any full geodesic \(P\) in \(Q_n\), the projection onto the first four directions is a full geodesic \(P_4\), and the condition that all new-direction edges of \(P\) are red is independent of \(m\). Consequently \(I_{C^{(m)}}(P)=\eta(P)I_{c^{(m)}}(P_4)\), where \(\eta(P)\in\{0,1\}\) is independent of \(m\). Summing over the seventeen masks gives zero by (P2). For \(n=4\), take \(C^{(m)}=c^{(m)}\).

Were a fixed-weight identity \(\sum_P w_PI_c(P)=\kappa\ne0\) valid in dimension \(n\), summing it over \(C^{(m)}\) would give \(17\kappa=\kappa\) in characteristic two, while exchanging the two finite sums and applying the lifted (P2) gives zero. Contradiction.

Finally, the antipodal translate of a color-zero path is a color-one path, giving \(I^{\mathrm{blue}}_c(P)=I_c(\tau P)\). Any fixed-weight sum involving both colors is therefore another fixed-weight sum of color-zero indicators, and is excluded as well. QED.

**Scope.** These results exclude all coloring-independent linear identities equating a signed or finite-field-weighted sum of monochromatic full-path indicators to a nonzero constant. They do not restrict coloring-dependent weights, nonlinear combinations of path indicators, inequalities, or equivariant chain obstructions involving other geometric objects. The characteristic-two obstruction follows from a finite Q4 certificate and a dimension-uniform projection argument, not from an exhaustive search in higher dimensions.


## Field-uniform obstruction to fixed geodesic calibrations

**Theorem.** Let n>=4, let K be any field, and let G_n denote the set of rooted ordered full antipodal geodesics of Q_n. For every legal antipodally odd edge coloring c write I_c(P)=1 if P is red and I_c(P)=0 otherwise. There are no coefficients w_P in K, independent of c, and no nonzero scalar kappa in K such that
sum_(P in G_n) w_P I_c(P) = kappa
for all legal c. The conclusion also holds if fixed-weight indicators of blue full geodesics are allowed.

**Odd-characteristic certificate in Q4.** Identify the sixteen antipodal orbits of unoriented Q4 edges by scanning undirected edges (u,u+e_i) with u_i=0, first by ascending u and then ascending dimension i. Each orbit receives its index upon first encounter. A mask determines the colors on these first edges, with the antipodal partners given the opposite colors.

Consider the two masks 0x0000 and 0x0001, giving base colorings c^(0),c^(1). Let D8 <= S4 be generated by the four-cycle (0 1 2 3) and the reflection (1 3), acting by relabeling dimensions. Put H = F_2^4 semidirect D8, a subgroup of the cube automorphism group of order 128. The 384 rooted ordered full geodesics form three free H-orbits of size 128; their direction-order sets are the three D8-orbits on S4. Representatives of these direction-order classes may be taken as (0,1,2,3), (0,1,3,2), (0,2,1,3).

The following table gives the numbers of red rooted full geodesics of the two base colorings in each H-orbit:
representative | 0x0000 | 0x0001
(0,1,2,3)       | 16     | 12
(0,1,3,2)       | 16     | 12
(0,2,1,3)       | 16     | 12.

This finite calculation requires examining sixteen roots and eight direction orders per row. To reproduce it, for each mask and root x, let the edge color in dimension i be its orbit mask bit plus the indicator that the lower endpoint of the edge is the later of the two antipodal orbit representatives. Iterate over the 128 paths in each row. For mask 0x0000 the rules simplify to c_0=c_1=c_2=x_3 and c_3=x_2, and each row has four admissible permutations with four red roots apiece. For mask 0x0001 only the antipodal pair of 0-edges joining 0000 to 0001 and 1110 to 1111 changes color. A direct enumeration of the eight permutations in each row gives respectively four, zero, zero, zero, two, zero, two, four admissible red roots in the first row; the other two rows have the same multiset of root counts, hence twelve in every row.

For each rooted path P of Q4, transitivity and freeness of H on its orbit imply
sum_(h in H) I_(h*c^(0))(P)=16,
sum_(h in H) I_(h*c^(1))(P)=12.
Here h*c denotes the pulled-back coloring under the cube automorphism h.

**Lifting to arbitrary n>=4.** For each h and a in {0,1}, extend h*c^(a) to Q_n by keeping its old four direction rules, independently of all new vertex bits, and prescribing the edge colors in every added dimension j>=4 by x_0. Every extension is legal and antipodally odd. For a rooted full Q_n path P, project its direction word onto the first four dimensions to obtain a rooted full Q4 path P_4. The colors of the added-direction edges depend only on P, so there is an indicator eta(P), independent of h and a, such that
I_(C_h^(a))(P)=eta(P) I_(h*c^(a))(P_4).
Consequently
sum_(h in H) I_(C_h^(0))(P)=16 eta(P),
sum_(h in H) I_(C_h^(1))(P)=12 eta(P).

Assume a constant calibration exists. Summing the asserted calibration identity over each of these two H-ensembles gives
128 kappa = 16 T = 12 T,
where T=sum_(P in G_n) w_P eta(P).
Thus 4T=0. In any field of odd characteristic, 4 and 128 are invertible, implying T=0 and kappa=0, a contradiction. This proves the theorem over all fields of odd characteristic, including characteristic zero.

**Characteristic two.** The preceding finite Q4 certificate in this same research note consists of seventeen legal mask colorings with even total red incidence at every rooted Q4 full geodesic. Extend each by the added-direction rules x_0 as above. The sum of their red indicators remains zero at every full path of Q_n. Summing a hypothetical constant calibration over the seventeen extensions gives 17 kappa=0. In any field of characteristic two this is kappa=0, a contradiction.

Finally, for each rooted path (x,pi), the rooted path (x,rev(pi)) traverses the antipodal images of its edges in reverse order. Therefore the color-one indicator of (x,pi) equals the color-zero indicator of (x,rev(pi)). A fixed-weight expression involving both monochromatic colors reduces to one involving red indicators, already excluded.

**Scope.** Every field is covered, with no hypothesis on the Boolean degree or influence graph of c. The obstruction excludes coloring-independent linear identities with a nonzero constant, while allowing nonlinear invariants, coloring-dependent coefficients, and chain-level constructions with auxiliary data. The Q4 certificate is dimension-uniform through the projection argument; finite verification is needed only for the two displayed three-row tables and the earlier seventeen-mask parity relation.


## The characteristic-two dimension threshold

The restriction n>=4 in the characteristic-two theorem is necessary. In Q3, identify directions as 0,1,2 and roots as three-bit integers. Let F be the following twelve rooted full paths, listed as (root, direction word):
(0,012), (0,102), (0,201), (0,210),
(1,021), (1,102), (1,120), (1,201),
(2,012), (2,021), (2,120), (2,210).
Then every legal antipodally odd coloring c of Q3 satisfies
sum_(P in F) I_c(P)=1 mod 2.

**Finite verification.** Q3 has six antipodal edge orbits and therefore 2^6=64 legal colorings. Encode one bit per orbit using the lower-endpoint scanning convention established above. For each mask, evaluate the colors along the twelve listed paths. Among the 64 masks, 48 yield one red path in F and 16 yield three red paths in F; in every case the sum is odd. This is a complete finite proof, independently checkable by enumerating six-bit masks and the twelve paths.

Thus the field-uniform non-calibration theorem starts at n=4, and its characteristic-two branch is sharp in dimension. The Q3 identity is only a low-dimensional certificate and does not extend via the padding projection in the manner of the Q4 obstruction.
