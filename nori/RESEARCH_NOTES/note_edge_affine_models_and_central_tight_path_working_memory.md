# Affine, nonlinear, and central-layer NORI1 edge-model investigations

- Stable ID: note_edge_affine_models_and_central_tight_path_working_memory
- Author: NORI manuscript editorial migration; mathematical origins recorded in original compositions
- Primary home: article:nori_article_viii_edges
- Labels: approach, partial_argument
- Lifecycle: active
- Epistemic status: proposed
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r4593_2
- Updated session: session_nori_r4593_2
- Disposition: none
- Successor: none

## Related references

- subsection:affine_and_nonlinear_edge_coloring_families, exact version 3
- subsection:central_layer_edge_carriers_and_tight_paths, exact version 1
- section:nori_edge_affine_blocks, exact version 3

## Research note

# Editorial scope and mathematical status

Structural model explorations and central tight-path translations useful for future NORI1 work but not independently proven publication-grade contributions. Established separate Article VIII theorems remain in their Subsection manuscripts.

The exact compositions below are copied verbatim from the previous manuscript hierarchy for reproducibility. Editorial transfer is not a refutation or a new mathematical proof. Manuscript historical versions and provenance remain accessible through nori.read_manuscript.


---

## Retired Subsection: Affine and nonlinear edge-coloring families

Source ID: `affine_and_nonlinear_edge_coloring_families`
Source Section: `nori_edge_affine_blocks`
Exact original Subsection composition: v3.

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



---

## Retired Subsection: Central-layer edge carriers and tight paths

Source ID: `central_layer_edge_carriers_and_tight_paths`
Source Section: `nori_edge_central_carriers`
Exact original Subsection composition: v1.

# Central cube-edge carriers and tight paths

Let n=2k and consider an antipodally odd coloring of physical edges of Q_n. A full monotone geodesic from 0 to 1 is encoded by an ordering of the n coordinate directions. Its vertices at rank j correspond to the nested j-subsets of the already used directions. Replacing one selected direction within a k-subset produces a Johnson-graph adjacency.

## Exact central tight-path transfer

For the central-vertex-gated edge-coloring models, a middle-belt monochromatic geodesic is equivalent to a tight path of complementary-odd colored k-subsets on 2k-1 distinct directions. Consecutive k-subsets overlap in k-1 directions; all distinct direction entries matter because a repeated cube coordinate would cease to yield a geodesic. The proved completion theorem extends a qualifying tight path with 2k-2 distinct directions to one with 2k-1 by choosing between the two unused directions and using complementary oddness. Together these are an exact conditional translation of the original edge problem into a central hypergraph problem.

The transfer has sharply delimited scope. Valid odd edge colorings can forbid all monochromatic antipodal geodesics constrained to a fixed middle-belt scheme, even if a monochromatic full geodesic exists elsewhere. Hence middle-belt nonexistence cannot be treated as failure of the original unrestricted conjecture.

## Cubical curvature and realizations

For a physical two-face, define mod-two curvature as the parity of its four edge colors. In odd ambient dimension, antipodal oddness forces at least 2^(n-2) odd-curvature squares, and the established functional-matching constructions attain this bound. The result supplies a quantitative geometric obstruction to flatness.

In even dimension, the converse type of phenomenon is possible: arbitrary complementary-odd middle-layer hypergraph labels extend to globally flat antipodally odd physical edge colorings. Thus vanishing curvature is compatible with flexible middle-layer data and does not by itself decide the existence of an extractable central path.

These theorems identify an exact Johnson/tight-path carrier, its completion mechanism, and its two main limitations: middle-belt root constraints and independent central color assignments. The remaining original edge-color conjecture calls for a root-mobile global carrier or a compatible path exchange beyond one middle belt.
