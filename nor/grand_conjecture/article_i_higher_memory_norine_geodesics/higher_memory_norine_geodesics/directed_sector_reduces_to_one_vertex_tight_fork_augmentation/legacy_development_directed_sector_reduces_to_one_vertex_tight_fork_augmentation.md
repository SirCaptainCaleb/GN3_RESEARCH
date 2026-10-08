# Directed sector reduces to one-vertex tight-fork augmentation — preserved pre-item development

## Composition

(none yet)

## Development

## Directed sector: reduction to one-vertex tight-fork augmentation

Let \(r\ge2\) be the arity of a translation-invariant coordinate label
\[
h(v_1,\ldots,v_r),
\qquad
h(v_r,\ldots,v_1)=1-h(v_1,\ldots,v_r).
\]
Under the tuple-arity convention this is the directed sector of \(N_{r+1}\).

Assume there is a counterexample on a ground set \(V\) of minimum size \(n\). Fix \(x\in V\). By minimality, \(V\setminus\{x\}\) has a one-change coordinate order. After naming its initial color \(\sigma\), write the word as
\[
\sigma^p(1-\sigma)^q.
\]
Endpoint blocking forces \(p,q\ge1\).

Using the converging-tight-fork formulation with center an ordered \((r-1)\)-tuple \(S\), the deletion order gives two color-\(\sigma\) tight branches
\[
P=A,S,
\qquad
Q=B,S^{\rm rev},
\]
with
\[
V=A\,\dot\cup\,B\,\dot\cup\,S\,\dot\cup\,\{x\},
\]
and with both \(A\) and \(B\) nonempty.

Let \(F_P,F_Q\) be the first ordered \((r-1)\)-tuples of the two branches. The two endpoint-blocking identities become
\[
h(x,F_P)=h(x,F_Q)=1-\sigma.
\]
By reversal antisymmetry,
\[
h(F_P^{\rm rev},x)=h(F_Q^{\rm rev},x)=\sigma.
\]

Thus every minimum counterexample in the directed translation-invariant sector yields, for every deleted vertex \(x\), a near-spanning fork with exactly one uncovered vertex satisfying four simultaneous terminal constraints:

- both branches are nontrivial;
- \(x\) cannot be prepended to either branch in color \(\sigma\);
- \(x\) is a color-\(\sigma\) right-extension of the reversed outer front of each branch.

### Closure target

It is therefore enough to prove the following one-vertex augmentation theorem in the directed sector:

> A color-\(\sigma\) converging tight fork covering \(V\setminus\{x\}\), with both branches nontrivial and with
> \[
> h(x,F_P)=h(x,F_Q)=1-\sigma
> \]
> (equivalently \(h(F_P^{\rm rev},x)=h(F_Q^{\rm rev},x)=\sigma\)),
> can be recentered or exchanged to a spanning converging tight fork.

This is materially narrower than arbitrary maximal-fork augmentation: minimum counterexample analysis reduces the uncovered set to one vertex and supplies a symmetric pair of reverse-front extension identities.
