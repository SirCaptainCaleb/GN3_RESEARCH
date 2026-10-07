# Closed repair loops have even aggregate winding on odd status cycles

## Metadata

- ID: closed_repair_loops_have_even_aggregate_winding_on_odd_status_cycles
- Parent Section: directed_nor_union_closed_bridge
- Position: 137
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Lift the cyclic transition positions to integers along a repair walk. A successful right repair moves one transition by +2 or +3; a left repair moves one transition by -2 or -3. Modulo 2, the signed displacement of a move is exactly the transport selector lambda. The global J2 potential gives xor lambda=0 on every closed repair loop, so the total lifted displacement is even. If the cyclic status length m is odd and the final transition set equals the initial set, the total lifted displacement is m times an aggregate winding number W, defined from the sum of lifted transition positions. Hence W is even. Therefore no equality-only closed repair loop on an odd status cycle can return after odd aggregate winding. In particular, any singleton-trap propagation that restores the same local state only after one full circuit would contradict the J2 law. This does not yet prove that every closed component has such a return, but it turns the parity target into a geometric winding statement.

## Frontier

- Development version when composed: None
- Development version now: 1
