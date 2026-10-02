# Disjoint crossing source tails pay quadratic anchor-switch loss

## Statement

Let R be a maximum linear 3-uniform path ending at y. Let T_1,...,T_m be pairwise vertex-disjoint paths, each meeting R exactly at its endpoints a_i,b_i. All attachment vertices are distinct internal junctions of R, and their order is a_1<...<a_m<b_1<...<b_m. Set delta_i=|R[a_i,b_i]|-|T_i|. For m>=2, delta_i>=0 and sum_i delta_i >=(m-1)^2. For i<j, delta_i+delta_j>=2|R[a_j,b_i]|.

## Body

Junctions mean the unique vertices common to two consecutive host edges, so every split used below has valid free boundary vertices. Replacing R[a_i,b_i] by T_i preserves a linear path ending at y. Its maximality gives delta_i>=0.

For i<j concatenate the R-prefix to a_i, then T_i to b_i, then R[b_i,a_j] backwards, then T_j to b_j, then the R-suffix to y. The pieces form a linear path: the three retained host blocks are disjoint and separated by omitted nonempty blocks; the tails meet R only at their displayed distinct endpoints, and meet neither each other nor any other host vertex. Put L=|R| and C=|R[a_j,b_i]|. The length of the concatenation is L+2C-delta_i-delta_j. Maximality at y proves the pair inequality.

For adjacent i,i+1 the segment from a_{i+1} to b_i contains m-2 intervening distinct junctions, so it has at least m-1 edges. Sum delta_i+delta_{i+1}>=2(m-1) over i=1,...,m-1. The left side is at most 2 sum_i delta_i because all deltas are nonnegative. Hence sum_i delta_i>=(m-1)^2.

This is a conditional simultaneous-exchange tool. The disjoint tails, internal-junction attachments, and the connection of its metric losses to a counting slack are not asserted for the entire selected family. It does not on its own improve 43/48. The later contact-potential reduction uses a different rotation budget and does not depend on this lemma.