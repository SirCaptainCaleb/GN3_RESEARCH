# An anchor compatibility neighborhood embeds in its two path orders

## Statement

Let F_d=P|Q be a chosen deletion cover of H-d in a boundary tournament with pc(H)>2, and let y,z be two distinct neighbors of d in the deletion-cover compatibility graph. If F_y and F_z are compatible, then y and z lie in the same one of P,Q and are consecutive in its displayed order. Consequently G[N(d)] is a subgraph of the disjoint union of the two ordinary path graphs obtained from the orders of the neighbor labels along P and Q; in particular G[N(d)] is a linear forest.

## Body

# Proof

Assume dy,dz,yz are compatibility edges. Then F_d,F_y,F_z form a compatibility triangle.

Apply the compatibility-triangle localization to the labels d,y,z. It supplies two common support classes X and R with d,y,z all belonging to X, and F_d has support partition (X-{d}) | R. Therefore y and z lie in the same component of F_d. Thus they lie together in P or together in Q; without loss, in P.

The same compatibility-triangle localization gives a common linear base order obtained after deleting d,y,z, and says that d,y,z all occupy one common insertion gap of that base order. Since F_d omits d, its displayed path P contains y and z. If some vertex w of P occurred strictly between y and z in the displayed order, then w remains after y and z are deleted, so y and z would determine two distinct insertion gaps in the residual order rather than one common gap. Hence no such w exists: y and z are consecutive in P.

Therefore every edge yz of G[N(d)] joins consecutive neighbor labels on one of the two displayed anchor paths P,Q. Restrict each displayed path order to the labels belonging to N(d). The possible neighborhood edges are a subset of the ordinary consecutive-label edges inherited from these two orders. Hence G[N(d)] is a subgraph of a disjoint union of two path graphs, and therefore a linear forest.