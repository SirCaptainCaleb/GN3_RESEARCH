# Eoin Long: exponential-length simple cycles in minimum-degree cube subgraphs

**Summary:** Minimum degree d in a cube subgraph forces a simple cycle with >=2^d edges. For balanced red-blue cubes, each color therefore contains an exponentially long cycle.

## Statement

Eoin Long (Combinatorica 33 (2013), 395–428) proved that any subgraph G of Q_N of minimum degree at least integer d>=2 contains a simple cycle of length at least 2^d; he also obtained a simple path with 2^d-1 edges. The bound is sharp for Q_d.

## Body

Source: Eoin Long, 'Long paths and cycles in subgraphs of the cube,' Combinatorica 33 (2013), 395–428, DOI 10.1007/s00493-013-2736-1, https://link.springer.com/article/10.1007/s00493-013-2736-1. The minimum-degree theorem gives a simple cycle length >=2^d when d>=2, and a path of length >=2^d-1. The n-dimensional hypercube Q_n has 2^n vertices. For a balanced 2-coloring of Q_N, both monochromatic spanning subgraphs are d-regular with d=N/2. Hence each contains a monochromatic simple cycle of length >=2^(N/2), for every even N>=4, with no antipodal assumption and no Eulerian parity requirement. If N divisible by four, both color degrees are even, so after extracting a long simple cycle the remaining monochromatic graph stays Eulerian and can be decomposed further into simple cycles. Caveat: a long simple cycle can repeat cube direction labels and need not contain a comparably long rainbow contiguous arc. The binary-reflected Gray-code Hamiltonian cycle of Q_d has length 2^d, yet any consecutive arc with distinct direction labels has at most three edges (bit 0 appears on every other edge). Thus this theorem alone does not establish a long dimension-simple monochromatic path or NORI1. Distinguish cycle length on 2^N cube vertices from support size among only N direction labels.

## Metadata

- ID: literature_eoin_long_exponential_cycles_min_degree_cube
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
