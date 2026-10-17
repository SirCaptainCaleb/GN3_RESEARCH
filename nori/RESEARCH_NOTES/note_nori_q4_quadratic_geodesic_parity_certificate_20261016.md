# Quadratic parity certificate for antipodal geodesics in Q4

- Stable ID: note_nori_q4_quadratic_geodesic_parity_certificate_20261016
- Author: unspecified; session provenance retained
- Primary home: subsection:complementary_rank_geodesic_counting_and_parity_blindness
- Labels: NORI1, finite-certificate, Boolean-algebra, quadratic-parity, computational-proof
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11022_1
- Updated session: session_nori_r11022_1
- Disposition: none
- Successor: none

## Related references

- subsection:complementary_rank_geodesic_counting_and_parity_blindness

## Research note

**Theorem.** In Q4, let M_P(c) be the Boolean indicator that a rooted full antipodal geodesic P is monochromatic. There is a fixed collection C of 1276 unordered path pairs such that for every legal antipodally odd coloring c,
\[
\boxed{\sum_{(P,Q)\in C}M_P(c)M_Q(c)=1\bmod2.}
\]
No analogous constant-one identity exists as a linear combination of individual indicators M_P. Thus the minimum polynomial degree in these indicators needed for such a parity certificate is two.

**Finite algebra proof.** Legal colorings have 16 independent Boolean edge-orbit bits z_j. If a full path uses orbit labels j_1,...,j_4, with antipodal color signs a_1,...,a_4, the indicator polynomial over the Boolean ring z_j^2=z_j is
\[
M_P=\prod_{k=2}^{4}(1+z_{j_1}+z_{j_k}+a_1+a_k).
\]
Path reversal and antipodal translation preserve this polynomial; there are 96 distinct path indicators. Their coefficient vectors use 209 square-free monomials and have rank 95 over F2; constant one is outside this span. Among the 4656 unordered pairs including diagonal pairs, 4225 product polynomials are distinct, involve 7409 monomials of degree at most six, and span rank 2991. Appending the constant-one polynomial does not increase this rank. Binary elimination yields the announced 1276 pair products. Its Boolean polynomial sum reduces to one.

**Independent check.** The Python source nori_quadratic_certificate_q4.py and the serialized 1276-term certificate nori_quadratic_certificate_q4.json were created in the conversation workspace. The JSON SHA256 hash is 2ff831471a49374c15b4a8b6eef8f5aa6d325760d322a03d41d59533147bce98. The program evaluates the certificate from original edge-orbit assignments on all 65536 legal Q4 colorings and confirms it always equals one, in addition to the polynomial verification.

**Limits.** Products of path indicators restricted to the same root, adjacent-order swaps, or a one-bit shifted root with unchanged order do not span one. Under the full Q4 automorphism group, the 4656 path pairs form 40 orbits; their orbit-sum parity functions have rank 22 and also do not span one. Hence the certificate is not derived from these simple local or fully symmetric pair interactions. This is a new finite algebraic existence certificate in dimension four, not a dimension-uniform closure argument; further degree-by-degree extensions should be avoided without a new structural mechanism.
