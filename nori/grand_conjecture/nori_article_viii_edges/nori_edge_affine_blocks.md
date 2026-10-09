# Affine and block edge-coloring families

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
