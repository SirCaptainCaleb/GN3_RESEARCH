# Mutually caged cycles are consistent but require center-dependent cross tournaments

## Metadata

- ID: mutually_caged_cycles_are_consistent_but_require_center_dependent_cross_tournaments
- Parent Section: directed_nor_union_closed_bridge
- Position: 53
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Adversarial false-model analysis in ternary arity. Let C=(c_i) and D=(d_j) be disjoint intended color-0 tight cycles. The canonical two-cycle join theorem can be blocked at every pair of junctions by the locally consistent prescriptions, at each center c_i: c_{i-1}->c_{i+1}->d_j->c_{i-1} for every d_j, and symmetrically at each center d_j: d_{j-1}->d_{j+1}->c_i->d_{j-1} for every c_i. Because ternary reversal-odd data are exactly independent tournaments at each center, these constraints occupy no conflicting reversal orbits and extend to a full coloring. Thus two mutually caged monochromatic cycles are a legitimate symbolic obstruction architecture, not merely a contradictory wish-list. However, center-independent completion of the cross tournaments cannot give a counterexample. If every T_{d}|C is the same tournament R_C and every T_{c}|D is the same tournament R_D, choose directed Hamilton paths c_1,...,c_m in R_C and d_1,...,d_k in R_D and interleave them. Every consecutive triple centered in D compares consecutive C vertices along R_C, and every triple centered in C compares consecutive D vertices along R_D, so the interleaved order is monochromatic (with the evident one-extra-vertex endpoint handling). Therefore any genuine false model based on mutually caged cycles must have essentially center-dependent cross tournaments. The adversarial construction problem reduces to building two indexed tournament families {T_d|C} and {T_c|D} with no interleaving whose successive cross comparisons are one-change, while retaining the cycle-caging constraints.

## Frontier

- Development version when composed: None
- Development version now: 1
