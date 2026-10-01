# Near equality in the fixed-entrance bound forces five-eighths double-contact mass

## Statement

In the setup of eb40ddcc33ca, let d_h(v) be the number of edges f in J_q(v) minus {h} whose contact set C_f on the chosen q-edge h-path has size two. Then for q>=4,
|J_q(v)|-d_h(v) <= ceil((3q-4)/4).

Consequently, if
|J_q(v)| >= floor((11q-5)/8)-r
for some r>=0, then
d_h(v) >= floor(5q/8)-r.
In particular equality in the exact local incident-rank bound forces at least floor(5q/8) double contacts.

## Body

Use the notation of eb40ddcc33ca. Let s be the number of singleton contact sets. The exact conflict transfer gives
s<=ceil((3q-8)/4).
Since
|J_q(v)|=1+s+d_h(v),
we obtain
|J_q(v)|-d_h(v)=1+s
<=1+ceil((3q-8)/4)
=ceil((3q-4)/4).

Now suppose
|J_q(v)|>=M_q-r,
where M_q=floor((11q-5)/8). Then
d_h(v)>=M_q-r-ceil((3q-4)/4).
A residue check modulo 8, or the elementary floor-ceiling identity
floor((11q-5)/8)-ceil((3q-4)/4)=floor(5q/8),
gives
d_h(v)>=floor(5q/8)-r.

Thus the configurations that make the fixed-entrance count large are necessarily rich in double contacts. The four-state extremal singleton pattern does not evade contact multiplicity; it forces approximately five double-contact edges for every eight units of rank.
