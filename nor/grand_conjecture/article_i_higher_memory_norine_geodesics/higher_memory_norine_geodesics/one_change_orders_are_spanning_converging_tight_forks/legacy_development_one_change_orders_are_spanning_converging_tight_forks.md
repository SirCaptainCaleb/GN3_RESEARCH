# One-change orders are spanning converging tight forks — preserved pre-item development

## Development

## Converging tight-fork formulation

Fix a directed ordered-(r)-tuple coloring (h) on (V) with
[
h(v_k,ldots,v_1)=1-h(v_1,ldots,v_k).
]
Call a vertex sequence (sigma)-tight, for (sigmain{0,1}), if every consecutive ordered (r)-tuple in the sequence has color (sigma).

### Theorem
The directed NOR conclusion is equivalent to the existence of a color (sigma), an ordered ((r-1))-tuple
[
S=(s_1,ldots,s_{r-1}),
]
and disjoint sequences (A,B), disjoint also from (S), whose vertices together with (S) partition (V), such that
[
P=A,S
qquad	ext{and}qquad
Q=B,S^{m rev}
]
are both (sigma)-tight.

Thus a one-change order is exactly a spanning pair of monochromatic tight paths converging to the same ((r-1))-tuple from opposite orientations.

### Proof
Suppose first that (P=A,S) and (Q=B,S^{m rev}) are (sigma)-tight and span in the stated sense. Form
[
pi=A,S,B^{m rev}.
]
Every (r)-window beginning in the (A)-part is a window of (P), hence has color (sigma). The remaining windows lie in
[
S,B^{m rev}.
]
After reversal, these are precisely the (r)-windows of
[
B,S^{m rev}=Q,
]
in reverse order. Reversal antisymmetry therefore gives color (1-sigma) on every such window. Hence the word of (pi) is
[
sigma^p(1-sigma)^q
]
for (p=|A|) and (q=|B|), so it changes at most once.

Conversely, let
[
pi=(v_1,ldots,v_n)
]
have word
[
sigma^p(1-sigma)^q,
qquad p+q=n-r+1.
]
Put
[
A=(v_1,ldots,v_p),qquad
S=(v_{p+1},ldots,v_{p+r-1}),
]
and
[
B=(v_n,v_{n-1},ldots,v_{p+r}).
]
Then (A,S) consists precisely of the first (p) windows of (pi), so it is (sigma)-tight. Also
[
B,S^{m rev}
]
is the reversal of the suffix
[
S,B^{m rev},
]
whose (q) windows all have color (1-sigma); reversal antisymmetry makes all windows of (B,S^{m rev}) color (sigma). The vertex sets are disjoint outside the common center (S) and cover (V).

The cases (p=0) or (q=0) are included: one branch then has only the center and is vacuously tight.

### Maximal-fork obstruction
Fix a (sigma)-tight fork ((P,Q)) with common reversed center and let (F_P,F_Q) be the ordered first ((r-1))-tuples of its two branches. If an uncovered vertex (x) cannot be prepended to either branch, then
[
h(x,F_P)=h(x,F_Q)=1-sigma.
]
Equivalently, by reversal antisymmetry,
[
h(F_P^{m rev},x)=h(F_Q^{m rev},x)=sigma.
]
Thus every vertex blocking both outward extensions is simultaneously a color-(sigma) right-extension of both reversed branch fronts.

This identifies the remaining augmentation problem sharply: a maximal nonspanning fork can fail only by converting all uncovered vertices into common right-extensions of the reversed fronts. A closure proof may therefore seek an exchange or recentering move that turns such a common right-extension into a strict fork augmentation.

### Audit
The equivalence uses no assumptions beyond reversal antisymmetry and distinctness of the underlying vertices. In particular it does not use topology, fixed excess, or any GN3-specific tournament structure.
