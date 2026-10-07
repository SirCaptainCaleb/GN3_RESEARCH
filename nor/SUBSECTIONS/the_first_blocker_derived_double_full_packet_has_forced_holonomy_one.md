# The first blocker derived double full packet has forced holonomy one

## Metadata

- ID: the_first_blocker_derived_double_full_packet_has_forced_holonomy_one
- Parent Section: directed_nor_union_closed_bridge
- Position: 184
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## The first blocker-derived double-full packet has forced holonomy one

Work in a minimum coboundary-flat pure-orientation ternary counterexample. Let
[
O=(v_1,ldots,v_m)
]
be a one-change deletion order with word
[
0^p1^q,qquad p,qge3,
]
and let (x) be the omitted perfect blocker with scan
[
s_i=alpha(x,v_i,v_{i+1})=1^{p+1}0^q.
]

The full prepended order
[
(x,v_1,v_2,v_3,v_4,ldots)
]
has initial statuses (1,0,0,ldots). Swap the first two coordinates:
[
(v_1,x,v_2,v_3,v_4,ldots).
]
Its first three statuses are
[
0,1,0.
]
By the perfect-blocker curvature tube, the two bounding tetrahedra
[
{x,v_1,v_2,v_3},qquad
{x,v_2,v_3,v_4}
]
are fully curved. Hence the first five coordinates form a double-full singleton packet.

Write its residual bit in the packet order
[
(a,b,c,d,e)=(v_1,x,v_2,v_3,v_4)
]
as
[
t=alpha(a,b,e)=alpha(a,c,e)=alpha(a,d,e).
]

### Theorem
[
oxed{t=1.}
]

### Proof

Assume (t=0). Consider the full order
[
F=(v_2,x,v_1,v_3,v_4,v_5,ldots,v_m).
]

Its first three statuses are:
[
alpha(v_2,x,v_1)=1
]
by cyclic invariance from (alpha(x,v_1,v_2)=s_1=1);
[
alpha(x,v_1,v_3)=0
]
by full curvature of the first blocker-tube tetrahedron; and
[
alpha(v_1,v_3,v_4)=t=0.
]
All later consecutive windows are the untouched windows
[
w_3,w_4,ldots,w_{p+q}.
]
Therefore (F) has word exactly
[
1,0^p,1^q.
]

Delete its first coordinate (v_2). The remaining order
[
O'=(x,v_1,v_3,v_4,ldots,v_m)
]
has word exactly
[
0^p1^q.
]
Thus (O') is a spanning one-change order of the deletion (Vsetminus{v_2}).

Since the full instance is a counterexample, the omitted coordinate (v_2) must be the unique perfect insertion blocker for (O'). For a (0^p1^q) carrier its scan must begin with (p+1) ones. Because (pge3), in particular its third scan bit must be (1).

But the first three scan bits of (v_2) along (O') are
[
alpha(v_2,x,v_1)=1,
]
[
alpha(v_2,v_1,v_3)=1-alpha(v_1,v_2,v_3)=1,
]
and
[
alpha(v_2,v_3,v_4)=w_2=0.
]
This contradicts the required perfect-blocker prefix (111).

Therefore (t
e0), so (t=1).

### Significance

The endpoint double-full packet produced from a perfect blocker has no free holonomy. Its two-sided boundary-reversal branch is forced.

Equivalently, after the first protected endpoint swap, the local five-set admits the unique two-sided color-1 resolution
[
(x,v_1,v_2,v_4,v_3),
]
using the notation above.

The proof is a protected codimension-two argument: it explicitly tracks the new omitted vertex (v_2) and compares its required blocker scan with inherited face values. No cyclic extremality, wrap-corner flatness, or carrier re-rooting without bookkeeping is used.

## Frontier

- Development version when composed: None
- Development version now: 1
