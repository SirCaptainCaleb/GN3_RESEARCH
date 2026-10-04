# Synthesis and the exact topological frontier

**Summary:** Nonzero exact-root carriers reduce to four central vertices and directed two- or three-cycles. Projected omission balance forces zero chambers except on two exceptional facets; a matching-block example shows those exceptions are real. The grand conjecture remains open.

## Statement

Article VII retains its exact formulations. Nonzero exact-root carriers have the bounded central configurations of Section 7. For the rooted omission map, strictly positive constant-vector balance forces every chamber to have zero omissions unless all original vertices occupy a single block and the auxiliary vertex is a singleton extreme block. The matching-block tournament on four vertices gives positive balance without a zero chamber on either exceptional facet, refuting the unrestricted facewise omission-balance implication. Converting root configurations or forcing useful omission balance remains open.

## Body

## Exact formulations and the pre-compression frontier

### The exact equivalence chain

The purpose of Article VII is not to replace the local GN3 theory of Articles I–VI. It is to identify the global obstruction geometrically and to translate the original conjecture into exact antipodal models.

The exact chain is
\[
\boxed{
\begin{aligned}
\operatorname{pc}(H)\le2
&\iff
\exists\pi\text{ whose defect intervals admit one common cut}\\
&\iff
H^+\text{ has a directed one-change spanning order}\\
&\iff
\Gamma(H^+)\text{ has a directed one-change pole geodesic}\\
&\iff
\text{the rooted complementary-support condition holds}\\
&\iff
R\cap A(R)\ne\varnothing.
\end{aligned}}
\]

The first line is the quantified defect-Helly theorem. The second is auxiliary exactification. The third is the memory lift. The fourth is the opposite-edge/common-terminal support dictionary normalized at \(r\). The fifth is the reachability criterion.

Every arrow in this chain is exact.

### What topology currently supplies

The root-topological route does not yet prove one of these exact conditions directly. What it supplies is structure:

- the Coxeter sphere of spanning orders;
- antipodal extreme-switch labels;
- cellular square and braid-hexagon constraints;
- the odd root map
  \[
  \phi(\pi)=e_a-e_{\bar b};
  \]
- balanced faces and directed root circulations;
- potentially positive-dimensional balanced loci via Bourgin–Yang;
- block separation, giant-block recurrence, cross-intersection, and front motion.

These are genuine mathematical outputs. They should not be discarded merely because they stop one step short of the theorem.

But they are compressed outputs. The exact target remains one concrete intersection or one exact complementary-support state.

### Route A: prove the stronger one-change conclusion

The candidate from the second Section asks whether every boundary tournament has a spanning order with at most one color change. A reversal-complement function on ordered triples is exactly a boundary tournament, so the candidate concerns the same input class with a stronger desired conclusion.

If this candidate holds, apply it to \(H\) itself and split into monochromatic blocks, reversing the non-tight block. This gives a two-cover. A universal theorem specifically producing \(1^a0^b\) could instead be applied to \(H^+\) and Theorem 3. Reversal preserves the direction of the switch, so these two reductions must be distinguished.

The one-change sufficient condition also gives a tight path on at least \(\lceil(n+2)/2\rceil\) vertices. This quantitative consequence, the endpoint involution including singleton paths, and the positive square-zero enumeration remain part of the support formulation.

A genuinely broader input class is provided by the base-dependent memory rule in the second Section. Any theorem about that class would need a separate proof and a precise reduction.

### Route B: prove only the exact auxiliary target

The alternative is to prove directed one-change existence only for the extensions \(H^+\). This is exactly equivalent to the grand conjecture. One may use the forced endpoint behavior of the auxiliary vertex and the local tournament structure supplied by the triple rule.

Articles I–VI develop deletion-cover compatibility, quadratic-potential descent, defect-line compression, endpoint transport, longest-path reversal structure, and equal-potential recurrence. Article VII seeks to turn topological balance into hypotheses to which those arguments apply. Neither balanced roots nor a moved switch front alone establishes that the full hypotheses of a closing repartition are satisfied.

These are two routes distinguished by the strength of the conclusion and by whether the auxiliary vertex is used, not by a nonexistent distinction between boundary tournaments and reversal-complement triple functions.

### The apparent exact-reachability conversion

Before the minimum-span compression of Section 7, the natural missing implication was
\[
\boxed{
\text{balanced or recurrent extreme-switch data}
\quad\Longrightarrow?\quad
R\cap A(R)\ne\varnothing.
}
\]

That implication is still not proved, and proving it directly would prove the grand conjecture. The neutral-corridor formulation therefore remains a valid optional route to the theorem.

It is no longer, however, the frontier of Article VII. Section 7 shows combinatorially that the recurrence needed to support the balanced face already collapses to bounded local GN3 structure: one minimizes switch span and transports one physical carrier to both extreme fronts. The explicit Bourgin--Yang dimension bound remains a genuine topological statement, but no further conversion of its zero set into a reachability intersection is required for the geodesic investigation itself.

### A cyclic guardrail

One attractive strengthening should be recorded only as a warning.

