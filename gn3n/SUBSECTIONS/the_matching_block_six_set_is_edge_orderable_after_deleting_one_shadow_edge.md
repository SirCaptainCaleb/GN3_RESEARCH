# The matching-block six-set is edge-orderable after deleting one shadow edge

## Metadata

- ID: the_matching_block_six_set_is_edge_orderable_after_deleting_one_shadow_edge
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 68
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Let U=C union {a,b} be the canonical matching-block exception of the six-set deletion theorem. Thus |C|=4, H[C], H[C+a], and H[C+b] are non-Hamiltonian, and C is partitioned into fixed-pair classes C_+,C_- of order two. For y in C_+ and z in C_-, the hook rectangle gives the comparison arcs ay->yb, bz->za, ay->az, and bz->by. Since the two bad five-sets C+a and C+b are edge-orderable, their comparison digraphs are acyclic. Consider the full comparison digraph Gamma(U) with the single shadow vertex ab deleted. Any directed cycle would have to use at least one mixed arc, since each five-set side is acyclic. Mixed arcs from the a-side to the b-side are exactly ay->yb for y in C_+, while mixed arcs from the b-side to the a-side are exactly bz->za for z in C_-. Choose two consecutive mixed arcs on a hypothetical directed cycle, first ay->yb and later bz->za, with no mixed arc between them. The intervening segment is a directed path inside Gamma(C+b) from by to bz. But the hook bz->by is itself an arc of Gamma(C+b), creating a directed cycle in the edge-orderable five-set C+b, contradiction. The opposite ordering of crossing types is symmetric. Therefore Gamma(U)-{ab} is acyclic. Equivalently, there is one edge order on all fourteen edges of K_U except ab that realizes every boundary comparison not involving ab. Hence the canonical six-set matching-block exception is an exact one-shadow-edge completion defect.
