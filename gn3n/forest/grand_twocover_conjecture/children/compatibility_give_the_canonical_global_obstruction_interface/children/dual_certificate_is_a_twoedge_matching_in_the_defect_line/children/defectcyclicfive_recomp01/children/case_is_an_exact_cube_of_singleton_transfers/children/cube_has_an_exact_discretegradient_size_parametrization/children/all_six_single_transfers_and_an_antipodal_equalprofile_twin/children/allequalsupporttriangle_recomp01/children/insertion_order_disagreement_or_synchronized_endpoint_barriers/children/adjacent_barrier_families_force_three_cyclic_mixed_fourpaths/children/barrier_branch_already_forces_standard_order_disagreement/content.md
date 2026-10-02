# The synchronized barrier branch already forces standard order disagreement

## Statement

Assume the synchronized endpoint-barrier branch of the all-equal {1,1,1} support triangle. Then explicit relative-order disagreement is forced between tight paths. Indeed, for every i the mixed tight four-path Q_i=(b_i,t_i,t_{i+2},a_{i+1}) orders the common vertices b_i,t_i oppositely to the displayed support path P_i=(t_i,b_i,...,a_i,t_{i+1}). Consequently the path-intersection calculus yields a reversed common ordered edge, a tight triple reversing an ordered edge at an intersection, or a vertex-simple tight cycle.

## Body

By 2bac72daae4a, Q_i=(b_i,t_i,t_{i+2},a_{i+1}) is a tight path. The displayed Hamilton path P_i on S_i begins (t_i,b_i). Thus P_i and Q_i have common vertices t_i,b_i, occurring in opposite relative orders. Apply Section 4 of pathcalc01, which is explicitly valid for arbitrary tight paths with differing supports. It yields one of the standard local order-disturbance witnesses: a reversed common ordered edge, a reversing tight triple at an intersection, or a vertex-simple tight cycle. No cyclic rotation of ordered triples is used.