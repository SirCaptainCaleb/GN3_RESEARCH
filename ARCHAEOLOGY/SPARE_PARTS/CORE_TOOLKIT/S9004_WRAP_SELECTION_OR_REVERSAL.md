# S9004 — Wrap Selection-or-Reversal Lemma

## Theorem

Let

`P=(p_0,p_1,...,p_r)`, `r>=1`,

be a literal tight path in a Strong Level-(1) boundary tournament, and consider the wrap state `p_rp_0`.

If `r=1`, the reversed dimer `(p_1,p_0)` is automatically a tight path.

Assume `r>=2`. Define the two wrap seams

`alpha=(p_r,p_0,p_1)`,

`beta=(p_{r-1},p_r,p_0)`,

and the two cyclic rotations

`P_H=(p_r,p_0,p_1,...,p_{r-1})`,

`P_T=(p_1,...,p_r,p_0)`.

Exactly one of the following four branches holds.

### Double wrap

Both `alpha` and `beta` are tight. Equivalently, both cyclic rotations are tight. In this case

`(p_0,p_1,...,p_r,p_0)`

is a tight Hamilton cycle on `V(P)`.

### Single wrap at the head rotation

`alpha` is tight and `beta` is bad. Then `P_H` is a tight Hamilton path, `P_T` is not, and boundary antisymmetry gives

`(p_0,p_r,p_{r-1})`

tight.

### Single wrap at the tail rotation

`beta` is tight and `alpha` is bad. Then `P_T` is a tight Hamilton path, `P_H` is not, and boundary antisymmetry gives

`(p_1,p_0,p_r)`

tight.

### Double fail

Both `alpha` and `beta` are bad. Then neither rotation is tight, and boundary antisymmetry gives both

`(p_1,p_0,p_r)`

and

`(p_0,p_r,p_{r-1})`

tight. If `r>=3`, these concatenate to the vertex-simple tight reverse `P4`

`(p_1,p_0,p_r,p_{r-1})`.

In particular, a single successful rotation is merely a cyclically shifted Hamilton path. A Hamilton cycle on the displayed support occurs exactly in the double-wrap branch.

## Proof

For `r=1`, a two-vertex path has no internal turn, so its reversal is automatically tight.

Assume `r>=2`. The head rotation `P_H` inherits every old consecutive turn of `P` except for the single new seam `alpha`. Hence `P_H` is tight if and only if `alpha` is tight.

Likewise `P_T` inherits every old turn except `beta`, so `P_T` is tight if and only if `beta` is tight.

The four truth combinations of `(alpha,beta)` are therefore exclusive and exhaustive.

If both are tight, every consecutive triple of the closed cyclic word

`(p_0,p_1,...,p_r,p_0)`

is tight: the internal turns come from `P` and the two wrap turns are exactly `alpha,beta`. Hence this is the double-wrap Hamilton cycle.

If exactly one seam is bad, its complete reversal is tight by Strong Level-(1) boundary antisymmetry, giving the reversed endpoint turn stated in the corresponding single-wrap branch.

If both seams are bad, boundary antisymmetry gives both reversed endpoint turns. When `r>=3`, the vertices `p_1,p_0,p_r,p_{r-1}` are distinct and the two displayed tight triples are consecutive, so they concatenate to the reverse `P4`.

This proves the tetrachotomy. ∎

## Why this is reusable

Many path-cover arguments try to make a named tail-to-head state current by rotating a rail. This lemma gives the complete local ledger: two successful seams produce a Hamilton cycle, one successful seam produces a new Hamilton order plus one exact reversed seam, and total failure produces both reversed endpoint turns.

The distinction between **single wrap** and **double wrap** is important. A successful cyclic rotation alone does not justify cycle language.

The result is order-free and independent of smallest-counterexample minimality, deletion structure, payment machinery, or any particular Engine frame.

## Scope and nonclaims

The theorem changes only the displayed path order. It does not claim that a successful rotation is a distinct cover, that the reverse packet is globally productive, or that the reverse `P4` closes a larger problem by itself.

## Provenance

Rescued initially from the universal path-cover theorem historically recorded as `R548` and strengthened with the exact four-branch refinement historically recorded as `R579`. Citation-graph review showed that the refinement belongs inside the same reusable primitive rather than as a second Spare Part.