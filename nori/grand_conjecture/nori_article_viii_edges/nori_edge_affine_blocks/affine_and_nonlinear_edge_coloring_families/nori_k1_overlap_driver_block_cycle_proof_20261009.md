# Overlapping nonlinear input supports in functional-driver block edge colorings

Theorem. Partition coordinates into blocks B_j, and let each block j depend on a self-dual Boolean gate on any subset of a distinct driver block B_sigma(j), where sigma(j) differs from j. Gates may overlap arbitrarily. With one bias b_j per block, every prescribed block-color vector is realized on an actual full antipodal geodesic. Proof: traverse each block contiguously. Each edge in B_j has color b_j+g_j(x)+1{driver before j}. Each functional dependency component has one cycle and trees. Choose a total order of cycle vertices. For each cycle arrow j to k, choose starting bits in driver block k to force the gate value required by this order; there is only one such cycle constraint per driver block and self-duality ensures both gate values are achievable. Choose remaining bits arbitrarily. Orient each tree arrow according to its now-fixed gate value to meet its block target. This creates no precedence cycle, since all tree edges are bridges and cycle edges follow a fixed linear order. Topologically order blocks, concatenate their directions, and obtain the target colors. No disjointness of gate supports is needed. This strengthens the recent arbitrary-selfdual-disjoint-block theorem; unrestricted odd edge colorings remain open.

DETAILS OF PHYSICAL ROOT CONSTRUCTION AND THE EXACT FUNCTIONAL-GRAPH CONDITION.

Write c_v(x)=b_j+g_j(x|_{M_j}) for v in B_j, with M_j subset of B_{sigma(j)} and sigma(j)!=j. Traversing all directions of B_{sigma(j)} before any B_j edge toggles EVERY bit of M_j. Thus, by gate self-duality, the gate output shifts by exactly one. Traversing B_j before B_{sigma(j)} leaves M_j unchanged. No other block changes M_j. This yields the exact identity
  color(B_j)=b_j+g_j(x|_{M_j})+e_j,
where e_j is the Boolean predicate driver block sigma(j) occurs BEFORE j in a total block order.

On each directed cycle j1->j2->...->jr->j1, choose any strict total order on its r vertices. For each arrow js->k, the cycle target fixes ONE equation on the root coordinates of B_k:
  g_js(x|_{M_js})=b_js+T_js+1{k before js}.
Because each cycle vertex k has exactly one predecessor js WITHIN THAT CYCLE, and each gate's support is contained in B_k, these cycle equations operate on disjoint coordinate blocks. The gate g_js is surjective, since g_js(bar y)=1+g_js(y); select any input assignment to M_js producing the desired bit. If there are other tree arrows j->k whose input supports overlap M_js, their gate outputs are allowed to be whatever the selected assignment makes them. That is the reason no support disjointness is needed. Then assign all otherwise unrestricted root coordinates arbitrarily and compute every tree gate output.

For every arrow j->k NOT in a cycle, its desired edge color T_j now uniquely determines which block comes first:
  k before j if g_j(x|_{M_j})+b_j+T_j=1,
  j before k otherwise.
These are orientations of tree edges, which cannot create a directed cycle no matter how they are chosen. The cycle edges themselves were oriented by a globally consistent total order, and each component contains only that one underlying cycle (with the 2-cycle treated as two parallel functional arcs giving the same precedence). Thus a topological block ordering exists. Concatenating full blocks in that order yields the required actual geodesic and block colors.

COUNTEREXAMPLE-FACING SCOPE. This theorem concerns original k=1 cube EDGES, NOT ordered three-faces, and makes no claim about direction-dependent biases within a block. It significantly weakens the independence assumptions for the general nonlinear class, but still uses the functional-dependency hypothesis that each consumer block's ENTIRE gate depends on only one other driver block. If that hypothesis fails, the root cycle-equation argument may impose multiple incompatible gate requirements on a single coordinate block.
