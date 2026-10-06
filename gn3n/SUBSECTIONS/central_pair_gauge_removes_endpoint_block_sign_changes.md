# Central-pair gauge removes endpoint-block sign changes

## Metadata

- ID: central_pair_gauge_removes_endpoint_block_sign_changes
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 36
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Central-pair gauge strengthens localization

The local gauge in [[local_span_gauge_localizes_terminal_tie_break_sign_flips]] can be made independent even of terminal-span endpoint exchanges.

For the selected determining span (I), choose the two positions immediately on opposite sides of its center (the central two positions when (|I|) is even, and the positions adjacent to the unique center when (|I|) is odd). Let their occupants be (u_-,u_+). Reversal exchanges these two positions. With a fixed total order on (V(H)), define the tie orientation by
[
g_c(pi,e)=+1iff u_-<u_+.
]
Then
[
g_c(pi^{m rev},e)=-g_c(pi,e).
]

Thus the selected-edge labeling remains odd, while a gauge-induced sign flip can occur only across an adjacent transposition meeting this central symmetric pair. In particular, permutations in arbitrarily large face blocks crossing either endpoint of (I) cannot flip the tie orientation merely by changing which vertex enters the terminal support.

Together with occurrence persistence this localizes every terminal sign-flip generator to the central part of the bounded determining interval:

- in unique-orientation chambers, a sign flip must alter both reflected occurrences whenever coexistence is protectedly impossible;
- in tie chambers, a sign flip must meet the fixed central gauge pair.

Hence the potentially unbounded endpoint face blocks are sign-neutral factors. Their size no longer enlarges the sign-changing Coxeter rank. This is the appropriate gauge for a protected-carrier repair; the span-endpoint gauge is unnecessarily sensitive to support exchange at the boundary.

## Frontier

- Development version when composed: None
- Development version now: 1
