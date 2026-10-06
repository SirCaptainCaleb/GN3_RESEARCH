# Twelve-label SAT remains feasible after both-hole seed selectors and immediate rooted conversions

## Metadata

- ID: twelve_label_sat_remains_feasible_after_both_hole_seed_selectors_and_immediate_rooted_conversions
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 105
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

The twelve-label finite model was strengthened using the minimum-pair cross-boundary seed theorem at both seams. At the P-to-Q seam it now explicitly requires Ham({a,b,q_1,x,y}) or Ham({a,b,x,y}) or Ham({b,q_1,x,y}); at the opposite seam it requires the symmetric disjunction Ham({d,c,p_1,x,y}) or Ham({d,c,x,y}) or Ham({c,p_1,x,y}). In addition, every immediate ambient-compatible two-cover conversion visible in the twelve-label frame was forbidden: a Hamilton order of {a,b,x,y} that can be prepended to Q; a Hamilton order of {b,q_1,x,y} that can be appended after P-b through the exposed pair (u,a); and the two symmetric conversions at the opposite seam. The strengthened MILP remains feasible. No individual one of the three seed types is forced at either seam: for each candidate seed separately there is a feasible model in which that candidate is non-Hamiltonian while one of the alternatives supplies the required seam seed. Thus revision 1704 genuinely changes the structural interpretation by guaranteeing a both-hole seed, but seed existence plus all immediately visible rooted conversions do not close the twelve-label state. The next justified strengthening is seed-preserving maximalization / endpoint saturation, which introduces conditional enlargement branches rather than another unconditional seed clause.
