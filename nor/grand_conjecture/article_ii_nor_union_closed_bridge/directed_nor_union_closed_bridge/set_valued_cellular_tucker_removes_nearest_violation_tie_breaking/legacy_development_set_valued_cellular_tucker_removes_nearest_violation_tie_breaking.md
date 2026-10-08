# Set valued cellular Tucker removes nearest violation tie breaking — preserved pre-item development

## Set-valued cellular Tucker removes nearest-violation tie breaking

Work in the ternary switch prism
[
X=P_V	imes I.
]
For a bad switch-state vertex z, do not select one violating window. Instead define
[
L(z)subset{pm1,ldots,pm n}
]
to be the set of signed physical middle coordinates of all violating ternary windows:
- +b if the violating window centered at b lies on the pre-switch side;
- -b if it lies on the post-switch side.

A physical coordinate b is the middle of at most one ternary window in a fixed order, so
[
{+b,-b}
otsubset L(z)
]
for every single state z.

Reversal gives exact set-valued antipodality:
[
L(-z)=-L(z).
]

### Theorem

Some genuine product cell C of the switch prism contains state vertices z,z' and a physical coordinate b with
[
+bin L(z),qquad -bin L(z').
]

### Proof

Suppose no product cell has such a complementary pair anywhere among the union of its vertex label sets.

For each state vertex z, send z to the barycenter of the crosspolytope face spanned by
[
{operatorname{sgn}(ell)e_{|ell|}:ellin L(z)}.
]
The label set is nonempty under counterexamplehood and has no complementary pair, so this barycenter lies in the boundary of the n-crosspolytope.

For any product cell C, by assumption the union
[
igcup_{zinmathrm{Vert}(C)}L(z)
]
contains no complementary pair. Hence all images of vertices of C lie in one common crosspolytope face. As in the cellular Tucker theorem, extend the map over C inside that convex face, inductively over cell dimension.

On antipodal boundary cells choose the extensions equivariantly. Because
[
L(-z)=-L(z),
]
the boundary map is antipodal. Thus one obtains an antipodal map
[
S^{n-1}=partial X	o S^{n-1}
]
which extends over the n-ball X, contradicting the odd degree of an antipodal sphere map.

Therefore a complementary product cell exists. QED.

### Extraction advantage

This theorem needs no nearest-violation selection and no tie-breaking rule. Inside the complementary cell, bubble b monotonically from a state where its centered window is a pre-switch violation to a state where its centered window is a post-switch violation.

Along that bubble path:
- if the b-centered violation persists through the cut crossing, subsection 118 gives an actual switch-crossing endpoint repair;
- if it disappears before the crossing and reappears afterward, the first and last toggles are same-side bubble repairs of subsection 143, with the threshold-energy/Radon behavior of subsections 144 and 146.

Thus the topological carrier-to-repair extraction is now set-valued and canonical up to the choice of bubble path inside one Coxeter cell.
