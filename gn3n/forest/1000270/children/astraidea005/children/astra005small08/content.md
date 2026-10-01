# Prescribed vertices are separable by a two-cover through order eight

## Statement

Let H be a boundary tournament on n<=8 vertices, and let s,t be distinct vertices. Then H has a spanning path cover with at most two tight paths such that s and t lie in different components.

## Body

# Separation through order eight

Let H be a boundary tournament on n<=8 vertices, and fix distinct vertices s,t.

For n<=6, partition V(H) into two sets A,B with s in A, t in B, and |A|,|B|<=3. Every set of at most three vertices is the support of a tight path, so A|B is the required two-cover.

Now let n=7. Put U=V(H)-{t}, so |U|=6 and s is in U. By the certified six-vertex small-set theorem, at least four of the six five-vertex subsets of U are Hamiltonian. Only one five-subset of U omits s, namely U-{s}; therefore some Hamiltonian five-set T contained in U contains s. Choose a Hamilton order of T. At least one endpoint is different from s; delete such an endpoint. The remaining four vertices form a Hamilton tight path A containing s. The complement V(H)-A has three vertices and contains t, hence is also the support of a tight path. Thus A together with its complement gives the required separated two-cover.

Finally let n=8. Choose any six-set U contained in V(H)-{t} with s in U. Again at least four five-subsets of U are Hamiltonian, while at most one five-subset omits s. Hence there is a Hamiltonian five-set A contained in U and containing s. Its complement has three vertices, contains t, and is a tight-path support. Thus A together with V(H)-A is the required separated two-cover.

Therefore Astra idea 005 holds for every boundary tournament of order at most eight.
