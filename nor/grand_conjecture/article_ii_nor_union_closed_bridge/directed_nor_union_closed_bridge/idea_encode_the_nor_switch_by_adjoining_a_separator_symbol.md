# Idea: encode the NOR switch by adjoining a separator symbol

## Composition

(none yet)

## Development

## Separator-symbol triangulation for one-change NOR

Idea / research direction, not yet a theorem.

Instead of treating a proposed switch position as an auxiliary scalar attached to a completed coordinate order, adjoin one distinguished separator symbol * to the coordinate set. A permutation of V union {*} is exactly:
1. a permutation pi of V; and
2. a cut position in pi, namely the location of *.

Thus the full switch-state space is naturally realized inside the ordinary type-A Coxeter/Freudenthal complex on n+1 symbols, rather than as an externally attached product coordinate. The separator is geometric data.

For a ternary order, windows strictly before * are prescribed one color and windows strictly after * the opposite color; windows crossing * are transition cells and should retain enough ordered-tail memory to decide whether the unique switch is legal. More generally for arity r, one should barycentrically refine the separator complex so that a crossing cell retains the last r-1 physical coordinates on the left and first r-1 on the right.

Reversal sends the word on V union {*} to its reverse while fixing the identity of * and moving it to the complementary cut. Therefore the separator model packages the switch-complement symmetry automatically into the Coxeter antipodal action.

This may be preferable to the naive permutohedron-times-interval construction because:
- every maximal simplex is an honest total order on one enlarged alphabet;
- adjacent chambers are ordinary Coxeter moves, including moves of * past one physical coordinate;
- face restrictions remain deletion-compatible;
- ordered memory around the switch can be retained by a flag/barycentric refinement.

Potential topological targets include Tucker/Ky Fan, Borsuk-Ulam, Hex/Connector, or a simplicial fixed-point theorem on this enlarged Coxeter sphere.

A good labeling should not use only the endpoints of a violating r-window: on an A_2 braid hexagon the three roots e_a-e_c, e_c-e_b, e_b-e_a already sum to zero tautologically. Therefore a successful label must additionally remember switch-side / phase information or the full ordered crossing state.

The intended proof architecture is:
counterexample -> every separator chamber has a violation -> antipodal signed labeling on the refined separator complex -> forced complementary/local critical simplex -> translate that critical Coxeter residue into one of the already-classified insertion/circuit/curvature repairs.

The unresolved step is the exact label and Tucker/Connector boundary condition.
