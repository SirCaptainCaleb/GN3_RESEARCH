# Article VIII - Antipodally odd edge colorings

## Article synopsis and main argument

# Antipodally odd physical edge colorings: algebraic and central carriers

Let c_i(x) denote the binary color of the undirected edge in direction i incident to x in Q_n. The physical-edge condition is c_i(x)=c_i(x xor e_i), and antipodal oddness requires c_i(bar x)=1-c_i(x). A full antipodal geodesic traverses every coordinate exactly once. Its edge-color word can be represented by a root x and a permutation p, with j-th color c_(p_j)(x xor {p_1,...,p_(j-1)}).

## Affine syndrome method

Suppose c_i(x)=b_i+sum_j A_ij x_j over F_2. The physical-edge and antipodal hypotheses are exactly A_ii=0 and odd row sums. For a prescribed direction-color vector w, the root equations along order p read

(Ax)_(p_j)=w_(p_j)+b_(p_j)+sum_(ell<j) A_(p_j,p_ell).

When A is nonsingular, every prescribed vector is realized for every order, by selecting its unique root. When A has low corank, adjacent direction exchanges change only local crossing terms. The proved square-or-braid syndrome arguments force realization of every direction-color word for corank at most two, and odd interleaving provides further rank-two and block-cyclic families. In particular these structured colorings have monochromatic full antipodal geodesics.

## Nonlinear functional blocks

Partition coordinate directions into blocks. In the functional-driver model, all edges in one block share a color determined by exterior driver coordinates. If the entire block is traversed contiguously, its driver bits remain fixed during its traversal, so its edges are monochromatic. Appropriate orders of blocks and choices of the initial driver bits realize target block-color patterns for the established self-dual dependency families. Nonlinear signed self-dual gates and several overlapping-support configurations satisfy the same whole-block scheduling principle under their stated hypotheses.

## Central Johnson geometry

For n=2k, a monotone full cube geodesic corresponds to a permutation of n directions and its rank-k vertices to k-subsets. Consecutive exchanges produce the Johnson graph J(2k,k). In central-gated coloring models, an exact middle-belt transfer identifies colored geodesics with tight paths of k-subsets on 2k-1 distinct directions. The complement-odd completion lemma extends a qualifying tight path using one of the remaining directions. These are actual physical cube-geodesic criteria only when the endpoint caps and distinct direction support are verified.

The middle carrier has strict limits. Valid odd edge colorings can forbid monochromatic paths inside particular middle belts. In odd dimension the total mod-two square curvature is quantitatively constrained, with at least 2^(n-2) odd squares in the sharp result; in even dimension complementary-odd middle-layer labels can extend to globally flat colorings. Therefore local curvature and a single central slice need not settle the unrestricted edge conjecture.

The algebraic and central results supply independent, exact closure theorems for extensive families of physical edge colorings. Their relevance to ordered-three-face colorings lies in their root-control and path-carrier mechanisms, while the latter problem also requires the colors of overlapping ordered three-face windows to be compatible.

## Affine and block edge-coloring families

# Affine edge equations and nonlinear block scheduling

For a physical edge coloring of Q_n let c_i(x) denote the color of the i-edge at x. Edge invariance is c_i(x)=c_i(x xor e_i), and antipodal oddness is c_i(bar x)=1-c_i(x). Given a permutation p and root x, the full antipodal geodesic with order p has j-th edge color c_(p_j)(x xor {p_1,...,p_(j-1)}). We study classes in which this sequence can be prescribed, rather than merely made constant.

## Affine syndrome method

Suppose c_i(x)=b_i+sum_j A_ij x_j over F_2. Physicality means A_ii=0; antipodal oddness means every row sum of A is one. Given a desired color vector w indexed by directions, the geodesic equations become

(Ax)_(p_j)=w_(p_j)+b_(p_j)+sum_(ell<j) A_(p_j,p_ell).

Thus the only obstruction for a fixed order is membership of the right side in the image of A. In the invertible case the root x is uniquely determined for every order and target. For rank deficiency, rearranging directions alters the crossing terms. The established affine results use adjacent square and braid exchanges to realize arbitrary targets in corank at most two; a separate odd-odd interleaving argument handles rank-two affine odd colorings. Cyclic odd block dependencies admit another all-rank construction by parity padding.

## Functional block scheduling

Partition directions into blocks with color functions depending on designated driver coordinates outside the block. Traverse each block contiguously. The color on its edges is constant during that traversal, because no driver coordinate of that block changes while it is traversed. Select the starting values of driver coordinates and a block order to realize the target block colors. The proved self-dual functional-block theorems solve this finite scheduling task for their prescribed dependency architectures, including broad nonlinear families and certain overlapping driver supports. Whole-block paths then give actual antipodal monochromatic edge geodesics.

## Central-rank control and scope

For edge colorings uniform on the relevant middle-rank layers, suitable paths crossing the central cut realize prescribed edge-color sequences. Fault-tolerant variants use multiple possible middle crossings and count how many survive exceptional edges. These conclusions require their stated layer or fault hypotheses and concern physical edge windows of length one.

The common architecture is exact control of a direction-indexed color vector: affine equations, block schedules, or middle-layer symmetry. It yields full closure in substantial edge-coloring classes, while translation to ordered-three-face NORI requires handling windows involving three consecutive directions and their exterior bits.

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

# Middle-rank Johnson carriers and tight-path obstructions

The antipodally odd physical edge problem admits a central-rank formulation in even dimension n=2k. A monotone antipodal geodesic corresponds to a permutation of all n coordinates; its intermediate cube vertices correspond to the nested sets of directions already used.

## The middle carrier

At rank k, these vertices are k-subsets. Exchanges of one direction produce Johnson adjacency, and a chain of consecutive k-subsets with overlap k−1 is a tight path. For the central-vertex-gated coloring models, the proved exact transfer identifies monochromatic middle-belt cube geodesics with tight k-uniform hypergraph paths through 2k−1 distinct coordinate directions. The requirement of distinct directions guarantees geodesicity in the cube. The complement-odd tight-path completion theorem shows that a qualifying path through 2k−2 distinct directions can be extended using one of the two remaining coordinates.

This is an exact reduction for the specified central carrier. It is not an unrestricted equivalent of the original edge conjecture: legal antipodally odd edge colorings can obstruct all monochromatic paths confined to particular central belts, while still leaving other root choices available.

## Curvature and flat central realizations

Define curvature of each physical square as the parity of its four edge colors. In odd dimension the antipodal parity law forces at least 2^(n−2) odd-curvature squares, and a matching class of constructions attains the bound. In even dimension, arbitrary complement-odd middle-layer hypergraph labeling can be realized by a globally flat odd edge coloring. Hence square curvature and middle-layer labeling retain distinct degrees of freedom.

The Johnson picture offers an exact combinatorial carrier with verifiable caps; the curvature results constrain possible global lifts and show why a single middle slice is insufficient. The remaining forcing task is to select a globally compatible rooted path while retaining its actual physical edge colors.

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
