# Four-direction seam forcing and mutual-reader confinement of near-full red witnesses

- Stable ID: note_nori_two_pair_seam_forcing_r11510
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, paired-flat, dimension-uniform, seam-completion, mutual-readers, critical-interface, witness-incidence, codimension-four, finite-certificate, positive-forcing, temporal-word-factorization
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11510_3
- Updated session: session_nori_r11510_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_double_square_temporal_word_transport_r11510

## Research note

# Two-pair seam completion with mutual-reader exceptions

Let N=2m>=6 and c be any paired-flat antipodally odd coloring. Each prescribed direction pair P={i,i'} has red/blue gate f_P independent of both bits in P, with colors f_P and 1+f_P, and f_P(bar x)=1+f_P(x).

**Theorem (four-direction seam forcing).** Fix two pairs P,Q, let J be the remaining N-4 directions, and suppose a zero full J-geodesic H goes from (u,y) to (u,bar y), freezing the four P,Q bits at u. Rename them 0,1 in P and 2,3 in Q. At J-root y write the two gates a(x2,x3), b(x0,x1). Then H extends to an all-zero full antipodal geodesic unless a=x_r+alpha, r in {2,3}, b=x_s+beta, s in {0,1}, and
  a(u)=1_{s=0}, b(u)=1_{r=2}. (SC1)
If a,b are such mutual unary readers, the exceptional seam positions form a four-vertex affine subcube.

**Four-bit proof.** Let A be the ordinary Q4 coloring with rules a,1+a,b,1+b. The colors of the four missing directions after H are A^+_i(v)=1+A_i(bar v), by antipodal oddness. A completion is an order pi of 0,1,2,3 and a cut k in {0,...,4}; start at u xor the first k directions of pi, use A-red edges for the first k steps, traverse H, and use A^+-red edges for the last 4-k steps. Translate u to 0000, write a,b as four-bit truth-table integers. The following 24 pairs (pi,k) cover 252 of the 256 table pairs:
(0213,0),(0213,4),(0231,2),
(0312,0),(0312,2),(0312,3),
(1203,1),(1203,3),(1230,2),
(1302,1),(1302,2),(1302,3),
(2013,2),(2031,1),(2031,3),
(2103,2),(2130,0),(2130,4),
(3021,1),(3021,2),(3021,4),
(3120,0),(3120,2),(3120,4).
Each is verified by evaluating the four traversed edge bits with A before the cut and A^+ afterward. The four uncovered table pairs are (3,10),(5,5),(10,3),(12,12), precisely (SC1) at u=0. Translation gives the displayed criterion for any u. Conversely, under (SC1), A^+=A because both gates are complement-odd on Q4. At u, each pair's zero edge toggles the bit not read by the other gate. Both reader bits stay fixed, hence the entire red component of u is a four-cycle using those two unread directions. No red full antipodal Q4 path contains u. Thus the four exceptions cannot be completed. This proves both directions of the local lemma. The insertion described above lifts the lemma to the original Q_N. QED.

**Global support confinement.** In a hypothetical bad paired-flat c, fix any P,Q and J-root y. Let U_y be the set of all u in F_2^4 supporting an all-zero full J-geodesic rooted at (u,y), allowing any order. If U_y is nonempty, the two outer gate restrictions at y must be mutual unary readers, and U_y lies in the four-vertex exceptional affine subcube (SC1). Thus |U_y|<=4. Either a single J-witness at a non-unary interface, or five J-witnesses from distinct u at a common J-root y, forces a full red antipodal geodesic. The hypotheses are tested within one arbitrary paired-flat coloring; they impose no global Boolean degree or feedback restriction.

**Endpoint-pair factorization.** Fix one pair P={i,j}, and the four faces F_u with its bits frozen to u. Every rooted full face path with temporal color word w has two full-path completions with the pair directions at its first and last steps in opposite orders, of words 0w0 and 1w1. For the (i,H,j) completion the endpoint colors are f_P(y) and 1+f_P(bar y)=f_P(y); swapping i,j complements both. Therefore the temporal blue-count polynomial for all rooted full paths whose first and last directions are the members of P is
 F_{c;P}^{end}(z)=(1+z^2) sum_{u in F_2^2} F_{c|F_u}(z).
This full temporal-word multiset is invariant under arbitrary changes to the odd pair gate f_P, with other pair gates fixed. The identity holds for all paired-flat legal Q_N, N>=4.

**Scope and verification.** The four-bit calculation is an all-dimensional conditional forcing mechanism, with a finite Boolean certificate. It does not guarantee a red J-geodesic in every coloring, so NORI1 remains open. The self-contained checker nori_two_pair_seam_certificate.py verified all 4096 (a,b,u) instances against all 120 order/cut possibilities, checked the 24-route certificate, and verified 20 nonlinear Q8 lifts. Full proof nori_two_pair_seam_forcing.md.
