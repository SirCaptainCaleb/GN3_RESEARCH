# Three isolated endpoint neighbors force a four-unit triangle deficit

## Statement

In the isolated-neighbor branch of c6b15d82c380, let k=deg_G(d) and let t(d) be the number of compatibility triangles containing the anchor d. Then t(d)<=max{0,k-4}.

## Body

Triangles containing d are in bijection with edges of the induced neighborhood graph G[N_G(d)], so t(d)=e(G[N_G(d)]). By 689b439cc429, G[N_G(d)] is a linear forest. In the branch under consideration it has at least three isolated vertices, namely the three isolated compatible endpoint labels supplied by c6b15d82c380. If k<=3 then t(d)=0. If k>=4, any forest on k vertices with at least three isolated vertices has at least four connected components unless all vertices are isolated; hence it has at most k-4 edges. Therefore t(d)<=max{0,k-4}.
