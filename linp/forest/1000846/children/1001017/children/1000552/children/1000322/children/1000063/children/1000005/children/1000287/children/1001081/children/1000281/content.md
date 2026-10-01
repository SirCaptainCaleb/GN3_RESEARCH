# Extremal-deletion transfer for punctured-Steiner regular systems

## Statement

Let d>=2 and let H be a d-regular linear 3-uniform hypergraph on 2d+2 vertices. Fix a vertex z. Then H-z has 2d+1 vertices, exactly d(2d-1)/3 edges, one vertex of degree d and all other 2d vertices of degree d-1. Consequently, if every P_d-free linear triple system on 2d+1 vertices has at most d(2d-1)/3 edges and every equality example has degree sequence different from (d,(d-1)^{2d}), then H-z contains a spanning P_d. If the equality-profile condition holds for every d in some family, then every one-vertex deletion of every corresponding punctured Steiner system contains a spanning P_d.

## Body

As in efe44a01f2dc, H has a perfect-matching leave. Let z* be the unique uncovered mate of z.

Since H is d-regular on 2d+2 vertices,
|E(H)|=d(2d+2)/3.
Deleting z removes exactly d edges, so
|E(H-z)|=d(2d+2)/3-d=d(2d-1)/3.

The vertex z* is not contained with z in any edge, so none of its d incident edges is deleted; hence
d_{H-z}(z*)=d.
Every other vertex w≠z,z* is paired with z in exactly one edge, and that edge is deleted. Thus
d_{H-z}(w)=d-1.
Therefore the degree sequence of H-z is
(d,(d-1)^{2d}).

Now assume the stated extremal hypothesis for P_d on 2d+1 vertices. If H-z were P_d-free, its edge count d(2d-1)/3 would attain the assumed extremal upper bound. Hence H-z would be an equality example. But by hypothesis no equality example has degree sequence (d,(d-1)^{2d}), contradiction.

Thus H-z contains a P_d. A d-edge linear 3-uniform path uses 2d+1 vertices, exactly all vertices of H-z, so it is spanning.

This abstracts the d=5 argument used for the 12-vertex Class-III case: there the exact P_5 theorem on 11 vertices gives extremal size 15, while the unique equality graph G_0 has degree sequence (5^6,3^5), incompatible with (5,4^{10}).