It is sufficient to find a spanning cyclic order whose transition-color word has at most two monochromatic components, but this is not necessary for a two-cover. There are edge-orderable boundary tournaments with
\[
\operatorname{pc}(H)=2
\]
for which every spanning cycle has at least four monochromatic transition components.

The correct cyclic invariant is not the number of runs.

For an oriented Hamilton cycle
\[
Z=(v_1,\ldots,v_n,v_1),
\]
let the cycle-edge positions be
\[
e_i=\{v_i,v_{i+1}\}.
\]
Construct a defect graph \(D_Z\) on these positions by joining
\[
e_{i-1},e_i
\]
exactly when
\[
(v_{i-1},v_i,v_{i+1})
\]
is non-tight.

A set of cut edges turns the cycle into tight inherited paths exactly when it meets every edge of \(D_Z\). Therefore
\[
\operatorname{pc}(H)
=
\min_Z\max\{1,\tau(D_Z)\}.
\]

In particular,
\[
\operatorname{pc}(H)\le2
\iff
\exists Z\text{ with }\tau(D_Z)\le2.
\]

This exact cyclic formulation may still be useful, but the false two-component-cycle strengthening is not part of the main route.

### Article thesis

Article VII retains the exact Helly, auxiliary-geodesic, complementary-support, and directed-reachability formulations, together with the Coxeter geometry, the failure of graph-only labeling arguments, the explicit barycentric root construction, Bourgin--Yang multiplicity, and carrier-face recurrence.

Its specifically geodesic contribution is now complete at the correct level: recurrent nonzero face geometry and global minimum switch span eliminate every unbounded permutahedral obstruction and hand the problem to bounded local GN3 structure. The article does **not** prove the grand two-cover conjecture, and it does not claim the exact intersection \(R\cap A(R)\ne\varnothing\). Those stronger statements remain equivalent or sufficient routes to the global theorem, while the false cyclic two-component strengthening stays excluded by the balanced-cut obstruction above.


## Closure: width-three mixed-end handoff


### Article VII closure theorem

The exact formulations established earlier remain unchanged:
\[
\operatorname{pc}(H)\le2
\]
is equivalent to the defect-Helly cut condition, to a directed \(1^*0^*\) order in the auxiliary exactification, to the corresponding directed one-change pole geodesic, to the complementary-support formulation, and to
\[
R\cap A(R)\ne\varnothing
\]
in the exact memory lift.

The new compression in Section 7 changes the role of the topological route. It is no longer necessary to synchronize an arbitrary collection of balanced face witnesses into one global reachability state.

**Theorem 9.1 (geodesic compression to a local GN3 interface).** If a boundary \(3\)-tournament \(H\) has no spanning two-cover, then a globally minimum-switch-span spanning order has one of the following forms:

1. its switch span \(d\) satisfies \(3\le d\le5\), and it yields a spanning three-cover with a middle component of order \(d-2\le3\);
2. \(d\ge6\), and \(H\) contains a Hamiltonian support of order four or five.

Moreover, for the positively balanced carrier face of Theorem 6.1, the same conclusion already holds on every non-diagonal recurrent branch: minimum span within the face and one physical carrier eliminate the giant-block/front-motion residue.

Thus all unbounded permutahedral behavior has disappeared. The exact reachability formulation remains mathematically equivalent to the conjecture, but the topology no longer carries an independent unresolved global obstruction.

### Minimum counterexamples have exact width three

There is a sharper consequence in the setting relevant to the grand conjecture.

**Corollary 9.2.** Let \(H\) be a minimum counterexample to the two-cover conjecture. Then the minimum switch span over all spanning orders of \(H\) is exactly three.

**Proof.** Fix \(x\in V(H)\). By minimality,
\[
H-x=P\mid Q
\]
for two tight paths \(P,Q\). Insert \(x\) between their displayed orders:
\[
P,\ x,\ Q.
\]
Every status except the three junction statuses meeting \(x\) is inherited from \(P\) or \(Q\) and is tight. Hence all switches lie across a window of three consecutive variable statuses, so the first-to-last switch span is at most three.

A counterexample has no spanning order with at most one switch, and Lemma 7.5 excludes switch span at most two. Therefore the global minimum is exactly three. \(\square\)

For a minimum-span order with
\[
b=a+3,
\]
Lemma 7.6 becomes especially concrete:
\[
L\mid\{z\}\mid R,
\qquad
z=v_{a+3},
\]
where \(L\) and \(R\) have tight orientations.

The first-switch condition says that \(z\) reverses one exposed end edge of the tight-oriented \(L\); the last-switch condition says that the same \(z\) reverses one exposed end edge of the tight-oriented \(R\). Let \(\alpha,\omega\) be the first and last status colors.

