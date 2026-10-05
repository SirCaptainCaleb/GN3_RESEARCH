# Antipodal reachability and the neutral corridor

**Summary:** The exact conjecture is an antipodal reachability self-intersection problem, not merely a convex-balance problem.

## Statement

In the auxiliary memory lift, a two-cover exists exactly when the color-1 reachability region intersects its antipodal image. Failure gives an antipodally invariant set meeting every increasing pole geodesic, with forced directed interface colors.

## Cold composition

## Exact reachability and the neutral corridor

### Reachability in the exactified memory lift

Return now to the auxiliary extension \(H^+\) from the fourth Section and work in the single memory-lift copy whose source color is \(1\). Orient every edge from lower rank to higher rank.

Let \(R\) be the set of states reachable from the source pole \(s\) by an increasing path using only color \(1\).

Because the antipodal involution reverses rank and complements color, the antipodal image \(A(R)\) has an exact dual interpretation.

**Proposition 6.** A state \(x\) lies in \(A(R)\) if and only if there is an increasing color-\(0\) path from \(x\) to the target pole \(t\).

**Proof.** A color-\(1\) increasing path from \(s\) to \(y\) maps under \(A\) to a color-\(0\) decreasing path from \(t\) to \(A(y)\). Reversing that path gives a color-\(0\) increasing path from \(A(y)\) to \(t\). The converse is the same argument reversed. \(\square\)

Hence
\[
\boxed{
R\cap A(R)\ne\varnothing
\iff
\Gamma(H^+)\text{ has a directed one-change pole geodesic}.
}
\]

If
\[
x\in R\cap A(R),
\]
concatenate a color-\(1\) increasing path from \(s\) to \(x\) with a color-\(0\) increasing path from \(x\) to \(t\). Rank increases at every step, so the concatenation has pole distance and is automatically geodesic.

Together with auxiliary exactification,
\[
\boxed{
\operatorname{pc}(H)\le2
\iff
R\cap A(R)\ne\varnothing.
}
\]

This is an exact state-space formulation of the original theorem.

### The neutral corridor

Assume
\[
R\cap A(R)=\varnothing
\]
and put
\[
N
=
V(\Gamma)\setminus\bigl(R\cup A(R)\bigr).
\]
Then
\[
A(N)=N.
\]

There is no increasing edge directly from \(R\) to \(A(R)\). Such an edge cannot have color \(1\), since its upper endpoint would then lie in \(R\). It cannot have color \(0\), since its lower endpoint would then have a color-\(0\) route through the upper endpoint to \(t\), placing it in \(A(R)\).

Every increasing pole-to-pole path starts in \(R\), ends in \(A(R)\), and therefore must meet \(N\). Such paths exist from the permutation construction, so \(N\ne\varnothing\). This is separation for increasing paths; the argument does not exclude an undirected edge whose lower endpoint is in \(A(R)\) and upper endpoint in \(R\).

The interface colors are forced:

- every increasing edge from \(R\) to \(N\) has color \(0\);
- every increasing edge from \(N\) to \(A(R)\) has color \(1\).

The antipode exchanges these two frontiers.

Thus failure produces an antipodally invariant set separating every increasing pole geodesic, with prescribed colors at the two directed interfaces. Conversely, disjointness of these particular reachability regions is exactly failure of the directed one-change target.

### Convex balance and actual intersection are different zeros

This distinction is the sharpest way to state the present frontier.

The root construction asks for a convex zero:
\[
0\in\operatorname{conv}\{\phi(\pi):\pi\in\mathcal C\}.
\]
Such a zero says that compressed extreme-defect vectors balance. Through the circulation criterion, it produces recurrence among switch fronts.

Reachability asks for an actual state-space intersection:
\[
x\in R\cap A(R).
\]
Such a point is not an average. It is one concrete memory state simultaneously reachable from the source by one color and from which the target is reachable by the other.

Therefore
\[
\boxed{
\text{root balance}
\neq
\text{reachability self-intersection}
}
\]
without an additional conversion theorem.

The unresolved topological problem may be phrased precisely as:

> Convert the multiplicity or recurrence forced by antipodal root topology into one actual state of the exactified memory lift lying in \(R\cap A(R)\), or into GN3-specific local structure that Articles III–VI can close.

This is more precise than asking vaguely for “a Borsuk–Ulam proof.”

### What a purely topological closure must preserve

Any theorem acting directly on the exactified memory lift must preserve three features simultaneously:

1. **distinguished poles:** the relevant antipodal pair is \(s,t\);
2. **geodesicity:** rank increases at every step, so no original label is reused;
3. **memory:** edge color records three successive cube directions.

A theorem producing an arbitrary antipodal path may fail the first two conditions. A theorem on ordinary cube-edge colorings may fail the third.

A universal directed one-change theorem for boundary tournaments would apply to the auxiliary extension. The undirected one-change conjecture permits either switch direction; it implies the grand conjecture by application to H itself and the cut-and-reverse construction. It does not automatically select the directed target in an individual extension.

Alternatively, work only with the auxiliary extensions and exploit their special vertex together with the consistent triple rule. Antipodal symmetry of arbitrary chamber words alone does not encode that rule.

### How the older topology fits

The earlier Tucker, root, and Bourgin–Yang programs should now be interpreted as candidate mechanisms for attacking the corridor.

- Tucker sought a local complementary state.
- Cellular root topology replaced one complementary edge by balanced recurrence.
- Bourgin–Yang sought enough balanced recurrence to make avoidance impossible.
- GN3-specific compression seeks to turn recurrence into a local reversal or support.

The reachability picture supplies the exact endpoint of that program: all of those mechanisms are useful only insofar as they force
\[
R\cap A(R)\ne\varnothing
\]
or a combinatorial contradiction to the existence of \(N\).

This is the exact topological frontier.


## Further developments

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

## Metadata

- ID: antipodal_reachability_and_neutral_corridor
- Kind: section
- Version: 6
- Math version: 4
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — Exact reachability and the neutral corridor](../SUBSECTIONS/antipodal_reachability_and_neutral_corridor_subsection_a.md) (`antipodal_reachability_and_neutral_corridor_subsection_a`; development v4; composition v1; stale=False)
- [Subsection 2 — Further developments](../SUBSECTIONS/antipodal_reachability_and_neutral_corridor_subsection_b.md) (`antipodal_reachability_and_neutral_corridor_subsection_b`; development v2; composition vNone; stale=True)
