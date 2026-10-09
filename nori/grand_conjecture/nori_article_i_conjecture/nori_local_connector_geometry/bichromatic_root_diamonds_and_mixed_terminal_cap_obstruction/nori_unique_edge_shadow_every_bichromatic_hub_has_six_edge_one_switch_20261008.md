# No-shared-edge NORI forces a genuine six-edge one-switch geodesic at every bichromatic hub

# Universal one-switch SIX-geodesic at every bichromatic hub in the unique-certified-edge regime

Assume n>=7 and c is a valid ACTIVE NORI ordered-three-face coloring on Q_n, with **NO physical cube edge** contained in monochromatic centered-connector squares of BOTH colors. The unconditional bichromatic-hub theorem gives a cube vertex z supporting genuine centered monochromatic four-edge connectors of both colors. Let A=A(z), B=B(z) denote incident direction sets whose certified center-square edge colors are 0 and 1, respectively. Then A and B are disjoint, |A|,|B|>=2, and the certified-center-square link theorem implies at most one isolated direction, hence |A|+|B|>=n-1>=6. The mixed-class physical-face selector lemma nori_bichromatic_hub_shadow_mixed_triple_middle_selector_rigidity_20261008 says that when a triple of directions through z has its middle member in A or B and at least one adjacent member in the opposite class, the actual ordered-three-face color equals that of the middle direction.

**THEOREM (the unbalanced obstruction is impossible).** Every such hub z lies on a genuine SIX-EDGE directed cube geodesic with EXACTLY ONE switch among its four ordered-three-face window colors. More explicitly, the direction list may be selected to yield actual color word (0,0,1,1) or (1,1,0,0). Its six directions are distinct, the path passes through z after its first three steps, and all its four colored three-faces physically contain z.

**Proof, balanced case.** If |A|,|B|>=3, select a1,a2,a3∈A and b1,b2,b3∈B, distinct. The direction word
 (b1,a1,a2,b2,b3,a3)
has four consecutive three-direction windows with middle directions (a1,a2,b2,b3), each adjacent to an opposite-class direction. Therefore their actual window colors through the common midpoint z are 0,0,1,1.

**Proof, unbalanced case.** As |A|+|B|>=6, if one class has size2, the other has size>=4. Suppose |B|=2, |A|>=4; the other case is symmetric. Pick ANY four distinct A directions a1,a2,a3,a4. Their centered four-edge direction word (a1,a2,a3,a4) has two window colors
  t1=c(F_z(a1,a2,a3),(a1,a2,a3)),
  t2=c(F_z(a2,a3,a4),(a2,a3,a4)).
If BOTH were 1, the centered path would be an honest monochromatic color-1 four-edge witness, certifying the physical square Q(z;a2,a3) with color1. In particular its two incident edges in directions a2 and a3 at z would carry color-1 certificates. But a2,a3∈A, so those SAME physical incident edges already carry color-0 certificates. This violates the NO BICHROMATIC COMMON PHYSICAL EDGE hypothesis. Therefore t1=0 or t2=0.

Consequently SOME ordered triple of three distinct A directions has actual color0; call that triple (a,b,c), and choose an unused fourth A direction d. Let B={u,v}. The six-edge order
 (a,b,c,u,v,d)
has four window colors exactly
  (0,0,1,1).
The first triple has color0 by selection. Each of the other three ordered triples has middle direction c∈A, u∈B, or v∈B with an adjacent opposite-class direction, so the selector lemma gives 0,1,1. Start the path at x=z xor {a,b,c}, reaching z after three steps; all four windows physically contain z. This is a genuine length-six one-switch geodesic. If |A|=2 and |B|>=4 interchange labels to obtain a (1,1,0,0) geodesic. QED.

**Corollary (rank-six root incidence).** At ANY bichromatic hub in the no-shared-edge case, there is a certified ordered six-direction support W and a physical root x (distance three from z) such that the actual directed monochromatic-prefix / one-switch six-edge path from x to x xor W has exactly one switch in its four-window color word. The construction is color-physical, not a convex-hull label, and remains valid for arbitrarily nonlinear dependence on exterior face bits.

**Why this matters and what it does not solve.** The earlier nori_bichromatic_hub_forces_six_edge_one_switch_or_monochromatic_majority_20261008 gave an apparent exceptional case of a large class with EVERY all-majority triple in the minority color. That case is now **contradicted** by the unique-color physical edge certificates, because any four majority directions would give a minority-colored square on a majority-certified edge. Thus the positive six-edge one-switch alternative is UNCONDITIONAL inside the no-bichromatic-edge branch. This still does not solve unrestricted NORI: for n>6 the geodesic does not span all directions, and appending unused directions can introduce extra color switches. The other branch (a bichromatic certified common edge) requires a different extraction/extension lemma.
