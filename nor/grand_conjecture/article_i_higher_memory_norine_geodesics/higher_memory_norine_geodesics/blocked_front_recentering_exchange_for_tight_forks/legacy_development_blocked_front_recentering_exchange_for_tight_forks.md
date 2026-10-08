# Blocked-front recentering exchange for tight forks — preserved pre-item development

## Development

## Blocked-front recentering exchange

Fix coordinate arity (r\ge2) and a color (sigma). Let
[
P=A,S,qquad Q=B,S^{\rm rev}
]
be a color-(sigma) converging tight fork, where (S) is an ordered ((r-1))-tuple and the two branches are disjoint outside (S).

Let
[
F_P=(p_1,ldots,p_{r-1})
]
be the first ((r-1))-tuple of (P), and let (x) be a vertex outside the fork. Suppose (x) is blocked from prepending (P):
[
h(x,F_P)=1-sigma.
]
By reversal antisymmetry,
[
h(F_P^{\rm rev},x)=sigma.
]

### Exchange lemma

There is a color-((1-sigma)) converging tight fork on exactly the vertex set
[
V(P)cup{x},
]
with common center (F_P): its two branches are
[
(x,F_P)
qquad	ext{and}qquad
P^{\rm rev}.
]

Indeed, ((x,F_P)) is color (1-sigma) by the blocking identity, while every (r)-window of (P^{\rm rev}) is the reversal of a color-(sigma) window of (P), hence has color (1-sigma). The first branch ends in (F_P), the second ends in (F_P^{\rm rev}), and they share precisely the center vertices.

Symmetrically, blocking (x) at (Q) yields a color-((1-sigma)) fork on (V(Q)cup{x}).

### Consequences for maximum and deletion forks

1. If a nonspanning fork has one vacuous outer branch, say (B=arnothing), then any blocked outside vertex (x) strictly enlarges the fork by the exchange lemma, because (V(Q)=S\subseteq V(P)). Therefore an inclusion- or cardinality-maximal nonspanning fork must have both outer branches nonempty.

2. More generally, absorbing (x) through (P) replaces the entire opposite outer branch (B) by the single vertex (x). If the original fork covers all but (x), with outer branch sizes
[
|A|=a,qquad |B|=b,
]
then the exchanged fork covers all but the (b) vertices of (B), and its outer branch sizes are (a) and (1).

3. In particular, when (b=1), the exchange preserves the number of covered vertices and swaps the omitted vertex (x) with the unique vertex of (B). Thus minimum-counterexample deletion forks with a singleton branch carry a canonical omission-exchange move.

### Audit

This is only a recentering identity; by itself it does not prove the one-vertex augmentation theorem when both outer branches are nonempty. Its value is that it identifies the obstruction more sharply: a blocked vertex can always be absorbed at the cost of discarding the opposite branch, so the unresolved issue is precisely how to retain or recover that opposite branch.
