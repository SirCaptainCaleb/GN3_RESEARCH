# The monotone four-label gap network has separated second-neighbor gaps

## Statement

Continue the gap-network residue of four_side_endpoint_lock_gap_network01 with X=(x_0,x_1,x_2,x_3). Then either H contains the proper tight cycle supplied by four_side_gap_order_cycle_or_monotone01, or the obstruction gaps satisfy g_0<g_1<g_2<g_3 in the X-order and additionally g_2-g_0>=3 and g_3-g_1>=3. Consequently g_3-g_0>=4, the interior path M has order at least six, and the original partner path P has order at least eight. In this monotone residue, each x_i reverses the distinct displayed edge b_{g_i}b_{g_i+1} through the tight triple (b_{g_i+1},x_i,b_{g_i}).

## Body

By four_side_gap_order_cycle_or_monotone01, absence of the proper-cycle branch forces the gap order to agree with X, so g_0<g_1<g_2<g_3. Suppose g_2-g_0=2. Distinctness then forces g_1=g_0+1 and g_2=g_0+2. The spacing theorem gives the tight four-vertex connector C=(x_0,b_{g_0+1},b_{g_2},x_2) from x_0 to x_2. The displayed subpath (x_0,x_1,x_2) of X is a tight three-vertex corridor with the same endpoints and internally disjoint from C. Apply 53d257fcf0a8: their five-vertex union is Hamiltonian. It meets both X and M, contradicting the defining no-mixed-support residue of four_side_endpoint_lock_gap_network01. Hence g_2-g_0>=3. The same argument on (x_1,x_2,x_3) gives g_3-g_1>=3. Since the gaps are integer positions, these inequalities imply g_3-g_0>=4. A path supporting gap indices differing by at least four must have at least six vertices, so |M|>=6 and |P|=|M|+2>=8. The reverse-through-gap triples are inherited from the second-type obstruction normal form.
