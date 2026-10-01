# Deficiency-two sink fans form alternating blocker systems with defects pinned at x

## Statement


Let H be a linear 3-graph of minimum degree q, let P=(p_1,...,p_{q-2}) be a linear path ending at x, let u,v be the two opposite last vertices of p_1, and let y,z lie outside V(P). Suppose both u and v are safe sinks: neither admits a safe clean extension avoiding y,z nor a safe single-blocker rotation avoiding y,z.

For each sink r in {u,v}, its endpoint fan has degree exactly q and exactly one of three forms:
(i) C=1,S=2,D=q-4, with one X-type singleton and one singleton through the other terminal;
(ii) C=2,S=0,D=q-3, with clean y- and z-edges;
(iii) C=2,S=1,D=q-4, with clean y- and z-edges and one X-type singleton.

Let W=V(P)\p_1 and let M_r be the matching on W whose edges are the blocker pairs of double-blocking edges through r. Then M_u and M_v are edge-disjoint. Each M_r is either perfect, or has exactly two unmatched vertices, one of which is x. Hence M_u union M_v is a disjoint union of alternating cycles together with at most one nontrivial alternating path after the common x-defect is accounted for:
- if both matchings are perfect, only cycles occur;
- if exactly one is imperfect, there is one alternating path from x to its secondary defect;
- if both are imperfect, x is isolated and there is at most one alternating path joining the two secondary defects.


## Body


Fix one sink endpoint r. Let C,S,D be the numbers of clean, single-blocking, and double-blocking edges through r other than p_1. The endpoint-deficiency inequality gives
  C+S+D=d_H(r)-1,
  S+2D<=2q-6,
  2C+S>=4.
Since there is no safe clean extension, every clean edge contains y or z, so C<=2. Since there is no safe single-blocker rotation, each singleton blocker is exceptional: its blocker is x or its edge contains y or z. If a clean y-edge exists, no singleton edge through r can also contain y by linearity; similarly for z. Writing C_y,C_z in {0,1}, this gives
  S<=1+(1-C_y)+(1-C_z)=3-C.

Thus C<=2, S<=3-C and 2C+S>=4 force C>=1. If C=1, then S=2. The unique clean edge contains, say, y; the two possible singleton types are then exactly X and Z. Hence
  C=1,S=2.
The degree and blocker-capacity inequalities give D=q-4 and d_H(r)=q.

If C=2, the clean y- and z-edges both occur. Every singleton must then be X-type, so S is 0 or 1. If S=0, the same equalities force D=q-3 and d_H(r)=q. If S=1, they force D=q-4 and d_H(r)=q. Moreover the number of unused blocker vertices in W is
  (2q-6)-(S+2D),
which is 0 in the first two cases and 1 in the third. This proves the exact three-form sink classification.

Now consider both opposite sink endpoints u and v. For fixed r, distinct hyperedges through r have disjoint blocker sets outside r, so the double-blocker pairs form a matching M_r on W. If the same pair {a,b} belonged to M_u and M_v, the corresponding hyperedges {u,a,b} and {v,a,b} would share two vertices, contradicting linearity. Thus M_u and M_v are edge-disjoint.

The exact sink classification determines the unmatched vertices of each M_r. In case (ii), D=q-3 and |W|=2q-6, so M_r is perfect. In case (i), D=q-4 and the two unmatched blocker vertices are x and the blocker of the non-X terminal singleton. In case (iii), D=q-4; the unique X-singleton uses x and there is exactly one further uncovered blocker vertex, so again the unmatched vertices are x and one secondary defect. Therefore every M_r is perfect or has exactly two defects, one pinned at x.

The union M_u union M_v has maximum degree at most two and alternates the two matching colors along every nontrivial component. Hence every component is an alternating cycle or path. The pinned defect description makes the possibilities exact.

If both matchings are perfect, every component is an alternating cycle. If exactly one is imperfect, exactly two degree-one defects occur, namely x and that matching's secondary defect, so there is exactly one open alternating path joining them. If both are imperfect, x is unmatched in both and is therefore isolated in the union; away from x only the two secondary defects can have degree one, so there is at most one nontrivial alternating path joining them, with the degenerate possibility that the two secondary defects coincide.

Thus all two-endpoint deficiency-two sink complexity reduces to alternating cycles and at most one open chain, with every open defect forced to x or one of at most two secondary vertices.
