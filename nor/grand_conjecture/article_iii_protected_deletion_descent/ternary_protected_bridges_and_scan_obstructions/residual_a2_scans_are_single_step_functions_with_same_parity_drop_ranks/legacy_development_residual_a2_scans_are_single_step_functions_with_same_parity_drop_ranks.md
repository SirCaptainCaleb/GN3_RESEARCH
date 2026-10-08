# Residual A2 scans are single-step functions with same-parity drop ranks — preserved pre-item development


Assume the recurrent flat A2 replacement obstruction with residual coordinates U={x,y,z} and common suffix T=(t_1,t_2,...). For u in U write

s_u(j)=alpha(u,t_j,t_{j+1}).

The recurrent packet gives

s_x(1)=s_y(1)=s_z(1)=1,

while counterexamplehood at the rear gives

s_x(last)=s_y(last)=s_z(last)=0.

Use the companion A2 weave result: an immediate 0-to-1 rise in any residual scan produces a spanning threshold-compatible weave. Hence in a surviving counterexample no scan s_u contains the adjacent pattern 01.

Therefore each residual scan is a single step function

s_u = 1...10...0.

Let d_u be its last index carrying the value 1.

Now use the flat pair-holonomy identity from the A2 suffix packet:

s_u(j) xor s_v(j)
=
alpha(u,v,t_j) xor alpha(u,v,t_{j+1}).

Summing over the suffix telescopes. The residual tournament at t_1 is the directed A2 cycle, and the recurrent return gives the same directed cycle at the rear. Hence for every pair u,v,

0
=
xor_j (s_u(j) xor s_v(j)).

For step-function scans, s_u xor s_v is 1 exactly on the interval between their two drop ranks. Therefore

xor_j (s_u(j) xor s_v(j))
=
|d_u-d_v| mod 2.

Thus every pair of drop ranks has even difference:

d_x congruent d_y congruent d_z mod 2.

Equivalently, the recurrent A2 suffix is controlled by three same-parity integer drop positions.

A second formulation uses prefix scan parities

P_u(k)=xor_{j<k} s_u(j).

Then the residual pair tournament at pivot t_k satisfies

alpha(u,v,t_k)
=
alpha(u,v,t_1) xor P_u(k) xor P_v(k).

So the entire tournament evolution is obtained from the initial directed triangle by vertex switching with switch-state (P_x,P_y,P_z), modulo simultaneous complementation. It therefore factors through the Klein four group automatically. The same-parity drop theorem is exactly the condition that this switching state returns to the identity class at the rear.

This reduces the remaining recurrent flat A2 obstruction from three arbitrary binary scans to three same-parity cut positions. The next closure target is to exclude unequal drop positions by a boundary-preserving weave or to show that equal drop positions already yield a spanning one-change construction.
