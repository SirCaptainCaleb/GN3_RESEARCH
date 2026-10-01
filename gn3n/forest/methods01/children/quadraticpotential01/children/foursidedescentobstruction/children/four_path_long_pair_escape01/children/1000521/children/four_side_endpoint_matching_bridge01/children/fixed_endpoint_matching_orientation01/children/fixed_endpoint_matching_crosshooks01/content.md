# The fixed-endpoint matching shell carries a complete opposite-orientation hook rectangle

## Statement

In the perfect-matching branch of four_side_endpoint_matching_bridge01, use fixed_endpoint_matching_orientation01 to write X=C_+ disjoint-union C_- with |C_+|=|C_-|=2 and fixed endpoints a,b, where (a,y,b) is tight for every y in C_+ and (b,z,a) is tight for every z in C_-. Then for every y in C_+ and z in C_-, the cross four-set {a,b,y,z} is non-Hamiltonian and both (y,a,z) and (z,b,y) are tight. Moreover each such cross four-set is either the exceptional cyclic non-Hamiltonian K4 or an edge-orderable matching-block K4 with {ay,bz} strictly below {az,by} in every representing edge order.

## Body

By fixed_endpoint_matching_orientation01, the two same-class pairs are exactly the two edges of the perfect-matching good-pair graph J. Hence every cross pair y in C_+, z in C_- is a nonedge of J, so {a,b,y,z} is non-Hamiltonian. The orientation-class definition gives (a,y,b) and (b,z,a) tight. Apply opposite_fixedpair_nonham_k4_class01 to this cross four-set. It forces (y,a,z) and (z,b,y) tight and gives the stated cyclic-or-matching-block classification with fixed block precedence. Since y,z were arbitrary, the four cross cells form the complete 2-by-2 hook rectangle.
