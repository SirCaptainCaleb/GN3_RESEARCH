# A shared-entrance packet forces the lower-half edge ranks upward

## Statement

Retain the X-branch of f84b001e0a61. Thus
  e_i={x_i,v,u_i}, i=1,...,k,
have edge ranks
  q_1<=...<=q_k,
put h=floor(k/2), and there are indices a,b>h and a set
  I subset {1,...,h}
of size M such that every x_i, i in I, belongs to both canonical source paths R_a,R_b.

Fix one host index a. If q_h<q_a, then
  M <= 4q_h-2q_a-1.
Equivalently,
  q_h >= ceil((2q_a+M+1)/4).

In particular, since q_a>=q_{h+1}, any strict median rank jump q_h<q_{h+1} satisfies
  M <= 4q_h-2q_{h+1}-1.
Thus a linear shared-entrance packet is incompatible with a large rank gap between the lower half of the family and its higher host paths.

## Body

For every i in I,
  phi(x_i)=q_i-1 <= q_h-1.
The source path R_a has
  L=q_a-1
edges. Under q_h<q_a, put
  R=q_h-1<L.
All M distinct vertices x_i lie on R_a and have vertex rank at most R.

Apply 5cee9bfe483f:
  M <= 4R-2L+1
     =4(q_h-1)-2(q_a-1)+1
     =4q_h-2q_a-1.
Rearranging gives
  4q_h >= 2q_a+M+1,
hence
  q_h >= ceil((2q_a+M+1)/4).

Finally q_a>=q_{h+1}, so replacing q_a by q_{h+1} gives the displayed median-jump inequality.
