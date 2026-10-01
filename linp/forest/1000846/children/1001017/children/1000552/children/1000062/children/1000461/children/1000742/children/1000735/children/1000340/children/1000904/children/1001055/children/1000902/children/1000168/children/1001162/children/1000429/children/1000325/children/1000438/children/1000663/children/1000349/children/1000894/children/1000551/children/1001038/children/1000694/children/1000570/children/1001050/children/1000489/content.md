# Mixed overlapping singleton contacts have two exact boundary forms

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path with last vertex v and last edge g_p. Let
  e_U={x,v,u},   phi(e_U)=r,
  e_X={y,v,z},   phi(e_X)=s
be distinct ascending nonspecial edges terminal at v, neither equal to g_p. Assume each has exactly one off-v contact with V(P)\g_p; the contact of e_U is its opposite terminal u, while the contact of e_X is its unique entrance y. Let I(u),I(y) be their path-edge occurrence intervals.

If I(u) and I(y) overlap, then
  r+s >= p+3.
Moreover, if r+s=p+3, exactly one of the following two configurations occurs.

(O) There is q with p=2q-3 and r=s=q, and on the central host edge g_{q-1},
  u=g_{q-2}∩g_{q-1},
  y=the private vertex of g_{q-1}.

(E) There is q with p=2q-2, s=q, r=q+1, and on the central host edge g_{q-1},
  u=the private vertex of g_{q-1},
  y=g_{q-1}∩g_q.

For the local switching-cell system of 9586a4d2317f, suppose additionally that e_U and e_X are both selected as distinct center-switcher witnesses by the D+Y cellwise injection of c8d14f7306ab. In case (O), at least one of the two adjacent occupied cells C_{q-2},C_{q-1} is paid. In case (E), the common cell C_{q-1} is doubly occupied and paid. Hence, by 39d0d99258db, every equality case forces a nearby switching output edge all of whose vertices have rank at least p.

## Body

Write the three vertices of a host edge g_k as
  A=g_{k-1}∩g_k,
  B=the private vertex of g_k,
  C=g_k∩g_{k+1},
omitting a boundary symbol when it does not exist. Since u and y are distinct vertices and their occurrence intervals overlap, they are two distinct members of {A,B,C} for a common host edge g_k.

The singleton-contact localization 49080cbf1371 gives the following bounds. For the terminal contact u:
- u=A implies p-r+2 <= k <= r-1;
- u=B implies p-r+2 <= k <= r-2;
- u=C implies p-r+1 <= k <= r-2.
For the entrance contact y:
- y=A implies p-s+2 <= k <= s;
- y=B implies p-s+2 <= k <= s-1;
- y=C implies p-s+1 <= k <= s-1.

There are six ordered placements.

1. (u,y)=(A,B). Combining k>=p-r+2 with k<=s-1, or symmetrically k>=p-s+2 with k<=r-1, gives r+s>=p+3. Equality forces
  k=r-1=s-1,
so r=s=q, p=2q-3, and k=q-1. This is (O).

2. (u,y)=(A,C). Here the first occurrence of u is on g_{k-1}, while y=g_k∩g_{k+1} is a clean joint entrance. This is exactly the configuration excluded by the certified clean-joint exclusion eac2e3da3eea, so it is impossible.

3. (u,y)=(B,A). The inequalities k>=p-s+2 and k<=r-2 give r+s>=p+4.

4. (u,y)=(B,C). The inequalities k>=p-r+2 and k<=s-1 give r+s>=p+3. If equality holds, then also the second pair k>=p-s+1 and k<=r-2 is tight, hence
  k=s-1=r-2.
Thus r=s+1. Writing s=q gives p=2q-2 and k=q-1, which is (E).

5. (u,y)=(C,A). Again k>=p-s+2 and k<=r-2 give r+s>=p+4.

6. (u,y)=(C,B). The same two inequalities give r+s>=p+4.

This proves the general classification. In particular, no source-clean hypothesis, paid certificate, minimum-rank terminal assignment, lower bound on the other terminal rank, or near-extremal assumption is needed.

For the switching-cell corollary, use only the local D+Y witness-selection rule from c8d14f7306ab. In (O), the two selected contacts lie in adjacent cells C_{q-2},C_{q-1}. If both cells were unpaid, they would be two consecutive unpaid occupied cells, contradicting the independent-set conclusion of 9586a4d2317f. Hence at least one is paid.

In (E), B and C are the two slots of the same cell C_{q-1}. Both switchers were selected. The c8d14f7306ab cellwise injection selects only one switcher from a doubly occupied unpaid cell, whereas a doubly occupied paid cell contributes two units and hence its two switchers. Therefore C_{q-1} must be paid. It is also a doubly occupied cell, so its two switchers and g_{q-1} form the usual switcher triangle.

Finally, 39d0d99258db identifies a paid cell exactly by the fact that its output edge lies entirely in V_{>=p}. The output is g_q or g_{q+1} in (O), and g_{q+1} in (E). Thus every equality case forces the asserted nearby high-rank output.
