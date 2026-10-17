# Balanced Q7 defeats every three-character root-Walsh minor

- Stable ID: note_be85d81b3c8929b59cfbffef
- Author: unspecified; session provenance retained
- Primary home: subsection:integral_saturation_and_fourier_rigidity_of_geodesic_incidence
- Labels: NORI1, balanced-seven-cube, finite-counterexample, Fourier-principal-minors, integer-certificate
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11435_2
- Updated session: session_nori_r11435_2
- Disposition: none
- Successor: none

## Related references

- subsection:integral_saturation_and_fourier_rigidity_of_geodesic_incidence, exact version 5

## Research note

**Theorem (certified vertex-balanced Q7 with all small Fourier Gram minors positive).** A legal coloring is encoded by the following seven 32-bit hexadecimal tables, indexed by the direction i=0,...,6:
2b6ba977; f01a3f0d; 9b855c4e; 203e3b1a; 53f7b024; ef3ceb49; f2d0c593.
For vertex x and direction i, remove bit i from the seven-bit word x, obtaining the exterior six-bit integer y. When y<32, c_i(x) is bit y of table i; otherwise c_i(x) is one minus bit (63-y) of the table. This specifies an undirected legal antipodally odd edge coloring.

For every one of the 5040 direction orders pi and every family A of at most three root-Walsh characters, the shifted Gram matrix
K_pi(A)_(S,R)=hat G_pi(S triangle R)-3*delta_(S,R)
is positive definite, although monochromatic full geodesics exist. The following integer minima certify positive definiteness. Walsh coefficients are written with denominator 64; S and R range over distinct nonzero root-character labels:
min_pi [64*(hat G_pi(0)-3)] = 48;
min_pi,S [4096*((hat G_pi(0)-3)^2 - hat G_pi(S)^2)] = 1392;
min_pi,S<R [262144*det K_pi({0,S,R})] = 12800.
Every other family A of size three is an XOR-translation of {0,S,R}, preserving its Gram entries. Every vertex has red degree three or four. The projective cycle-grade histogram is
G=1:1052, G=3:10268, G=5:10868, G=7:852 (sum 23040).
In particular, the coloring has 1052 witness supports. Its mean G is 4, its variance is 299/180, and every direction-order conditional mean belongs to [15/4,17/4]. Thus the global second-moment sufficient condition (variance>3) and every direction-order first-moment sufficient condition (mean<3) are both inapplicable.

PROOF CERTIFICATE: C++17 standard-library source at https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/69a07bc09f28ee7bb53a610c4f4bf86c9a028b4a/nori/certificates/nori_q7_cubic_minor_obstruction.cpp . The verifier checks both legal-coloring equations, all vertex degrees, all 64 folded roots per direction order, the integer Walsh-Hadamard coefficients, every one of 1953 nontrivial three-character determinants per order, and the full projective grade histogram, asserting all stated minima and counts. This refutes the proposed universal sufficiency of three-character Fourier-minor negativity even in the balanced Q7 regime. It does not refute the correct cubic Fourier forcing implication, nor NORI1 itself.
