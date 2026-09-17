# S9002 — Punctured Component-Drop Pair Theorem

## Theorem

Let `H` be a finite Strong Level-(1) boundary tournament, and let `W` be a proper subset of `V(H)`. Suppose `H[W]` has two literal path covers

`R = R_1 | ... | R_c`

and

`T = T_1 | ... | T_r`

with `r<c`. Then `H` contains a graph-intrinsic balanced opposite-sign pair.

Equivalently: whenever the same proper induced subsystem is represented once with `c` path components and once with fewer than `c` path components, the component drop itself forces an opposite-sign pair certificate in the ambient tournament.

No smallest-counterexample hypothesis, endpoint hypothesis, extremality condition, or deleted-marker structure is required.

## Signed-support convention used here

Only the elementary dimer/singleton cases are needed. If `x,p,y` are distinct and `(y,x,p)` is tight, regard the oriented dimer `(x,p)` as **head-signed** by witness `y`. If `(p,x,y)` is tight, regard `(p,x)` as **tail-signed** by witness `y`.

For a singleton `(d)`, the two-vertex paths `(y,d)` and `(d,y)` are automatically tight because they have no internal turn. Thus `(d)` may carry the corresponding head or tail sign witnessed by `y`.

A **balanced opposite-sign pair** in this statement is a pair of disjoint signed supports of opposite polarity. The construction below uses one common witness and therefore produces a graph-intrinsic certificate once the displayed vertices are fixed.

## Proof

First we show that `T` contains an adjacent selected state crossing two components of `R`.

Suppose not. Then every adjacent state selected by every `T_i` has both endpoints in a single `R`-component. Consequently each connected path `T_i` is contained entirely in one `R_j`: if a `T_i` ever left one `R`-component for another, its first such departure would be an adjacent selected state crossing the two components. Since the `T_i` cover all of `W`, every one of the `c` nonempty `R`-components contains at least one `T`-component. Distinct `R`-components are disjoint, so these `T`-components are distinct. Hence `r>=c`, contrary to hypothesis.

Therefore `T` selects some adjacent state `xy` whose endpoints lie in distinct components of `R`.

Because `W` is proper, choose a spare vertex

`d in V(H) \ W`.

Let `R_x` be the `R`-component containing `x`.

### Case 1: `R_x` is the singleton `(x)`

The selected two-vertex state `(x,y)` is automatically a tight path, so the singleton `(x)` is tail-signed by witness `y`. The two-vertex path `(y,d)` is also automatically tight, so the disjoint singleton `(d)` is head-signed by the same witness `y`.

Thus `(x)` and `(d)` form a balanced opposite-sign pair.

### Case 2: `R_x` has at least two vertices

Choose a vertex `p` adjacent to `x` on the literal path `R_x`. Since `y` lies in a different `R`-component, the vertices `p,x,y` are distinct.

Apply boundary antisymmetry to the reversal pair

`(y,x,p)` and `(p,x,y)`.

Exactly one of these two ordered triples is tight.

If `(y,x,p)` is tight, then the dimer `(x,p)` is head-signed by witness `y`. The automatic two-vertex path `(d,y)` makes the singleton `(d)` tail-signed by `y`. Their supports are disjoint because `{x,p}` is contained in `W` while `d` is outside `W`.

If instead `(p,x,y)` is tight, then the dimer `(p,x)` is tail-signed by witness `y`. The automatic two-vertex path `(y,d)` makes the singleton `(d)` head-signed by `y`, again on a disjoint support.

In either orientation we obtain a balanced opposite-sign pair.

The two cases exhaust the component containing `x`, proving the theorem. ∎

## Why this is reusable

The theorem is a generic **component-drop compiler**. Its input is merely two literal covers of one proper residue with different component counts. It does not care how those covers were obtained. Thus any argument that fragments a proper residue into more paths and later recompletes the same residue with fewer paths may immediately export a balanced-pair certificate.

A frequently used specialization compares two exact two-covers of the same proper residue: if a vertex is an endpoint in one cover and internal in the other, deleting that vertex produces respectively an at-most-two-cover and a three-cover of the same punctured residue, so the theorem applies.

## Scope and nonclaims

The resulting pair is graph-intrinsic historical information. The theorem does **not** assert that its two supports are simultaneously selected in either source cover, that the pair is unique, that it is current in a later representative, or that the pair by itself closes the global two-cover problem.

The proper-subset hypothesis is essential to this proof because it supplies the spare ambient vertex `d` used for the opposite singleton sign.

## Provenance

Rescued from the accepted general component-drop theorem historically recorded as `R159`, with its cross-state upgrade `R176` inlined so the Spare Part does not depend on archaeology result numbers. The corpus phrase-mining pass identified `balanced pair` in 118 source files (226 uses) and `component drop` in 46 source files (74 uses), making this one of the clearest theorem-level reusable mechanisms behind a high-frequency phrase cluster.