# Source-sink deletion components are fixed-rank Johnson incidence components

## Metadata

- ID: source_sink_deletion_components_are_fixed_rank_johnson_incidence_components
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 259
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Let R be any source-sink deletion-cover edge graph in the sign cube of a minimum counterexample, in particular any top-dimensional core remaining after unique-face collapses. Write a sign vertex by its plus set A. Every naturally oriented cube edge goes A -> A-{x}. Since every nonisolated vertex of R is a pure source or pure sink, a connected component C is bipartite with all edges directed from sources to sinks. If one source has plus-size m, every adjacent sink has plus-size m-1; every other source adjacent to that sink again has plus-size m. Connectivity therefore implies that all sources of C have one common size m and all sinks have size m-1. A source A represents a non-Hamiltonian m-set whose complement is Hamiltonian; an incident edge A -> A-{x} means the core A-{x} is Hamiltonian. If two sources A,A' share a sink, then A and A' differ by exactly one exchange and have the common Hamiltonian core A intersect A'. Thus the source projection of C is a connected subgraph of the Johnson graph on m-sets, with edges certified by Hamiltonian (m-1)-cores. Antipodal sign reversal sends C to a component whose source size is n-m+1. Consequently a connected component can be self-antipodal only if m=n-m+1, equivalently n is odd and m=(n+1)/2. Hence every self-antipodal top-core component is automatically balanced and lives at exactly the old odd-support scale; all unbalanced components occur in distinct antipodal pairs. This identifies the generalized residue behind the earlier negative odd support cycle: not necessarily a cycle, but a balanced self-antipodal Johnson-incidence component of non-Hamiltonian one-vertex extensions of Hamiltonian cores.
