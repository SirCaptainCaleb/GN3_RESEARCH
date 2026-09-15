# S9036 — Complete Mate-Box Collapse

## Theorem

Let H satisfy pc(H)>k. For j=1,...,r let A_j={alpha_{j,i}: i in I_j} be finite families of ordered turns. Assume that for every tuple (i_1,...,i_r) there is a literal spanning k-component path proposal C(i_1,...,i_r) whose only possibly bad turns are holes h_{j,i_j} with complete reversals alpha_{j,i_j}. Then at least one family A_j is entirely tight.

## Proof

Fix a tuple (i_1,...,i_r). If all chosen turns alpha_{j,i_j} were bad, boundary antisymmetry would make every reversed hole h_{j,i_j} tight. By hypothesis those are the only possible holes in C(i_1,...,i_r), so that proposal would be a literal spanning k-cover, contradicting pc(H)>k. Hence every tuple satisfies the clause alpha_{1,i_1} tight OR ... OR alpha_{r,i_r} tight. Now suppose no A_j were entirely tight. For each j choose i_j with alpha_{j,i_j} bad. The corresponding Cartesian tuple makes every literal in its clause false, contradiction. Therefore some A_j consists entirely of tight turns.

## Why this is reusable

A full Cartesian box of candidate covers cannot fail in every coordinate family: one entire mate family must be tight. This is a generic finite propositional compiler for turning many literal candidate-cover failures into simultaneous intrinsic turns.

## Scope and nonclaims

Every Cartesian tuple must have a complete literal proposal with no holes beyond the listed ones. Partial boxes and proposals with hidden extra holes are outside the theorem.

## Provenance

Rescued from accepted archived result `R163`.
