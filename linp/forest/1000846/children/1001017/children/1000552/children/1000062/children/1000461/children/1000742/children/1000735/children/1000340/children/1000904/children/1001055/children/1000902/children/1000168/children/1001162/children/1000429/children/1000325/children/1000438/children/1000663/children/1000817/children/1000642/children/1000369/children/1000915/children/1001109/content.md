# Long balanced lenses have pairwise intersecting auxiliary sides

## Statement

Let P be a globally longest L-edge linear path. Let two genuine clean balanced endpoint lenses on P have host intervals I_1,I_2, each of host-side length greater than (L+1)/2. Then their off-host lens sides have an internal common vertex.

Equivalently: a family of genuine balanced endpoint lenses on one globally longest host path whose host intervals all have length greater than (L+1)/2 has pairwise internally intersecting auxiliary sides.

## Body

Let I_1,I_2 be the two host intervals.

They cannot be disjoint: two disjoint subintervals of the L-edge host path cannot both have length greater than (L+1)/2.

If I_1 and I_2 cross, the conclusion is exactly 67a0061b9889: crossing balanced endpoint lenses on a maximum host path must intersect off the host.

It remains to consider the nested case. Relabel so that I_2 is contained in I_1. The outer interval I_1 has length greater than (L+1)/2. By cd79177973e9, two nested balanced lenses with internally disjoint off-host sides would force the outer host interval to have length at most (L+1)/2. Hence the off-host sides cannot be internally disjoint.

These cases exhaust the relative positions of two host intervals.
