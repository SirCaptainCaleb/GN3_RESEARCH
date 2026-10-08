# Convex run extremality forces curvature barriers between long runs — preserved pre-item development

## Composition

(none yet)

## Development

## Convex run extremality forces curvature barriers between long runs

Work in the coboundary-flat pure-orientation sector. Let C be a cyclic full-support order of minimum positive variation in a counterexample, so q(C)=4. Among all four-change cyclic orders, choose C maximizing
[
Phi(C)=r_1^2+r_2^2+r_3^2+r_4^2,
]
where r_1,...,r_4 are the four positive color-run lengths.

### Theorem

If a transition of C is carried by a flat tetrahedron, then at least one of the two color runs incident with that transition has length at most 3.

Equivalently, every transition separating two runs of length at least 4 is fully curved.

### Proof

Let the flat transition separate a left run of length a and a right run of length b, with
[
a,bge4.
]

In the coboundary-flat sector, a flat transition admits both endpoint repairs. By the audited endpoint-repair theorem, either repair weakly decreases cyclic variation. Since C already has minimum possible counterexample variation 4, neither repair can lower variation to 2; both therefore remain four-change cycles.

The corrected transport theorem says a successful right repair deletes the chosen transition and creates a new transition d_R positions to the right, where
[
d_Rin{2,3}.
]
Because b>=4, this target lies strictly inside the same right run, before its next transition. Hence only the two incident run lengths change:
[
(a,b)longmapsto(a+d_R,b-d_R).
]
Therefore
[
Delta_RPhi
=
(a+d_R)^2+(b-d_R)^2-a^2-b^2
=
2d_R(a-b+d_R).
]

Similarly the left repair has some
[
d_Lin{2,3},
]
and because a>=4 it stays inside the left run:
[
(a,b)longmapsto(a-d_L,b+d_L),
]
so
[
Delta_LPhi
=
2d_L(b-a+d_L).
]

If neither repair increased Phi, then
[
a-b+d_Rle0
quad	ext{and}quad
b-a+d_Lle0.
]
Thus
[
b-age d_Rge2,
qquad
a-bge d_Lge2,
]
an impossibility.

Hence one repair produces a four-change cycle with strictly larger Phi, contradicting the choice of C. Therefore a flat transition cannot separate two runs both of length at least 4. QED.

### Interpretation

A Phi-maximal closed repair state has a sharp geometry:
- long-long boundaries are pinned fully-curved universal switches;
- every mobile flat switch is incident with a short run of length 1, 2, or 3.

Thus any closed component of the flat-sector repair graph must be supported in short-run corridors between curvature barriers. The global escape problem reduces to analyzing what happens when a bidirectionally repairable switch repeatedly meets runs of length at most 3, where repairs may cross a neighboring switch and the simple convex transfer formula no longer applies.

This supplies a genuine secondary potential on the part of the repair graph away from switch interactions.
