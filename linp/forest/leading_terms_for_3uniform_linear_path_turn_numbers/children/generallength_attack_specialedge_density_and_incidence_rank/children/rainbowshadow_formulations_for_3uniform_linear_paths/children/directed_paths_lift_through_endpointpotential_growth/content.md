# Ascending-edge directed paths lift through endpoint-potential growth

## Statement

Let H be a finite linear 3-graph with endpoint potential phi. For every ascending nonspecial edge e={x,u,v} with unique entrance x, orient two auxiliary arcs x->u and x->v. Then every auxiliary directed path x_0->x_1->...->x_p forces phi(x_p)>=phi(x_0)+p, and hence H contains a linear hypergraph path of length at least p. Thus the longest directed path in the ascending-edge orientation is a lower bound for the longest linear path in H.

## Body

For an ascending nonspecial edge e={x,u,v} of rank q=phi(e), its entrance satisfies
phi(x)=q-1.
Each terminal t in {u,v} is a last vertex of some q-edge path ending in e, so
phi(t)>=q=phi(x)+1.
Hence every auxiliary arc x->t strictly raises endpoint potential by at least one:
phi(t)>=phi(x)+1.

Along a directed path
x_0->x_1->...->x_p
we therefore obtain iteratively
phi(x_i)>=phi(x_0)+i,
so in particular
phi(x_p)>=phi(x_0)+p>=p.

By definition of endpoint potential phi(x_p), there exists a linear hypergraph path in H of length phi(x_p) ending at x_p. Therefore H contains a linear path of length at least p.

Importantly, this conclusion does not require the parent hyperedges of the directed arcs themselves to form a linear path. Nonconsecutive parent hyperedges could in principle have extra intersections; the potential monotonicity bypasses that lifting issue completely.