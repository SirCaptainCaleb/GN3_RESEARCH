# S9001 — Reverse-Ear Lemma

## Theorem

Let

`P=(v_0,...,v_k)`

and `K` be vertex-simple tight paths in a finite Strong Level-(1) boundary tournament. Let `E` be a `K`-subpath from `v_i` to `v_j` such that `v_i,v_j` are consecutive contacts of `K` with `P`, so every internal vertex of `E` lies outside `P`, and suppose `i>j`.

Then one of the following occurs:

1. `E` is the single state `v_i v_j` with `i=j+1`, so `K` contains the exact reversal of the old `P`-state `v_j v_i`;
2. one of the two `P/E` seams yields a tight reverse trimer; or
3. `E` together with the old `P`-segment from `v_j` through `v_{i-1}` forms a vertex-simple proper tight cycle.

Consequently, outside these explicit outputs, the vertices of `P` encountered along any tight path `K` occur in increasing `P`-order.

## Proof

Let `E` run from `v_i` to `v_j`, with no internal vertex of `E` on `P`, and assume `i>j`.

If `E` is the single state `v_i v_j` and `i=j+1`, then this state is exactly the reversal of the old adjacent state `v_j v_i` of `P`, giving the first output.

Otherwise let `x` be the successor of `v_i` on `E` and `y` the predecessor of `v_j` on `E`. In the one-state nonadjacent case, `x=v_j` and `y=v_i`. Because `i>j`, both `v_{i-1}` and `v_{j+1}` exist. Test the two seams

`(v_{i-1},v_i,x)` and `(y,v_j,v_{j+1})`.

If the first seam is bad, boundary antisymmetry makes

`(x,v_i,v_{i-1})`

tight, a reverse trimer. If the second seam is bad, boundary antisymmetry makes

`(v_{j+1},v_j,y)`

tight, again a reverse trimer.

Suppose instead that both seams are tight. Traverse `E` from `v_i` to `v_j`, then follow the old `P`-segment

`v_j,v_{j+1},...,v_{i-1}`,

and close back to `v_i` through the first tested seam. Every turn of the resulting closed walk lies either on `E`, on `P`, or is one of the two tested seams. Because the internal vertices of `E` avoid `P`, the resulting tight cycle is vertex-simple. This gives the third output.

Thus every reverse-order encounter between consecutive `K`-contacts with `P` produces one of the stated certificates. If none occurs, no such reverse-order pair exists, so all `P`-contacts appear along `K` in increasing `P`-order. ∎

## Same-support corollary

Let `P` and `Q` be vertex-simple tight Hamilton paths on the same vertex set. If their literal orders differ, then either:

- `Q` contains the exact reversal of an adjacent state of `P`;
- there is a tight reverse trimer at a comparison seam; or
- there is a vertex-simple proper tight cycle.

Indeed, read the vertices in `P`-order along `Q`. If the resulting permutation is not the identity, it has a descent. Choose a descent between consecutive `Q`-contacts and apply the theorem.

This is the reusable form behind same-support representative-rigidity arguments and exact-cover order comparisons.

## Scope and persistence

This is a pure Strong Level-(1) path-interaction theorem. It assumes no smallest-counterexample minimality, completion theorem, boundedness, selected-state persistence, or contradiction-from-cycle principle.

The reversal state, reverse trimer, and proper cycle are graph-intrinsic once exhibited. The theorem does **not** assert that either input path remains selected in a later cover, nor that a proper tight cycle is itself contradictory.

## Proof-design warning

A bare Reverse-Ear output is often too cheap to count as progress. Given any tight path containing three chosen vertices, two of the three possible middle-labelled tight trimers on those vertices necessarily disagree with the path order and therefore trigger this theorem. Thus a useful application should retain some non-generic coordinate, for example:

- a prescribed cap or boundary state;
- a named source adjacency;
- a deletion-fiber or representative role;
- a distinguished historical edge; or
- a downstream physical proposal that consumes the particular reversal, trimer, or cycle.

In other words, Reverse-Ear is a powerful **local interaction primitive**, not by itself a global descent theorem.

## Provenance

Rescued from the accepted general result historically recorded as `R435` (Reverse Ear Lemma). The proof-design warning records the accepted ubiquity observation historically isolated as `R483`. The same-support corollary is the form repeatedly used in later exact-cover comparison arguments, including the E8998 composition.