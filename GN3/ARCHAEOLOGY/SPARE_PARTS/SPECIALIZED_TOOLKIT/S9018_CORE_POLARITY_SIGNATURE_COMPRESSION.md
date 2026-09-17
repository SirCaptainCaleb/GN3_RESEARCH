# S9018 — Core-Polarity Signature Compression

## Theorem

Let `H` be a finite Strong Level-(1) boundary tournament. Fix a three-vertex core

`C={a,b,c}`

and an exterior set `E` disjoint from `C`.

For `x in E` and `d in C`, write `C-{d}={u,v}`. Define the **core-polarity match-set**

`M_C(x) subseteq C`

by declaring

`d in M_C(x)` iff `(u,d,v)` and `(u,x,v)` have the same polarity,

that is,

`[(u,d,v) is tight] = [(u,x,v) is tight]`.

This is independent of the ordering chosen for `u,v`: swapping `u,v` replaces each tested turn by its complete reversal, so boundary antisymmetry complements both Boolean values and preserves their equality. Equivalently, one may orient `u,v` uniquely so that `(u,d,v)` is tight; then `d in M_C(x)` exactly when `(u,x,v)` is tight.

Let `Gamma_C` be the graph on `E` in which distinct exterior vertices `x,y` are adjacent exactly when the induced five-set `C union {x,y}` has a tight Hamilton path of order five.

Then:

1. For each `d in C`, the coordinate class

   `E_d={x in E : d in M_C(x)}`

   is a clique of `Gamma_C`.

2. Consequently, if `U subseteq E` is independent in `Gamma_C`, then the match-sets `M_C(x)`, `x in U`, are pairwise disjoint. In particular,

   `sum_{x in U} |M_C(x)| <= 3`.

3. If `U={x,y,z}` has three exterior vertices and all three pair-extensions

   `C union {x,y}`, `C union {x,z}`, `C union {y,z}`

   are Hamilton-P5-free, then, up to independent relabelling of the core coordinates and of `x,y,z`, the signature triple

   `(M_C(x),M_C(y),M_C(z))`

   is exactly one of

   `(emptyset,emptyset,emptyset)`,

   `({a},emptyset,emptyset)`,

   `({a,b},emptyset,emptyset)`,

   `({a},{b},emptyset)`,

   `({a,b,c},emptyset,emptyset)`,

   `({a,b},{c},emptyset)`,

   `({a},{b},{c})`.

Thus a nine-bit three-exterior polarity table collapses to seven normal forms whenever the three exterior pairs are all Hamilton-P5-free.

## Parallel-trimer lemma

The only local ingredient needed for the compression theorem is the following boundary-tournament fact.

**Lemma.** Let `a,c,p,q,r` be five distinct vertices. If

`(a,p,c)`, `(a,q,c)`, `(a,r,c)`

are tight, then the induced subsystem on `{a,c,p,q,r}` has a tight Hamilton path of order five.

### Proof

For distinct `x,y in {p,q,r}`, write

`x ->_a y` iff `(x,a,y)` is tight,

`x ->_c y` iff `(x,c,y)` is tight.

Boundary antisymmetry makes each relation a tournament on `{p,q,r}`.

If distinct `x,y,z` satisfy `x ->_a y ->_c z`, then

`x,a,y,c,z`

is already a tight Hamilton P5, because its middle turn `(a,y,c)` is one of the three hypotheses. Assume for contradiction that no tight Hamilton P5 exists. Then no such mixed chain exists.

If the tournament `T_a` were transitive, relabel its vertices so that

`x ->_a y`, `y ->_a z`, `x ->_a z`.

Avoiding `x,a,y,c,z` forces `z ->_c y`, while avoiding `x,a,z,c,y` forces `y ->_c z`, impossible. Hence `T_a` is a directed 3-cycle. Relabel so

`p ->_a q ->_a r ->_a p`.

Avoidance of the three mixed-chain P5s forces the opposite `c`-cycle

`r ->_c q`, `p ->_c r`, `q ->_c p`.

Still assuming no Hamilton P5, inspect the six words

