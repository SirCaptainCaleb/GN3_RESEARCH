# Near equality has a periodic four-cell contact normal form

## Statement

Use the fixed-entrance setup of eb40ddcc33ca, q>=4. Let s,d,u be the numbers of singleton contact sets, double contact sets, and unused vertices on W=V(P) minus h, and put
alpha=ceil((3q-8)/4),
M=floor((11q-5)/8).
If
|J_q(v)|=M-r,
then
(alpha-s)+u = 2r+(alpha mod 2).
In particular
s>=alpha-2r-1
and
u<=2r+1.

Moreover, in the four-state representation of eb40ddcc33ca, all but at most 8r+18 interior state transitions are the critical cycle transitions
00->01, 01->11, 11->10, 10->00
with their full weights 2,1,0,0. Hence, after deleting O(r+1) exceptional cells and O(1) boundary cells, the singleton contact pattern is a union of intervals with the period-four normal form
0,0,2,1,0,0,2,1,...
up to cyclic phase.

Thus exact or near equality simultaneously forces almost maximum singleton density, almost no unused vertices, linear double-contact mass, and an essentially periodic contact geometry.

## Body

The contact identity is
s+2d+u=2q-2
and
|J_q(v)|=1+s+d=q+(s-u)/2.
The exact transfer theorem gives
M=q+floor(alpha/2).
Therefore
2r=2(M-|J_q(v)|)
=2floor(alpha/2)-s+u
=alpha-(alpha mod 2)-s+u.
Rearranging gives
(alpha-s)+u=2r+(alpha mod 2),
and the first assertions follow.

For the periodic statement use the state sigma_i=(A_{i-1},A_i) from eb40ddcc33ca. For ordinary two-vertex cells the maximal transition weights are
00->00:0, 00->01:2,
01->10:0, 01->11:1,
10->00:0, 10->01:1,
11->10:0.
With potentials
pi(00)=0, pi(01)=-5/4, pi(10)=-3/4, pi(11)=-3/2,
every actual transition of weight w satisfies
w<=3/4+pi(sigma)-pi(tau).
Equality is possible exactly on
00->01 of weight 2,
01->11 of weight 1,
11->10 of weight 0,
10->00 of weight 0.
Every other allowed transition, or any underfilled equality-type transition, has slack at least 1/4.

The exact identity above shows that total singleton loss from alpha is at most 2r+1. Removing the first cell and final endpoint loses at most two more singleton units. Over the remaining L-1 transitions, L=q-3, telescoping the potential inequality adds boundary potential error at most 3/2. Hence the total transition slack is at most 2r+18/4. Since each noncritical transition contributes at least 1/4, there are at most 8r+18 noncritical transitions.

Between noncritical transitions the state walk is forced to follow the unique equality cycle
00->01->11->10->00,
whose successive singleton weights are 2,1,0,0. Rephasing gives the stated 0,0,2,1 periodic normal form.