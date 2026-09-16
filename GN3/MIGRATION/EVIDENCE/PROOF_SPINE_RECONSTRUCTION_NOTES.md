# Proof-spine reconstruction notes

This file contains migration status, provenance, topology, audit notes, and open research questions that are intentionally excluded from the mathematical proof-spine documents.

## Status

The GN3 proof spine is a supervised migration reconstruction and has not yet received final GN3 certification.

## File order

The mathematical spine is read from `GN3/PROOF_SPINE/PRELIMINARIES.md`, followed by the two current continuations `FIXED_PAIR_REDUCTION.md` and `LONGEST_PATH_AND_CUBE.md`.

The fixed-pair reduction and the Boolean-cube construction both use the orientation classes determined by a fixed pair `{a,c}`. The globally longest-path argument does not use that setup and gives the shortest known universal entrance to the nonextendable three-path configuration.

The cube construction remains useful because it carries additional comparison information relative to a finite family of maximum spanning three-path forests; it is not needed merely to reach the nonextendable three-path configuration.

## Current mathematical frontier

The fixed-pair line reduces later interaction to the case in which a two-vertex path through a previously treated vertex has one of the two original supports through `{a,c}`. The missing theorem must use the entire later pair of disjoint two-vertex paths, not merely the one meeting the treated vertex, to force a spanning two-path cover or a configuration involving a genuinely new support.

The longest-path/cube line reaches a spanning three-path cover `A|B|C` in which no endpoint of `B` or `C` can be transferred into either end of `A`. The missing theorem is a recursive continuation from that configuration to a spanning two-path cover or to a state decreasing in a genuinely well-founded global order.

A possible synthesis, not yet a theorem, is: strict descent except when the construction remains on an old two-vertex support; then use the fixed-pair construction to rule out indefinite equality.

## Provenance

The small-order argument was reconstructed from the certified E8997 proof. Its finite ingredients correspond to the fixed three-vertex-path extension theorem, the five-vertex Hamiltonian-density results, and the complement-free Johnson `J(10,5)` cut bound.

The fixed-pair line reconstructs the mathematics previously represented by R2185, R2222, R2224, R2226, R2229, R2230, and R2231. The endpoint-selection route is the accepted R224 -> R433 route. The invalidated R2225 and R2228 compositions and the flagged E9006 composition are not used.

The longest-path/cube line reconstructs the surviving mathematics of E8998/R2143, R2136, R2153, and E9003/R2147.

## Language policy

The mathematical files should use ordinary graph-theoretic language. Legacy result numbers, audit statuses, Engine names, migration status, proof-topology commentary, and strategic research discussion belong here or in `GN3/PROVENANCE.md`, not in the proof text.