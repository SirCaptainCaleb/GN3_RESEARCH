# Lens-free selected cycle chords yield theta, outer intersection, or two late gates

## Statement

Retain the lens-free family H_v from 6f2f8b7f1053. Fix a center-edge incidence
  (v,e),  e={x,v,u} in H_v,
and write r=phi(e). Let f,g be the two hyperedges whose terminal-pair edges are adjacent to e on its clean-U11 fundamental cycle C_e. Then
  phi(f),phi(g)>=r.

Choose canonical maximum source rails
  R_e,R_f,R_g
ending at the unique entrances of e,f,g, of lengths
  r-1, phi(f)-1, phi(g)-1.

At least one of the following holds:

(1) |V(R_e) intersect V(R_f)|>=2;
(2) |V(R_e) intersect V(R_g)|>=2;
(3) V(R_f) intersect V(R_g) is nonempty;
(4) both adjacent intersections are unique aligned joints, the outer rails R_f,R_g are disjoint, and their gate indices t_f,t_g on R_e satisfy
    min{t_f,t_g} >= ceil((r-1)/2).

Moreover e still carries, at the selected center v, its common-anchor switching certificate from 6f2f8b7f1053. Hence in residual case (4) the same source rail R_e simultaneously has two late fundamental-cycle gates and belongs to a whole-chord selected state whose certificate anchor precursor contains both x and u.

## Body

By 6f2f8b7f1053, e is minimum-rank on its fundamental cycle, so its two cycle neighbors f,g satisfy
  phi(f),phi(g)>=phi(e)=r.
All three parent hyperedges lie in the source-clean U11 graph.

The edges e,f share a terminal, so their canonical source rails intersect by 0c885137ea8c. Similarly R_e and R_g intersect.

If either adjacent pair has at least two common vertices, we obtain (1) or (2). Assume therefore that each adjacent intersection is unique. The universal unique-intersection theorem 5854d853a44b makes each common vertex an aligned joint at the same index on the two corresponding maximum source rails. Denote the two gate indices on R_e by t_f,t_g.

If R_f and R_g intersect, outcome (3) holds. Otherwise the outer rails are disjoint. Apply e4cf6b2dc266 to the three maximum endpoint paths
  A=R_f, B=R_e, C=R_g.
The two adjacent unique intersections are aligned gates and the outer rails are disjoint, so
  min{t_f,t_g}
  >= ceil(min{|R_f|,|R_g|}/2).
Since |R_f|=phi(f)-1>=r-1 and |R_g|=phi(g)-1>=r-1,
  min{t_f,t_g}>=ceil((r-1)/2),
which is (4).

The final selected-anchor assertion is inherited directly from 6f2f8b7f1053 and is not used in the four-way proof. It is deliberately retained as additional structure for the residual case. No endpoint-lens premise is used.