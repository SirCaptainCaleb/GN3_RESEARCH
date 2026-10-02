# Tight U_11 collisions have half-rank central form outside two explicit low-rank boundary cases

## Statement

Retain an interior U_11 color-terminal collision x_i=v_j on a nondecreasing-rank rainbow terminal-pair path and suppose
  r_j+r_{j+1}<=r_i+2.
Let R_i=(g_1,...,g_{r_i-1}) be the chosen maximum source path ending at x_i, with last edge h.

Then equality holds:
  r_j+r_{j+1}=r_i+2.
Moreover r_i>=4, and exactly the following possibilities remain.

(1) Low-rank even case: r_i=4 and r_j=r_{j+1}=3. The collision closes a local linear 3-cycle. No assertion of two genuine exact off-x_i contacts is made.

(2) Even central case: r_i=2m with m>=3. Then r_j=r_{j+1}=m+1, neither adjacent parent equals h, and both genuine exact contacts c_j,c_{j+1} lie on g_m. Each is one of the backward joint, private vertex, or forward joint of g_m, and the two are distinct. Hence g_m,E_j,E_{j+1} is a linear 3-cycle.

(3) Odd central case: r_i=2m+1 with m>=2, r_j=m+1 and r_{j+1}=m+2. The contact c_j is the joint g_m∩g_{m+1}. If E_{j+1}!=h, its exact contact c_{j+1} lies on g_m or g_{m+1}, and one of those host edges with E_j,E_{j+1} forms a linear 3-cycle. The only possible last-edge boundary is m=2 (r_i=5), E_{j+1}=h; in that case g_3,E_j,h is a linear 3-cycle.

Thus every failure of the plus-three inequality lies at the exact half-rank boundary and still closes a local 3-cycle; the previous two-exact-contact normal form requires the explicit low-rank boundary qualification above.

## Body

The universal collision bound 867efd696575 gives
  r_j+r_{j+1}>=r_i+2,
so equality holds under the hypothesis.

If r_i=2m, the individual bounds in 867efd696575 give
  r_j,r_{j+1}>=m+1.
Equality of the sum forces
  r_j=r_{j+1}=m+1.
If one adjacent parent equals the host last edge h, then its rank equals p=r_i-1=2m-1: the p-edge path R_i ends in h, while 608468bb403b bounds every adjacent parent rank by p. Thus m+1=2m-1, so m=2. Therefore for m>=3 neither adjacent parent is h. In that range m+1<p, so 49080cbf1371 applies to both exact contacts and gives
  a(c)<=m,  b(c)>=m.
Each occurrence interval therefore contains index m, so both contacts lie on g_m; exactness and linearity make them distinct, and g_m,E_j,E_{j+1} is a linear 3-cycle.

It remains to treat m=2, i.e. r_i=4, p=3, r_j=r_{j+1}=3. Since the rank sum is r_i+2 rather than r_i+3, 20ee63fa1617 gives either a local 3-cycle directly or the explicit last-edge boundary. In the boundary case, 3216d2e9afcd gives a local cycle containing the other adjacent parent, whose rank is 3. Every linear cycle has length at least three, while f2925a904b8e bounds this one by 3; hence it is a linear 3-cycle. This proves (1) without asserting two exact contacts.

Now let r_i=2m+1. Equality in the individual bounds from 867efd696575 forces
  r_j=m+1,  r_{j+1}=m+2.
The case m=1 is impossible because c9a012c1b82e bounds both adjacent parent ranks by p=2, while r_{j+1}=3. Hence m>=2.

For E_j, rank m+1 is strictly below p=2m. Its exact contact exists: if E_j=h then h would have rank p, forcing m+1=2m and m=1, already excluded. Applying 49080cbf1371 gives
  a(c_j)<=m,  b(c_j)>=m+1.
Since a path vertex occurs in at most two consecutive path edges,
  [a(c_j),b(c_j)]=[m,m+1],
so c_j=g_m∩g_{m+1}.

If E_{j+1}!=h, both contacts are genuine. Because the rank sum is below r_i+3, 20ee63fa1617 forces the local-3-cycle alternative, so the occurrence interval of c_{j+1} overlaps [m,m+1]. Hence c_{j+1} lies on g_m or g_{m+1}, giving the stated central 3-cycle.

If E_{j+1}=h, then its rank m+2 equals p=2m, so m=2. Thus r_i=5, p=4, r_j=3, and c_j=g_2∩g_3. The boundary cycle of 3216d2e9afcd has length at most r_j=3, hence exactly three; its host segment is g_3,g_4=h, so g_3,E_j,h is the claimed 3-cycle.