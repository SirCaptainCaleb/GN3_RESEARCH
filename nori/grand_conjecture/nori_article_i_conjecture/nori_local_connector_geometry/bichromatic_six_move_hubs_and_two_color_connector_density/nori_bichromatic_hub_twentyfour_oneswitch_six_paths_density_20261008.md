# At least 24 genuine one-switch six-geodesics at every bichromatic NORI hub; 72 if balanced

# Quantitative centered six-geodesic theorem: at least 24 one-switch paths at every bichromatic hub, 72 if balanced

Work under the hypotheses and notation of nori_unique_edge_shadow_every_bichromatic_hub_has_six_edge_one_switch_20261008: n>=7, valid active NORI physical ordered-three-face coloring, no physical cube edge is certified by monochromatic centered four-geodesic middle squares of BOTH colors, and z is a bichromatic hub with disjoint incident certified-edge direction classes A (color0) and B (color1). Put p=|A|>=2,q=|B|>=2, p+q>=n−1>=6. All six-edge paths below pass through z after exactly three steps, so their four colored windows are genuine physical ordered faces through z.

**THEOREM 1 (balanced exact witness family).** If p>=3 and q>=3, at least
  2 (p)_3 (q)_3
different directed SIX-edge centered antipodal-on-support geodesics have at most one ordered-three-face color change, where (r)_k=r(r-1)...(r-k+1). Specifically for every ordered triple (a1,a2,a3) of A and ordered triple (b1,b2,b3) of B, the direction order
  (b1,a1,a2,b2,b3,a3)
has genuine window word (0,0,1,1), and exchanging A,B gives a distinct order with word (1,1,0,0). Each six-direction order and the prescribed center z uniquely determines its actual start x=z xor {first three directions}; all such orders are distinct, so the count is literal, not weighted. In the minimal p=q=3 case this is 2*6*6=72.

**THEOREM 2 (unbalanced majority-direction density).** Suppose q=2 and p>=4. Let T_A be the set of ordered triples (a,b,c) of distinct elements of A whose physical centered ordered-three-face through z has color0 (the A class's certified color). Then
  |T_A| >= (p)_3/2.
For every triple (a,b,c)∈T_A, every d∈A\{a,b,c}, and both ordered choices (u,v) of the two directions B, the six-edge centered path with direction order
  (a,b,c,u,v,d)
has actual window word (0,0,1,1). Hence there are at least
  2 (p−3)|T_A| >= (p)_4 >=24
different one-switch centered six-geodesics. If p=2,q>=4, interchange A and B, obtaining at least (q)_4 and pattern (1,1,0,0).

**Proof of the density bound.** For ANY four pairwise distinct A directions a,b,c,d, we CANNOT have both of the centered ordered-three-face values c(F_z(a,b,c),(a,b,c))=1 and c(F_z(b,c,d),(b,c,d))=1. Otherwise the four-edge centered direction word (a,b,c,d) is a genuine monochromatic color-1 witness with its middle pair {b,c} in A; its certified physical middle square supplies a color-1 certificate on the incident physical b- and c-edges at z, already certified color0 because b,c belong A. This is forbidden by the no-common-edge assumption. Choose a,b,c,d as a uniformly random ordered four-tuple of distinct A directions. Each of the marginal ordered triples (a,b,c) and (b,c,d) is uniformly distributed over all (p)_3 injective A-triples. Since the event both colors1 is impossible, the expected number of color-1 values among the two triples is at most1. Both marginals have probability 1−|T_A|/(p)_3 of being color1; hence
  2(1−|T_A|/(p)_3)<=1,
which rearranges to |T_A|>=(p)_3/2. QED.

**Universal corollary.** Because p+q>=6, either both >=3 (Theorem1) or one equals2 and the other>=4 (Theorem2). Thus **EVERY bichromatic hub** in the no-common-edge active NORI branch is the center of AT LEAST TWENTY-FOUR distinct honest length-six one-switch directed cube geodesics (with exactly four ordered-three-face windows). In the balanced case at least 72. No affine assumptions, fixed colors on whole facets, or assumed geodesic induction are involved.

**Relation to topology.** These literal rank-six path witnesses provide many actual coherent path states near a certified-square bichromatic hub; they can be used as vertices/cells of a memory-aware higher-dimensional carrier. However their multiple direction orders and starting roots do not automatically concatenate without coordinate repetition, nor is the uniform centered count itself enough to force the exact same-root complementary reversed-tail reachability intersection. This is a robust local multiplicity theorem, not unrestricted grand closure.
