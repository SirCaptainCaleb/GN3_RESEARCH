# Balanced Q12 refutes existential two-sweep and sublinear mismatch hypotheses

- Stable ID: note_a16c9ca04fb509fefb7004e3
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: NORI1, counterexample, two-sweep, dimension-six, all-dimensional-products
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10003_3
- Updated session: session_nori_r10003_3
- Disposition: none
- Successor: none

## Related references

- note:note_6927ebc76b2a03c463c9e3ba

## Research note

**Theorem (existential reversible two-sweep conjecture is false).** There exists an antipodally odd binary coloring c of undirected edges of Q_6 such that for every root x and every direction order pi, U_pi^2(x) differs from the antipode bar x, although c admits a monochromatic full antipodal geodesic. Here U_i(x)=x xor 2^i when c_i(x)=0, and U_i(x)=x otherwise, and U_pi applies U_i in the order pi. Thus the existential strengthening in Proposition 4 of the existing paired-direction-involution manuscript is refuted; NORI1 itself is unaffected.

**Six compact truth tables.** Identify vertices with integers 0,...,63, with bit indices 0,...,5. For the edge in direction i at x, remove bit i from the 6-bit expansion to obtain rho_i(x)=(x mod 2^i)+2^i floor(x/2^(i+1)). Define c_i(x) to be bit rho_i(x) of the 32-bit table T_i (least significant bit has index zero):
T=(0xd7aaaa14, 0xeb555528, 0x4f0f0f0d, 0xb0f0f0f2, 0xd99d4664, 0xd99d4664).
The rule ignores its own bit by construction. Direct inspection of the 32-bit tables shows T_i[rho_i(bar x)]=1-T_i[rho_i(x)], establishing antipodal oddness for all i and x. The same property was independently checked over all 384 pairs (i,x).

**Exhaustive certificate.** For each of the 720 permutations pi and 64 roots x, put v=x and perform two passes: for each i in pi, replace v by v xor 2^i if bit rho_i(v) of T_i equals zero. Count d=popcount(v xor (x xor 63)). The histogram of d over all 46080 tests is
d=0:0; d=1:3120; d=2:10080; d=3:13968; d=4:12864; d=5:6048; d=6:0.
The totals sum to 46080. Thus no reversible two-sweep witness exists, with minimum deficiency one. Two independent enumerations (one using an in-memory coloring matrix and one calculating the table bits from scratch in pure Python) agree on the zero witness count and the full histogram.

**Positive NORI1 witness.** At x=2, traverse directions (1,5,3,2,0,4); direct table lookup gives edge colors (0,0,0,0,0,0), so this is a monochromatic antipodal geodesic. The coloring has twelve roots supporting color-zero full geodesics; its color-one root set is the same by antipodal translation and undirected reversal.

**Consequences.** The same-pi sufficient condition U_pi^2(x)=bar x, with pi and x both freely selected, is strictly stronger than the grand conjecture and is false. For any h>=1, the independent Cartesian power c^box h has a monochromatic full antipodal geodesic but no reversible two-sweep witnesses: each factor of a hypothetical witness would be a witness in c. In dimensions 6h this gives good antipodally odd colorings with Z(c^box h)=0. In particular witness density zero is compatible with NORI1 itself, and the previously proposed universal sublinear opposed-sweep mismatch bound cannot hold for arbitrary legal colorings. Whether analogous balanced examples exist is a separate question; this six-bit coloring is not vertex-balanced (its zero-degree distribution is 16 vertices of degree 1, 6 of degree 2, 20 of degree 3, 6 of degree 4, and 16 of degree 5).

**Independent verification pseudocode.** For every permutation pi of range(6), and root x in range(64), initialize v=x; repeat twice the updates: for i in pi, flip bit i of v when the direction-i edge at v has color zero; test v==(x xor 63). This produces zero witnesses.

**Balanced counterexample.** Let c be the legal Q6 coloring above, and define its paired lift C on Q12 by C_i(x,y)=c_i(x), C_(6+i)(x,y)=1-c_i(x) for i=0,...,5. This coloring is vertex-balanced, antipodally odd, and undirected. Every red sweep of C projects to the red sweep of c in the induced order of the first six directions. Therefore any two-sweep antipodal witness for C would project to one for c, which does not exist. Nevertheless a zero full geodesic of C begins at integer root 2 and uses directions (8,10,11,1,5,3,2,0,4,6,7,9), ending at its antipode 4093.

**Linear mismatch.** In the manuscript, Delta(a)=min_(x,pi) d_H(U_pi(x),U_pi^(-1)(bar x)). Its vanishing is equivalent to an antipodal two-sweep witness. Hence Delta(C)>=1. By established Cartesian additivity Delta(C^box r)=r Delta(C)>=r for balanced good colorings in dimension 12r. This disproves the proposed uniform o(n) mismatch upper bound even over vertex-balanced colorings already admitting monochromatic full geodesics. The earlier conditional theorem remains logically sound, while its antecedent is false. The existential two-sweep strengthening is false even under balance.
