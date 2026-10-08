# Audit correction: same-position replacement is already implied by insertion

## Metadata

- ID: exchange_minimal_blocker_words_are_alternating_with_at_most_one_thick_run
- Parent Section: monochromatic_connector_blocks
- Position: 18
- Row version: 2
- Development version: 2
- Composition version: 1
- Composition stale: False

## Composition

The proposed same-position replacement strengthening is redundant: its skipped-bit 1100/0011 condition already implies an adjacent insertion. No stronger run restriction follows. A genuine exchange must relocate the displaced coordinate or involve several coordinates; the informative failed strengthening is retained.

## Development


The proposed exchange strengthening was redundant.

In path-normalized square-path gauge, replacing c_i by an uncovered vertex a would require
(r_{i-2},r_{i-1},r_{i+1},r_{i+2})=1100
or 0011
after choosing the switch state of a.

But the skipped bit r_i has one of the two binary values. If the displayed pattern is 1100, then:
- when r_i=0, the consecutive substring (r_{i-2},r_{i-1},r_i,r_{i+1}) is 1100;
- when r_i=1, the consecutive substring (r_{i-1},r_i,r_{i+1},r_{i+2}) is 1100.
Thus an interior insertion was already available at an adjacent gap.

The same argument applies to 0011.

Therefore a vertex blocked from all interior insertions is automatically blocked from the same-position one-for-one replacement considered here. No additional run-structure conclusion follows.

The valid obstruction remains the exact one from the preceding subsections: the incidence word avoids consecutive 0011 and 1100, equivalently no boundary has two constant runs of length at least two on both sides.

Any genuinely stronger support-preserving exchange must move the displaced connector vertex to a different position, or perform a multi-vertex exchange. That is the correct next target for the collective whole-shore repair complex.
