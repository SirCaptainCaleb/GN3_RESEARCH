# A fixed-pair perfect matching forces a complete opposite-orientation hook rectangle

## Statement

Let H be a boundary tournament, let a,b be distinct vertices, and let X be a four-set disjoint from {a,b}. Let J on X join xy exactly when H[{a,b,x,y}] is Hamiltonian, and suppose J is a perfect matching. Write X=C_+ disjoint-union C_- as in fixedpair_perfect_matching_orientation01. Then for every y in C_+ and z in C_-, the four-set {a,b,y,z} is non-Hamiltonian and the four triples (a,y,b), (b,z,a), (y,a,z), (z,b,y) are tight. Moreover each cross four-set is either the exceptional cyclic non-Hamiltonian K4 or an edge-orderable matching-block K4 with {ay,bz} strictly before {az,by} in every representing edge order.

## Body

By fixedpair_perfect_matching_orientation01, C_+,C_- are the two matching edges of J and each cross pair is a nonedge, hence {a,b,y,z} is non-Hamiltonian. The class definitions give (a,y,b) and (b,z,a). Apply opposite_fixedpair_nonham_k4_class01 to obtain (y,a,z),(z,b,y) and the cyclic-or-matching-block classification. This holds for every one of the four cross pairs.
