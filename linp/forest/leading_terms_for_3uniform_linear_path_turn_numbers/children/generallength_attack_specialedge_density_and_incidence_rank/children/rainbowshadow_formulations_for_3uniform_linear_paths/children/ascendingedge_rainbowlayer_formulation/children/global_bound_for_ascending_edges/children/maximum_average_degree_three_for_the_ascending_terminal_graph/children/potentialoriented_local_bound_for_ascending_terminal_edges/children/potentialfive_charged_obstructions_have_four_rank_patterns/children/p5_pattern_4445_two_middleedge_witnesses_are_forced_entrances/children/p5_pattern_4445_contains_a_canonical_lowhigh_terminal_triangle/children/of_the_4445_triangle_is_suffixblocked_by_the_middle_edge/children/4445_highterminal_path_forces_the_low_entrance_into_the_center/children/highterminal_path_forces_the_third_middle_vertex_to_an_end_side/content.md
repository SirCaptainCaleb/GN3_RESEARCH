# The v-late branch of a 4445 high-terminal path forces the third middle vertex to an end side

## Statement

In the 4445 triangle setting, let g_3={a,b,c}, phi(b)=phi(c)=3, and let
  R=(r_1,...,r_5)
be a five-edge path ending at u_b with v∈r_4.

By 26b4d33bfabe, b is either private in r_3 or b=r_2∩r_3.

Assume g_3 is not itself an edge of R.

(i) If b is private in r_3, then a∈V(r_1∪r_2).

(ii) If b=r_2∩r_3, then a∈V(r_4∪r_5).

Thus, outside the exact coincidence g_3∈E(R), the v-late branch forces the third vertex a of the canonical triangle to a prescribed side of the path according to the central position of b.

## Body

Because g_3 is not an edge of R and r_3 contains b in both alternatives from 26b4d33bfabe, linearity gives
  r_3∩g_3={b}.
Hence c∉r_3.

On a five-edge path, the position-sensitive potential bound for phi(c)=3 allows c only as the private vertex of r_3 or at one of the joints r_2∩r_3, r_3∩r_4. Every such position lies on r_3, so the preceding paragraph excludes all of them. Thus c is absent from V(R).

For (i), suppose b is private in r_3 and a∉V(r_1∪r_2). Since g_3 is not an edge of R and contains b, we have r_3∩g_3={b}. The vertex c is absent from R, and by assumption so is a from r_1∪r_2. Hence g_3 is disjoint from r_1,r_2. Therefore
  (r_1,r_2,r_3,g_3)
is a four-edge linear path. The last edge g_3 is entered through b, while c is a distinct last vertex. This gives phi(c)>=4, contradiction. Hence a∈r_1∪r_2.

For (ii), suppose b=r_2∩r_3 and a∉V(r_4∪r_5). Again r_3∩g_3={b}, and c is absent from R. The path property keeps b out of r_4∪r_5, while the hypothesis keeps a out of those edges. Thus g_3 is disjoint from r_4,r_5. Therefore the reversed suffix
  (r_5,r_4,r_3,g_3)
is a four-edge linear path ending in g_3 through b, with c as a distinct last vertex. This contradicts phi(c)=3. Therefore a∈r_4∪r_5.