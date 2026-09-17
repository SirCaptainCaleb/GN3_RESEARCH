# S9015 — Three-Component Broad-Interval Augmentation

## Theorem

Let `G` be an edge-ordered complete graph and let `F` be a spanning cover of `G` by `c>=3` vertex-disjoint increasing paths, each oriented in its increasing direction.

For a vertex `v` on one of the paths, let `L(v)` denote the label of its incoming path edge when that edge exists and put `L(v)=-infinity` at a path source. Likewise let `U(v)` denote the label of its outgoing path edge when it exists and put `U(v)=+infinity` at a path terminal.

Suppose `p->v` is a selected edge of one component `C`. Let `t` be the terminal vertex of a second component `A`, and let `s` be the source vertex of a third component `B`, with `A,B,C` pairwise distinct. If

`L(t) < lambda(tv) < U(v)`

and

`L(p) < lambda(ps) < U(s)`,

then deleting the selected edge `p->v` and adding `t->v` and `p->s` produces a spanning cover by `c-1` vertex-disjoint increasing paths.

The conclusion remains valid when `A` or `B` is a singleton under the endpoint conventions above.

## Proof

Write

`A=(a_0,...,a_r=t)`,

`C=(c_0,...,c_i=p,c_{i+1}=v,...,c_m)`,

and

`B=(s=b_0,b_1,...,b_q)`,

allowing `A` or `B` to consist of one vertex.

Delete the selected edge `p->v` from `C`. Replace the three components `A,C,B` by

`A'=(a_0,...,t,v,c_{i+2},...,c_m)`

and

`B'=(c_0,...,p,s,b_1,...,b_q)`,

with the evident omissions when a displayed inherited segment is empty.

The two new paths together contain exactly the vertices previously contained in `A,C,B`, and every untouched component of `F` is left unchanged. Thus the new family still spans `G`. Three old components have been replaced by two, so the component count drops from `c` to `c-1`.

It remains only to check increasingness at the two new seams. Every comparison internal to an inherited path segment is unchanged.

At the seam `t->v`, the edge entering `t`, when present, has label `L(t)`, while the edge leaving `v`, when present, has label `U(v)`. Hence

`L(t) < lambda(tv) < U(v)`

is exactly the complete condition required for the concatenation through `t->v` to remain increasing. If `A` is a singleton, the lower comparison is absent and is encoded by `L(t)=-infinity`; if `v` is terminal, the upper comparison is absent and is encoded by `U(v)=+infinity`.

Similarly, at the seam `p->s`, the edge entering `p`, when present, has label `L(p)`, while the edge leaving `s`, when present, has label `U(s)`. Thus

`L(p) < lambda(ps) < U(s)`

is exactly the complete seam condition for `B'`.

No vertex acquires two incoming or two outgoing selected edges: `p` loses `p->v` and gains `p->s`, while `v` loses its old incoming edge and gains `t->v`; the terminal `t` and source `s` receive the complementary new incidences. Therefore the two new components are vertex-simple directed paths.

Hence the modified family is a spanning increasing path cover with one fewer component. ∎

## Why this is reusable

This is the collision-free three-component augmentation move behind the broad-interval relation. It is independent of boundary tournaments, smallest-counterexample minimality, and any particular Engine frame. In a minimum-component increasing path cover, every attempted triple of this form must violate at least one of the two displayed seam inequalities.

## Scope and nonclaims

The theorem only treats a single length-three cooperative augmentation involving three distinct cover components. It does not license arbitrary alternating paths or matchings in the broad-interval graph; longer alternations can alter both incidences of one original vertex and require separate increasingness checks.

## Provenance

Rescued from accepted `R956`, whose proof is already purely edge-ordered and human. This promotion is intentional despite the result belonging to the edge-orderable subtheory: Spare Parts are organized by reusability, not by requiring order-free scope.