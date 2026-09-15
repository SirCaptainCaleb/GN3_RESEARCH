# S9008 — Three-Cover Six-Clause Splice Fan

## Theorem

Let `H` be a finite Strong Level-(1) boundary tournament with `pc(H)>2`, and suppose

`H = A | B | C`

is a literal spanning three-path cover in which all three component paths are nontrivial.

For every ordered pair of distinct components, say

`A=(a_0,...,a_p)` and `B=(b_0,...,b_q)` with `p,q>=1`,

consider the spanning two-path proposal obtained by concatenating `A` to `B` and leaving `C` unchanged:

`(a_0,...,a_p,b_0,...,b_q) | C`.

Its complete uncertified-turn set consists exactly of the two seam turns

`h_1=(a_{p-1},a_p,b_0)`

and

`h_2=(a_p,b_0,b_1)`.

At least one of these two turns is bad. Consequently boundary antisymmetry forces the physical mate clause

`(b_0,a_p,a_{p-1})` tight

or

`(b_1,b_0,a_p)` tight.

Applying this construction to all six ordered pairs among `A,B,C` yields six explicit two-hole mate clauses attached to the same literal spanning three-cover.

## Proof

Fix an ordered pair of components `A,B` and leave `C` unchanged.

Every consecutive triple lying entirely inside `A` is tight because `A` is a tight path, and every consecutive triple lying entirely inside `B` is tight because `B` is a tight path. In the concatenated path

`A*B=(a_0,...,a_p,b_0,...,b_q)`,

the only new consecutive triples are the two triples straddling the splice:

`h_1=(a_{p-1},a_p,b_0)`

and

`h_2=(a_p,b_0,b_1)`.

Hence these two turns are exactly the complete uncertified-turn set of the spanning proposal `(A*B)|C`.

If both `h_1` and `h_2` were tight, then `A*B` itself would be a tight path. Together with `C`, it would form a spanning two-cover of `H`, contradicting `pc(H)>2`.

Thus at least one of `h_1,h_2` is bad. Strong Level-(1) boundary antisymmetry converts a bad turn into the tight complete reversal. Therefore

`h_1` bad implies `(b_0,a_p,a_{p-1})` tight,

while

`h_2` bad implies `(b_1,b_0,a_p)` tight.

So the displayed mate disjunction holds for the ordered pair `(A,B)`.

The argument uses only the literal orders of the two chosen component paths and therefore applies independently to each ordered pair

`(A,B), (A,C), (B,A), (B,C), (C,A), (C,B)`.

This gives six explicit physical mate clauses. ∎

## Why this is reusable

The theorem is a generic seam compiler for any nontrivial spanning three-cover. It turns the global obstruction `pc(H)>2` into six local, physically oriented disjunctions without invoking smallest-counterexample minimality, deletion geometry, extremality, payment machinery, or a specialized frame.

It is particularly useful when a later argument needs exact reverse endpoint turns rather than an abstract statement that two rails cannot simply concatenate.

## Scope and nonclaims

The theorem does not assert that any one mate clause closes `H`, that two clauses are complementary, or that the six clauses necessarily contain a stronger cycle/fork pattern.

The output is exactly the six local disjunctions, with their literal component orders retained.

## Provenance

Rescued from the accepted order-free seam compiler historically recorded as `R879`. Source-ranking identified it as one of the cleanest general parents behind recurring `two-hole`, `reverse seam`, and physical splice vocabulary in the corpus.