# Audit: minimum-short-phase symmetry does not give one Johnson cut layer — preserved pre-item development

## Composition

(none yet)

## Development

Let a ternary deletion order O=(v_1,...,v_m) have one-change word 0^p1^q, and let L={v_1,...,v_p} be the canonical physical cut used by the protected-root theorem. The canonical insertion root crosses L.

The family of deletion witnesses minimizing min(p,q) is indeed closed under reversal/color normalization as a family of WORD PROFILES: reversal exchanges (p,q) with (q,p). However this does not put both orientations over one fixed Johnson layer.

If p is the short phase, L is a p-set. After reversal, the canonical first-phase cut has size q and consists of the last q coordinates of the original deletion order. In ternary arity these two cuts are not complements: p+q=n-3 while the deletion order has n-1 coordinates, leaving two overlap/boundary coordinates outside the two phase cuts, plus the omitted coordinate in the full universe.

More importantly, if q is the short phase in the original orientation, the original canonical root need only enter somewhere to the right of the first p-cut. Its entering endpoint is not forced to lie in the last q coordinate positions. Thus multiplying the root by a side sign does NOT automatically turn it into an outward edge of a physical q-shore.

Therefore the previous claim that minimum-short-phase normalization yields an antipodal double cover over a single Johnson layer J(n,ell) is false.

What remains valid is a weaker separation:

1. For linear root separation and Johnson-edge arguments, orient each extremal witness so that the globally minimum phase ell occurs first. Then all canonical roots cross a genuine common-size ell-cut, so the state family lies over J(n,ell). This oriented slice is not antipodally closed, but separation/Farkas arguments do not require antipodality.

2. For antipodal topology, retain both orientations and their actual canonical first-phase cuts. The involution swaps the two cut-size layers ell and n-3-ell. A faithful equivariant carrier must remember this two-layer provenance (or find a different invariant encoding); it cannot identify both layers by a naive phase-side sign.

Thus the correct architecture is: fixed Johnson layer for non-equivariant separation/minimization, two-layer cut provenance for genuinely antipodal fixed-point constructions.
