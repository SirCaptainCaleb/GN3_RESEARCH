# Dual-polarity witness reduction

**Summary:** Selecting the nearest local inversion witness in either color direction makes every two-sided occurrence bounded near the center.

## Statement

Use local witnesses in both color directions and select the witness-location pair nearest the status-word center. A noncentered witness occurring on both reflected sides has start separation at most 3 for three-bit witnesses and at most 4 for four-bit alternating witnesses.

## Body

The local witnesses are the three patterns for a nonadjacent zero-to-one inversion together with their color complements. An interval avoiding all six has no unequal pair of bits at distance at least two, so an interval of length at least four is monochromatic. Between two reflected copies of the nearest selected witness there is no closer witness of either color direction. Their inward-facing bits are opposite. Hence the intervening interval has length at most two, giving the stated separation bounds. Centered self-reflecting witnesses are handled separately by the antipodal tie-break sign.

## Metadata

- ID: dual_polarity_witness_reduction
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Limbo
