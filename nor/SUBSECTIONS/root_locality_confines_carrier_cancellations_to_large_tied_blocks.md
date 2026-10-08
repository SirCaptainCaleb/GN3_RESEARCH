# Root locality confines carrier cancellations to large tied blocks

## Metadata

- ID: root_locality_confines_carrier_cancellations_to_large_tied_blocks
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 367
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

In an ordered-partition cell whose root labels come from actual refining chamber orders, a block-rank functional is nonpositive on each source-to-target root. A zero positive combination therefore uses only within-block roots. Window-slide roots span r+1 consecutive coordinates, so their noninert cancellations require a tied block of size at least r+1; outermost-change roots require r+2. The remaining positive roots form a balanced flow and hence contain a directed cycle in one tied block. Ternary thresholds are four and five coordinates. Adjacent-swap refinement destroys the same window-slide certificate; packet-sized realization and the inert-zero attachment analysis remain the exact obligations.

## Development

Combination of the ordered-partition geometry in Article II §228, the physical window-slide dictionary in §225, and the all-arity outermost carrier.

Theorem. Let F=B_1|...|B_s be an ordered-partition cell. Suppose every root contributing to its affine labels is attached to an actual coordinate order refining F. Orient every root from an earlier coordinate of that order to a later one. Choose a block-rank functional φ(e_a−e_c)=rank_F(a)−rank_F(c). Every contributing root has φ≤0. If a positive weighted sum of these roots is zero, each contributing root with positive weight must have φ=0. Thus every surviving cancellation edge lies entirely in one tied block.

For a physical window-slide root e_{v_i}−e_{v_{i+r}}, its endpoints are r positions apart and the whole contiguous (r+1)-coordinate packet lies in that same block. Hence a noninert window-root zero requires a tied block of size at least r+1 and cell dimension at least r. For an outermost-change root e_{v_p}−e_{v_{q+r}}, p<q, the analogous block has size at least r+2 and dimension at least r+1. In ternary arity these thresholds are four and five coordinates respectively.

The conclusion also holds when vertex labels are positive sums of physical roots: expand the affine zero into its contributing roots before applying φ. The positive roots in each tied block form a balanced directed flow, since every coordinate coefficient of the sum vanishes. Any nonempty finite balanced directed flow contains a directed cycle, obtained by following a positive outgoing edge until a vertex repeats. Thus a zero supplies a directed root cycle entirely within an appropriately large contiguous tied block.

This sharpens the two-opposite-root observation: the common tied block must contain the full ordered packet, not just its two endpoint coordinates. Refining that block to an adjacent-swap edge with those endpoints next to each other destroys the same physical window-slide certificate for r≥2. A valid extraction should retain a packet-sized block or explicitly change the certificate.

Scope. The labels must come from chamber orders refining the stated common cell; arbitrary incident labels or omitted-coordinate roots do not satisfy this locality premise. Inert zero labels require the separate local attachment/isolation analysis. Localization alone does not realize the directed cycle as a global legal path.
