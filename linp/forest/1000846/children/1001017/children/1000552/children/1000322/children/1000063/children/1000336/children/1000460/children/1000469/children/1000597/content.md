# Every private vertex of a minimum-degree cycle has a mobile ear

## Statement

Let C=(e_1,...,e_q) be a linear q-cycle in a linear 3-graph H with minimum degree at least q. For each i let p_i be the private vertex of e_i, i.e. the unique vertex of e_i not used in the two cycle intersections. Then there is an edge f_i != e_i through p_i having at most one additional vertex on V(C). More quantitatively, if C_0(i),C_1(i),C_2(i) count the noncycle edges through p_i having respectively 0,1,2 other vertices on V(C), then 2C_0(i)+C_1(i)>=1.

## Body

Any edge f!=e_i through p_i cannot contain either of the two cycle-joint vertices of e_i, since otherwise f and e_i would share p_i and that joint, contradicting linearity. Distinct edges through p_i have pairwise disjoint non-p_i vertex pairs. Thus the total number of cycle contacts made by the noncycle star at p_i is C_1(i)+2C_2(i), and these contacts are distinct vertices among V(C) minus e_i, a set of size 2q-3. Hence C_1(i)+2C_2(i)<=2q-3. Also C_0(i)+C_1(i)+C_2(i)=d_H(p_i)-1>=q-1. Doubling the latter inequality and subtracting the former gives 2C_0(i)+C_1(i)>=1.
