# Frontier correction: special scan is closed and arbitrary scan reduces to endpoint square lifting — preserved pre-item development

## Frontier correction after recent Article III developments

Assessment through revision 2862.

### Recent gains that survive audit

1. Width-two full/full threshold corridors are now understood locally.
   - The exact central reflection sends A B B A to B A A B with no exterior spill.
   - A genuinely terminal width-two residue collapses to a rigid six-coordinate table.
   - That rigid table admits a stronger weave (0,3,1,2,4,5) which preserves the right exterior and leaves only one left reconnection bit.
   - If that bit is good, the corridor is crossed. If it is bad, the left packet is exactly a double-full singleton, so the residue hands off to the already-audited one-sided singleton resolution.
   Hence width-two full/full geometry is not an independent terminal obstruction.

2. Closed width-two reflection recurrence has an exact lifted circulation, and a companion rotation realizes each reflection label as an honest protected barrier label. This gives a legitimate recurrence-to-root-circulation route if ever needed. It is secondary after the stronger one-reconnection-bit reduction above.

3. One-exception fans reduce to the ordinary Article III deletion/reinsertion interface: deleting the exceptional coordinate gives a one-change deletion witness with an adjacent clone pair, and reinserting the exception exposes a certified flat/full transition with only bounded outer splice data.

### Strategic correction: the special-scan descent is conditional

The subsection titled “Protected deletion-carrier descent closes the coboundary-flat ternary sector” proves a complete terminating descent under the SPECIAL perfect-blocker scan

s = 1^(p+1) 0^q.

Under that hypothesis, endpoint surgery replaces a one-change deletion carrier with run lengths (p,q) by another carrier with run lengths (p-3,q+3). Reapplication would force p,p-3,p-6,... all to remain at least four, impossible.

This is a complete proof of the special-scan subcase.

The arbitrary-scan flat sector is still live because insertion blocking does not force that special scan. The later audit already states this correctly. Therefore future closure work should treat the special-scan branch as finished and avoid spending effort on its endpoint double-full gadgets.

### Live arbitrary-scan endpoint frontier

For each endpoint witness, the canonical fully-curved endpoint barrier yields a physical root

rho_i = e_{x_i} - e_{x_{i+1}}

carried by a rank-two cut

C_i = {x_i,a_i}

with forced successor

C_i^+ = {x_{i+1},a_i}.

Along a physical endpoint cycle, the next attained cut is

C_{i+1} = {x_{i+1},a_{i+1}}.

Thus every chronological step is a two-edge path in J(n,2). When x_i,x_{i+1},a_i,a_{i+1} are distinct, the missing corner is

M_i = {x_i,a_{i+1}}.

Realizing M_i for the SAME physical root copies the next partner backward:

a_i <- a_{i+1}.

This is the actual square-lift operation presently justified. It is a copy move, not a partner swap. Earlier synchronization arguments requiring a two-witness SWAP lift are correspondingly stronger than the currently established theorem.

### Closure target

Prove the witness-preserving endpoint square-lift lemma in the following affirmative form:

For every nondegenerate Johnson square arising from consecutive endpoint witnesses, the missing corner M_i is realized by a legal endpoint/deletion witness for the same physical root, or the attempted lift yields a full-support one-change order or a strict protected-witness improvement.

Degenerate Johnson triangles already belong to the low-support A2/A3 extraction regime.

If this square-lift theorem is established, the endpoint partner holonomy becomes manipulable by genuine witness moves rather than formal cut algebra. That is the current shortest closure-relevant target for the arbitrary-scan flat sector.

### Guidance

Prioritize the missing-corner realization itself. Use the exact endpoint provenance of the two adjacent attained cuts and the common physical root. Seek an explicit deletion/reinsertion order realizing {x_i,a_{i+1}}. Treat failure as useful: show the failed splice improves the deletion witness or produces a directly extractable A2/A3 packet.

Keep the copy-vs-swap distinction explicit throughout.
