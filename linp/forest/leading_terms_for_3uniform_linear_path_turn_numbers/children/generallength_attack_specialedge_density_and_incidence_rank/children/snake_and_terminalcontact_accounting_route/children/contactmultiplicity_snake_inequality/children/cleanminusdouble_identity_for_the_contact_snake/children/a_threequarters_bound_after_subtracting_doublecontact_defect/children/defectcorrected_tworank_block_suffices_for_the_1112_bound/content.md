# A clean-only defect-corrected two-rank block suffices for the 11/12 bound

## Statement

Choose maximum endpoint paths P_x. Count only ascending nonspecial edges whose unique source incidence is genuinely clean, mu_x(e)=0, and assign each such edge to a minimum-potential terminal v. If for every v,q the number of assigned clean edges of ranks q,q+1 that are not double on P_v is at most three, then C-D<=3/4 sum_v phi(v). Hence 3m-C+D<=2 sum phi-n gives m<=11/12 sum phi-n/3, and m<=((11ell-15)/12)n in every P_ell-free system.

## Body


For each nonisolated vertex x choose a maximum endpoint path P_x as in c312c26b7c1d. Call an ascending nonspecial edge e clean at its source x if x is its unique entrance and
  mu_x(e)=0
relative to P_x.

By 4e165e65be58, every clean incidence is of this form and each edge has at most one clean incidence. Let C be the total number of clean incidences.

Assign every clean edge e to one of its two terminal vertices v of minimum endpoint potential, breaking ties arbitrarily. Let
  c(v)
be the number of clean edges assigned to v. Then
  C=sum_v c(v).

Fix v, put p=phi(v), and for each rank r let
  n_r^cl(v)=number of assigned clean edges of rank r,
  d_r^cl(v)=number of those edges having mu_v(e)=2
on the chosen terminal path P_v.

Because assignment is to a minimum-potential terminal, every assigned edge is potential-charged at v. Hence its rank lies in the certified window
  ceil((p+2)/2) <= r <= p.

Let D_v be the total number of double-contact incidences at v over all incident edges, not merely assigned clean edges. Then
  c(v)-D_v
  <= sum_r [n_r^cl(v)-d_r^cl(v)],                    (1)
because D_v contains every assigned-clean double and possibly additional doubles.

Assume the CLEAN defect-corrected consecutive-rank block:
for every v and every q,
  [n_q^cl(v)-d_q^cl(v)]
  +[n_{q+1}^cl(v)-d_{q+1}^cl(v)]
  <=3.                                               (2)

Pair the admissible rank levels exactly as in a9d95378e855. The same certified bottom-level bounds yield
  sum_r [n_r^cl-d_r^cl]
  <= floor(3p/4)
  <=3p/4.
Together with (1),
  c(v)-D_v<=3phi(v)/4.

Summing over v gives
  C-D <= (3/4)S,
where S=sum_v phi(v) and D=sum_v D_v.

Now use the exact clean-minus-double contact identity
  3m-C+D <= 2S-n.
Then
  3m <= 2S-n +(C-D)
      <= (11/4)S-n,
so
  m <= (11/12)S-n/3.
For P_ell-free H, S<=(ell-1)n and hence
  m <= ((11ell-15)/12)n.

Thus the 11/12 coefficient does not require controlling all ascending edges. It suffices to control, in each two-rank block, only those ascending edges whose SOURCE incidence is genuinely clean and whose assigned terminal incidence remains single after double-contact credit.
