# Canonical endpoint swap reaches the double-full gadget — preserved pre-item development

Let the canonical cyclic endpoint carrier come from deletion word 0^p1^q with p,q>=3, deletion order (v_1,...,v_m), omitted blocker x, and perfect-blocker scan
s_i=alpha(x,v_i,v_{i+1})=1^(p+1)0^q.

Use cyclic order (x,v_1,...,v_m). Its final two wrap statuses are 0,0 and its initial inserted status is 1. Swap the cyclicly adjacent pair v_m,x, giving
(...,v_{m-3},v_{m-2},v_{m-1},x,v_m,v_1,...).

The status
S=alpha(v_{m-2},v_{m-1},x)=s_{m-2}=0.
Its left neighbor is alpha(v_{m-3},v_{m-2},v_{m-1})=1 because q>=3. Its right neighbor is
alpha(v_{m-1},x,v_m)=1-alpha(v_{m-1},v_m,x)=1
by alternation and the old wrap zero. Thus the new order contains a 101 singleton packet.

Both transition tetrahedra are fully curved. On the left,
alpha(v_{m-3},v_{m-2},x)=s_{m-3}=0;
together with consecutive statuses 1,0 the coboundary-flat tetrahedral identity gives the full pattern. On the right,
alpha(v_{m-2},v_{m-1},v_m)=1
from the tail of the q-run; together with consecutive statuses 0,1 the same identity gives the full pattern.

No property of the old 2-to-1 transition tetrahedron was used. Therefore the flat-corner hypothesis in the older endpoint-repair route is unnecessary for reaching the double-full singleton. Every canonical endpoint carrier with p,q>=3 reaches a double-full singleton by this one adjacent swap, and the two proved one-sided monotone resolutions apply unconditionally.

This is a local handoff theorem. One of the two resolutions simply returns toward the original endpoint order; the other exports reconnection risk to the q-side. Global closure still requires termination/extraction of that exported risk.
