# A five-set contains at most two fully curved tetrahedra — preserved pre-item development

## Development


## A five-set contains at most two fully curved tetrahedra

Let alpha be an alternating orientation on triples, and encode it by increasing-order face bits f(ijk).

Recall that on an increasing four-set a<b<c<d, full curvature is equivalent to

f(abc)=f(acd) != f(abd)=f(bcd).

### Theorem
Among the five tetrahedral facets of any five-set, at most two are fully curved.

### Proof
Suppose two facets are fully curved. Relabel the five vertices increasingly as 1<2<3<4<5 so that the two chosen facets are

Q_5={1,2,3,4},
Q_4={1,2,3,5}.

Put a=f(123).

Full curvature of Q_5 gives

f(134)=a,
f(124)=f(234)=1-a.

Full curvature of Q_4 gives

f(135)=a,
f(125)=f(235)=1-a.

Now inspect each of the remaining three facets.

For Q_3={1,2,4,5}, full curvature would require

f(124) != f(125),

because in a fully curved increasing tetrahedron the two faces obtained by deleting the third and fourth vertices lie in opposite classes. But both displayed values equal 1-a. Hence Q_3 is not fully curved.

For Q_2={1,3,4,5}, full curvature would require

f(134) != f(135),

but both equal a. Hence Q_2 is not fully curved.

For Q_1={2,3,4,5}, full curvature would require

f(234) != f(235),

but both equal 1-a. Hence Q_1 is not fully curved.

Thus once two facets of a five-set are fully curved, the other three are not. In particular no five-set contains three fully curved tetrahedra. QED.

### Corollary with coboundary parity

Singly-curved tetrahedra are exactly the support of delta f, so their number among the five facets of a five-set is even.

Therefore, if a five-set contains two fully curved facets, among its remaining three facets the number of singly-curved facets is 0 or 2. In particular at least one of the remaining facets is flat.

### Significance

The fully-curved 4-uniform hypergraph is locally sparse:

every 5-set spans at most two universal switch gadgets.

Hence the irreducible even-curvature obstruction cannot fill a simplex densely. Any attempt to trap a Connector carrier entirely inside fully-curved tetrahedra must repeatedly pass through five-sets containing flat or singly-curved escape facets.

This gives a concrete local sparsity input for the simplex connector program.
