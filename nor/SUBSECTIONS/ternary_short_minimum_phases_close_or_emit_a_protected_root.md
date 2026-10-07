# Ternary short minimum phases close or emit a protected root

## Metadata

- ID: ternary_short_minimum_phases_close_or_emit_a_protected_root
- Parent Section: ternary_protected_bridges_and_scan_obstructions
- Position: 61
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

For globally minimum ternary deletion carriers, p=1 closes directly. At p=2, blocking and replacement force a full-flat singleton 010 packet; its monochromatic five-coordinate resolution removes the left reconnection, and threshold-band combing on the right either reaches the old one-phase and yields a spanning one-change order or stops at a fully-curved boundary with a protected root. Thus short minimum phases do not form an escape case: p<=2 closes or hands off to protected-root extraction.

## Development

For a globally minimum ternary deletion carrier, p=1 is impossible: front blocking forces s1=1, and inserting x after v1 gives a one-change full word for either value of s2. For p=2, blocking forces s1=s2=1. Replacing v2 by x shows s3=0, since s3=1 would give either a shorter first phase or a monochromatic deletion witness. Hence (v1,x,v2,v3,v4) has pattern 010, with the left transition tetrahedron fully curved and the right one flat. The existing full-flat singleton theorem gives a monochromatic five-coordinate resolution beginning with the endpoint pair (x,v1), so there is no left reconnection. Combing the right boundary by the threshold-band potential either reaches the untouched old one-phase and yields a spanning one-change order, or stops at a fully-curved boundary and emits a protected root. Thus p=1 closes directly, p=2 closes or emits a root, and the ternary program has no short-phase escape from the root handoff.
