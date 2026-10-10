# Explicit one-bit physical Q7 coloring forbidding g-third and g-fifth good paths

# Explicit Q7 example forbidding every full good path with a prescribed g THIRD or FIFTH

Fix R={0,1,2,3,4,5}, g=6. The following coloring is legal antipodally reversal-odd and depends on no exterior bits other than the fixed bit x_g.

Enumerate all ordered triples t of distinct coordinates in lexicographic order. Give every no-g ordered triple t a separate Boolean variable f(t), numbering these 120 variables in their first-appearance order. For ordered triples t containing g, set h(t)=h0(min_lex(t,reverse t)) + 1[t>reverse t], and enumerate the 45 canonical representatives lexicographically after the first 120 f variables, giving 165 variables total. Let bit i−1 of the 165-bit integer
  0x10c40013edffbc7c29f7b7fbff7b8696b03e185208
be variable i. Set c(t,F)=h(t) for t containing g. For t omitting g, use c(t,F)=f(t) when fixed g-bit is 0 and c(t,F)=1−f(reverse t) when fixed g-bit is 1. Dependence on all other exterior bits is absent.

**Theorem (explicit exhaustive certificate).** This is a well-defined physical NORI coloring with no full antipodal seven-edge one-switch geodesic in which g is the third or fifth direction.

**Proof/certificate.** The reversal condition for g-faces holds by the canonical h definition, and for no-g faces by the prescribed swap of the fixed g-bit. Enumerate all 7! orders and both starting g-bits (every other starting bit is irrelevant). For order p and initial g-bit z, define window colors c_i by the above function on ordered free triple (p_i,p_(i+1),p_(i+2)), evaluated at fixed g-bit z+1[pos_p(g)<i]. Then sum [c_i≠c_(i+1)] over i=1,...,4. Independent direct evaluation of the 10,080 cases gives the count of good paths indexed by the position of g:
  position 1: 109; 2: 78; 3: 0; 4: 28; 5: 0; 6: 78; 7: 109.
The standalone checker nori_q7_fixed_third_no_go.py contains the packed coloring, NORI axiom verification, and exhaustive check (including a full good witness at another position).

**Consequence.** For unrestricted NORI, even a highly structured legal coordinate-one-bit family can block EVERY good full path with a specified coordinate centrally located as third/fifth move. The g-third extraction principle proven under a UNIVERSAL flipper cannot be extended to arbitrary g merely by continuity or a pointwise perturbation. In this example there are still 402 good full ordered paths, and the separate theorem nori_q7_one_exceptional_exterior_bit_forced_second_position_20261009 proves that ALL colorings of the present class possess a good path with g second. Thus this example is a precise local positional obstruction, not a counterexample to the grand conjecture.
