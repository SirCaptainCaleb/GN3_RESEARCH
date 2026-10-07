# The long-phase double-splice endpoint branch is a one-defect threshold-band state

## Metadata

- ID: the_long_phase_double_splice_endpoint_branch_is_a_one_defect_threshold_band_state
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 137
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Continue the pinned endpoint surgery of root 128. The only branch left open there has
p>=4,
lambda=alpha(a,c,d)=1,
mu=alpha(a,d,e)=1.

Root 128 constructs the deletion order omitting c
O_c=(x,b,a,d,e,...)
with exact status word
0,0,1,0^(p-3),1^q.

Compare this with the original one-change target
0^p 1^q.
There is exactly one mismatch: rank 3 has value 1 instead of 0. Every rank from 4 through the original phase cut is already 0, and the entire old one-phase suffix is unchanged and equal to 1.

Therefore the maximal target-compatible interval containing the true switch extends from rank 4 all the way to the right endpoint. Its unique unresolved left boundary is the rank-3 mismatch, with local status pair
1,0
across ranks 3,4.

Apply the audited threshold-band boundary theorem.

- If the tetrahedron supporting this 1->0 boundary is flat in the required endpoint direction, perform the boundary repair. Every rank in the old matched interval is preserved, rank 3 becomes matched, and only windows farther to the left may change. Hence the target-compatible band strictly enlarges to the left.

- If the boundary tetrahedron is fully curved, retain its actual protected physical root and stop.

After a flat repair, repeat at the new left boundary of the enlarged matched interval. The band length is a strict integer potential and can increase only finitely many times.

If the process reaches the left endpoint without encountering a full barrier, every window agrees with the target 0^p1^q and O_c is a genuine one-change deletion witness.

Hence the long-phase double-splice branch has the finite dichotomy:
1. a new one-change deletion witness omitting c; or
2. a fully-curved protected-root barrier with the already-clean right suffix retained.

This closes the local branch explicitly left open in the witness-class audit: the case p>=4, lambda=mu=1 does not require a third splice bit. It is a one-defect threshold-band state.

The conclusion is local-to-global handoff, not full NOR closure: the protected-root alternative still requires compatible global extraction.

## Frontier

- Development version when composed: None
- Development version now: 1
