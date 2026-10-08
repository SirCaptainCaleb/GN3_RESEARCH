# The recurrent flat A2 cycle forces the residual triple and forbids scan valleys — preserved pre-item development

## Development

Work in the recurrent flat A2 replacement cycle with residual coordinates U={x,y,z} and common deletion carriers
...A,B,z,y,C,D,... (omit x),
...A,B,y,x,C,D,... (omit z),
...A,B,x,z,C,D,... (omit y),
all with the same one-change word 0^p1^q. The known local identities are alpha(A,B,u)=0 for u in U; alpha(B,x,z)=alpha(B,z,y)=alpha(B,y,x)=1; alpha(x,z,C)=alpha(z,y,C)=alpha(y,x,C)=1; and the common suffix from C,D onward is in the color-1 phase.

First, alpha(x,y,z)=1. If alpha(x,y,z)=0, then in the deletion carrier omitting x, inserting x between B and z gives affected statuses
alpha(A,B,x)=0,
alpha(B,x,z)=1,
alpha(x,z,y)=1-alpha(x,y,z)=1,
alpha(z,y,C)=1,
after which the untouched suffix remains color 1. This would be a spanning one-change order, contradiction.

Second, for each residual coordinate u, take the companion seven-coordinate weave ending in u and delete its final u. The remaining protected front block has word 0,1,1,1 and ends in the original ordered suffix pair (C,D). Now insert u at any later interior gap of the untouched color-1 suffix T=(t_1,t_2,...), where s_u(j)=alpha(u,t_j,t_{j+1}). The three new statuses are
s_u(j-1), 1-s_u(j), s_u(j+1).
Therefore a suffix scan valley 101 would produce insertion packet 111 and hence a spanning one-change order. Thus every residual suffix scan is 101-free.

So the recurrent A2 obstruction has:
(1) forced residual triple orientation alpha(x,y,z)=1;
(2) all three residual scans start at 1, end at 0, and avoid 101.
In particular isolated zero defects in any residual scan are impossible.
