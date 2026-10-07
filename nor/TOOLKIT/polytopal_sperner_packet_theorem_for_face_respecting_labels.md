# Polytopal Sperner packet theorem for face-respecting labels

**Summary:** A face-respecting vertex labeling of any triangulated polytope forces one simplex whose geometric simplex meets the convex hull of its labels. This is the Brouwer/Sperner form suited to cut-valued labels rather than coordinate-valued labels.

## Statement

Let Q be a convex polytope with a triangulation K. If every vertex x of K is labeled by a vertex lambda(x) of the minimal face of Q containing x, then some simplex sigma of K contains a point y lying in both sigma and conv{lambda(x): x in Vert(sigma)}.

## Body

## Statement

Let Q be a convex polytope and K any triangulation of Q. For each triangulation vertex x choose a polytope vertex lambda(x) belonging to the minimal face F(x) of Q that contains x.

Then there is a simplex sigma of K and a point y such that

y in sigma intersect conv{lambda(x): x in Vert(sigma)}.

Equivalently, the piecewise-affine label map f:Q->Q obtained by sending each triangulation vertex x to lambda(x) has a fixed point.

## Proof

Because lambda(x) lies in F(x), every face F of Q is mapped into itself on the vertices of the induced triangulation K|F. By affine extension, f(F) is contained in F for every face F. In particular f maps Q continuously to itself.

Brouwer's fixed-point theorem gives y in Q with f(y)=y. Let sigma be a simplex of K containing y. Since f is affine on sigma,

y=f(y) belongs to conv{lambda(x):x in Vert(sigma)}.

Also y belongs to sigma, proving the claim.

## Relation to ordinary Sperner

For Q a simplex and K its barycentric subdivision, choosing lambda(x) among the vertices of the minimal containing face is exactly a Sperner labeling. A fully labeled simplex is one way the intersection conclusion is realized.

The polytope formulation is more appropriate when labels are themselves combinatorial states such as p-cuts, matchings, or bases.

## NOR relevance

For fixed p, the centered hypersimplex Delta(n,p) has vertices z_C=1_C-(p/n)1 indexed by p-cuts C. A protected Article III root crossing C determines an adjacent cut C'. Hence a face-respecting labeling by protected cuts can be fed directly into this theorem. The output is a simplex carrying a convexly compatible packet of cut labels, which is the natural discrete analogue of the convex root packets used by the repaired hairy-ball carrier.

This theorem alone does not construct the required NOR labeling. The substantive obligation is to assign each triangulation vertex a protected cut belonging to its minimal hypersimplex face while retaining root and side provenance.

## Metadata

- ID: polytopal_sperner_packet_theorem_for_face_respecting_labels
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
