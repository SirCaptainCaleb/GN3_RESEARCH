# Opposite blocker thicknesses at a shared boundary force collective insertion

## Metadata

- ID: opposite_blocker_thicknesses_at_a_shared_boundary_force_collective_insertion
- Parent Section: hartman_least_unreachable_connectors
- Position: 18
- Row version: 2
- Development version: 2
- Composition version: 1
- Composition stale: False

## Composition

Opposite left/right thicknesses at a common incidence wall supply the six cross incidences for a two-vertex insertion, provided the ordered internal pair is forward in the same gauge. Thickness data alone in arbitrary independently normalized words do not supply that orientation.

## Development

Let r and s be the incidence words of two uncovered vertices relative to one path-normalized connector, and suppose both vertices are individually blocked, so neither word contains 1100 or 0011. Consider a position where both words have the same 1-to-0 boundary: r_i=s_i=1 and r_{i+1}=s_{i+1}=0. Call r left-thick if r_{i-1}=1 and right-thick if r_{i+2}=0, with the analogous definitions for s. Individual blocking implies no word is thick on both sides at this boundary. The two-vertex insertion criterion shows that if r is left-thick and s is right-thick, then the ordered block (a,b) inserts at this gap. If s is left-thick and r is right-thick, the reversed block inserts. Therefore collective blocking forces the two words never to carry opposite thicknesses at a shared boundary. The complemented statement holds at a shared 0-to-1 boundary. This is a genuine pairwise coherence constraint beyond the one-vertex blocker condition.

Elevation audit: the displayed six cross incidences give a pair insertion only in a gauge in which its ordered internal edge a→b is forward. Opposite thicknesses in arbitrary independently normalized incidence words do not establish that internal edge. State the conclusion conditionally on this common pair-normalized gauge; the internal orientation is an independent prerequisite.
