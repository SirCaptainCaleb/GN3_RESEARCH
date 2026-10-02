# Single-contact central windows give a two-envelope local bound in every uniformity

## Statement


Let H be a finite linear r-graph, r>=3. Fix a nonisolated vertex v of rank p and a maximum p-edge path
  P=(g_1,...,g_p)
with last vertex v and last edge h=g_p. For an incident edge e!=h put
  mu_v(e)=|(e\{v}) intersect (V(P)\h)|.

Let e be an ascending nonspecial edge of rank s<p at which v is terminal, and suppose mu_v(e)=1. Let c be its unique contact with V(P)\h, and let a and b be the first and last indices of path edges containing c. Then
  a<=s-1,
  b>=p-s+2.
If c is a terminal vertex of e rather than its unique entrance, then in fact a<=s-2.

Consequently, for q<p, if s_q(v;P) is the number of ascending nonspecial edges terminal at v, of edge rank at most q, and having mu_v(e)=1, then
  s_q(v;P)
  <= B_r(p,q)
  := max{0,(r-1)(2q-p)-(2r-3)}.

Now let t(v)>0 count all ascending nonspecial edges terminal at v, let q=q(v)<p be their maximum edge rank, and let
  X_v=sum_{f contains v} max(mu_v(f)-1,0),
with mu_v(h)=1 as in the general contact-multiplicity inequality. Then
  t(v)-X_v
  <= min{
       ((6r-7)/8)q+(7-2r)/4,
       B_r(p,q)
     }.

Thus the two leading-order envelopes cross at
  q/p = 8(r-1)/(10r-9).
More exactly, whenever B_r(p,q)>0 the central-window envelope is no larger than the fixed-entrance envelope if
  q <= [8(r-1)p+2(6r-5)]/(10r-9).
For r=3, B_3(p,q)=max{0,4q-2p-3}, recovering the existing 3-uniform single-contact window.


## Body


Write x for the unique entrance of e. Since s<p, the edge e is not the last edge h. Because e and h both contain v and H is linear, no vertex of e\{v} lies in h. The hypothesis mu_v(e)=1 therefore says that c is the only vertex of e\{v} lying anywhere on P.

For the left bound, first suppose c=x. By definition of a, the prefix g_1,...,g_a is a linear path with last vertex x. Hence
  a<=phi(x)=s-1,
because e is ascending.

Suppose instead that c is one of the terminal vertices of e. Then x and every other vertex of e\{v,c} are absent from P. Hence
  g_1,...,g_a,e
is a linear path of length a+1 ending in e, and it enters e through the terminal vertex c. If a+1>s this exceeds the edge rank s. If a+1=s it is a longest path ending in the nonspecial edge e with entrance label c, contradicting that x is the unique entrance. Therefore a+1<=s-1 and a<=s-2.

For the right bound, suppose b<=p-s+1. Then the final s-1 path edges
  g_{p-s+2},...,g_p
avoid c. They also avoid every other vertex of e except v, because c is the unique contact outside h and e cap h={v}. Appending e gives an s-edge linear path ending in e with entrance label v. But v is terminal at e and x is its unique entrance, again a contradiction. Thus b>=p-s+2.

Now fix q<p. Every contact c belonging to an edge counted by s_q(v;P) has first occurrence at most q-1 and last occurrence at least p-q+2. A vertex of P outside h is either private in one path edge or is a joint of two consecutive path edges. Since q<p, the eligible private positions are the internal edges
  g_i,  p-q+2<=i<=q-1,
and the eligible joints are
  g_i cap g_{i+1},  p-q+1<=i<=q-1.
There are
  max(0,2q-p-2)
eligible internal edge positions, each with r-2 private vertices, and
  max(0,2q-p-1)
eligible joints. Their total is exactly
  max{0,(r-1)(2q-p)-(2r-3)}.
Distinct edges through v have disjoint off-v vertex sets by linearity, so their unique contacts are distinct. This proves the bound for s_q(v;P).

For the two-envelope inequality, let T(v) be the t(v) ascending nonspecial edges terminal at v. Every e in T(v) has edge rank at most q<p, so e!=h. Also mu_v(e) cannot be zero: otherwise P,e would be a (p+1)-edge linear path, contradicting phi(e)<=q<p. Hence every e in T(v) has mu_v(e)>=1.

Let X_v^T be the excess multiplicity contributed only by T(v). Then
  t(v)-X_v
  <= t(v)-X_v^T
  = sum_{e in T(v)} [1-max(mu_v(e)-1,0)]
  <= #{e in T(v): mu_v(e)=1}
  <= B_r(p,q).
On the other hand, the certified general-r fixed-entrance capacity bound applied at a maximum-rank edge in T(v) gives
  t(v)<=((6r-7)/8)q+(7-2r)/4,
so the same upper bound holds for t(v)-X_v. Taking the minimum gives the claimed two-envelope estimate.

Finally,
  B_r(p,q)-[((6r-7)/8)q+(7-2r)/4]
  = ((10r-9)/8)q-(r-1)p-(6r-5)/4
whenever B_r(p,q)>0, which gives the exact crossover condition and the stated leading-order ratio.
