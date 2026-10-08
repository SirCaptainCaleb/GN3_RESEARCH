# Every minimum signature shore contains a common-A3 protected triangle

## Composition

(none yet)

## Development

## Every minimum signature shore contains a common-A3 protected triangle

Use the switching normalization of §332:
B -> z -> A -> x,
so x is a sink and z dominates A.

By §337 every vertex of A has both an out-neighbor and an in-neighbor in the induced tournament T[A]. Hence T[A] contains a directed cycle. A shortest directed cycle in a tournament has length three, so choose
u -> v -> w -> u
inside A.

Consider the four-set
Q={x,u,v,w}.

Because x is a sink, the following three chamber orders have exact word 10:

1. (u,w,x,v):
alpha(u,w,x)=1,
alpha(w,x,v)=0.
Hence it carries u->v.

2. (v,u,x,w):
alpha(v,u,x)=1,
alpha(u,x,w)=0.
Hence it carries v->w.

3. (w,v,x,u):
alpha(w,v,x)=1,
alpha(v,x,u)=0.
Hence it carries w->u.

For the first packet, for example, the off-faces are
alpha(u,w,v)=0,
alpha(u,x,v)=1,
the fully-curved pattern for the 1->0 transition. The other two are cyclically identical. Thus all three are actual protected roots in the same A3 permutahedral block Q.

Their physical sum is
(e_u-e_v)+(e_v-e_w)+(e_w-e_u)=0.

Therefore every minimum unresolved signature shore contains a positive protected-root 3-cycle confined to one common A3 face.

This invokes the existing common-face A3 extraction theorem directly: the minimum-shore obstruction cannot remain purely inside A. It yields a spanning NOR-good order, a strict admissible deletion improvement, or a protected root exiting the four-set Q.

The remaining branch is consequently an EXTERIOR ejection from this canonical A3 triangle. Its provenance is substantially stronger than an arbitrary protected-root handoff: three of the four active coordinates lie in the minimum shore and the fourth is the connector vertex x.
