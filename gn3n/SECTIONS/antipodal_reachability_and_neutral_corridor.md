# Antipodal reachability and the neutral corridor

**Summary:** The exact conjecture is an antipodal reachability self-intersection problem, not merely a convex-balance problem.

## Statement

In the exactified memory lift, the theorem is equivalent to intersection of a red reachability region with its antipodal image; failure produces an antipodally invariant separating neutral corridor.

## Body

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

Since the ranked graph connects the poles, every pole-to-pole path must therefore meet \(N\). In particular \(N\ne\varnothing\).

The interface colors are forced:

- every increasing edge from \(R\) to \(N\) has color \(0\);
- every increasing edge from \(N\) to \(A(R)\) has color \(1\).

The antipode exchanges these two frontiers.

Thus a counterexample is equivalent to the existence of an antipodally invariant separating corridor with prescribed opposite colors on its lower and upper boundary.

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

The candidate memory-two geodesic conjecture from the second Section is one clean way to package all three requirements. If it is proved, the corridor is impossible in every reversal-complement memory coloring, not merely in GN3.

The alternative is to prove that the corridor cannot coexist with the additional local tournament structure of a boundary tournament.

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


## Metadata

- ID: antipodal_reachability_and_neutral_corridor
- Kind: section
- Version: 3
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — crystallized, version 3: Exact reachability and the neutral corridor
- Subsection 2 — HOT, version 1: Further developments
