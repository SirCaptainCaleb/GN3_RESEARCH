# The zero-root support component is uniformly balanced

## Composition

(none yet)

## Development

Let H be a minimum counterexample on n=2r+1 vertices. For each hole v choose a minimum-imbalance deletion cover F_v, and suppose the zero exact-root theorem supplies one balanced selected cover F_x=P|Q with |P|=|Q|=r. Let J be the selected support graph: its vertices are the path supports occurring in the F_v and the edge labeled v joins the two supports of F_v.

Let T be the connected component of J containing the balanced edge PQ. Then every support vertex of T has cardinality r. Consequently every selected deletion cover whose edge lies in T is balanced r|r.

Proof. On every edge AB of J, with hole label v, the supports are disjoint and A union B=V(H)-{v}; hence |A|+|B|=2r. Therefore along an edge, size transforms by s -> 2r-s. Along a path, support sizes alternate between two values s and 2r-s; equivalently the size is constant on each bipartition class of a tree and the same parity conclusion remains true around any walk. Since T contains adjacent supports P,Q with |P|=|Q|=r, both alternating values equal r. Hence every support reached from P or Q has size r.

Thus the zero root propagates exact balance through its entire selected-support component without any order compatibility hypothesis. In particular strict support containment is impossible inside T, and every edge label occurring in T has a balanced minimum-imbalance deletion cover.
