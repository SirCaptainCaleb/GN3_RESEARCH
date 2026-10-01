# Sharp endpoint threshold strengthens the equality leave spike

## Statement

For an exact-density P_ell-free system with n=6d+1+s and leave U, one has Delta(U)>=6d+s-4ell+6. Thus the leave maximum degree is at least s+6, s+2, or s+4 according as ell is 0,1,2 mod3. At s=2 this means degrees at least 8,4,6.

## Body

Let ell>=4, d=floor(2ell/3), n=6d+1+s, and let U be the leave graph of an exact-density P_ell-free linear triple system H.

For every vertex v,
  d_H(v)=(6d+s-d_U(v))/2.

The certified endpoint-potential floor implies that any linear 3-graph with minimum degree at least 2ell-2 contains P_ell, because
  ceil(((2ell-2)+1)/2)=ell.
Hence P_ell-freeness forces
  delta(H)<=2ell-3.
For a vertex attaining minimum degree,
  (6d+s-d_U(v))/2 <=2ell-3,
so
  d_U(v)>=6d+s-4ell+6.
Therefore
  Delta(U)>=6d+s-4ell+6.                            (1)

Evaluating:
- ell=3r, d=2r: Delta(U)>=s+6;
- ell=3r+1, d=2r: Delta(U)>=s+2;
- ell=3r+2, d=2r+1: Delta(U)>=s+4.

At s=2 this gives leave maximum degree at least 8,4,6 respectively.

In the s=2 defect identity z=sum_{j>=2}(j-1)n_{2j}, a leave vertex of degree 8 contributes three units, while one of degree 6 contributes two. Thus the maximum-degree spike alone forces z>=3 in residue zero and z>=2 in residue two, matching the branch-deletion lower bounds from dbaf1a6e3cd7 by a different mechanism.
