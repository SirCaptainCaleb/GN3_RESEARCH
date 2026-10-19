# Q6 paired-square switches span every rootwise linear witness-census variation

- Stable ID: note_nori_xvi_linear_root_census_square_switch_obstruction_20261018_r11755
- Author: unspecified; session provenance retained
- Primary home: subsection:edge_conditioned_turn_census_and_critical_flip_forcing
- Labels: NORI1, square-switch, paired-flat, balanced, rooted-geodesics, linear-invariant-obstruction, computational-certificate, Q6
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11755_1
- Updated session: session_nori_r11755_1
- Disposition: none
- Successor: none

## Related references

- subsection:obstruction_compatibility_and_a_programme_for_nori1_closure

## Research note

# Paired-flat Q6 square switches defeat all linear root-census invariants

Let directions 0,...,5 form pairs (0,1), (2,3), (4,5). Let f_i be a Boolean function of the four bits outside pair i, satisfying f_i(z+1111)=1+f_i(z). Define c_{2i}=f_i, c_{2i+1}=1+f_i (mod 2). This is legal, paired-flat, and vertex-balanced. Toggling f_i at any complementary pair z,15-z switches an antipodal pair of alternating (2i,2i+1)-squares.

For each root x, let N_x be the number of all-red full geodesics rooted at x, and S_x the signed count of those geodesics, each weighted by the sign of its permutation of directions 0,...,5. Path reversal gives N_{63-x}=N_x and S_{63-x}=-S_x. Hence the joint root census is determined by (N_0,...,N_31,S_0,...,S_31).

**Theorem (finite arithmetic certificate).** The real span of changes in these 64 quantities over legal paired-square switches is R^64. Consequently no nonzero real linear functional of this joint root census is preserved under every such switch.

Encode each f_i by an integer h_i between 0 and 255: when z<8 its value is bit z of h_i, and for z>=8 its value is one minus bit 15-z of h_i. For each listed row (h0,h1,h2;i,z), form the prescribed coloring c and its switched neighbor c', compute all 64 rooted red counts N_x and signed counts S_x by testing all 720 permutations at each root, and concatenate the 32 differences N_x(c')-N_x(c), followed by the 32 differences S_x(c')-S_x(c), x=0,...,31. The resulting 64x64 integer matrix has determinant 950 modulo 1009, as verified by Gaussian elimination over F_1009. The nonzero determinant proves the theorem. The row certificates are:

215,122,188;1,1
224,113,85;0,6
72,211,239;0,4
134,72,251;1,6
253,207,173;2,0
239,97,37;1,5
182,199,107;2,5
98,51,167;2,6
130,67,218;0,7
199,244,129;1,6
89,130,22;0,5
143,223,95;1,2
166,185,128;2,2
115,57,9;1,6
134,104,19;1,2
240,70,51;1,4
241,153,196;1,6
213,139,11;2,2
214,10,228;0,6
251,53,38;1,2
248,20,246;1,3
3,216,163;2,1
42,41,111;0,7
0,33,159;1,4
27,187,34;2,1
242,55,242;0,3
232,244,174;2,5
7,27,28;2,2
38,165,196;0,4
70,247,24;0,4
203,25,70;0,5
64,58,221;2,1
216,63,49;1,3
111,38,111;1,4
118,113,219;2,1
26,81,157;1,7
104,93,136;0,5
178,156,159;1,1
99,139,199;0,3
236,2,80;1,6
87,152,47;0,2
67,52,190;0,6
35,25,32;1,7
36,121,145;0,1
32,1,255;2,0
74,202,134;2,0
53,152,50;2,3
191,142,122;2,1
75,234,23;0,6
87,89,22;1,4
220,232,32;1,7
230,13,97;2,5
129,253,183;1,0
184,51,217;2,5
35,242,28;0,7
66,132,168;1,2
176,111,145;2,3
211,12,101;1,4
45,111,180;1,1
38,154,135;1,6
118,178,132;1,5
251,185,193;1,7
159,10,38;1,2
61,243,105;2,2

**Independent scalar-count witness.** Define f0=x5, f1=maj(x0,x4,x5), f2=maj(x0,x1,x3), where maj(a,b,c)=ab+ac+bc modulo 2. Toggle f0 at the two complementary outside-bit strings (x2,x3,x4,x5)=(0,1,0,0),(1,0,1,1). Direct enumeration over all roots and orders gives 208 red and 208 blue full geodesics before the switch, and 212 red and 212 blue afterwards. Thus the total monochromatic rooted count changes from 416 to 424. Every modulus not dividing 8 fails to be a universal congruence invariant of the total.

**Scope.** This eliminates linear conservation laws based on the full pair of rooted unsigned and permutation-signed witness-count vectors, even under perfectly balanced paired-flat square switches. It does not eliminate nonlinear or order-retaining indices, and does not refute witness existence: both endpoints of every certified switch are good. The theorem is a Q6 computer-verifiable finite certificate, not NORI1 closure.
