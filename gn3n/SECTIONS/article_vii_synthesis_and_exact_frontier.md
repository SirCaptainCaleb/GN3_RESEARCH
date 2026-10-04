# Synthesis and the exact topological frontier

**Summary:** Article VII is closed as a geodesic compression route; in a minimum counterexample exact deficiency one forces a canonical Hamiltonian four-support with non-Hamiltonian path-cover-two complement.

## Statement

Article VII gives exact Helly, auxiliary-geodesic, complementary-support, and reachability formulations and closes the geodesic/topological route as a compression mechanism. Recurrent faces have no unbounded residue; and in a minimum counterexample the exact inversion deficiency is one, forcing a canonical Hamiltonian four-support with non-Hamiltonian path-cover-two complement. The exact reachability intersection remains equivalent to the grand conjecture, not a proved theorem.

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


## Metadata

- ID: article_vii_synthesis_and_exact_frontier
- Kind: section
- Version: 13
- Math version: 8
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — crystallized, version 5: Exact formulations and the pre-compression frontier
- Subsection 2 — crystallized, version 3: Closure: width-three mixed-end handoff
- Subsection 3 — crystallized, version 3: Exact-deficiency sharpening of the terminal handoff
- Subsection 4 — HOT, version 1: (untitled)
