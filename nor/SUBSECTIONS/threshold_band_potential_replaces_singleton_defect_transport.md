# Threshold-band potential replaces singleton-defect transport

## Metadata

- ID: threshold_band_potential_replaces_singleton_defect_transport
- Parent Section: ternary_protected_bridges_and_scan_obstructions
- Position: 40
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

In the coboundary-flat ternary sector, the correct common potential for repeated boundary repairs is not singleton-defect rank but the length B of the maximal contiguous threshold-compatible interval around a chosen one-change cut. If the nearest mismatch outside that interval is supported by a flat boundary tetrahedron, the outward endpoint repair changes (wrong,right) to (right,right), preserves the old compatible interval, and absorbs the mismatch. Hence B strictly increases. Flat boundary repairs therefore cannot cycle; they terminate either in a spanning one-change order or at a fully-curved boundary barrier.

Applied to the residual antipodal braid exits, this removes the need for the unproved E=1 singleton-transport claims. The audited 0100 -> 0011 local change must be evaluated as a complete boundary packet: the extra outer change is allowed, because subsequent flat repair is governed by B rather than defect count. Thus a residual protected exit can be combed outward through all flat boundary states with a genuine well-founded potential.

The remaining antipodal obstruction is correspondingly sharper: after finite flat combing, an unresolved protected exit reaches a fully-curved boundary barrier. Closing the flat sector now requires a boundary-safe crossing of such a barrier, or a proof that the two antipodal exits cannot both terminate at fully-curved barriers in a globally maximal-band state.

## Development

## Threshold-band potential replaces singleton-defect transport

Work in the coboundary-flat ternary sector. For a full coordinate order pi, a proposed threshold cut k, and polarity eta, let B(pi,k,eta) be the length of the maximal contiguous interval of ternary-window ranks containing the cut on which the actual color word agrees with the one-change target.

The current antipodal frontier should be organized by this state, not by the unsupported assertion that a single exported defect remains a singleton.

### Lemma
Suppose the nearest mismatch immediately outside the matched interval lies on a constant-color side of the target, and the tetrahedron supporting the boundary transition (wrong,right) is flat. Then the outward endpoint repair strictly increases B.

Indeed, the flat endpoint repair changes the boundary pair of statuses from (wrong,right) to (right,right) and changes only windows farther outward. Every rank in the old matched interval remains fixed, while the former boundary mismatch becomes matched. Thus B increases by at least one. The reversed argument handles the other side.

Consequently flat boundary repairs admit a common well-founded potential: no sequence which always repairs a nearest flat boundary mismatch can cycle. It terminates either with a spanning one-change order, or with every unresolved boundary of the maximal matched interval supported by a fully-curved tetrahedron.

### Application to the residual antipodal braid
In the caged antipodal state, the two canonical exits are already proved to preserve the outside order on their protected sides. If an exit does not close, choose the threshold cut agreeing with the unchanged protected phase and take its maximal matched interval. The exposed boundary mismatch may then be combed outward whenever its boundary tetrahedron is flat. This iteration is justified by B; it does not require the defect set to remain a singleton and does not require later witnesses to retain the original minimum-first-phase property.

In particular the audited local transformation 0100 -> 0011 is not a reason to abandon the move merely because the defect count changes. The correct invariant is the target-compatible interval. The extra changed outer window must be included in that interval calculation; if it is the new boundary mismatch and its support is flat, the next outward repair strictly enlarges B.

Thus subsections 24/30 should not be used as singleton-defect rank transport. Their intended termination role is replaced by threshold-band combing.

### Remaining obstruction
After this replacement, the antipodal iteration problem has a sharper terminal form: a residual protected exit either closes, or after finitely many flat outward repairs reaches a target-compatible band whose unresolved exported boundary is fully curved. The remaining local theorem is therefore a boundary-safe crossing of a fully-curved barrier (or a proof that the two antipodal exits cannot both terminate at such barriers in a globally maximal-band state).

This imports the older threshold-band potential into Article III as the common potential requested by the current audit, while leaving the genuine fully-curved barrier case open.