- If \(\alpha\ne\omega\), the two reversals have the same endpoint type. Since the two exposed edges are disjoint, the common-reverser argument gives a Hamiltonian four-support.
- If \(\alpha=\omega\), the reversals have mixed endpoint type. Writing the tight-oriented exposed edges, up to symmetry, as
  \[
  \ldots,a_0,a_1
  \qquad\text{and}\qquad
  p_1,p_2,\ldots
  \]
  gives
  \[
  (z,a_1,a_0),\qquad(p_2,p_1,z)
  \]
  tight. Exactly one of
  \[
  (p_1,z,a_1),\qquad(a_1,z,p_1)
  \]
  is tight. The first gives the Hamiltonian five-path
  \[
  (p_2,p_1,z,a_1,a_0),
  \]
  while the second is the parallel-middle relation
  \[
  (a_1,z,p_1)\ \text{tight}.
  \]

Therefore the geodesic route has a single genuinely local terminal form after bounded Hamiltonian supports are separated off:

\[
\boxed{
\text{width-three singleton carrier with mixed-end parallel-middle data}.
}
\]

This is precisely a local GN3 configuration, not an antipodal-topology problem.

### Final status of the two topological formulations

The root-space formulation and the exact reachability formulation now have different roles.

The root-space topology is **closed as a compression mechanism**: positive balance on every chamber, block separation, and minimum-span carrier transport reduce every nonzero recurrent branch to a two-cover or bounded local structure, while global minimum span absorbs the diagonal branch.

The exact reachability statement
\[
R\cap A(R)\ne\varnothing
\]
remains an exact reformulation of the grand conjecture, not an independently proved theorem. A direct topological proof of that intersection would still solve the conjecture, but Article VII no longer needs such a proof in order to finish its own geodesic investigation. Any hypothetical failure is already compressed to the width-three local interface above.

Accordingly, no further continuation of the antipodal-geodesic, carrier-face, Tucker/Ky Fan, Bourgin--Yang, or neutral-corridor machinery is presently justified. The unresolved mathematics lies in the local GN3 handoff, which belongs to the other articles' path-cover and small-support arguments rather than to Article VII.


## Exact-deficiency sharpening of the terminal handoff


### Exact-deficiency sharpening of the terminal handoff

The exact inversion-window coordinates sharpen the minimum-counterexample conclusion one final step. For
\[
\delta(\pi)=q(\pi)-p(\pi)-1,
\]
the exact criterion of Section 1 says that \(\delta\le0\) is already a two-cover certificate. If \(H\) is a minimum counterexample and
\[
H-x=P\mid Q,
\]
then the order
\[
(P,x,Q^{\rm rev})
\]
has all statuses away from the three \(x\)-junctions equal to \(1\) on the left and \(0\) on the right. Hence \(\delta\le1\); counterexamplehood forces
\[
\delta=1.
\]

The deficiency-one canonical partial cover from Section 6 therefore has a single hole, namely \(x\). Its two displayed tight paths are exactly \(P\) and \(Q\), and \(x\) reverses the terminal edge of both. A common terminal-edge reverser of two disjoint tight paths gives a Hamiltonian four-support. By minimum-counterexample induction its complement is non-Hamiltonian with path-cover number exactly two.

Accordingly the sharp terminal statement of Article VII is
\[
\boxed{
\text{minimum counterexample}
\Longrightarrow
\text{canonical Hamiltonian four-support }K
\text{ with }\operatorname{pc}(H-K)=2
\text{ and }H-K\text{ non-Hamiltonian}.
}
\]

This strictly sharpens the earlier width-three \(4/5\)-support or mixed-end description. The width-three and recurrent-face theorems remain the correct global compression statements for an arbitrary no-two-cover boundary tournament; the exact-deficiency argument is the stronger endpoint available after minimum-counterexample induction.

It also resolves the specific synchronization question raised by the coordinated-face program at the level needed by this article. One may still study directed cycles of exact roots, but Article VII does not need to turn a whole cycle into one reachability intersection. The exact inversion coordinate collapses a minimum counterexample to a one-hole deletion cover before that synchronization is necessary, and the one hole already forces the canonical four-support handoff.

The direct reachability assertion
\[
R\cap A(R)\ne\varnothing
\]
remains equivalent to the grand conjecture and is not proved here. Article VII is closed more modestly and more sharply: the global geodesic/topological obstruction has been eliminated, and the surviving minimum-counterexample state is a single bounded four-support interface.


## The remaining face-to-cover conversion

### Current status of the face-to-cover conversion

The earlier descriptions in this Section of Article VII as closed, and the assertion that no further topological continuation is justified, are superseded by the following precise status. The small-support compression results do not prove a two-cover and do not prove that every obstruction to the grand conjecture has been eliminated. The exact reachability intersection remains unproved.

The bounded-central-block theorem in [[topological_recurrence_to_local_gn3_structure]] gives a uniform reduction within Article VII itself. For a positively balanced exact-root carrier whose chambers all have positive deficiency, either a zero-root chamber occurs or its nonzero-root geometry has one central block of order at most four, exterior blocks of order at most two, at most four consecutive root coordinates, and at most ten actual vertices determining the varying root labels after irrelevant exterior block orders are fixed. The proof uses ordered-partition block freedom and boundary antisymmetry, not minimum-counterexample or disturbance arguments.

