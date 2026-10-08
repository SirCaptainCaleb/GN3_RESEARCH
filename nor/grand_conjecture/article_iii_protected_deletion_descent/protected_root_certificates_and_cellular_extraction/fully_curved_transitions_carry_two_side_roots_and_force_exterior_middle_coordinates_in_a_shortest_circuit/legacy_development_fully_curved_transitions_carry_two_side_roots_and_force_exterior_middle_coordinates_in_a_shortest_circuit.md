# Fully-curved transitions carry two side roots and force exterior middle coordinates in a shortest circuit — preserved pre-item development

## A fully-curved transition has two fully-curved side roots

Let a full coordinate order contain four consecutive coordinates
[
(a,b,c,d)
]
with a fully-curved ternary transition normalized as
[
alpha(a,b,c)=1,qquad alpha(b,c,d)=0.
]
Its physical slide root is
[
a	o d,qquad ho=e_a-e_d.
]

For a fully-curved (1	o0) tetrahedron the two off-faces are
[
alpha(a,b,d)=0,qquad alpha(a,c,d)=1.
]

Now use the same four coordinates in the two endpoint-swapped orders.

### Swap the last pair

In
[
(a,b,d,c)
]
the consecutive statuses are
[
alpha(a,b,d)=0,qquad
alpha(b,d,c)=1-alpha(b,c,d)=1.
]
Thus this order carries the actual transition root
[
a	o c.
]
Its off-faces are
[
alpha(a,b,c)=1,qquad
alpha(a,d,c)=1-alpha(a,c,d)=0,
]
so this (0	o1) transition is itself fully curved.

### Swap the first pair

In
[
(b,a,c,d)
]
the consecutive statuses are
[
alpha(b,a,c)=1-alpha(a,b,c)=0,qquad
alpha(a,c,d)=1.
]
Thus this order carries the actual transition root
[
b	o d.
]
Its off-faces are
[
alpha(b,a,d)=1-alpha(a,b,d)=1,qquad
alpha(b,c,d)=0,
]
so this (0	o1) transition is again fully curved.

Therefore every fully-curved transition edge
[
a	o d
]
comes with a local fully-curved side-root triangle fragment
[
a	o c,qquad b	o d.
]

## Consequence for a shortest positive physical-root cycle

Let
[
C:x_0	o x_1	ocdots	o x_{k-1}	o x_0
]
be a shortest directed cycle in any realized-root class that is closed under these two fully-curved side-root realizations. Suppose one cycle edge is the fully-curved transition root
[
a	o d
]
witnessed by ((a,b,c,d)).

Then neither middle coordinate can lie on the cycle support:
[
b,c
otin V(C).
]

Indeed, if (cin V(C)), then the realized root (a	o c) is a directed chord. Together with the old directed segment from (c) back to (a), it gives a strictly shorter positive root cycle. Likewise, if (bin V(C)), the realized root (b	o d) together with the old segment from (d) back to (b) gives a strictly shorter positive root cycle.

In particular, a shortest positive cycle containing a fully-curved transition root cannot be Hamiltonian on the ambient coordinate set: that one edge already requires two ambient coordinates outside its cycle support.

### Scope

The chord conclusion is unconditional for the enlarged class of actual fully-curved transition roots. When applying it to a narrower provenance class (for example terminal threshold-band roots with a specified protected side), one must still verify that the endpoint-swapped side root retains the required provenance. The local algebra alone proves full curvature and the physical root direction; it does not by itself preserve a chosen global band certificate.

This isolates a useful target for the mixed-circuit program: prove side-root provenance closure, or enough one-sided provenance closure, for a minimum protected circuit. If that is achieved, every protected full-barrier edge forces two coordinates outside the circuit, and Hamiltonian positive protected circuits disappear immediately.
