# Every flat gap-one terminal cycle forces a balanced lens between entrance rails

## Statement

Let
  C=(e_0,...,e_{c-1}), c>=4,
be a flat gap-one terminal cycle with
  e_i={x_i,t_i,t_{i+1}},
where every e_i is ascending nonspecial of rank p-1, every t_i has vertex rank p, and every private entrance x_i has vertex rank p-2. For canonical maximum entrance rails R_i ending at x_i, some two distinct rails contain a balanced elementary lens. Equivalently, the entrance-rail lens-free residual is impossible.

## Body

Assume for contradiction that the cycle is entrance-rail lens-free. Then all conclusions of 960a5153b900, 8777d2ccd614, and 14bb137811b4 apply.

If c=5, 14bb137811b4 already gives a contradiction.

If c=4, the four rails R_0,R_1,R_2,R_3 have unique intersections on each consecutive pair by 960a5153b900, while the opposite pairs R_0,R_2 and R_1,R_3 are disjoint by 14bb137811b4. This is forbidden by the four-path lemma 188e6b091d88.

Now let c>=6 and fix i. Consider the four equal-length maximum entrance rails in the cyclic order
  A=R_i,
  B=R_{i+1},
  C=R_{i+2},
  D=R_{i-1}.
The pairs A-B, B-C, and D-A are adjacent rail pairs, so each has exactly one common vertex by 960a5153b900. The pair C-D has cyclic index difference three, so
  V(C) intersect V(D)={t_{i+1}}
by 8777d2ccd614, again a unique intersection. The opposite pairs A-C and B-D have cyclic index difference two and are therefore disjoint by 14bb137811b4. Thus A,B,C,D satisfy exactly the forbidden configuration of 188e6b091d88, a contradiction.

Hence no entrance-rail lens-free flat gap-one terminal cycle exists. Therefore every such cycle contains a balanced elementary lens between two distinct canonical entrance rails.