# The mixed plus-three state with owner rank 2q-4 forces a triangle or adjacent source-path overlap

## Statement

Let x_i=v_j be an interior U_11 color-terminal collision on a nondecreasing-edge-rank rainbow terminal-pair path, and suppose
  r_i=2q-4,
  {r_j,r_{j+1}}={q-1,q}.
Let
  R_i=(g_1,...,g_{2q-5})
be the chosen maximum source path ending at x_i, with exact contacts c_j,c_{j+1} of the two adjacent parent edges.

Then at least one of the following holds:

(1) the two exact contact intervals overlap, and some edge of R_i together with E_j,E_{j+1} forms a linear 3-cycle;

(2) one of c_j,c_{j+1} is the unique entrance x_s of its parent edge E_s, with s in {j,j+1}, and
    |V(R_i) intersect V(R_s)|>=2.

More precisely, in the disjoint-contact case the later exact contact is always a unique entrance.

## Body

Put p=2q-5. Since
  (q-1)+q=2q-1=p+4,
the rank-sum inequality of the certified separated-singleton theorem 2cc651f9fa5d is tight whenever the two contact intervals are disjoint.

If the contact intervals overlap, exactness gives a path edge containing both contacts; together with E_j,E_{j+1} it forms the local linear 3-cycle exactly as in 20ee63fa1617. This is (1).

Assume the intervals are disjoint and orient them from the earlier contact c_- to the later contact c_+.

First suppose the earlier contact belongs to the rank-(q-1) edge. Equality in the proof of 2cc651f9fa5d forces
  a(c_-)=p-(q-1)+1=q-3,
  b(c_-)=q-2.
Hence disjointness gives
  a(c_+)>=q-1.
The later edge has rank q, and 49080cbf1371 gives a(c_+)<=q-1. Therefore
  a(c_+)=q-1.
An opposite-terminal singleton contact of a rank-q edge would instead satisfy the stronger bound
  a(c_+)<=q-2.
Thus c_+ is the unique entrance of the rank-q edge.

Now suppose the earlier contact belongs to the rank-q edge. Equality similarly forces
  a(c_-)=p-q+1=q-4,
  b(c_-)=q-3.
Thus the later rank-(q-1) contact satisfies
  a(c_+)>=q-2.
The general singleton bound gives a(c_+)<=q-2, while an opposite-terminal contact would satisfy
  a(c_+)<=q-3.
Therefore again c_+ is the unique entrance of its parent edge.

Write c_+=x_s for that adjacent parent edge E_s. Since x_s belongs to R_i and is the last vertex of the chosen maximum source path R_s, the two paths cannot have x_s as their unique common vertex by 5854d853a44b. Hence
  |V(R_i) intersect V(R_s)|>=2,
proving (2).