# Aligned potential mass earns a second copy of the fixed-entrance coefficient gain

## Statement

Let S_0 be the total endpoint potential on vertices v whose maximum ascending-terminal edge rank equals phi(v). Then every linear r-uniform hypergraph satisfies m <= c_r S - ((2r-1)/(8r(r-1)))S_0 + O_r(n_+), where c_r=1-(2r-1)/(8r(r-1)) is the general fixed-entrance coefficient. Thus any asymptotic extremizer for c_r must have S_0=o(S): almost all potential mass lies at rank-misaligned vertices.

## Body

Let H be a finite linear r-uniform hypergraph, r>=3. For each nonisolated vertex v put p_v=phi(v), and let t(v) count ascending nonspecial edges terminal at v. If t(v)>0 let q(v) be the maximum rank of such an edge; if t(v)=0 put q(v)=0.

Define the aligned set
  V_0={v:t(v)>0 and q(v)=p_v},
and aligned potential mass
  S_0=sum_{v in V_0} p_v.
Let
  S=sum_v p_v.

Choose the global maximum endpoint paths P_v as follows:
- for v in V_0, choose P_v to end in a rank-p_v ascending edge terminal at v;
- for v notin V_0, choose any maximum endpoint path.

Let X_v be excess contact multiplicity on P_v and X=sum_v X_v.

For v in V_0, 3b170b2ae6 gives
  t(v)-X_v <= lambda p_v+O_r(1),
where
  lambda=(2r-3)/4.

For v notin V_0, discard the nonnegative X_v and use the raw fixed-entrance count a570a11f0001:
  t(v)-X_v <= t(v)
            <= alpha p_v+O_r(1),
where
  alpha=(6r-7)/8.

Summing,
  (r-1)A-X
  =sum_v(t(v)-X_v)
  <= alpha S -(alpha-lambda)S_0 + O_r(n_+).         (1)

Now
  alpha-lambda
   =(6r-7)/8-(2r-3)/4
   =(2r-1)/8.                                       (2)

Since X>=0,
  A-X
  <=[(r-1)A-X]/(r-1)
  <= alpha/(r-1) S
    -(2r-1)/(8(r-1)) S_0
    +O_r(n_+).                                      (3)

The arbitrary-r contact identity 6c9c2c5a0fcb gives
  rm <= (r-1)S-(r-2)n_+ +(C-X),
and C<=A. Using (3),
  m <= c_r S
       -(2r-1)/(8r(r-1)) S_0
       +O_r(n_+),                                   (4)
where
  c_r=1-(2r-1)/(8r(r-1))
is the general fixed-entrance leading coefficient.

Thus every unit of aligned potential mass earns the same coefficient decrement
  (2r-1)/(8r(r-1))
a second time.

In particular, for a sequence with S tending to infinity relative to n_+ and
  m = c_r S-o(S),
equation (4) forces
  S_0=o(S).
Hence any asymptotic extremizer for the fixed-entrance coefficient must place asymptotically all potential mass on rank-misaligned vertices q(v)<phi(v).
