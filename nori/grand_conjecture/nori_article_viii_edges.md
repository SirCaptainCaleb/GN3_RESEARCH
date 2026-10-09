# Article VIII - Antipodally odd edge colorings

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
