# Equality forces a high-degree low-potential ascending source

## Statement

Every exact-density P_ell-free equality obstruction contains a vertex v with d_H(v)>=3d+1 and phi(v)<=ell-2, where d=floor(2ell/3). Consequently v is the entrance of at least 3d-2ell+6 ascending nonspecial edges: at least 6, 4, or 5 in residues ell=0,1,2 mod3 respectively. Their terminal pairs are disjoint, giving at least twice as many distinct higher-potential outneighbors.

## Body

Let H be an exact-density P_ell-free linear triple system,
  |E(H)|=dn,  d=floor(2ell/3),
and write n=6d+1+s with leave graph U.

The leave has average degree s and every leave degree has parity
  d_U(v)≡n-1≡s (mod 2).

If U were s-regular, then
  d_H(v)=(6d+s-s)/2=3d
for every vertex. The minimum-degree endpoint-potential floor would then give a P_ell, since
  ceil((3d+1)/2)>=ell.
Thus U is not regular.

Because all d_U(v) have the same parity as s, nonregularity plus average s implies that some vertex v has
  d_U(v)<=s-2.
Therefore
  d_H(v)=(6d+s-d_U(v))/2 >=3d+1.                    (1)

Let L be the global maximum path length. Since H is P_ell-free,
  L<=ell-1.
If phi(v)=L, then there is a globally longest path ending at v. The certified longest-path terminal degree inequality db94e08d513d gives
  d_H(v)<=2L-1<=2ell-3.
But 3d+1>2ell-3 in every residue class, contradiction. Hence
  phi(v)<=L-1<=ell-2.                                (2)

Let c(v) be the number of ascending nonspecial edges whose unique entrance is v. By the certified local source inequality 22362096041e,
  d_H(v)-c(v)<=2phi(v)-1.
Using (1),(2),
  c(v)>=3d+1-[2(ell-2)-1]
      =3d-2ell+6.                                    (3)

Thus:
- ell=3r, d=2r: c(v)>=6;
- ell=3r+1, d=2r: c(v)>=4;
- ell=3r+2, d=2r+1: c(v)>=5.

Moreover the terminal pairs of these c(v) source edges are pairwise disjoint by linearity, so v has at least 2c(v) distinct higher-potential outneighbors in the ascending orientation.

Hence every exact-density P_ell-free equality obstruction contains a vertex of degree at least 3d+1, endpoint potential at most ell-2, and ascending source multiplicity at least 6,4,5 by residue.