This is a finite reduction of one face-geometric branch, not a reduction of the grand conjecture to order ten. Two conversion problems remain. In the diagonal branch, p=c gives equal canonical path lengths but can leave a nonempty hole. In the non-diagonal branch, bounded determining data still have to produce a spanning cover or force a useful change of face.

### Rooted omission vectors

For a spanning order (pi=(L,r,R)) of the auxiliary extension, let (P_pi) be the longest suffix of (L), followed by (r), that is a tight path. Let (Q_pi) be the corresponding rooted path on the right, obtained from the longest initial segment of (R) whose reversal followed by (r) is tight. Define
[
A(pi)=V(L)setminus V(P_pi),qquad
B(pi)=V(R)setminus V(Q_pi),
]
and
[
D(pi)=mathbf 1_{A(pi)}-mathbf 1_{B(pi)}.
]
Reversal exchanges (A) and (B), so (D(pi^{m rev})=-D(pi)). Also (D(pi)=0) exactly when the two rooted tight tails cover every original vertex, which by auxiliary exactification is exactly a spanning two-cover of (H).

Along the chamber order every (D(pi)) has signed threshold form
[
+cdots+,0cdots0, -cdots-.
]
It is never identically positive or identically negative, because an original vertex adjacent to (r) belongs to a two-vertex tight path with (r).

### A dimension-tight quotient map

Let (n=|V(H)|). The boundary of the centered permutahedron on (H^+) is (S^{n-1}). Project the omission vector to
[
mathbb R^{V(H)}/langlemathbf1angle,
]
which also has dimension (n-1). Averaging projected omission vectors on every proper face and extending affinely over the barycentric subdivision gives a continuous odd map. Borsuk--Ulam therefore gives a zero. Its carrier face (F) has strictly positive chamber weights satisfying
[
sum_{piinmathcal V(F)}lambda_pi D(pi)=c,mathbf1
]
for some scalar (c).

This yields a sharper structural frontier:

**Facewise omission-balance problem.** If a proper permutahedral face admits a strictly positive convex combination of rooted omission vectors equal to a constant vector, must it contain a chamber with (D(pi)=0)?

A positive answer proves the two-cover conjecture directly through auxiliary exactification, without minimum-counterexample or disturbance arguments. The extra structure is that each chamber label is a signed prefix/suffix threshold vector of actual omitted vertices and all chambers of (F) arise by independent permutations inside ordered face blocks. The remaining task is therefore an uncrossing or face-convexity problem for threshold omissions inside one ordered partition, not a generic convex-cancellation problem.

The sharper theorem leaves only a two- or four-vertex central block with two singleton witness families supported on the same vertex \(z\), or a three-vertex block with a singleton witness \(\{z\}\) on one side and the full star at \(z\) as the opposite pair family. Moreover, every simple directed root cycle has length two or three. The proof of these sharper bounds sometimes converts a matched pair of tight triples directly into a spanning two-cover; it is therefore stronger than a zero-root argument alone.

The remaining nonzero cases have global deletion distance at most three. This is a consequence under the no-zero-root face hypothesis, not a universal bound on \(\kappa_2(H)\).


### Localization of omission balance and the two exceptional facets

The facewise omission-balance question above has a precise exception. Let the auxiliary vertex be \(r\), let \(V=V(H)\), and use the rooted omission vectors \(D(\pi)\) just defined. In the chamber order their entries on original vertices have the form
\[
+\cdots+,\,0\cdots0,\,-\cdots-.
\]
In particular, if original vertices \(u,v\) lie in distinct ordered face blocks with the block of \(u\) earlier, then
\[
D(\pi)_u\ge D(\pi)_v
\]
for every chamber of that face.

**Proposition (localization to the two exceptional facets).** Let \(F\) be a proper face of the permutahedron on \(V\cup\{r\}\). Suppose
\[
\sum_{\pi\in\mathcal V(F)}\lambda_\pi D(\pi)=c\mathbf1,
\qquad \lambda_\pi>0,\quad \sum_\pi\lambda_\pi=1.
\]
If \(F\) is neither \(\{r\}\mid V\) nor \(V\mid\{r\}\), then \(D(\pi)=0\) for every chamber of \(F\).

**Proof.** If original vertices occur in at least two face blocks, the displayed coordinate inequality and equality of coordinate averages imply
\[
D(\pi)_u=D(\pi)_v
\]
for every chamber and every pair in different original-vertex blocks. Positivity of every coefficient is essential here. Using any vertex in a second block also equates two coordinates in the same block. Thus every chamber vector is constant on all original vertices.

At least one original vertex is adjacent to \(r\) in each chamber and belongs to a rooted tight path of order two. Its omission coordinate is zero. Therefore the constant vector is zero.

If all original vertices occur in one block, a proper face can have only that block and the singleton block \(\{r\}\), in either order. These are exactly the two excluded facets. \(\square\)

Thus, under the assumption that \(H\) has no two-cover, every zero of the projected omission map must have one of the two exceptional facets as its carrier. The Borsuk--Ulam conclusion by itself does not exclude this possibility.

