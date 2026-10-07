# After crossing the flip block the surviving defect becomes a monotone one-band

## Metadata

- ID: after_crossing_the_flip_block_the_surviving_defect_becomes_a_monotone_one_band
- Parent Section: ternary_protected_bridges_and_scan_obstructions
- Position: 59
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## After crossing the flip block the surviving defect becomes a monotone one-band

Continue from subsection 58 in the branch h_{j-4}=1 and lambda=0. After deleting v_{j-2} and performing the three forced forward endpoint repairs, the local order has the form

(..., q,r,x,u,d,a,c,b,e, ...)

and every consecutive ternary status from alpha(q,r,x) through alpha(c,b,e) is 1.

All windows strictly before q,r are unchanged old zero-phase windows. The untouched suffix to the right eventually consists of the old zero phase followed by the original one phase.

Therefore the modified order has a distinguished contiguous 1-band lying inside the old zero phase. Its left endpoint is already fixed; only its right boundary needs to move.

### Monotone rightward combing

Apply the audited threshold-band repair theorem to the right boundary of this 1-band.

At each boundary transition 1->0:

- if the boundary tetrahedron is flat in the required endpoint direction, perform the corresponding adjacent repair; the entire changed window packet is checked by the threshold-band theorem, the old 1-band is preserved, and its right endpoint moves strictly right;
- if no such flat repair is available, the terminal boundary is fully curved and emits its protected physical slide root.

Because the right endpoint advances in the finite coordinate order, the flat-repair branch cannot cycle.

### Terminal alternatives

If the advancing 1-band reaches the original 1-phase of the deletion carrier, the intervening old zero segment has been absorbed. The complete status word is then

0^*1^*,

so a one-change deletion carrier has been produced.

Otherwise the process stops earlier at a fully-curved 1->0 boundary, producing a protected root while preserving the already repaired left state.

Thus the lambda=0 branch of subsection 58 does not require further local chord classification. It enters the global Article III dichotomy with a one-sided monotone potential:

right endpoint of the inserted 1-band strictly advances, or a protected root is emitted.

Combined with subsection 58, the h_{j-4}=1 branch now has only two outcomes:
- lambda=1: immediate full barrier and root;
- lambda=0: finite rightward combing to either NOR on the deletion carrier or a full barrier and root.

Hence the special perfect-blocker branch reduces completely to either an explicit one-change full/deletion order or a protected root certificate. What remains globally is to exploit the emitted roots with their retained provenance; no recurrent local transport remains in this special-scan branch.

## Frontier

- Development version when composed: None
- Development version now: 1
