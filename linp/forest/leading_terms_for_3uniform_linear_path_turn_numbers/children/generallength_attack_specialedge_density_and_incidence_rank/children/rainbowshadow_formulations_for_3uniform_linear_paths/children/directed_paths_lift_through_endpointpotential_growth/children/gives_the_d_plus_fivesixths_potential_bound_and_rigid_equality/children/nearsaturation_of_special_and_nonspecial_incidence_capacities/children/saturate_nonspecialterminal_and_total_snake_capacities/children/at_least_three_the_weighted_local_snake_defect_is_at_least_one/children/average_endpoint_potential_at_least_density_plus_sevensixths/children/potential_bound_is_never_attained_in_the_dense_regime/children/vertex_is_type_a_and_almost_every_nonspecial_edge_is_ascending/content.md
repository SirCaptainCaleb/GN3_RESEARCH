# Near the seven-sixths floor, almost every vertex is Type A and almost every nonspecial edge is ascending

## Statement

Let H be a finite linear 3-graph with phi(v)>=3 for every vertex, and suppose
  sum_v phi(v)=m+(7/6+eta)n
for eta>=0.

Let R be the set of vertices that are not Type A, i.e. do not satisfy
  a(v)=2, b(v)=0.
Let s be the number of special edges, and let N^- be the number of nonspecial nonascending edges.

Then
  |R|<=6 eta n,
  (4/3-4eta)n <= s <= (4/3+2eta)n,
and
  N^-<=6 eta n.

Moreover every nonspecial nonascending edge has its unique entrance in R.

## Body

Write
  W=sum_v[(1/2)a(v)+b(v)].
By the exact slack identity e503661c0fab and
  average(phi)=m/n+7/6+eta
             =m/n+5/6+(1/3+eta),
we have
  W=n+3eta n.                                         (1)

By 9fe13355ecae every local weighted defect is at least one. The only integer patterns with weighted defect exactly one are (2,0) and (0,1), and 45050da20aaa excludes (0,1). Hence Type A is the unique weight-one state; every vertex in R has weighted defect at least 3/2. Therefore
  W >= (n-|R|)*1 + |R|*(3/2)
    = n + |R|/2.
Together with (1),
  |R|<=6eta n.                                        (2)

Let A0=sum_v a(v), B0=sum_v b(v). From W=n+3eta n,
  A0=2n+6eta n-2B0.
The special-incidence identity gives
  3s=sum_v(2+a(v)-b(v))
     =2n+A0-B0
     =4n+6eta n-3B0,
so
  s=(4/3)n+2eta n-B0.                                 (3)

We claim B0<=6eta n. Since the forbidden local patterns (0,0),(1,0),(0,1) are excluded, every vertex satisfies a(v)+b(v)>=2. Thus
  b(v)<=2([(1/2)a(v)+b(v)]-1).
Summing and using (1) gives
  B0<=2(W-n)=6eta n.
Insert 0<=B0<=6eta n into (3) to obtain
  (4/3-4eta)n <= s <= (4/3+2eta)n.                    (4)

Let A_asc be the number of ascending nonspecial edges. Ascending accounting gives
  3m-A_asc <= 2sum_v phi(v)-n
             =2m+(4/3+2eta)n,
hence
  A_asc >= m-(4/3+2eta)n.                             (5)

The total number of nonspecial edges is m-s. By the lower bound on s from (4),
  m-s <= m-(4/3-4eta)n.
Subtract (5):
  N^-=(m-s)-A_asc <=6eta n.

Finally d059bf8631a0 shows that at every Type-A vertex all nonspecial source edges are ascending. Therefore the unique entrance of every nonascending nonspecial edge lies in R.