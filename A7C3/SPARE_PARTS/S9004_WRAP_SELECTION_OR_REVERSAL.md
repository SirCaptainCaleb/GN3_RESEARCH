# S9004 — Wrap Selection-or-Reversal Lemma

## Theorem

Let

`P=(p_0,p_1,...,p_r)`, `r>=1`,

be a literal tight path component of a path cover in a Strong Level-(1) boundary tournament. Consider the wrap state joining the tail of `P` back to its head,

`p_r p_0`.

If `r=1`, reversing the two-vertex component gives another literal cover of the same cardinality selecting the wrap state.

If `r>=2`, then one of the following holds:

1. the head rotation

   `(p_r,p_0,p_1,...,p_{r-1})`

   is tight;
2. the tail rotation

   `(p_1,...,p_r,p_0)`

   is tight;
3. both new wrap seam turns are bad, in which case boundary antisymmetry forces

   `(p_1,p_0,p_r)` and `(p_0,p_r,p_{r-1})`

   to be tight.

In case 3 the two reversed turns are opposite-end signed terminal-dimer certificates. If `r>=3`, they concatenate to the literal tight path

`(p_1,p_0,p_r,p_{r-1})`.

Thus failure to select the wrap by a cyclic rotation is never silent: it produces an explicit reversed endpoint packet, and for paths of order at least four it produces a tight reverse `P4`.

## Proof

When `r=1`, the component has two vertices and therefore no internal turn condition. Its reversal `(p_1,p_0)` is automatically a tight path.

Assume `r>=2`. The head rotation

`P_H=(p_r,p_0,p_1,...,p_{r-1})`

inherits every old consecutive turn of `P` except for one new turn, namely

`(p_r,p_0,p_1)`.

Hence if this new turn is tight, `P_H` is a tight path on the same support and selects the wrap state `p_rp_0`.

Similarly the tail rotation

`P_T=(p_1,...,p_r,p_0)`

inherits every old turn except for the single new turn

`(p_{r-1},p_r,p_0)`.

If that turn is tight, `P_T` is a tight path on the same support selecting the same wrap state.

Suppose neither rotation is tight. Then both new seam turns are bad. Strong Level-(1) boundary antisymmetry says that the complete reversal of a bad ordered triple is tight. Therefore

`(p_1,p_0,p_r)`

and

`(p_0,p_r,p_{r-1})`

are tight.

These are the exact reversed endpoint turns advertised above. When `r>=3`, the vertices `p_1` and `p_{r-1}` are distinct, so the two tight consecutive turns concatenate to the vertex-simple tight `P4`

`(p_1,p_0,p_r,p_{r-1})`.

This proves the trichotomy. ∎

## Why this is reusable

Many path-cover arguments try to make a named tail-to-head state current by rotating a rail. This lemma packages the entire local obstruction: either a rotation works immediately, or the two failed seams manufacture exact reversed endpoint geometry.

The result is order-free, independent of smallest-counterexample minimality, deletion structure, payment machinery, or any particular Engine frame.

## Scope and nonclaims

The theorem changes only the displayed component and preserves the number of cover components. It does not claim that the rotated cover is new, that the reverse packet is globally productive, or that the reverse `P4` closes a larger problem by itself.

## Provenance

Rescued from the accepted universal path-cover theorem historically recorded as `R548`. The phrase-mining pass repeatedly surfaced reverse-terminal, wrap-seam, and reversed-dimer geometry; this theorem is one of the clean general sources behind that recurring pattern.