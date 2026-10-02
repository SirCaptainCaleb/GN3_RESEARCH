# Gap-three two-hole rotations force high-potential omitted vertices

## Statement

Let Q=(p_1,...,p_s) be an s-edge wrong-entrance path omitting exactly two vertices a,b, chosen so that sort(phi(a),phi(b)) is lexicographically maximal among such states. A two-hole collision spanning one omitted cell gives an (s+1)-edge wrong-entrance lift and is impossible. A gap-three collision instead rotates Q to another s-edge wrong-entrance two-hole state. If its cut is between p_i and p_{i+3}, then both current holes satisfy phi(a),phi(b)>=max{i,s-i-2}; in particular a cut within r cells of either end forces both hole potentials at least s-r-2.

## Body

The two blocker edges through the holes splice into Q whenever their outer contacts cap a single omitted cell; the resulting path has length s+1 with unchanged final suffix, contradicting the wrong-entrance rank bound. If the cap distance is three, the same splice has length s and produces another admissible two-hole state, replacing two old path vertices by the old holes. Choose the original state lexicographically maximal in the sorted hole-potential pair. The ejected vertices lie in p_{i+1}∪p_{i+2}; the position-sensitive endpoint-potential bound gives each potential at least max{i,s-i-2}. Maximality then forces the old hole pair to dominate the new pair coordinatewise at its minimum, so both original holes satisfy the same lower bound.