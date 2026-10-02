# Local non-Hamiltonian interfaces force opposite-extremal matching blocks

**Summary:** Local non-Hamiltonian interfaces force opposite-extremal matching blocks.

## Statement

Let H be a boundary tournament. Let S=(u,s_1,s_2,v) be a tight four-path, and let r_i,r_{i+1},r_j,r_{j+1} be vertices outside S (not necessarily all distinct except as required by the displayed four-sets below). Suppose (r_{i+1},u,r_i) and (r_{j+1},v,r_j) are tight. Assume the five-sets {r_i,u,s_1,s_2,v} and {u,s_1,s_2,v,r_{j+1}} are non-Hamiltonian, and the four-sets A={s_1,u,r_i,r_{i+1}} and B={s_2,v,r_j,r_{j+1}} are non-Hamiltonian. Then A and B are edge-orderable matching-block four-sets. In A, the opposite-edge matching {u r_i, s_1 r_{i+1}} is the highest block; in B, {v r_{j+1}, s_2 r_j} is the lowest block. Consequently (u,s_1,r_{i+1}), (u,r_{i+1},s_1), (r_i,s_1,r_{i+1}), (r_i,r_{i+1},s_1), (s_2,r_j,v), (r_j,s_2,v), (s_2,r_j,r_{j+1}), and (r_j,s_2,r_{j+1}) are tight.

## Body

Because (u,s_1,s_2) and (s_1,s_2,v) are tight, if (r_i,u,s_1) were tight then (r_i,u,s_1,s_2,v) would be a Hamilton tight path on the first displayed five-set, contrary to its assumed non-Hamiltonicity. Hence boundary antisymmetry gives (s_1,u,r_i) tight. Symmetrically, if (s_2,v,r_{j+1}) were tight then (u,s_1,s_2,v,r_{j+1}) would Hamiltonize the second displayed five-set, so (r_{j+1},v,s_2) is tight.

The four-sets A and B are non-Hamiltonian by hypothesis. The small-set matching-block classification therefore represents each by an edge order whose three opposite-edge perfect matchings form strict blocks.

For A define M_0={u r_i,s_1 r_{i+1}}, M_1={u s_1,r_i r_{i+1}}, M_2={u r_{i+1},r_i s_1}. Tightness of (s_1,u,r_i) means u s_1<u r_i, hence M_1<M_0. Tightness of (r_{i+1},u,r_i) means u r_{i+1}<u r_i, hence M_2<M_0. Thus M_0 is the highest block. Comparing every edge in M_1 and M_2 with the appropriate edge in M_0 gives the four asserted A-side tight triples.

For B define N_0={v r_{j+1},s_2 r_j}, N_1={v s_2,r_j r_{j+1}}, N_2={v r_j,s_2 r_{j+1}}. Tightness of (r_{j+1},v,s_2) gives v r_{j+1}<v s_2, hence N_0<N_1. Tightness of (r_{j+1},v,r_j) gives v r_{j+1}<v r_j, hence N_0<N_2. Thus N_0 is the lowest block, and the four asserted B-side triples follow. No minimum-counterexample, path-cover, ambient-order, or extremality hypothesis is used.

## Metadata

- ID: local_opposite_extremal_matching_interfaces01
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
