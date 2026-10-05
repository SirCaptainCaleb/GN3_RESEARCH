# Local forbidden patterns and witness handoff

## Metadata

- ID: spanning_orders_and_defect_helly_subsection_c
- Parent Section: spanning_orders_and_defect_helly
- Position: 3
- Row version: 3
- Development version: 3
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

The exact criterion
[
q(pi)le p(pi)+1
]
has a finite local form. A bad word has a zero followed by a one at distance at least two. Choose such a pair with minimum separation.

If the separation is two, the three-bit subword is (001) or (011). If the separation is at least three, minimality forces every position immediately after the first zero to be (1), and every position immediately before the last one to be (0). Separation at least four would force an overlap carrying both values, so the only remaining case has separation three and subword (0101).

Therefore
[
oxed{
qle p+1
iff
epsilon_1cdotsepsilon_m	ext{ avoids }001, 011, 0101.
}
]

Thus every failure of the exact two-cover criterion is witnessed on at most four consecutive status positions.

Under reverse-complement, (001) and (011) exchange, while the alternating pattern is the centered self-reflecting type. These local witnesses are the inputs to the fixed witness-path topology developed later in [[local_witness_topology_and_the_finite_terminal_theorem]].

Complementing all triple colors preserves path-cover number after reversing each path, so the opposite-polarity witnesses
[
110, 100, 1010
]
may be tracked simultaneously. This dual-polarity refinement is what removes the formerly unbounded symmetric-double witness branch.
