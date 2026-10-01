# Every three-set occurs as a reachable three-side at order eleven

## Statement

Assume the balanced order-eight theorem astra003balanced8 and the global balanced-surface connectivity 59bfc75bfb10. Then for every three-element subset X of V(H), the universal Astra component contains a spanning 4|4|3 cover whose three-vertex component has support exactly X. Hence the reachable three-side support family is all binom(11,3)=165 triples.

## Body

# Full triple reachability on the order-eleven 4|4|3 surface

Fix an arbitrary three-element subset X⊆V(H). Every three-vertex boundary tournament has a tight Hamilton path, so X itself can serve as a three-vertex path component.

Its complement W=V(H)-X has order eight. By astra003balanced8, W has an exact balanced 4|4 two-cover P|Q. Therefore

X|P|Q

is a spanning 3|4|4 tight-path cover of H.

By 59bfc75bfb10, every spanning 4|4|3 cover belongs to the universal order-eleven Astra component K. Thus this state is reachable in K.

Since X was arbitrary, every one of the binom(11,3)=165 three-subsets occurs as a reachable three-side support. This strengthens the earlier pair/codegree result 71c87221f4e3 from complete pair reachability to complete triple reachability.
