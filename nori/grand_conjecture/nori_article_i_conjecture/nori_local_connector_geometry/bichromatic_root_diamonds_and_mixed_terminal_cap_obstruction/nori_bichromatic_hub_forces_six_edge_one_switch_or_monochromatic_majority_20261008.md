# Bichromatic NORI hubs force a one-switch six-geodesic or uniform minority-color majority triples

# Six-edge one-switch hub connectors from a bichromatic, no-shared-edge middle-square partition

Let n>=7 and c be any ACTIVE NORI ordered physical 3-face coloring in the NO OPPOSITE-COLOR COMMON-EDGE regime (case B of the certified edge-shadow dichotomy). By the bichromatic-hub theorem, choose a physical hub z whose certified middle-pair incident direction sets A,B have colors0 and1, respectively; they are disjoint and |A|,|B|>=2, with at most one isolated remaining direction. By the proved mixed-class middle-selector rigidity, for ANY ordered triple (u,v,w) of distinct directions through z, if the middle direction v is in A or B and either u or w is in the OPPOSITE class, then its physical ordered face color is the bit q(v)=0 for v∈A, 1 for v∈B.

**THEOREM 1 (balanced hub => genuine one-switch length-six geodesic).** If |A|>=3 and |B|>=3, choose three distinct A directions a1,a2,a3 and three distinct B directions b1,b2,b3. Take the six-direction order
  pi=(b1,a1,a2,b2,b3,a3),
and the starting cube root
  x=z xor {b1,a1,a2}.
After three moves this full six-edge direction-distinct geodesic passes through hub z. Its FOUR ordered-three-face windows have actual physical face-color word
  (0,0,1,1).
Indeed every window is a physical three-face through z (the common hub of all length-three windows of a centered length-six geodesic), and the ordered triples and middle directions are
  (b1,a1,a2) middle A =>0,
  (a1,a2,b2) middle A =>0,
  (a2,b2,b3) middle B =>1,
  (b2,b3,a3) middle B =>1;
every triple has adjacent directions from opposite classes. Thus it is a genuine six-edge geodesic with EXACTLY ONE switch. No parity, affine or root-approximation hypothesis is used.

Reversing the A and B roles yields an analogous (1,1,0,0) six-edge path. The result is universal for EVERY bichromatic hub whose two certified direction classes each contain at least3 directions.

**THEOREM 2 (extremely unbalanced hubs have rigid majority triples if there is no six-edge good hub path).** Suppose |B|=2, |A|>=4. Choose ANY ordered triple of distinct directions (a1,a2,a3) in A and an additional a4∈A; let B={b1,b2}. Consider the centered six-edge order
  pi=(a1,a2,a3,b1,b2,a4),
with starting root x=z xor {a1,a2,a3}. Its ordered-three-face word is
   (T,0,1,1),
where T=c(F(z;{a1,a2,a3}),(a1,a2,a3)) is the actual ordered color of the ALL-A triple through z: the remaining three windows have middles a3∈A, b1∈B,b2∈B and contain adjacent mixed-class directions. Therefore T=0 yields a genuine ONE-SWITCH six-edge path.

CONTRAPOSITION: If there is NO six-edge one-switch geodesic centered at this z using only certified directions A∪B, then EVERY ordered triple (a1,a2,a3) of distinct directions entirely in A must have color 1 (the MINORITY color) on the physical triple face through z. The proof holds for all orders of a1,a2,a3 because a4,b1,b2 can always be chosen as above. The symmetric statement holds if |A|=2,|B|>=4: all ordered triple faces through z entirely in majority B must have minority A's color0.

**Interpretation.** In dimensions n>=7, the no-shared-edge regime forces a sharp local dichotomy: either a literal one-switch SIX-edge geodesic exists at the bichromatic hub, OR the hub's certified direction-color classes are unbalanced and the entire ordered-three-face restriction to their majority class is monochromatic in the OPPOSITE color. This is a useful input to long-path reachability: if the majority class has >=6 directions, that second case itself yields fully MONOCHROMATIC SIX-edge geodesics through z in arbitrary six majority directions.

**Scope.** A good length-six geodesic is NOT the full antipodal n-geodesic unless n=6; for n>=7 it may be one or more directions short, and a further extension could introduce another switch. This is a genuine, all-dimension LOCAL connector lemma, not a solution of the grand conjecture. It gives precise rank-six path certificates useful for near-spanning cap and root-profile arguments.
