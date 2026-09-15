# S9022 — Parallel Source Turns Force an Endpoint-Controlled Hamilton P5

## Theorem A — Hamilton P5 existence

Let `a,c,p,q,r` be five distinct vertices in a Strong Level-(1) boundary tournament. If

    (a,p,c), (a,q,c), (a,r,c)

are tight, then the induced subsystem on `{a,c,p,q,r}` has a tight Hamilton path of order five.

### Proof

For distinct `x,y in {p,q,r}`, write

    x ->_a y  iff  (x,a,y) is tight,
    x ->_c y  iff  (x,c,y) is tight.

By boundary antisymmetry, each relation is a tournament on `{p,q,r}`.

If distinct `x,y,z` satisfy `x ->_a y ->_c z`, then

    x,a,y,c,z

is a tight Hamilton P5: its middle turn `(a,y,c)` is one of the three hypotheses.

Assume for contradiction that no tight Hamilton P5 exists. Then there is no such mixed chain.

If `T_a` were transitive, relabel its vertices so

    x ->_a y,  y ->_a z,  x ->_a z.

Avoiding `x,a,y,c,z` forces `z ->_c y`, while avoiding `x,a,z,c,y` forces `y ->_c z`, contradicting that `T_c` is a tournament. Hence `T_a` is a directed 3-cycle. Relabel so

    p ->_a q ->_a r ->_a p.

Avoiding the three mixed-chain P5s then forces the opposite `c`-cycle

    r ->_c q,  p ->_c r,  q ->_c p.

Still assuming no Hamilton P5, inspect the six words

    a p c r q,
    a q c p r,
    a r c q p,
    p q a r c,
    q r a p c,
    r p a q c.

In each word the first two required turns are already tight from the source hypotheses and the two displayed cycles. Therefore the last turn must be bad; applying boundary antisymmetry to its complete reversal forces, respectively,

    (q,r,c), (r,p,c), (p,q,c),
    (a,q,p), (a,r,q), (a,p,r).

Now inspect

    a p r c q,
    a q p c r,
    a r q c p,
    p a q r c,
    q a r p c,
    r a p q c.

The same reasoning, using the turns just forced, yields

    (c,r,p), (c,p,q), (c,q,r),
    (r,q,a), (p,r,a), (q,p,a).

At this point only three source-only reversal bits are relevant. Write

    u = [(q,p,r) is tight],
    v = [(p,q,r) is tight],
    w = [(p,r,q) is tight].

For each of the eight values of `(u,v,w)`, the indicated pair of candidate words has every required turn already certified except one pair of complete reversals:

    000:  a c q r p   |   r p q c a
    100:  c a r q p   |   q p r a c
    010:  a c p q r   |   q r p c a
    110:  a c p q r   |   q r p c a
    001:  c a p r q   |   r q p a c
    101:  c a p r q   |   r q p a c
    011:  a c r p q   |   p q r c a
    111:  c a q p r   |   p r q a c.

For example, in the `000` row the only undecided turns are `(a,c,q)` and `(q,c,a)`, which are complete reversals. The same holds row by row. Boundary antisymmetry therefore makes exactly one undecided turn tight in each row, so one word in the relevant pair is a tight Hamilton P5. This contradicts the assumption that no Hamilton P5 exists.

Hence `{a,c,p,q,r}` always has a tight Hamilton P5. QED.

## Theorem B — a source spoke can be an endpoint

Let `A,C,p,q,r` be distinct vertices of a Strong Level-(1) boundary tournament and suppose

`(A,s,C)`

is tight for every `s∈{p,q,r}`. Then the induced five-set `{A,C,p,q,r}` has a tight Hamilton `P5` with at least one endpoint in `{p,q,r}`.

The source-spoke endpoint cannot in general be prescribed in advance: for each designated source label there are examples satisfying the three source turns in which that label is not an endpoint of any tight Hamilton `P5`.

### Proof

The preceding theorem gives at least one tight Hamilton `P5` on the source five-set. If one endpoint is already a source spoke, there is nothing to prove. Otherwise the endpoints are `A,C`, and after renaming the three internal source spokes as `x,y,z`, the path has one of the two orientations

`A,x,y,z,C` or `C,x,y,z,A`.

### Case 1: `A,x,y,z,C`

Write Boolean indicators

`α=[(A,y,z)]`, `β=[(z,C,x)]`, `γ=[(z,C,y)]`,
`δ=[(C,y,x)]`, `ε=[(x,A,y)]`, `η=[(x,A,z)]`.

By boundary antisymmetry, each complete-reversal turn has the complementary value. Consider the seven source-endpoint candidates

`A,y,z,C,x`,
`A,z,C,y,x`,
`x,A,y,C,z`,
`x,A,z,C,y`,
`y,A,x,C,z`,
`z,A,x,y,C`,
`z,y,A,x,C`.

Using the source turns and the turns already certified by the original Hamilton path, their success conditions are respectively

`α∧β`, `γ∧δ`, `ε∧¬γ`, `η∧γ`, `¬ε∧¬β`, `¬η∧¬δ`, `¬α∧¬ε`.

Assume all seven fail. Failure of the last gives `α∨ε`. If `α=0`, then `ε=1`. If `α=1`, failure of the first gives `β=0`, and failure of the fifth again gives `ε=1`. Thus always `ε=1`. Failure of the third gives `γ=1`; failure of the second then gives `δ=0`; failure of the sixth gives `η=1`. But then the fourth candidate succeeds, contradiction.

### Case 2: `C,x,y,z,A`

Use

`β=[(z,C,x)]`, `γ=[(z,C,y)]`, `ε=[(x,A,y)]`, `η=[(x,A,z)]`.

The five candidates

`A,z,C,x,y`,
`x,A,z,C,y`,
`y,z,A,x,C`,
`x,A,y,C,z`,
`y,A,x,C,z`

have success conditions

`β`, `η∧γ`, `¬η`, `ε∧¬γ`, `¬ε∧¬β`.

If all fail, the first gives `β=0`, the third gives `η=1`, the second gives `γ=0`, and the fourth gives `ε=0`; the fifth then succeeds, contradiction.

Hence some tight Hamilton source `P5` has a source-spoke endpoint.

## Non-prescribability

Take the global ordinary-edge order

`pq < Ar < AC < qr < Ap < Cp < pr < Aq < Cr < Cq`.

The induced comparison orientation is a Strong Level-(1) boundary tournament and satisfies all three source turns because

`Ap<Cp`, `Aq<Cq`, `Ar<Cr`.

Its tight Hamilton `P5` orders are exactly

`A,p,r,C,q` and `r,A,p,C,q`.

Thus the designated spoke `p` is never an endpoint. Relabelling the source spokes shows that no fixed source label can be universally prescribed.

No ancestry, deletion-cover, or minimum-counterexample input is used.

## Why this is reusable

Three parallel source turns already force a Hamilton five-path, and one can always choose such a path with some source-spoke endpoint. This is a completely local five-vertex theorem with no cover-minimality or ancestry input.

## Scope and nonclaims

The endpoint source label cannot be prescribed in advance, as the explicit edge-order example shows.

## Provenance

Rescued from accepted archived results `R1031`, `R1046`. The endpoint strengthening `R1046` has explicit PASS status.
