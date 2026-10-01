# A long entrance-side replacement region pushes cycle-neighbor gates outside the common-path interval

## Statement

Retain residual case (4) of d0a41dede20a for a selected strict-gap edge
  e={x,v,u}
of edge rank r. Let R_e be its canonical maximum source path, of length r-1, and let A be the selected common-path precursor at terminal v.

Assume e lies in alternative (B) of bbaf9e0b90fc: there is a common vertex z of R_e and A such that the two segments
  R_e[z,x] and A[z,x]
are internally vertex-disjoint and have the same length ell.

Let f be either fundamental-cycle neighbor of e, and let R_f be a canonical maximum source path for f. In residual case (4),
  V(R_f) intersect V(R_e)={s}
is a unique aligned joint whose index t on R_e satisfies
  t>=ceil((r-1)/2).

If
  ell>floor((r-1)/2),
then at least one of the following holds:
(1) |V(R_f) intersect V(A)|>=2;
(2) V(R_f) intersect V(A)={w} and w does not lie in the open A-segment A(z,x).

Consequently, if both fundamental-cycle neighbors meet A uniquely, then for a long entrance-side replacement region both of their unique A-gates lie outside A(z,x).

## Body

Put n=r-1=|R_e|. The segment R_e[z,x] is a terminal segment of R_e ending at its last vertex x and has ell edges.

We first show that the aligned gate s lies in the interior of R_e[z,x]. If z is the joint between source-path edges j and j+1, then
  ell=n-j.
The inequality ell>floor(n/2) gives
  j<ceil(n/2)<=t,
so the joint s at index t occurs strictly after z and before x.

If z is private to source-path edge j, then
  ell=n-j+1.
The same inequality gives
  j<=ceil(n/2)<=t.
Thus the joint s, lying between edges t and t+1, again occurs strictly after z and before x. Therefore in all cases s belongs to the open R_e-segment R_e(z,x).

Now apply 6118d601301a. If R_f and A have at least two common vertices, outcome (1) holds. Otherwise their unique common vertex w is an aligned joint. The two segments R_e[z,x] and A[z,x] form the explicit clean equal-length replacement region supplied by bbaf9e0b90fc. Since s lies in the interior of its R_e-side, 6118d601301a forbids w from lying in the interior of its A-side. Hence
  w notin A(z,x),
which is outcome (2).

Apply the same argument independently to both fundamental-cycle neighbors of e for the final assertion.
