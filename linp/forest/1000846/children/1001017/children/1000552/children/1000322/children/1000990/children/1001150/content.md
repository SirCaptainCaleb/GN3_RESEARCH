# Threshold-cover plus sharp deletion kills the strict Turan layer for ell at least six

## Statement

Let ell>=6, d=floor(2ell/3), and H be P_ell-free with |E(H)|>=d|V(H)|+1. Suppose H has the equality-layer threshold-cover structure for D={v:d(v)=d+1}, and suppose the sharp deletion step gives m_2+2m_3<=|D|-1. Then H cannot contain a nonspecial edge. Equivalently, under the simultaneous equality-layer/Turan induction, every strict counterexample is eliminated for ell>=6; the remaining substantive obstruction is the equality layer |E(H)|=d|V(H)|.

## Body


Let ell>=6 and put
  d=floor(2ell/3),  k=d+1.
Suppose H is a P_ell-free linear 3-graph satisfying the simultaneous strict-layer hypotheses:
(1) m=|E(H)|>=d|V(H)|+1;
(2) H contains a nonspecial edge with a witness path P;
(3) for D={v:d_H(v)=k}, every edge outside P meets D;
(4) writing m_i for the number of edges containing exactly i vertices of D, one has
    m_2+2m_3<=|D|-1.
Condition (4) is exactly the conclusion supplied by 76745a69ec91 once H-D is known to satisfy the sharp d|X| bound.

Put X=V(H)\D and D_0=|D|.

STEP 1: many one-D edges.
Degree summation over D gives
  kD_0=m_1+2m_2+3m_3.
Let R=m_2+2m_3<=D_0-1. Then
  2m_2+3m_3=2R-m_3<=2D_0-2.
Hence
  m_1>=kD_0-(2D_0-2)
      =(d-1)D_0+2.                                    (A)

STEP 2: the strict edge count forces D_0 large relative to X.
Every edge avoiding D belongs to P, so
  m_0=|E(H-D)|<=ell-1.
The number of edges meeting D is at most the total D-degree kD_0. Therefore
  m<=ell-1+kD_0.
Combining with m>=d(D_0+|X|)+1 and k=d+1 gives
  d|X|<=D_0+ell-2,
or
  D_0>=d|X|-ell+2.                                     (B)

Substitute (B) into (A):
  m_1 >= d(d-1)|X|-(d-1)(ell-2)+2.                    (C)

STEP 3: X is not small.
Each m_1 edge contains one vertex of D and two vertices of X. By linearity, no pair (d,x) with d∈D,x∈X occurs in two edges. Hence
  2m_1<=D_0|X|.
Together with (A),
  D_0|X|>=2(d-1)D_0+4,
so, since D_0>0,
  |X|>2d-2.
Thus
  |X|>=2d-1.                                           (D)

STEP 4: rainbow contradiction.
Form the simple graph G on X whose edges are the m_1 hyperedges, coloring xy by the unique d∈D for which {d,x,y}∈E(H). Linearity makes G simple and properly edge-colored.

Every rainbow graph path in G lifts to a linear hypergraph path in H: consecutive lifted hyperedges meet at the shared X-vertex, nonconsecutive graph edges are vertex-disjoint along a simple graph path, and distinct colors give distinct D-vertices disjoint from X. Since H is P_ell-free, G has no rainbow P_ell.

By the certified Ergemlidze--Gyori--Methuku bound e4fb292edb26,
  m_1 < ((9ell+5)/7)|X|.                               (E)

For d=floor(2ell/3), one has
  (9ell+5)/7 <= 2d+2.
Indeed, checking ell modulo three:
ell=3r gives 27r+5<=28r+14;
ell=3r+1 gives 27r+14<=28r+14;
ell=3r+2 gives 27r+23<=28r+28.

For d>=5, (C),(D),(E) would imply
  (d^2-3d-2)(2d-1)
    < (d-1)(ell-2)-2.
But ell<3(d+1)/2, while direct algebra for d>=5 gives
  (d^2-3d-2)(2d-1) > (3/2)(d-1)(d+1)
                         > (d-1)(ell-2)-2,
a contradiction.

It remains only d=4, corresponding to ell=6 or 7.
For ell=6, (E) has coefficient 59/7, so from (C),(D)
  (12-59/7)|X| >= (25/7)*7=25,
whereas the constant loss is only
  3(6-2)-2=10.
For ell=7, the coefficient is 68/7 and
  (12-68/7)|X| >= (16/7)*7=16
while
  3(7-2)-2=13.
Again contradiction.

Therefore no H satisfying (1)--(4) exists for any ell>=6.

Consequently, in a simultaneous induction proving the sharp Turan bound and the equality-layer assertion S_ell, the strict layer m>=d n+1 is automatic for ell>=6 once the equality layer supplies the threshold-cover conclusion and the smaller graph H-D satisfies the sharp Turan bound. The substantive remaining obstruction is the equality layer m=d n (plus the already-small base lengths).
