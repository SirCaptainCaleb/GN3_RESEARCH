# Every dangerous center pays one-eighth into progress or local obstruction

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path ending at v, and let F be a family of single blockers through v. Restrict to the interior cells C_i={b_i,z_i}, 1<=i<=p-3, and let s_int be the number of blockers whose unique precursor contact lies in these cells.

Let D be the number of cells containing two F-contacts. For every occupied cell C_i let h_i=g_{i+2} be its standard rotation output, and call C_i paid unless h_i is in branch (3) of 6205fe95ecf8, namely
  phi(h_i)=p,
  h_i is nonspecial ascending,
  its unique entrance is the forward joint g_{i+2}∩g_{i+3},
  and that joint has potential p-1.
Let Y be the number of paid occupied cells.

Then
  D+Y >= s_int-ceil((p-3)/2).

Each paid cell has at least one of:
(a) strict rank rise phi(h_i)>p;
(b) a special rank-p output edge;
(c) a nonspecial rank-p output whose forward joint has endpoint potential at least p.

Each doubly occupied cell supports a linear switcher triangle.

Consequently, for the switching family supplied by b032348c1a8a at any active misaligned vertex v of potential p>=8,
  D+Y >= p/8-eta_v-O(1).
Thus every low-defect dangerous center pays linearly into rank rise, specialness, high-potential forward joints, or switcher triangles; the unpaid flat rank-p branch cannot absorb the five-eighths switching density.

## Body

Let C be the number of occupied interior cells. Because each cell has exactly two possible contact vertices and distinct blockers through v have distinct non-v contacts,
  s_int=C+D.                                           (1)

We first show that unpaid cells cannot be consecutive. Suppose C_i and C_{i+1} are both unpaid. Their outputs are the consecutive host edges
  h_i=g_{i+2},  h_{i+1}=g_{i+3}.
Since C_i is unpaid, branch (3) of 6205fe95ecf8 gives that
  x=g_{i+2}∩g_{i+3}
is the unique entrance of h_i and
  phi(x)=p-1.                                         (2)

But C_{i+1} is occupied. The standard p-edge rotation produced from C_{i+1} ends in h_{i+1}=g_{i+3}. By the two-endpoint rotation lemma 465568d6d8dc, the backward joint of this output edge, which is exactly
  g_{i+2}∩g_{i+3}=x,
can be chosen as the last vertex of that p-edge rotation. Hence
  phi(x)>=p,                                          (3)
contradicting (2). Therefore unpaid occupied cells form an independent set in the path of p-3 interior cell positions. If A is their number,
  A<=ceil((p-3)/2).                                   (4)

By definition Y=C-A. Combining (1) and (4),
  D+Y=D+C-A=s_int-A
      >=s_int-ceil((p-3)/2).                          (5)

The classification of a paid cell is exactly the complement of branch (3) in the exhaustive output decomposition 6205fe95ecf8: either the output has rank greater than p; or it has rank p and is special; or it has rank p, is nonspecial nonascending, and its forward joint has potential at least p.

If C_i is doubly occupied, its two contact vertices are b_i and z_i. Let the corresponding blocker edges be f_b,f_z. They meet each other at v, and meet g_i respectively at b_i,z_i; by linearity there are no other pairwise intersections. Since v is outside the precursor edge g_i, the three edges
  g_i,f_b,f_z
form a linear 3-cycle.

Now take F to be the switching family from b032348c1a8a. Boundary positions account for only O(1) switchers, so
  s_int>=|F|-O(1)
       >=(5/8)p-eta_v-O(1).
Substitution into (5) yields
  D+Y >= (1/8)p-eta_v-O(1).
This holds at arbitrary p; no global-top assumption is used.