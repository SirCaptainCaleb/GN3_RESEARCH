# S9014 — Signed-Interval Rebirth and Tight-Path Cut Memory

## Theorem

Let

`P=(v_0,...,v_k)`

be a graph-intrinsic tight path, and let `S` be any vertex set such that `P-S` is nonempty.

Call a **surviving interval** a maximal nonempty contiguous block of vertices of `P` that remains after deleting `S`. Every surviving interval

`I=(v_i,...,v_j)`

in the old path order remembers its immediate cut neighbors:

- if `i>0`, then `v_{i-1}` is deleted and `(v_{i-1},I)` is a tight path;
- if `j<k`, then `v_{j+1}` is deleted and `(I,v_{j+1})` is a tight path.

In particular, signed intervals regenerate canonically.

### Head-signed form

Suppose `P` is head-signed by a witness `w`, meaning

`(w,v_0,...,v_k)`

is tight. Let `I=(v_i,...,v_j)` be the first surviving interval of `P-S`.

- If `i=0`, then `I` remains head-signed by `w`.
- If `i>0`, then `I` is head-signed by the immediately preceding deleted vertex `v_{i-1}`.

### Tail-signed form

Dually, suppose

`(v_0,...,v_k,z)`

is tight, and let `J=(v_i,...,v_j)` be the last surviving interval of `P-S`.

- If `j=k`, then `J` remains tail-signed by `z`.
- If `j<k`, then `J` is tail-signed by the immediately following deleted vertex `v_{j+1}`.

Thus deletion of arbitrary vertices from a tight path does not erase boundary information: every surviving interval retains exact cut-side witness data, and the first or last surviving interval of a signed support is automatically reborn as a signed descendant.

## Proof

Any contiguous subpath of a tight path is tight.

Let `I=(v_i,...,v_j)` be a surviving interval of `P-S`.

If `i>0`, maximality of the interval means `v_{i-1}` is deleted. The sequence

`(v_{i-1},v_i,...,v_j)`

is a contiguous subpath of `P`, hence is tight. Therefore `v_{i-1}` is an exact left cut witness for `I`.

Likewise, if `j<k`, maximality gives `v_{j+1}` deleted, and

`(v_i,...,v_j,v_{j+1})`

is a contiguous subpath of `P`, hence tight. This proves the two-sided cut-memory statement.

Now assume the head-signed form. Let `I` be the first surviving interval.

If `i=0`, then

`(w,v_0,...,v_j)`

is a prefix of the certified tight extension `(w,P)`, so `I` remains head-signed by `w`.

If `i>0`, the cut-memory statement already gives

`(v_{i-1},I)`

tight, so the immediately deleted old-path neighbor `v_{i-1}` becomes the new head witness.

The tail-signed form is the exact reverse-order argument using the last surviving interval. ∎

## Why this is reusable

This theorem is the basic memory law for historical tight supports. A later deletion or marker may fragment an old path, but each surviving block comes with exact old-neighbor certificates. On a signed side, the relevant surviving block is never merely an anonymous subpath: it inherits the old witness when the signed endpoint survives, or receives the adjacent deleted vertex as a replacement witness when the cut moves inward.

Repeated contacts therefore produce a nested ancestry chain with explicit witnesses rather than a sequence of unrelated supports.

## Scope and nonclaims

The theorem is purely path-order theoretic. It uses no smallest-counterexample hypothesis, path-cover representative, exchange mechanism, payment theory, or even boundary antisymmetry beyond whatever ambient notion certifies the original tight path.

It does not preserve the original signed anchor when that anchor itself is deleted, and it does not assert that the surviving interval remains selected in any later cover.

## Provenance

Rescued from the accepted theorem historically recorded as `R425`. Phrase mining found broad recurring `signed support` and `historical signed` vocabulary, while citation mining showed that the precise reusable primitive was this short cut-memory/rebirth law rather than the many later wrappers built on it.