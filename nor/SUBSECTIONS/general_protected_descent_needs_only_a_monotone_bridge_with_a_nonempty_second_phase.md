# General protected descent needs only a monotone bridge with a nonempty second phase

## Metadata

- ID: general_protected_descent_needs_only_a_monotone_bridge_with_a_nonempty_second_phase
- Parent Section: directed_nor_union_closed_bridge
- Position: 193
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## General protected descent needs only a monotone bridge with a nonempty second phase

Refine subsection 190. Let (h) be a reversal-odd binary label on ordered (r)-tuples, and assume a minimum coordinate counterexample. Let
[
O=(v_1,ldots,v_m)
]
be a one-change deletion order with word
[
0^p1^q
]
and omitted coordinate (x), with (pge r).

Replace (v_p) by (x), preserving the order of every other coordinate:
[
O'=(v_1,ldots,v_{p-1},x,v_{p+1},ldots,v_m).
]

Exactly the (r) windows whose starts are
[
p-r+1,ldots,p
]
change. Let their word be
[
B=b_1cdots b_r.
]
Then the full word of (O') is
[
0^{p-r};B;1^q.
]

### Monotone bridge descent

It is sufficient that
[
B=0^a1^{r-a}
qquad	ext{for some }0le a<r.
]
Then (O') is itself one-change, with run lengths
[
p'=p-r+a=p-(r-a),
qquad
q'=q+r-a.
]
Hence
[
p'<p.
]

Since the ambient full instance is a counterexample, the newly omitted coordinate (v_p) is automatically a perfect blocker for (O'). Therefore every minimum-counterexample theorem can be reapplied to (O'). If such a nontrivial monotone bridge is available for every suitable deletion carrier, iteration gives a strict finite descent of the first run and closes the general coordinate conjecture.

Thus subsection 190's all-ones bridge hypothesis is stronger than necessary.

### Extremal reformulation

Choose, among all one-change deletion witnesses in a minimum counterexample and both color polarities, one with the first run length (p) minimal.

For this extremal witness, every protected replacement bridge is constrained as follows:

- it cannot be (0^a1^{r-a}) with (a<r), because that would produce a deletion witness with smaller first run;
- therefore every bridge is either
  1. the inert word (0^r), which preserves the first-run length, or
  2. contains an adjacent descent (10).

This is a sharper target for the general switch-prism / ordered-tail / Radon program. One need not force an all-ones packet. It suffices to rule out the dichotomy
[
oxed{0^r 	ext{or a bridge containing }10}
]
for all protected exchanges.

The topological labeling problem can therefore focus on the first (10) descent in a nonmonotone bridge, together with a separate mechanism for eliminating the inert (0^r) exchanges. This retains the second-wisdom-pass requirement that all other coordinates stay in the same deletion order.

## Frontier

- Development version when composed: None
- Development version now: 1
