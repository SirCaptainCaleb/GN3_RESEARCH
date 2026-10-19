# Quadratic geodesic incidence: Q4 identity and Q5 characteristic-101 obstruction

- Stable ID: note_nori_quadratic_geodesic_calibrations_q4_q5_20261018_r11755
- Author: session_nori_r11755_4
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: NORI1, geodesic-calibration, quadratic-incidence, finite-certificate, cube-automorphisms, F101, Q4, Q5, dimension-uniform-obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11755_4
- Updated session: session_nori_r11755_4
- Disposition: none
- Successor: none

## Related references

- subsection:edge_conditioned_turn_census_and_critical_flip_forcing
- subsection:obstruction_compatibility_and_a_programme_for_nori1_closure

## Research note

# Quadratic monochromatic-geodesic incidence: a four-cube identity and a five-cube obstruction

Investigation session session_nori_r11755_4. Motivated by the characteristic-independent linear-calibration obstruction in note_nori_pfaffian_mod8_does_not_determine_geodesic_parity_20261016 v4.

For every n, let G_n consist of unoriented full antipodal geodesics represented by their smaller antipodal root and a permutation of all n dimensions. For each legal antipodally odd coloring c, put I_c(P)=1 when all edges of P are red and 0 otherwise. A quadratic calibration over a field K is a universal identity k = sum_P a_P I_c(P) + sum_{P<Q} b_{P,Q} I_c(P)I_c(Q), for fixed coefficients independent of c and a fixed nonzero k. Both factors in each quadratic term use the SAME edge assignment, including shared edges.

**Theorem 1 (four-cube quadratic calibration, complete finite verification).** For every legal coloring of Q4, the sum over distinct simultaneously red unoriented full geodesics P<Q of alpha_{o(P,Q)} is 48. The 71 pair-orbit indices are canonically numbered by listing 192 paths (root 0 through 7, then lexicographic dimension permutations), scanning unordered pairs in lexicographic order, and numbering each orbit under the full 384-element cube automorphism group upon first encounter. The nonzero pairs (orbit index, coefficient) are:
(0,4),(2,1),(3,-10),(4,-6),(6,6),(8,22),(12,12),(13,-4),(14,-11),(17,1),(18,-4),(19,9),(21,-6),(23,6),(25,-6),(28,8),(30,6),(34,-14),(35,15),(37,6),(38,-12),(39,6),(41,-12),(44,8),(46,6),(52,-4),(56,-12),(57,6),(60,6),(61,-12),(62,-2),(66,-12),(67,6),(68,6).
All other coefficients vanish.

Proof: A standalone C++17 verifier constructs the sixteen antipodal edge orbits, the 192 unoriented full paths, the group action and its 71 pair orbits, and then checks the integer identity for all 2^16 color masks. It returns PASS: 65536 legal colorings, sum identically 48, and red-geodesic counts between 4 and 24. The sum implies a red full geodesic for every coloring of Q4; this is a finite certificate in an already settled dimension.

**Theorem 2 (dimension-uniform quadratic-calibration obstruction over F_101).** For every n>=5, there is no fixed quadratic calibration with nonzero right side over the field F_101.

Proof in Q5: The cube automorphism group has order 2^5*5!=3840, invertible modulo 101. Averaging any proposed calibration over that group makes all linear path coefficients equal and all coefficients of pairs in the same group orbit equal, while preserving its nonzero constant. The 1920 unoriented full geodesics have 565 orbits of unordered distinct pairs. Thus a putative calibration supplies a vector with 566 entries: one coefficient for the total red-path count and 565 coefficients for simultaneously-red pair counts.

Enumerate antipodal orbits of Q5 edges by scanning undirected edges in ascending smaller endpoint and ascending dimension, giving 40 mask bits. Test the 454 masks defined by mask=s for s=0,...,99 and mask=(next output of standard C++ mt19937_64 seeded 20261018) modulo 2^40 for s=100,...,453. A deterministic Gaussian eliminator over F_101 constructs their 454-by-566 incidence matrix A and obtains rank(A)=396 and rank([A|1])=397. The first inconsistent row is sample 453, with mask 604191828233 and a reduced right side 44. The 565 pair orbits are generated independently of the coloring: normalize the first oriented path to (root=0, dimension order 01234) by the unique cube automorphism and record the normalized second; minimize this key over reversal of the first path and interchange of the two paths. Since the group acts transitively on oriented full paths, these keys classify pair orbits. The modular rank contradiction is a finite proof of nonexistence for Q5.

For n>5, extend every arbitrary Q5 legal coloring by making the five old-direction rules independent of all added bits and setting each new-direction edge color to x_0. This preserves antipodal oddness. The indicator of any full Qn path factors as eta(P) I_c(proj_5 P), where eta(P) in {0,1} depends on P alone. Every putative quadratic identity in Qn restricts to an identity of degree at most two in Q5 red path indicators (using I^2=I when two projected paths coincide), with the same nonzero constant. Contradiction.

The C++17 verifiers were run and passed in the session. File names: nori_quadratic_q4_verify.cpp and nori_quadratic_q5_mod101_verify.cpp; each compiles with g++ -std=c++17 -O2 without third-party packages.

**Limits.** The Q4 certificate is a restricted-dimension identity. The Q5 obstruction applies over F_101 and thereby in every dimension n>=5. It does not by itself rule out characteristic-zero calibrations with denominators divisible by 101. Coloring-dependent coefficients, products of three or more witnesses, inequality-based forcing and the boundary-conditioned one-square repair mechanism remain untested by this theorem. This investigation does not establish unrestricted NORI1 or the simple boundary-3-tournament implication.
