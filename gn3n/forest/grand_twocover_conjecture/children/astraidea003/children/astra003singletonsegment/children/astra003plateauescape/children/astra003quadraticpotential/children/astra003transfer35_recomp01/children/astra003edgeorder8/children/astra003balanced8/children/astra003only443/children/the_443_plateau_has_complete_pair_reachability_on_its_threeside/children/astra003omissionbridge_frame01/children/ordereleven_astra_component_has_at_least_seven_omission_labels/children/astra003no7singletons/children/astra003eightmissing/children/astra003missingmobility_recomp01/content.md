# Eight-label missing-edge shells force three-way mobility or four simultaneous bad extensions

## Statement

Assume the eight-label missing-edge shell and fix a reachable x-omission state P|Q|(x) for a missing omission edge xy. Put G_x=S-{x,y} and E_x=T union {y}; each five-side contains three G_x-labels and two E_x-labels. Reciprocal swaps are only good-good or bad-bad. If g and b are their respective counts, then g+b>=5, b<=4, and g>=1. More sharply, either g>=3, giving at least three distinct Johnson-distance-one moves of the good three-support while singleton x and the bad 2+2 split remain fixed, or b>=3. In the latter case all three unordered 2+2 partitions of E_x are reachable with the good 3+3 split fixed, and for either fixed good three-set A, the four-core A union {x} has C union {e} non-Hamiltonian for every e in E_x.

## Body

Mixed reciprocal swaps would change the required 2+2 distribution of the four bad labels to 1+3, so they are impossible. The reciprocal-swap lower bound supplies at least five cells, all in the 3x3 good-good block or 2x2 bad-bad block. Hence g+b>=5 and b<=4, so g>=1. If b<=2 then g>=3, and distinct good-good cells give distinct Johnson neighbors of the good three-support while preserving singleton and bad split.

If b>=3, at least three of the four cross-cells between the two bad pairs are reciprocal. The four cross-cells fall into two pairs, each pair producing one of the two other unordered 2+2 partitions of E_x. Three cells therefore hit both target classes, so together with the original split all three bad-label pairings are reachable while the good split is fixed.

Fix a good three-set A and C=A union {x}. Across the three reachable bad pairings, whenever {e,f} is the bad pair on the A-side, the six-set A union {x,e,f} has e and f as its two bad deletions; hence both C union {e} and C union {f} are non-Hamiltonian. The three pairings cover every bad label, giving four simultaneous bad extensions of C.