# Affine and nonlinear edge-coloring families

# Affine and nonlinear block families in the antipodally odd edge problem

For physical undirected edges of Q_n, write c_i(x) for the color of the edge in direction i incident with x; thus c_i(x)=c_i(x xor e_i). Antipodal oddness is c_i(bar x)=1-c_i(x). A full direction-distinct geodesic starting from root x in order p=(p_1,...,p_n) has colors c_(p_j)(x xor {p_1,...,p_(j-1)}). Unlike ordered-three-face NORI, each new step contributes exactly one edge color, so global color words can be studied by choosing the root and permutation.

## Affine coloring and change equations

Let c_i(x)=b_i+sum_j A_ij x_j over F_2, with A_ii=0 and each row of A having odd sum. These conditions ensure physical-edge invariance and antipodal oddness. A prescribed direction-color word w imposes n linear equations on x and order-dependent crossing corrections: at step j, the equation is (Ax)_(p_j)=w_j+b_(p_j)+sum_(ell<j) A_(p_j,p_ell). A root realizing w therefore exists whenever its right side lies in the column image of A. If A is surjective this holds for every order and word.

For deficient rank, the existing corank-one and corank-two closure theorems exploit changes of the direction permutation to alter the residual syndrome. An adjacent swap of directions i,j changes the right-hand sides only through the mutual coefficients A_ij,A_ji, giving an explicit square-or-braid adjustment. The established odd-odd interleaving theorem proves that rank-two affine odd colorings realize every prescribed direction-indexed color vector; corank at most two likewise admits a global syndrome construction. These are stronger than the monochromatic closure required by the original edge conjecture.

## Functional block colorings

Partition the direction set into blocks B_1,...,B_m and assign each block a Boolean color function of designated driving coordinates. If all coordinates of a block are traversed consecutively, the colors within that block remain constant whenever the function depends only on coordinates outside that block. The problem reduces to selecting a block order and starting input bits that realize desired block colors.

For disjoint driver supports the root bits can be chosen independently, and the established functional-block theorem realizes every desired block-color pattern under its stated self-dual and dependency hypotheses. The nonlinear extension replaces linear parity gates with odd self-dual Boolean functions; the proof uses the freedom to choose appropriate inputs and a whole-block schedule, and includes overlapping driver supports in the specialized functional-driver setting. These statements concern their explicit block architectures, where the local root constraints can be solved consistently.

## Central-rank structured families

Additional edge-coloring families have colors uniform on one central exterior-Hamming-rank layer (in even dimension), or on paired near-central layers (in odd dimension). Their proofs select a monotone middle-level crossing, then choose the initial and terminal subpaths to fit the specified color vector. Robust versions tolerate a bounded number of faulty central edges by counting many candidate geodesics and avoiding corrupted edges. Such results describe large structured classes with unconditional full-geodesic closure; uniformity and quantitative fault hypotheses are essential.

Taken together, affine syndrome surjectivity, block scheduling and central-rank crossings give independent mechanisms for realizing monochromatic and even arbitrarily prescribed edge-color words. Their successful extraction relies on the single-edge window structure and does not automatically transfer to physical ordered-three-face NORI.
