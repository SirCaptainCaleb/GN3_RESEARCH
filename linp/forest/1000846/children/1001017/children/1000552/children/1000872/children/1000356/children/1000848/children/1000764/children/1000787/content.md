# The defect-corrected two-rank block is automatic at the half-rank top boundary

## Statement

Let v have
  p=phi(v)=2q-2,
and fix a maximum p-edge endpoint path P_v.

Suppose four potential-charged ascending edges assigned to v have ranks in {q,q+1}. Let n_r be their rank counts and d_r the number among them that are double contacts on P_v.

Then
  (n_q-d_q)+(n_{q+1}-d_{q+1}) <= 1.
In particular the defect-corrected consecutive-rank block bound <=3 holds with two units to spare.

## Body

By the odd-central-window theorem, at p=2q-2 there is at most one rank-q edge among the four. The only critical four-edge pattern not already excluded by the existing spacing/rank machinery is therefore
  q,(q+1),(q+1),(q+1).

Fix its rank-q edge e and three high rank-(q+1) edges.

The top-boundary all-visible theorem 0592bb08cd2d says that on every maximum P_v, each high edge has its unique entrance visible in one of the four central slots a,b,c,d.

For every such occupied high entrance y, the subsequent cross-cut analysis places its opposite terminal z_y on P_v as well:
- for y in {a,b}, eddd8ad49835 places z_y in the right side;
- if d is occupied, d22fb281de15 places z_d and any other right-side high terminal in the left side as appropriate;
- in the sole d-free pattern abc, 4b2eb2497cf0 and the ac conflict 872bb5f4effc place z_a and z_c on opposite sides, while eddd8ad49835 places z_b on the right.

Thus each of the three rank-(q+1) high edges contains both of its non-v vertices on P_v: its entrance and its opposite terminal. Hence all three are double contacts at v. Therefore
  d_{q+1}>=3.

Since n_q+n_{q+1}=4,
  (n_q-d_q)+(n_{q+1}-d_{q+1})
  <=4-3=1.

Any smaller family is even easier. Thus the corrected block holds at p=2q-2.
