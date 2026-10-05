# Repair frontier: protected iteration reduced to finite terminal compression

## Metadata

- ID: repair_frontier_protected_iteration_reduced_to_finite_terminal_compression
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 29
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

## Repair frontier after the protected-carrier audit

The failed existential filtration should not be repaired by returning to \(Y_r\). The correct iteration target is the protected complex
\[
X_r=\{F:\text{every chamber of }F\text{ has selected witness depth at least }r\}.
\]

The remaining obligations are now finite.

1. [[protected_rank_three_coherence_from_terminal_block_compression]] shows that, **conditional on the terminal coupling-block bound \(|B|\le4\)**, every genuinely non-product terminal Coxeter interaction has rank at most three.
2. Rank two is already closed by safe transport/collapse plus endpoint exclusion.
3. Rank three is closed as follows:
   - determining span at most eight: two slack positions in the ten-window collapse the whole \(A_3\) residue;
   - determining span nine: simultaneous reflected alternating occurrences force a strictly more central alternating witness, so endpoint sign-flip edges are impossible;
   - determining span ten: the existing maximal endpoint-exclusion lemma applies.
4. Exterior face blocks are disjoint safe permutahedron factors. Every chamber in those factors remains outward, so their products are protected and contractible.

Thus the earlier “arbitrary higher-dimensional acyclic carrier” problem is no longer the frontier. The load-bearing unresolved point is the finite-terminal compression itself: provide explicit proofs of the block-size/cross-intersection statements used to obtain \(|B|\le4\) and eliminate the disjoint single-sided terminal branches.

In particular, the next repair attempt should focus on the finite protected face combinatorics listed in [[independent_audit_finite_terminal_compression_proof_obligations]], not on further Coxeter coherence or on the existential face filtration.
