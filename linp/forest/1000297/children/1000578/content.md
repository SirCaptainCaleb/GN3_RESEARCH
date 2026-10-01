# Random endpoint exposure and entropy charging

## Statement

Randomly order the vertices and expose each hyperedge through its earliest vertex, producing a random assignment of every edge to one endpoint. For a longest loose path P, analyze the probability that an assigned off-path edge creates a legal extension or splice at the first exposed contact with P. Average over the random order to obtain a global inequality in which an edge that is locally 'bad' for one endpoint is unlikely to be bad for all three endpoints simultaneously. Seek an expectation bound that replaces deterministic minimum-rank assignment and yields a smaller average congestion constant.

## Body

Why it might matter globally:
The present coefficient loss may partly come from committing every edge to one deterministic terminal and paying worst-case local congestion there. Random assignment can symmetrize the three vertices of an edge and convert mutually exclusive obstruction patterns into averaged savings. If the obstruction events at different endpoints cannot all be large in a linear hypergraph, the expectation could produce a strict leading-term gain without classifying every local pattern.

Plausible first attack:
For one edge e={a,b,c} outside a fixed longest path, define B_x as the event that assigning e to x fails to create a usable extension/splice because of the first contact geometry. Express the random-order assignment probabilities exactly and prove a local inequality sum_x Pr[x is assigned and B_x] <= 1-epsilon whenever e has at least two geometrically distinct path contacts. Then sum over edges and isolate the truly one-contact exceptional family.
