# Pure-sign jumps in a fixed insertion fiber localize to a protected 2r-coordinate packet

## Composition

(none yet)

## Development


Continue the fixed insertion-fiber dichotomy. Let h have ordered-tuple arity r, let O be a fixed one-change deletion order with omitted coordinate x, and let F_j,F_{j+1} be adjacent insertion states obtained by swapping x across one old coordinate.

Assume this edge is the exceptional pure-sign jump: every threshold defect of F_j is positive, while every threshold defect of F_{j+1} is negative.

First, such an edge must occur while the x-packet meets the threshold cut. If every r-window containing x in F_j and F_{j+1} lay entirely on the 0-side, every possible mismatch on both endpoints would be positive. If they lay entirely on the 1-side, every possible mismatch would be negative. Hence the threshold cut lies inside the union of the two local x-packets.

Now let x occupy position k in F_j and position k+1 in F_{j+1}. In F_j the r-windows containing x start at ranks

k-r+1,...,k.

In F_{j+1} they start at

k-r+2,...,k+1.

Therefore the union of all windows whose content can depend on this adjacent move has start ranks

k-r+1,...,k+1,

a total of r+1 windows. Their coordinate support runs from the first coordinate of the start-(k-r+1) window through the last coordinate of the start-(k+1) window, hence contains at most 2r consecutive coordinates.

Every coordinate outside this packet has the same relative order at both endpoints, and every window outside the packet has the same actual color and the same inherited threshold phase.

Thus the remaining fixed-fiber carrier-extraction problem is bounded:

Every minimum-counterexample insertion fiber either exposes a protected 10 descent directly, or contains one adjacent pure-sign jump supported on at most 2r consecutive coordinates around the threshold cut.

No arbitrary permutohedral face is needed. The order of every coordinate outside this 2r packet is fixed and protected.

For r=3 this reduces the exceptional carrier to at most six consecutive coordinates, matching the scale of the audited full/flat and holonomy packets. For general r, the new target is a finite protected 2r-window bridge theorem rather than global path extraction.
