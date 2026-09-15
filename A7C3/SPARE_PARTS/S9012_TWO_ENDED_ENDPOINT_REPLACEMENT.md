# S9012 — Two-Ended Endpoint Replacement Lemma

## Theorem

Let

`Q=(q_0,q_1,...,q_r)`, `r>=2`,

be a vertex-simple Hamilton tight path on a support `X` in a finite Strong Level-(1) boundary tournament, and let `y` be a vertex outside `X`.

Assume `X∪{y}` is non-Hamiltonian. Suppose nevertheless that there is

- a Hamilton tight path `L` on `(X-{q_0})∪{y}`, and
- a Hamilton tight path `R` on `(X-{q_r})∪{y}`.

Then at least one of the three path comparisons

`(Q,L)`, `(Q,R)`, `(L,R)`

has an explicit Reverse-Ear output: an exact reversed old adjacent state, a tight reverse trimer at a seam, or a vertex-simple proper tight cycle.

Equivalently, outside explicit reverse-order geometry, one exterior vertex cannot Hamilton-replace both endpoints of a Hamilton path while the full one-vertex extension remains non-Hamiltonian.

More precisely, if `(Q,L)` is Reverse-Ear-quiet, then

`L=(y,q_1,q_2,...,q_r)`

or

`L=(q_1,y,q_2,...,q_r)`.

If `(Q,R)` is Reverse-Ear-quiet, then

`R=(q_0,...,q_{r-1},y)`

or

`R=(q_0,...,q_{r-2},y,q_{r-1})`.

If `(L,R)` is quiet as well, only the boundary-overlap cases `r=2` or `r=3` survive, and each directly concatenates to a Hamilton path on `X∪{y}`, contradiction.

## Proof

Suppose, for contradiction, that all three comparisons are Reverse-Ear-quiet.

Compare `Q` with `L`. Their common vertices are exactly `q_1,...,q_r`. Reverse-Ear quietness forces these contacts to occur along `L` in increasing `Q`-order. Hence `L` is obtained by inserting `y` somewhere into

`(q_1,...,q_r)`.

If `y` were not in one of the first two positions, `L` would begin with `(q_1,q_2)`. Since `(q_0,q_1,q_2)` is tight on `Q`, prepending `q_0` would make a Hamilton tight path on `X∪{y}`, contrary to hypothesis. Thus

`L=(y,q_1,...,q_r)`

or

`L=(q_1,y,q_2,...,q_r)`.

Dually, compare `Q` with `R`. Quietness forces the common vertices `q_0,...,q_{r-1}` to occur in increasing `Q`-order. Thus `R` is obtained by inserting `y` into

`(q_0,...,q_{r-1})`.

If `y` were not in one of the last two positions, `R` would end with `(q_{r-2},q_{r-1})`, and appending `q_r` using the tight turn `(q_{r-2},q_{r-1},q_r)` would Hamiltonize `X∪{y}`. Therefore

`R=(q_0,...,q_{r-1},y)`

or

`R=(q_0,...,q_{r-2},y,q_{r-1})`.

There are four combinations of these two forced forms. Compare `L` and `R`.

If

`L=(y,q_1,...,q_r)` and `R=(q_0,...,q_{r-1},y)`,

then `y` and `q_1` occur in opposite orders, so Reverse-Ear fires.

If

`L=(y,q_1,...,q_r)` and `R=(q_0,...,q_{r-2},y,q_{r-1})`,

the same reversal occurs for `r>=3`; the only quiet possibility is `r=2`.

If

`L=(q_1,y,q_2,...,q_r)` and `R=(q_0,...,q_{r-1},y)`,

then `y` and `q_2` occur in opposite orders for `r>=3`; again only `r=2` can remain quiet.

Finally, if

`L=(q_1,y,q_2,...,q_r)` and `R=(q_0,...,q_{r-2},y,q_{r-1})`,

then `y` and `q_2` occur in opposite orders for `r>=4`; for `r=2` the common pair `q_1,y` is reversed, so only `r=3` can remain quiet.

Thus simultaneous quietness leaves only three boundary-overlap cases.

For `r=2`, the first quiet pairing gives

`L=(y,q_1,q_2)`, `R=(q_0,y,q_1)`,

whose certified turns concatenate to

`(q_0,y,q_1,q_2)`.

The other quiet `r=2` pairing gives

`L=(q_1,y,q_2)`, `R=(q_0,q_1,y)`,

which concatenate to

`(q_0,q_1,y,q_2)`.

For `r=3`, the sole quiet pairing gives

`L=(q_1,y,q_2,q_3)`, `R=(q_0,q_1,y,q_2)`,

which concatenate to

`(q_0,q_1,y,q_2,q_3)`.

Each is a Hamilton tight path on `X∪{y}`, contradicting non-Hamiltonicity. Therefore one of the three comparisons must have an explicit Reverse-Ear output. ∎

## Why this is reusable

The lemma converts a two-sided endpoint-replacement phenomenon into either full Hamilton extension or explicit reverse-order geometry. It is independent of smallest-counterexample minimality, cover structure, uniformity, longest-path assumptions, and payment machinery.

Its only nontrivial reusable input is the Reverse-Ear Lemma `S9001`.

## Scope and nonclaims

The theorem does not say which comparison fires or consume the resulting Reverse-Ear certificate. It does not imply a spanning two-cover without another argument.

## Provenance

Rescued from the accepted all-order theorem historically recorded as `R966`. Citation-graph mining found it referenced from **24 distinct corpus files**, and its entire proof reduces to reusable path-order comparison plus three tiny boundary-overlap checks.