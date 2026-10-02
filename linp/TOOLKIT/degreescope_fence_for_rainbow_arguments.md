# Degree-scope fence for rainbow arguments

## Statement

Keep the original-hypergraph minimum degree and the properly edge-colored shadow-graph minimum degree as separate, simultaneously useful hypotheses. A rainbow-path theorem stated for minimum degree applies to the derived graph degree delta(J), not to the hypergraph degree delta(H). Do not discard delta(H): it remains available for hypergraph-side dense-core, peeling, attachment, and special-edge arguments.

## Body

The original 3-uniform degree d_H(v) counts hyperedges through v. After a density-core reduction one may assume delta(H)>=|E(H)|/|V(H)| (or use a stronger problem-specific core threshold such as the live dense-core all-special conjecture). The shadow degree d_J(v) counts retained colored pairs incident with v in a derived properly edge-colored graph. If a rainbow theorem assumes minimum graph degree delta, it must be invoked on J or on a graph subgraph J0 obtained by graph-side peeling/density maximization. There is no license to insert delta(H) into that theorem. Conversely, passing to J0 does not replace the useful lower bound on delta(H): the two degree conditions support different parts of the proof and may be used together. In the A/B shadow route, the proved two-stage reduction supplies both a hypergraph core H0 and a shadow core J0. In rank-layer graphs J_k, any minimum-degree cleanup is again a cleanup inside J_k; the hypergraph minimum-degree information remains separate background structure.

## Metadata

- ID: degreescope_fence_for_rainbow_arguments
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
