# Compatible deletion-cover pairs reduce to two-cover, reversal, disturbance, or rail shortening — preserved pre-item development

## Composition

(none yet)

## Development

Let H be a minimum counterexample and let F_a,F_b be deletion covers of H-a and H-b.

If their restricted support partitions agree but their common-support orders disagree, the order-disagreement theorem yields a displayed-edge reversal.

Assume F_a,F_b are compatible. On H-{a,b}, let the common ordered supports be P,Q. The insertion-slot theorem puts a,b into the same common support, say P, in equal or adjacent insertion slots.

1. If the slots are separated, simultaneous insertion gives a spanning two-cover of H.
2. If the slots are adjacent, the insertion-slot theorem gives the positioned reversing triple across the unique core vertex between them.
3. If the slots coincide at an internal gap of P, [[equal_internal_insertion_slots_are_comparison_disturbances_or_endpoint_rooted_supports]] (development v2) gives either:
   - a direct mixed comparison edge / split-or-leave-return disturbance, or
   - inherited rail shortening by two when the gap is an end-edge of P, or
   - a spanning two-cover.
4. If the common slot is an endpoint gap, the corrected same-endpoint analysis [[same_endpoint_backtracking_gives_rooted_rail_shortening]] gives:
   - a spanning two-cover when the second common support has order at most two, or
   - explicit inherited rail shortening by two or four, with the other common rail preserved.

Therefore every support-compatible pair of deletion covers yields one of four structural outcomes:
(a) spanning two-cover;
(b) positioned reversal / order disagreement;
(c) mixed-edge, split-edge, or leave-and-return comparison disturbance;
(d) explicit inherited rail shortening.

In particular there is no remaining featureless compatible-pair or same-endpoint-backtracking state once bare bounded-support outputs are replaced by their retained positional geometry. No small-order cutoff or computation is used.
