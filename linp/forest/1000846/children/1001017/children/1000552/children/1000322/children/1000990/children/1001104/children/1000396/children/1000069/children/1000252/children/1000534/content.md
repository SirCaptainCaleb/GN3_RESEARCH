# Either charge amplifies by four or all negative charge is trapped one level below the top

## Statement

In an exact-density P_ell-free equality obstruction, either max_v k_v>=kappa+4, or every negative-charge vertex has endpoint potential exactly ell-2. In the exceptional case, each negative vertex v with k_v=-r sources at least kappa+r+2 rank-(ell-1) ascending edges whose terminal pairs lie in the top layer T={phi=ell-1}; these form a strong-rainbow properly colored matching graph on T, and every u in T has positive charge k_u>=kappa.

## Body


Retain the exact-density charge setting and write
  kappa=3d-2ell+3.

By 37c98d3f2a7d, max k>=kappa+2. We sharpen this unless all negative charge lies at the top-minus-one potential level.

Let v have negative charge k_v<0 and put p=phi(v). As in 37c98d3f2a7d, v cannot have global maximum endpoint potential, so p<=ell-2. If in fact
  p<=ell-3,
then for a maximum p-edge path ending at v, the opposite endpoint z satisfies
  d_H(z)<=2p-1<=2ell-7.
Hence
  k_z=3d-d_H(z)
      >=3d-2ell+7
      =kappa+4.
Thus if max k<kappa+4, every negative-charge vertex must satisfy
  phi(v)=ell-2.                                     (1)

Assume this exceptional state. Let
  N={v:k_v<0},
  T={u:phi(u)=ell-1}.
Since N is nonempty and every v∈N has phi(v)=ell-2, the global maximum path length is ell-1, so T is nonempty.

For v∈N, write k_v=-r. The local source inequality gives at least
  c(v)>=kappa+r+2
ascending nonspecial edges sourced at v. Because phi(v)=ell-2, every such edge has rank ell-1. Its two terminals have endpoint potential at least ell-1, and P_ell-freeness gives at most ell-1, so both terminals lie in T.

Therefore the exceptional state carries a canonical properly edge-colored graph G on T:
- each v∈N is a color;
- each rank-(ell-1) ascending edge {v,x,y} sourced at v gives graph edge xy of color v;
- each color class is a matching of size at least kappa+(-k_v)+2;
- the coloring is proper by linearity;
- every rainbow path in G lifts to a linear hypergraph path, since the colors N lie at potential ell-2 and hence are disjoint from T.

Finally, every u∈T has phi(u)=ell-1=L. A globally longest path ending at u gives
  d_H(u)<=2ell-3,
hence
  k_u>=3d-(2ell-3)=kappa.                           (2)

Thus failure of the kappa+4 amplification forces a two-layer charge normal form:
all negative charge lies in N=L_{ell-2}, all its ascending source flow goes through a strong-rainbow matching graph on the top layer T=L_{ell-1}, and every top-layer vertex carries positive charge at least kappa.
