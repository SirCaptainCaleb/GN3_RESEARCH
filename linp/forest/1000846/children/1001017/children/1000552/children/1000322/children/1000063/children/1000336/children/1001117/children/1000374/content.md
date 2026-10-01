# Flat Type-A boundary sinks either branch through a common entrance or form a rainbow terminal triangle

## Statement

In loss-one sink case A at the boundary q=delta, let e={x,y,z} be the source ascending nonspecial edge of rank q, let a be the opposite endpoint of the deficiency-two path, and let f_y,f_z be the two clean terminal branches through {a,y} and {a,z}. Assume neither branch is special, both have rank q, and both are ascending. Then exactly one of the following holds. (i) phi(a)=q-1, and a is the common unique entrance of both f_y and f_z. (ii) phi(a)>=q, and a is terminal for both f_y and f_z; hence the terminal-pair edges of e,f_y,f_z form the triangle yz,ya,za. In case (ii) this triangle is rainbow in the threshold graph R_q: the three entrance colors are pairwise distinct and all have potential q-1.

## Body

By 321866bdcbef, y is terminal for f_y and z is terminal for f_z. For each ascending rank-q branch, 2a6eed0ab1f4 classifies the other cycle joint a: it is the entrance exactly when phi(a)=q-1, and otherwise it is terminal with phi(a)>=q. Since phi(a) is common to both branches, the two branches have the same type at a, proving the dichotomy. In case (ii), e has terminal pair yz, f_y has terminal pair ya, and f_z has terminal pair za. Their entrance colors are distinct: two adjacent terminal-pair edges with the same entrance would correspond to hyperedges sharing both that entrance and their common terminal, contradicting linearity. Each entrance has potential q-1 by ascendingness, while y,z,a have potential at least q. Thus all three edges occur in R_q and form a rainbow triangle.
