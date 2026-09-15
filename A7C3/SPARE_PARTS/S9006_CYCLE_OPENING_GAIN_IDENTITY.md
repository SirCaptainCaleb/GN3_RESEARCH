# S9006 — Cycle-Opening Gain Identity

## Theorem

Let a spanning path cover on a fixed `n`-vertex set initially have `q` path components. Suppose a compatible selected-state exchange adds and removes states with **raw gain**

`g = (# inserted states) - (# removed states)`,

and suppose the resulting selected-state system has only vertex-simple path components and physical tight-cycle components. If exactly `c` cycle components occur, then opening one selected state on each cycle yields a genuine spanning path cover with

`q' = q - g + c`

components.

Equivalently,

`q - q' = g - c`.

Thus actual path-cover improvement is raw exchange gain minus cycle debt. A physical tight cycle is constructive bookkeeping debt, not a contradiction: each cycle costs exactly one selected state to open.

## Proof

A path cover with `q` components on `n` fixed vertices contains exactly

`n-q`

selected adjacent states, because a path on `m` vertices contributes `m-1` selected states.

After the compatible exchange, raw gain `g` changes the selected-state count to

`n-q+g`.

Suppose the resulting system has exactly `c` physical tight-cycle components. Remove one selected state from each cycle. Deleting one state opens that cycle into a vertex-simple tight path and does not affect any other component. After all `c` cycles are opened, the resulting spanning path system therefore has

`n-q+g-c`

selected states.

If the resulting genuine path cover has `q'` components, it also has exactly `n-q'` selected states. Hence

`n-q' = n-q+g-c`,

so

`q-q' = g-c`.

This is the claimed identity. ∎

## Why this is reusable

The identity cleanly separates two quantities that are often conflated in exchange arguments:

- combinatorial edge gain from the exchange itself;
- topological debt created when some resulting components are cycles rather than paths.

It applies whenever the exchange preserves the local compatibility needed for every connected component to be a path or a physical tight cycle. No smallest-counterexample hypothesis or particular Engine geometry is involved.

## Scope and nonclaims

The theorem does not certify that a proposed exchange is compatible, physical, or tight. Those facts must be proved separately.

It also does not say cycles are harmless in every downstream argument; it says exactly how much path-cover gain is lost when they must be opened.

## Provenance

Rescued from the accepted bookkeeping identity historically recorded as `R17`. The corpus phrase `cycle debt` occurs in 24 source files with 44 uses, often in arguments whose actual invariant is precisely this gain-minus-debt formula.