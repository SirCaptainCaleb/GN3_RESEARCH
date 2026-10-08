# Simplex connector program reduces to defect walls and tetrahedral curvature — preserved pre-item development

## Composition

(none yet)

## Development


## Simplex connector program reduces to defect walls and tetrahedral curvature

The completed Freudenthal cube gives an actual simplex triangulation, and the ternary memory lift embeds in its next barycentric refinement as the adjacency graph of overlapping rank-two flags.

For a ternary reversal-odd label, write

h(a,b,c)=alpha(a,b,c) xor 1_{d({a,b,c})=b},

with alpha alternating and d an optional marked vertex on each triangle.

Two independent structures are now available.

### 1. Defect-safe insertion has canonical boundary connectors

For a fixed new vertex x and a defect-free order O, the marked triangles {x,v_i,v_{i+1}} define L/R/X/N symbols. The initial L-run determines the leftmost safe insertion and the terminal R-run determines the rightmost safe insertion. Thus the d-field creates a one-dimensional admissible carrier with canonical access from both ends.

### 2. Orientation curvature is simplicial

Fix increasing-coordinate face bits f on triangles. On every tetrahedron Q,

(delta f)(Q)=1

if and only if Q is singly curved, meaning exactly one pivot link is cyclic.

Hence singly-curved tetrahedra form the support of a genuine simplicial 3-coboundary. In particular their parity on the five tetrahedral facets of every 4-simplex is even.

Fully-curved tetrahedra have delta f=0 and are invisible to this first curvature cochain.

### Proposed Connector mechanism

The correct Sperner/Connector object is therefore not a support-only vertex labeling and not an arbitrary chamber label.

Use the barycentric simplex refinement carrying the memory states. Thicken the defect-safe insertion carriers into state cells. Across these cells, the only orientation obstruction to continuously moving a local repair is the tetrahedral curvature of alpha.

The singly-curved part has mod-2 conservation because it is delta f. Its Poincare-dual support is therefore a relative cycle/connector in the simplex. A connector theorem should be applied to this dual carrier to force one of two outcomes:

1. a repair path crosses the curvature carrier and reaches a defect-safe orientation-compatible state, yielding a one-change order; or
2. the obstruction is trapped entirely in the delta f=0 region, reducing the problem to flat/fully-curved tetrahedra.

The second branch is already algebraically narrower: when delta f=0, alpha has an edge-potential representation by an ordinary tournament, and the pure-orientation target becomes a directed Hamilton path whose distance-two chord directions change at most once.

Thus a plausible rigorous decomposition is

general ternary NOR
-> defect-safe connector carrier
-> coboundary-curvature crossing
-> either closure or delta f=0 tournament branch
-> remaining fully-curved/two-chord obstruction.

### Exact proof obligations

To turn this into a proof one must establish:

- a cell-level carrier whose vertices/edges are actual compatible memory states, so a connector path extracts a geodesic rather than an arbitrary walk;
- a precise duality between crossing the singly-curved coboundary support and changing the orientation-failure side of an extremal safe insertion;
- a terminal theorem for the delta f=0 tournament two-chord branch, or a further parity obstruction showing fully-curved tetrahedra cannot support a minimum counterexample.

This formulation keeps the two-step memory and simplex topology simultaneously. It also explains why ordinary Sperner labels on subset vertices were too weak: they discarded both the defect-safe carrier and the tetrahedral curvature cochain.
