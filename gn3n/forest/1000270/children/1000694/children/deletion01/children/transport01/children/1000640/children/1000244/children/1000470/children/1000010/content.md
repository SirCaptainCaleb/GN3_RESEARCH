# Every deletion state is incompatible with the deletion states at its four endpoints

## Statement

Fix one deletion cover F_d=P|Q for each deletion label d in a minimum counterexample, and form the full pair-state compatibility graph. If y is any of the four displayed endpoints of P or Q in F_d, then F_d and F_y are incompatible. Consequently every compatibility neighbor of d is an internal vertex of one of the two displayed paths of F_d.

## Body

Let y be an endpoint of one component of F_d, and consider the chosen deletion cover F_y of H-y.

Apply 93340a1f1a6a to the endpoint comparison between F_d and F_y. That theorem says the comparison necessarily exposes either an internal-restoration support crossing or an ordered-cover disagreement on the common two-deletion subtournament.

Either outcome means that F_d and F_y do not induce the same full pair-state data on their common vertices. Hence they are not adjacent in the full compatibility graph.

Since F_d has exactly two components and each has two endpoints, all four displayed endpoint labels are nonneighbors of d. Therefore every compatibility neighbor of d lies internally on P or Q.