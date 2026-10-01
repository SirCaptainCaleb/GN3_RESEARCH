# Inductive path-hull reduction for lower-rank nonspecial edges

## Statement

Assume the dense-core all-special conjecture is true for every forbidden length r with 4<=r<ell. Let H be a P_ell^(3)-free linear 3-graph of minimum degree delta, and let e be a nonspecial edge of rank q<=ell-2. For every q-edge path P ending in e, put U=V(P) and G=H[U]. Then:

(1) |U|=2q+1, so G is automatically P_{q+1}^(3)-free.

(2) e has rank exactly q in G and is nonspecial in G with the same unique entrance as in H.

(3) Consequently
    delta(G) <= floor(2(q+1)/3).

Hence every such witness path P contains a vertex v with at least
    d_H(v)-floor(2(q+1)/3)
and in particular at least
    delta-floor(2(q+1)/3)
incident edges not wholly contained in V(P).

Every such external incident edge meets V(P) in either exactly v or exactly two vertices including v; equivalently, relative to the spanning path hull it is a clean ear or a one-contact chord. Thus, under induction on ell, every lower-rank nonspecial edge q<=ell-2 forces an ear-rich vertex on each maximum q-edge witness path.

## Body

A q-edge linear 3-uniform path has exactly 2q+1 vertices, so |U|=2q+1. A (q+1)-edge linear path would require 2q+3 vertices; therefore G cannot contain P_{q+1}.

The path P remains present in G, so phi_G(e)>=q. Since G is an induced subhypergraph of H, any path in G is also a path in H, and phi_H(e)=q; hence phi_G(e)=q.

Every q-edge path in G ending in e is also a q-edge longest path in H ending in e. Because e is nonspecial in H, all such paths enter e through the same unique entrance x. Thus e remains nonspecial in G with entrance x.

Now q+1<ell, so the inductive hypothesis applies to G at forbidden length q+1. If delta(G)>2(q+1)/3, then every edge of G would be special, contradicting that e is nonspecial. Hence
delta(G)<=floor(2(q+1)/3).

Choose v in U with d_G(v)=delta(G). Since d_H(v)>=delta, at least
d_H(v)-d_G(v)>=delta-floor(2(q+1)/3)
edges through v are not wholly contained in U.

Finally, because H is linear and v lies in U, an edge f through v not contained in U cannot contain two further vertices of U if those two together with v form an edge already represented inside the path hull; more generally it can meet U only in v or in v plus one additional vertex unless f itself is wholly contained in U. Thus each external f is either a clean ear (one U-contact) or a one-contact chord (two U-contacts total).
