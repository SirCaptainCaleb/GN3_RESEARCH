# Every pair in an eight-set escapes through an external reachable three-side on a trapped 3|5|5 plateau

## Statement

Let K be a trapped connected Astra-003 component consisting of 3|5|5 states on thirteen vertices, and let D be its family of reachable three-side supports. For every eight-vertex set W and every pair L subset W, there exists r outside W such that L union {r} belongs to D. In particular, if W supports the six-cycle normal form of five_three_sixcycle_normalform01 with distinguished pair {a,d} and recurring pairs A_0,A_1,A_2, then there are exterior labels r_*,r_0,r_1,r_2 in V(H)-W such that {a,d,r_*}, A_0 union {r_0}, A_1 union {r_1}, and A_2 union {r_2} are all reachable three-side supports in the same trapped component.

## Body

By the certified pair-completeness theorem 4ca435ad8cae, every pair L of vertices has D-codegree at least seven: there are at least seven distinct vertices r outside L with L union {r} in D. If L is contained in an eight-set W, only six vertices of W lie outside L. Therefore at least one of the seven extension labels lies outside W. This proves the general assertion. The six-cycle specialization applies the same conclusion to the four indicated pairs inside its eight-vertex support. No claim is made that the four exterior witnesses are distinct.
