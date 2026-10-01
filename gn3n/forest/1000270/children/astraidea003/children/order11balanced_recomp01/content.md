# All balanced order-eleven states lie in one Astra component

## Statement

Let H be an order-eleven minimum counterexample. Assume every omission-containing Astra component has at least nine reachable singleton labels, every vertex x has some 5|5|1 state with singleton x, and every 4|4|3 state reaches some 5|5|1 state. Then all 5|5|1 states and all 4|4|3 states lie in one Astra connected component.

## Body

For a fixed singleton x, any two 5|5|1 states are adjacent by replacing the two five-sides on H-x, so singleton-label sets of distinct omission-containing components are disjoint. Each such component contains at least nine singleton labels, while H has only eleven vertices; hence there can be only one omission-containing component. Since every vertex x occurs in some 5|5|1 state, that unique component contains a 5|5|1 state for every singleton label, and the fixed-singleton adjacency puts every 5|5|1 state in it. Finally every 4|4|3 state reaches a 5|5|1 state by the standard bridge, so reversibility puts every 4|4|3 state in the same component.
