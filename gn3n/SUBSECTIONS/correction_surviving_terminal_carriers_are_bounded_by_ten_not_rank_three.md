# Correction: surviving terminal carriers are bounded by ten, not rank three

## Metadata

- ID: correction_surviving_terminal_carriers_are_bounded_by_ten_not_rank_three
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 31
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False
- Provisional declared dependencies: ["protected_rank_three_coherence_from_terminal_block_compression", "explicit_proofs_for_finite_terminal_compression", "independent_audit_existential_versus_protected_filtration_gap", "rank_two_terminal_carriers_are_genuinely_protected"]

## Cold composition

(none yet)

## Development

## Correction: the rank-three reduction does not cover the surviving terminal branch

The claim in [[protected_rank_three_coherence_from_terminal_block_compression]] that the terminal coupling-block bound (|B|le4) reduces every non-product terminal interaction to Coxeter rank at most three uses that block bound outside its proved scope.

The explicit proof package [[explicit_proofs_for_finite_terminal_compression]] shows the exact situation:

- the block (B) with (|B|le4) is the unique bridging block in a **disjoint single-sided** terminal configuration;
- the disjoint alternating branch is impossible;
- the disjoint span-two branch is also impossible.

Thus after the finite-terminal compression is completed, the branch to which the (|B|le4) theorem applies has disappeared.

The actual surviving terminal configurations are centered witnesses and reflected double/overlapping witnesses. Their *total determining support* is bounded by at most six, eight, or ten vertices depending on type, but the present proof does not show that all sign-changing freedom lies in one block of order at most four. Consequently one may bound the active terminal Coxeter rank by at most nine after factoring off completely disjoint exterior directions, but not by three from the existing block theorem.

Therefore the protected-filtration repair remains open at the following bounded statement:

**Bounded protected terminal-carrier lemma.** For every protected zero face at depth (r) whose nonseparable terminal geometry is centered or overlapping on a determining interval (I) of order at most ten, construct an inclusion-compatible equivariant acyclic carrier lying wholly in (X_{r+1}).

The recent results remain useful inputs:

1. rank-two square/hexagon carriers can be chosen protected;
2. order-nine and order-ten endpoint sign-flip residues are excluded by the protected alternating-word argument;
3. every terminal support has order at most ten, now with explicit proofs in the canonical record;
4. all Coxeter directions completely outside (I) are safe product factors and preserve outwardness.

Hence the remaining global problem is genuinely **finite-dimensional and local to at most ten terminal positions**, but it has not yet been reduced to rank three. Any closure should analyze these centered/overlapping terminal faces directly or prove an additional localization theorem for their sign-changing face blocks.
