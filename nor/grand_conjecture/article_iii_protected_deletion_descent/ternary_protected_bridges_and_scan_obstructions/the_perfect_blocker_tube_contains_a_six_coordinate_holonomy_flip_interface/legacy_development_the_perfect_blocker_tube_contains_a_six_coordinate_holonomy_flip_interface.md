# The perfect-blocker tube contains a six-coordinate holonomy-flip interface — preserved pre-item development


Continue with a globally minimum-first-phase deletion carrier
O=(v_1,...,v_m),  w=0^p1^q,  p,q>=4,
and omitted perfect blocker x with scan
s_i=alpha(x,v_i,v_{i+1})=1^(p+1)0^q.

For each i=1,...,p-1 consider the five-coordinate order
P_i=(v_i,x,v_{i+1},v_{i+2},v_{i+3}).

Its consecutive ternary statuses are
alpha(v_i,x,v_{i+1})=0,
alpha(x,v_{i+1},v_{i+2})=1,
alpha(v_{i+1},v_{i+2},v_{i+3})=0.
The first equality is alternation from s_i=1, the second is s_{i+1}=1, and the third is the old zero-phase status w_{i+1}=0.

Moreover the two transition tetrahedra are
Q_i={x,v_i,v_{i+1},v_{i+2}}
and
Q_{i+1}={x,v_{i+1},v_{i+2},v_{i+3}},
both fully curved by the perfect-blocker full-curvature tube. Hence P_i is a double-full singleton packet.

Let h_i be its residual holonomy bit. The double-full identities give the equivalent expressions
h_i
= alpha(v_i,x,v_{i+3})
= alpha(v_i,v_{i+1},v_{i+3})
= alpha(v_i,v_{i+2},v_{i+3}).

At the left endpoint, the blocker-derived double-full theorem proves
h_1=1.

At the other end of this chain,
h_{p-1}=alpha(v_{p-1},x,v_{p+2}).
This is exactly the residual bit t of the canonical middle insertion packet
(v_{p-1},v_p,v_{p+1},x,v_{p+2}).
The preceding subsection proves, from minimum first-phase extremality, that t=0. Therefore
h_{p-1}=0.

Since the binary sequence h_1,...,h_{p-1} starts at 1 and ends at 0, there exists j in {1,...,p-2} with
h_j=1,
h_{j+1}=0.

Thus every minimum flat-sector counterexample contains a six-coordinate protected interface
(v_j,x,v_{j+1},v_{j+2},v_{j+3},v_{j+4})
consisting of two overlapping double-full singleton packets with opposite residual holonomy. The packets share the fully-curved tetrahedron
{x,v_{j+1},v_{j+2},v_{j+3}},
and all four relevant blocker scan bits are 1 while the three consecutive old carrier windows are 0.

Writing
a=v_j, b=v_{j+1}, c=v_{j+2}, d=v_{j+3}, e=v_{j+4},
the forced old-coordinate triangle data include
abc=bcd=cde=0,
abd=acd=1
(from h_j=1),
and
bce=bde=0
(from h_{j+1}=0).
Coboundary flatness leaves only one further old five-set bit among abe,ace,ade, with
ace=abe,
ade=1-abe.

A useful internal consequence, independent of that last bit, is that
(a,d,b,c,e)
is 0-monochromatic:
alpha(a,d,b)=0,
alpha(d,b,c)=0,
alpha(b,c,e)=0.
The first equality is alternation from abd=1; the second is cyclic invariance from bcd=0; the third is bce=0.

This does not yet close the boundary reconnection, because the new first and last ordered pairs differ from the old ones. But it is a sharper finite target than an arbitrary full barrier: the remaining flat obstruction must contain an actual 1-to-0 holonomy interface, and its five old coordinates already admit a target-color internal weave independent of the final residual bit.

Closure target: use the surrounding perfect-blocker scan and the known old carrier windows to reconnect the weave (a,d,b,c,e), or extract a strictly improved deletion witness from one of its two changed boundary pairs. The immediate right exterior window is still in the old zero phase unless j=p-2, in which case it is exactly the old phase-transition window; endpoint cases should therefore retain that distinction explicitly. The unconstrained four-bit independence theorem does not apply without these holonomy-flip provenance relations.
