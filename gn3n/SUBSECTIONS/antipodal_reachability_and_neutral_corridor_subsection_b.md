# Further developments

## Metadata

- ID: antipodal_reachability_and_neutral_corridor_subsection_b
- Parent Section: antipodal_reachability_and_neutral_corridor
- Position: 2
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

### Nearest-violation Tucker labeling

Work in the auxiliary extension (H^+) with distinguished vertex (r). Assume there is no directed one-change spanning order. For a spanning order (pi), let (x_d(pi),y_d(pi)) denote the left-zero and right-one violation indicators at equal distance (d) from (r), as in [[auxiliary_violation_vector_has_exact_chamber_zeros]]. Fix distinct original vertices (a,b) and use the antipodal gauge
[
g_{ab}(pi)=
egin{cases}
+1,&a	ext{ precedes }b,\
-1,&b	ext{ precedes }a.
end{cases}
]
Set
[
F_d(pi)=x_d(pi)-y_d(pi)+g_{ab}(pi)x_d(pi)y_d(pi).
]
Then (F(pi^{m rev})=-F(pi)), and (F(pi)
e0) for every chamber under the present assumption.

Let
[
d(pi)=min{d:F_d(pi)
e0}
]
and define the signed-basis label
[
ell(pi)=operatorname{sgn}(F_{d(pi)}(pi)),e_{d(pi)}.
]
Reversal preserves the distance index and negates the sign, so
[
ell(pi^{m rev})=-ell(pi).
]

If (H) has (n) original vertices, then (H^+) has (n+1) vertices. The centered permutahedron of (H^+) has boundary (S^{n-1}). There are at most (n-2) nontrivial violation distances, so the labels lie in (mathbb R^{n-2}).

For each nonempty proper permutahedron face (C), assign its barycenter the average
[
L(z_C)=rac1{|mathcal V(C)|}sum_{piinmathcal V(C)}ell(pi),
]
and extend affinely over the barycentric subdivision. This gives a continuous odd map
[
L:S^{n-1}	omathbb R^{n-2}.
]
Bourgin--Yang therefore gives
[
dim L^{-1}(0)ge1.
]

Exactly as in the positive-carrier argument for the root maps, every zero has a carrier face (C) and strictly positive coefficients
[
lambda_pi>0qquad(piinmathcal V(C))
]
with
[
sum_{piinmathcal V(C)}lambda_piell(pi)=0.
]

Because the labels are signed basis vectors, coordinate balance is completely explicit.

**Proposition.** For every distance (d) that occurs among the labels of chambers of (C), both (+e_d) and (-e_d) occur among the chamber labels of (C).

**Proof.** In coordinate (d), the positive relation reads
[
sum_{ell(pi)=+e_d}lambda_pi
=
sum_{ell(pi)=-e_d}lambda_pi.
]
If one sign occurs, the corresponding side is positive, so the other side is positive as well. (square)

Let
[
d_0=min{d(pi):piinmathcal V(C)}.
]
Then every chamber of (C) has no violation at any distance (<d_0), while (C) contains chambers labeled (+e_{d_0}) and (-e_{d_0}).

Thus the topological output is no longer a diffuse convex recurrence. It is one ordered-partition face on which all chambers share a common protected radius around (r), and at the first distance where any violation can occur both left and right signs are realized.

### Protected windows force thin blocks

Write the carrier face as an ordered partition
[
C=B_1|cdots|B_k,
]
and let (B_j) be the block containing (r).

For every chamber of (C), every left or right status window at distance (<d_0) from (r) has its prescribed one-change color. Therefore none of those three-position windows can lie wholly in one block of (C): if such a window lay in one block, swapping its first and third vertices would stay in (C) and boundary antisymmetry would flip its status, producing a closer violation in one of the two chambers.

In particular:

**Corollary.** If (d_0ge2), then
[
|B_j|le3.
]

**Proof.** If (|B_j|ge4), choose a chamber in which (r) is last inside (B_j) and three other vertices of (B_j) occupy the three positions immediately preceding (r). Those three positions form the left status window at distance (1<d_0). It is required to be tight in every chamber of (C). Swapping its first and third vertices produces another chamber of (C) in which that triple is its boundary flip and hence non-tight, contradiction. (square)

More generally, every protected three-position window within distance (d_0-1) from (r) must straddle a block boundary of (C). Thus a large protected radius forces a dense sequence of ordered-partition boundaries near (r).

This gives a new global structural alternative:

- either a directed one-change chamber exists, hence a two-cover of (H);
- or there is a proper permutahedron face with a common protected radius, paired opposite nearest-violation labels at the first bad distance, and locally thin ordered-partition blocks around the auxiliary vertex.

The conclusion uses no minimum-counterexample hypothesis and no disturbance analysis.
