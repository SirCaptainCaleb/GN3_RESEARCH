# Pairwise-blocked shared walls carry a coherent direction

## Composition

Eligible pair-normalized insertions forbid opposite blocker thicknesses at a shared wall. An arbitrary family's incidence words need not admit the required simultaneous internal-edge normalization, so unconditional family-wide wall coherence is not proved.

## Development

Fix one connector gap boundary at which a family of individually blocked incidence words all change from 1 to 0. For each word, individual blocking allows at most one of two thickness flags: left-thick means the preceding bit is also 1, and right-thick means the following bit is also 0. By the collective-insertion theorem, two vertices with opposite thicknesses at this same wall would insert together in one of the two internal orders. Hence in a pairwise-blocked family, left-thick and right-thick words cannot coexist at a shared wall. Every nontrivial shared blocker wall therefore has a coherent orientation: all thick words point left, all point right, or all are thin. The complemented statement holds for a shared 0-to-1 wall. This supplies a discrete directed-wall structure for a Hartman least-unreachable argument.

Elevation audit: the thickness implication is conditional on the relevant ordered pair being forward in the same gauge as its incidence words. There is no proved simultaneous normalization for an arbitrary family. The result therefore forbids opposite thicknesses for eligible pair-normalized insertions; an unconditional family-wide coherent wall direction requires an additional orientation/normalization theorem.
