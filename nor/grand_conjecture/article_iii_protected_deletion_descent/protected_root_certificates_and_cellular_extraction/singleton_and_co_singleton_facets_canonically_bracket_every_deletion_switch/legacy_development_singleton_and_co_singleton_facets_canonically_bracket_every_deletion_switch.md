# Singleton and co-singleton facets canonically bracket every deletion switch — preserved pre-item development

## Development

## Singleton and co-singleton facets canonically bracket every deletion switch

Assume a minimum counterexample. For each coordinate \(x\), fix a good deletion order
\[
O_x=g(V\setminus\{x\})=(a_1,\ldots,a_{n-1}).
\]
Since prepending or appending \(x\) gives a full order, both resulting orders are bad.

Normalize the deletion word as
\[
0^p1^q,\qquad p,q\ge1,
\]
after a global color convention. Its unique switch is between the consecutive windows
\[
(a_p,a_{p+1},a_{p+2})
\quad\text{and}\quad
(a_{p+1},a_{p+2},a_{p+3}).
\]
Define
\[
\ell(x)=a_p,\qquad r(x)=a_{p+3}.
\]

### Singleton facet

The canonical singleton-facet order
\[
x\,O_x
\]
has first change at rank \(1\) and its last change is the inherited deletion switch. Hence its outermost root is
\[
\boxed{x\to r(x).}
\]

### Co-singleton facet

The canonical co-singleton order
\[
O_x\,x
\]
has its first change at the inherited deletion switch and, because the final singleton block must contain the target of the outermost root, its last change is at the final possible rank. Hence its outermost root is
\[
\boxed{\ell(x)\to x.}
\]

### Switch triangle

The unique switch of \(O_x\) itself has physical slide root
\[
\ell(x)\to r(x).
\]
Therefore the three physical roots satisfy the exact type-A relation
\[
(e_{\ell(x)}-e_x)+(e_x-e_{r(x)})
=
e_{\ell(x)}-e_{r(x)}.
\]

Thus every canonical good deletion order carries a realized switch triangle
\[
\boxed{\ell(x)\to x\to r(x),\qquad \ell(x)\to r(x).}
\]

The two edges through \(x\) are outermost roots of canonical singleton/co-singleton facet witnesses; the long edge is the actual consecutive-window slide across the unique switch of the good deletion order.

### Consequence

The endpoint insertion problem can be organized around these switch triangles rather than arbitrary root cycles. The two bad endpoint insertions of \(x\) bracket the unique good-deletion switch from opposite sides, and their outermost roots factor the switch root exactly. Any witness-preserving shortcut that replaces the two endpoint edges by the switch edge, or conversely lifts the switch edge through \(x\), has a built-in physical root identity.
