# Every paid clean-cycle chord yields theta, outer intersection, or two late source gates

## Statement

Let e be one of the paid-certified nonforest edges supplied by bee5f8c756bb, lying on its clean U_11 fundamental cycle C_e. Write r=phi(e), and let f,g be the two cycle neighbors of e. Then
  phi(f),phi(g) >= r.
Choose canonical maximum source rails R_e,R_f,R_g, of lengths
  r-1, phi(f)-1, phi(g)-1.

Then at least one of the following holds:
(1) |V(R_e)∩V(R_f)|>=2;
(2) |V(R_e)∩V(R_g)|>=2;
(3) V(R_f)∩V(R_g) is nonempty;
(4) both adjacent intersections are unique aligned joints, the outer rails R_f,R_g are disjoint, and if their gate indices on R_e are t_f,t_g, then
    min{t_f,t_g} >= ceil((r-1)/2).

Thus every paid clean-cycle chord either immediately creates theta/multiple-overlap structure, closes a three-rail intersection triangle, or forces both adjacent simple gates into the late half of its source rail.

## Body

Because f and e share one terminal and both are ascending nonspecial, their canonical source rails intersect by 0c885137ea8c. The same holds for e and g.

If either adjacent pair has at least two common vertices, we are in (1) or (2). Hence assume both adjacent intersections are unique. By the universal unique-intersection alignment theorem 5854d853a44b, write their common vertices as aligned joints at indices t_f and t_g on the respective rail pairs.

If R_f and R_g intersect, we are in (3). Otherwise the outer rails are disjoint. Apply e4cf6b2dc266 to the three maximum paths
  A=R_f, B=R_e, C=R_g.
Its two aligned gates are t_f,t_g, so
  min{t_f,t_g}
  >= ceil(min{|R_f|,|R_g|}/2).

Since e is minimum-rank on its fundamental cycle by bee5f8c756bb,
  phi(f),phi(g)>=phi(e)=r.
Therefore
  |R_f|=phi(f)-1>=r-1,
  |R_g|=phi(g)-1>=r-1.
Consequently
  min{t_f,t_g}>=ceil((r-1)/2),
which is (4).
