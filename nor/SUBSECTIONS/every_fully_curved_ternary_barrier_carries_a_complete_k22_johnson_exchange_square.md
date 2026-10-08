# Every fully-curved ternary barrier carries a complete K22 Johnson exchange square

## Metadata

- ID: every_fully_curved_ternary_barrier_carries_a_complete_k22_johnson_exchange_square
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 230
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## A fully-curved tetrahedron realizes the complete (K_{2,2}) exchange square at one central cut

Strengthen the preceding side-root observation.

Let four consecutive coordinates in a full order be
[
(a,b,c,d)
]
and suppose they carry a fully-curved transition normalized as
[
alpha(a,b,c)=1,qquad alpha(b,c,d)=0.
]
Full curvature gives the off-faces
[
alpha(a,b,d)=0,qquad alpha(a,c,d)=1.
]

Let (C) be the central prefix cut, taken immediately after the first two positions of this four-coordinate block. Thus
[
a,bin C,qquad c,d
otin C.
]

Consider the four orders obtained by independently swapping the left endpoint pair and the right endpoint pair.

1. Original:
[
(a,b,c,d):quad 1,0,
]
so the root is
[
a	o d.
]

2. Swap the right pair:
[
(a,b,d,c):quad
alpha(a,b,d)=0,quad alpha(b,d,c)=1,
]
so the root is
[
a	o c.
]

3. Swap the left pair:
[
(b,a,c,d):quad
alpha(b,a,c)=0,quad alpha(a,c,d)=1,
]
so the root is
[
b	o d.
]

4. Swap both endpoint pairs:
[
(b,a,d,c):quad
alpha(b,a,d)=1,quad alpha(a,d,c)=0,
]
so the root is
[
b	o c.
]

Each of the four displayed transitions is fully curved. For example, the two off-faces in case 4 are
[
alpha(b,a,c)=0,qquad alpha(b,d,c)=1,
]
which is the fully-curved off-face pattern for a (1	o0) transition; the other cases are analogous.

Crucially, all four orders have the **same central cut as a set**:
[
C=	ext{(old prefix)}cup{a,b}.
]
Only the order within the two-element inside block ({a,b}) and the two-element outside block ({c,d}) changes.

Hence one fully-curved barrier realizes the complete bipartite family of same-rank exchanges
[
oxed{
a	o c,quad a	o d,quad b	o c,quad b	o d
}
]
from the same Johnson vertex (C).

Equivalently, if
[
C_{uv}=C-{u}+{v}
qquad(uin{a,b}, vin{c,d}),
]
then the four realized roots are exactly
[
mathbf 1_C-mathbf 1_{C_{uv}}=e_u-e_v.
]

### Rank-two consequence

The four roots satisfy the exact square relation
[
(e_a-e_c)+(e_b-e_d)
=
(e_a-e_d)+(e_b-e_c).
]
Thus a fully-curved terminal barrier does not merely emit one isolated root. It canonically carries a complete rank-two exchange square in the Johnson layer of its central cut.

This is stronger than a generic physical-root label: the square is realized by the four endpoint-orderings of the *same tetrahedron*, with no corner-lift hypothesis and no partner-alignment choice.

### Why this matters for the circuit frontier

The global protected-root obstruction should therefore be studied as a cellular object whose full barriers contribute genuine Johnson squares. In particular:

- if a positive circuit uses one edge of such a square and meets one of the two middle coordinates elsewhere, another edge of the same realized square is a directed chord candidate;
- commuting ambiguity at a single fully-curved barrier is already resolved locally: all four exchange corners exist at the same central cut;
- the remaining coherence problem is only how these canonical squares glue when consecutive roots come from different barrier packets.

So the local rank-two cell required by the proposed compatible equivariant complex is present automatically at every fully-curved ternary barrier.

## Frontier

- Development version when composed: None
- Development version now: 1
