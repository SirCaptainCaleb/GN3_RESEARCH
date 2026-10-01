# The order-preserving mixed residue through x is either multiply crossed or supported on one old-path cut

## Statement

Continue the order-preserving no-direct-crossing normal form of astra003lockedbridgenormal, and suppose the split long-side class is represented by a displayed old path R=(r_1,...,r_m). Its vertices are partitioned between the mixed-component monochromatic block B and the residual monochromatic block C of the two-cover T. Then either the old path R contains at least two ordinary edges whose endpoints lie in different T-components, or there is a unique index i such that V(B) and V(C) are exactly the two contiguous intervals {r_1,...,r_i} and {r_{i+1},...,r_m}, in one order. Thus after excluding multiple crossing, the rigid residue through x is controlled by a single cut of one old long path.

## Body

Mark each vertex r_j by the T-component containing it, equivalently by whether it belongs to B or C. Because both B and C are nonempty, the binary word of marks uses both symbols. Every old-path edge r_j r_{j+1} whose endpoint marks differ is an ordinary edge of the displayed path R crossing the two T-component supports. If the mark word changes value at least twice, R contains at least two such crossing edges, giving the first alternative. Otherwise it changes exactly once, at some index i. Then one mark occurs on r_1,...,r_i and the other on r_{i+1},...,r_m, so the two block supports are contiguous complementary intervals of the old displayed path. Conversely such a contiguous split has exactly one old-path crossing edge. No orientation assumption beyond the already established order preservation inside each monochromatic T-block is needed for this support conclusion.
