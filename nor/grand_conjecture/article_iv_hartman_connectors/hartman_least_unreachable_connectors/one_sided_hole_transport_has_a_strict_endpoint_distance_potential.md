# One-sided hole transport has a strict endpoint-distance potential

## Composition

Distance to a selected endpoint is a candidate finite potential for one-sided hole transport. Termination follows if every proposed step is a legal compatible connector exchange and decreases that distance. The supplied deletion prescription still needs all new incidences checked, with two-sided and endpoint stops retained.

## Development

In the one-sided adjacent-gap exchange of the preceding subsection, suppose the unresolved incidence is on the left. While the modified block remains at least two positions from the global left endpoint, delete the next obstructing connector vertex together with the current shared-hole vertex and retain the inserted pair b,a. This preserves connector support size and leaves both global endpoint pairs unchanged. The sole unchecked distance-two incidence moves one connector position farther left. Therefore the integer distance from the obstruction to the left endpoint strictly decreases. The process cannot cycle. It terminates when the incidence becomes satisfied, when a new obstruction also appears on the right and the state becomes two-sided, or when the left endpoint collar is reached. The right-hand version is symmetric.

Audit scope: decreasing distance proves termination only for an explicitly realized sequence of legal connector states. A candidate whose unchecked distance-two incidence fails is not a zero square-path. The instruction to delete the next obstructing coordinate does not yet verify every new distance-one/distance-two incidence or the inherited two endpoint ports. Accordingly this is a proposed transport potential conditional on a legal-step lemma, with two-sided and endpoint stops still open.