**Example (the exceptional facets really can balance).** Identify four original vertices with \(\mathbb F_2^2\). Order the three nonzero differences as \(d_1<d_2<d_3\), and give the ordinary edge \(\{x,y\}\) the class of \(x+y\). Declare
\[
(x,y,z)\text{ tight}\quad\Longleftrightarrow\quad
\operatorname{class}(x+y)<\operatorname{class}(y+z).
\]
The two classes are different, so boundary reversal complements tightness. This is the matching-block boundary tournament.

It has no tight Hamilton path. Such a path would have three successive, strictly increasing edge classes, hence differences \(d_1,d_2,d_3\). Their sum is zero in \(\mathbb F_2^2\), so its final vertex would equal its initial vertex. This contradicts distinctness. It does, of course, have a two-cover by two pairs.

On the facet \(\{r\}\mid V\), the left rooted path is the singleton \(r\). The right rooted path covers either two or three original vertices; it never covers four because that would give a tight Hamilton path of \(H\). Hence no chamber of this facet has \(D=0\).

Translations of \(\mathbb F_2^2\) preserve edge classes and act transitively on original vertices. The uniform average of \(D\) over all chambers of this facet is therefore a constant vector. Exactly half the orders have a non-tight first original triple, allowing the reversed rooted prefix to cover three original vertices; the other half cover only two. Thus the average number omitted is \(3/2\), and
\[
\frac1{4!}\sum_{\pi\in\mathcal V(\{r\}\mid V)}D(\pi)
=-\frac38\mathbf1.
\]
All weights are strictly positive. Reversal gives the opposite constant on \(V\mid\{r\}\).

This refutes the universal facewise implication proposed above: strictly positive projected omission balance need not yield a zero chamber in the same face. It does not refute the grand conjecture. The viable strengthened target is to force a projected zero outside the two exceptional facets, or to extract a two-cover directly from balance on an exceptional facet. The localization proposition proves the first target sufficient; the example shows why the second cannot demand a Hamilton path.


### Facewise omission balance collapses to the two extreme auxiliary facets

Retain the rooted omission notation
\[
D(\pi)={\bf1}_{A(\pi)}-{\bf1}_{B(\pi)}
\]
on spanning orders \(\pi=(L,r,R)\) of \(H^+\). Thus \(A(\pi)\) is a prefix of \(L\), \(B(\pi)\) is a suffix of \(R\), and \(D(\pi)=0\) is exactly a two-cover certificate for \(H\).

Let
\[
F=C_1|\cdots|C_t
\]
be a nonempty proper permutahedron face, and suppose \(r\in C_j\). Assume there are strictly positive weights
\[
\lambda_\pi>0\qquad(\pi\in\mathcal V(F)),\qquad
\sum_\pi\lambda_\pi=1,
\]
such that
\[
\sum_\pi\lambda_\pi D(\pi)=c\,{\bf1}
\]
for some scalar \(c\).

**Theorem (facewise omission reduction).**
If \(F\) is not one of the two extreme facets
\[
\{r\}|V(H),
\qquad
V(H)|\{r\},
\]
then \(F\) contains a chamber \(\pi\) with
\[
D(\pi)=0.
\]
In fact, except for a terminal two-block configuration with the auxiliary block containing original vertices, the argument forces \(D=0\) in every chamber of \(F\); that remaining terminal configuration also collapses by the probability argument below.

**Proof.**

First suppose
\[
1<j<t.
\]
Every original vertex in a block before \(C_j\) is always left of \(r\), hence its \(D\)-coordinate is in \(\{0,1\}\). Every original vertex in a block after \(C_j\) has coordinate in \(\{0,-1\}\). Since all weighted coordinate averages equal \(c\), both sides force
\[
c=0.
\]
Strict positivity of all \(\lambda_\pi\) then implies that every original vertex outside \(C_j\) has \(D\)-coordinate \(0\) in every chamber.

If some chamber had \(A(\pi)\ne\varnothing\), then, because \(A(\pi)\) is a prefix of \(L\) and there is a whole face block before \(C_j\), the first original vertex of the chamber would lie in \(A(\pi)\), contradicting its identically zero coordinate. Hence \(A(\pi)=\varnothing\) for every chamber. The symmetric suffix argument gives \(B(\pi)=\varnothing\). Thus every chamber has \(D=0\).

Now suppose \(j=1\); the case \(j=t\) is symmetric. Every original vertex outside \(C_1\) has coordinate in \(\{0,-1\}\), so
\[
c\le0.
\]
If \(c=0\), strict positivity makes every outside coordinate identically zero. A nonempty suffix \(B(\pi)\) would contain the last original vertex of the chamber, which lies outside \(C_1\), a contradiction. Thus \(B(\pi)=\varnothing\) for every chamber. The remaining coordinates are then nonnegative, have average zero, and hence \(A(\pi)=\varnothing\) as well.

Assume therefore
\[
c=-W<0.
\]

If \(C_1\ne\{r\}\), choose
\[
x\in C_1-\{r\}.
\]
Let \(E\) be the event, under the positive weights \(\lambda\), that every original vertex outside \(C_1\) belongs to \(B(\pi)\), and write its total weight as \(e\).

