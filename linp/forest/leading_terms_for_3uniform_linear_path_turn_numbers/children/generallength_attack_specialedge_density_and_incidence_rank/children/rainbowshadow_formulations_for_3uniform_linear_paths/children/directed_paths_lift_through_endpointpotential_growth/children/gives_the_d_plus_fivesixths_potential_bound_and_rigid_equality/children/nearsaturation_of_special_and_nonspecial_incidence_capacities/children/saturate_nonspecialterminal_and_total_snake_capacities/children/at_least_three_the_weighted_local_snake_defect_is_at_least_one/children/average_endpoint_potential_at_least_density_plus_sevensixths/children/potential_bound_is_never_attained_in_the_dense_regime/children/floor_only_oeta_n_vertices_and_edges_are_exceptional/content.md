# Near the density-plus-seven-sixths floor, only O(eta n) vertices and edges are exceptional

## Statement

Let H be a finite linear 3-graph with phi(v)>=3 for every vertex. Write
  S=sum_v phi(v)=m+(7/6)n+eta n,
with eta>=0. For each vertex put
  delta_ns(v)=(2phi(v)-3)-t_ns(v),
  b(v)=(2phi(v)-1)-d_D^-(v),
and call v Type A when (delta_ns(v),b(v))=(2,0).

Then:
(1) the number of non-Type-A vertices is at most 6 eta n;
(2) B:=sum_v b(v) <= 6 eta n;
(3) the number N_na of nonascending nonspecial edges is at most B, hence N_na<=6 eta n.

Thus if eta=o(1), all but o(n) vertices are Type A and all but o(n) nonspecial edges are ascending.

## Body

By e503661c0fab and the definition of eta,
  (1/2)A+B
   = 3[(S/n)-(m/n)-5/6]n
   = 3(1/3+eta)n
   = n+3eta n,
where A=sum_v delta_ns(v), B=sum_v b(v).

By 9fe13355ecae, every vertex has local weighted defect
  w(v):=(1/2)delta_ns(v)+b(v)>=1.
By 45050da20aaa the only integer pair attaining w(v)=1 is Type A=(2,0), because Type B=(0,1) is impossible. Every non-Type-A vertex therefore has w(v)>=3/2. Since
  sum_v(w(v)-1)=3eta n,
the number of non-Type-A vertices is at most
  2*3eta n=6eta n.

For B, Type-A vertices contribute b=0. At a non-Type-A vertex, the forbidden patterns imply delta_ns(v)+b(v)>=2 whenever b(v)>0. Hence
  b(v) <= delta_ns(v)+2b(v)-2 = 2(w(v)-1).
(The inequality is trivial when b=0.) Summing gives
  B<=2 sum_v(w(v)-1)=6eta n.

Now count special edges. At v the number s_v of incident special edges is
  s_v=d_D^-(v)-t_ns(v)
     =[2phi(v)-1-b(v)]-[2phi(v)-3-delta_ns(v)]
     =2+delta_ns(v)-b(v).
Therefore
  3s=2n+A-B.

Ascending accounting gives
  3m-A_up <= 2S-n,
so
  A_up >= 3m-2S+n
       = m-(4/3)n-2eta n.

The total number of nonspecial edges is
  m-s = m-(2n+A-B)/3.
Thus the number N_na=(m-s)-A_up of nonascending nonspecial edges satisfies
  N_na
  <= m-(2n+A-B)/3 - [m-(4/3)n-2eta n]
  = (2n-A+B)/3+2eta n.

From (1/2)A+B=n+3eta n we have
  A+2B=2n+6eta n,
so
  2n-A+B+6eta n =3B.
Hence the preceding upper bound is exactly
  N_na<=B.

Combining with B<=6eta n yields N_na<=6eta n.