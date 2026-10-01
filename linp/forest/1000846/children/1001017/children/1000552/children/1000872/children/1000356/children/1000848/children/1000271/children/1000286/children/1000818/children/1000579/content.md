# Unique intersections remain aligned joints when maximum rail lengths differ by one

## Statement

Let Q be a maximum p-edge path ending at x and R a maximum (p+1)-edge path ending at y. If Q and R have exactly one common vertex w, then w is a joint on both paths at the same index: w=e_i∩e_{i+1}=f_i∩f_{i+1} for some i. Thus the aligned-joint rigidity of equal-length maximum rails extends exactly to the mixed consecutive-length case needed for two-rank 0-1-1 blocks.

## Body


Let
  Q=(e_1,...,e_p),   R=(f_1,...,f_{p+1})
be maximum endpoint paths ending physically at x,y, with
  phi(x)=p,  phi(y)=p+1.
Assume
  V(Q) cap V(R)={w}.

Let i be the first edge index of Q containing w and ell the last; thus ell is i if w is private on Q and i+1 if w is a joint.
Let k be the first edge index of R containing w and j the last; similarly j is k or k+1.

First splice the Q-prefix through its first occurrence of w to the R-suffix from the last occurrence of w:
  e_1,...,e_i, f_j,f_{j+1},...,f_{p+1}.
The unique-intersection hypothesis makes this linear and it ends physically at y. Its length is
  i + (p+1-j+1)=i+p-j+2.
Maximality at y gives
  i+p-j+2 <= p+1,
hence
  j>=i+1.                                            (1)

Conversely splice the R-prefix through its first occurrence of w to the Q-suffix from the last occurrence:
  f_1,...,f_k, e_ell,e_{ell+1},...,e_p.
This is linear and ends at x, with length
  k+(p-ell+1).
Maximality at x gives
  k+p-ell+1<=p,
hence
  ell>=k+1.                                          (2)

If w were private on Q, ell=i. Then (2) gives k<=i-1, hence
  j<=k+1<=i,
contradicting (1). Thus w is a Q-joint and ell=i+1.

If w were private on R, j=k. Then (1) gives k>=i+1 while (2) gives k<=i, contradiction. Thus w is an R-joint and j=k+1.

Now (1) gives k>=i and (2), with ell=i+1, gives k<=i. Therefore
  k=i.

Hence
  w=e_i cap e_{i+1}=f_i cap f_{i+1}.
So a unique intersection of two maximum endpoint paths whose lengths differ by one is an aligned same-index joint, exactly as in the equal-length case.
