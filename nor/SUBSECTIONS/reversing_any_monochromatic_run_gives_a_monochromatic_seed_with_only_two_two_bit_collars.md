# Reversing any monochromatic run gives a monochromatic seed with only two two-bit collars

## Metadata

- ID: reversing_any_monochromatic_run_gives_a_monochromatic_seed_with_only_two_two_bit_collars
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 279
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Reversing any monochromatic run gives a monochromatic seed with only two two-bit collars

Let a full ternary order have an arbitrary binary status word, and let
\[
c_r=c_{r+1}=\cdots=c_{r+B-1}=\eta
\]
be any maximal monochromatic run of length \(B\ge1\).

Its exact supporting coordinate interval is
\[
Z=(v_r,v_{r+1},\ldots,v_{r+B+1}).
\]
Reverse \(Z\), leaving every coordinate outside \(Z\) fixed.

Every ternary window wholly inside \(Z\) becomes the reversal of an old \(\eta\)-window, hence by alternation has color \(1-\eta\). Every window wholly outside \(Z\) is unchanged.

Only windows crossing the two ends of \(Z\) can change, and there are at most two on each side. Therefore the reversed order contains a monochromatic seed
\[
(1-\eta)^B
\]
whose entire uncontrolled neighborhood is confined to two collars of at most two status bits each.

If the chosen run is an endpoint run, only one collar exists.

### Counterexample consequence

Apply monochromatic-band combing (§276) to the seed.

Flat endpoint repairs strictly enlarge it. Hence in a counterexample the process must terminate at a fully-curved barrier before the seed reaches both global endpoints. Thus:

\[
\boxed{\text{Every chosen monochromatic run of every full order yields a protected fully-curved root.}}
\]

The protected root may depend on the chosen run and on the deterministic outward repair convention; the statement is existence of an actual protected barrier reachable from that run by a terminating sequence of full-order surgeries.

### Minimum-variation consequence

No separate local classification of variation levels \(3,\ldots,9\) is needed merely to obtain protected roots. For a minimum-change witness at any level, choose any run, reverse its support, and comb the resulting monochromatic seed. The outcome is NOR or a protected root.

Thus all finite variation levels from §262 feed the same protected-root extraction problem.

## Frontier

- Development version when composed: None
- Development version now: 1
