# A minimum signature shore has internal witness partners and size at least two

## Composition

(none yet)

## Development

## A minimum signature shore has no singleton case and carries internal witness partners

Continue from §334. Let x,z be a shortcut-free pair with a minimum nonempty signature shore
A={u:alpha(x,z,u)=0},
and B the opposite shore.

Fix u in A. Section 334 shows that x,u has a protected shortcut. Equivalently its pair signature
f_u(y)=alpha(x,u,y)
is nonconstant.

But §334 also gives
f_u(z)=1
and
f_u(y)=1 for every y in B.

Therefore every zero of f_u lies inside A\{u}. Since f_u is nonconstant, at least one such zero exists. Choose
p(u) in A\{u}
with
alpha(x,u,p(u))=0.

Likewise z,u is protected, and its pair signature
g_u(y)=alpha(z,u,y)
is forced to be zero on x and on all of B. Hence it must take value one somewhere in A\{u}; choose
q(u) in A\{u}
with
alpha(z,u,q(u))=1.

Consequently |A|>=2.

More structurally, the minimum shore carries two fixed-point-free directed choice maps
u -> p(u),  u -> q(u)
on A, certifying the internal variation required by the protected pairs x-u and z-u.

Each choice digraph contains a directed cycle entirely inside A. The next target is to convert one such internal cycle of pair-signature flips into either a smaller shortcut-free signature shore or a common-cell protected dependence.

Thus the singleton-shore branch listed in §334 is impossible in a minimum counterexample.
