# Audit protected deletion carrier descent closes the flat ternary sector

## Metadata

- ID: audit_protected_deletion_carrier_descent_closes_the_flat_ternary_sector
- Parent Section: directed_nor_union_closed_bridge
- Position: 191
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

In a minimum coboundary-flat alternating ternary counterexample, every one-change deletion carrier has word 0^p1^q with p,q>=4 and an omitted perfect blocker x. The protected reorder H=(v_p,v_1,...,v_{p-1},x,v_{p+1},...,v_m) has word A,0^(p-3),1^(q+3). If A=0, H is a spanning one-change order. Hence A=1; deleting v_p leaves a new one-change deletion carrier 0^(p-3)1^(q+3), now omitting v_p. Counterexamplehood makes v_p its perfect blocker automatically, so the same argument renews. Iteration forces p,p-3,p-6,... all >=4, impossible. Thus directed ternary NOR holds throughout the coboundary-flat alternating sector. The proof uses only audited endpoint blocking, p,q>=4, and the blocker-tube off-diagonal identity; no cyclic extremality, wrap-corner flatness, or untracked local packet surgery is used.

## Development

## Audit: protected deletion-carrier descent closes the flat ternary sector

The closure argument of subsection 187 survives direct index audit.

Let
[
O=(v_1,ldots,v_m)
]
be any one-change deletion carrier in a minimum coboundary-flat alternating ternary counterexample, with
[
w=0^p1^q,qquad p,qge4,
]
and omitted perfect blocker (x) with scan
[
s=1^{p+1}0^q.
]

Construct
[
H=(v_p,v_1,ldots,v_{p-1},x,v_{p+1},ldots,v_m).
]

Its status word is exactly
[
A,;0^{p-3},;1^{q+3},
qquad
A=alpha(v_p,v_1,v_2).
]

The three inserted 1-statuses are:
[
alpha(v_{p-2},v_{p-1},x)=s_{p-2}=1,
]
[
alpha(v_{p-1},x,v_{p+1})
=1-alpha(x,v_{p-1},v_{p+1})
=1-w_{p-1}
=1,
]
using the full blocker-tube tetrahedron (Q_{p-1}), and
[
alpha(x,v_{p+1},v_{p+2})=s_{p+1}=1.
]
All remaining suffix statuses are the old 1-run (w_{p+1},ldots,w_{m-2}).

If (A=0), the full word is (0^{p-2}1^{q+3}), proving NOR. Hence in a counterexample (A=1).

Deleting the first coordinate (v_p) leaves
[
O'=(v_1,ldots,v_{p-1},x,v_{p+1},ldots,v_m)
]
with word
[
0^{p-3}1^{q+3}.
]

This is a genuine one-change order on (Vsetminus{v_p}). Since the ambient full instance is assumed to be a counterexample, no insertion of (v_p) into (O') can yield a good full order; therefore (v_p) is automatically a perfect blocker for this new carrier. No inheritance of the old scan is assumed.

All minimum-counterexample deletion-carrier theorems therefore apply afresh to (O'), in particular the audited lower bound that both run lengths are at least four. Thus either (p-3<4), giving an immediate contradiction, or the same construction applies again and produces first-run lengths
[
p,;p-3,;p-6,ldots
]
all required to be at least four. This is impossible for finite (p).

Hence no minimum counterexample exists in the coboundary-flat alternating ternary sector.

### Status

This is a complete closure of the flat alternating ternary sector, conditional only on the already-audited ingredients:
1. minimum-counterexample endpoint defect / perfect blocker scan;
2. endpoint run lower bound (p,qge4);
3. the perfect-blocker full-curvature tube identity at (Q_{p-1}).

It does not use the withdrawn wrap-corner flatness, cyclic run extremality, unrestricted cellular bubble extraction, or any untracked local packet surgery.

This realizes the second-wisdom-pass strategy criterion: full support is preserved in the surgery, the new omitted coordinate is explicit, the new deletion witness is explicit, and the improvement (pmapsto p-3) is strict and self-renewing.
