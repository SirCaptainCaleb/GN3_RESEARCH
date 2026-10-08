# Outward buffer vertices bypass the internal two-deletion obstruction — preserved pre-item development

## Outward buffer replacement converts a genuine double to a one-triple boundary test

Let a protected positive span-two reflected double have displayed full determining span
[
J=(x,C,y),
qquad
C=(c_1,ldots,c_N),
]
with reflected starts (a<b). Thus (x) is the first vertex of the left determining window and (y) is the last vertex of the right determining window. The internal status word of (C) is positive-word-free.

Let (L) be the set of vertices lying strictly to the left of (x) in the ambient spanning order, and (R) the set lying strictly to the right of (y). Reordering vertices wholly in (L), or wholly in (R), changes only witness starts farther outward than the selected reflected edge.

### Left replacement

Suppose some (ellin L) satisfies
[
h(ell,c_1,c_2)=1.
]
Reorder the left outer prefix so that (x) moves to the old position of (ell) and (ell) occupies the boundary position formerly occupied by (x). Leave (C) fixed.

Every changed status strictly before the old left start (a) is farther outward. At start (a), the new first status is
[
h(ell,c_1,c_2)=1.
]
Since every positive forbidden word
[
001,quad 011,quad 0101
]
begins with (0), no positive witness can now start at (a). All starts strictly inside (C) retain the positive-word-free corridor status.

Thus a single left buffer satisfying the displayed triple removes the left occurrence without creating a witness at the same or more-central depth.

### Right replacement

Dually, suppose some (rin R) satisfies
[
h(c_{N-1},c_N,r)=0.
]
Move (y) into the old outer position of (r) and put (r) in the boundary position formerly occupied by (y), leaving (C) fixed.

Every newly changed status strictly after the old right occurrence is farther outward. The new final internal status is (0). Since every positive forbidden word ends in (1), appending this terminal (0) to the positive-word-free corridor cannot create a new positive witness ending at the right boundary.

### Two-sided buffer lemma

If there exist
[
ellin L,qquad rin R
]
with
[
h(ell,c_1,c_2)=1,
qquad
h(c_{N-1},c_N,r)=0,
]
then the two replacements may be performed simultaneously. The full status word across the old determining span is obtained from the positive-word-free corridor word by adjoining a leading (1) and a trailing (0). This enlarged word is again positive-word-free. All other changed statuses lie strictly farther outward.

Hence the resulting chamber has no positive witness at the selected depth or any more-central depth: it is a genuine outward repair, even when (operatorname{pc}(H[J])>2). This bypasses the no-internal-repair obstruction because the mutable support uses vertices outside (J).

### Blocked-side consequence

Therefore any reflected double that survives this enlarged-window test has at least one completely blocked outward side. Up to reversal, one may assume
[
h(ell,c_1,c_2)=0
qquad	ext{for every }ellin L.
]
Boundary antisymmetry then gives the uniform reverse family
[
h(c_2,c_1,ell)=1
qquad(ellin L).
]

The right-blocked alternative is symmetric:
[
h(c_{N-1},c_N,r)=1
qquad(rin R).
]

Thus a genuine unbounded obstruction is not merely a two-deletion corridor. Unless it already admits an outward repair, an entire outer prefix or suffix is uniformly polarized against one exposed corridor edge. This is a global structural constraint unavailable to surgeries confined to (J).
