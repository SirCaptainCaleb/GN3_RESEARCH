# Inert protected exchanges force a mutual blocker pair defect — preserved pre-item development

## Development

## Inert protected exchanges force a mutual-blocker pair defect

Work in a minimum coordinate counterexample for a reversal-odd binary label on ordered (r)-tuples. Choose a one-change deletion carrier
[
O_y=(v_1,ldots,v_{p-1},y,v_{p+1},ldots,v_m)
]
with word
[
0^p1^q,
]
where (y=v_p), and let (x) be the omitted coordinate.

Assume the protected replacement of (y) by (x) is inert:
[
O_x=(v_1,ldots,v_{p-1},x,v_{p+1},ldots,v_m)
]
also has word exactly
[
0^p1^q.
]

Then (x) and (y) form a mutual blocker pair over the common codimension-two core
[
C=(v_1,ldots,v_{p-1},v_{p+1},ldots,v_m).
]
Indeed (x) blocks every insertion into (O_y), while (y) blocks every insertion into (O_x), because the ambient full instance is a counterexample. The reverse protected replacement is also inert, since it recovers (O_y).

### Pair-defect theorem

Consider the two full orders obtained by inserting both blockers consecutively at the common protected gap:
[
F_{xy}=(v_1,ldots,v_{p-1},x,y,v_{p+1},ldots,v_m),
]
[
F_{yx}=(v_1,ldots,v_{p-1},y,x,v_{p+1},ldots,v_m).
]

For (F_{xy}), all windows strictly before the local insertion packet are inherited zeros. The local insertion packet consists of (r) new windows. Its final window is
[
h(y,v_{p+1},ldots,v_{p+r-1}),
]
which is exactly the protected start-(p) window of (O_y), hence equals (0). After this packet, the untouched suffix begins with the old start-(p+1) window, hence has color (1).

Therefore, if the first (r-1) local windows of (F_{xy}) were all (0), the full word would be
[
0^*1^*
]
and NOR would hold. Counterexamplehood forces at least one of those first (r-1) windows to have color (1).

Every one of those first (r-1) local windows contains both (x) and (y).

The same argument applied to (F_{yx}) shows that its first (r-1) pair-crossing windows also contain at least one (1).

Thus every inert protected exchange canonically produces two nonempty pair-defect sets
[
D_{xy},D_{yx}subseteq{1,ldots,r-1},
]
recording the positions of color-1 windows containing both blockers in the two pair orders.

### Significance

At a first-run-minimal deletion witness, subsection 193 says every protected bridge is either inert (0^r) or contains a (10) descent. The inert branch can now be replaced by a lower-dimensional protected obstruction: a mutual blocker pair on a fixed codimension-two core carrying nonempty pair-defect packets in both pair orientations.

This suggests a two-level carrier strategy:
1. noninert bridges are labeled by their first (10) descent;
2. inert bridges are labeled by their induced pair-defect data on the common codimension-two core.

No arbitrary permutation-face connectivity is used; all data live in the same-deleted-order fibers required by the second wisdom pass.
