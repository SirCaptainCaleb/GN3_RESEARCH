# Unpaid near-saturation forces linear anchor-to-maximum symmetric difference in every uniformity

## Statement

Let H be a finite linear r-graph with r>=3. Let h be an ascending nonspecial edge of rank q>=4, let v be terminal at h, and let
  Q=(g_1,...,g_q=h)
be a longest h-path with last vertex v. Put
  R=V(Q)\h,
so |R|=(r-1)(q-1).

Let p=phi(v)>q, let P be a maximum p-edge path ending at v, and put
  U=V(P)\last(P),
so |U|=(r-1)(p-1).

Let T be a family of t distinct edges through v, containing h, such that every f in T has phi(f)<=q and every f in T\{h} has exactly one off-v contact with U. For f in T\{h}, put
  C_Q(f)=(f\{v}) intersect R,
and let
  D_Q(T)=#{f in T\{h}: |C_Q(f)|>=2}.

Write s_r(q)=alpha_r(q-3), where alpha_r is the exact singleton-contact bound from dcf886f98a51. Then
  D_Q(T) >= t-1-s_r(q),
and
  |R\U| >= D_Q(T),
  |U\R| >= D_Q(T)+(r-1)(p-q).

Consequently, if
  J_max(q)=1+floor(((r-1)(q-1)+s_r(q))/2)
and t>=J_max(q)-tau, then
  D_Q(T)
  >= floor(((r-1)(q-1)-s_r(q))/2)-tau
  = ((2r-1)/8)q-O_r(1)-tau.
Thus any near-saturated terminal-single family forces linear two-sided symmetric difference between the rank-q anchor precursor and every chosen maximum p-path.

In particular, the conclusion applies to a family of globally unpaid signature-(0,1,...,1) ascending edges from 6c9c2c5a0fcb, after restricting to one terminal v and a maximum-rank anchor h with q<phi(v).

For r=3, every anchor-multiple edge is an anchor-double edge and its unique P-contact lies among the same two off-v vertices, so one obtains the stronger crossing matching of the existing gap-one theory. For r>3 that edgewise matching need not exist, but the symmetric-difference conclusion survives unchanged.

## Body

For every f in T\{h}, the set C_Q(f) is nonempty: otherwise Q,f would be a (q+1)-edge linear path, contradicting phi(f)<=q. Since distinct members of T share v, linearity makes the sets C_Q(f) pairwise disjoint.

By the exact fixed-entrance transfer dcf886f98a51, among all rank-at-most-q edges through v at most s_r(q) have singleton contact on R. Therefore at most s_r(q) members of T\{h} have |C_Q(f)|=1, and hence
  D_Q(T)>=t-1-s_r(q).

Fix f counted by D_Q(T). By hypothesis f has exactly one off-v contact with U; call it c_f. If c_f is not in C_Q(f), then every vertex of C_Q(f) lies in R\U. If c_f is in C_Q(f), then all vertices of C_Q(f) except c_f lie in R\U. Since |C_Q(f)|>=2, in either case C_Q(f) contains at least one vertex of R\U.

The sets C_Q(f) are pairwise disjoint, so these omitted anchor vertices may be chosen distinctly for all f counted by D_Q(T). Thus
  |R\U|>=D_Q(T).

Finally,
  |U\R|-|R\U|=|U|-|R|=(r-1)(p-q),
which gives
  |U\R|>=D_Q(T)+(r-1)(p-q).

If t>=J_max(q)-tau, then
  D_Q(T)
  >=J_max(q)-tau-1-s_r(q)
  =floor(((r-1)(q-1)-s_r(q))/2)-tau.
Since s_r(q)=((2r-3)/4)q+O_r(1), the final asymptotic form follows.

For a globally unpaid signature-(0,1,...,1) edge, every terminal incidence has contact multiplicity one on the globally chosen maximum endpoint path. Hence the terminal-single hypothesis above is automatic at the assigned center whenever q<phi(v).
