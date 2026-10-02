# Same-end extenders do not automatically concatenate

## Statement

There is a boundary tournament on four vertices {a,b,r_1,r_2} such that R=(r_1,r_2) is a tight path, both (a,r_1,r_2) and (b,r_1,r_2) are tight, but neither (a,b,r_1) nor (b,a,r_1) is tight. Hence boundary antisymmetry alone does not allow two common left extenders of a tight path to be ordered so that both can be prepended. Any argument using such a concatenation requires additional structure.

## Body

Take the edge-orderable boundary tournament induced by the strict order on ordinary edges

a r_1 < b r_1 < a b < r_1 r_2 < a r_2 < b r_2.

By definition, (x,y,z) is tight exactly when xy<yz. Since a r_1<r_1 r_2 and b r_1<r_1 r_2, both (a,r_1,r_2) and (b,r_1,r_2) are tight, so a and b both left-extend R=(r_1,r_2). On the other hand, (a,b,r_1) would require ab<b r_1, while (b,a,r_1) would require ab<a r_1. Both inequalities fail because a r_1<b r_1<ab. Thus neither ordering of a,b can simply be prepended to R. In particular, the inference that boundary antisymmetry lets one interchange a,b so that (a,b,r_1) is tight is invalid: (a,b,r_1) and (b,a,r_1) are not a reversal pair because they have different middle vertices.