# Two full switches around a singleton have a monochromatic five-vertex resolution — preserved pre-item development

## Development

## A singleton trapped between two fully-curved switches has a monochromatic five-vertex resolution

Work in the coboundary-flat pure-orientation sector. Let five consecutive coordinates be
(a,b,c,d,e)
with local status pattern
sigma, tau, sigma,
where tau=1-sigma:
alpha(a,b,c)=sigma,
alpha(b,c,d)=tau,
alpha(c,d,e)=sigma.
Assume both transition tetrahedra
Q_L={a,b,c,d}, Q_R={b,c,d,e}
are fully curved. This is exactly the local geometry around a singleton color run whose two bounding switches are both pinned universal switches.

Full curvature of Q_L forces
alpha(a,b,d)=tau,
alpha(a,c,d)=sigma.
Full curvature of Q_R forces
alpha(b,c,e)=sigma,
alpha(b,d,e)=tau.

Because the sector is coboundary-flat, applying delta alpha=0 to the remaining three tetrahedra shows that the three as-yet-undetermined face values coincide:
alpha(a,b,e)=alpha(a,c,e)=alpha(a,d,e)=:t.

Thus the entire oriented five-set is determined by one residual bit t.

### Monochromatic resolution
There are two cases.

If t=tau, then the order
(b,a,c,e,d)
is tau-monochromatic:
alpha(b,a,c)=tau,
alpha(a,c,e)=tau,
alpha(c,e,d)=tau.

If t=sigma, then the order
(b,a,d,e,c)
is sigma-monochromatic:
alpha(b,a,d)=sigma,
alpha(a,d,e)=sigma,
alpha(d,e,c)=sigma.

Therefore every five-set formed by two overlapping fully-curved transition tetrahedra around a singleton run admits an explicit monochromatic Hamilton order on those five coordinates.

### What this does and does not prove
This is a genuine local resolution gadget. It does not by itself lower the variation of the ambient full-support cyclic order, because replacing the five consecutive coordinates also changes the two reconnection packets to the outside coordinates. In particular neither monochromatic resolution preserves the original ordered endpoint pairs.

However it sharply constrains any all-curved closed repair state: the only reason the singleton trap can remain globally irreducible is boundary incompatibility with the two surrounding runs. The interior five-coordinate obstruction itself disappears completely.

A useful next target is a boundary-compatible version: show that one of the two monochromatic resolutions can be chosen so that at least one reconnection side matches its surrounding run, after which the flat endpoint-repair machinery on the other side may finish the surgery.
