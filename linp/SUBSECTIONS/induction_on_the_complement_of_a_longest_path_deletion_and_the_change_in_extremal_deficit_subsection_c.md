# Lemma 3

## Metadata

- ID: induction_on_the_complement_of_a_longest_path_deletion_and_the_change_in_extremal_deficit_subsection_c
- Parent Section: induction_on_the_complement_of_a_longest_path_deletion_and_the_change_in_extremal_deficit
- Position: 3
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Let \(H\) be vertex-minimal among linear \(3\)-graphs satisfying all of the following:

1. \(|E(H)|/|V(H)|\ge d\);
2. \(\delta(H)\ge d+1\);
3. \(H\) contains a fixed nonspecial edge together with a fixed maximum path \(P\) that witnesses its nonspeciality.

Assume in addition that
\[
|E(H)|=d|V(H)|.
\]
Let \(w\notin V(P)\) satisfy
\[
d_H(w)\le d.
\]
Then there is a vertex \(u\ne w\) such that
\[
d_H(u)=d+1,\qquad d_{H-w}(u)=d,
\]
and exactly one hyperedge contains the pair \(\{u,w\}\).

#### Proof
Since \(w\notin V(P)\), deleting \(w\) preserves the fixed path and therefore preserves the specified nonspecial witness. Lemma 2 gives
\[
r_d(H-w)
=
r_d(H)+d_H(w)-d
\le0,
\]
so \(H-w\) still has density at least \(d\).

If \(\delta(H-w)\ge d+1\), then \(H-w\) would satisfy all three defining properties of \(H\), contradicting vertex-minimality. Hence some vertex \(u\) satisfies
\[
d_{H-w}(u)\le d.
\]
Since \(\delta(H)\ge d+1\),
\[
d_H(u)\ge d+1.
\]
Linearity implies that deleting \(w\) removes at most one edge through \(u\), because two distinct hyperedges containing both \(u\) and \(w\) would share two vertices. Therefore
\[
d_H(u)-1\le d_{H-w}(u)\le d.
\]
It follows that
\[
d_H(u)=d+1,\qquad d_{H-w}(u)=d,
\]
and exactly one hyperedge contains \(\{u,w\}\). ∎

Thus deletion of a low-degree vertex outside the witness path produces a specific edge joining it to a degree-\((d+1)\) vertex; it does not by itself contradict minimality.

## Frontier

- Development version when composed: None
- Development version now: 1
