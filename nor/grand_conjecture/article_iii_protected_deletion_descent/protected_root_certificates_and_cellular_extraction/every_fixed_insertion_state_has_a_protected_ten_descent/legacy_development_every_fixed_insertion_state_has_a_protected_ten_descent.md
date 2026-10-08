# Every fixed insertion state has a protected ten descent — preserved pre-item development

## Every fixed insertion state has a protected ten-descent

Let (h) be any reversal-odd binary label on ordered (r)-tuples. Let
[
O=(v_1,ldots,v_m)
]
be a one-change deletion order in a minimum coordinate counterexample, with word
[
0^p1^q,
]
and let (x) be the omitted coordinate.

For each gap (j), let (F_j) be the full order obtained by inserting (x) in that gap while preserving the relative order of all (v_i).

### Theorem

Every (F_j) contains an adjacent actual-color descent
[
10
]
such that at least one of the two participating (r)-windows meets (x).

Equivalently, every insertion-fiber state carries a protected physical root (e_a-e_c) after allowing the two boundary adjacencies of the (x)-packet.

### Proof

The full instance is a counterexample, so the binary window word of (F_j) has at least two changes.

Every (r)-window of (F_j) that does not meet (x) is an unchanged window of (O). Deleting from the word of (F_j) the contiguous packet of windows meeting (x) therefore leaves a subsequence of the old word
[
0^p1^q.
]
In particular, among two adjacent windows of (F_j) that both lie strictly outside the (x)-packet, a (10) descent is impossible: before the old switch they are (00), after it they are (11), and at the old switch they are (01).

Any binary linear word with at least two changes contains a (10) descent. Hence some (10) descent exists in (F_j), and by the previous paragraph it cannot be supported entirely outside the (x)-packet. Thus at least one of its two windows meets (x).

Sliding from the first window of this descent to the second drops one physical coordinate (a) and enters one physical coordinate (c), giving the protected root
[
e_a-e_c.
]
The descent may lie internally in the (x)-packet or across one of its two packet boundaries.

### Endpoint behavior and trajectory

At the left endpoint (F_0), counterexamplehood forces the new first window to have color (1), while the first old window has color (0). Hence the leftmost protected descent occurs at the extreme left boundary.

At the right endpoint (F_m), the last old phase is color (1) and counterexamplehood forces the new final window to have color (0). Hence a protected descent occurs at the extreme right boundary.

As (j) increases by one, the support of every possible protected descent is contained in the union of the two adjacent (x)-packets, which has at most (r+1) affected window ranks and at most (2r) coordinates.

Thus the fixed insertion fiber carries a bounded **descent trajectory** from the left endpoint of the threshold word to the right endpoint. The remaining extraction problem is not existence of a root certificate; it is to control a jump of the descent trajectory across the threshold cut between two adjacent insertion states.

### Relation to §§201–203

This strengthens the fixed-fiber dichotomy. Pure-sign defect states do not eliminate root descents: if a pure-sign state were free of (10), its whole actual word would itself be monotone (0^*1^*), contradicting counterexamplehood. What can remain exceptional is only a one-edge relocation of all available protected descents from one side of the threshold cut to the other.

That exceptional jump is automatically confined to the same protected (2r)-coordinate packet identified in §203.
