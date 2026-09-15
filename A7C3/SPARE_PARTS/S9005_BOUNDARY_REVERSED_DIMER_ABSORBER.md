# S9005 — Boundary-Reversed Hamilton Dimer Absorber

## Theorem

Let `X` be a finite induced vertex set in a Strong Level-(1) boundary tournament. Suppose there are distinct vertices `u,v in X` and two Hamilton tight paths of `X` with the following boundary states:

- one Hamilton path begins with the ordered dimer `(u,v)`;
- one Hamilton path ends with the reverse ordered dimer `(v,u)`.

Then every exterior vertex `d notin X` Hamilton-extends `X`.

More precisely, boundary antisymmetry makes exactly one of

`(d,u,v)` and `(v,u,d)`

tight. In the first case, prepend `d` to the Hamilton path beginning with `(u,v)`. In the second case, append `d` to the Hamilton path ending with `(v,u)`. Either way `X∪{d}` has a Hamilton tight path.

Thus a Hamilton support carrying opposite orientations of one boundary dimer at its two available ends is a universal one-vertex absorber.

## Proof

Fix an exterior vertex `d notin X`.

Apply Strong Level-(1) boundary antisymmetry to the complete-reversal pair

`(d,u,v)` and `(v,u,d)`.

Exactly one of these ordered triples is tight.

If `(d,u,v)` is tight, take the Hamilton tight path of `X` that begins with `(u,v)` and prepend `d`. Every old consecutive turn remains unchanged and tight, and the only new turn is exactly `(d,u,v)`. Hence the resulting order is a Hamilton tight path on `X∪{d}`.

If instead `(v,u,d)` is tight, take the Hamilton tight path of `X` that ends with `(v,u)` and append `d`. Again every old turn is preserved and the only new turn is the certified turn `(v,u,d)`, so this order is Hamiltonian on `X∪{d}`.

The two cases are exhaustive, proving that every exterior vertex Hamilton-extends `X`. ∎

## Why this is reusable

The lemma turns a very small boundary certificate into universal extension power. It is especially useful when two different Hamilton representatives of one support expose the same physical dimer in opposite orientations at opposite ends. No synchronization of the full Hamilton orders is required.

The statement is order-free and size-free. It uses no smallest-counterexample minimality, deletion cover, transitive-cell structure, extremality, or payment machinery.

## Scope and nonclaims

The extending Hamilton order may depend on the exterior vertex `d`; the theorem does not assert one universal order of `X` that accepts every exterior vertex.

It also does not by itself give a spanning two-cover of a larger tournament. It is a one-vertex absorption certificate for the support `X`.

## Provenance

Rescued from the accepted order-free theorem historically recorded as `R561`. Corpus mining identified `reverse boundary dimer` across 42 source files with 81 uses, and theorem-source review showed that this short absorber is the clean general statement underlying many of those appearances.