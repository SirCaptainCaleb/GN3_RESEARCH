# A switch-adjacent xz insertion absorbs the whole shore unless three two-step edge descents are absent — preserved pre-item development

## Composition

(none yet)

## Development

Let A be a shore of the switching split B -> z -> A -> x, and let
O=(a_1,...,a_k)
be a NOR-good A-order with word 0^p1^q.

For a cut j in {p,p+1,p+2}, let
P_j=(a_1,...,a_j),
S_j=(a_{j+1},...,a_k).
All internal windows of P_j are zero and all internal windows of S_j are one.

Write e_i=1 when a_i -> a_{i+1} in the switching-normalized shore tournament.

Consider the spanning order on A union {x,z}
Q_j=P_j, x,z, S_j.
The only nontrivial collar statuses are
alpha(a_{j-1},a_j,x)=1-e_{j-1},
alpha(z,a_{j+1},a_{j+2})=1-e_{j+1},
while
alpha(a_j,x,z)=0
and
alpha(x,z,a_{j+1})=0.
Therefore Q_j has a one-change word whenever
e_{j-1}=1 and e_{j+1}=0:
the entire prefix through the xz pair is zero and the suffix is one.

The same conclusion is obtained with the reversed pair z,x, with the switch placed on the other side of the pair.

Hence collective absorption of all of A succeeds if any of
(e_{p-1},e_{p+1}),
(e_p,e_{p+2}),
(e_{p+1},e_{p+3})
equals (1,0), with endpoint clipping.

If no such splice exists, the five-edge neighborhood of the shore switch satisfies the two-step monotonicity implications
e_{p-1}=1 => e_{p+1}=1,
e_p=1 => e_{p+2}=1,
e_{p+1}=1 => e_{p+3}=1.
Thus failure of the full-shore one-change splice is a bounded local edge-pattern obstruction, independent of the remote shore endpoints.
