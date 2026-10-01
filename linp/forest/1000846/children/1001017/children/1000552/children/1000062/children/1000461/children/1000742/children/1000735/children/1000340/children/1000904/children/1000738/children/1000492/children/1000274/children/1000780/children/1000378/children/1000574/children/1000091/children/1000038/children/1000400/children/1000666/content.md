# Entrance rails on a flat gap-one terminal cycle are blocked on both sides within distance two

## Statement

Let C=(e_0,...,e_{c-1}) be a linear terminal-cycle consisting of flat ascending nonspecial edges of common rank p-1, whose terminal vertices all have potential p and whose entrance labels x_i have potential p-2 and are private on their cycle edges. For each i let R_i be a maximum (p-2)-edge entrance path ending at x_i with R_i,e_i a longest (p-1)-edge path ending in e_i. Then R_i meets e_{i+1} union e_{i+2} and also meets e_{i-1} union e_{i-2}, with indices modulo c. If c>=6 these two cycle arcs are vertex-disjoint, so R_i has at least two distinct foreign-cycle contacts, one on each side of e_i. For c=5 the two arcs meet at the terminal joint e_{i+2} intersect e_{i-2}, so a single contact at that joint may satisfy both requirements and no two-contact conclusion is asserted.

## Body

Suppose R_i is disjoint from e_{i+1} union e_{i+2}. Because x_i is private on e_i and R_i,e_i is a linear path, R_i avoids the two terminal vertices of e_i. The cycle is linear and the entrance labels are private, so
R_i,e_i,e_{i+1},e_{i+2}
is then a linear path. Its length is (p-2)+3=p+1. It ends at the forward terminal of e_{i+2}, a terminal vertex of a flat cycle edge and hence a vertex of potential p. This contradicts the definition of endpoint potential. Therefore R_i meets e_{i+1} union e_{i+2}. Reversing the cycle orientation gives the backward assertion.

If c>=6, the forward arc {e_{i+1},e_{i+2}} and backward arc {e_{i-1},e_{i-2}} are vertex-disjoint: no edge occurs in both, and no edge from one arc is consecutive to an edge from the other in the cycle. By linearity of the terminal cycle, a single R_i contact therefore cannot serve both requirements. Hence R_i has at least two distinct foreign-cycle contacts.

For c=5, however, e_{i+2} and e_{i-2} are consecutive cycle edges and share their terminal joint. A contact at that joint can satisfy both the forward and backward requirements, so the preceding argument does not force two distinct contacts.