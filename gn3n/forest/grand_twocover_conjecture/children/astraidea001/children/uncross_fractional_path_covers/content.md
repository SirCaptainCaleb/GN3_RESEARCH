# Uncross fractional path covers

## Statement

Conjecture that every minimum-total-weight fractional cover by tight-path supports in a finite boundary tournament admits an uncrossing sequence to an optimal fractional cover whose positive supports form a laminar family under inclusion after deleting duplicate vertices of overlap; further, every such laminar optimum of total weight at most two is integral. The maneuver is to replace two crossing path supports by at most two new tight-path supports on their union/intersection while preserving vertex-cover inequalities and not increasing total weight.

## Body

Why it might matter globally:
Astra-001 already identifies tau*(H)<=2 as the weighted half-path statement. A general uncrossing-plus-laminar-rounding theorem would convert that fractional route into an actual spanning two-path cover, attacking the integrality gap rather than endpoint surgery.

Plausible first attack:
Take two positive-weight paths P,Q in an extreme fractional optimum with both V(P)-V(Q) and V(Q)-V(P) nonempty. Analyze the maximal common consecutive subpaths and the first/last disagreement points. Try to prove a two-support exchange lemma that either merges P,Q on their union or replaces them by P',Q' with strictly simpler overlap pattern while preserving the coordinatewise incidence-vector inequality needed for cover feasibility.