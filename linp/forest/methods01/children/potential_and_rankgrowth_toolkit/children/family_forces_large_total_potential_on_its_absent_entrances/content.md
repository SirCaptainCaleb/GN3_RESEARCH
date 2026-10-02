# A long terminal-only singleton family forces large total potential on its absent entrances

## Statement

Let P be a maximum p-edge path ending at v, and let e_1,...,e_k be terminal-only singleton ascending edges through v ordered by their contact positions on P. Let x_i be the absent unique entrance of e_i. Then
sum_{i=1}^k phi(x_i) >= [k(p+3)-2p-10]/2.
In particular, for k=Omega(p), the distinct off-path entrances carry Omega(kp) total endpoint potential.

## Body

Write r_i=phi(e_i)=phi(x_i)+1. By 2bee7f7c5680, r_i+r_{i+2}>=p+5 for i=1,...,k-2. Summing gives
2 sum_i r_i -(r_1+r_2+r_{k-1}+r_k) >= (k-2)(p+5).
Discarding the nonnegative boundary term yields
sum_i r_i >= (k-2)(p+5)/2.
Therefore
sum_i phi(x_i)=sum_i(r_i-1)
>= (k-2)(p+5)/2-k
= [k(p+3)-2p-10]/2.
The entrance vertices x_i are distinct because distinct edges through v can share no second vertex by linearity.