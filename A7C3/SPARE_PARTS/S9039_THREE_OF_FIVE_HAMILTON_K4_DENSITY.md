# S9039 — Three-of-Five Hamilton K4 Deletions

## Theorem

Every edge-ordered `K5` has at least three vertex deletions whose remaining four vertices support an increasing Hamilton `P4`. Equivalently, at most two of its five induced `K4`s are non-Hamiltonian.

Consequently, if `h_4(r)` denotes the number of four-subsets of an edge-ordered `K_r`, `r>=5`, that support an increasing Hamilton `P4`, then

`h_4(r) >= (3/5) C(r,4)`.

## Proof

By `S9020`, a non-Hamiltonian edge-ordered `K4` has its three opposite-edge perfect matchings in strict height blocks. Hence taking opposite edges preserves comparison between adjacent edges: if `e,f` are adjacent edges of such a bad `K4` and `e*,f*` are their respective opposite edges, then

`e < f  iff  e* < f*`.

Suppose for contradiction that an edge-ordered `K5` on vertices

`{a,b,c,d,e}`

has three non-Hamiltonian vertex-deleted `K4`s. Relabel so the bad cells are those obtained by deleting `a`, `b`, and `c`.

In the bad cell on `{b,c,d,e}`, the adjacent edges `bd,be` have opposite edges `ce,cd`. Therefore

`bd < be  iff  ce < cd`.

In the bad cell on `{a,c,d,e}`, the adjacent edges `ce,cd` have opposite edges `ad,ae`. Therefore

`ce < cd  iff  ad < ae`.

In the bad cell on `{a,b,d,e}`, the adjacent edges `ad,ae` have opposite edges `be,bd`. Therefore

`ad < ae  iff  be < bd`.

Chaining the three equivalences gives

`bd < be  iff  be < bd`,

impossible in a strict total edge order. Thus at most two of the five induced `K4`s are non-Hamiltonian, proving the first assertion.

For the density statement, count incidences `(X,Y)` where `X` is a Hamilton four-set and `Y` is a five-set containing `X`. Every five-set contains at least three Hamilton four-sets, so the number of incidences is at least

`3 C(r,5)`.

Every four-set lies in exactly `r-4` five-sets. Hence

`(r-4) h_4(r) >= 3 C(r,5)`.

Using

`C(r,5) = ((r-4)/5) C(r,4)`

gives

`h_4(r) >= (3/5) C(r,4)`.

∎

## Why this is reusable

The theorem is a tiny local obstruction with a global density consequence. Together with Hamilton-five density, it supplies complementary `4+5` Hamilton supports in order nine and is the missing local ingredient in the human proof of `S9019` through order ten.

## Scope and nonclaims

The `3/5` bound is a lower bound obtained by double counting. This theorem does not classify equality, and it does not assert that every edge-ordered `K5` is Hamiltonian.

## Provenance

Human synthesis from the matching-height `K4` classification in `S9020`. No computation is used.