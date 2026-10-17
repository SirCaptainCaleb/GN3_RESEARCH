# Tensor amplification of shortest monochromatic antipodal path excess

- Stable ID: note_98b1e0fc35badd4e7eb3124d
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, tensorization, shortest-path, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11486_1
- Updated session: session_nori_r11486_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

For any legal c on Q_n, let L(c) be the shortest red path length between antipodes, finite by Wu--Yang (2026), and e(c)=(L(c)-n)/2. For block product colorings c plus d, L(c plus d)=L(c)+L(d), hence e is additive. Proof: a red antipodal product path projects to red antipodal walks in both factors, giving the lower bound; concatenating minimizing red paths gives equality. Every blue antipodal path translates to a red antipodal path, so the red minimum is the monochromatic minimum. If a universal bound L(c)<=n+o(n) held, a counterexample with e(c)>0 would tensor to dimensions kn with excess ke(c), contradicting sublinearity. Therefore any universal sublinear additive detour theorem proves unrestricted NORI1. More strongly, E(n)=max_c e(c) is superadditive for n>=2; if E(n0)>0, then E(n)>=floor((n-2)/n0)E(n0), giving liminf E(n)/n>=E(n0)/n0. Thus either NORI1 holds or some positive proportional detour is forced in every sufficiently large dimension. This is an all-dimensional quantitative gap-amplification theorem; the near-geodesic bound remains unproved.
