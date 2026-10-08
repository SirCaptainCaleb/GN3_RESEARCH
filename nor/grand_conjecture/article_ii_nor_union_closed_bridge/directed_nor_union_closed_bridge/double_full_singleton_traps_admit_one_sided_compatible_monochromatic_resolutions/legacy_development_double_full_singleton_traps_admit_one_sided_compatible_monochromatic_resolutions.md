# Double-full singleton traps admit one-sided compatible monochromatic resolutions — preserved pre-item development

## The double-full singleton gadget always has a one-sided tau-compatible resolution

Continue the five-vertex setup of the previous subsection. Let
...,u,a,b,c,d,e,v,...
occur in the cyclic order, with local status pattern
alpha(u,a,b)=sigma,
alpha(a,b,c)=sigma,
alpha(b,c,d)=tau,
alpha(c,d,e)=sigma,
alpha(d,e,v)=sigma,
where tau=1-sigma, and suppose the two tetrahedra {a,b,c,d} and {b,c,d,e} are fully curved. As before, coboundary flatness leaves one residual bit
t=alpha(a,b,e)=alpha(a,c,e)=alpha(a,d,e).

The fully-curved identities also give
alpha(u,b,a)=tau
by reversing the known status alpha(u,a,b)=sigma, and
alpha(e,d,v)=tau
by reversing alpha(d,e,v)=sigma.

### Case t=tau
The five-vertex order
(b,a,c,e,d)
is tau-monochromatic internally. Moreover its first boundary window and last boundary window are also tau:
alpha(u,b,a)=tau,
alpha(e,d,v)=tau.
Hence
(u,b,a,c,e,d,v)
has five consecutive tau-statuses. The singleton trap has been replaced by one coherent tau block across both immediate reconnection sides. Only the next outer windows, involving the coordinates before u and after v, can create new variation.

### Case t=sigma
There are two useful tau-monochromatic resolutions.

The order
(b,a,e,d,c)
has internal word tau,tau,tau and starts with the reversed pair (b,a). Therefore
(u,b,a,e,d,c)
begins with four consecutive tau-statuses: it is left-compatible with the surrounding order.

The order
(c,b,a,e,d)
also has internal word tau,tau,tau and ends with the reversed pair (e,d). Therefore
(c,b,a,e,d,v)
ends with four consecutive tau-statuses: it is right-compatible.

Thus when t=sigma one may choose a tau-resolution compatible with either desired side.

### Consequence
A singleton run trapped between two overlapping fully-curved switches is never a genuinely two-sided local obstruction. Its five-set admits:
- a tau-resolution compatible with both immediate sides when t=tau;
- two tau-resolutions, one compatible with each side, when t=sigma.

The unresolved difficulty is pushed exactly one window farther outward. This suggests a finite propagation scheme: repeatedly choose the resolution compatible with the currently protected side. Either the opposite reconnection becomes compatible and the singleton trap disappears, or incompatibility propagates outward through the adjacent run. A closed repair component would therefore have to support an indefinitely propagating one-sided incompatibility around the cycle.

This is the natural next place to seek a parity/holonomy contradiction or to reconnect with the signed-middle switch-prism carrier.
