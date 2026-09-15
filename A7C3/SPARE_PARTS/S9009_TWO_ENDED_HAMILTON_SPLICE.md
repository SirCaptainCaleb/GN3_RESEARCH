# S9009 — Two-Ended Hamilton Absorber Splice Lemma

## Theorem

Let `H` be a finite exact-reversal tight-turn system. Let `X,Y` partition `V(H)`, and suppose `Y` has a literal two-path cover

`U | V`

with both rails nonempty. Choose an endpoint `x` of `U` and an endpoint `y` of `V` in opposite splice roles. In one orientation write

`U=(x,u_1,...,u_r)`,

`V=(v_0,...,v_{s-1},y)`,

and suppose `X∪{x,y}` has a Hamilton tight path

`Q=(y,q_1,...,q_t,x)`.

Form the vertex-simple spanning word

`K=(v_0,...,v_{s-1},y,q_1,...,q_t,x,u_1,...,u_r)`,

omitting an empty residual piece when necessary.

Its complete uncertified-turn set consists of at most the two attachment turns

`alpha=(v_{s-1},y,q_1)`

when the left residual seam exists, and

`beta=(q_t,x,u_1)`

when the right residual seam exists.

If `pc(H)>1`, at least one existing attachment turn is bad, so exact reversal gives `reverse(alpha)` tight or `reverse(beta)` tight, with nonexistent holes omitted.

If `pc(H)>2`, then both residual seams exist and both `alpha` and `beta` are bad. Consequently both reversed attachment turns are tight simultaneously.

The other endpoint-role choices are obtained by the corresponding role-correct concatenation, without reversing any certified tight path.

## Proof

Because `X,Y` partition `V(H)`, because `Q` spans exactly `X∪{x,y}`, and because `Q` meets the two residue rails only at `x,y`, the displayed word `K` is vertex-simple and spans `H`.

Every consecutive triple wholly inside the surviving part of `V` is tight. Every consecutive triple wholly inside `Q` is tight. Every consecutive triple wholly inside the surviving part of `U` is tight. Therefore the only turns whose tightness is not inherited from one of the displayed paths are the two possible attachment turns `alpha` and `beta`. If a residual piece is empty, its corresponding seam simply does not exist.

Assume first that `pc(H)>1`. If every existing attachment turn were tight, then every consecutive turn of `K` would be tight, so `K` itself would be a Hamilton path of `H`, contradicting `pc(H)>1`. Hence at least one existing attachment turn is bad. Exact-reversal antisymmetry makes the complete reversal of that bad turn tight, proving the mate disjunction.

Now assume `pc(H)>2`. Suppose the complete list of bad consecutive turns in `K` had size at most one. It cannot have size zero by the preceding paragraph, so let `gamma` be its unique bad consecutive turn.

Cut the spanning word `K` at either of the two word edges lying inside `gamma`. The cut produces two nonempty contiguous subwords whose vertex sets partition `V(H)`. It creates no new consecutive triples. Every consecutive triple remaining inside either subword was already a consecutive triple of `K` distinct from `gamma`, and therefore is tight. Thus the two subwords are tight paths forming a spanning two-cover of `H`, contradicting `pc(H)>2`.

So `K` must contain at least two bad turns. But its complete uncertified-turn set contains at most `alpha,beta`, while all other turns are already certified tight. Therefore both seams must exist and both `alpha,beta` must be bad. Exact reversal then certifies both reversed attachment turns simultaneously.

The three other endpoint-role configurations are proved by forming the corresponding endpoint-compatible spanning word and repeating the same complete-window argument. ∎

## Why this is reusable

This lemma packages a common absorber maneuver: a Hamilton path through a central support and one endpoint of each residue rail is inserted between the two residual rail pieces. The resulting spanning word has a complete bad-turn ledger of size at most two.

The stronger `pc(H)>2` conclusion is especially useful: a one-hole spanning word is impossible because one cut would turn it into a spanning two-cover. Thus two residual seams, when present as the only possible defects, must both be genuine bad turns.

## Scope and nonclaims

The theorem does not produce the Hamilton absorber `Q` or the residue two-cover `U|V`. It does not apply when the chosen endpoints lie on the same residue rail.

The simultaneous reversed seams are local certificates. The lemma does not claim they alone close the ambient problem.

## Provenance

Rescued from the accepted order-free absorber-splice theorem historically recorded as `R933`. Source-level phrase mining identified it as a portable parent of recurring two-hole, attachment-seam, and Hamilton-absorber arguments.