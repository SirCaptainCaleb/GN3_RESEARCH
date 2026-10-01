# The four-label gap network always forces a proper tight cycle

## Statement

Let H be a minimum counterexample and suppose outcome (3) of four_side_endpoint_lock_gap_network01 holds beside the Hamiltonian four-path X=(x_0,x_1,x_2,x_3) and displayed interior path M=(b_1,...,b_h). Then H contains a proper vertex-simple tight cycle. More precisely, the monotone gap-order residue of four_side_gap_order_cycle_or_monotone01 is impossible: if g_0<g_1<g_2<g_3 are the second-type obstruction gaps of x_0,x_1,x_2,x_3, then H contains the mixed Hamiltonian four-path (b_{g_2+1},x_2,x_1,b_{g_1}), contradicting the defining absence of a mixed Hamiltonian four/five-support in the gap-network branch. Consequently the gap order has an inversion, and the displayed X-subpath together with the opposite gap connector forms a proper tight cycle. The complement of that cycle is non-Hamiltonian with path-cover number two, and the certified cycle-consumption theorem yields a tight triple reversing a displayed consecutive pair on the cycle or on a complementary two-cover path.

## Body

Work in outcome (3) of four_side_endpoint_lock_gap_network01, so the nonincreasing endpoint-repartition outcome and the mixed Hamiltonian four/five-support outcome are both absent. By four_side_gap_order_cycle_or_monotone01, either a proper tight cycle already exists or the distinct second-type obstruction gaps occur in the displayed X-order, say g_0<g_1<g_2<g_3. Assume the latter.

Because g_1 has a smaller distinct gap g_0, we have g_1>=2. The second-type normal form for x_1 gives the tight prefix path (b_1,...,b_{g_1},x_1), hence (b_{g_1-1},b_{g_1},x_1) is tight. If (b_{g_1},x_1,x_2) were tight, then (b_{g_1-1},b_{g_1},x_1,x_2) would be a Hamiltonian four-path meeting both X and M, contradicting the absence of the mixed-support outcome. Therefore (b_{g_1},x_1,x_2) is non-tight, so boundary antisymmetry gives (x_2,x_1,b_{g_1}) tight.

Similarly, because g_2 has the larger distinct gap g_3, we have g_2<=h-2. The second-type normal form for x_2 gives the tight suffix path (x_2,b_{g_2+1},...,b_h), hence (x_2,b_{g_2+1},b_{g_2+2}) is tight. If (x_1,x_2,b_{g_2+1}) were tight, then (x_1,x_2,b_{g_2+1},b_{g_2+2}) would be a mixed Hamiltonian four-path, again impossible. Thus boundary antisymmetry gives (b_{g_2+1},x_2,x_1) tight.

The last two tight triples concatenate to the Hamiltonian four-path (b_{g_2+1},x_2,x_1,b_{g_1}). Its four vertices are distinct because g_1<g_2, and it meets both X and M. This contradicts the defining no-mixed-support assumption. Hence the monotone gap-order residue cannot occur. The only remaining alternative of four_side_gap_order_cycle_or_monotone01 is a gap-order inversion, which supplies a proper vertex-simple tight cycle whose two arcs are an X-subpath and an internally disjoint connector through M.

Opening that proper cycle gives a Hamiltonian path on its support. Minimum-counterexample calculus therefore makes its complement non-Hamiltonian with path-cover number two. Finally f21cfb4840ff applies to the same two-arc cycle and supplies a tight triple reversing a displayed consecutive pair of the cycle or of a complementary two-cover path.