For every outside vertex \(y\),
\[
D_y=-{\bf1}_{\{y\in B\}},
\]
so its average \(-W\) gives
\[
\Pr_\lambda(y\in B)=W.
\]
Since \(E\subseteq\{y\in B\}\),
\[
e\le W.
\]

Write
\[
a_x=\Pr_\lambda(x\in A),
\qquad
b_x=\Pr_\lambda(x\in B).
\]
If \(x\in B(\pi)\), the suffix property forces every later outside vertex into \(B(\pi)\), hence
\[
\{x\in B\}\subseteq E
\]
and therefore
\[
b_x\le e.
\]
The balance equation at coordinate \(x\) is
\[
a_x-b_x=-W,
\]
so
\[
b_x=a_x+W\ge W.
\]
Consequently
\[
W\le b_x\le e\le W.
\]
Thus
\[
a_x=0,\qquad b_x=e=W.
\]

The same argument holds for every \(x\in C_1-\{r\}\). Hence on every chamber in \(E\), all original vertices of \(C_1\) and all outside vertices belong to \(B(\pi)\): every original vertex of \(H\) is omitted on the right. This is impossible, because whenever \(R\ne\varnothing\), the first vertex of \(R\) together with \(r\) is a two-vertex tight path, so the rooted right path \(Q_\pi\) always contains at least that vertex.

Thus \(c<0\) is impossible whenever \(C_1\ne\{r\}\).

It remains only
\[
C_1=\{r\}.
\]
If \(t\ge3\), choose vertices \(u\in C_i\), \(v\in C_j\) with
\[
2\le i<j\le t.
\]
Because \(B(\pi)\) is a suffix of \(R\),
\[
{\bf1}_{\{u\in B\}}\le{\bf1}_{\{v\in B\}}
\]
in every chamber. Their weighted expectations are both \(W\), so strict positivity forces equality chamberwise. Varying \(u,v\) shows that in every chamber either every original vertex is in \(B\) or none is. The former is impossible by the immediate-neighbor observation, while the latter contradicts \(W>0\).

Therefore the only unresolved case with \(j=1\) is
\[
F=\{r\}|V(H).
\]
The symmetric argument leaves only
\[
F=V(H)|\{r\}.
\]
This proves the theorem. \(\square\)

### The reduction is sharp at the level of convex cancellation

The two exceptional facets cannot be discarded by a generic convexity argument. On the facet
\[
\{r\}|V(H),
\]
one has
\[
D(\pi)=-{\bf1}_{B(\pi)},
\]
where \(B(\pi)\) is the suffix omitted after the maximal rooted right path.

For a standard non-Hamiltonian four-vertex matching-block boundary tournament, the uniform distribution on all \(24\) permutations gives
\[
\Pr(v\in B)=\frac38
\]
for every vertex \(v\), while no permutation has \(B=\varnothing\). Thus
\[
\frac1{24}\sum_\pi D(\pi)
=
-\frac38\,{\bf1}
\]
is a genuine full-support constant balance with no zero chamber.

Accordingly, the facewise omission theorem is sharp:
\[
\boxed{
\text{all non-extreme carrier faces close;}
\quad
\text{the only genuine convex-cancellation residue is the pair of extreme facets.}
}
\]

The remaining global topological question is therefore whether an odd zero of the quotient omission map can be supported entirely by those two antipodal extreme facets when the whole tournament has no two-cover. Local averaging alone cannot answer this.

### The exceptional facets carry essential degree

The matching-block example above shows that the two exceptional facets can support projected omission balance without a zero chamber. In a hypothetical counterexample, the limitation is stronger: the projected omission map is topologically forced to have a zero in the interior of each exceptional facet.

Let
\[
F^-=\{r\}\mid V(H)
\]
be the left exceptional facet. It is canonically a copy of the centered permutahedron \(P_V\) on the original vertex set, of dimension \(n-1\). Its boundary is therefore an \((n-2)\)-sphere.

On \(F^-\), every omission vector has the form
\[
D(\pi)=-\mathbf 1_{B(\pi)},
\]
where \(B(\pi)\) is a suffix of the original-vertex order. Hence, if
\[
G=B_1|\cdots|B_t
\]
is any proper face of \(P_V\), and \(u\in B_i,\ v\in B_j\) with \(i<j\), then
\[
D(\pi)_u\ge D(\pi)_v
\]
for every chamber \(\pi\) of \(G\). The same inequalities hold for the face-average omission vector assigned to the barycenter of \(G\), and therefore throughout every barycentric simplex whose largest face is \(G\).

Write
\[
Q=\mathbb R^{V(H)}/\langle\mathbf 1\rangle
\]
and, for an ordered partition \(G\), let
\[
C_G=
\left\{
[y]\in Q:
y_u\ge y_v
\text{ whenever }
u\in B_i,\ v\in B_j,\ i<j
\right\}.
\]
Thus the projected omission map on the barycentric subdivision of \(\partial P_V\) is carried by the spherical carrier
\[
K_G=(C_G\setminus\{0\})/\mathbb R_{>0}.
\]

