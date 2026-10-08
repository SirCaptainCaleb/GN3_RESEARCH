# The surviving earlier defect either hits a full barrier or crosses the flip block — preserved pre-item development

## Composition

(none yet)

## Development

## The surviving earlier defect either hits a full barrier or crosses the flip block

Continue with subsection 56 in the branch h_{j-4}=1. After deleting t=v_{j-2}, the local order is

(...,q,r,u,x,a,d,b,c,e,...)

with
q=v_{j-4}, r=v_{j-3}, u=v_{j-1}, a=v_j,

and local statuses

...,0, 1,0,0,0,0,...

where
alpha(q,r,u)=1,
alpha(r,u,x)=0,
alpha(u,x,a)=0,
alpha(x,a,d)=0,
alpha(a,d,b)=0.

### First forward repair is forced

The transition 1->0 on the tetrahedron {q,r,u,x} admits the last-pair repair because

alpha(q,r,x)=alpha(x,q,r)=1

by cyclic invariance and the special blocker scan.

Swap u,x. The order becomes

(...,q,r,x,u,a,d,b,c,e,...).

The endpoint-repair identities give

alpha(q,r,x)=1,
alpha(r,x,u)=1,
alpha(x,u,a)=1.

Put
lambda=alpha(u,a,d).

So the advancing 1-island now ends according to lambda.

### If lambda=1: a full barrier is reached

The next transition is

alpha(u,a,d)=1,
alpha(a,d,b)=0

on {u,a,d,b}.

The last-pair repair would require alpha(u,a,b)=1, but u,a,b are consecutive old zero-phase coordinates, so alpha(u,a,b)=0.

Coboundary flatness on {u,a,b,d}, using
alpha(u,a,b)=0,
alpha(a,b,d)=1
from the holonomy-flip table,
and alpha(u,a,d)=lambda=1,
forces alpha(u,b,d)=0.
Hence alpha(u,d,b)=1 by alternation.

For the 1->0 transition, the first-pair repair would require alpha(u,d,b)=0. It fails.

Thus both endpoint repairs fail: {u,a,d,b} is fully curved. The advancing defect emits the protected physical root e_u-e_b.

### If lambda=0: two more forward repairs are forced

Now the transition is

alpha(x,u,a)=1,
alpha(u,a,d)=0.

Coboundary flatness on {x,u,c,d}, together with the perfect-blocker/holonomy identities, yields

alpha(x,u,d)=1-lambda=1.

Therefore the last-pair repair is available: swap a,d. The local 1-island advances through d.

After that swap the next transition is on the ordered tetrahedron (d,a,b,c), with statuses

alpha(d,a,b)=1,
alpha(a,b,c)=0.

But
alpha(d,a,c)=alpha(a,c,d)=1

by cyclic invariance and the holonomy-flip identity alpha(a,c,d)=1. Hence the last-pair repair is again available: swap b,c.

After these two repairs the local order has passed to

(...,q,r,x,u,d,a,c,b,e,...)

and the consecutive statuses through the entire former holonomy-flip block are all 1 up to the final crossing beyond b,e.

### Dichotomy

Starting from the only unresolved h_{j-4}=1 branch, the defect cannot immediately reflect:

- lambda=1 gives a new fully-curved protected-root barrier strictly to the right of the deletion-created defect;
- lambda=0 forces the transition through the whole six-coordinate holonomy-flip interior by explicit forward endpoint repairs.

The remaining scalar boundary datum is now the first status beyond that crossed block. Thus the special perfect-scan branch has a genuine directed transport mechanism at least through the canonical holonomy interface; recurrence would have to occur farther outside, not inside the same packet.
