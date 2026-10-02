# Location-sensitive lift of the Minty walk

## Statement

If the scalar potential φ on the vertex-level nonspecial-edge digraph is too coarse to control the transient part, lift the walk state to remember a path together with the location of the first blocking contact. A clean extension is the positive step; a two-contact Pósa rotation or truncation at the first blocker is the backward step. Seek a step score for which every closed state-walk has nonpositive total score.

## Body

The scalar Minty inequality records only the multiplicative change in φ and therefore cannot distinguish a backward step caused by an early blocker from one caused by a late blocker. The existing first-contact, tail-blocker, and two-contact rotation lemmas show that blocker position is additional structured information. A minimal lift is therefore to use states consisting of a linear path with a distinguished last vertex and, when a proposed nonspecial edge cannot be appended cleanly, the first edge of the path meeting it. Clean appending moves receive positive score. A two-contact blocker permits a length-preserving Pósa rotation; more complicated contact patterns permit truncation with a loss measured by the blocker position. The target is a Minty-style no-positive-closed-walk theorem in this lifted finite state graph. Such a theorem would manufacture a potential sensitive to blocker location while projecting back to the ordinary vertex-level digraph. This route is intended as a refinement, not a replacement, of the direct vertex-level potential.