Assume now that \(H\) has no spanning two-cover. By the facewise omission theorem above, the projected omission map has no zero on \(\partial F^-\): any zero there would have a proper nonexceptional carrier face in the full auxiliary permutahedron and would force an actual chamber with \(D=0\).

Each \(K_G\) is contractible. Indeed \(C_G\) is a proper convex cone; after quotienting its lineality space, the pointed part has a spherically convex section, and \(K_G\) is the join of that section with the sphere of the lineality space.

Compare the normalized omission map on \(\partial P_V\) with
\[
h(x)=-\frac{x}{\|x\|}.
\]
If \(x\) lies in the permutahedron face \(G\), then the coordinates of \(x\) increase from earlier to later blocks, so the coordinates of \(-x\) decrease from earlier to later blocks. Therefore
\[
h(G)\subseteq K_G.
\]
The normalized omission map is carried by the same acyclic carrier. The acyclic carrier theorem makes the two maps homotopic.

Consequently
\[
\deg(\widehat D|_{\partial F^-})
=
\deg(h)
=
(-1)^{n-1},
\]
up to the harmless orientation convention for \(Q\). In particular the degree has absolute value one.

Every continuous extension of this boundary map over the exceptional facet \(F^-\) must therefore hit the origin. The barycentric omission map is such an extension, so \(F^-\) contains an interior projected omission zero. Reversal gives the same conclusion for
\[
F^+=V(H)\mid\{r\}.
\]

Thus in a hypothetical counterexample the two exceptional facets do not merely permit topological cancellation:
\[
\boxed{
\text{each exceptional facet carries an essential degree-one omission zero.}
}
\]

This sharpens the limitation of the rooted omission projection. The global Borsuk--Ulam zero can be absorbed by the two extreme facets for a structural degree reason. Therefore a continuation that uses only the same projected omission map and the same quotient target cannot force a useful nonexceptional zero; additional information or a genuinely different target is required.


### The exact violation map escapes the exceptional omission facets

The omission projection fails for a topologically structural reason on the two extreme auxiliary facets, but the exact auxiliary violation vector behaves differently.

Let \(n=|V(H)|\), so the auxiliary tournament \(H^+\) has \(n+1\) vertices and the boundary of its centered permutahedron is
\[
S^{n-1}.
\]
Use the odd violation vector
\[
F(\pi)=(F_d(\pi))_{1\le d\le n-2}
\]
from [[auxiliary_violation_vector_has_exact_chamber_zeros]], where
\[
F_d=x_d-y_d+g\,x_dy_d.
\]
Its chamber zeros are exactly directed one-change orders and therefore exactly two-cover certificates for \(H\).

Average \(F\) over every proper face and extend affinely on the barycentric subdivision. This gives a continuous odd map
\[
\mathcal F:S^{n-1}\longrightarrow\mathbb R^{n-2}.
\]
Bourgin--Yang therefore gives
\[
\dim \mathcal F^{-1}(0)\ge1.
\]
Every zero has the usual positive carrier-face expansion:
\[
\sum_{\pi\in\mathcal V(C)}\lambda_\pi F(\pi)=0,
\qquad
\lambda_\pi>0.
\]

Now consider the exceptional facet
\[
C^-=\{r\}\mid V(H).
\]
Here \(r\) is first in every chamber. There are no left violations, so
\[
x_d=0,\qquad F_d=-y_d\in\{0,-1\}
\]
for every chamber and every distance \(d\). If a positive convex combination of these vectors were zero, every coordinate of every chamber vector would have to vanish. Thus every chamber in the carrier would satisfy
\[
F(\pi)=0,
\]
which is already a directed one-change order and hence a two-cover of \(H\).

Therefore, under the counterexample hypothesis,
\[
\mathcal F^{-1}(0)\cap C^-=\varnothing.
\]
By reversal,
\[
\mathcal F^{-1}(0)\cap C^+=\varnothing,
\qquad
C^+=V(H)\mid\{r\}.
\]

Hence:
\[
\boxed{
\text{if }H\text{ has no two-cover, every zero carrier of the exact violation map is nonexceptional.}
}
\]

This contrasts sharply with the projected omission map, whose two exceptional facets carry essential degree-one zeros. The violation map therefore genuinely escapes Astra's exceptional-facet obstruction.

The remaining gap is different: positive balance of the violation vectors on a nonexceptional face does not yet imply that one chamber has \(F=0\). The next structural target is a facewise conversion theorem for these positional violation vectors, ideally using fixed-center intermediate value and the fact that the zero locus has positive dimension.


### A side-set gauge and exact closure on singleton-\(r\) carrier faces

The coordinatewise gauge in the exact violation vector can be replaced by one global double-violation coordinate in a way that is better adapted to faces.

