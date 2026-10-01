# Pair-deletion parity cocycle

## Statement

For each unordered pair {u,v}, normalize a two-cover of H-{u,v} and encode a binary attachment type describing which of the two deleted vertices is forced toward which side or endpoint when direct reinsertion is blocked. Conjecture that, after choosing a canonical normalization and excluding immediate theorem-closing configurations, these bits satisfy a triangle parity relation s_uv xor s_vw xor s_wu = 0. Hence s_uv = c_u xor c_v for vertex labels c_u in {0,1}, producing a global bipartition of the vertices. Seek to show that the two parity classes inherit coherent endpoint orders and form the two paths of a spanning cover.

## Body

The first task is to define s_uv so that it is invariant under reversal of both cover components and does not depend on arbitrary cover choice. Candidate definitions should be built from a certified forced-separation or order-disagreement event, not from raw displayed endpoint names. Then study three labels u,v,w and compare the three pair-deletion covers on their common H-{u,v,w} core. If odd triangle parity occurs, attempt to splice the three inconsistent attachment requirements into a short Hamiltonian replacement or a direct two-cover. If every triangle has even parity, elementary F_2 cohomology on the complete graph gives vertex labels c_u with s_uv=c_u xor c_v. The remaining theorem is then an order-synchronization problem inside and across the two classes.
