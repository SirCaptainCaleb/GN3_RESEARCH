# The separated plus-three state at a 2q-3 cut forces adjacent source-path overlap

## Statement

Retain case (P_3) of c9982d3355c8:
  r_i=2q-3,
  r_j=r_{j+1}=q,
and suppose the two exact contact intervals on
  R_i=(g_1,...,g_{2q-4})
are disjoint.

Let c_+ be the later exact contact. Then c_+ is the unique entrance of whichever adjacent parent edge F in {E_j,E_{j+1}} contains it.

Consequently, if F=E_s with s in {j,j+1}, then
  x_s=c_+ belongs to V(R_i)
and
  |V(R_i) intersect V(R_s)|>=2.

## Body

By c9982d3355c8, the later contact c_+ has first occurrence index
  a(c_+)=q-1
and is either the private vertex of g_{q-1} or the joint
  g_{q-1} intersect g_q.

Suppose c_+ were the opposite terminal of its rank-q parent edge F. The stronger opposite-terminal part of the certified singleton-window theorem 49080cbf1371 would give
  a(c_+)<=q-2,
contradicting a(c_+)=q-1. Therefore c_+ is the unique entrance x_s of F=E_s.

Thus x_s lies on R_i. The chosen maximum source path R_s ends at x_s. If R_i and R_s had x_s as their only common vertex, the certified unique-intersection theorem 5854d853a44b would force x_s to be an internal aligned joint of R_s, contradicting that x_s is its last vertex. Hence the two source paths have at least two common vertices.