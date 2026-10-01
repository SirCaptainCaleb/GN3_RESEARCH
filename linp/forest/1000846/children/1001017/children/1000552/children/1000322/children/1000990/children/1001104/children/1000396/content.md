# Leave deviations form a zero-sum charge field whose negative mass forces ascending flow

## Statement

For an exact-density system with n=6d+1+s, define k_v=(d_U(v)-s)/2. Then k_v is integral, sum_v k_v=0, and d_H(v)=3d-k_v. If H is P_ell-free, max k_v>=kappa=3d-2ell+3, equal to 3,1,2 by residue. Every vertex with k_v=-r<0 has phi(v)<=ell-2 and sources at least kappa+r+2 ascending nonspecial edges. Thus negative leave charge is quantitatively converted into upward potential flow.

## Body

Fix ell>=4 and d=floor(2ell/3). Let H be an exact-density linear triple system with
  |E(H)|=d n,
write
  n=6d+1+s,
and let U be the uncovered-pair leave graph.

Because
  d_U(v)=n-1-2d_H(v),
every leave degree has parity n-1, which is the parity of s. Define
  k_v=(d_U(v)-s)/2 ∈ Z.

Then
  d_H(v)
   =(6d+s-d_U(v))/2
   =3d-k_v.                                         (1)

Since the average leave degree is s,
  sum_v(d_U(v)-s)=0,
hence
  sum_v k_v=0.                                      (2)

Thus exact density is equivalent to a zero-sum integer deviation field around hypergraph degree 3d.

Assume now H is P_ell-free. The endpoint-potential floor implies delta(H)<=2ell-3. By (1), for a minimum-degree vertex,
  3d-k_v<=2ell-3,
so
  max_v k_v >= kappa:=3d-2ell+3.                   (3)

By residues,
  kappa=3,1,2
for ell congruent to 0,1,2 modulo 3.

Now let k_v=-r<0. Then
  d_H(v)=3d+r.
This exceeds 2ell-3 in every residue class. If phi(v) were the global maximum path length L, a globally longest path ending at v would trigger the terminal degree bound
  d_H(v)<=2L-1<=2ell-3,
contradiction. Therefore
  phi(v)<=ell-2.                                    (4)

Let c(v) count ascending nonspecial edges with unique entrance v. The certified local source inequality gives
  d_H(v)-c(v)<=2phi(v)-1.
Using (1),(4),
  c(v)>=3d+r-[2(ell-2)-1]
      =3d-2ell+5+r
      =kappa+r+2.                                   (5)

Hence every negative charge creates a large ascending fan:
- residue 0: c(v)>=r+5;
- residue 1: c(v)>=r+3;
- residue 2: c(v)>=r+4.

If
  R=sum_{k_v<0}(-k_v)=sum_{k_v>0}k_v
is the total charge mass, then summing (5) over the negative-charge vertices yields
  A >= R +(kappa+2)|{v:k_v<0}|,
where A is the total number of ascending nonspecial edges.

This gives an exact bridge between Steiner leave irregularity and potential flow: positive leave spikes (low H-degree) must be balanced by negative leave charge, and every unit of negative charge appears at a high-degree, below-top-potential source with quantitatively forced upward branching.
