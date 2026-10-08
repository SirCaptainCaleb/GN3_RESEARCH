# The common left reconnection of a holonomy toggle is a forced full barrier — preserved pre-item development

## Composition

(none yet)

## Development

## The common left reconnection of a holonomy toggle is a forced full barrier

Continue in the special perfect-blocker branch. Let the holonomy-flip six-set begin at old coordinate a=v_j, and write the two preceding old coordinates

t=v_{j-2}, u=v_{j-1}.

Both phase-toggle chambers of subsection 48 begin with the same ordered pair (x,a), so after the unchanged old prefix the common local order starts

(...,t,u,x,a,...).

Inside the zero phase the old carrier gives
alpha(t,u,a)=0.

The special perfect-blocker scan gives
alpha(x,t,u)=1,
alpha(x,u,a)=1.

By cyclic invariance and alternation,

alpha(t,u,x)=1,
alpha(u,x,a)=0.

Thus the common left reconnection contains the transition

1,0

on the consecutive tetrahedron {t,u,x,a}. The preceding untouched old window is color 0, so the fixed exterior pattern begins 0,1,0.

### The barrier is fully curved

For the ordered transition (t,u,x,a), the last-pair endpoint repair would require
alpha(t,u,a)=alpha(t,u,x)=1,
but alpha(t,u,a)=0, so it fails.

Coboundary flatness on the four-set {x,t,u,a} gives
alpha(x,t,u)+alpha(x,t,a)+alpha(x,u,a)+alpha(t,u,a)=0.
Substituting 1,1,0 for the known terms yields
alpha(x,t,a)=0,
hence by alternation
alpha(t,x,a)=1.

The first-pair endpoint repair of the 1->0 transition would require alpha(t,x,a)=0, so it also fails.

Therefore {t,u,x,a} is fully curved.

### Canonical root certificate

The two consecutive ternary windows

(t,u,x) -> (u,x,a)

form a protected 10 descent. The slide drops t and enters a, so the common left reconnection emits the physical root

rho_j=e_t-e_a=e_{v_{j-2}}-e_{v_j}.

Thus the holonomy phase toggle has an exact Article III handoff:

- its six-coordinate interior is transition-optimal and can be toggled 0000 <-> 1111 with no exterior change;
- its unavoidable left exterior oscillation is a fully-curved barrier carrying a canonical protected root.

There is no missing flat repair at this boundary. Any closure of the special perfect-blocker branch must either use the opposite/right reconnection or combine these canonical barrier roots with a genuinely cut-changing root state.
