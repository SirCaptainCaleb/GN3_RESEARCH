# One-sided common-anchor source contacts force quadratic rank spread

## Statement

Let R=(g_1,...,g_L) avoid v. Let F be m distinct ascending nonspecial edges e={x,v,u}, with x,u on R, rank r_e<=q, and a clean maximum source path S_e of length r_e-1 ending at x. Orient R once, and set a_e to the first index containing x. Partition F according to whether u is after or before x. Assume the following weak one-sided source-contact property:
if u is after x, V(S_e) intersect V(R) is contained in V(g_1 union ... union g_{min(L,a_e+1)});
if u is before x, that intersection is contained in V(g_{a_e} union ... union g_L).
Then, with Delta=sum_{e in F}(q-r_e),
Delta >= m^2/24-m/2.
Also, for every integer D>=0, at most 12(D+1) members have r_e>=q-D.
The entrance-side equal-exchange and order-inversion branches on a common anchor satisfy this weak property.

## Body

The basic extension is independent of intersections between different source paths. If S_e avoids both non-v vertices of a distinct edge f through v, then S_e,e,f is a linear path of length r_e+1 ending in f. Consequently r_f>=r_e+1.

In each orientation partition the edges by parity of a_e and into three slots at a fixed a_e; this gives at most six classes per orientation and twelve in total. Linearity at v makes the entrances distinct; a host edge has at most three possible entrances. In any class consecutive first indices differ by at least two.

For forward edges with a_f>=a_e+2, both non-v vertices of f lie beyond the initial host-edge block permitted for S_e. Indeed the entrance of f first occurs at a_f, and its other endpoint is farther forward; the two endpoints cannot share a host edge by linearity. Thus S_e avoids f, so r_f>=r_e+1.
For backward edges in the same first-index order, the source of the later edge avoids both non-v vertices of the earlier edge; its allowed host block starts at the later first index, whereas both earlier endpoints occur strictly before that block. Thus ranks strictly decrease. The parity separation covers junctions and private vertices in host edges.

A class of size k therefore has distinct integer ranks at most q, and contributes at least 0+1+...+(k-1)=k(k-1)/2 to Delta. If the twelve class sizes are k_l, pad by zeros and use sum k_l^2>=m^2/12. This gives Delta>=m^2/24-m/2. A band of D+1 integer ranks contains at most D+1 members per class, proving the band bound.

The hypotheses deliberately use a weak host-edge-block condition to cover same-edge boundary ambiguity. When all source/anchor contacts other than x are on the side opposite u, contacts lie in those blocks. Mutual source-path disjointness and payment transfer are not hypotheses.