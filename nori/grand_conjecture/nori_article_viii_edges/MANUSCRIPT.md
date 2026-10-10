# Article VIII - Antipodally odd edge colorings

## Article setting and orientation

Let c_i(x) denote the binary color of the undirected edge in direction i incident to x in Q_n. The physical-edge condition is c_i(x)=c_i(x xor e_i), and antipodal oddness requires c_i(bar x)=1-c_i(x). A full antipodal geodesic traverses every coordinate exactly once. Its edge-color word can be represented by a root x and a permutation p, with j-th color c_(p_j)(x xor {p_1,...,p_(j-1)}).

Suppose c_i(x)=b_i+sum_j A_ij x_j over F_2. The physical-edge and antipodal hypotheses are exactly A_ii=0 and odd row sums. For a prescribed direction-color vector w, the root equations along order p read

*Full Article composition: [source manuscript](../nori_article_viii_edges.md).*

## Affine and block edge-coloring families

For a physical edge coloring of Q_n let c_i(x) denote the color of the i-edge at x. Edge invariance is c_i(x)=c_i(x xor e_i), and antipodal oddness is c_i(bar x)=1-c_i(x). Given a permutation p and root x, the full antipodal geodesic with order p has j-th edge color c_(p_j)(x xor {p_1,...,p_(j-1)}). We study classes in which this sequence can be prescribed, rather than merely made constant.

Suppose c_i(x)=b_i+sum_j A_ij x_j over F_2. Physicality means A_ii=0; antipodal oddness means every row sum of A is one. Given a desired color vector w indexed by directions, the geodesic equations become

*Full Section composition: [source manuscript](nori_edge_affine_blocks.md).*

### Affine and nonlinear edge-coloring families

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

## Central edge carriers and antipodal topology

The antipodally odd physical edge problem admits a central-rank formulation in even dimension n=2k. A monotone antipodal geodesic corresponds to a permutation of all n coordinates; its intermediate cube vertices correspond to the nested sets of directions already used.

At rank k, these vertices are k-subsets. Exchanges of one direction produce Johnson adjacency, and a chain of consecutive k-subsets with overlap k−1 is a tight path. For the central-vertex-gated coloring models, the proved exact transfer identifies monochromatic middle-belt cube geodesics with tight k-uniform hypergraph paths through 2k−1 distinct coordinate directions. The requirement of distinct directions guarantees geodesicity in the cube. The complement-odd tight-path completion theorem shows that a qualifying path through 2k−2 distinct directions can be extended using one of the two remaining coordinates.

*Full Section composition: [source manuscript](nori_edge_central_carriers.md).*

### Central-layer edge carriers and tight paths

# Central cube-edge carriers and tight paths

Let n=2k and consider an antipodally odd coloring of physical edges of Q_n. A full monotone geodesic from 0 to 1 is encoded by an ordering of the n coordinate directions. Its vertices at rank j correspond to the nested j-subsets of the already used directions. Replacing one selected direction within a k-subset produces a Johnson-graph adjacency.

## Exact central tight-path transfer

For the central-vertex-gated edge-coloring models, a middle-belt monochromatic geodesic is equivalent to a tight path of complementary-odd colored k-subsets on 2k-1 distinct directions. Consecutive k-subsets overlap in k-1 directions; all distinct direction entries matter because a repeated cube coordinate would cease to yield a geodesic. The proved completion theorem extends a qualifying tight path with 2k-2 distinct directions to one with 2k-1 by choosing between the two unused directions and using complementary oddness. Together these are an exact conditional translation of the original edge problem into a central hypergraph problem.

The transfer has sharply delimited scope. Valid odd edge colorings can forbid all monochromatic antipodal geodesics constrained to a fixed middle-belt scheme, even if a monochromatic full geodesic exists elsewhere. Hence middle-belt nonexistence cannot be treated as failure of the original unrestricted conjecture.

## Cubical curvature and realizations

For a physical two-face, define mod-two curvature as the parity of its four edge colors. In odd ambient dimension, antipodal oddness forces at least 2^(n-2) odd-curvature squares, and the established functional-matching constructions attain this bound. The result supplies a quantitative geometric obstruction to flatness.

In even dimension, the converse type of phenomenon is possible: arbitrary complementary-odd middle-layer hypergraph labels extend to globally flat antipodally odd physical edge colorings. Thus vanishing curvature is compatible with flexible middle-layer data and does not by itself decide the existence of an extractable central path.

These theorems identify an exact Johnson/tight-path carrier, its completion mechanism, and its two main limitations: middle-belt root constraints and independent central color assignments. The remaining original edge-color conjecture calls for a root-mobile global carrier or a compatible path exchange beyond one middle belt.
