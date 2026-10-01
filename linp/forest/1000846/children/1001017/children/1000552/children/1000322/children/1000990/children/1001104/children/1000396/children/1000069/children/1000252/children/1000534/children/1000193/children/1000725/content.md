# In the stalled two-level state every longest path is top-potential except for a constant defect

## Statement

Let L=ell-1 in the stalled state max k<=kappa+3. If u is top-potential with k_u=kappa+h, 0<=h<=3, then every globally longest L-edge path ending at u contains at least 2L-4h-6 top-potential vertices, hence at most 4h+7 low-level vertices. In particular every such path contains at most 19 vertices of potential ell-2.

## Body

Assume the stalled two-level state 2b32ca95800e. Put
  L=ell-1,
  S={phi=L-1},
  T={phi=L}.
Let u∈T and write
  k_u=kappa+h,
where 0<=h<=3 because max k<=kappa+3.

Then
  d_H(u)=3d-k_u
        =(2ell-3+kappa)-(kappa+h)
        =2L-1-h.                                    (1)

Fix any globally longest L-edge path
  P=(g_1,...,g_L)
ending at u.

Let B_P(u) be the number of incident edges f!=g_L whose two non-u vertices both lie on V(P)\g_L. By the certified exact terminal slack db94e08d513d,
  d_H(u)+B_P(u)<=2L-1.
Using (1),
  B_P(u)<=h.                                        (2)

Every incident edge f!=g_L must meet P outside u, otherwise P,f is an (L+1)-edge path. If f is not a double blocker, it therefore has exactly one non-u contact vertex on P. There are
  d_H(u)-1=2L-2-h
nonlast incident edges, so by (2) at least
  2L-2-2h                                          (3)
are one-vertex blockers.

Because distinct edges through u share no second vertex, their blocker vertices are distinct. A blocker vertex that is a path joint can account for at most one such edge. The final joint g_{L-1}∩g_L cannot occur as a blocker, because f and g_L would then share both u and that joint. Hence there are at most L-2 available precursor joints. From (3), at least
  (2L-2-2h)-(L-2)=L-2h                            (4)
one-vertex blockers contact private/free vertices of precursor path edges.

At most two such contacts lie on g_1 and at most one lies on each g_j for 2<=j<=L-1. Therefore the number of distinct path-edge indices carrying a private/free blocker is at least
  L-2h-1.                                          (5)

Discard the possible indices j=L-2,L-1. For every remaining index j<=L-3, choose one private/free blocker edge f_j. It meets P exactly in g_j and g_L. The certified two-contact rotation a51a7f9cff95 gives another globally longest L-edge path whose final edge is g_{j+2}; the two possible last vertices are exactly the two vertices of
  g_{j+2}\g_{j+3}.
Hence both vertices of this two-set have endpoint potential L and belong to T.

For distinct j<=L-3 these two-sets are pairwise disjoint. Therefore P contains at least
  2[(L-2h-1)-2]
   =2L-4h-6                                         (6)
distinct top-potential vertices.

Since |V(P)|=2L+1, the number of low-level vertices from S on P is at most
  (2L+1)-(2L-4h-6)
  =4h+7
  <=19.                                             (7)

Thus every globally longest path ending at a top-layer vertex contains only a constant-size low-potential defect; at charge kappa it contains at most 7 low-level vertices, and even at the maximal stalled charge kappa+3 it contains at most 19.
