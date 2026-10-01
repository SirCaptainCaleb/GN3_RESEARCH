# Prescribed-separation deletion covers have linear incompatibility density

## Statement

Let (H;s,t) be a minimum-order counterexample to prescribed separation, let D=V(H)-{s,t}, and put m=|D|. For each x in D choose one two-cover F_x of H-x separating s and t. Form the compatibility graph G on D, joining x,y when F_x,F_y are compatible on V(H)-{x,y}. Then G is K_4-free. Consequently e(G)<=floor(m^2/3), and some chosen deletion cover F_x is incompatible with at least ceil((m-3)/3) of the other chosen covers.

## Body

By minimum order, for every x in D the smaller tournament H-x has a two-cover separating the surviving prescribed pair s,t, so the family {F_x:x in D} exists.

Suppose four labels x_1,x_2,x_3,x_4 formed a K_4 in G. The corresponding four deletion covers are pairwise compatible. The four-cover compatibility gluing theorem for q=2 therefore produces a two-cover of H whose restriction to each H-x_i has the same pair states as F_{x_i}. In every F_{x_i}, the vertices s and t lie in different components. Hence the global two-cover also places s and t in different components, contradicting that (H;s,t) is a prescribed-separation counterexample. Therefore G is K_4-free.

By Turán's theorem for K_4-free graphs,
[
e(G)le leftlfloor rac{m^2}{3}ightfloor.
]
The incompatibility graph is the complement of G on the same m vertices, so its average degree is
[
m-1-rac{2e(G)}m
ge
m-1-rac{2lfloor m^2/3floor}{m}.
]
Hence some vertex has incompatibility degree at least
[
leftlceil m-1-rac{2lfloor m^2/3floor}{m}ightceil
=
leftlceilrac{m-3}{3}ightceil.
]
Thus one separating deletion state disagrees with a linear number of the others.

This argument uses no compatibility-triangle localization, so it remains valid independently of the current audit defect in compattriangle01.