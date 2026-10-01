# Quadratic-maximal relocation plateaux can slide only from larger blocks toward smaller ones

## Statement

Assume an Astra-006 c<=3 relocation component contains no ordering with c<=2. Among all reachable orderings equipped with a partition into three nonempty contiguous tight paths, choose A|B|C maximizing Phi=|A|^2+|B|^2+|C|^2. Let X=(x_1,...,x_p) and Y=(y_1,...,y_q) be any two of the three components, placed adjacently in either order using the free whole-block permutations, and assume p,q>=2. Put T_L=(x_{p-1},x_p,y_1) and T_R=(x_p,y_1,y_2). Then XY is not tight. Moreover: if p=q, both T_L,T_R are non-tight; if p>q, either both are non-tight or T_L is non-tight and T_R tight, so the only available cut slide transfers x_p from the larger block X to the smaller block Y; if p<q, either both are non-tight or T_L is tight and T_R non-tight, so the only available slide transfers y_1 from the larger Y to the smaller X. Hence for every equal-size pair, both join triples are non-tight in each of the two block orders, and each ordered interface yields the corresponding reversed tight four-path.

## Body

# Proof

Consider the finite set of orderings reachable from the starting c=3 ordering by contiguous block relocations while preserving c<=3. By hypothesis none has c<=2.

For every reachable ordering consider every partition of it into three nonempty contiguous tight paths. Choose one displayed state A|B|C maximizing

Phi=|A|^2+|B|^2+|C|^2.

Whole-block relocations can permute A,B,C arbitrarily while preserving c<=3 and preserving Phi. Therefore any ordered pair X,Y of the three components may be placed adjacently without leaving the same reachable relocation component.

Fix such an adjacency X|Y with p=|X|, q=|Y|, p,q>=2. By the certified three-block interface trichotomy a099fe174571, exactly one of three situations occurs:

1. both join triples T_L,T_R are tight, in which case XY is one tight path;
2. exactly one join triple is tight, in which case the cut slides by one vertex while both resulting pieces remain tight;
3. both join triples are non-tight, in which case the reversed four-vertex order (y_2,y_1,x_p,x_{p-1}) is tight.

Case 1 is impossible: XY together with the untouched third component would give a reachable ordering with c<=2.

Suppose case 2 holds. If T_L is tight and T_R is non-tight, the cut slides right, replacing sizes p,q by p+1,q-1. The change in quadratic potential is

Delta Phi=(p+1)^2+(q-1)^2-p^2-q^2=2(p-q)+2.

If p>=q, this is positive, contradicting maximality of Phi. Therefore this slide pattern can occur only when p<q; in that case it transfers one vertex y_1 from the larger Y into the smaller X.

If instead T_L is non-tight and T_R is tight, the cut slides left, replacing p,q by p-1,q+1. Now

Delta Phi=(p-1)^2+(q+1)^2-p^2-q^2=2(q-p)+2.

If q>=p this is positive, again contradicting maximality. Hence this pattern can occur only when p>q; it transfers x_p from the larger X into the smaller Y.

In particular if p=q, either possible one-step slide would increase Phi by 2. So neither single-tight pattern can occur. Since merging is also impossible, both join triples must be non-tight. Boundary antisymmetry then gives the tight reversed four-path from the interface trichotomy.

Finally whole-block permutation freedom lets us apply the same argument after reversing the block order Y|X. Thus for every equal-size pair both join triples are non-tight in both ordered block interfaces, with a reversed tight four-path supplied at each interface.

The result is arbitrary-order: only component sizes and the two local join triples are used.