`a p c r q`,
`a q c p r`,
`a r c q p`,
`p q a r c`,
`q r a p c`,
`r p a q c`.

In each word the first two required turns are already tight from the source hypotheses and the two displayed cycles. Therefore its final turn must be bad. Boundary antisymmetry forces, respectively,

`(q,r,c)`, `(r,p,c)`, `(p,q,c)`,
`(a,q,p)`, `(a,r,q)`, `(a,p,r)`

tight.

Now inspect

`a p r c q`,
`a q p c r`,
`a r q c p`,
`p a q r c`,
`q a r p c`,
`r a p q c`.

The same argument, using the newly forced turns, gives

`(c,r,p)`, `(c,p,q)`, `(c,q,r)`,
`(r,q,a)`, `(p,r,a)`, `(q,p,a)`

tight.

Only three source-only reversal bits remain relevant. Put

`u=[(q,p,r) is tight]`,
`v=[(p,q,r) is tight]`,
`w=[(p,r,q) is tight]`.

For each value of `(u,v,w)`, the indicated pair of candidate words has every required turn already certified except one complete-reversal pair:

`000:  a c q r p   |   r p q c a`

`100:  c a r q p   |   q p r a c`

`010:  a c p q r   |   q r p c a`

`110:  a c p q r   |   q r p c a`

`001:  c a p r q   |   r q p a c`

`101:  c a p r q   |   r q p a c`

`011:  a c r p q   |   p q r c a`

`111:  c a q p r   |   p r q a c`.

Boundary antisymmetry makes exactly one turn in each undecided reversal pair tight, so in every row one of the two candidate words is a tight Hamilton P5. This contradicts the assumption. ∎

## Proof of the compression theorem

Fix `d in C` and suppose `x,y in E_d`. Choose the ordering `C-{d}={u,v}` for which `(u,d,v)` is tight. By the definition of the match-set,

`(u,d,v)`, `(u,x,v)`, `(u,y,v)`

are three parallel tight trimers with common ordered endpoints `u,v` and three distinct middle vertices `d,x,y`. The parallel-trimer lemma gives a tight Hamilton P5 on

`{u,v,d,x,y}=C union {x,y}`.

Thus `xy` is an edge of `Gamma_C`, and `E_d` is a clique.

If `U` is independent in `Gamma_C`, no two of its vertices can therefore share a coordinate. Hence the sets `M_C(x)`, `x in U`, are pairwise disjoint subsets of the three-element set `C`. Summing their sizes gives

`sum_{x in U}|M_C(x)| <= |C|=3`.

Now let `U={x,y,z}` be independent. Pairwise disjointness implies that the sorted cardinality triple of

`M_C(x), M_C(y), M_C(z)`

is one of

`(0,0,0)`, `(1,0,0)`, `(2,0,0)`, `(1,1,0)`, `(3,0,0)`, `(2,1,0)`, `(1,1,1)`.

Relabelling the exterior vertices orders the three sizes, and relabelling the three core coordinates sends each disjoint realization of a fixed cardinality pattern to the corresponding displayed representative. These are therefore exactly the seven normal forms. ∎

## Why this is reusable

The theorem turns a collection of apparently independent polarity bits into a small set-system constraint. A shared core coordinate is not merely a local coincidence: it immediately creates a Hamilton P5 on the corresponding exterior pair. Consequently any family of pairwise P5-free exterior pairs behaves like a packing of subsets into a three-element ground set.

This compression is useful before any detailed case split. In the three-exterior case, nine Boolean match bits reduce to seven unlabeled configurations.

## Scope and nonclaims

This theorem does not assert that a three-vertex independent exterior family exists. It only classifies the signatures of such a family if it exists. It uses no smallest-counterexample minimality, path-cover structure, phase bookkeeping, retained source cover, spectator path, or Engine-specific ancestry.

The result is a local structural compressor, not by itself a closure theorem.

## Provenance

Promoted from accepted workspace result `R2151`. Its sole substantive ingredient is the parallel-trimer Hamilton-P5 theorem historically recorded as `R1031`; that lemma has been included above so this Spare Part is self-contained.