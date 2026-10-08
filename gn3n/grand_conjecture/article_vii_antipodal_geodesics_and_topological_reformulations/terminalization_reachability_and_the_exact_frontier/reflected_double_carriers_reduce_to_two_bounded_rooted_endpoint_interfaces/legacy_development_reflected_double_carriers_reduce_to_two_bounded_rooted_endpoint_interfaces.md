# Reflected-double carriers reduce to two bounded rooted endpoint interfaces — preserved pre-item development

## Development

## Reflected-double carriers have a two-cover corridor; only the endpoint interfaces remain

Continue with the consistent positive-word filtration
[
mathcal W_+={001,011,0101}.
]

Let a protected chamber carry both reflected orientations of one selected unsigned witness edge (e_r), with disjoint determining windows (L) and (R). The full span (Lleadsto R) may be arbitrarily long, as shown by [[positive_reflected_double_carriers_have_unbounded_local_spans]].

Nevertheless the unbounded middle has a rigid exact form.

Let (C) be the status interval strictly between the two displayed positive occurrences, after deleting the status coordinates belonging to the two occurrence words themselves. Every positive forbidden occurrence wholly contained in (C) would represent a reflected witness edge strictly closer to the center than (e_r). Protection therefore gives:

**Corridor lemma.**
The middle word (C) avoids
[
001,qquad011,qquad0101.
]
Consequently
[
C=1^a0^b
qquad	ext{or}qquad
C=1^a010^b
]
for some (a,bge0).

Equivalently, the vertex interval underlying the corridor already admits the canonical two-cover order supplied by the exact inversion-window criterion. The length of the corridor is irrelevant: all of its nontrivial order-level structure is one cut, with at most the single (010) exceptional island allowed by the exact language.

This yields a useful decomposition of the reflected-double obstruction.

### Bounded-interface reduction

Choose two bounded endpoint neighborhoods (J_L,J_R), each containing its determining window and enough adjacent corridor vertices to include every positive witness window meeting that endpoint. Their orders are bounded uniformly because positive witnesses use at most six consecutive vertices.

Outside (J_Lcup J_R), leave the chamber order unchanged. The middle corridor remains in its exact two-cover form.

Therefore any repair of the reflected-double branch only has to solve two rooted finite problems:

1. replace the order on (J_L) so that the left selected occurrence disappears while the interface with the frozen corridor creates no positive witness of depth at most (r);
2. do the reversal-symmetric replacement on (J_R).

If such rooted endpoint repairs exist, they may be performed independently when (J_L,J_R) are disjoint. All Coxeter directions supported strictly inside the frozen corridor or outside the two endpoint neighborhoods can then be transported from the protected source face; they do not interact with the repair windows. With inherited masks as in [[frozen_window_carriers_and_separator_relabeling_require_precise_invariants]], these directions give contractible permutahedral product factors.

Thus the reflected-double branch does **not** require a two-cover theorem on its entire, potentially unbounded determining span. It requires a finite **rooted endpoint surgery theorem** compatible with a frozen positive-word-free corridor.

A sufficient endpoint statement is:

**Rooted positive endpoint surgery (remaining local obligation).**
Let (J) be the bounded neighborhood of one reflected positive witness, with its inward boundary attached to a positive-word-free corridor. Then there is a reorder of (H[J]) which removes the selected occurrence and such that every newly created positive witness meeting the inward boundary is farther outward than the selected edge (equivalently, no at-most-depth-(r) witness is created across the frozen interface).

The ordinary eight/ten-vertex two-cover theorem does not include this rooted boundary condition, so it cannot simply be cited. The prescribed-endpoint and six-set transport tools are natural inputs, but an explicit rooted proof is still required.

### Consequence for the current frontier

The consistent positive-only route now has the following shape.

- Exclusive disjoint span-two carriers have support at most ten and are handled by ordinary finite surgery.
- Exclusive disjoint alternating carriers are impossible by [[positive_word_filtration_is_antipodal_and_exclusive_alternating_windows_collapse]].
- Reflected-double carriers may have arbitrarily long spans, but their middle corridor is already a frozen two-cover order; only two bounded rooted endpoint interfaces remain.
- Once rooted endpoint surgery is proved, the frozen-window/inherited-mask carrier construction can be applied to the two endpoint windows and the safe corridor/exterior product factors.

So the polarity mismatch has been replaced by a finite rooted-interface problem rather than an unbounded terminal-support problem.
