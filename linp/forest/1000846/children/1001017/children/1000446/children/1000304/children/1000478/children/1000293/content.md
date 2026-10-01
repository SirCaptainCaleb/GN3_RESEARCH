# Refuted: incidence-rank bound for ascending edges

## Statement

Refuted. It is not true in general that rank_R(N_↑)>=2A/3 for the incidence matrix restricted to ascending edges. The family c3e95f4ce77d has A=9t and rank_R(N_↑)=5t+2, which violates the bound for every t>=3.

## Body

The conjecture is refuted by c3e95f4ce77d. That family consists of t properly 3-edge-colored K_{3,3} terminal components sharing three entrance vertices. For t>=2 all 9t hyperedges are ascending, while the ascending incidence rank is 5t+2. Thus at t=3 the rank is 17<18=2A/3, and asymptotically rank/A tends to 5/9. The failure is informative: the sharp global count A<=3n/2, if true, cannot be obtained merely by forcing the ascending incidence columns to consume 2/3 of a dimension per edge.
