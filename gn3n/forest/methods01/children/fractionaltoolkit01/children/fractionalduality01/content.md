# Fractional path-cover duality and weighted capture

## Statement

For every finite boundary tournament H, let tau*(H) be its fractional path-cover number. For every nonzero nonnegative vertex weighting w, write W=w(V(H)) and M(w)=max_P w(V(P)), where P ranges over tight paths. Then
tau*(H)=max_{w>=0, w not identically 0} W/M(w).
Equivalently, for T>0, tau*(H)<=T if and only if every nonnegative vertex weighting w admits a tight path P with w(V(P))>=W/T.

## Body

Let F be the finite family of tight-path supports. The fractional path-cover linear program is
minimize sum_{P in F} y_P
subject to sum_{P containing v} y_P >= 1 for every vertex v and y_P>=0.
Its dual is
maximize sum_v w_v
subject to sum_{v in P} w_v <= 1 for every P in F and w_v>=0.
Finite-dimensional LP duality gives equality of the two optima.

For a nonzero nonnegative weighting w, scaling by 1/M(w) makes it dual feasible, with objective W/M(w), so W/M(w)<=tau*(H). Conversely, if w is any nonzero dual-feasible weighting then M(w)<=1; rescaling w by 1/M(w) preserves feasibility after normalization of the largest path constraint and weakly increases the objective to W/M(w). Since the feasible polytope is finite-dimensional and the optimum is attained, the maximum formula follows. The threshold-T formulation is an immediate rearrangement.

This is the line-independent LP core of weightedfractionalduality01. The Astra-001 equivalence and sharp-half-order consequences are applications and remain in that route.
