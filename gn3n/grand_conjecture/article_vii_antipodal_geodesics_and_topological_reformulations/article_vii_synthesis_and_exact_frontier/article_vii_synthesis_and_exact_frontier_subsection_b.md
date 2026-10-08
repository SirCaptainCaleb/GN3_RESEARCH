# Closure: width-three mixed-end handoff


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
