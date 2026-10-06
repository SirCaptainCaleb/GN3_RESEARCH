# Audit of the depth filtration: the remaining same-face gap

## Metadata

- ID: audit_of_the_depth_filtration_the_remaining_same_face_gap
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 5
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development


### Audit of the depth filtration: the remaining same-face gap

The relative-index depth filtration has the right global topology, but its current mixed-face step uses a stronger local statement than the finite terminal theorem presently supplies.

At depth (r), the proof defines
[
Sigma_r=Delta{Finmathcal P_r:s_r(F)=0}
]
and needs
[
Sigma_rsubseteq Y_{r+1}.
]
For a separator vertex (F) containing both (+e_r) and (-e_r), this inclusion requires **the same face (F)** to contain a chamber of depth (>r).

The established paired-witness lemma supplies this in the separable branch: if a face-block boundary separates the two determining windows, blockwise splicing stays inside (F) and produces an outward chamber.

The terminal branch is different. The finite terminal theorem says only that the bounded centered/overlapping determining support has path-cover number at most two. The outward-local-replacement lemma in [[terminal_support_surgery_gives_a_genuine_outward_escape]] upgrades this to an actual spanning order whose selected witness is deeper than (e_r), but that replacement may reorder vertices across block boundaries of (F). Therefore the new order need not be a chamber of (F).

Hence the implication
[
F	ext{ mixed at depth }r
Longrightarrow
Finmathcal P_{r+1}
]
is proved in the separable branch but is not yet justified in the terminal finite branch. In particular, local two-coverability of the terminal support does not by itself establish
[
Sigma_rsubseteq Y_{r+1}.
]

This does **not** reopen the old carrier-reweighting problem. The global depth filtration remains the right framework, and finite-support extension to an outward global order is now available. What remains is a narrower coherence problem: either

1. strengthen the terminal finite theorem to a **face-respecting outward escape**, i.e. show that a terminal mixed face itself contains an outward chamber; or
2. replace the literal inclusion (Sigma_rsubseteq Y_{r+1}) by an equivariant map from (Sigma_r) to the next depth space, using the bounded outward surgery, which is enough for genus monotonicity.

The second option is topologically sufficient because an equivariant map
[
Sigma_r	o Y_{r+1}
]
already implies
[
gamma(Sigma_r)legamma(Y_{r+1}).
]
Thus the exact remaining terminalization task is no longer to construct a new balanced carrier by hand, but to make the bounded terminal replacement **coherent on chains of mixed faces** (or prove the stronger same-face statement).


## Frontier

- Development version when composed: None
- Development version now: 1
