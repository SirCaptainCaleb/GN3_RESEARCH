# Degree-saturated connected lifted circuits expose a complementary A3 pair or a one-exception fan

## Metadata

- ID: degree_saturated_connected_lifted_circuits_either_repair_in_a3_or_force_one_exception_fans
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 208
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## A fixed-cut A3 alternative for degree-saturated connected lifted circuits

Work in the pure alternating ternary sector with the honest switch-prism labels
[
widehatho=(ho,s)in Woplusmathbb R,
]
using the nearest-violation selector. Fix a deterministic reversal-compatible tie rule which, in one initial-color copy, prefers the post-side violation among equally near pre/post violations; use the reversed preference on the reversal-mate copy.

Suppose a support-minimal positive lifted zero is genuinely multi-cycle, has connected physical support, and uses every physical coordinate. The physical support is then a connected bicyclic circuit (figure-eight or theta).

### One-block horizontal carrier

Let (F) be the ordered-partition face carrying the zero. Every support root is weakly forward in the (F)-block order. Every support edge lies on a directed physical cycle, so the total block increment around each cycle is zero. Hence every support edge is block-neutral. Connectivity and full physical support force all coordinates into one tied block. Thus the horizontal carrier is the top permutahedron face: every coordinate order is an allowed chamber refinement.

### Fixed-cut locality

Keep one active vertical cut fixed. The top horizontal face lets us move any chosen four coordinates into the four ranks surrounding that fixed cut. This is different from taking a far-away violating window and moving the cut vertically to it; no long vertical transport is used.

Choose a pre-side support label
[
(e_a-e_c,+1)
]
coming from a selected violating window ((a,b,c)). Let the pre-switch target be (eta), so
[
alpha(a,b,c)=1-eta.
]

For any (d
otin{a,b,c}), use the exact A3 refinement
[
a,b,c,d
]
with the fixed switch between
[
L=(a,b,c),qquad R=(b,c,d).
]

If
[
alpha(b,c,d)=1-eta,
]
then (R) matches the post target and (L) is the nearest central pre-side violation, so the selector chooses ((e_a-e_c,+1)).

In the reversed A3 chamber
[
d,c,b,a,
]
the post-side internal window is ((c,b,a)), whose color is
[
alpha(c,b,a)=1-alpha(a,b,c)=eta.
]
Hence it violates the post target. With the stated reversal-compatible tie rule the selected label is
[
(e_c-e_a,-1)=-(e_a-e_c,+1).
]

Therefore this one exact A3 product carrier contains an honest two-term complementary lifted pair with the same physical middle (b).

### Fan alternative

Consequently we have the following purely local dichotomy for every pre-side support label ((a,b,c)):

1. for some (d
otin{a,b,c}), an exact cut-adjacent A3 carrier contains the complementary pair
   [
   (e_a-e_c,+1),quad(e_c-e_a,-1);
   ]
   or
2. for every (d
otin{a,b,c}),
   [
   alpha(b,c,d)=eta.
   ]

In the second case cyclic invariance gives
[
alpha(b,c,a)=alpha(a,b,c)=1-eta,
]
so ((b,c)) has the one-exception fan
[
alpha(b,c,x)=
egin{cases}
1-eta,&x=a,\
eta,&xin Vsetminus{a,b,c}.
end{cases}
]

The post-side statement is obtained symmetrically: a post-side support label ((a,b,c)) either exposes a fixed-cut complementary A3 pair or forces a one-exception fan on its leading pair ((a,b)), with exceptional coordinate (c).

### Audit qualification

This subsection does **not** claim that the existence of the complementary A3 pair is already a terminating global repair. The later four-window audit shows that unrestricted neighbor-replacement paths need not decrease the previously proposed potential. Thus the valid conclusion here is carrier extraction: complementary A3 pair OR one-exception fan.

Any use of the fan alternative as a forced property of a counterexample must first rule out or correctly resolve the complementary-pair branch with an audited extraction theorem.

## Frontier

- Development version when composed: None
- Development version now: 2
