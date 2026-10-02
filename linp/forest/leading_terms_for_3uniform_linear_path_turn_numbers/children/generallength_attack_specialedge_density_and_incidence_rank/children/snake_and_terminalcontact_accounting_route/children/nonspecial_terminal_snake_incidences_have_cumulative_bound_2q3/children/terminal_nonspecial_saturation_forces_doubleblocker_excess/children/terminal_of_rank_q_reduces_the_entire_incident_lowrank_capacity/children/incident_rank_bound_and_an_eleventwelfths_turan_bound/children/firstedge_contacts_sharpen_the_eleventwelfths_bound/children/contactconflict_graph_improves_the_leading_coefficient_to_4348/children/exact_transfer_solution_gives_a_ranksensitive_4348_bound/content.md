# Exact transfer solution gives a rank-sensitive 43/48 bound

## Statement

Let H be a finite linear 3-graph. If h is an ascending edge of rank q and v is terminal at h, then
|{f in E(H): v in f and phi(f)<=q}| <= floor((11q-5)/8)
for q>=4; for q=2,3 the sharper bounds are 1 and 2.

Consequently, if t(v) counts ascending edges at which v is terminal and p=phi(v), then
t(v)<=gamma(p),
where gamma(1)=0, gamma(2)=1, gamma(3)=2, and gamma(p)=floor((11p-5)/8) for p>=4.

Let S=sum_v phi(v), let n_+ be the number of nonisolated vertices, let rho(p) be the least nonnegative residue of 3p-5 modulo 8, put R=sum_v rho(phi(v)), and let N_2,N_3 count vertices of ranks 2,3. If A is the number of ascending edges and m=|E(H)|, then
A <= (11S-5n_+-R-8N_2-8N_3)/16
and
m <= (43S-21n_+-R-8N_2-8N_3)/48.
In particular every P_ell^(3)-free linear 3-graph satisfies
m <= ((43ell-64)/48)n.

## Body

Fix h,v,q and a q-edge path P=(g_1,...,g_q) ending in h=g_q at v. Let x=g_{q-1} intersect h; ascendingness gives phi(x)=q-1. Put W=V(P) minus h. For every f!=h through v with phi(f)<=q let C_f=(f minus {v}) intersect W. These contact sets are nonempty, pairwise disjoint, and have size one or two.

Write z_i=g_i intersect g_{i+1}; write g_1={a_1,b_1,z_1}; and for 2<=i<=q-1 let b_i be the private vertex of g_i. The four vertices a_1,b_1,b_{q-2},z_{q-2} cannot themselves be singleton contact sets, by the first-edge and last-edge wrong-entrance splices.

For 1<=i<=q-3, every singleton contact in the forward part of g_i conflicts with every singleton contact in the backward part of g_{i+2}: if f and k have singleton contacts c and d in those two parts, then
g_1,...,g_i,f,k,g_{i+2},...,g_{q-1}
is a q-edge linear path ending at x, contradicting phi(x)=q-1. After the four forbidden vertices are deleted, the potential singleton positions are
C_1={z_1},
C_i={b_i,z_i} for 2<=i<=L:=q-3,
and the endpoint r=b_{q-1}.
If A_i is the indicator that C_i contains at least one singleton contact, then
A_i=1 implies z_{i+1} is not singleton and b_{i+2} is not singleton,
whenever those vertices exist; also A_L=1 forbids r.

We solve this finite transfer exactly. For i>=1 let F_i(u,v) be the maximum number of singleton vertices selected in C_1,...,C_i subject to (A_{i-1},A_i)=(u,v), with A_0=0. The initial values are
F_1(0,0)=0, F_1(0,1)=1.
For i>=1 the transitions are
00->00 with increment 0, 00->01 with increment 2,
01->10 with increment 0, 01->11 with increment 1,
10->00 with increment 0, 10->01 with increment 1,
11->10 with increment 0.
Indeed, in C_{i+1}, the vertex b_{i+1} is available exactly when A_{i-1}=0 and z_{i+1} is available exactly when A_i=0; if at least one is available, selecting all available vertices is optimal for a transition with A_{i+1}=1.

Four successive applications of this recurrence add exactly 3 to every finite state value once i>=2. The four residue classes are obtained from
F_2=(0,2,1,2),
F_3=(1,2,2,3),
F_4=(2,3,3,3),
F_5=(3,4,3,4),
in the state order 00,01,10,11. Finally r contributes one exactly when A_L=0. Therefore the exact maximum number s of singleton contact sets is
s <= alpha_L := ceil((3L+1)/4)
              = ceil((3q-8)/4).
The same formula directly covers q=4, where L=1 and the endpoint conflict is {z_1,b_3}.

Let d be the number of double contact sets and u the number of unused vertices of W. Then
s+2d+u=2q-2
and
|J_q(v)|=1+s+d.
For fixed s, d<=floor((2q-2-s)/2), whence
|J_q(v)|<=q+floor(s/2)
          <=q+floor(ceil((3q-8)/4)/2)
          =floor((11q-5)/8).
This proves the local statement; q=2,3 follow from the standard small fixed-entrance arguments.

For a nonisolated vertex v with t(v)>0, choose a maximum-rank ascending edge terminal at v. Its rank q is at most p=phi(v), so monotonicity of the local bound gives t(v)<=gamma(p). Every ascending edge has exactly two terminals, hence
2A=sum_v t(v)<=sum_v gamma(phi(v)).
For p>=1,
gamma(p)=floor((11p-5)/8)-1_{p=2}-1_{p=3}.
Writing rho(p) for the residue of 3p-5 modulo 8 gives
sum_v gamma(phi(v))
=(11S-5n_+-R)/8-N_2-N_3.
This is the asserted bound on A. Combining it with the certified ascending-incidence inequality
3m-A<=2S-n_+
gives
m <= (43S-21n_+-R-8N_2-8N_3)/48.
Finally S<=(ell-1)n_+ in a P_ell-free system, and the nonnegative correction terms may be discarded, yielding
m<=((43ell-64)/48)n_+<=((43ell-64)/48)n.

Thus the full conflict mechanism is a four-state path transfer, not merely a matching. Its asymptotic extremal cycle is the state cycle 00->01->11->10->00, of total singleton weight 3 in four cells; this is the source of the coefficient 43/48.