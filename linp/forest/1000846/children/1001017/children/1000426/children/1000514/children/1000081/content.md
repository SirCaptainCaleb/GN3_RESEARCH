# Three-colored K3,3 family refutes the special-edge nullity conjecture

## Statement

The special-edge nullity conjecture 7305b7ec9d2a is false. In the certified family c3e95f4ce77d, all m=9t edges are ascending nonspecial and there are n=6t+3 vertices, while rank_R(N)=5t+2. Hence s=0 but nullity_R(N)=m-rank_R(N)=4t-2>0. Equivalently b=9t>6t+3=n for t>=2, contradicting the consequence b<=rank(N)<=n that nullity(N)<=s would imply.

## Body

In c3e95f4ce77d the hypergraph H_t has
  m=9t,
  n=6t+3,
and every edge is ascending nonspecial. Hence the number s of special edges is zero and b=m=9t.

The same certified object computes
  rank_R(N)=5t+2.
Therefore
  nullity_R(N)=m-rank_R(N)
               =9t-(5t+2)
               =4t-2>0
for every t>=2.

Thus nullity_R(N)<=s would read 4t-2<=0, impossible.

There is also a rank-free contradiction to the main intended consequence of the conjecture. If nullity(N)<=s, then
  rank(N)=m-nullity(N)>=m-s=b.
Since rank(N)<=n, this would imply b<=n. But here
  b=9t>6t+3=n
for t>=2.

Thus 7305b7ec9d2a is decisively refuted by an already certified family. The surviving rank route must use path-length/density hypotheses or a more nuanced structural parameter; special-edge count alone cannot control incidence nullity.
