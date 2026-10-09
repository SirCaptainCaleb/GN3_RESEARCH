# A six-direction physical hub can saturate all 144 odd pentagons despite active NORI antipodal oddness

# All six-support physical-hub pentagons can simultaneously attain their minimum: an exact face-local obstruction

**Theorem (explicit six-direction universal local-saturation example).** There is an ARBITRARY binary ordered-triple function h on the six symbols {0,1,2,3,4,5} for which EVERY directed cyclic ordering of EVERY five-subset has exactly ONE same-color pair among its five neighboring ordered-three-window colors. All 6*24=144 local pentagons are simultaneously sharp; exactly 6*48=288 of 6*120=720 ordered five-direction words have one switch and the remaining432 have two, and no five-order is monochromatic. This h need NOT obey same-hub reversal oddness. It nevertheless embeds at a fixed physical hub of a fully LEGAL active NORI face coloring on Q6, paired with antipodal-reversal colors at the antipodal hub. Therefore no claim that every arbitrary physical six-hub chart has a monochromatic five-support or a strict average pentagon surplus can follow from the active NORI axiom alone.

**Complete 120-bit certificate in a compact 20x6 table.** Each first column T={a<b<c} denotes an unordered triple. The six bits are the h-values for the six ordered permutations of T in their LEXICOGRAPHIC order (a,b,c),(a,c,b),(b,a,c),(b,c,a),(c,a,b),(c,b,a):
012 101110
013 101110
014 011000
015 011000
023 001111
024 010110
025 010110
034 010110
035 010110
045 000101
123 001111
124 011100
125 011100
134 011100
135 011100
145 000101
234 111100
235 111100
245 000101
345 000101

**Finite proof, exact 144-case certificate.** For each of the six 5-subsets S, enumerate directed cyclic permutations exactly once by writing its smallest direction first, followed by the 4!=24 orders of the other directions. For p=(p0,...,p4), set
 w_j=h(p_j,p_(j+1),p_(j+2)), with indices modulo5.
Read h from the table. Direct substitution in these 6*24 cases gives
  sum_(j=0)^4 1{w_j=w_(j+1)}=1
in EACH case. This last identity is the finite certificate; it can be checked from the 20x6 table by a twelve-line loop with no solver or hypothesis beyond the displayed bits. Each 5-cycle's five rotations then yield exactly two one-switch orders and three two-switch orders; multiply by 6*24 cycles for 288 and432. All cycles attain equality in the baseline physical pentagon 2/5 density theorem.

**Actual active NORI embedding.** Fix z∈Q6. Each physical 3face F through z has one free direction set T. Assign c(F,(a,b,c))=h(a,b,c) for all six orientations of T, using the table. Its physical antipodal face bar F passes through bar z and is distinct from F because n=6>3. Assign c(bar F,(c,b,a))=1-h(a,b,c) for every orientation. No face through z also passes through bar z, and free direction sets distinguish the first-step faces, so these values are all consistent with each other. Complete every remaining physical-face involution orbit arbitrarily by choosing one representative face/orientation color and assigning its antipodal reversed mate the complement. The resulting globally LEGAL active NORI coloring has the specified six-direction local h at z, and all its local physical pentagons centered at z saturate the lower bound. This is not a counterexample to full grand closure: other hubs and full paths can be good.

**Strategic consequence.** Compare nori_cross_support_six_to_five_density_gain_coordinate_only_20261009: its six-direction reversal-odd input CANNOT be generalized to arbitrary colors of the ordered triple types at one hub. The physically unrestricted positive density theorem nori_unrestricted_large_dimension_strict_four_fifths_switch_coefficient_ramsey_20261009 uses sufficiently many directions to force rich supports by Ramsey; at six directions the present example shows that approach has a genuine local obstacle. A grand forcing lemma must connect physical hubs/roots or exploit joint two-tail incidence, rather than arguing from one arbitrary six-direction h_z in isolation.

**Short independent verification specification (optional).** Use Python itertools.combinations(range(6),5) and itertools.permutations(S), retaining orders whose first coordinate is min(S); read h using the lexicographic table and test the displayed cyclic equality sum. This tests precisely all 144 cyclic classes; the table itself provides the complete non-probabilistic certificate.
