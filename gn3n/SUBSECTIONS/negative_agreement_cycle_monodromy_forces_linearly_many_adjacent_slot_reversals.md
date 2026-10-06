# Negative agreement-cycle monodromy forces linearly many adjacent-slot reversals

## Metadata

- ID: negative_agreement_cycle_monodromy_forces_linearly_many_adjacent_slot_reversals
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 222
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Retain the compatible negative spanning support-agreement cycle in its odd single-switch normal form, with n=2r+1 and two ordered path supports of size r in every deletion cover. Assume path orders agree on every agreement edge, so each transition between consecutive holes has equal or adjacent insertion slots. Include the current hole as a distinguished extra position beside the 2r ordered path slots. An equal-slot transition replaces the next hole label in one fixed path slot and is therefore one star transposition involving the hole position. An adjacent-slot transition shifts the unique intervening core vertex by one slot and is therefore a star 3-cycle involving the hole position; equivalently it is a product of two star transpositions. After one full traversal, the hole returns to itself while the negative support identification exchanges the two ordered r-lists. Thus the resulting permutation on the 2r+1 positions is the product of r disjoint transpositions exchanging corresponding positions of the two paths. Let A be the number of adjacent-slot transitions. Expanding every star 3-cycle into two star transpositions gives a factorization of this final permutation into 2r+1+A star transpositions about the hole position. A permutation fixing the pivot and consisting of r disjoint 2-cycles requires at least 3r star transpositions: all 2r moved positions must occur, and each target cycle disjoint from the pivot requires at least one of its positions to occur a second time in order for the pivot to enter and leave that cycle while ending fixed. Hence 2r+1+A>=3r, so A>=r-1. Therefore the exceptional compatible agreement cycle carries at least r-1 adjacent-slot positioned reversals. In particular the reversal core has positive linear density around the cycle; it cannot be treated as one isolated disturbance.

## Frontier

- Development version when composed: None
- Development version now: 1
