# Second companion weave forces the immediate residual scan pair to be 00 — preserved pre-item development


Assume the recurrent flat A2 replacement configuration with residual coordinates x,y,z and common suffix C,D,E,F,... . Fix u=z and use the other two residuals x,y.

The recurrent identities give a second local ordering

(A,B,x,y,D,C,z)

whose five consecutive local ternary statuses are all 0.

Append E,F and write

a = alpha(z,D,E),
b = alpha(z,E,F).

Using flatness on the four-set {z,C,D,E} together with alpha(z,C,D)=1 and the old suffix status alpha(C,D,E)=1 gives

alpha(C,z,E)=1-a.

Hence the next two statuses after the all-zero local block are

1-a, b,

after which the untouched suffix returns to color 1.

If (a,b) is 01, 10, or 11, the resulting full order has at most one color change. Therefore in a counterexample the only surviving possibility is

(a,b)=(0,0).

By cyclic symmetry of the three residual coordinates, the same conclusion holds for each u in {x,y,z}:

alpha(u,D,E)=alpha(u,E,F)=0.

Thus the recurrent A2 obstruction forces the first two residual scan bits after the common boundary to be 00 for all three residual vertices.

This is strictly stronger than merely forbidding an immediate 01 rise at that boundary. It is still only a local boundary statement; no global monotonicity of the entire residual scan is claimed.
