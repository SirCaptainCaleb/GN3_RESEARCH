# Ternary path-system insertion theorem

**Status: GN3 AUDIT PASS.**

This module concerns a reversal-symmetric ternary path system rather than a boundary tournament. Its exact mathematical text passed independent GN3 audit in the toolkit batch at snapshot `99e9c98a80d3d0cefcffef343fb67a6f973ee432`.

Let `V` be a finite set and let `E` be a set of ordered triples of distinct vertices. Call a vertex sequence **tight** when every consecutive ordered triple belongs to `E`.

Assume the following two properties.

1. For every three distinct vertices `u,v,w`, at least one of `(u,v,w)` and `(w,u,v)` belongs to `E`.
2. Reversal symmetry holds: `(u,v,w) in E` if and only if `(w,v,u) in E`.

## Theorem. Every exterior vertex has two insertion positions

Let

`P=(v_0,...,v_{k-1})`

be a tight path and let `x notin V(P)`. Then at least two of the `k+1` positions obtained by inserting `x` into the displayed order of `P` give a tight path.

Consequently every `n`-vertex system satisfying the two assumptions has at least

`2^(n-1)`

Hamilton tight paths.

This bound is sharp.

**Proof.** Fix an adjacent pair `v_i,v_{i+1}` of `P`. On the three-set `{x,v_i,v_{i+1}}`, reversal symmetry means that tightness depends only on which vertex is in the middle. Let

`q_y=1`

when the two reverse orders having middle vertex `y` are tight. Applying the first axiom to the three cyclic choices gives

`q_x or q_{v_i}`,

`q_{v_i} or q_{v_{i+1}}`,

`q_{v_{i+1}} or q_x`.

Hence at most one of the three values `q_x,q_{v_i},q_{v_{i+1}}` is zero.

The adjacent pair `v_i,v_{i+1}` can therefore forbid at most one insertion position: immediately before `v_i`, between `v_i,v_{i+1}`, or immediately after `v_{i+1}`, according to which middle vertex is the unique forbidden one. Every new triple created by inserting `x` is associated with one adjacent pair of `P`. Thus the `k-1` adjacent pairs can forbid at most `k-1` of the `k+1` insertion positions. At least two positions remain tight.

For the counting statement, fix a vertex `x`. Every Hamilton tight path on `V-{x}` has at least two insertions of `x`, and deleting `x` from a resulting path recovers both the parent path and the insertion position. Hence, if `N(V)` denotes the number of Hamilton tight paths,

`N(V)>=2N(V-{x})`.

Starting from `N=1` on one vertex gives `N(V)>=2^(n-1)`.

For sharpness, fix a total order on `V` and declare `(a,b,c)` tight exactly when `b` is not the largest of `{a,b,c}`. The two axioms hold. A Hamilton ordering is tight exactly when it has no interior local maximum. Such an ordering decreases to the minimum element and then increases. It is determined uniquely by choosing which of the other `n-1` vertices lie to the left of the minimum, so there are exactly `2^(n-1)` Hamilton tight paths. ∎

## Legacy provenance

This theorem rewrites A7C3 `S9016`.