Let the original vertex set be \(V\), let \(r\) be the auxiliary vertex, and for a spanning order \(\pi\) write
\[
L_r(\pi)=\{v\in V:v\text{ occurs left of }r\},
\qquad
R_r(\pi)=V\setminus L_r(\pi).
\]
Fix once and for all a total order \(\prec\) on subsets of \(V\). Define an antipodal sign \(g_{\rm set}\) by
\[
g_{\rm set}(\pi)=
\begin{cases}
+1,&|L_r(\pi)|<|R_r(\pi)|,\\
-1,&|L_r(\pi)|>|R_r(\pi)|,\\
+1,&|L_r|=|R_r|\text{ and }L_r\prec R_r,\\
-1,&|L_r|=|R_r|\text{ and }R_r\prec L_r.
\end{cases}
\]
Reversal exchanges \(L_r\) and \(R_r\), hence
\[
g_{\rm set}(\pi^{\rm rev})=-g_{\rm set}(\pi).
\]

For the left/right violation bits \(x_d,y_d\) of [[auxiliary_violation_vector_has_exact_chamber_zeros]], define
\[
A_d(\pi)=x_d(\pi)-y_d(\pi),
\]
and choose arbitrary positive weights \(w_d>0\). Put
\[
B(\pi)
=
g_{\rm set}(\pi)\sum_d w_d x_d(\pi)y_d(\pi).
\]
Then
\[
\Theta(\pi)=\bigl((A_d(\pi))_d,B(\pi)\bigr)
\]
is odd. Its target has dimension \(n-1\), equal to the dimension of the auxiliary Coxeter sphere.

Moreover
\[
\Theta(\pi)=0
\]
if and only if \(\pi\) has no violations. Indeed \(A_d=0\) gives \(x_d=y_d\) at every distance, while \(B=0\), since \(g_{\rm set}=\pm1\) and all \(w_d>0\), forces
\[
x_dy_d=0
\]
for every \(d\). Thus \(x_d=y_d=0\) for all \(d\).

Average \(\Theta\) on proper face barycenters and extend affinely. Borsuk--Ulam gives a zero and the usual strictly positive expansion over every chamber of its carrier face.

The key advantage of \(g_{\rm set}\) is the following.

**Theorem (singleton-\(r\) carrier conversion).**
Let
\[
C=C_1|\cdots|C_t
\]
be a proper permutahedron face in which
\[
C_j=\{r\}.
\]
Suppose there are strictly positive weights
\[
\lambda_\pi>0\qquad(\pi\in\mathcal V(C))
\]
with
\[
\sum_\pi\lambda_\pi\Theta(\pi)=0.
\]
Then every chamber of \(C\) is violation-free. In particular \(H\) has a spanning two-cover.

**Proof.**
Because \(r\) is a singleton block, the set of original vertices left of \(r\) and the set right of \(r\) are fixed throughout \(C\). Hence
\[
g_{\rm set}(\pi)=g_0\in\{\pm1\}
\]
is constant on all chambers of \(C\).

The last coordinate of the positive balance is therefore
\[
0
=
g_0\sum_\pi\lambda_\pi\sum_d w_dx_d(\pi)y_d(\pi).
\]
Every summand inside the last sum is nonnegative, every \(w_d\) is positive, and every \(\lambda_\pi\) is positive. Hence
\[
x_d(\pi)y_d(\pi)=0
\]
for every chamber \(\pi\) and every distance \(d\).

Now fix \(d\). Since \(r\) is a singleton block, the chamber set factors as
\[
\mathcal V(C)
=
\mathcal L\times\mathcal R,
\]
where \(\mathcal L\) consists of the independent permutations in blocks left of \(r\), and \(\mathcal R\) those right of \(r\). The bit \(x_d\) depends only on the left factor and \(y_d\) only on the right factor.

If some left factor had \(x_d=1\) and some right factor had \(y_d=1\), their product chamber would satisfy
\[
x_dy_d=1,
\]
contrary to the preceding paragraph. Therefore at least one of the two functions is identically zero on its factor.

But the \(A_d\)-coordinate of the positive balance says
\[
\sum_\pi\lambda_\pi x_d(\pi)
=
\sum_\pi\lambda_\pi y_d(\pi).
\]
If one side is identically zero, positivity forces the other side to be identically zero as well. Hence
\[
x_d(\pi)=y_d(\pi)=0
\]
for every chamber. Since \(d\) was arbitrary, every chamber of \(C\) is violation-free. \(\square\)

Thus the exact violation map has no unresolved singleton-\(r\) carrier geometry at all:
\[
\boxed{
\text{positive }\Theta\text{-balance on a face with }\{r\}\text{ as a block}
\Longrightarrow
\text{an actual two-cover certificate}.
}
\]

Consequently, under the counterexample hypothesis, every zero carrier of the \(\Theta\)-map must place \(r\) in a block containing at least one original vertex. This eliminates the central singleton case as well as the two extreme singleton facets; the only remaining face-to-cover obstruction is genuinely the geometry of a nontrivial \(r\)-block.


## Metadata

- ID: article_vii_synthesis_and_exact_frontier
- Kind: section
- Version: 25
- Math version: 17
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — crystallized, version 5: Exact formulations and the pre-compression frontier
- Subsection 2 — crystallized, version 3: Closure: width-three mixed-end handoff
- Subsection 3 — crystallized, version 3: Exact-deficiency sharpening of the terminal handoff
- Subsection 4 — HOT, version 10: The remaining face-to-cover conversion
