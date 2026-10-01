# All-long deletion states cannot remain in neutral omission-replacement dynamics

## Statement

Let H be a minimum counterexample and let H-x=P|Q be a deletion two-cover with |P|,|Q|>=6. Then at least one of the following occurs: (1) H contains a genuine reversing tight triple; (2) two deletion covers arising in the internal omission-replacement dynamics are support-incompatible or have order disagreement on a common support; (3) H has a spanning three-cover admitting an explicit strict quadratic-potential decrease. In particular, if reversal, support/order disagreement, and strict descent are excluded, one-label internal omission replacements of the stated form cannot persist indefinitely.

## Body

# Proof

Use deletion_long_threeway01 on each displayed component of every deletion state reached below. A one-label internal omission replacement supplied by outcome (2) of deletion_long_threeway01 preserves the order of the replaced component except for swapping the omitted label into the deleted label's internal slot, leaves the opposite component unchanged, and preserves both displayed endpoints of both components. It also preserves the two component orders. Thus every reached state again has both component orders at least six and the same four displayed endpoint vertices as the initial state.

Assume outcomes (1) and (3) never occur. Then from any reached deletion cover F_a=A|B, deletion_long_threeway01 applied to A gives an internal omission replacement of some p in A by a, producing a deletion cover F_p. Applied to B it gives an internal omission replacement of some q in B by a, producing F_q. Each replacement pair is fully compatible on the common domain and the corresponding singleton lifts are adjacent by one legal singleton-swap move.

The two neighbors F_p and F_q are support-incompatible with one another: on their common domain V(H)-{p,q}, the label a is present in both covers, but in F_p it lies in the A-side while in F_q it lies in the B-side. Hence no compatible triangle uses the two opposite-side replacement edges through F_a.

Starting from the initial state, build a walk by alternating replacement sides: after entering a state through a replacement in one displayed component, leave through an internal omission replacement in the other displayed component. This never immediately backtracks. Moreover for every three consecutive states, the first and third covers are support-incompatible by the preceding paragraph, so the walk has no triangular shortcut. The state space is finite, so some state repeats. Take the segment from its first occurrence to its next occurrence. After deleting any earlier repeated subsegments, this yields a simple cycle of deletion-cover states of length at least four.

Every state on this cycle still contains the four original displayed endpoints, because all replacements are internal. Hence the cycle has a nonempty common surviving core. If one omitted label occurs at two distinct states of the simple cycle, the corresponding two covers of the same deletion H-a are distinct; therefore either their support partitions differ or their induced orders differ on a common support, giving outcome (2). Thus, if outcome (2) is also excluded, the cycle has distinct omitted labels.

Now apply the certified singleton-swap cycle theorem swapcycleorderdefect01. The singleton lifts form a cycle of length at least four with distinct omitted labels and nonempty common surviving core, so some two deletion covers on the cycle have order disagreement. This is outcome (2), contradiction.

Therefore at least one of (1)-(3) must occur. ∎
