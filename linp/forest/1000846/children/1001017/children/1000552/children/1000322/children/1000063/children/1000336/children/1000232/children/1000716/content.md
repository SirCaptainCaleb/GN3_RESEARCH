# Fixed-hole window state for the final loss-one obstruction

## Statement

For a loss-one x-ending state P in the boundary q=delta analysis, retain the fixed omitted vertex b together with the minimal two-edge interval I(P,b) containing all non-x one-contact external chords through b whenever no corrected two-chord bridge exists. Seek a canonical move that either increases the path length, changes the fixed hole, or moves I(P,b) monotonically toward an endpoint. A closed state walk with unchanged hole and window should force repeated use of the same path vertices by distinct b-edges or by the omitted two-contact edge, contradicting linearity.

## Body

The fixed-hole residual dichotomy 467601f9b227 shows that after excluding an immediately usable corrected bridge, only two geometries remain: a completely external b-edge, or concentration of every non-x one-contact b-edge in a two-edge window. Neither geometry is locally contradictory: the external edge can attach to the omitted edge g_{i+1} only by sacrificing one long side of the path, while three distinct one-contact b-edges can fit inside two consecutive path edges. Thus further progress should be encoded as a state transition rather than a one-shot splice. The suggested secondary data are the fixed hole b and the minimal concentration window I. The imported Minty/Tucker philosophy is relevant only at this reduced state level: one needs a deterministic move and a secondary potential, not a topological argument on the original hypergraph. Missing obligation: define the canonical move in both residual branches and prove either strict secondary-potential progress or an impossible closed walk.
