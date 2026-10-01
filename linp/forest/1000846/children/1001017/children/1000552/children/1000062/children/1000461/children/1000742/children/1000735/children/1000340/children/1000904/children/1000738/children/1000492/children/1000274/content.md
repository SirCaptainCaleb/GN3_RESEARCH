# Top-rank alignment converts Astra double-contact mass directly into multiplicity credit

## Statement

Let q(v) be the maximum rank of an ascending nonspecial edge terminal at v. If q(v)=phi(v)=p, then choosing the global endpoint path P_v to end in such a top-rank ascending edge gives t(v)-X_v <= ((2r-3)/4)p+O_r(1), where X_v is excess contact multiplicity. Consequently, if every vertex supporting ascending terminal edges is top-rank aligned, the global leading coefficient improves to 1-(2r-1)/(4r(r-1)); for r=3 this is 19/24.

## Body

Let H be a finite linear r-uniform hypergraph, r>=3. Fix a nonisolated vertex v and put p=phi(v). Let t(v) be the number of ascending nonspecial edges for which v is terminal.

Assume t(v)>0 and that among those edges there is one h of rank exactly p. Since v is terminal at h and phi(h)=p=phi(v), choose the globally selected maximum endpoint path P_v to be a p-edge path ending in h with last vertex v.

Let X_v be the excess contact multiplicity on P_v:
  X_v=sum_{e contains v} max(mu_v(e)-1,0).

For every ascending edge terminal at v, its rank is at most p, so it belongs to
  J_p(v)={f:v in f, phi(f)<=p}.
Hence
  t(v)<=|J_p(v)|.

Use the fixed-entrance contact decomposition relative to h:
- s singleton contact sets;
- n_j contact sets of size j>=2.
Then
  |J_p(v)|=1+s+sum_{j>=2} n_j.

Meanwhile X_v contains, for these same J_p(v) incidences, at least
  sum_{j>=2}(j-1)n_j.
Therefore
  t(v)-X_v
  <= |J_p(v)|-sum_{j>=2}(j-1)n_j
  = 1+s+sum_{j>=2}(2-j)n_j
  <=1+s.                                             (1)

By the arbitrary-r singleton run count a570a11f0001,
  s <= lambda(p-2)+(r-1),
where
  lambda=(2r-3)/4.
Equivalently,
  s <= lambda p + O_r(1).
Thus
  t(v)-X_v <= ((2r-3)/4)p + O_r(1).                 (2)

This is strictly stronger than the raw fixed-entrance terminal count
  t(v)<=((6r-7)/8)p+O_r(1):
all nonsingleton contacts are paid by excess multiplicity.

GLOBAL CONDITIONAL CONSEQUENCE.
Suppose every vertex with t(v)>0 is top-rank aligned in this sense, so its maximum ascending terminal rank equals phi(v), and choose P_v accordingly. Summing (2),
  (r-1)A - X
  =sum_v t(v)-X
  <= ((2r-3)/4)S + O_r(n_+).                        (3)

Since X>=0,
  A-X
  <= [(r-1)A-X]/(r-1)
  <= (2r-3)/(4(r-1)) S + O_r(n_+).                 (4)

The r-uniform contact identity 6c9c2c5a0fcb gives
  rm <= (r-1)S-(r-2)n_+ +(C-X),
and C<=A, hence
  rm <= (r-1)S +(A-X)+O_r(n_+).

Using (4), the leading S-coefficient is
  [(r-1)+(2r-3)/(4(r-1))]/r
  = [4r^2-6r+1]/[4r(r-1)]
  = 1-(2r-1)/[4r(r-1)].

Thus in the fully top-rank-aligned regime the leading coefficient is twice as far below one as Astra's general bound.
